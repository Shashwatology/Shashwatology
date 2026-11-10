#!/usr/bin/env python3
"""
Generate the monthly activity & streak visualization card (cards/activity.svg)
using real GitHub contribution metrics from data/contributions.json.
"""

import os
import json
import datetime
from svg_utils import make_card_svg, PAPER, INK, INK_SOFT, MUTED, COBALT, RULE

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
DATA_FILE = os.path.join(ROOT, "data", "contributions.json")
OUT_FILE = os.path.join(ROOT, "cards", "activity.svg")

def generate():
    if not os.path.exists(DATA_FILE):
        print(f"Error: {DATA_FILE} not found. Run fetch_github_data.py first.")
        return

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    monthly_raw = data.get("monthly", [])
    if not monthly_raw:
        print("No monthly data available")
        return

    w = 880
    h = 340
    monthly = monthly_raw[-12:]
    
    # Identify highest month
    best_month = max(monthly, key=lambda m: m["total"])
    top_total = max(1, best_month["total"])

    # Bar chart coordinates
    chart_x0, chart_x1 = 44, 580
    base_y = 280
    max_bar_h = 135
    gap = 9
    bar_w = (chart_x1 - chart_x0 - gap * (len(monthly) - 1)) / len(monthly)

    bars_svg = []
    for i, m in enumerate(monthly):
        is_best = (m["total"] == best_month["total"] and m["month"] == best_month["month"])
        # Minimum bar height so months with 0 still show subtle baseline indicator
        bh = max(3, round((m["total"] / top_total) * max_bar_h))
        x = chart_x0 + i * (bar_w + gap)
        y = base_y - bh
        fill = COBALT if is_best else (INK if m["total"] > 0 else "#C9C9C4")
        
        try:
            m_date = datetime.date.fromisoformat(m["month"] + "-01")
            m_label = m_date.strftime("%b")
        except Exception:
            m_label = m["month"][-2:]

        delay = 0.5 + i * 0.05
        bars_svg.append(
            f'<rect class="g" style="animation-delay:{delay:.2f}s" '
            f'x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{bh}" rx="3" fill="{fill}">'
            f'<title>{m_label} {m["month"][:4]}: {m["total"]} contributions</title>'
            f'</rect>'
            f'<text class="f" style="animation-delay:{delay:.2f}s" '
            f'x="{x + bar_w/2:.1f}" y="{base_y + 20}" text-anchor="middle" '
            f'font-family="\'Geist Mono\', monospace" font-size="10.5" fill="{MUTED}">{m_label}</text>'
        )

        if is_best and m["total"] > 0:
            bars_svg.append(
                f'<text class="p" style="animation-delay:1.2s" '
                f'x="{x + bar_w/2:.1f}" y="{y - 8:.1f}" text-anchor="middle" '
                f'font-family="\'Geist Mono\', monospace" font-size="10.5" font-weight="600" fill="{COBALT}">'
                f'{m["total"]}</text>'
            )

    # Right side metrics panel
    cs = data.get("current_streak", {}).get("length", 0)
    ls = data.get("longest_streak", {}).get("length", 0)
    total_active = data.get("active_days", 0)
    total_days = len(data.get("days", [])) or 365
    best_day = data.get("best_day", {})
    best_day_count = best_day.get("count", 0)
    best_day_date = best_day.get("date", "")

    streak_note = "current streak, and the longest" if cs >= ls and cs > 0 else f"current streak, longest {ls} days"
    if cs == 0:
        streak_note = f"longest streak was {ls} days"

    stats_items = [
        (f'{ls} <tspan font-style="italic">days</tspan>', streak_note),
        (f'{total_active}<tspan font-size="22" fill="#8E8E93"> / {total_days}</tspan>', "days with active contributions"),
        (f'{best_day_count} <tspan font-style="italic">commits</tspan>', f"busiest day ({best_day_date})" if best_day_date else "on the busiest day"),
    ]

    side_panel = []
    panel_x = 625
    for idx, (headline, caption) in enumerate(stats_items):
        stat_y = 105 + idx * 80
        delay = 0.8 + idx * 0.12
        side_panel.append(
            f'<g class="r" style="animation-delay:{delay:.2f}s">'
            f'<text x="{panel_x}" y="{stat_y}" font-family="\'Instrument Serif\', Georgia, serif" font-size="34" fill="{INK}">{headline}</text>'
            f'<text x="{panel_x}" y="{stat_y + 22}" font-family="\'Geist\', sans-serif" font-size="12" fill="{MUTED}">{caption}</text>'
            f'</g>'
        )
        if idx < 2:
            side_panel.append(
                f'<line x1="{panel_x}" y1="{stat_y + 38}" x2="{w - 44}" y2="{stat_y + 38}" stroke="{RULE}" stroke-width="1"/>'
            )

    total_c = data.get("total_contributions", 0)

    body = f"""
  <!-- Card Background -->
  <rect width="{w}" height="{h}" rx="12" fill="{PAPER}" stroke="{RULE}" stroke-width="1"/>

  <!-- Left Header -->
  <text class="f" style="animation-delay:0.1s" x="44" y="50" 
        font-family="'Geist Mono', monospace" font-size="11" letter-spacing="1" fill="{MUTED}">
    THE LAST 12 MONTHS ON GITHUB
  </text>
  <text class="r" style="animation-delay:0.2s" x="42" y="96" 
        font-family="'Instrument Serif', Georgia, serif" font-size="44" fill="{INK}">
    {total_c:,} <tspan font-style="italic" fill="{COBALT}">contributions</tspan>
  </text>

  <!-- Left Chart Baseline -->
  <line x1="{chart_x0}" y1="{base_y + 2}" x2="{chart_x1}" y2="{base_y + 2}" stroke="{RULE}" stroke-width="1"/>

  <!-- Monthly Bars -->
  {''.join(bars_svg)}

  <!-- Vertical Divider Between Chart and Stats -->
  <line x1="600" y1="44" x2="600" y2="{h - 36}" stroke="{RULE}" stroke-width="1" stroke-dasharray="3 3"/>

  <!-- Right Metrics Panel -->
  {''.join(side_panel)}
"""

    svg_out = make_card_svg(
        w, h, body,
        font_keys=["serif", "serif-i", "sans", "mono"],
        label=f"Shashwat Upadhyay: Activity in the last 12 months with {total_c} total contributions"
    )

    os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write(svg_out)
    print(f"Generated {OUT_FILE} ({len(svg_out)} bytes)")

if __name__ == "__main__":
    generate()

