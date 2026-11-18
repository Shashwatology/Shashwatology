#!/usr/bin/env python3
"""
Fetch live repository statistics, stars, forks, and language breakdown for shashwatology
from GitHub's public REST API and write to data/github_stats.json.
"""
import os
import json
import urllib.request

USERNAME = os.environ.get("GH_PROFILE_USER", "shashwatology")
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_STATS = os.path.join(BASE_DIR, "data", "github_stats.json")

def main():
    url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100&sort=updated"
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "ResearchPortfolio/1.0 (mailto:shashwatology.s@gmail.com)"}
    )

    try:
        with urllib.request.urlopen(req, timeout=20) as resp:
            repos = json.loads(resp.read().decode("utf-8"))
        print(f"Total public repos: {len(repos)}")
        total_stars = sum(r.get("stargazers_count", 0) for r in repos)
        total_forks = sum(r.get("forks_count", 0) for r in repos)

        lang_counts = {}
        for r in repos:
            lang = r.get("language")
            if lang:
                lang_counts[lang] = lang_counts.get(lang, 0) + 1

        tot_langs = sum(lang_counts.values()) or 1
        lang_dist = [
            {"name": k, "count": v, "pct": round((v / tot_langs) * 100, 1)}
            for k, v in sorted(lang_counts.items(), key=lambda x: (-x[1], x[0]))
        ]

        top_repos = [
            {
                "name": r.get("name"),
                "desc": r.get("description") or "",
                "stars": r.get("stargazers_count", 0),
                "forks": r.get("forks_count", 0),
                "lang": r.get("language") or "Python",
                "url": r.get("html_url"),
            }
            for r in sorted(repos, key=lambda x: (-x.get("stargazers_count", 0), x.get("name", "")))
        ]

        stats = {
            "username": USERNAME,
            "public_repos": len(repos),
            "total_stars": total_stars,
            "total_forks": total_forks,
            "languages": lang_dist,
            "top_repos": top_repos[:6],
        }

        os.makedirs(os.path.dirname(OUT_STATS), exist_ok=True)
        with open(OUT_STATS, "w", encoding="utf-8") as f:
            json.dump(stats, f, indent=2)
        print(f"Saved {OUT_STATS}: {len(repos)} repos, {total_stars} stars, {total_forks} forks")
    except Exception as e:
        print(f"Warning: could not fetch live repo stats ({e}); keeping existing data if present.")

if __name__ == "__main__":
    main()
