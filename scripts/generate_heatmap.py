#!/usr/bin/env python3
"""
Generate a compact, premium blue contribution heatmap card (cards/heatmap.svg)
combining the 53-week GitHub calendar with an integrated telemetry stats strip.
Month labels sit cleanly above the grid (GitHub style) so the legend never overlaps.
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
    num_cols = (len(days) + lead + 6) // 7

    # Symmetrical margins: 40px left & 40px right -> usable grid width = 800px
    gx = 40
    usable_w = w - 2 * gx  # 800
    step = usable_w / max(1, num_cols)  # ~15.09px for 53 cols
    cell_size = round(step - 3.0, 1)    # ~12.1px
    gy = 72  # Tight room for month labels at y=64

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

        x = gx + col * step
        y = gy + row * step

        twinkle_attr = f' class="twinkle" style="animation-delay:{(col * 0.13 + row * 0.25) % 3.2:.2f}s"' if level >= 3 else ""
        cells.append(
            f'<rect{twinkle_attr} x="{x:.1f}" y="{y:.1f}" width="{cell_size}" height="{cell_size}" rx="2" fill="{fill}">'
            f'<title>{d["date"]}: {count} contribution{"s" if count != 1 else ""}</title>'
            f'</rect>'
        )

    grid_right = gx + (num_cols - 1) * step + cell_size
    grid_bottom = gy + 7 * step

    # Render all month labels cleanly ABOVE the grid (avoiding trailing label clipping)
    month_labels = "".join(
        f'<text x="{gx + c * step:.1f}" y="{gy - 8:.1f}" '
        f'font-family="\'Geist Mono\', monospace" font-size="9.5" fill="{MUTED}">{m}</text>'
        for c, m in months if c < num_cols - 1
    )

    # Legend cleanly on bottom right, right-aligned to grid_right
    more_w = 30
    swatch_step = 14
    legend_right = grid_right - more_w
    legend_start_x = legend_right - len(BLUE_LEVELS) * swatch_step
    legend_y = grid_bottom + 5

    legend_rects = "".join(
        f'<rect x="{legend_start_x + idx * swatch_step:.1f}" y="{legend_y:.1f}" '
        f'width="10" height="10" rx="2" fill="{c}"/>'
        for idx, c in enumerate(BLUE_LEVELS)
    )

    card_h = 236

    total_c = data.get("total_contributions", 0)
    ls = data.get("longest_streak", {}).get("length", 0)
    active_d = data.get("active_days", 0)
    best_c = data.get("best_day", {}).get("count", 0)

    body = f"""
  <!-- Card Background -->
  <rect width="{w}" height="{card_h}" rx="10" fill="{PAPER}" stroke="{RULE}" stroke-width="1"/>

  <!-- Card Header -->
  <g>
    <circle class="ring" cx="44" cy="31" r="4.5" fill="none" stroke="{COBALT}" stroke-width="1.2"/>
    <circle class="live" cx="44" cy="31" r="4" fill="{COBALT}"/>
    <text x="56" y="36" font-family="'Instrument Serif', Georgia, serif" font-size="26" fill="{INK}">
      Every day, <tspan font-style="italic" fill="{COBALT}">in blue</tspan>
    </text>
    <text x="{grid_right:.1f}" y="34" text-anchor="end" 
          font-family="'Geist Mono', monospace" font-size="10" letter-spacing="0.8" fill="{MUTED}">
      REFRESHED DAILY // SHASHWATOLOGY
    </text>
  </g>
  <line x1="40" y1="47" x2="{grid_right:.1f}" y2="47" stroke="{RULE}" stroke-width="0.8"/>

  <!-- Month Headers Above Grid -->
  <g>
    {month_labels}
  </g>

  <!-- Grid Cells -->
  <g>
    {''.join(cells)}
  </g>

  <!-- Legend Cleanly Below Right -->
  <g>
    <text x="{legend_start_x - 6:.1f}" y="{legend_y + 8.5:.1f}" text-anchor="end" 
          font-family="'Geist Mono', monospace" font-size="9.5" fill="{MUTED}">less</text>
    {legend_rects}
    <text x="{grid_right:.1f}" y="{legend_y + 8.5:.1f}" text-anchor="end"
          font-family="'Geist Mono', monospace" font-size="9.5" fill="{MUTED}">more</text>
  </g>

  <!-- Integrated Telemetry Strip at Bottom -->
  <line x1="40" y1="{card_h - 40}" x2="{grid_right:.1f}" y2="{card_h - 40}" stroke="{RULE}" stroke-width="0.8"/>
  <g font-family="'Geist Mono', monospace" font-size="11">
    <text x="40" y="{card_h - 17}" fill="{MUTED}">TOTAL: <tspan font-weight="600" fill="{INK}">{total_c:,}</tspan></text>
    <text x="235" y="{card_h - 17}" fill="{MUTED}">LONGEST STREAK: <tspan font-weight="600" fill="{COBALT}">{ls} DAYS</tspan></text>
    <text x="470" y="{card_h - 17}" fill="{MUTED}">ACTIVE DAYS: <tspan font-weight="600" fill="{INK}">{active_d}</tspan></text>
    <text x="{grid_right:.1f}" y="{card_h - 17}" text-anchor="end" fill="{MUTED}">PEAK DAY: <tspan font-weight="600" fill="{COBALT}">{best_c} COMMITS</tspan></text>
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
