#!/usr/bin/env python3
"""
Render all custom SVG cards for Shashwat Upadhyay's GitHub Profile README (Master Revision V3.3).

Ultra-tight Swiss editorial rhythm (zero wasted vertical space), bespoke vector icons on
clickable nav buttons, subtle drop-shadow depth on the 2x-retina portrait, indexed hairline
section headers, live GitHub-native SVG animations, and CSS :hover micro-interactions.
"""

import os
import json
import re
from html import escape
from svg_utils import (
    make_card_svg, wrap_text, render_lines,
    PAPER, PAPER_MUTED, INK, INK_SOFT, MUTED, RULE,
    COBALT, CYAN, VIOLET, DARK_NAVY
)

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
DATA_DIR = os.path.join(ROOT, "data")
CARDS_DIR = os.path.join(ROOT, "cards")
ASSETS_DIR = os.path.join(ROOT, "assets")
PORTRAIT_SVG = os.path.join(ASSETS_DIR, "shashwat-portrait.svg")

W = 880  # Full README column width


def load_json(name):
    path = os.path.join(DATA_DIR, name)
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


# ==============================================================================
# 1. COMPACT HERO CARD (880 x 286)
# ==============================================================================
def render_hero():
    h = 286

    portrait_inner = ""
    if os.path.exists(PORTRAIT_SVG):
        with open(PORTRAIT_SVG, "r", encoding="utf-8") as pf:
            p_content = pf.read()
            m = re.search(r"<svg[^>]*>(.*?)</svg>", p_content, re.DOTALL)
            if m:
                portrait_inner = m.group(1)

    body = f"""
  <defs>
    <clipPath id="hero-clip">
      <rect width="{W}" height="{h}" rx="12"/>
    </clipPath>
    <filter id="port-shadow" x="-10%" y="-8%" width="125%" height="122%">
      <feDropShadow dx="0" dy="6" stdDeviation="7" flood-color="#0B1638" flood-opacity="0.14"/>
    </filter>
    <linearGradient id="upadhyay-blue" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="450" y2="0">
      <stop offset="0" stop-color="{COBALT}"/>
      <stop offset=".35" stop-color="{COBALT}"/>
      <stop offset=".5" stop-color="{CYAN}"/>
      <stop offset=".65" stop-color="{COBALT}"/>
      <stop offset="1" stop-color="{COBALT}"/>
      <animateTransform attributeName="gradientTransform" type="translate"
        values="-450 0; 450 0; 450 0" keyTimes="0;.45;1" dur="5.8s" begin="0.8s" repeatCount="indefinite"/>
    </linearGradient>
    <linearGradient id="top-beam" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="260" y2="0">
      <stop offset="0" stop-color="{COBALT}" stop-opacity="0"/>
      <stop offset=".45" stop-color="{COBALT}" stop-opacity="0.85"/>
      <stop offset=".6" stop-color="{CYAN}" stop-opacity="1"/>
      <stop offset="1" stop-color="{CYAN}" stop-opacity="0"/>
      <animateTransform attributeName="gradientTransform" type="translate"
        values="-260 0; 940 0" dur="6.5s" repeatCount="indefinite"/>
    </linearGradient>
    <radialGradient id="hero-ambient" cx="84%" cy="50%" r="36%">
      <stop offset="0%" stop-color="{COBALT}" stop-opacity="0.12"/>
      <stop offset="60%" stop-color="{CYAN}" stop-opacity="0.04"/>
      <stop offset="100%" stop-color="{COBALT}" stop-opacity="0"/>
    </radialGradient>
    <pattern id="hero-grid" width="22" height="22" patternUnits="userSpaceOnUse">
      <circle cx="1.5" cy="1.5" r="0.8" fill="{COBALT}" fill-opacity="0.14"/>
    </pattern>
  </defs>

  <g class="card-interactive">
    <g clip-path="url(#hero-clip)">
      <rect class="card-bg" width="{W}" height="{h}" rx="12" fill="{PAPER}" stroke="{RULE}" stroke-width="1"/>
      <rect x="520" y="0" width="360" height="{h}" fill="url(#hero-grid)"/>
      <rect width="{W}" height="{h}" fill="url(#hero-ambient)"/>
      <!-- Animated Top Light Beam -->
      <rect x="0" y="0" width="{W}" height="2.4" fill="url(#top-beam)"/>
    </g>
    <rect class="card-bg" x="0.5" y="0.5" width="{W - 1}" height="{h - 1}" rx="12" fill="none" stroke="{RULE}" stroke-width="1"/>

    <!-- Left Column: Typography & Verified Credentials -->
    <g>
      <circle class="ring" cx="44" cy="34" r="4" fill="none" stroke="{COBALT}" stroke-width="1.2"/>
      <circle class="live" cx="44" cy="34" r="3.5" fill="{COBALT}"/>
      <text x="58" y="38" font-family="'Geist Mono', monospace" font-size="10.5" letter-spacing="1.2" fill="{MUTED}">
        INDEPENDENT AI RESEARCHER // MULTIMODAL SYSTEMS
      </text>
    </g>

    <!-- Editorial Headline Name -->
    <text class="r" style="animation-delay:0.05s" x="40" y="108"
          font-family="'Instrument Serif', Georgia, serif" font-size="74" letter-spacing="-1" fill="{INK}">
      Shashwat
    </text>
    <text class="r" style="animation-delay:0.15s" x="40" y="170"
          font-family="'Instrument Serif', Georgia, serif" font-style="italic" font-size="74" letter-spacing="-1" fill="url(#upadhyay-blue)">
      Upadhyay.
    </text>

    <!-- Tagline & Core Statement Grounded in Resume -->
    <g class="r" style="animation-delay:0.25s">
      <text x="44" y="201" font-family="'Geist', sans-serif" font-weight="600" font-size="14.5" fill="{INK_SOFT}">
        Researching intelligence. Building systems.
      </text>
      <text x="44" y="220" font-family="'Geist', sans-serif" font-size="12.5" fill="{MUTED}">
        Multimodal AI · Computer Vision · Digital Twins · ML Security · Quant
      </text>
      <text x="44" y="239" font-family="'Geist Mono', monospace" font-size="10.8" fill="{MUTED}">
        BVoc Cyber Security (SAKEC, 2024–2028) · BS Data Science (IIT Madras, 2023–2028)
      </text>
    </g>

    <!-- Editorial Separator -->
    <line x1="44" y1="252" x2="610" y2="252" stroke="{RULE}" stroke-width="0.8"/>

    <!-- Research Affiliations Strip -->
    <text x="44" y="270" font-family="'Geist Mono', monospace" font-size="10" letter-spacing="0.4" fill="{MUTED}">
      <tspan fill="{COBALT}" font-weight="600">AFFILIATIONS //</tspan> MNIT Jaipur (MoHUA) · IIT (ISM) Dhanbad · WorldQuant · Mumbai, India
    </text>

    <!-- Right Column: Floating 2x-Retina Editorial Studio Portrait -->
    <g transform="translate(644, 19)" filter="url(#port-shadow)">
      <g transform="scale(0.95)">
        {portrait_inner}
      </g>
    </g>
  </g>
"""

    svg_out = make_card_svg(
        W, h, body,
        font_keys=["serif", "serif-i", "sans", "sans-b", "mono"],
        label="Shashwat Upadhyay — Research in Motion. Independent AI Researcher."
    )
    with open(os.path.join(CARDS_DIR, "hero.svg"), "w", encoding="utf-8") as f:
        f.write(svg_out)
    with open(os.path.join(ASSETS_DIR, "hero.svg"), "w", encoding="utf-8") as f:
        f.write(svg_out)
    print("wrote cards/hero.svg & assets/hero.svg")


# ==============================================================================
# 1B. FIVE INDIVIDUAL CLICKABLE QUICK-LINK BUTTONS WITH VECTOR ICONS (176 x 38)
# ==============================================================================
def render_nav_links():
    # Clean crisp 14x14 monochrome vector icons (origin 0,0)
    icons = {
        "github": '<path d="M7 0.5a6.5 6.5 0 0 0-2.05 12.67c.32.06.44-.14.44-.31v-1.1c-1.8.39-2.18-.87-2.18-.87-.3-.75-.72-.95-.72-.95-.59-.4.04-.39.04-.39.65.05 1 .67 1 .67.58 1 1.52.71 1.89.54.06-.42.23-.71.41-.87-1.44-.16-2.95-.72-2.95-3.2 0-.71.25-1.29.67-1.74-.07-.16-.29-.82.06-1.71 0 0 .55-.18 1.79.66a6.2 6.2 0 0 1 3.26 0c1.24-.84 1.79-.66 1.79-.66.35.89.13 1.55.06 1.71.42.45.67 1.03.67 1.74 0 2.49-1.52 3.04-2.96 3.2.23.2.44.6.44 1.21v1.79c0 .17.12.38.44.31A6.5 6.5 0 0 0 7 0.5z" fill="#315EFF"/>',
        "scholar": '<path d="M7 1.2L0.5 5l6.5 3.8L13.5 5 7 1.2zm-4.2 5.4v3.1c0 1.2 1.9 2.3 4.2 2.3s4.2-1.1 4.2-2.3V6.6L7 9.1 2.8 6.6z" fill="#315EFF"/>',
        "linkedin": '<rect x="0.8" y="0.8" width="12.4" height="12.4" rx="2.4" fill="none" stroke="#315EFF" stroke-width="1.3"/><circle cx="4.3" cy="4.4" r="0.95" fill="#315EFF"/><rect x="3.5" y="6.2" width="1.6" height="4.5" fill="#315EFF"/><path d="M6.7 6.2h1.5v.65c.25-.42.78-.75 1.45-.75 1.25 0 1.85.8 1.85 2.1v2.5H9.9V8.45c0-.6-.25-1-.8-1-.58 0-.85.4-.85 1v2.25H6.7V6.2z" fill="#315EFF"/>',
        "researchgate": '<rect x="0.8" y="0.8" width="12.4" height="12.4" rx="2.4" fill="none" stroke="#315EFF" stroke-width="1.3"/><text x="7" y="10.2" text-anchor="middle" font-family="\'Geist Mono\', monospace" font-size="7.2" font-weight="700" fill="#315EFF">RG</text>',
        "email": '<rect x="1" y="2.5" width="12" height="9" rx="1.6" fill="none" stroke="#315EFF" stroke-width="1.3"/><path d="M1.6 3.3L7 7.6l5.4-4.3" fill="none" stroke="#315EFF" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>',
    }

    items = [
        ("github", "GitHub"),
        ("scholar", "Scholar"),
        ("linkedin", "LinkedIn"),
        ("researchgate", "ResearchGate"),
        ("email", "Email"),
    ]
    pw = 176
    ph = 38

    for idx, (slug, label) in enumerate(items):
        wave_delay = idx * 0.35
        sheen_delay = idx * 0.9
        body = f"""
  <defs>
    <clipPath id="nav-clip-{slug}">
      <rect x="3" y="3" width="{pw - 6}" height="{ph - 6}" rx="7"/>
    </clipPath>
    <linearGradient id="nav-accent-{slug}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{COBALT}" stop-opacity="0"/>
      <stop offset="50%" stop-color="{COBALT}" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="{CYAN}" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="nav-sheen-{slug}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0"/>
      <stop offset="50%" stop-color="#FFFFFF" stop-opacity="0.65"/>
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <g class="card-interactive">
    <g clip-path="url(#nav-clip-{slug})">
      <rect class="card-bg" x="3" y="3" width="{pw - 6}" height="{ph - 6}" rx="7" fill="{PAPER}" stroke="{RULE}" stroke-width="1"/>
      <rect class="accent-bar" style="animation-delay:{wave_delay:.2f}s" x="18" y="3" width="{pw - 36}" height="2" rx="1" fill="url(#nav-accent-{slug})"/>
      <rect class="sh" style="animation-delay:{sheen_delay:.2f}s" x="0" y="0" width="42" height="{ph}" fill="url(#nav-sheen-{slug})"/>
    </g>
    <rect class="card-bg" x="3.5" y="3.5" width="{pw - 7}" height="{ph - 7}" rx="7" fill="none" stroke="{RULE}" stroke-width="1"/>
    <!-- Bespoke Vector Icon -->
    <g transform="translate(16, 12)">
      {icons[slug]}
    </g>
    <text x="38" y="23" font-family="'Geist Mono', monospace" font-size="11" font-weight="600" fill="{INK}">
      {escape(label)}
    </text>
    <text class="n" style="animation-delay:{wave_delay:.2f}s" x="{pw - 16}" y="23" text-anchor="end" font-family="'Geist Mono', monospace" font-size="11.5" fill="{COBALT}">&#8599;</text>
  </g>
"""
        svg_out = make_card_svg(
            pw, ph, body,
            font_keys=["mono"],
            label=f"Open Shashwat Upadhyay's {label}"
        )
        with open(os.path.join(CARDS_DIR, f"nav-{slug}.svg"), "w", encoding="utf-8") as f:
            f.write(svg_out)
    print("wrote cards/nav-*.svg (5 icon-equipped clickable nav buttons)")


# ==============================================================================
# 2. FIVE INDIVIDUAL CLICKABLE RESEARCH DOMAIN CARDS (Zero Wasted Air)
# ==============================================================================
def render_research_domains():
    # Row 1: tight 150px height
    r1_w = 293
    r1_h = 150
    pad = 4
    inner_w = r1_w - 2 * pad  # 285
    inner_h = r1_h - 2 * pad  # 142

    row1_domains = [
        {
            "slug": "domain-01",
            "num": "01",
            "title_1": "Multimodal AI &",
            "title_2": "Physiological Computing",
            "summary": "Non-contact vital monitoring via video, spatial-temporal models, and multimodal sensor fusion.",
            "foci": "PhysioFM · rPPG · WardOS · Fusion",
            "delay": 0.4,
        },
        {
            "slug": "domain-02",
            "num": "02",
            "title_1": "Intelligent Infrastructure",
            "title_2": "& Digital Twins",
            "summary": "Synchronized 3D simulation testbeds and edge computer vision for connected urban transit.",
            "foci": "IMPACT · SUMO · Unity 3D · YOLO",
            "delay": 1.6,
        },
        {
            "slug": "domain-03",
            "num": "03",
            "title_1": "Trustworthy AI &",
            "title_2": "ML Security",
            "summary": "Auditing VLM preprocessing attack surfaces, alpha-channel drift, and zero-label behavioral risk.",
            "foci": "VLM Security · SEV · SentinelAI",
            "delay": 2.8,
        }
    ]

    for d in row1_domains:
        summary_lines = wrap_text(d["summary"], 35)
        slug = d["slug"]
        delay = d["delay"]
        body = f"""
  <defs>
    <clipPath id="clip-{slug}">
      <rect x="{pad}" y="{pad}" width="{inner_w}" height="{inner_h}" rx="8"/>
    </clipPath>
    <linearGradient id="accent-{slug}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{COBALT}" stop-opacity="0"/>
      <stop offset="45%" stop-color="{COBALT}" stop-opacity="0.9"/>
      <stop offset="65%" stop-color="{CYAN}" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="{CYAN}" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="sheen-{slug}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0"/>
      <stop offset="50%" stop-color="#FFFFFF" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <g class="card-interactive">
    <g clip-path="url(#clip-{slug})">
      <rect class="card-bg" x="{pad}" y="{pad}" width="{inner_w}" height="{inner_h}" rx="8" fill="{PAPER}" stroke="{RULE}" stroke-width="1"/>
      <rect class="accent-bar" style="animation-delay:{delay:.1f}s" x="{pad + 16}" y="{pad}" width="{inner_w - 32}" height="2.2" rx="1" fill="url(#accent-{slug})"/>
      <rect class="sh" style="animation-delay:{delay:.1f}s" x="0" y="0" width="60" height="{r1_h}" fill="url(#sheen-{slug})"/>
    </g>
    <rect class="card-bg" x="{pad + 0.5}" y="{pad + 0.5}" width="{inner_w - 1}" height="{inner_h - 1}" rx="8" fill="none" stroke="{RULE}" stroke-width="1"/>

    <!-- Header number & arrow -->
    <text x="{pad + 16}" y="{pad + 22}" font-family="'Geist Mono', monospace" font-size="10" font-weight="600" fill="{COBALT}">{d['num']} //</text>
    <text class="n" style="animation-delay:{delay * 0.4:.1f}s" x="{pad + inner_w - 16}" y="{pad + 22}" text-anchor="end" font-family="'Geist Mono', monospace" font-size="11.5" fill="{COBALT}">&#8599;</text>

    <!-- 2-line title -->
    <text x="{pad + 16}" y="{pad + 40}" font-family="'Geist', sans-serif" font-weight="600" font-size="13.5" fill="{INK}">{escape(d['title_1'])}</text>
    <text x="{pad + 16}" y="{pad + 56}" font-family="'Geist', sans-serif" font-weight="600" font-size="13.5" fill="{INK}">{escape(d['title_2'])}</text>

    <!-- Complete 3-line summary -->
    {render_lines(pad + 16, pad + 75, summary_lines, 14.5, f'font-family="\'Geist\', sans-serif" font-size="11" fill="{INK_SOFT}"')}

    <!-- Divider & technical tags -->
    <line x1="{pad + 16}" y1="{pad + inner_h - 25}" x2="{pad + inner_w - 16}" y2="{pad + inner_h - 25}" stroke="{RULE}" stroke-width="0.7"/>
    <text x="{pad + 16}" y="{pad + inner_h - 9}" font-family="'Geist Mono', monospace" font-size="9.5" fill="{MUTED}">{escape(d['foci'])}</text>
  </g>
"""
        svg_out = make_card_svg(
            r1_w, r1_h, body,
            font_keys=["sans", "sans-b", "mono"],
            label=f"Research Direction {d['num']}: {d['title_1']} {d['title_2']}"
        )
        with open(os.path.join(CARDS_DIR, f"{slug}.svg"), "w", encoding="utf-8") as f:
            f.write(svg_out)

    # Row 2: tight 114px height (eliminates the 35px empty internal void!)
    r2_w = 440
    r2_h = 114
    inner2_w = r2_w - 2 * pad  # 432
    inner2_h = r2_h - 2 * pad  # 106

    row2_domains = [
        {
            "slug": "domain-04",
            "num": "04",
            "title": "Computer Vision & Document Intelligence",
            "summary": "Object detection, CNN scientific image segmentation, and end-to-end OCR document parsing pipelines.",
            "foci": "YOLOv8 12k+ (92% acc) · OCR (96% acc) · CLIP",
            "delay": 1.0,
        },
        {
            "slug": "domain-05",
            "num": "05",
            "title": "Quantitative Research & Financial Modelling",
            "summary": "Statistical alpha signal discovery, multi-year equity backtesting, and systematic variance reduction.",
            "foci": "Alpha Signals · Sharpe > 1.5 · 22% Variance Cut",
            "delay": 2.2,
        }
    ]

    for d in row2_domains:
        summary_lines = wrap_text(d["summary"], 54)
        slug = d["slug"]
        delay = d["delay"]
        body = f"""
  <defs>
    <clipPath id="clip-{slug}">
      <rect x="{pad}" y="{pad}" width="{inner2_w}" height="{inner2_h}" rx="8"/>
    </clipPath>
    <linearGradient id="accent-{slug}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{COBALT}" stop-opacity="0"/>
      <stop offset="45%" stop-color="{COBALT}" stop-opacity="0.9"/>
      <stop offset="65%" stop-color="{CYAN}" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="{CYAN}" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="sheen-{slug}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0"/>
      <stop offset="50%" stop-color="#FFFFFF" stop-opacity="0.5"/>
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <g class="card-interactive">
    <g clip-path="url(#clip-{slug})">
      <rect class="card-bg" x="{pad}" y="{pad}" width="{inner2_w}" height="{inner2_h}" rx="8" fill="{PAPER}" stroke="{RULE}" stroke-width="1"/>
      <rect class="accent-bar" style="animation-delay:{delay:.1f}s" x="{pad + 18}" y="{pad}" width="{inner2_w - 36}" height="2.2" rx="1" fill="url(#accent-{slug})"/>
      <rect class="sh" style="animation-delay:{delay:.1f}s" x="0" y="0" width="76" height="{r2_h}" fill="url(#sheen-{slug})"/>
    </g>
    <rect class="card-bg" x="{pad + 0.5}" y="{pad + 0.5}" width="{inner2_w - 1}" height="{inner2_h - 1}" rx="8" fill="none" stroke="{RULE}" stroke-width="1"/>

    <!-- Subtle Technical XY Grid Motif in Corner -->
    <path d="M {pad + inner2_w - 34} {pad + 12} L {pad + inner2_w - 12} {pad + 12} M {pad + inner2_w - 12} {pad + 12} L {pad + inner2_w - 12} {pad + 32}"
          fill="none" stroke="{COBALT}" stroke-width="1.2" stroke-opacity="0.45"/>
    <circle class="live" style="animation-delay:{delay * 0.5:.1f}s" cx="{pad + inner2_w - 12}" cy="{pad + 12}" r="2.2" fill="{COBALT}"/>

    <!-- Header Number & Title -->
    <text x="{pad + 18}" y="{pad + 24}" font-family="'Geist Mono', monospace" font-size="10.5" font-weight="600" fill="{COBALT}">{d['num']} //</text>
    <text x="{pad + 52}" y="{pad + 24}" font-family="'Geist', sans-serif" font-weight="600" font-size="13.5" fill="{INK}">{escape(d['title'])}</text>
    <text class="n" style="animation-delay:{delay * 0.4:.1f}s" x="{pad + inner2_w - 40}" y="{pad + 24}" font-family="'Geist Mono', monospace" font-size="11.5" fill="{COBALT}">&#8599;</text>

    <!-- Complete 2-line description -->
    {render_lines(pad + 18, pad + 46, summary_lines, 16, f'font-family="\'Geist\', sans-serif" font-size="11.5" fill="{INK_SOFT}"')}

    <!-- Divider & focus tags -->
    <line x1="{pad + 18}" y1="{pad + inner2_h - 24}" x2="{pad + inner2_w - 18}" y2="{pad + inner2_h - 24}" stroke="{RULE}" stroke-width="0.7"/>
    <text x="{pad + 18}" y="{pad + inner2_h - 9}" font-family="'Geist Mono', monospace" font-size="9.5" fill="{MUTED}">{escape(d['foci'])}</text>
  </g>
"""
        svg_out = make_card_svg(
            r2_w, r2_h, body,
            font_keys=["sans", "sans-b", "mono"],
            label=f"Research Direction {d['num']}: {d['title']}"
        )
        with open(os.path.join(CARDS_DIR, f"{slug}.svg"), "w", encoding="utf-8") as f:
            f.write(svg_out)

    print("wrote cards/domain-01..05.svg (tightened, zero internal void)")


# ==============================================================================
# 3. THREE COMPACT FEATURED PROJECT CARDS (293 x 168 EACH, TIGHT & PUNCHY)
# ==============================================================================
def render_three_featured_projects():
    tile_w = 293
    tile_h = 168
    pad = 4
    inner_w = tile_w - 2 * pad  # 285
    inner_h = tile_h - 2 * pad  # 160

    projects = [
        {
            "id": "physiofm",
            "name": "PhysioFM",
            "subtitle": "rPPG Foundation Model",
            "desc": "Hierarchical Swin-V2 + STDS framework diagnosing optimization mode collapse in continuous physiological waveforms.",
            "tech": "Swin-V2 · STDS · UBFC-rPPG · SHMS",
            "color": COBALT,
            "delay": 0.3,
        },
        {
            "id": "digital-twins",
            "name": "Urban Digital Twins",
            "subtitle": "Smart Mobility & Transit Testbeds",
            "desc": "GIS-integrated Unity 3D twin of a 25 km Jaipur corridor coupling SUMO traffic with edge YOLO (18% peak load cut).",
            "tech": "SUMO · Unity 3D · YOLO · IMPACT",
            "color": "#00A896",
            "delay": 1.5,
        },
        {
            "id": "vlm-security",
            "name": "Semantic Drift in VLMs",
            "subtitle": "Preprocessing Attack Surface (IGI Global)",
            "desc": "Exposing RGBA-to-RGB alpha-channel flattening vulnerabilities in VLMs with SEV defense verification (Accepted Chapter).",
            "tech": "VLM Security · SEV · DOI: 10.4018",
            "color": VIOLET,
            "delay": 2.7,
        }
    ]

    for p in projects:
        desc_lines = wrap_text(p["desc"], 35)
        pid = p["id"]
        c = p["color"]
        delay = p["delay"]
        extra_css = f".card-interactive:hover .card-bg {{ stroke: {c}; }}"
        body = f"""
  <defs>
    <clipPath id="clip-proj-{pid}">
      <rect x="{pad}" y="{pad}" width="{inner_w}" height="{inner_h}" rx="10"/>
    </clipPath>
    <linearGradient id="proj-bar-{pid}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{c}" stop-opacity="0.15"/>
      <stop offset="50%" stop-color="{c}" stop-opacity="1"/>
      <stop offset="100%" stop-color="{c}" stop-opacity="0.15"/>
    </linearGradient>
    <linearGradient id="proj-sheen-{pid}" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0"/>
      <stop offset="50%" stop-color="#FFFFFF" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <g class="card-interactive">
    <g clip-path="url(#clip-proj-{pid})">
      <rect class="card-bg" x="{pad}" y="{pad}" width="{inner_w}" height="{inner_h}" rx="10" fill="{PAPER}" stroke="{RULE}" stroke-width="1"/>
      <rect class="accent-bar" style="animation-delay:{delay:.1f}s" x="{pad}" y="{pad}" width="{inner_w}" height="3" fill="url(#proj-bar-{pid})"/>
      <rect class="sh" style="animation-delay:{delay:.1f}s" x="0" y="0" width="64" height="{tile_h}" fill="url(#proj-sheen-{pid})"/>
    </g>
    <rect class="card-bg" x="{pad + 0.5}" y="{pad + 0.5}" width="{inner_w - 1}" height="{inner_h - 1}" rx="10" fill="none" stroke="{RULE}" stroke-width="1"/>

    <g>
      <circle class="ring" style="animation-delay:{delay * 0.5:.1f}s" cx="{pad + 20}" cy="{pad + 22}" r="4.5" fill="none" stroke="{c}" stroke-width="1.2"/>
      <rect x="{pad + 16}" y="{pad + 18}" width="8" height="8" rx="2" fill="{c}"/>
      <text x="{pad + 32}" y="{pad + 26}" font-family="'Geist', sans-serif" font-weight="600" font-size="14.5" fill="{INK}">
        {escape(p['name'])}
      </text>
      <text class="n" style="animation-delay:{delay * 0.4:.1f}s" x="{pad + inner_w - 16}" y="{pad + 26}" text-anchor="end" font-family="'Geist Mono', monospace" font-size="12" fill="{c}">&#8599;</text>

      <!-- Subtitle -->
      <text x="{pad + 16}" y="{pad + 43}" font-family="'Geist Mono', monospace" font-size="9.5" fill="{MUTED}">{escape(p['subtitle'])}</text>

      <!-- Description -->
      {render_lines(pad + 16, pad + 62, desc_lines, 15, f'font-family="\'Geist\', sans-serif" font-size="11" fill="{INK_SOFT}"')}

      <!-- Divider & Tech Label -->
      <line x1="{pad + 16}" y1="{pad + inner_h - 28}" x2="{pad + inner_w - 16}" y2="{pad + inner_h - 28}" stroke="{RULE}" stroke-width="0.8"/>
      <text x="{pad + 16}" y="{pad + inner_h - 11}" font-family="'Geist Mono', monospace" font-size="9.5" font-weight="600" fill="{c}">{escape(p['tech'])}</text>
    </g>
  </g>
"""
        svg_out = make_card_svg(
            tile_w, tile_h, body,
            font_keys=["sans", "sans-b", "mono"],
            label=f"{p['name']}: {p['subtitle']}",
            extra_css=extra_css
        )
        with open(os.path.join(CARDS_DIR, f"project-{pid}.svg"), "w", encoding="utf-8") as f:
            f.write(svg_out)
        print(f"wrote cards/project-{pid}.svg")


# ==============================================================================
# 4. TIGHT ACADEMIC & RESEARCH MILESTONES STRIP (880 x 96)
# ==============================================================================
def render_timeline():
    w = 880
    h = 96

    milestones = [
        ("2023 — 2028", "IIT Madras", "BS Data Science"),
        ("2024 — 2028", "SAKEC", "BVoc Cyber Security"),
        ("May — Jul 2024", "MNIT (AMRUT)", "Research Intern"),
        ("Apr — Sep 2025", "WorldQuant", "Quant Consultant"),
        ("May 2025 — Pres", "MNIT (MoHUA)", "Transit Researcher"),
        ("Nov — Dec 2025", "IIT Dhanbad", "ML Research Intern"),
    ]

    items_svg = []
    step_x = (w - 48) / len(milestones)
    for i, (period, org, title) in enumerate(milestones):
        x = 24 + i * step_x
        delay = i * 0.45
        items_svg.append(f"""
    <g>
      <circle class="ring" style="animation-delay:{delay:.2f}s" cx="{x + 6}" cy="42" r="4.5" fill="none" stroke="{COBALT}" stroke-width="1.2"/>
      <circle cx="{x + 6}" cy="42" r="4" fill="{COBALT}"/>
      <text x="{x + 6}" y="25" font-family="'Geist Mono', monospace" font-size="9.5" font-weight="600" fill="{COBALT}">{period}</text>
      <text x="{x + 6}" y="61" font-family="'Geist', sans-serif" font-weight="600" font-size="11.5" fill="{INK}">{escape(org)}</text>
      <text x="{x + 6}" y="77" font-family="'Geist', sans-serif" font-size="10.5" fill="{MUTED}">{escape(title)}</text>
    </g>
        """)

    body = f"""
  <defs>
    <linearGradient id="tl-pulse" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="140" y2="0">
      <stop offset="0" stop-color="{COBALT}" stop-opacity="0"/>
      <stop offset=".55" stop-color="{COBALT}" stop-opacity="0.95"/>
      <stop offset=".85" stop-color="{CYAN}" stop-opacity="1"/>
      <stop offset="1" stop-color="{CYAN}" stop-opacity="0"/>
      <animateTransform attributeName="gradientTransform" type="translate"
        values="-120 0; 880 0" dur="4.8s" repeatCount="indefinite"/>
    </linearGradient>
    <clipPath id="tl-clip">
      <rect x="24" y="38" width="{w - 48}" height="8"/>
    </clipPath>
  </defs>

  <rect width="{w}" height="{h}" rx="8" fill="{PAPER}" stroke="{RULE}" stroke-width="1"/>
  <line x1="24" y1="42" x2="{w - 24}" y2="42" stroke="{RULE}" stroke-width="1.2"/>
  <g clip-path="url(#tl-clip)">
    <line x1="24" y1="42" x2="{w - 24}" y2="42" stroke="url(#tl-pulse)" stroke-width="2.2" stroke-linecap="round"/>
  </g>
  {''.join(items_svg)}
"""

    svg_out = make_card_svg(
        w, h, body,
        font_keys=["sans", "sans-b", "mono"],
        label="Academic and Research Milestones"
    )
    with open(os.path.join(CARDS_DIR, "research-timeline.svg"), "w", encoding="utf-8") as f:
        f.write(svg_out)
    print("wrote cards/research-timeline.svg (tight 96px height)")


# ==============================================================================
# 5. INDEXED SWISS EDITORIAL SECTION HEADERS (880 x 36, WITH HAIRLINE RULE & TAG)
# ==============================================================================
def render_section_title(slug, index_num, title, italic, badge, dark_fg="#E6EDF3", light_fg=INK):
    for theme, fg, rule_c, muted_c in [
        ("light", light_fg, "#DCDCD7", "#6E6E73"),
        ("dark", dark_fg, "#30363D", "#8B949E"),
    ]:
        # Approximate width of the heading so the hairline starts cleanly right after the text
        approx_text_w = 46 + int((len(title) + len(italic) + 1) * 12.2)
        rule_x1 = min(640, approx_text_w + 14)
        rule_x2 = W - (len(badge) * 6.5 + 18)

        body = f"""
  <text x="2" y="24" font-family="'Geist Mono', monospace" font-size="10.5" font-weight="600" fill="{COBALT}">
    {index_num} //
  </text>
  <text x="42" y="26" font-family="'Instrument Serif', Georgia, serif" font-size="27" fill="{fg}">
    {escape(title)} <tspan font-style="italic" fill="{COBALT}">{escape(italic)}</tspan>
  </text>
  <line x1="{rule_x1}" y1="20" x2="{rule_x2:.0f}" y2="20" stroke="{rule_c}" stroke-width="0.9"/>
  <circle cx="{rule_x2 + 6:.0f}" cy="20" r="2" fill="{COBALT}"/>
  <text x="{W - 2}" y="23.5" text-anchor="end" font-family="'Geist Mono', monospace" font-size="9.5" letter-spacing="0.8" fill="{muted_c}">
    {escape(badge)}
  </text>
"""
        svg_out = make_card_svg(
            W, 34, body,
            font_keys=["serif", "serif-i", "mono"],
            label=f"Section {index_num}: {title} {italic}"
        )
        with open(os.path.join(CARDS_DIR, f"title-{slug}-{theme}.svg"), "w", encoding="utf-8") as f:
            f.write(svg_out)


def render_all_titles():
    titles = [
        ("research", "01", "Research", "Directions", "5 PILLARS"),
        ("projects", "02", "Featured", "Research Projects", "3 SYSTEMS"),
        ("publications", "03", "Publications &", "Milestones", "7 WORKS"),
        ("stack", "04", "Technology", "Toolkit", "CORE STACK"),
        ("activity", "05", "GitHub", "Telemetry & Heatmap", "LIVE DATA"),
        ("repos", "06", "Featured", "Repositories & Codebases", "OPEN SOURCE"),
        ("connect", "07", "Connect &", "Collaborate", "REACH OUT"),
    ]
    for slug, num, t, it, badge in titles:
        render_section_title(slug, num, t, it, badge)
    print("wrote indexed hairline title SVGs")


def main():
    os.makedirs(CARDS_DIR, exist_ok=True)
    render_hero()
    render_nav_links()
    render_research_domains()
    render_three_featured_projects()
    render_timeline()
    render_all_titles()
    print("Rendered Master Revision V3.3 cards successfully.")


if __name__ == "__main__":
    main()
