#!/usr/bin/env python3
"""
Generate the 16:9 Master Editorial Visual for Shashwat Upadhyay:
"RESEARCH IN MOTION — Intelligence across modalities."

Canvas: 1280 x 720 (16:9).
Composition:
- Transition from warm paper neutral tones into deep midnight navy & electric cobalt.
- Center: Layered RGB & Thermal silhouette with rPPG physiological wave extraction.
- Left: Digital twin urban mobility network (arterial routes, SUMO traffic nodes).
- Right: Multimodal ML, computer vision patches, VLM security layers & anomaly hyperplanes.
- Swiss editorial grid, precise scientific telemetry, restrained cyan/violet accents.
"""

import os
import base64

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
OUT_SVG = os.path.join(ROOT, "assets", "research-visual.svg")
OUT_CARD = os.path.join(ROOT, "cards", "research-visual.svg")
FONTS = os.path.join(ROOT, "fonts")

def get_font_css():
    css = []
    font_map = [
        ("Instrument Serif", "normal", 400, "serif-400.woff"),
        ("Instrument Serif", "italic", 400, "serif-italic.woff"),
        ("Geist", "normal", 400, "geist-400.woff"),
        ("Geist", "normal", 600, "geist-600.woff"),
        ("Geist Mono", "normal", 400, "geistmono-400.woff"),
    ]
    for fam, style, weight, fn in font_map:
        path = os.path.join(FONTS, fn)
        if os.path.exists(path):
            with open(path, "rb") as f:
                b64 = base64.b64encode(f.read()).decode("utf-8")
            css.append(
                f"@font-face {{ font-family: '{fam}'; font-style: {style}; font-weight: {weight}; "
                f"src: url(data:font/woff;base64,{b64}) format('woff'); }}"
            )
    return "".join(css)

def generate_svg():
    w, h = 1280, 720
    font_css = get_font_css()

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}" role="img" aria-label="Research in Motion: Intelligence Across Modalities">
  <title>Research in Motion: Intelligence Across Modalities — Shashwat Upadhyay</title>
  <defs>
    <style>
      {font_css}
      .mono {{ font-family: 'Geist Mono', ui-monospace, SFMono-Regular, Menlo, monospace; }}
      .sans {{ font-family: 'Geist', system-ui, -apple-system, sans-serif; }}
      .serif {{ font-family: 'Instrument Serif', Georgia, serif; }}
      
      @keyframes pulse-subtle {{
        0%, 100% {{ opacity: 0.85; }}
        50% {{ opacity: 0.35; }}
      }}
      @keyframes wave-flow {{
        0% {{ stroke-dashoffset: 0; }}
        100% {{ stroke-dashoffset: -120; }}
      }}
      @keyframes scanline {{
        0% {{ transform: translateY(0); }}
        100% {{ transform: translateY(320px); }}
      }}
      
      .live-pulse {{ animation: pulse-subtle 4s ease-in-out infinite; }}
      .flow-line {{ stroke-dasharray: 6 6; animation: wave-flow 12s linear infinite; }}
      .scan-bar {{ animation: scanline 8s ease-in-out infinite alternate; }}
      
      @media (prefers-reduced-motion: reduce) {{
        .live-pulse, .flow-line, .scan-bar {{ animation: none !important; }}
      }}
    </style>

    <!-- Canvas Background Gradient: Warm Paper to Deep Midnight Navy & Cobalt -->
    <linearGradient id="bg-canvas" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#F5F5F0"/>
      <stop offset="28%" stop-color="#EBECE6"/>
      <stop offset="56%" stop-color="#141D2F"/>
      <stop offset="85%" stop-color="#080C16"/>
      <stop offset="100%" stop-color="#04060B"/>
    </linearGradient>

    <!-- Thermal & Infrared Gradient -->
    <linearGradient id="thermal-ramp" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#1E3A8A" stop-opacity="0.8"/>
      <stop offset="35%" stop-color="#315EFF" stop-opacity="0.9"/>
      <stop offset="65%" stop-color="#7DDFFF" stop-opacity="0.95"/>
      <stop offset="90%" stop-color="#C084FC" stop-opacity="0.85"/>
      <stop offset="100%" stop-color="#F43F5E" stop-opacity="0.6"/>
    </linearGradient>

    <!-- Subtle Grid Pattern -->
    <pattern id="swiss-grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#FFFFFF" stroke-opacity="0.04" stroke-width="0.8"/>
      <circle cx="0" cy="0" r="1" fill="#FFFFFF" fill-opacity="0.12"/>
    </pattern>

    <!-- Halftone Dot Pattern for Document & Modality Atoms -->
    <pattern id="atom-dots" width="8" height="8" patternUnits="userSpaceOnUse">
      <circle cx="4" cy="4" r="1.2" fill="#7DDFFF" fill-opacity="0.25"/>
    </pattern>

    <!-- Glow Filter -->
    <filter id="soft-glow" x="-20%" y="-20%" width="140%" height="140%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feComposite in="SourceGraphic" in2="blur" operator="over"/>
    </filter>
  </defs>

  <!-- 1. BASE BACKGROUND -->
  <rect width="{w}" height="{h}" fill="url(#bg-canvas)"/>
  <rect width="{w}" height="{h}" fill="url(#swiss-grid)"/>

  <!-- 2. SWISS EDITORIAL BORDERS & RULERS -->
  <rect x="24" y="24" width="{w-48}" height="{h-48}" fill="none" stroke="#FFFFFF" stroke-opacity="0.12" stroke-width="1"/>
  
  <!-- Outer Corner Marks -->
  <path d="M 18 36 L 18 18 L 36 18" fill="none" stroke="#315EFF" stroke-width="2"/>
  <path d="M {w-36} 18 L {w-18} 18 L {w-18} 36" fill="none" stroke="#315EFF" stroke-width="2"/>
  <path d="M 18 {h-36} L 18 {h-18} L 36 {h-18}" fill="none" stroke="#315EFF" stroke-width="2"/>
  <path d="M {w-36} {h-18} L {w-18} {h-18} L {w-18} {h-36}" fill="none" stroke="#315EFF" stroke-width="2"/>

  <!-- Editorial Header Bar -->
  <line x1="24" y1="72" x2="{w-24}" y2="72" stroke="#FFFFFF" stroke-opacity="0.12" stroke-width="1"/>
  <text x="44" y="52" class="mono" font-size="11" letter-spacing="1.5" fill="#131313">RESEARCH IN MOTION // EDITORIAL IDENTITY</text>
  <text x="500" y="52" class="mono" font-size="11" letter-spacing="1" fill="#FFFFFF" fill-opacity="0.5">FIG 01.0 — CROSS-MODALITY SPATIAL SYNTHESIS</text>
  <text x="{w-44}" y="52" text-anchor="end" class="mono" font-size="11" letter-spacing="1" fill="#7DDFFF">SHASHWAT UPADHYAY</text>

  <!-- Left/Right Modality Tags -->
  <text x="44" y="104" class="mono" font-size="9" letter-spacing="1.2" fill="#131313" fill-opacity="0.6">[MODALITY 01: DIGITAL TWIN &amp; MOBILITY]</text>
  <text x="{w-44}" y="104" text-anchor="end" class="mono" font-size="9" letter-spacing="1.2" fill="#7DDFFF">[MODALITY 02: MULTIMODAL &amp; SECURE AI]</text>

  <!-- ============================================================== -->
  <!-- 3. LEFT SECTION: DIGITAL TWIN URBAN MOBILITY NETWORK (SUMO)     -->
  <!-- ============================================================== -->
  <g transform="translate(60, 140)">
    <!-- Mobility Grid Box -->
    <rect width="320" height="420" rx="6" fill="#131313" fill-opacity="0.03" stroke="#131313" stroke-opacity="0.12"/>
    <text x="16" y="26" class="mono" font-size="10" font-weight="600" fill="#131313">URBAN MOBILITY DIGITAL TWIN</text>
    <text x="16" y="40" class="mono" font-size="8.5" fill="#131313" fill-opacity="0.55">SUMO MICRO-SIMULATION · YOLO CALIBRATION</text>

    <!-- Road Arteries (Network Topology) -->
    <g stroke="#131313" stroke-opacity="0.25" stroke-width="1.5" fill="none">
      <!-- Major Radial Arterials -->
      <path d="M 20 280 C 80 280 120 240 160 210 C 200 180 250 160 300 150"/>
      <path d="M 40 380 C 110 320 140 260 160 210 C 180 150 200 110 240 70"/>
      <path d="M 280 380 C 230 330 190 270 160 210 C 130 150 100 120 30 90"/>
      <!-- Ring Corridors -->
      <ellipse cx="160" cy="210" rx="90" ry="70" stroke-dasharray="3 3" stroke-opacity="0.2"/>
      <ellipse cx="160" cy="210" rx="140" ry="110" stroke-dasharray="2 4" stroke-opacity="0.15"/>
    </g>

    <!-- Active Vehicle Trajectories (Electric Cobalt & Cyan Flows) -->
    <g fill="none">
      <path d="M 20 280 C 80 280 120 240 160 210 C 200 180 250 160 300 150" 
            stroke="#315EFF" stroke-width="2" class="flow-line"/>
      <path d="M 40 380 C 110 320 140 260 160 210" 
            stroke="#7DDFFF" stroke-width="2" class="flow-line"/>
      <path d="M 160 210 C 180 150 200 110 240 70" 
            stroke="#315EFF" stroke-width="1.8" class="flow-line"/>
    </g>

    <!-- Intersection Nodes & Sensor Gateways -->
    <!-- Central Traffic Nexus -->
    <circle cx="160" cy="210" r="7" fill="#315EFF" filter="url(#soft-glow)"/>
    <circle cx="160" cy="210" r="14" fill="none" stroke="#7DDFFF" stroke-width="1" class="live-pulse"/>
    <text x="178" y="214" class="mono" font-size="8.5" fill="#131313" font-weight="600">NEXUS_ALPHA [60Hz]</text>

    <!-- Satellite Connected Nodes -->
    <circle cx="70" cy="280" r="4" fill="#131313" fill-opacity="0.8"/>
    <circle cx="240" cy="165" r="4" fill="#315EFF"/>
    <circle cx="210" cy="115" r="4" fill="#7DDFFF"/>
    <circle cx="100" cy="335" r="4" fill="#131313" fill-opacity="0.6"/>
    <circle cx="115" cy="140" r="4" fill="#315EFF"/>

    <!-- Dynamic Telemetry Overlay -->
    <g transform="translate(16, 330)">
      <rect width="130" height="66" rx="4" fill="#FFFFFF" fill-opacity="0.85" stroke="#131313" stroke-opacity="0.12"/>
      <text x="8" y="16" class="mono" font-size="8" fill="#131313" font-weight="600">TRAFFIC STATE // REAL-TIME</text>
      <text x="8" y="30" class="mono" font-size="7.5" fill="#315EFF">VEH_COUNT: 1,482</text>
      <text x="8" y="44" class="mono" font-size="7.5" fill="#131313" fill-opacity="0.7">LATENCY: 14.2ms</text>
      <text x="8" y="58" class="mono" font-size="7.5" fill="#131313" fill-opacity="0.7">YOLO-V9 ACC: 94.8%</text>
    </g>
  </g>

  <!-- ============================================================== -->
  <!-- 4. CENTER SECTION: MULTIMODAL SILHOUETTE & PHYSIO COMPUTING    -->
  <!-- ============================================================== -->
  <g transform="translate(490, 120)">
    <!-- Scientific Calibration Axis & Crosshairs -->
    <line x1="150" y1="20" x2="150" y2="480" stroke="#FFFFFF" stroke-opacity="0.08" stroke-width="1"/>
    <line x1="10" y1="260" x2="290" y2="260" stroke="#FFFFFF" stroke-opacity="0.08" stroke-width="1"/>

    <!-- Concentric Isocontours (Simulating Remote Sensing & Thermal Scanners) -->
    <ellipse cx="150" cy="200" rx="130" ry="170" fill="none" stroke="#315EFF" stroke-opacity="0.2" stroke-width="1" stroke-dasharray="4 6"/>
    <ellipse cx="150" cy="200" rx="100" ry="135" fill="none" stroke="#7DDFFF" stroke-opacity="0.25" stroke-width="1"/>
    <ellipse cx="150" cy="200" rx="70" ry="95" fill="none" stroke="#8B5CF6" stroke-opacity="0.3" stroke-width="1" stroke-dasharray="2 4"/>

    <!-- Central Layered Human Silhouette -->
    <!-- Outer RGB Envelope Contour -->
    <path d="M 100 180 C 100 115 120 70 150 70 C 180 70 200 115 200 180 C 200 230 185 255 150 265 C 115 255 100 230 100 180 Z"
          fill="none" stroke="#7DDFFF" stroke-opacity="0.4" stroke-width="1.5"/>

    <!-- Thermal Isobar Body Shading (Multi-Layer Pseudocolor Contours) -->
    <path d="M 112 180 C 112 125 128 85 150 85 C 172 85 188 125 188 180 C 188 220 176 242 150 250 C 124 242 112 220 112 180 Z"
          fill="url(#thermal-ramp)" fill-opacity="0.18" stroke="#315EFF" stroke-opacity="0.6" stroke-width="1.2"/>

    <path d="M 124 175 C 124 135 135 105 150 105 C 165 105 176 135 176 175 C 176 208 166 225 150 232 C 134 225 124 208 124 175 Z"
          fill="url(#thermal-ramp)" fill-opacity="0.3" stroke="#7DDFFF" stroke-opacity="0.8" stroke-width="1.2"/>

    <!-- Subtle Scanlines over Face & Torso -->
    <g stroke="#7DDFFF" stroke-opacity="0.35" stroke-width="0.8">
      <line x1="118" y1="125" x2="182" y2="125"/>
      <line x1="122" y1="140" x2="178" y2="140"/>
      <line x1="126" y1="155" x2="174" y2="155"/>
      <line x1="124" y1="170" x2="176" y2="170"/>
      <line x1="128" y1="185" x2="172" y2="185"/>
      <line x1="132" y1="200" x2="168" y2="200"/>
    </g>

    <!-- Torso / Trapezius Contours -->
    <path d="M 50 380 C 70 330 105 295 130 280 L 170 280 C 195 295 230 330 250 380 Z"
          fill="#315EFF" fill-opacity="0.08" stroke="#315EFF" stroke-opacity="0.3" stroke-width="1.2"/>
    <g stroke="#FFFFFF" stroke-opacity="0.12" stroke-width="0.8">
      <line x1="75" y1="315" x2="225" y2="315"/>
      <line x1="62" y1="340" x2="238" y2="340"/>
      <line x1="52" y1="365" x2="248" y2="365"/>
    </g>

    <!-- rPPG Forehead Region of Interest (ROI) Crosshairs -->
    <g transform="translate(150, 130)">
      <circle cx="0" cy="0" r="12" fill="none" stroke="#7DDFFF" stroke-width="1.5" class="live-pulse"/>
      <line x1="-18" y1="0" x2="18" y2="0" stroke="#7DDFFF" stroke-width="1"/>
      <line x1="0" y1="-18" x2="0" y2="18" stroke="#7DDFFF" stroke-width="1"/>
      <rect x="-24" y="-32" width="48" height="13" rx="2" fill="#315EFF"/>
      <text x="0" y="-23" text-anchor="middle" class="mono" font-size="7.5" font-weight="bold" fill="#FFFFFF">ROI // BVP</text>
    </g>

    <!-- Extracted Physiological Blood Volume Pulse (BVP) Waveform -->
    <g transform="translate(20, 395)">
      <rect width="260" height="60" rx="4" fill="#0D1527" fill-opacity="0.85" stroke="#315EFF" stroke-opacity="0.4"/>
      <text x="12" y="15" class="mono" font-size="8" fill="#7DDFFF" font-weight="600">RECONSTRUCTED BVP SIGNAL [PHYSIOFM]</text>
      <text x="248" y="15" text-anchor="end" class="mono" font-size="8" fill="#315EFF">HR: 71.4 BPM</text>
      <!-- Pulsatile Photoplethysmogram Curve (Dicrotic Notch) -->
      <path d="M 12 40 
               Q 25 15, 35 40 T 45 40 
               Q 58 12, 68 38 T 78 40 
               Q 91 14, 101 39 T 111 40 
               Q 124 13, 134 38 T 144 40 
               Q 157 14, 167 39 T 177 40 
               Q 190 12, 200 38 T 210 40 
               Q 223 15, 233 40 T 248 40" 
            fill="none" stroke="#7DDFFF" stroke-width="2" filter="url(#soft-glow)"/>
    </g>
  </g>

  <!-- ============================================================== -->
  <!-- 5. RIGHT SECTION: MULTIMODAL ML, VLM ATTACK & SECURITY GRAPHS  -->
  <!-- ============================================================== -->
  <g transform="translate(860, 140)">
    <!-- Container Box -->
    <rect width="360" height="420" rx="6" fill="#0D1527" fill-opacity="0.7" stroke="#315EFF" stroke-opacity="0.25"/>
    <text x="20" y="26" class="mono" font-size="10" font-weight="600" fill="#7DDFFF">MULTIMODAL INTELLIGENCE &amp; ML SECURITY</text>
    <text x="20" y="40" class="mono" font-size="8.5" fill="#FFFFFF" fill-opacity="0.5">VLM PREPROCESSING SURFACE · SENTINEL ANOMALY SPACES</text>

    <!-- A. Vision-Language Semantic Drift Architecture Diagram -->
    <g transform="translate(20, 60)">
      <!-- Step 1: User-Visible RGBA Image Box -->
      <rect width="90" height="74" rx="4" fill="#141F36" stroke="#7DDFFF" stroke-opacity="0.4"/>
      <rect x="6" y="6" width="78" height="42" fill="#FFFFFF" fill-opacity="0.05"/>
      <rect x="6" y="6" width="78" height="42" fill="url(#atom-dots)"/>
      <text x="45" y="62" text-anchor="middle" class="mono" font-size="7.5" fill="#FFFFFF" fill-opacity="0.8">IMAGE (I_u) [RGBA]</text>
      <text x="45" y="70" text-anchor="middle" class="mono" font-size="6.5" fill="#7DDFFF">Hidden Alpha α≤10</text>

      <!-- Connecting Arrow: Compositing Operator -->
      <path d="M 94 37 L 126 37" stroke="#315EFF" stroke-width="1.5" stroke-dasharray="2 2"/>
      <polygon points="126,34 132,37 126,40" fill="#315EFF"/>
      <text x="110" y="30" text-anchor="middle" class="mono" font-size="6.5" fill="#FFFFFF" fill-opacity="0.6">FLATTEN</text>

      <!-- Step 2: Model-Visible RGB Tensor Box -->
      <rect x="136" y="0" width="90" height="74" rx="4" fill="#090E1A" stroke="#F43F5E" stroke-opacity="0.6"/>
      <rect x="142" y="6" width="78" height="42" fill="#000000"/>
      <text x="181" y="28" text-anchor="middle" class="mono" font-size="7" fill="#F43F5E" font-weight="bold">[PAYLOAD REVEALED]</text>
      <text x="181" y="62" text-anchor="middle" class="mono" font-size="7.5" fill="#FFFFFF" fill-opacity="0.8">TENSOR (I_m) [RGB]</text>
      <text x="181" y="70" text-anchor="middle" class="mono" font-size="6.5" fill="#F43F5E">Semantic Drift Triggered</text>

      <!-- Step 3: SEV Defense Verifier Badge -->
      <g transform="translate(236, 12)">
        <rect width="84" height="50" rx="3" fill="#101D38" stroke="#315EFF" stroke-width="1"/>
        <text x="42" y="16" text-anchor="middle" class="mono" font-size="7" font-weight="bold" fill="#7DDFFF">SEV DEFENSE</text>
        <text x="42" y="28" text-anchor="middle" class="mono" font-size="6.5" fill="#FFFFFF" fill-opacity="0.7">OCR Discrepancy</text>
        <text x="42" y="40" text-anchor="middle" class="mono" font-size="6.5" fill="#10B981">DR: 100% | FPR: 0%</text>
      </g>
    </g>

    <!-- B. Unsupervised Anomaly Isolation Hyperplane (SentinelAI) -->
    <g transform="translate(20, 160)">
      <line x1="0" y1="0" x2="320" y2="0" stroke="#FFFFFF" stroke-opacity="0.1"/>
      <text x="0" y="20" class="mono" font-size="9" font-weight="600" fill="#FFFFFF" fill-opacity="0.9">SENTINEL-AI // UNSUPERVISED ISOLATION BOUNDARY</text>

      <!-- Coordinate Box for Anomaly Clusters -->
      <rect y="30" width="320" height="100" rx="4" fill="#080C16" stroke="#FFFFFF" stroke-opacity="0.08"/>
      
      <!-- Inliers (Normal Cluster) -->
      <g fill="#315EFF" fill-opacity="0.6">
        <circle cx="80" cy="80" r="3"/>
        <circle cx="95" cy="70" r="2.5"/>
        <circle cx="88" cy="90" r="3"/>
        <circle cx="110" cy="75" r="2"/>
        <circle cx="102" cy="85" r="3"/>
        <circle cx="75" cy="65" r="2.5"/>
        <circle cx="120" cy="82" r="3"/>
      </g>
      <!-- Decision Boundary Splitting Planes -->
      <line x1="40" y1="110" x2="160" y2="40" stroke="#7DDFFF" stroke-width="1.2" stroke-dasharray="3 3"/>
      <line x1="160" y1="120" x2="220" y2="40" stroke="#8B5CF6" stroke-width="1" stroke-dasharray="2 4"/>

      <!-- Outlier Anomaly Threat (Host Infiltration Spike) -->
      <circle cx="270" cy="55" r="5" fill="#F43F5E" filter="url(#soft-glow)"/>
      <circle cx="270" cy="55" r="11" fill="none" stroke="#F43F5E" stroke-width="1" class="live-pulse"/>
      <text x="255" y="80" class="mono" font-size="7" fill="#F43F5E">OUTLIER SCORE: 0.94</text>
      <text x="255" y="90" class="mono" font-size="6.5" fill="#FFFFFF" fill-opacity="0.6">SSH_BURST_FAIL</text>

      <text x="14" y="50" class="mono" font-size="7" fill="#7DDFFF">CLUSTER_INLIERS [NORMAL]</text>
      <text x="14" y="62" class="mono" font-size="6.5" fill="#FFFFFF" fill-opacity="0.5">ISOLATION FOREST DEPTH: 8</text>
    </g>

    <!-- C. Multimodal Visual Atom Index (Semantic Ctrl-F / CLIP Grid) -->
    <g transform="translate(20, 310)">
      <line x1="0" y1="0" x2="320" y2="0" stroke="#FFFFFF" stroke-opacity="0.1"/>
      <text x="0" y="18" class="mono" font-size="9" font-weight="600" fill="#7DDFFF">SEMANTIC CTRL-F // VISUAL ATOM VECTORIZATION</text>
      
      <!-- Visual Atoms Matrix -->
      <g transform="translate(0, 28)">
        <!-- 4x2 Visual Patch Grid -->
        <rect x="0" y="0" width="28" height="24" rx="2" fill="#141F36" stroke="#315EFF" stroke-width="0.8"/>
        <rect x="34" y="0" width="28" height="24" rx="2" fill="#141F36" stroke="#315EFF" stroke-width="0.8"/>
        <rect x="68" y="0" width="28" height="24" rx="2" fill="#315EFF" stroke="#7DDFFF" stroke-width="1.2"/>
        <rect x="102" y="0" width="28" height="24" rx="2" fill="#141F36" stroke="#315EFF" stroke-width="0.8"/>

        <rect x="0" y="30" width="28" height="24" rx="2" fill="#141F36" stroke="#315EFF" stroke-width="0.8"/>
        <rect x="34" y="30" width="28" height="24" rx="2" fill="#141F36" stroke="#315EFF" stroke-width="0.8"/>
        <rect x="68" y="30" width="28" height="24" rx="2" fill="#141F36" stroke="#315EFF" stroke-width="0.8"/>
        <rect x="102" y="30" width="28" height="24" rx="2" fill="#141F36" stroke="#315EFF" stroke-width="0.8"/>

        <text x="145" y="16" class="mono" font-size="7.5" fill="#FFFFFF" fill-opacity="0.85">MATCH: ATOM [2, 0]</text>
        <text x="145" y="28" class="mono" font-size="7.5" fill="#7DDFFF">SIMILARITY: 0.884</text>
        <text x="145" y="42" class="mono" font-size="6.5" fill="#FFFFFF" fill-opacity="0.5">TEXT QUERY: "occluded license plate"</text>
      </g>
    </g>
  </g>

  <!-- ============================================================== -->
  <!-- 6. FOOTER EDITORIAL METADATA & SYSTEM CODES                     -->
  <!-- ============================================================== -->
  <line x1="24" y1="{h-64}" x2="{w-24}" y2="{h-64}" stroke="#FFFFFF" stroke-opacity="0.12" stroke-width="1"/>
  
  <text x="44" y="{h-36}" class="serif" font-size="24" fill="#FFFFFF">Shashwat Upadhyay</text>
  <text x="250" y="{h-40}" class="mono" font-size="9" letter-spacing="1" fill="#FFFFFF" fill-opacity="0.5">INDEPENDENT RESEARCH · SYSTEMS · CROSS-MODAL INTELLIGENCE</text>
  
  <text x="{w-44}" y="{h-40}" text-anchor="end" class="mono" font-size="9" letter-spacing="1.2" fill="#7DDFFF">SYS_ID // RIM-2026-XMODAL</text>
  <text x="{w-44}" y="{h-25}" text-anchor="end" class="mono" font-size="8" fill="#FFFFFF" fill-opacity="0.4">LATENCY: DETERMINISTIC · REPRODUCIBILITY: 100%</text>

  <!-- Visual Crosshair Calibration Accents -->
  <circle cx="{w/2}" cy="{h-64}" r="3" fill="#315EFF"/>
  <circle cx="{w/2}" cy="72" r="3" fill="#315EFF"/>
</svg>
"""
    with open(OUT_SVG, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated 16:9 master research visual: {OUT_SVG}")

    with open(OUT_CARD, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Generated 16:9 card copy: {OUT_CARD}")

if __name__ == "__main__":
    generate_svg()

