#!/usr/bin/env python3
"""
Generate the tight, punchy monthly activity, streak, repository metrics & language distribution card
(cards/activity.svg) using real GitHub telemetry from data/contributions.json and data/github_stats.json.
"""

import os
import json
import datetime
from svg_utils import make_card_svg, PAPER, INK, INK_SOFT, MUTED, COBALT, RULE

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
DATA_FILE = os.path.join(ROOT, "data", "contributions.json")
STATS_FILE = os.path.join(ROOT, "data", "github_stats.json")
OUT_FILE = os.path.join(ROOT, "cards", "activity.svg")

SHORT_LANG = {
    "TypeScript": "TS",
    "JavaScript": "JS",
    "Jupyter Notebook": "Jupyter",
}


def generate():
    if not os.path.exists(DATA_FILE):
        print(f"Error: {DATA_FILE} not found. Run fetch_github_data.py first.")
        return

    with open(DATA_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    stats = {}
    if os.path.exists(STATS_FILE):
        with open(STATS_FILE, "r", encoding="utf-8") as sf:
            stats = json.load(sf)

    monthly_raw = data.get("monthly", [])
    if not monthly_raw:
        print("No monthly data available")
        return

    w = 880
    h = 322
    monthly = monthly_raw[-12:]

    best_month = max(monthly, key=lambda m: m["total"])
    top_total = max(1, best_month["total"])

    # Tight Bar chart coordinates
    chart_x0, chart_x1 = 44, 580
    base_y = 224
    max_bar_h = 112
    gap = 9
    bar_w = (chart_x1 - chart_x0 - gap * (len(monthly) - 1)) / len(monthly)

    bars_svg = []
    for i, m in enumerate(monthly):
        is_best = (m["total"] == best_month["total"] and m["month"] == best_month["month"])
        bh = max(3, round((m["total"] / top_total) * max_bar_h))
        x = chart_x0 + i * (bar_w + gap)
        y = base_y - bh
        fill = COBALT if is_best else (INK if m["total"] > 0 else "#C9C9C4")

        try:
            m_date = datetime.date.fromisoformat(m["month"] + "-01")
            m_label = m_date.strftime("%b")
        except Exception:
            m_label = m["month"][-2:]

        delay = 0.35 + i * 0.04
        bars_svg.append(
            f'<rect class="g" style="animation-delay:{delay:.2f}s" '
            f'x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{bh}" rx="3" fill="{fill}">'
            f'<title>{m_label} {m["month"][:4]}: {m["total"]} contributions</title>'
            f'</rect>'
            f'<text class="f" style="animation-delay:{delay:.2f}s" '
            f'x="{x + bar_w/2:.1f}" y="{base_y + 17}" text-anchor="middle" '
            f'font-family="\'Geist Mono\', monospace" font-size="10" fill="{MUTED}">{m_label}</text>'
        )

        if is_best and m["total"] > 0:
            bars_svg.append(
                f'<text class="p" style="animation-delay:0.9s" '
                f'x="{x + bar_w/2:.1f}" y="{y - 7:.1f}" text-anchor="middle" '
                f'font-family="\'Geist Mono\', monospace" font-size="10.5" font-weight="600" fill="{COBALT}">'
                f'{m["total"]}</text>'
            )

    # Right side metrics panel (tight vertical rhythm)
    cs = data.get("current_streak", {}).get("length", 0)
    ls = data.get("longest_streak", {}).get("length", 0)
    total_active = data.get("active_days", 0)
    total_days = len(data.get("days", [])) or 365
    best_day = data.get("best_day", {})
    best_day_count = best_day.get("count", 0)
    best_day_date = best_day.get("date", "")

    if cs > 0:
        streak_note = f"current streak {cs}d · longest {ls}d"
    else:
        streak_note = f"longest streak was {ls} days"

    stats_items = [
        (f'{ls} <tspan font-style="italic">days</tspan>', streak_note),
        (f'{total_active}<tspan font-size="19" fill="#8E8E93"> / {total_days}</tspan>', "active contribution days"),
        (f'{best_day_count} <tspan font-style="italic">commits</tspan>', f"busiest day ({best_day_date})" if best_day_date else "on the busiest day"),
    ]

    side_panel = []
    panel_x = 625
    for idx, (headline, caption) in enumerate(stats_items):
        stat_y = 74 + idx * 66
        delay = 0.5 + idx * 0.1
        side_panel.append(
            f'<g class="r" style="animation-delay:{delay:.2f}s">'
            f'<text x="{panel_x}" y="{stat_y}" font-family="\'Instrument Serif\', Georgia, serif" font-size="30" fill="{INK}">{headline}</text>'
            f'<text x="{panel_x}" y="{stat_y + 18}" font-family="\'Geist\', sans-serif" font-size="11" fill="{MUTED}">{caption}</text>'
            f'</g>'
        )
        if idx < 2:
            side_panel.append(
                f'<line x1="{panel_x}" y1="{stat_y + 29}" x2="{w - 44}" y2="{stat_y + 29}" stroke="{RULE}" stroke-width="0.8"/>'
            )

    total_c = data.get("total_contributions", 0)

    # Repository & Language Telemetry
    public_repos = stats.get("public_repos", 46)
    total_stars = stats.get("total_stars", 63)
    total_forks = stats.get("total_forks", 18)

    lang_colors = {
        "Python": "#3572A5",
        "TypeScript": "#3178C6",
        "HTML": "#E34C26",
        "CSS": "#563D7C",
        "C++": "#F34B7D",
        "Jupyter Notebook": "#DA5B0B",
        "JavaScript": "#F1E05A",
        "Other": "#8E8E93",
    }

    raw_langs = stats.get("languages", [
        {"name": "Python", "pct": 30.0},
        {"name": "TypeScript", "pct": 30.0},
        {"name": "HTML", "pct": 16.7},
        {"name": "CSS", "pct": 13.3},
        {"name": "C++", "pct": 3.3},
    ])

    display_langs = list(raw_langs[:5])
    top_sum = sum(l["pct"] for l in display_langs)
    rem = round(max(0.0, 100.0 - top_sum), 1)
    if rem >= 1.0:
        display_langs.append({"name": "Other", "pct": rem})

    total_pct = sum(l["pct"] for l in display_langs) or 100.0
    lang_bar_x = 450
    lang_bar_w = 386
    lang_bar_y = 278
    lang_bar_h = 7

    bar_segments = []
    cur_x = lang_bar_x
    for idx, l in enumerate(display_langs):
        if idx == len(display_langs) - 1:
            seg_w = max(0.0, (lang_bar_x + lang_bar_w) - cur_x)
        else:
            seg_w = (l["pct"] / total_pct) * lang_bar_w
        c = lang_colors.get(l["name"], COBALT)
        bar_segments.append(
            f'<rect x="{cur_x:.1f}" y="{lang_bar_y}" width="{seg_w:.1f}" height="{lang_bar_h}" fill="{c}">'
            f'<title>{l["name"]}: {l["pct"]}%</title></rect>'
        )
        cur_x += seg_w

    lang_labels = " · ".join(
        f"{SHORT_LANG.get(l['name'], l['name'])} {round(l['pct'])}%"
        for l in display_langs
    )

    body = f"""
  <defs>
    <linearGradient id="lang-sheen" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0"/>
      <stop offset="50%" stop-color="#FFFFFF" stop-opacity="0.75"/>
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="lang-clip">
      <rect x="{lang_bar_x}" y="{lang_bar_y}" width="{lang_bar_w}" height="{lang_bar_h}" rx="3.5"/>
    </clipPath>
  </defs>

  <!-- Card Background -->
  <rect width="{w}" height="{h}" rx="12" fill="{PAPER}" stroke="{RULE}" stroke-width="1"/>

  <!-- Left Header -->
  <text class="f" style="animation-delay:0.05s" x="44" y="36"
        font-family="'Geist Mono', monospace" font-size="10" letter-spacing="1" fill="{MUTED}">
    THE LAST 12 MONTHS ON GITHUB
  </text>
  <text class="r" style="animation-delay:0.12s" x="42" y="74"
        font-family="'Instrument Serif', Georgia, serif" font-size="38" fill="{INK}">
    {total_c:,} <tspan font-style="italic" fill="{COBALT}">contributions</tspan>
  </text>

  <!-- Left Chart Baseline -->
  <line x1="{chart_x0}" y1="{base_y + 2}" x2="{chart_x1}" y2="{base_y + 2}" stroke="{RULE}" stroke-width="1"/>

  <!-- Monthly Bars -->
  {''.join(bars_svg)}

  <!-- Vertical Divider Between Chart and Stats -->
  <line x1="600" y1="30" x2="600" y2="244" stroke="{RULE}" stroke-width="1" stroke-dasharray="3 3"/>

  <!-- Right Metrics Panel -->
  {''.join(side_panel)}

  <!-- Bottom Horizontal Divider -->
  <line x1="44" y1="258" x2="{w - 44}" y2="258" stroke="{RULE}" stroke-width="1"/>

  <!-- Bottom Strip: Repository Stats on Left -->
  <g font-family="'Geist Mono', monospace" font-size="11" fill="{INK}">
    <text x="44" y="284">
      <tspan font-weight="600" fill="{COBALT}">{public_repos}</tspan> Repositories
      <tspan fill="{MUTED}">·</tspan>
      <tspan font-weight="600" fill="{COBALT}">{total_stars}</tspan> Stars
      <tspan fill="{MUTED}">·</tspan>
      <tspan font-weight="600" fill="{COBALT}">{total_forks}</tspan> Forks
    </text>
    <text x="44" y="304" font-family="'Geist', sans-serif" font-size="10.8" fill="{MUTED}">
      Primary ecosystems: Research prototypes, AI tooling, multimodal digital twins
    </text>
  </g>

  <!-- Bottom Strip: Stacked Language Bar on Right -->
  <g>
    <rect x="{lang_bar_x}" y="{lang_bar_y}" width="{lang_bar_w}" height="{lang_bar_h}" rx="3.5" fill="#E2E2DE"/>
    <g clip-path="url(#lang-clip)">
      {''.join(bar_segments)}
      <rect class="sh" x="{lang_bar_x}" y="{lang_bar_y - 2}" width="64" height="{lang_bar_h + 4}" fill="url(#lang-sheen)"/>
    </g>
    <text x="{lang_bar_x + lang_bar_w}" y="304" text-anchor="end" font-family="'Geist Mono', monospace" font-size="9.5" fill="{MUTED}">
      {lang_labels}
    </text>
  </g>
"""

    svg_out = make_card_svg(
        w, h, body,
        font_keys=["serif", "serif-i", "sans", "mono"],
        label=f"Shashwat Upadhyay: Activity in the last 12 months with {total_c} total contributions, {public_repos} repos, {total_stars} stars"
    )

    os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)
    with open(OUT_FILE, "w", encoding="utf-8") as f:
        f.write(svg_out)
    print(f"Generated tight {OUT_FILE} ({len(svg_out)} bytes)")


if __name__ == "__main__":
    generate()
