#!/usr/bin/env python3
"""
Render all custom SVG cards for Shashwat Upadhyay's GitHub Profile README (Version 2.0).

Compact, editorial layout:
- cards/hero.svg (880x310 compact hero with real blue-duotone scanline portrait)
- cards/research-map.svg (880x220 compact 2x2 research grid with coordinate motifs)
- cards/project-physiofm.svg (horizontal card 1 of 3)
- cards/project-digital-twins.svg (horizontal card 2 of 3)
- cards/project-vlm-security.svg (horizontal card 3 of 3)
- cards/research-timeline.svg (880x110 slim academic milestone strip)
- cards/title-*.svg (clean section headers)
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
# 1. COMPACT HERO CARD (880 x 310)
# ==============================================================================
def render_hero():
    h = 310
    
    # Load processed portrait SVG content
    portrait_inner = ""
    if os.path.exists(PORTRAIT_SVG):
        with open(PORTRAIT_SVG, "r", encoding="utf-8") as pf:
            p_content = pf.read()
            m = re.search(r"<svg[^>]*>(.*?)</svg>", p_content, re.DOTALL)
            if m:
                portrait_inner = m.group(1)

    profile_data = load_json("profile.json")
    links = profile_data.get("links", {})

    body = f"""
  <defs>
    <linearGradient id="text-sheen" gradientUnits="userSpaceOnUse" x1="0" y1="0" x2="600" y2="0">
      <stop offset="0" stop-color="{INK}"/>
      <stop offset=".4" stop-color="{INK}"/>
      <stop offset=".5" stop-color="{COBALT}"/>
      <stop offset=".6" stop-color="{INK}"/>
      <stop offset="1" stop-color="{INK}"/>
      <animateTransform attributeName="gradientTransform" type="translate" 
        values="-600 0;600 0;600 0" keyTimes="0;.45;1" dur="7s" begin="1.5s" repeatCount="indefinite"/>
    </linearGradient>
  </defs>

  <!-- Card Canvas -->
  <rect width="{W}" height="{h}" rx="12" fill="{PAPER}" stroke="{RULE}" stroke-width="1"/>

  <!-- Left Column: Typography & Links -->
  <!-- Technical Identifier -->
  <g>
    <circle class="live" cx="44" cy="40" r="3.5" fill="{COBALT}"/>
    <text x="56" y="44" font-family="'Geist Mono', monospace" font-size="10.5" letter-spacing="1.2" fill="{MUTED}">
      INDEPENDENT AI RESEARCHER // MULTIMODAL SYSTEMS
    </text>
  </g>

  <!-- Editorial Headline Name -->
  <text x="40" y="118" 
        font-family="'Instrument Serif', Georgia, serif" font-size="74" letter-spacing="-1" fill="{INK}">
    Shashwat
  </text>
  <text x="40" y="184" 
        font-family="'Instrument Serif', Georgia, serif" font-style="italic" font-size="74" letter-spacing="-1" fill="url(#text-sheen)">
    Upadhyay.
  </text>

  <!-- Tagline & Core Statement -->
  <g>
    <text x="44" y="218" font-family="'Geist', sans-serif" font-weight="600" font-size="14.5" fill="{INK_SOFT}">
      Researching intelligence. Building systems.
    </text>
    <text x="44" y="238" font-family="'Geist', sans-serif" font-size="12.5" fill="{MUTED}">
      Multimodal AI · Computer Vision · Digital Twins · ML Security
    </text>
    <text x="44" y="258" font-family="'Geist Mono', monospace" font-size="11" fill="{MUTED}">
      BVoc Cyber Security (SAKEC) · BS Data Science (IIT Madras)
    </text>
  </g>

  <!-- Editorial Separator -->
  <line x1="44" y1="274" x2="610" y2="274" stroke="{RULE}" stroke-width="0.8"/>

  <!-- Clickable Professional Links -->
  <g font-family="'Geist Mono', monospace" font-size="11" fill="{INK}">
    <text x="44" y="295">GitHub</text>
    <text class="n" x="84" y="295" fill="{COBALT}">&#8599;</text>
    
    <text x="108" y="295" fill="{MUTED}">·</text>
    <text x="122" y="295">LinkedIn</text>
    <text class="n" x="174" y="295" fill="{COBALT}">&#8599;</text>

    <text x="198" y="295" fill="{MUTED}">·</text>
    <text x="212" y="295">ResearchGate</text>
    <text class="n" x="296" y="295" fill="{COBALT}">&#8599;</text>

    <text x="320" y="295" fill="{MUTED}">·</text>
    <text x="334" y="295">Publications</text>
    <text class="n" x="414" y="295" fill="{COBALT}">&#8599;</text>

    <text x="438" y="295" fill="{MUTED}">·</text>
    <text x="452" y="295">Email</text>
    <text class="n" x="486" y="295" fill="{COBALT}">&#8599;</text>
  </g>

  <!-- Right Column: Real Blue-Duotone Scanline Portrait (200 x 245) -->
  <g transform="translate(642, 28)">
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
# 2. COMPACT RESEARCH MAP (4 DOMAINS IN 2x2 GRID, 880 x 220)
# ==============================================================================
def render_research_map():
    h = 244
    col_w = (W - 36) / 2  # 422px
    row_h = 106
    
    research_data = load_json("research.json")
    domains = research_data.get("domains", [])

    cards_svg = []
    for idx, d in enumerate(domains[:4]):
        col = idx % 2
        row = idx // 2
        cx = 12 + col * (col_w + 12)
        cy = 10 + row * (row_h + 12)

        foci_text = " · ".join(d.get("foci", [])[:3])
        summary_lines = wrap_text(d.get('summary', ''), 46)

        cards_svg.append(f"""
    <g transform="translate({cx:.1f}, {cy:.1f})">
      <rect width="{col_w:.1f}" height="{row_h}" rx="8" fill="{PAPER}" stroke="{RULE}" stroke-width="1"/>
      
      <!-- Subtle Technical XY Grid Motif in Corner -->
      <path d="M {col_w-36:.1f} 14 L {col_w-14:.1f} 14 M {col_w-14:.1f} 14 L {col_w-14:.1f} 36" 
            fill="none" stroke="{COBALT}" stroke-width="1.2" stroke-opacity="0.5"/>
      <circle cx="{col_w-14:.1f}" cy="14" r="2" fill="{COBALT}"/>

      <!-- Header Number & Title -->
      <text x="18" y="24" font-family="'Geist Mono', monospace" font-size="10.5" font-weight="600" fill="{COBALT}">{d.get('number', '01')} //</text>
      <text x="50" y="24" font-family="'Geist', sans-serif" font-weight="600" font-size="13.5" fill="{INK}">{escape(d.get('title', ''))}</text>
      <text class="n" x="{col_w - 46:.1f}" y="24" font-family="'Geist Mono', monospace" font-size="12" fill="{COBALT}">&#8599;</text>
      
      <!-- Concise 2-line description -->
      {render_lines(18, 44, summary_lines[:2], 16, f'font-family="\'Geist\', sans-serif" font-size="11.5" fill="{INK_SOFT}"')}
      
      <!-- Focus technical labels -->
      <line x1="18" y1="{row_h - 26}" x2="{col_w - 18:.1f}" y2="{row_h - 26}" stroke="{RULE}" stroke-width="0.7"/>
      <text x="18" y="{row_h - 11}" font-family="'Geist Mono', monospace" font-size="9.5" fill="{MUTED}">{escape(foci_text)}</text>
    </g>
        """)

    body = f"""
  <rect width="{W}" height="{h}" rx="10" fill="none"/>
  {''.join(cards_svg)}
"""

    svg_out = make_card_svg(
        W, h, body,
        font_keys=["sans", "sans-b", "mono"],
        label="Four Core Research Directions: Multimodal AI, Digital Twins, ML Security, Document Intelligence"
    )
    with open(os.path.join(CARDS_DIR, "research-map.svg"), "w", encoding="utf-8") as f:
        f.write(svg_out)
    print("wrote cards/research-map.svg")

# ==============================================================================
# 3. THREE COMPACT FEATURED PROJECT CARDS (ROW OF 3, ~285px EACH)
# ==============================================================================
def render_three_featured_projects():
    tile_w = (W - 24) / 3  # 285.33px
    tile_h = 165

    projects = [
        {
            "id": "physiofm",
            "name": "PhysioFM",
            "subtitle": "rPPG Foundation Model",
            "desc": "Hierarchical Swin-V2 + STDS framework diagnosing optimization mode collapse in continuous physiological waveforms.",
            "tech": "Swin-V2 · STDS · UBFC-rPPG",
            "color": COBALT,
            "url": "https://github.com/Shashwatology/PhysioFM"
        },
        {
            "id": "digital-twins",
            "name": "Urban Digital Twins",
            "subtitle": "Smart Mobility Testbeds",
            "desc": "Real-time microscopic traffic simulation testbeds coupling SUMO with Unity 3D and edge YOLO object detection.",
            "tech": "SUMO · Unity 3D · YOLO",
            "color": "#00C2A8",
            "url": "https://github.com/Shashwatology/Guardian-Travel-Twin-"
        },
        {
            "id": "vlm-security",
            "name": "Semantic Drift in VLMs",
            "subtitle": "Preprocessing Attack Surface",
            "desc": "Exposing RGBA-to-RGB alpha-channel flattening vulnerabilities in Vision-Language Models with SEV defense verification.",
            "tech": "VLM Preprocessing · SEV Defense",
            "color": VIOLET,
            "url": "https://github.com/Shashwatology/semantic-drift-vlm-attacks"
        }
    ]

    for idx, p in enumerate(projects):
        body = f"""
  <rect width="{tile_w:.1f}" height="{tile_h}" rx="10" fill="{PAPER}" stroke="{RULE}" stroke-width="1"/>
  
  <g>
    <!-- Header Indicator & Link Arrow -->
    <rect x="20" y="20" width="8" height="8" rx="2" fill="{p['color']}"/>
    <text x="36" y="28" font-family="'Geist', sans-serif" font-weight="600" font-size="15" fill="{INK}">
      {escape(p['name'])}
    </text>
    <text class="n" x="{tile_w - 24:.1f}" y="28" font-family="'Geist Mono', monospace" font-size="12" fill="{p['color']}">&#8599;</text>

    <!-- Subtitle -->
    <text x="20" y="46" font-family="'Geist Mono', monospace" font-size="10" fill="{MUTED}">{escape(p['subtitle'])}</text>

    <!-- Description (wrapped to 2 lines) -->
    {render_lines(20, 72, wrap_text(p['desc'], 34), 18, f'font-family="\'Geist\', sans-serif" font-size="11.5" fill="{INK_SOFT}"')}

    <!-- Divider & Tech Label -->
    <line x1="20" y1="{tile_h - 36}" x2="{tile_w - 20:.1f}" y2="{tile_h - 36}" stroke="{RULE}" stroke-width="0.8"/>
    <text x="20" y="{tile_h - 18}" font-family="'Geist Mono', monospace" font-size="10" fill="{p['color']}">{escape(p['tech'])}</text>
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
# 4. SLIM ACADEMIC MILESTONES STRIP (880 x 100)
# ==============================================================================
def render_timeline():
    w = 880
    h = 100
    
    milestones = [
        ("2022 — Present", "SAKEC", "BVoc Cyber Security"),
        ("2023 — Present", "IIT Madras", "BS Data Science"),
        ("2024", "MNIT Jaipur (AMRUT)", "Research Intern (rPPG)"),
        ("2024", "NIT Warangal", "Research Association"),
    ]

    items_svg = []
    step_x = (w - 40) / len(milestones)
    for i, (period, org, title) in enumerate(milestones):
        x = 24 + i * step_x
        items_svg.append(f"""
    <g>
      <circle cx="{x + 6}" cy="42" r="4" fill="{COBALT}"/>
      <text x="{x + 6}" y="26" font-family="'Geist Mono', monospace" font-size="10" font-weight="600" fill="{COBALT}">{period}</text>
      <text x="{x + 6}" y="62" font-family="'Geist', sans-serif" font-weight="600" font-size="12" fill="{INK}">{escape(org)}</text>
      <text x="{x + 6}" y="78" font-family="'Geist', sans-serif" font-size="11" fill="{MUTED}">{escape(title)}</text>
    </g>
        """)

    body = f"""
  <rect width="{w}" height="{h}" rx="8" fill="{PAPER}" stroke="{RULE}" stroke-width="1"/>
  <line x1="24" y1="42" x2="{w - 24}" y2="42" stroke="{RULE}" stroke-width="1"/>
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
        ("connect", "Connect &", "Collaborate")
    ]
    for slug, t, it in titles:
        render_section_title(slug, t, it)
    print("wrote title SVGs")

def main():
    os.makedirs(CARDS_DIR, exist_ok=True)
    render_hero()
    render_research_map()
    render_three_featured_projects()
    render_timeline()
    render_all_titles()
    print("Rendered Version 2.0 cards successfully.")

if __name__ == "__main__":
    main()
