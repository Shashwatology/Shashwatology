#!/usr/bin/env python3
"""
SVG utility module for generating high-end editorial SVG cards with embedded fonts,
refined animation keyframes, CSS hover micro-interactions, and Swiss typographic grids.
"""

import os
import base64
from html import escape

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
FONTS_DIR = os.path.join(ROOT, "fonts")

# Brand Design Tokens
PAPER = "#F5F5F0"
PAPER_LIGHT = "#FAFAF7"
PAPER_MUTED = "#EBECE6"
PAPER_BORDER = "#DCDCD7"
INK = "#131313"
INK_SOFT = "#363638"
MUTED = "#6E6E73"
RULE = "#DCDCD7"
COBALT = "#315EFF"
CYAN = "#7DDFFF"
VIOLET = "#8B5CF6"
DARK_NAVY = "#0B1021"
DARK_SURFACE = "#121A2F"

FONT_FILES = {
    "serif": ("Instrument Serif", "normal", 400, "serif-400.woff"),
    "serif-i": ("Instrument Serif", "italic", 400, "serif-italic.woff"),
    "sans": ("Geist", "normal", 400, "geist-400.woff"),
    "sans-b": ("Geist", "normal", 600, "geist-600.woff"),
    "mono": ("Geist Mono", "normal", 400, "geistmono-400.woff"),
}

FONT_CACHE = {}

def get_font_css(keys=None):
    if keys is None:
        keys = ["serif", "serif-i", "sans", "sans-b", "mono"]
    css = []
    for k in keys:
        if k not in FONT_FILES:
            continue
        if k not in FONT_CACHE:
            fam, style, weight, fn = FONT_FILES[k]
            fpath = os.path.join(FONTS_DIR, fn)
            if os.path.exists(fpath):
                with open(fpath, "rb") as f:
                    b64 = base64.b64encode(f.read()).decode("utf-8")
                FONT_CACHE[k] = (
                    f"@font-face {{ font-family: '{fam}'; font-style: {style}; font-weight: {weight}; "
                    f"src: url(data:font/woff;base64,{b64}) format('woff'); }}\n"
                )
            else:
                FONT_CACHE[k] = ""
        css.append(FONT_CACHE[k])
    return "".join(css)

BASE_CSS = """
@keyframes rise { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: none; } }
@keyframes fade { from { opacity: 0; } to { opacity: 1; } }
@keyframes grow { from { transform: scaleY(0); } to { transform: scaleY(1); } }
@keyframes pop { 0% { opacity: 0; transform: scale(.6); } 70% { opacity: 1; transform: scale(1.08); } 100% { opacity: 1; transform: none; } }
@keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: .28; } }
@keyframes pulse-ring { 0% { transform: scale(0.8); opacity: 0.65; } 100% { transform: scale(2.4); opacity: 0; } }
@keyframes nudge { 0%, 100% { transform: none; } 50% { transform: translate(2.5px, -2px); } }
@keyframes sheen { 0% { transform: translateX(-340px) skewX(-22deg); opacity: 0; } 12% { opacity: 0.55; } 34% { transform: translateX(620px) skewX(-22deg); opacity: 0; } 100% { transform: translateX(620px) skewX(-22deg); opacity: 0; } }
@keyframes border-glide { 0% { stroke-dashoffset: 240; opacity: 0; } 15% { opacity: 0.9; } 85% { opacity: 0.9; } 100% { stroke-dashoffset: -240; opacity: 0; } }
@keyframes accent-wave { 0%, 100% { opacity: 0.18; } 50% { opacity: 0.95; } }
@keyframes cell-shimmer { 0%, 100% { opacity: 1; } 50% { opacity: 0.62; } }

.r { animation: rise 0.65s cubic-bezier(0.22, 1, 0.36, 1) both; transform-box: fill-box; }
.f { animation: fade 0.6s ease both; }
.g { animation: grow 0.75s cubic-bezier(0.22, 1, 0.36, 1) both; transform-box: fill-box; transform-origin: bottom; }
.p { animation: pop 0.55s cubic-bezier(0.22, 1, 0.36, 1) both; transform-box: fill-box; transform-origin: center; }
.live { animation: pulse 2.2s ease-in-out infinite; }
.ring { transform-box: fill-box; transform-origin: center; animation: pulse-ring 2.6s cubic-bezier(0.2, 0.8, 0.4, 1) infinite; }
.n { transform-box: fill-box; animation: nudge 2.6s ease-in-out infinite; transition: transform 0.25s ease; }
.sh { animation: sheen 7.5s ease-in-out infinite; pointer-events: none; }
.accent-bar { animation: accent-wave 4.2s ease-in-out infinite; }
.twinkle { animation: cell-shimmer 3.2s ease-in-out infinite; }

/* Interactive Hover Micro-Effects (active on direct SVG view and local preview) */
.card-interactive { cursor: pointer; }
.card-interactive .card-bg { transition: fill 0.25s ease, stroke 0.25s ease, stroke-width 0.25s ease; }
.card-interactive:hover .card-bg { fill: #FAFAF7; stroke: #315EFF; stroke-width: 1.5; }
.card-interactive:hover .n { animation: none; transform: translate(3px, -3px); }
.card-interactive:hover .hover-accent { opacity: 1; }
.hover-accent { transition: opacity 0.25s ease; }

@media (prefers-reduced-motion: reduce) {
  .r, .f, .g, .p, .live, .ring, .n, .sh, .accent-bar, .twinkle { animation: none !important; }
}
"""

def wrap_text(text, max_chars):
    lines = []
    line = ""
    for word in text.split():
        if line and len(line) + 1 + len(word) > max_chars:
            lines.append(line)
            line = word
        else:
            line = f"{line} {word}".strip()
    if line:
        lines.append(line)
    return lines

def render_lines(x, y, lines, line_height, attrs):
    return "".join(
        f'<text x="{x}" y="{y + i * line_height}" {attrs}>{escape(l)}</text>'
        for i, l in enumerate(lines)
    )

def make_card_svg(width, height, body, font_keys=None, label="", extra_css=""):
    font_css = get_font_css(font_keys)
    css = font_css + BASE_CSS + extra_css
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="{escape(label)}">\n'
        f'<title>{escape(label)}</title>\n'
        f'<style>\n{css}\n</style>\n'
        f'{body}\n'
        f'</svg>'
    )
