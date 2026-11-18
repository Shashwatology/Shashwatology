#!/usr/bin/env python3
"""
Render all custom SVG cards for Shashwat Upadhyay's GitHub Profile README (Master Revision V3.1).

Every interactive card is rendered as an individual SVG so that 100% of links in README.md
are natively clickable on GitHub:
- cards/hero.svg (880x295 compact hero with permanent cobalt #315EFF Upadhyay + cyan sweep)
- cards/nav-*.svg (5 individual clickable top quick-link buttons: GitHub, Scholar, LinkedIn, ResearchGate, Email)
- cards/domain-01..05.svg (5 individual clickable research direction cards, zero text clipping/truncation)
- cards/project-*.svg (3 individual clickable featured project cards with clean gutters)
- cards/research-timeline.svg (880x110 accurate 6-milestone academic & research strip)
- cards/title-*.svg (clean light/dark adaptive section headers)
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
# 1. COMPACT HERO CARD (880 x 296)
# ==============================================================================
def render_hero():
    h = 296
    
    # Load processed portrait SVG content
    portrait_inner = ""
    if os.path.exists(PORTRAIT_SVG):
        with open(PORTRAIT_SVG, "r", encoding="utf-8") as pf:
            p_content = pf.read()
            m = re.search(r"<svg[^>]*>(.*?)</svg>", p_content, re.DOTALL)
            if m:
                portrait_inner = m.group(1)

    # Surname Upadhyay is permanently Cobalt Blue (#315EFF) with an animated cyan sheen sweep (#7DDFFF)
    body = f"""
  <defs>
    <linearGradient id="upadhyay-blue" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="450" y2="0">
      <stop offset="0" stop-color="{COBALT}"/>
      <stop offset=".35" stop-color="{COBALT}"/>
      <stop offset=".5" stop-color="{CYAN}"/>
      <stop offset=".65" stop-color="{COBALT}"/>
      <stop offset="1" stop-color="{COBALT}"/>
      <animateTransform attributeName="gradientTransform" type="translate" 
        values="-450 0; 450 0; 450 0" keyTimes="0;.45;1" dur="6s" begin="1s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>

  <!-- Card Canvas -->
  <rect width="{W}" height="{h}" rx="12" fill="{PAPER}" stroke="{RULE}" stroke-width="1"/>

  <!-- Left Column: Typography & Verified Credentials -->
  <!-- Technical Identifier -->
  <g>
    <circle class="live" cx="44" cy="36" r="3.5" fill="{COBALT}"/>
    <text x="56" y="40" font-family="'Geist Mono', monospace" font-size="10.5" letter-spacing="1.2" fill="{MUTED}">
      INDEPENDENT AI RESEARCHER // MULTIMODAL SYSTEMS
    </text>
  </g>

  <!-- Editorial Headline Name -->
  <text x="40" y="112" 
        font-family="'Instrument Serif', Georgia, serif" font-size="74" letter-spacing="-1" fill="{INK}">
    Shashwat
  </text>
  <text x="40" y="176" 
        font-family="'Instrument Serif', Georgia, serif" font-style="italic" font-size="74" letter-spacing="-1" fill="url(#upadhyay-blue)">
    Upadhyay.
  </text>

  <!-- Tagline & Core Statement Grounded in Resume -->
  <g>
    <text x="44" y="208" font-family="'Geist', sans-serif" font-weight="600" font-size="14.5" fill="{INK_SOFT}">
      Researching intelligence. Building systems.
    </text>
    <text x="44" y="228" font-family="'Geist', sans-serif" font-size="12.5" fill="{MUTED}">
      Multimodal AI · Computer Vision · Digital Twins · ML Security · Quant
    </text>
    <text x="44" y="248" font-family="'Geist Mono', monospace" font-size="10.8" fill="{MUTED}">
      BVoc Cyber Security (SAKEC, 2024–2028) · BS Data Science (IIT Madras, 2023–2028)
    </text>
  </g>

  <!-- Editorial Separator -->
  <line x1="44" y1="262" x2="610" y2="262" stroke="{RULE}" stroke-width="0.8"/>

  <!-- Research Affiliations Strip (Real clickable links are rendered directly below as individual SVG buttons) -->
  <text x="44" y="280" font-family="'Geist Mono', monospace" font-size="10" letter-spacing="0.4" fill="{MUTED}">
    <tspan fill="{COBALT}" font-weight="600">AFFILIATIONS //</tspan> MNIT Jaipur (MoHUA) · IIT (ISM) Dhanbad · WorldQuant · Mumbai, India
  </text>

  <!-- Right Column: Real Blue-Duotone Scanline Portrait (200 x 245) -->
  <g transform="translate(642, 24)">
    <g transform="scale(0.95)">
      {portrait_inner}
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
# 1B. FIVE INDIVIDUAL CLICKABLE HERO QUICK-LINK PILLS (176 x 38 EACH)
# ==============================================================================
def render_nav_links():
    items = [
        ("github", "GitHub"),
        ("scholar", "Google Scholar"),
        ("linkedin", "LinkedIn"),
        ("researchgate", "ResearchGate"),
        ("email", "Email"),
    ]
    pw = 176
    ph = 38

    for slug, label in items:
        body = f"""
  <rect x="3" y="3" width="{pw - 6}" height="{ph - 6}" rx="7" fill="{PAPER}" stroke="{RULE}" stroke-width="1"/>
  <text x="{pw / 2 - 6:.1f}" y="23" text-anchor="middle" font-family="'Geist Mono', monospace" font-size="11" font-weight="600" fill="{INK}">
    {escape(label)}
  </text>
  <text class="n" x="{pw - 18}" y="23" text-anchor="end" font-family="'Geist Mono', monospace" font-size="11.5" fill="{COBALT}">&#8599;</text>
"""
        svg_out = make_card_svg(
            pw, ph, body,
            font_keys=["mono"],
            label=f"Open Shashwat Upadhyay's {label}"
        )
        with open(os.path.join(CARDS_DIR, f"nav-{slug}.svg"), "w", encoding="utf-8") as f:
            f.write(svg_out)
    print("wrote cards/nav-*.svg (5 individual clickable nav buttons)")

# ==============================================================================
# 2. FIVE INDIVIDUAL CLICKABLE RESEARCH DOMAIN CARDS (Zero truncation/overflow)
# ==============================================================================
def render_research_domains():
    # Row 1: 3 cards (293 x 162 each, rendered side-by-side at width="33.333%")
    r1_w = 293
    r1_h = 162
    pad = 4
    inner_w = r1_w - 2 * pad  # 285
    inner_h = r1_h - 2 * pad  # 154

    row1_domains = [
        {
            "slug": "domain-01",
            "num": "01",
            "title_1": "Multimodal AI &",
            "title_2": "Physiological Computing",
            "summary": "Non-contact vital monitoring via video, spatial-temporal models, and multimodal sensor fusion.",
            "foci": "PhysioFM · rPPG · WardOS · Fusion",
        },
        {
            "slug": "domain-02",
            "num": "02",
            "title_1": "Intelligent Infrastructure",
            "title_2": "& Digital Twins",
            "summary": "Synchronized 3D simulation testbeds and edge computer vision for connected urban transit.",
            "foci": "IMPACT · SUMO · Unity 3D · YOLO",
        },
        {
            "slug": "domain-03",
            "num": "03",
            "title_1": "Trustworthy AI &",
            "title_2": "ML Security",
            "summary": "Auditing VLM preprocessing attack surfaces, alpha-channel drift, and zero-label behavioral risk.",
            "foci": "VLM Security · SEV · SentinelAI",
        }
    ]

    for d in row1_domains:
        summary_lines = wrap_text(d["summary"], 35)
        body = f"""
  <rect x="{pad}" y="{pad}" width="{inner_w}" height="{inner_h}" rx="8" fill="{PAPER}" stroke="{RULE}" stroke-width="1"/>
  
  <!-- Header number & arrow -->
  <text x="{pad + 16}" y="{pad + 24}" font-family="'Geist Mono', monospace" font-size="10" font-weight="600" fill="{COBALT}">{d['num']} //</text>
  <text class="n" x="{pad + inner_w - 18}" y="{pad + 24}" text-anchor="end" font-family="'Geist Mono', monospace" font-size="11.5" fill="{COBALT}">&#8599;</text>

  <!-- 2-line title -->
  <text x="{pad + 16}" y="{pad + 43}" font-family="'Geist', sans-serif" font-weight="600" font-size="13.5" fill="{INK}">{escape(d['title_1'])}</text>
  <text x="{pad + 16}" y="{pad + 60}" font-family="'Geist', sans-serif" font-weight="600" font-size="13.5" fill="{INK}">{escape(d['title_2'])}</text>

  <!-- Complete 3-line summary (never truncated) -->
  {render_lines(pad + 16, pad + 80, summary_lines, 15, f'font-family="\'Geist\', sans-serif" font-size="11" fill="{INK_SOFT}"')}

  <!-- Divider & technical tags -->
  <line x1="{pad + 16}" y1="{pad + inner_h - 28}" x2="{pad + inner_w - 16}" y2="{pad + inner_h - 28}" stroke="{RULE}" stroke-width="0.7"/>
  <text x="{pad + 16}" y="{pad + inner_h - 11}" font-family="'Geist Mono', monospace" font-size="9.5" fill="{MUTED}">{escape(d['foci'])}</text>
"""
        svg_out = make_card_svg(
            r1_w, r1_h, body,
            font_keys=["sans", "sans-b", "mono"],
            label=f"Research Direction {d['num']}: {d['title_1']} {d['title_2']}"
        )
        with open(os.path.join(CARDS_DIR, f"{d['slug']}.svg"), "w", encoding="utf-8") as f:
            f.write(svg_out)

    # Row 2: 2 cards (440 x 140 each, rendered side-by-side at width="50%")
    r2_w = 440
    r2_h = 140
    inner2_w = r2_w - 2 * pad  # 432
    inner2_h = r2_h - 2 * pad  # 132

    row2_domains = [
        {
            "slug": "domain-04",
            "num": "04",
            "title": "Computer Vision & Document Intelligence",
            "summary": "Object detection, CNN scientific image segmentation, and end-to-end OCR document parsing pipelines.",
            "foci": "YOLOv8 12k+ (92% acc) · OCR (96% acc) · CLIP",
        },
        {
            "slug": "domain-05",
            "num": "05",
            "title": "Quantitative Research & Financial Modelling",
            "summary": "Statistical alpha signal discovery, multi-year equity backtesting, and systematic variance reduction.",
            "foci": "Alpha Signals · Sharpe > 1.5 · 22% Variance Cut",
        }
    ]

    for d in row2_domains:
        summary_lines = wrap_text(d["summary"], 54)
        body = f"""
  <rect x="{pad}" y="{pad}" width="{inner2_w}" height="{inner2_h}" rx="8" fill="{PAPER}" stroke="{RULE}" stroke-width="1"/>
  
  <!-- Subtle Technical XY Grid Motif in Corner -->
  <path d="M {pad + inner2_w - 36} {pad + 14} L {pad + inner2_w - 14} {pad + 14} M {pad + inner2_w - 14} {pad + 14} L {pad + inner2_w - 14} {pad + 36}" 
        fill="none" stroke="{COBALT}" stroke-width="1.2" stroke-opacity="0.45"/>
  <circle cx="{pad + inner2_w - 14}" cy="{pad + 14}" r="2" fill="{COBALT}"/>

  <!-- Header Number & Title -->
  <text x="{pad + 18}" y="{pad + 27}" font-family="'Geist Mono', monospace" font-size="10.5" font-weight="600" fill="{COBALT}">{d['num']} //</text>
  <text x="{pad + 52}" y="{pad + 27}" font-family="'Geist', sans-serif" font-weight="600" font-size="13.5" fill="{INK}">{escape(d['title'])}</text>
  <text class="n" x="{pad + inner2_w - 42}" y="{pad + 27}" font-family="'Geist Mono', monospace" font-size="11.5" fill="{COBALT}">&#8599;</text>

  <!-- Complete 2-line description -->
  {render_lines(pad + 18, pad + 52, summary_lines, 17, f'font-family="\'Geist\', sans-serif" font-size="11.5" fill="{INK_SOFT}"')}

  <!-- Divider & focus tags (generous right margin) -->
  <line x1="{pad + 18}" y1="{pad + inner2_h - 28}" x2="{pad + inner2_w - 18}" y2="{pad + inner2_h - 28}" stroke="{RULE}" stroke-width="0.7"/>
  <text x="{pad + 18}" y="{pad + inner2_h - 11}" font-family="'Geist Mono', monospace" font-size="9.5" fill="{MUTED}">{escape(d['foci'])}</text>
"""
        svg_out = make_card_svg(
            r2_w, r2_h, body,
            font_keys=["sans", "sans-b", "mono"],
            label=f"Research Direction {d['num']}: {d['title']}"
        )
        with open(os.path.join(CARDS_DIR, f"{d['slug']}.svg"), "w", encoding="utf-8") as f:
            f.write(svg_out)

    print("wrote cards/domain-01..05.svg (5 individual clickable research direction cards)")

# ==============================================================================
# 3. THREE COMPACT FEATURED PROJECT CARDS (ROW OF 3, 293 x 186 EACH WITH GUTTERS)
# ==============================================================================
def render_three_featured_projects():
    tile_w = 293
    tile_h = 186
    pad = 4
    inner_w = tile_w - 2 * pad  # 285
    inner_h = tile_h - 2 * pad  # 178

    projects = [
        {
            "id": "physiofm",
            "name": "PhysioFM",
            "subtitle": "rPPG Foundation Model",
            "desc": "Hierarchical Swin-V2 + STDS framework diagnosing optimization mode collapse in continuous physiological waveforms.",
            "tech": "Swin-V2 · STDS · UBFC-rPPG · SHMS",
            "color": COBALT,
        },
        {
            "id": "digital-twins",
            "name": "Urban Digital Twins",
            "subtitle": "Smart Mobility & Transit Testbeds",
            "desc": "GIS-integrated Unity 3D twin of a 25 km Jaipur corridor coupling SUMO traffic with edge YOLO (18% peak load cut).",
            "tech": "SUMO · Unity 3D · YOLO · IMPACT",
            "color": "#00C2A8",
        },
        {
            "id": "vlm-security",
            "name": "Semantic Drift in VLMs",
            "subtitle": "Preprocessing Attack Surface (IGI Global)",
            "desc": "Exposing RGBA-to-RGB alpha-channel flattening vulnerabilities in VLMs with SEV defense verification (Accepted Chapter).",
            "tech": "VLM Security · SEV · DOI: 10.4018",
            "color": VIOLET,
        }
    ]

    for p in projects:
        desc_lines = wrap_text(p["desc"], 34)
        body = f"""
  <rect x="{pad}" y="{pad}" width="{inner_w}" height="{inner_h}" rx="10" fill="{PAPER}" stroke="{RULE}" stroke-width="1"/>
  
  <g>
    <!-- Header Indicator & Link Arrow -->
    <rect x="{pad + 18}" y="{pad + 20}" width="8" height="8" rx="2" fill="{p['color']}"/>
    <text x="{pad + 34}" y="{pad + 28}" font-family="'Geist', sans-serif" font-weight="600" font-size="14.5" fill="{INK}">
      {escape(p['name'])}
    </text>
    <text class="n" x="{pad + inner_w - 18}" y="{pad + 28}" text-anchor="end" font-family="'Geist Mono', monospace" font-size="12" fill="{p['color']}">&#8599;</text>

    <!-- Subtitle -->
    <text x="{pad + 18}" y="{pad + 46}" font-family="'Geist Mono', monospace" font-size="9.5" fill="{MUTED}">{escape(p['subtitle'])}</text>

    <!-- Description (max 4 lines with clean bottom breathing space) -->
    {render_lines(pad + 18, pad + 68, desc_lines, 16, f'font-family="\'Geist\', sans-serif" font-size="11" fill="{INK_SOFT}"')}

    <!-- Divider & Tech Label -->
    <line x1="{pad + 18}" y1="{pad + inner_h - 32}" x2="{pad + inner_w - 18}" y2="{pad + inner_h - 32}" stroke="{RULE}" stroke-width="0.8"/>
    <text x="{pad + 18}" y="{pad + inner_h - 14}" font-family="'Geist Mono', monospace" font-size="9.5" fill="{p['color']}">{escape(p['tech'])}</text>
  </g>
"""
        svg_out = make_card_svg(
            tile_w, tile_h, body,
            font_keys=["sans", "sans-b", "mono"],
            label=f"{p['name']}: {p['subtitle']}"
        )
        with open(os.path.join(CARDS_DIR, f"project-{p['id']}.svg"), "w", encoding="utf-8") as f:
            f.write(svg_out)
        print(f"wrote cards/project-{p['id']}.svg")

# ==============================================================================
# 4. SLIM ACADEMIC & RESEARCH MILESTONES STRIP (880 x 110)
# ==============================================================================
def render_timeline():
    w = 880
    h = 110
    
    # 6 accurate milestones directly from resume
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
        items_svg.append(f"""
    <g>
      <circle cx="{x + 6}" cy="46" r="4" fill="{COBALT}"/>
      <text x="{x + 6}" y="28" font-family="'Geist Mono', monospace" font-size="9.5" font-weight="600" fill="{COBALT}">{period}</text>
      <text x="{x + 6}" y="66" font-family="'Geist', sans-serif" font-weight="600" font-size="11.5" fill="{INK}">{escape(org)}</text>
      <text x="{x + 6}" y="84" font-family="'Geist', sans-serif" font-size="10.5" fill="{MUTED}">{escape(title)}</text>
    </g>
        """)

    body = f"""
  <rect width="{w}" height="{h}" rx="8" fill="{PAPER}" stroke="{RULE}" stroke-width="1"/>
  <line x1="24" y1="46" x2="{w - 24}" y2="46" stroke="{RULE}" stroke-width="1"/>
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
# 5. EDITORIAL SECTION TITLES
# ==============================================================================
def render_section_title(slug, title, italic, dark_fg="#E6EDF3", light_fg=INK):
    for theme, fg in [("light", light_fg), ("dark", dark_fg)]:
        body = f"""
  <text x="2" y="32" 
        font-family="'Instrument Serif', Georgia, serif" font-size="28" fill="{fg}">
    {escape(title)} <tspan font-style="italic" fill="{COBALT}">{escape(italic)}</tspan>
  </text>
"""
        svg_out = make_card_svg(
            W, 44, body,
            font_keys=["serif", "serif-i"],
            label=f"Section: {title} {italic}"
        )
        with open(os.path.join(CARDS_DIR, f"title-{slug}-{theme}.svg"), "w", encoding="utf-8") as f:
            f.write(svg_out)

def render_all_titles():
    titles = [
        ("research", "Research", "Directions"),
        ("projects", "Featured", "Research Projects"),
        ("publications", "Publications &", "Milestones"),
        ("stack", "Technology", "Toolkit"),
        ("activity", "GitHub", "Telemetry & Heatmap"),
        ("repos", "Featured", "Repositories & Codebases"),
        ("connect", "Connect &", "Collaborate")
    ]
    for slug, t, it in titles:
        render_section_title(slug, t, it)
    print("wrote title SVGs")

def main():
    os.makedirs(CARDS_DIR, exist_ok=True)
    render_hero()
    render_nav_links()
    render_research_domains()
    render_three_featured_projects()
    render_timeline()
    render_all_titles()
    print("Rendered Master Revision V3.1 cards successfully.")

if __name__ == "__main__":
    main()
