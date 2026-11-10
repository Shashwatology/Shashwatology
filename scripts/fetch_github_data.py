#!/usr/bin/env python3
"""
Fetch real daily contribution counts and user data for shashwatology from GitHub's
public unauthenticated endpoints, and generate data/contributions.json and data/profile.json.
"""
import datetime
import json
import os
import re
import sys
import urllib.request
from bs4 import BeautifulSoup

USERNAME = os.environ.get("GH_PROFILE_USER", "shashwatology")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTRIB_URL = f"https://github.com/users/{USERNAME}/contributions"
OUT_CONTRIB = os.path.join(BASE_DIR, "data", "contributions.json")
OUT_PROFILE = os.path.join(BASE_DIR, "data", "profile.json")

def fetch_contributions():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    req = urllib.request.Request(CONTRIB_URL, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        html_text = resp.read().decode("utf-8")

    soup = BeautifulSoup(html_text, "html.parser")
    cells = soup.select("td.ContributionCalendar-day")
    if not cells:
        print("Warning: No calendar cells found with td.ContributionCalendar-day, attempting fallback", file=sys.stderr)
        # Try table or rect or other elements if github changed markup
        cells = soup.find_all(attrs={"data-date": True})

    days = []
    for td in cells:
        date = td.get("data-date")
        if not date:
            continue
        td_id = td.get("id")
        tooltip_el = soup.find("tool-tip", attrs={"for": td_id}) if td_id else None
        text = tooltip_el.get_text(strip=True) if tooltip_el else ""
        if not text:
            # check aria-label or title
            text = td.get("aria-label") or td.get("title") or ""
        
        if re.search(r"no contributions", text, re.I):
            count = 0
        else:
            m = re.search(r"(\d+)\s+contribution", text, re.I)
            if not m:
                m = re.match(r"^(\d+)", text)
            count = int(m.group(1)) if m else 0

        level = int(td.get("data-level") or 0)
        days.append({"date": date, "count": count, "level": level})

    days.sort(key=lambda d: d["date"])
    return days

def compute_current_streak(days):
    if not days:
        return 0, None, None
    idx = len(days) - 1
    if days[idx]["count"] == 0 and idx > 0:
        idx -= 1  # current day may still be in progress
    streak = 0
    end_idx = idx
    while idx >= 0 and days[idx]["count"] > 0:
        streak += 1
        idx -= 1
    start_idx = idx + 1
    if streak == 0:
        return 0, None, None
    return streak, days[start_idx]["date"], days[end_idx]["date"]

def compute_longest_streak(days):
    longest = run = 0
    longest_start = longest_end = None
    run_start_idx = None
    for i, d in enumerate(days):
        if d["count"] > 0:
            if run == 0:
                run_start_idx = i
            run += 1
            if run > longest:
                longest = run
                longest_start = days[run_start_idx]["date"]
                longest_end = days[i]["date"]
        else:
            run = 0
    return longest, longest_start, longest_end

def build_contributions_data(days):
    if not days:
        return {}
    total = sum(d["count"] for d in days)
    active_days = sum(1 for d in days if d["count"] > 0)
    best = max(days, key=lambda d: d["count"]) if days else {"date": "", "count": 0}
    cur_len, cur_start, cur_end = compute_current_streak(days)
    long_len, long_start, long_end = compute_longest_streak(days)

    monthly = {}
    for d in days:
        key = d["date"][:7]
        monthly[key] = monthly.get(key, 0) + d["count"]
    monthly_list = [{"month": k, "total": v} for k, v in sorted(monthly.items())]

    return {
        "username": USERNAME,
        "generated_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "range": {"start": days[0]["date"], "end": days[-1]["date"]},
        "total_contributions": total,
        "active_days": active_days,
        "avg_per_active_day": round(total / active_days, 1) if active_days else 0,
        "current_streak": {"length": cur_len, "start": cur_start, "end": cur_end},
        "longest_streak": {"length": long_len, "start": long_start, "end": long_end},
        "best_day": {"date": best["date"], "count": best["count"]},
        "monthly": monthly_list,
        "days": days,
    }

def fetch_user_profile():
    url = f"https://api.github.com/users/{USERNAME}"
    headers = {"User-Agent": "Mozilla/5.0"}
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data
    except Exception as e:
        print(f"Error fetching user profile: {e}", file=sys.stderr)
        return {}

def main():
    print(f"Fetching contribution data for {USERNAME}...")
    days = fetch_contributions()
    contrib_data = build_contributions_data(days)
    
    os.makedirs(os.path.dirname(OUT_CONTRIB), exist_ok=True)
    with open(OUT_CONTRIB, "w", encoding="utf-8") as f:
        json.dump(contrib_data, f, indent=2)
    print(f"Saved {OUT_CONTRIB}: {contrib_data.get('total_contributions', 0)} total contributions, "
          f"{contrib_data.get('active_days', 0)} active days, "
          f"current streak {contrib_data.get('current_streak', {}).get('length', 0)}, "
          f"longest streak {contrib_data.get('longest_streak', {}).get('length', 0)}")

    print(f"Fetching user profile for {USERNAME}...")
    profile = fetch_user_profile()
    with open(OUT_PROFILE, "w", encoding="utf-8") as f:
        json.dump(profile, f, indent=2)
    print(f"Saved {OUT_PROFILE}")

if __name__ == "__main__":
    main()

