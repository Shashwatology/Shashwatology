#!/usr/bin/env python3
"""
Render all custom SVG cards for Shashwat Upadhyay's GitHub Profile README.

Cards rendered:
- cards/hero.svg (Hero card with editorial layout and embedded portrait/silhouette)
- cards/research-map.svg (4 Research Directions overview grid)
- cards/research-timeline.svg (Academic and research milestones)
- cards/project-*.svg (PhysioFM, Digital Twins, VLM Security, SentinelAI, BreatheSync)
- cards/repo-*.svg (Top curated repositories)
- cards/title-*.svg (Light and Dark mode section titles)
"""

import os
import json
import re
from html import escape
from svg_utils import (
    make_card_svg, wrap_text, render_lines,
    PAPER, PAPER_MUTED, INK, INK_SOFT, MUTED, RULE,
    COBALT, CYAN, VIOLET, DARK_NAVY, DARK_SURFACE
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
# 1. HERO CARD
# ==============================================================================
def render_hero():
    h = 430
    
    # Load portrait SVG inner content
    portrait_inner = ""
    if os.path.exists(PORTRAIT_SVG):
        with open(PORTRAIT_SVG, "r", encoding="utf-8") as pf:
            p_content = pf.read()
            # Extract everything between <svg ...> and </svg>
            m = re.search(r"<svg[^>]*>(.*?)</svg>", p_content, re.DOTALL)
            if m:
                portrait_inner = m.group(1)

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
    <clipPath id="portrait-frame">
      <rect width="320" height="360" rx="8"/>
    </clipPath>
  </defs>

  <!-- Card Canvas -->
  <rect width="{W}" height="{h}" rx="14" fill="{PAPER}" stroke="{RULE}" stroke-width="1"/>

  <!-- Left Column: Typography & Links -->
  <!-- Status Badge -->
  <g class="f" style="animation-delay:0.1s">
    <rect class="live" x="44" y="44" width="8" height="8" rx="2" fill="{COBALT}"/>
    <text x="60" y="52" font-family="'Geist Mono', monospace" font-size="11.5" letter-spacing="1.2" fill="{MUTED}">
      INDEPENDENT AI RESEARCHER // MULTIMODAL SYSTEMS
    </text>
  </g>

  <!-- Name -->
  <text class="r" style="animation-delay:0.2s" x="40" y="160" 
        font-family="'Instrument Serif', Georgia, serif" font-size="94" letter-spacing="-1.5" fill="{INK}">
    Shashwat
  </text>
  <text class="r" style="animation-delay:0.35s" x="40" y="244" 
        font-family="'Instrument Serif', Georgia, serif" font-style="italic" font-size="94" letter-spacing="-1.5" fill="url(#text-sheen)">
    Upadhyay
  </text>

  <!-- Tagline & Core Statement -->
  <g class="r" style="animation-delay:0.55s">
    <text x="44" y="286" font-family="'Geist', sans-serif" font-weight="600" font-size="16" fill="{INK_SOFT}">
      Researching intelligence. Building systems.
    </text>
    <text x="44" y="310" font-family="'Geist', sans-serif" font-size="14" fill="{MUTED}">
      Multimodal Learning · Computer Vision · Digital Twins · ML Security
    </text>
    <text x="44" y="332" font-family="'Geist Mono', monospace" font-size="11.5" fill="{MUTED}">
      BVoc Cyber Security (SAKEC) &amp; BS Data Science (IIT Madras)
    </text>
  </g>

  <!-- Editorial Separator -->
  <line x1="44" y1="362" x2="510" y2="362" stroke="{RULE}" stroke-width="1"/>

  <!-- Professional Links Row -->
  <g class="f" style="animation-delay:0.8s" font-family="'Geist Mono', monospace" font-size="12" fill="{INK}">
    <text x="44" y="390">github.com/shashwatology</text>
    <text class="n" x="228" y="390" fill="{COBALT}">&#8599;</text>
    
    <text x="256" y="390" fill="{MUTED}">·</text>
    <text x="272" y="390">linkedin</text>
    <text class="n" x="328" y="390" fill="{COBALT}">&#8599;</text>

    <text x="354" y="390" fill="{MUTED}">·</text>
    <text x="370" y="390">researchgate</text>
    <text class="n" x="466" y="390" fill="{COBALT}">&#8599;</text>
  </g>

  <!-- Right Column: Small Monochrome Artistic Portrait / Scientific Silhouette -->
  <g transform="translate(528, 35)">
    <!-- Container Box -->
    <rect width="308" height="360" rx="8" fill="#FAF9F5" stroke="{RULE}" stroke-width="1"/>
    <g transform="scale(0.96) translate(6, 0)">
      {portrait_inner}
    </g>
  </g>
"""

    svg_out = make_card_svg(
        W, h, body,
        font_keys=["serif", "serif-i", "sans", "sans-b", "mono"],
        label="Shashwat Upadhyay — Research in Motion. Independent AI Researcher, Multimodal Learning, Computer Vision, Digital Twins."
    )
    with open(os.path.join(CARDS_DIR, "hero.svg"), "w", encoding="utf-8") as f:
        f.write(svg_out)
    print("wrote cards/hero.svg")

# ==============================================================================
# 2. RESEARCH MAP (4 DOMAINS GRID)
# ==============================================================================
def render_research_map():
    h = 320
    col_w = (W - 36) / 2  # 422px each
    row_h = 135
    
    research_data = load_json("research.json")
    domains = research_data.get("domains", [])

    cards_svg = []
    for idx, d in enumerate(domains[:4]):
        col = idx % 2
        row = idx // 2
        cx = 12 + col * (col_w + 12)
        cy = 20 + row * (row_h + 12)

        delay = 0.2 + idx * 0.1
        foci_text = " · ".join(d.get("foci", [])[:3])

        cards_svg.append(f"""
    <g class="r" style="animation-delay:{delay:.2f}s" transform="translate({cx:.1f}, {cy:.1f})">
      <rect width="{col_w:.1f}" height="{row_h}" rx="8" fill="{PAPER}" stroke="{RULE}" stroke-width="1"/>
      <!-- Header number & title -->
      <text x="20" y="28" font-family="'Geist Mono', monospace" font-size="11" font-weight="600" fill="{COBALT}">{d.get('number', '01')} //</text>
      <text x="56" y="28" font-family="'Geist', sans-serif" font-weight="600" font-size="14.5" fill="{INK}">{escape(d.get('title', ''))}</text>
      <text class="n" x="{col_w - 28:.1f}" y="28" font-family="'Geist Mono', monospace" font-size="13" fill="{COBALT}">&#8599;</text>
      
      <!-- Summary -->
      {render_lines(20, 54, wrap_text(d.get('summary', ''), 44), 18, f'font-family="\'Geist\', sans-serif" font-size="12.5" fill="{INK_SOFT}"')}
      
      <!-- Focus Pills -->
      <line x1="20" y1="102" x2="{col_w - 20:.1f}" y2="102" stroke="{RULE}" stroke-width="0.8"/>
      <text x="20" y="119" font-family="'Geist Mono', monospace" font-size="10" fill="{MUTED}">{escape(foci_text)}</text>
    </g>
        """)

    body = f"""
  <rect width="{W}" height="{h}" rx="12" fill="none"/>
  {''.join(cards_svg)}
"""

    svg_out = make_card_svg(
        W, h, body,
        font_keys=["sans", "sans-b", "mono"],
        label="Research Directions: Multimodal AI, Digital Twins, ML Security, Document Intelligence"
    )
    with open(os.path.join(CARDS_DIR, "research-map.svg"), "w", encoding="utf-8") as f:
        f.write(svg_out)
    print("wrote cards/research-map.svg")

# ==============================================================================
# 3. SELECTED RESEARCH PROJECT CARDS
# ==============================================================================
def render_project_card(card_id, title, subtitle, objective, methods, status, repo_url, accent):
    w = 880
    h = 190

    methods_str = " · ".join(methods)
    body = f"""
  <rect width="{w}" height="{h}" rx="12" fill="{PAPER}" stroke="{RULE}" stroke-width="1"/>
  
  <g class="r" style="animation-delay:0.15s">
    <!-- Accent indicator -->
    <rect x="28" y="28" width="10" height="10" rx="2" fill="{accent}"/>
    <text x="46" y="37" font-family="'Geist Mono', monospace" font-size="11" letter-spacing="1" fill="{MUTED}">
      RESEARCH PROJECT //
    </text>
    <text x="180" y="37" font-family="'Geist Mono', monospace" font-size="11" font-weight="600" fill="{accent}">
      {escape(status)}
    </text>
    <text class="n" x="{w - 40}" y="37" font-family="'Geist Mono', monospace" font-size="14" fill="{accent}">&#8599;</text>

    <!-- Project Title & Subtitle -->
    <text x="28" y="72" font-family="'Instrument Serif', Georgia, serif" font-size="32" fill="{INK}">
      {escape(title)} <tspan font-family="'Geist', sans-serif" font-size="15" font-weight="normal" fill="{MUTED}">— {escape(subtitle)}</tspan>
    </text>

    <!-- Objective -->
    {render_lines(28, 102, wrap_text(objective, 86), 20, f'font-family="\'Geist\', sans-serif" font-size="13" fill="{INK_SOFT}"')}

    <!-- Divider & Methods -->
    <line x1="28" y1="148" x2="{w - 28}" y2="148" stroke="{RULE}" stroke-width="1"/>
    <text x="28" y="168" font-family="'Geist Mono', monospace" font-size="11" fill="{MUTED}">
      METHODS: <tspan fill="{INK}">{escape(methods_str)}</tspan>
    </text>
  </g>
"""

    svg_out = make_card_svg(
        w, h, body,
        font_keys=["serif", "serif-i", "sans", "sans-b", "mono"],
        label=f"{title}: {subtitle}"
    )
    with open(os.path.join(CARDS_DIR, f"project-{card_id}.svg"), "w", encoding="utf-8") as f:
        f.write(svg_out)
    print(f"wrote cards/project-{card_id}.svg")

def render_all_projects():
    research_data = load_json("research.json")
    for p in research_data.get("projects", []):
        render_project_card(
            p["id"], p["title"], p["subtitle"],
            p["objective"], p["methods"], p["status"],
            p["repo_url"], p.get("accent", COBALT)
        )

# ==============================================================================
# 4. ACADEMIC & RESEARCH JOURNEY TIMELINE
# ==============================================================================
def render_timeline():
    w = 880
    h = 240
    
    milestones = [
        ("2022 — Present", "SAKEC", "BVoc in Cyber Security", "Threat Intelligence, Network Defense & Hardware Security"),
        ("2023 — Present", "IIT Madras", "BS in Data Science & Applications", "Machine Learning, Scientific Computing & Statistics"),
        ("2024", "MNIT Jaipur (AMRUT)", "Research Intern", "Remote Photoplethysmography (rPPG), SwinV2 & STDS"),
        ("2024", "NIT Warangal", "Research Association", "Intelligent Systems & Computational Experiments"),
        ("2024", "SIH Prototype", "Guardian Travel Twin", "Smart-City Mobility & Microscopic Traffic Simulation"),
    ]

    items_svg = []
    step_x = (w - 60) / len(milestones)
    for i, (period, org, title, desc) in enumerate(milestones):
        x = 36 + i * step_x
        delay = 0.2 + i * 0.1
        items_svg.append(f"""
    <g class="r" style="animation-delay:{delay:.2f}s">
      <!-- Milestone Node -->
      <circle cx="{x + 8}" cy="70" r="5" fill="{COBALT}"/>
      <circle cx="{x + 8}" cy="70" r="10" fill="none" stroke="{CYAN}" stroke-width="1" stroke-opacity="0.6"/>
      
      <!-- Date -->
      <text x="{x + 8}" y="46" font-family="'Geist Mono', monospace" font-size="10.5" font-weight="600" fill="{COBALT}">{period}</text>
      
      <!-- Org & Title -->
      <text x="{x + 8}" y="102" font-family="'Geist', sans-serif" font-weight="600" font-size="13.5" fill="{INK}">{escape(org)}</text>
      <text x="{x + 8}" y="122" font-family="'Geist', sans-serif" font-size="12" fill="{INK_SOFT}">{escape(title)}</text>
      
      <!-- Detail -->
      {render_lines(x + 8, 144, wrap_text(desc, 18), 16, f'font-family="\'Geist\', sans-serif" font-size="10.5" fill="{MUTED}"')}
    </g>
        """)

    body = f"""
  <rect width="{w}" height="{h}" rx="12" fill="{PAPER}" stroke="{RULE}" stroke-width="1"/>
  
  <!-- Horizontal Track -->
  <line x1="40" y1="70" x2="{w - 40}" y2="70" stroke="{RULE}" stroke-width="1.5"/>

  <!-- Milestone Elements -->
  {''.join(items_svg)}
"""

    svg_out = make_card_svg(
        w, h, body,
        font_keys=["sans", "sans-b", "mono"],
        label="Academic and Research Milestones Timeline"
    )
    with open(os.path.join(CARDS_DIR, "research-timeline.svg"), "w", encoding="utf-8") as f:
        f.write(svg_out)
    print("wrote cards/research-timeline.svg")

# ==============================================================================
# 5. REPOSITORY CARDS
# ==============================================================================
def render_repo_card(name, desc, lang, color, stars, index, total=3):
    tile_w = (W - 12 * (total - 1)) / total  # ~285px each in a row of 3
    tile_h = 175
    delay = 0.3 + index * 0.12

    meta = f"{lang}  ·  ★ {stars}" if stars else f"{lang}  ·  Research"
    body = f"""
  <rect width="{tile_w}" height="{tile_h}" rx="10" fill="{PAPER}" stroke="{RULE}" stroke-width="1"/>
  <g class="r" style="animation-delay:{delay:.2f}s">
    <rect x="20" y="24" width="8" height="8" rx="2" fill="{color}"/>
    <text x="36" y="32" font-family="'Geist', sans-serif" font-weight="600" font-size="16" fill="{INK}">
      {escape(name)}
    </text>
    <text class="n" x="{tile_w - 24}" y="32" font-family="'Geist Mono', monospace" font-size="13" fill="{color}">&#8599;</text>

    {render_lines(20, 62, wrap_text(desc, 30), 19, f'font-family="\'Geist\', sans-serif" font-size="12.5" fill="{INK_SOFT}"')}
    
    <line x1="20" y1="{tile_h - 38}" x2="{tile_w - 20}" y2="{tile_h - 38}" stroke="{RULE}" stroke-width="0.8"/>
    <text x="20" y="{tile_h - 20}" font-family="'Geist Mono', monospace" font-size="11" fill="{MUTED}">
      {escape(meta)}
    </text>
  </g>
"""

    svg_out = make_card_svg(
        tile_w, tile_h, body,
        font_keys=["sans", "sans-b", "mono"],
        label=f"Repository {name}: {desc}"
    )
    with open(os.path.join(CARDS_DIR, f"repo-{name}.svg"), "w", encoding="utf-8") as f:
        f.write(svg_out)
    print(f"wrote cards/repo-{name}.svg")

def render_all_repo_cards():
    top_repos = [
        ("PhysioFM", "Foundation models & failure diagnostics in contactless rPPG.", "Python", COBALT, 0),
        ("SentinelAI", "Adaptive SSH threat intelligence & unsupervised anomaly scoring.", "Python", "#2563EB", 1),
        ("BreatheSync", "Respiratory health diagnostics with 6-sec voice samples & digital twin.", "TypeScript", CYAN, 0),
        ("IITM-Python-Grpa", "Introduction to Python Graded Programming Assessments (GRPA).", "Python", "#F59E0B", 51),
        ("Semantic-Ctrl-F", "Localized image search via visual atoms and CLIP embeddings.", "Python", VIOLET, 0),
        ("semantic-drift-vlm-attacks", "Preprocessing attack surface and SEV defense in Vision-Language Models.", "Python", "#EF4444", 1)
    ]
    for idx, (name, desc, lang, color, stars) in enumerate(top_repos):
        render_repo_card(name, desc, lang, color, stars, idx % 3, 3)

# ==============================================================================
# 6. EDITORIAL SECTION TITLES (DARK & LIGHT THEMES)
# ==============================================================================
def render_section_title(slug, title, italic, dark_fg="#E6EDF3", light_fg=INK):
    for theme, fg in [("light", light_fg), ("dark", dark_fg)]:
        body = f"""
  <text class="r" style="animation-delay:0.1s" x="4" y="38" 
        font-family="'Instrument Serif', Georgia, serif" font-size="34" fill="{fg}">
    {escape(title)} <tspan font-style="italic" fill="{COBALT}">{escape(italic)}</tspan>
  </text>
"""
        svg_out = make_card_svg(
            W, 52, body,
            font_keys=["serif", "serif-i"],
            label=f"Section: {title} {italic}"
        )
        with open(os.path.join(CARDS_DIR, f"title-{slug}-{theme}.svg"), "w", encoding="utf-8") as f:
            f.write(svg_out)
    print(f"wrote cards/title-{slug}-light.svg & dark.svg")

def render_all_titles():
    titles = [
        ("research", "Research", "Directions"),
        ("projects", "Selected", "Research & Projects"),
        ("publications", "Publications &", "Research Output"),
        ("journey", "Academic &", "Research Journey"),
        ("activity", "GitHub", "Activity & Telemetry"),
        ("repos", "Featured", "Repositories"),
        ("stack", "Technology", "Toolkit"),
        ("connect", "Connect &", "Collaborate")
    ]
    for slug, t, it in titles:
        render_section_title(slug, t, it)

def main():
    os.makedirs(CARDS_DIR, exist_ok=True)
    render_hero()
    render_research_map()
    render_all_projects()
    render_timeline()
    render_all_repo_cards()
    render_all_titles()
    print("All cards rendered successfully.")

if __name__ == "__main__":
    main()

