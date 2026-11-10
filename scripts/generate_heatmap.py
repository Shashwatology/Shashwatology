#!/usr/bin/env python3
"""
Generate the electric cobalt blue contribution calendar card (cards/heatmap.svg)
using real GitHub contribution data from data/contributions.json.
"""

import os
import json
import datetime
from svg_utils import make_card_svg, PAPER, INK, MUTED, COBALT, RULE

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
DATA_FILE = os.path.join(ROOT, "data", "contributions.json")
OUT_FILE = os.path.join(ROOT, "cards", "heatmap.svg")

BLUE_LEVELS = [
    "#E2E2DE",  # 0: empty
    "#C8D3FF",  # 1: 1-5
    "#94A8FF",  # 2: 6-15
    "#6280FF",  # 3: 16-30
    "#315EFF",  # 4: 31-50
    "#1A3BE0",  # 5: >50
]

def level_for(count):
    if count == 0:
        return 0
    elif count <= 5:
        return 1
    elif count <= 15:
        return 2
    elif count <= 30:
        return 3
    elif count <= 50:
        return 4
    else:
        return 5

def generate():
    if not os.path.exists(DATA_FILE):
        print(f"Error: {DATA_FILE} not found. Run fetch_github_data.py first.")
        return

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    days = data.get("days", [])
    if not days:
        print("No days in contributions.json")
        return

    w = 880
    first_date = datetime.date.fromisoformat(days[0]["date"])
    lead = (first_date.weekday() + 1) % 7  # 0 = Sunday

    cell_size = 11.5
    step = 14.2
    gx = 42
    gy = 88

    cells = []
    months = []
    seen_months = set()

    for i, d in enumerate(days):
        k = i + lead
        col, row = divmod(k, 7)
        date = datetime.date.fromisoformat(d["date"])
        if date.day <= 7 and (date.year, date.month) not in seen_months and row == 0:
            seen_months.add((date.year, date.month))
            months.append((col, date.strftime("%b")))

        count = d["count"]
        level = level_for(count)
        fill = BLUE_LEVELS[level]
        delay = 0.4 + col * 0.02 + row * 0.015

        x = gx + col * step
        y = gy + row * step

        cells.append(
            f'<rect class="p" style="animation-delay:{delay:.2f}s" '
            f'x="{x:.1f}" y="{y:.1f}" width="{cell_size}" height="{cell_size}" rx="2.5" fill="{fill}">'
            f'<title>{d["date"]}: {count} contribution{"s" if count != 1 else ""}</title>'
            f'</rect>'
        )

    num_cols = (len(days) + lead + 6) // 7
    grid_right = gx + num_cols * step - 2

    month_labels = "".join(
        f'<text x="{gx + c * step:.1f}" y="{gy + 7 * step + 18:.1f}" '
        f'font-family="\'Geist Mono\', monospace" font-size="10" fill="{MUTED}">{m}</text>'
        for c, m in months if c < num_cols - 4
    )

    legend_start_x = grid_right - len(BLUE_LEVELS) * 15
    legend_rects = "".join(
        f'<rect x="{legend_start_x + idx * 15}" y="{gy + 7 * step + 8}" '
        f'width="11" height="11" rx="2" fill="{c}"/>'
        for idx, c in enumerate(BLUE_LEVELS)
    )

    card_h = gy + 7 * step + 44

    body = f"""
  <!-- Card Background -->
  <rect width="{w}" height="{card_h}" rx="12" fill="{PAPER}" stroke="{RULE}" stroke-width="1"/>

  <!-- Card Header -->
  <text class="r" style="animation-delay:0.1s" x="42" y="52" 
        font-family="'Instrument Serif', Georgia, serif" font-size="32" fill="{INK}">
    Every day, <tspan font-style="italic" fill="{COBALT}">in blue</tspan>
  </text>
  <text class="f" style="animation-delay:0.2s" x="{grid_right}" y="48" text-anchor="end" 
        font-family="'Geist Mono', monospace" font-size="11" letter-spacing="1" fill="{MUTED}">
    REFRESHED DAILY // SHASHWATOLOGY
  </text>
  <line x1="42" y1="68" x2="{grid_right}" y2="68" stroke="{RULE}" stroke-width="1"/>

  <!-- Grid Cells -->
  <g>
    {''.join(cells)}
  </g>

  <!-- Legend & Month Footer -->
  <g class="f" style="animation-delay:1.2s">
    {month_labels}
    <text x="{legend_start_x - 8}" y="{gy + 7 * step + 17}" text-anchor="end" 
          font-family="'Geist Mono', monospace" font-size="10" fill="{MUTED}">less</text>
    {legend_rects}
    <text x="{legend_start_x + len(BLUE_LEVELS) * 15 + 6}" y="{gy + 7 * step + 17}" 
          font-family="'Geist Mono', monospace" font-size="10" fill="{MUTED}">more</text>
  </g>
"""

    total_c = data.get("total_contributions", 0)
    svg_out = make_card_svg(
        w, card_h, body,
        font_keys=["serif", "serif-i", "mono"],
        label=f"Shashwat Upadhyay: GitHub Contribution Calendar with {total_c} contributions in the last year"
    )

    os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write(svg_out)
    print(f"Generated {OUT_FILE} ({len(svg_out)} bytes)")

if __name__ == "__main__":
    generate()

