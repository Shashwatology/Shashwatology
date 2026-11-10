#!/usr/bin/env python3
"""
Generate a compact, premium blue contribution heatmap card (cards/heatmap.svg)
combining the 53-week GitHub calendar with an integrated telemetry stats strip.
"""

import os
import json
import datetime
from svg_utils import make_card_svg, PAPER, INK, INK_SOFT, MUTED, COBALT, CYAN, RULE

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
        print(f"Error: {DATA_FILE} not found.")
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

    cell_size = 11.2
    step = 14.1
    gx = 40
    gy = 74

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
        delay = 0.2 + col * 0.015 + row * 0.01

        x = gx + col * step
        y = gy + row * step

        cells.append(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{cell_size}" height="{cell_size}" rx="2" fill="{fill}">'
            f'<title>{d["date"]}: {count} contribution{"s" if count != 1 else ""}</title>'
            f'</rect>'
        )

    num_cols = (len(days) + lead + 6) // 7
    grid_right = gx + num_cols * step - 2

    month_labels = "".join(
        f'<text x="{gx + c * step:.1f}" y="{gy + 7 * step + 16:.1f}" '
        f'font-family="\'Geist Mono\', monospace" font-size="9.5" fill="{MUTED}">{m}</text>'
        for c, m in months if c < num_cols - 4
    )

    legend_start_x = grid_right - len(BLUE_LEVELS) * 14
    legend_rects = "".join(
        f'<rect x="{legend_start_x + idx * 14}" y="{gy + 7 * step + 7}" '
        f'width="10" height="10" rx="2" fill="{c}"/>'
        for idx, c in enumerate(BLUE_LEVELS)
    )

    card_h = 240

    total_c = data.get("total_contributions", 0)
    ls = data.get("longest_streak", {}).get("length", 0)
    active_d = data.get("active_days", 0)
    best_c = data.get("best_day", {}).get("count", 0)

    body = f"""
  <!-- Card Background -->
  <rect width="{w}" height="{card_h}" rx="10" fill="{PAPER}" stroke="{RULE}" stroke-width="1"/>

  <!-- Card Header -->
  <g>
    <circle class="live" cx="44" cy="38" r="4" fill="{COBALT}"/>
    <text x="56" y="42" font-family="'Instrument Serif', Georgia, serif" font-size="28" fill="{INK}">
      Every day, <tspan font-style="italic" fill="{COBALT}">in blue</tspan>
    </text>
    <text x="{grid_right}" y="40" text-anchor="end" 
          font-family="'Geist Mono', monospace" font-size="10.5" letter-spacing="0.8" fill="{MUTED}">
      REFRESHED DAILY // SHASHWATOLOGY
    </text>
  </g>
  <line x1="40" y1="56" x2="{grid_right}" y2="56" stroke="{RULE}" stroke-width="0.8"/>

  <!-- Grid Cells -->
  <g>
    {''.join(cells)}
  </g>

  <!-- Legend & Month Footer -->
  <g>
    {month_labels}
    <text x="{legend_start_x - 6}" y="{gy + 7 * step + 15}" text-anchor="end" 
          font-family="'Geist Mono', monospace" font-size="9.5" fill="{MUTED}">less</text>
    {legend_rects}
    <text x="{legend_start_x + len(BLUE_LEVELS) * 14 + 4}" y="{gy + 7 * step + 15}" 
          font-family="'Geist Mono', monospace" font-size="9.5" fill="{MUTED}">more</text>
  </g>

  <!-- Integrated Telemetry Strip at Bottom -->
  <line x1="40" y1="{card_h - 40}" x2="{grid_right}" y2="{card_h - 40}" stroke="{RULE}" stroke-width="0.8"/>
  <g font-family="'Geist Mono', monospace" font-size="11">
    <text x="40" y="{card_h - 18}" fill="{MUTED}">TOTAL: <tspan font-weight="600" fill="{INK}">{total_c:,}</tspan></text>
    <text x="220" y="{card_h - 18}" fill="{MUTED}">LONGEST STREAK: <tspan font-weight="600" fill="{COBALT}">{ls} DAYS</tspan></text>
    <text x="440" y="{card_h - 18}" fill="{MUTED}">ACTIVE DAYS: <tspan font-weight="600" fill="{INK}">{active_d}</tspan></text>
    <text x="{grid_right}" y="{card_h - 18}" text-anchor="end" fill="{MUTED}">PEAK DAY: <tspan font-weight="600" fill="{COBALT}">{best_c} COMMITS</tspan></text>
  </g>
"""

    svg_out = make_card_svg(
        w, card_h, body,
        font_keys=["serif", "serif-i", "mono"],
        label=f"Shashwat Upadhyay: GitHub Contribution Calendar with {total_c} contributions in the last year"
    )

    os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write(svg_out)
    print(f"Generated compact {OUT_FILE} ({len(svg_out)} bytes)")

if __name__ == "__main__":
    generate()
