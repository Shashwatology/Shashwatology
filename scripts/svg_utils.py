#!/usr/bin/env python3
"""
SVG utility module for generating high-end editorial SVG cards with embedded fonts,
refined animation keyframes, and Swiss typographic grids.
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
@keyframes rise { from { opacity: 0; transform: translateY(14px); } to { opacity: 1; transform: none; } }
@keyframes fade { from { opacity: 0; } to { opacity: 1; } }
@keyframes grow { from { transform: scaleY(0); } to { transform: scaleY(1); } }
@keyframes pop { 0% { opacity: 0; transform: scale(.4); } 70% { opacity: 1; transform: scale(1.1); } 100% { opacity: 1; transform: none; } }
@keyframes pulse { 0%, 100% { opacity: 1; } 50% { opacity: .25; } }
@keyframes nudge { 0%, 100% { transform: none; } 50% { transform: translateX(3px); } }
@keyframes sheen { 0% { transform: translateX(-300px) skewX(-20deg); } 20%, 100% { transform: translateX(500px) skewX(-20deg); } }

.r { opacity: 0; animation: rise .75s cubic-bezier(.2,.7,.2,1) both; transform-box: fill-box; }
.f { opacity: 0; animation: fade .85s ease-out both; }
.g { transform-box: fill-box; transform-origin: bottom; transform: scaleY(0); animation: grow .8s cubic-bezier(.2,.7,.2,1) both; }
.p { opacity: 0; transform-box: fill-box; transform-origin: center; animation: pop .4s ease-out both; }
.live { animation: pulse 2s ease-in-out infinite; }
.n { transform-box: fill-box; animation: nudge 2s ease-in-out infinite; }
.sh { animation: sheen 6s ease-in-out infinite; }

@media (prefers-reduced-motion: reduce) {
  .r, .f, .g, .p, .live, .n, .sh { animation: none !important; opacity: 1 !important; transform: none !important; }
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

