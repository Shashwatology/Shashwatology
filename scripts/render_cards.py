#!/usr/bin/env python3
"""
Render all custom SVG cards for Shashwat Upadhyay's GitHub Profile README (Master Revision V3.4).

Flagship Studio Polish:
- cards/hero.svg: 2x-retina floating studio portrait, permanent cobalt Upadhyay with cyan sweep,
                  subtle animated multimodal signal spline, radar pulse, ambient blueprint dot field
- cards/nav-*.svg: 5 clickable icon-equipped buttons with staggered wave & sheen
- cards/domain-01..05.svg: 5 clickable research cards with rounded micro-chip tags & zero internal void
- cards/project-*.svg: 3 clickable project cards with animated scientific micro-diagrams
                       (rPPG waveform, transit twin graph, VLM alpha-layer drift)
- cards/badge-*.svg: 5 crisp local editorial status badges for Publications table (zero ugly line-wrap)
- cards/research-timeline.svg: tight 96px 6-milestone strip with traveling cyan signal pulse
- cards/title-*.svg: indexed Swiss hairline section headers
- cards/footer-bar.svg: subtle animated editorial monograph signature rule
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


def render_chips(start_x, y, tags, max_x, pill_fill="#EAECE6", text_fill=INK_SOFT, border_fill="#D7D9D2"):
    """Render compact rounded micro-chips cleanly on one row without ever exceeding max_x."""
    svg_parts = []
    cx = start_x
    h = 17
    for idx, t in enumerate(tags):
        # Geist Mono 8.6px is ~5.2px per char + 11px horizontal padding
        tw = int(len(t) * 5.25 + 12)
        if cx + tw > max_x:
            break
        # First chip subtly cobalt-tinted for focal hierarchy
        if idx == 0:
            pf, bf, tf = "#E7EDFF", "#C2D2FF", COBALT
        else:
            pf, bf, tf = pill_fill, border_fill, text_fill
        svg_parts.append(
            f'<rect x="{cx}" y="{y}" width="{tw}" height="{h}" rx="4" fill="{pf}" stroke="{bf}" stroke-width="0.6"/>'
            f'<text x="{cx + tw / 2:.1f}" y="{y + 11.6:.1f}" text-anchor="middle" '
            f'font-family="\'Geist Mono\', monospace" font-size="8.6" font-weight="600" fill="{tf}">{escape(t)}</text>'
        )
        cx += tw + 5
    return "".join(svg_parts)


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

    extra_css = """
    @keyframes wave-flow {
      from { stroke-dashoffset: 320; }
      to { stroke-dashoffset: 0; }
    }
    .signal-wave { stroke-dasharray: 160 160; animation: wave-flow 7s linear infinite; }
    """

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
    <linearGradient id="wave-grad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{COBALT}" stop-opacity="0"/>
      <stop offset="35%" stop-color="{COBALT}" stop-opacity="0.22"/>
      <stop offset="70%" stop-color="{CYAN}" stop-opacity="0.28"/>
      <stop offset="100%" stop-color="{COBALT}" stop-opacity="0"/>
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
      <!-- Subtle Multimodal Research Signal Wave Behind Right-Mid Canvas -->
      <path d="M 350 155 C 400 120, 430 190, 480 150 S 545 118, 595 154 S 630 180, 660 148"
            fill="none" stroke="{COBALT}" stroke-opacity="0.09" stroke-width="1.2"/>
      <path class="signal-wave" d="M 350 155 C 400 120, 430 190, 480 150 S 545 118, 595 154 S 630 180, 660 148"
            fill="none" stroke="url(#wave-grad)" stroke-width="1.6"/>
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
        label="Shashwat Upadhyay — Research in Motion. Independent AI Researcher.",
        extra_css=extra_css
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
    print("wrote cards/nav-*.svg")


# ==============================================================================
# 2. FIVE INDIVIDUAL CLICKABLE RESEARCH DOMAIN CARDS WITH MICRO-CHIP PILLS
# ==============================================================================
def render_research_domains():
    r1_w = 293
    r1_h = 152
    pad = 4
    inner_w = r1_w - 2 * pad  # 285
    inner_h = r1_h - 2 * pad  # 144

    row1_domains = [
        {
            "slug": "domain-01",
            "num": "01",
            "title_1": "Multimodal AI &",
            "title_2": "Physiological Computing",
            "summary": "Non-contact vital monitoring via video, spatial-temporal models, and multimodal sensor fusion.",
            "tags": ["PhysioFM", "rPPG", "WardOS", "Fusion"],
            "delay": 0.4,
        },
        {
            "slug": "domain-02",
            "num": "02",
            "title_1": "Intelligent Infrastructure",
            "title_2": "& Digital Twins",
            "summary": "Synchronized 3D simulation testbeds and edge computer vision for connected urban transit.",
            "tags": ["IMPACT", "SUMO", "Unity 3D", "YOLO"],
            "delay": 1.6,
        },
        {
            "slug": "domain-03",
            "num": "03",
            "title_1": "Trustworthy AI &",
            "title_2": "ML Security",
            "summary": "Auditing VLM preprocessing attack surfaces, alpha-channel drift, and zero-label behavioral risk.",
            "tags": ["VLM Security", "SEV", "SentinelAI"],
            "delay": 2.8,
        }
    ]

    for d in row1_domains:
        summary_lines = wrap_text(d["summary"], 35)
        slug = d["slug"]
        delay = d["delay"]
        chips_svg = render_chips(pad + 16, pad + inner_h - 24, d["tags"], pad + inner_w - 14)
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

    <text x="{pad + 16}" y="{pad + 22}" font-family="'Geist Mono', monospace" font-size="10" font-weight="600" fill="{COBALT}">{d['num']} //</text>
    <text class="n" style="animation-delay:{delay * 0.4:.1f}s" x="{pad + inner_w - 16}" y="{pad + 22}" text-anchor="end" font-family="'Geist Mono', monospace" font-size="11.5" fill="{COBALT}">&#8599;</text>

    <text x="{pad + 16}" y="{pad + 40}" font-family="'Geist', sans-serif" font-weight="600" font-size="13.5" fill="{INK}">{escape(d['title_1'])}</text>
    <text x="{pad + 16}" y="{pad + 56}" font-family="'Geist', sans-serif" font-weight="600" font-size="13.5" fill="{INK}">{escape(d['title_2'])}</text>

    {render_lines(pad + 16, pad + 75, summary_lines, 14.2, f'font-family="\'Geist\', sans-serif" font-size="11" fill="{INK_SOFT}"')}

    <!-- Crisp Micro-Chip Tags -->
    <g>{chips_svg}</g>
  </g>
"""
        svg_out = make_card_svg(
            r1_w, r1_h, body,
            font_keys=["sans", "sans-b", "mono"],
            label=f"Research Direction {d['num']}: {d['title_1']} {d['title_2']}"
        )
        with open(os.path.join(CARDS_DIR, f"{slug}.svg"), "w", encoding="utf-8") as f:
            f.write(svg_out)

    # Row 2: 2 cards (440 x 116)
    r2_w = 440
    r2_h = 116
    inner2_w = r2_w - 2 * pad  # 432
    inner2_h = r2_h - 2 * pad  # 108

    row2_domains = [
        {
            "slug": "domain-04",
            "num": "04",
            "title": "Computer Vision & Document Intelligence",
            "summary": "Object detection, CNN scientific image segmentation, and end-to-end OCR document parsing pipelines.",
            "tags": ["YOLOv8 (92% acc)", "OCR (96% acc)", "CLIP Retrieval", "IIT Dhanbad"],
            "delay": 1.0,
        },
        {
            "slug": "domain-05",
            "num": "05",
            "title": "Quantitative Research & Financial Modelling",
            "summary": "Statistical alpha signal discovery, multi-year equity backtesting, and systematic variance reduction.",
            "tags": ["Alpha Signals", "Sharpe > 1.5", "-22% Variance", "WorldQuant"],
            "delay": 2.2,
        }
    ]

    for d in row2_domains:
        summary_lines = wrap_text(d["summary"], 54)
        slug = d["slug"]
        delay = d["delay"]
        chips_svg = render_chips(pad + 18, pad + inner2_h - 24, d["tags"], pad + inner2_w - 16)
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

    <path d="M {pad + inner2_w - 34} {pad + 12} L {pad + inner2_w - 12} {pad + 12} M {pad + inner2_w - 12} {pad + 12} L {pad + inner2_w - 12} {pad + 32}"
          fill="none" stroke="{COBALT}" stroke-width="1.2" stroke-opacity="0.45"/>
    <circle class="live" style="animation-delay:{delay * 0.5:.1f}s" cx="{pad + inner2_w - 12}" cy="{pad + 12}" r="2.2" fill="{COBALT}"/>

    <text x="{pad + 18}" y="{pad + 24}" font-family="'Geist Mono', monospace" font-size="10.5" font-weight="600" fill="{COBALT}">{d['num']} //</text>
    <text x="{pad + 52}" y="{pad + 24}" font-family="'Geist', sans-serif" font-weight="600" font-size="13.5" fill="{INK}">{escape(d['title'])}</text>
    <text class="n" style="animation-delay:{delay * 0.4:.1f}s" x="{pad + inner2_w - 40}" y="{pad + 24}" font-family="'Geist Mono', monospace" font-size="11.5" fill="{COBALT}">&#8599;</text>

    {render_lines(pad + 18, pad + 45, summary_lines, 15.5, f'font-family="\'Geist\', sans-serif" font-size="11.5" fill="{INK_SOFT}"')}

    <!-- Crisp Micro-Chip Tags -->
    <g>{chips_svg}</g>
  </g>
"""
        svg_out = make_card_svg(
            r2_w, r2_h, body,
            font_keys=["sans", "sans-b", "mono"],
            label=f"Research Direction {d['num']}: {d['title']}"
        )
        with open(os.path.join(CARDS_DIR, f"{slug}.svg"), "w", encoding="utf-8") as f:
            f.write(svg_out)

    print("wrote cards/domain-01..05.svg (with micro-chip tags)")


# ==============================================================================
# 3. THREE FEATURED PROJECT CARDS WITH ANIMATED SCIENTIFIC MICRO-VISUALS
# ==============================================================================
def render_three_featured_projects():
    tile_w = 293
    tile_h = 172
    pad = 4
    inner_w = tile_w - 2 * pad  # 285
    inner_h = tile_h - 2 * pad  # 164

    # Animated domain-specific scientific micro-motifs positioned top-right (origin 0,0, ~56x20)
    motifs = {
        "physiofm": f"""
      <!-- Animated rPPG Physiological Waveform -->
      <path d="M 0 11 L 10 11 L 14 4 L 18 17 L 23 1 L 28 15 L 32 11 L 46 11"
            fill="none" stroke="{COBALT}" stroke-opacity="0.22" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/>
      <path d="M 0 11 L 10 11 L 14 4 L 18 17 L 23 1 L 28 15 L 32 11 L 46 11"
            fill="none" stroke="{COBALT}" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"
            stroke-dasharray="28 60">
        <animate attributeName="stroke-dashoffset" from="88" to="0" dur="2.6s" repeatCount="indefinite"/>
      </path>
        """,
        "digital-twins": """
      <!-- Animated Connected Urban Transit Digital Twin Graph -->
      <path d="M 4 14 L 22 4 L 42 13 M 4 14 L 42 13" fill="none" stroke="#00A896" stroke-opacity="0.35" stroke-width="1.1"/>
      <circle cx="4" cy="14" r="2.3" fill="#00A896"/>
      <circle cx="22" cy="4" r="2.3" fill="#00A896"/>
      <circle cx="42" cy="13" r="2.3" fill="#00A896"/>
      <circle r="2" fill="#00C2A8">
        <animateMotion dur="3.2s" repeatCount="indefinite" path="M 4 14 L 22 4 L 42 13 L 4 14"/>
      </circle>
        """,
        "vlm-security": f"""
      <!-- Animated RGBA-to-RGB Alpha-Layer Semantic Drift Motif -->
      <rect x="6" y="3" width="16" height="12" rx="2" fill="none" stroke="{VIOLET}" stroke-opacity="0.4" stroke-width="1.1"/>
      <rect x="14" y="6" width="16" height="12" rx="2" fill="{VIOLET}" fill-opacity="0.14" stroke="{VIOLET}" stroke-width="1.2">
        <animateTransform attributeName="transform" type="translate" values="0 0; 6 -2; 0 0" dur="3.4s" repeatCount="indefinite"/>
      </rect>
      <circle cx="38" cy="10" r="2" fill="{VIOLET}" class="live"/>
        """
    }

    projects = [
        {
            "id": "physiofm",
            "name": "PhysioFM",
            "subtitle": "rPPG Foundation Model",
            "desc": "Hierarchical Swin-V2 + STDS framework diagnosing optimization mode collapse in continuous physiological waveforms.",
            "tech": "Swin-V2 · STDS · UBFC-rPPG · SHMS",
            "color": COBALT,
            "pill_bg": "#E7EDFF",
            "delay": 0.3,
        },
        {
            "id": "digital-twins",
            "name": "Urban Digital Twins",
            "subtitle": "Smart Mobility & Transit Testbeds",
            "desc": "GIS-integrated Unity 3D twin of a 25 km Jaipur corridor coupling SUMO traffic with edge YOLO (18% peak load cut).",
            "tech": "SUMO · Unity 3D · YOLO · IMPACT",
            "color": "#009E8C",
            "pill_bg": "#E3F6F3",
            "delay": 1.5,
        },
        {
            "id": "vlm-security",
            "name": "Semantic Drift in VLMs",
            "subtitle": "Preprocessing Attack (IGI Global)",
            "desc": "Exposing RGBA-to-RGB alpha-channel flattening vulnerabilities in VLMs with SEV defense verification (Accepted Chapter).",
            "tech": "VLM Security · SEV · DOI: 10.4018",
            "color": VIOLET,
            "pill_bg": "#EFE9FF",
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

      <!-- Subtitle + Subtle Animated Scientific Micro-Diagram -->
      <text x="{pad + 16}" y="{pad + 44}" font-family="'Geist Mono', monospace" font-size="9.2" fill="{MUTED}">{escape(p['subtitle'])}</text>
      <g transform="translate({pad + inner_w - 64}, {pad + 32})">
        {motifs[pid]}
      </g>

      <!-- Description -->
      {render_lines(pad + 16, pad + 65, desc_lines, 15, f'font-family="\'Geist\', sans-serif" font-size="11" fill="{INK_SOFT}"')}

      <!-- Tinted Tech Pill Strip -->
      <rect x="{pad + 16}" y="{pad + inner_h - 27}" width="{inner_w - 32}" height="19" rx="5" fill="{p['pill_bg']}"/>
      <text x="{pad + inner_w / 2:.1f}" y="{pad + inner_h - 14.2:.1f}" text-anchor="middle" font-family="'Geist Mono', monospace" font-size="9.2" font-weight="600" fill="{c}">{escape(p['tech'])}</text>
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
        print(f"wrote cards/project-{pid}.svg (with animated micro-diagram)")


# ==============================================================================
# 3B. CRISP LOCAL EDITORIAL STATUS BADGES FOR PUBLICATIONS TABLE (NEVER WRAP)
# ==============================================================================
def render_status_badges():
    badges = [
        ("accepted", "ACCEPTED · DOI", 118, "#1E46E8", "#E8EEFF", "#B8CAFF"),
        ("published", "PUBLISHED", 96, "#00897B", "#E2F6F3", "#A6E3DA"),
        ("award", "★ BEST PAPER", 114, "#B45309", "#FEF3C7", "#FCD34D"),
        ("review", "UNDER REVIEW", 112, "#374151", "#F3F4F6", "#D1D5DB"),
        ("presented", "PRESENTED", 96, "#7C3AED", "#EFE9FF", "#C4B5FD"),
    ]
    bh = 24
    for slug, text, bw, fg, bg, border in badges:
        dot = "" if text.startswith("★") else f'<circle cx="11" cy="{bh / 2:.1f}" r="3" fill="{fg}"/>'
        tx = bw / 2 if text.startswith("★") else (bw / 2 + 5)
        body = f"""
  <rect x="0.75" y="0.75" width="{bw - 1.5}" height="{bh - 1.5}" rx="12" fill="{bg}" stroke="{border}" stroke-width="1"/>
  {dot}
  <text x="{tx:.1f}" y="15.6" text-anchor="middle" font-family="'Geist Mono', monospace" font-size="9.8" font-weight="600" letter-spacing="0.3" fill="{fg}">
    {escape(text)}
  </text>
"""
        svg_out = make_card_svg(bw, bh, body, font_keys=["mono"], label=text)
        with open(os.path.join(CARDS_DIR, f"badge-{slug}.svg"), "w", encoding="utf-8") as f:
            f.write(svg_out)
    print("wrote cards/badge-*.svg (5 crisp publication status badges)")


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
    print("wrote cards/research-timeline.svg")


# ==============================================================================
# 5. INDEXED SWISS EDITORIAL SECTION HEADERS (880 x 34) + ANIMATED FOOTER BAR
# ==============================================================================
def render_section_title(slug, index_num, title, italic, badge, dark_fg="#E6EDF3", light_fg=INK):
    for theme, fg, rule_c, muted_c in [
        ("light", light_fg, "#DCDCD7", "#6E6E73"),
        ("dark", dark_fg, "#30363D", "#8B949E"),
    ]:
        approx_text_w = 46 + int((len(title) + len(italic) + 1) * 11.4)
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


def render_footer_bar():
    body = f"""
  <defs>
    <linearGradient id="foot-pulse" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="220" y2="0">
      <stop offset="0" stop-color="{COBALT}" stop-opacity="0"/>
      <stop offset=".5" stop-color="{COBALT}" stop-opacity="0.95"/>
      <stop offset=".75" stop-color="{CYAN}" stop-opacity="1"/>
      <stop offset="1" stop-color="{CYAN}" stop-opacity="0"/>
      <animateTransform attributeName="gradientTransform" type="translate"
        values="-220 0; 960 0" dur="5.5s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>
  <rect x="0" y="2.5" width="{W}" height="1" fill="{COBALT}" fill-opacity="0.22"/>
  <rect x="0" y="2" width="{W}" height="2" rx="1" fill="url(#foot-pulse)"/>
"""
    svg_out = make_card_svg(W, 6, body, font_keys=[], label="Editorial footer accent bar")
    with open(os.path.join(CARDS_DIR, "footer-bar.svg"), "w", encoding="utf-8") as f:
        f.write(svg_out)
    print("wrote cards/footer-bar.svg")


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
    render_status_badges()
    render_timeline()
    render_all_titles()
    render_footer_bar()
    print("Rendered Master Revision V3.4 cards successfully.")


if __name__ == "__main__":
    main()
