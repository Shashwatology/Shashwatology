#!/usr/bin/env python3
"""
Portrait Processing Pipeline for Shashwat Upadhyay - Research Portfolio.

Transforms a source portrait photo (assets/profile-photo.jpg) into an elegant,
monochrome ASCII / fine scanline halftone vector illustration.
If no source photo is present, generates a scientific multimodal silhouette
placeholder (layered RGB + Thermal imaging contours with calibration crosshairs).
"""

import os
import sys
import cv2
import numpy as np
from PIL import Image, ImageEnhance, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
ASSETS = os.path.join(ROOT, "assets")
SOURCE_PHOTO = os.path.join(ASSETS, "profile-photo.jpg")
FALLBACK_AVATAR = os.path.join(ASSETS, "github-avatar.png")
OUT_PNG = os.path.join(ASSETS, "shashwat-portrait.png")
OUT_SVG = os.path.join(ASSETS, "shashwat-portrait.svg")

# Density ramp for editorial terminal ASCII rendering (light to dark)
ASCII_RAMP = " .`:-=+*cs#%@"

def generate_scientific_placeholder_svg():
    """Generates an ultra-premium scientific multimodal silhouette placeholder SVG."""
    w, h = 320, 360
    # Layered contours, thermal gradient lines, and calibration markers
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
  <defs>
    <linearGradient id="thermal-grad" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0%" stop-color="#315EFF" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#7DDFFF" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#8B5CF6" stop-opacity="0.7"/>
    </linearGradient>
    <pattern id="grid-dots" width="16" height="16" patternUnits="userSpaceOnUse">
      <circle cx="2" cy="2" r="0.8" fill="#131313" fill-opacity="0.12"/>
    </pattern>
  </defs>

  <!-- Background Grid -->
  <rect width="{w}" height="{h}" fill="none"/>
  <rect width="{w}" height="{h}" fill="url(#grid-dots)"/>

  <!-- Outer Scientific Frame -->
  <rect x="12" y="12" width="{w-24}" height="{h-24}" rx="8" fill="none" stroke="#131313" stroke-opacity="0.15" stroke-dasharray="3 3"/>
  <path d="M 12 28 L 12 12 L 28 12" fill="none" stroke="#315EFF" stroke-width="2"/>
  <path d="M {w-28} 12 L {w-12} 12 L {w-12} 28" fill="none" stroke="#315EFF" stroke-width="2"/>
  <path d="M 12 {h-28} L 12 {h-12} L 28 {h-12}" fill="none" stroke="#315EFF" stroke-width="2"/>
  <path d="M {w-28} {h-12} L {w-12} {h-12} L {w-12} {h-28}" fill="none" stroke="#315EFF" stroke-width="2"/>

  <!-- Coordinate Metadata -->
  <text x="24" y="32" font-family="'Geist Mono', monospace" font-size="9" fill="#131313" fill-opacity="0.5">MODALITY // RGB+THERMAL [rPPG]</text>
  <text x="{w-24}" y="32" text-anchor="end" font-family="'Geist Mono', monospace" font-size="9" fill="#315EFF">λ: 520nm-850nm</text>

  <!-- Central Scientific Silhouette: Abstract Human Contour & Multimodal Waveforms -->
  <g transform="translate(160, 185)">
    <!-- Layered Physiological Resonance Waves -->
    <circle cx="0" cy="-30" r="54" fill="none" stroke="#315EFF" stroke-width="1" stroke-dasharray="2 4" stroke-opacity="0.4"/>
    <circle cx="0" cy="-30" r="68" fill="none" stroke="#7DDFFF" stroke-width="1" stroke-opacity="0.5"/>
    <circle cx="0" cy="-30" r="82" fill="none" stroke="#8B5CF6" stroke-width="0.8" stroke-dasharray="4 6" stroke-opacity="0.4"/>

    <!-- Head & Shoulders Silhouette Form (Isometric / Editorial Contours) -->
    <!-- Head Contour -->
    <path d="M -32 -30 C -32 -65 32 -65 32 -30 C 32 -5 20 18 0 24 C -20 18 -32 -5 -32 -30 Z" 
          fill="#131313" fill-opacity="0.04" stroke="#131313" stroke-opacity="0.3" stroke-width="1.2"/>
    
    <!-- Facial Isocontour Lines (Simulating Thermal/3D Mesh Scanning) -->
    <path d="M -22 -35 Q 0 -45 22 -35" fill="none" stroke="#315EFF" stroke-width="1.2" stroke-opacity="0.7"/>
    <path d="M -26 -20 Q 0 -30 26 -20" fill="none" stroke="#315EFF" stroke-width="1.2" stroke-opacity="0.7"/>
    <path d="M -20 -5 Q 0 -12 20 -5" fill="none" stroke="#131313" stroke-width="1" stroke-opacity="0.4"/>
    <path d="M -14 8 Q 0 4 14 8" fill="none" stroke="#131313" stroke-width="1" stroke-opacity="0.4"/>
    
    <!-- Eye & Facial Calibration Points -->
    <circle cx="-12" cy="-28" r="2.2" fill="#315EFF"/>
    <circle cx="12" cy="-28" r="2.2" fill="#315EFF"/>
    <line x1="-18" y1="-28" x2="-6" y2="-28" stroke="#7DDFFF" stroke-width="0.8"/>
    <line x1="6" y1="-28" x2="18" y2="-28" stroke="#7DDFFF" stroke-width="0.8"/>
    <line x1="0" y1="-32" x2="0" y2="-12" stroke="#131313" stroke-width="0.8" stroke-opacity="0.3"/>

    <!-- Shoulders / Torso Contour -->
    <path d="M -75 95 C -65 65 -45 42 -18 32 L 18 32 C 45 42 65 65 75 95 Z" 
          fill="#131313" fill-opacity="0.03" stroke="#131313" stroke-opacity="0.25" stroke-width="1.2"/>
    
    <!-- Horizontal scanlines through torso -->
    <line x1="-55" y1="52" x2="55" y2="52" stroke="#131313" stroke-opacity="0.15" stroke-width="1"/>
    <line x1="-65" y1="68" x2="65" y2="68" stroke="#315EFF" stroke-opacity="0.35" stroke-width="1" stroke-dasharray="4 2"/>
    <line x1="-72" y1="84" x2="72" y2="84" stroke="#131313" stroke-opacity="0.15" stroke-width="1"/>

    <!-- Crosshair Target on Forehead (Typical rPPG Region of Interest - ROI) -->
    <g transform="translate(0, -42)">
      <circle cx="0" cy="0" r="8" fill="none" stroke="#315EFF" stroke-width="1.2"/>
      <line x1="-12" y1="0" x2="12" y2="0" stroke="#315EFF" stroke-width="1"/>
      <line x1="0" y1="-12" x2="0" y2="12" stroke="#315EFF" stroke-width="1"/>
      <rect x="-14" y="-22" width="28" height="9" rx="2" fill="#315EFF"/>
      <text x="0" y="-15" text-anchor="middle" font-family="'Geist Mono', monospace" font-size="6.5" font-weight="bold" fill="#ffffff">ROI:BVP</text>
    </g>
  </g>

  <!-- Technical Telemetry Footer -->
  <line x1="24" y1="{h-38}" x2="{w-24}" y2="{h-38}" stroke="#131313" stroke-opacity="0.1"/>
  <text x="24" y="{h-22}" font-family="'Geist Mono', monospace" font-size="8.5" fill="#131313" fill-opacity="0.6">STATUS: CALIBRATED</text>
  <text x="{w-24}" y="{h-22}" text-anchor="end" font-family="'Geist Mono', monospace" font-size="8.5" fill="#131313" fill-opacity="0.6">SYNC: 60Hz 1080p</text>
</svg>
"""
    with open(OUT_SVG, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Generated scientific placeholder SVG: {OUT_SVG}")

    # Also generate a high-res PNG version using PIL
    # We can create a crisp monochrome bitmap
    img = Image.new("RGBA", (320, 360), (245, 245, 240, 255))
    # We'll save the SVG directly; for PNG, if needed, save transparent canvas
    img.save(OUT_PNG)
    print(f"Saved portrait placeholder PNG: {OUT_PNG}")

def process_photo(photo_path):
    """Processes a user-provided photo into an editorial ASCII / scanline monochrome illustration."""
    print(f"Processing photo from {photo_path}...")
    try:
        im = Image.open(photo_path).convert("L")
    except Exception as e:
        print(f"Failed to open image {photo_path}: {e}")
        return False

    # Target grid resolution
    cols = 96
    # Compute proportional rows (character aspect ratio ~1:2)
    aspect = im.size[1] / im.size[0]
    rows = int(cols * aspect * 0.5)
    rows = max(40, min(120, rows))

    # Pre-processing: Contrast & unsharp mask
    im = ImageEnhance.Contrast(im).enhance(1.4)
    im = ImageEnhance.Sharpness(im).enhance(1.3)
    im_small = im.resize((cols, rows), Image.Resampling.LANCZOS)
    px = im_small.load()

    lines = []
    for y in range(rows):
        row_str = []
        for x in range(cols):
            val = px[x, y]
            idx = int((val / 255.0) * (len(ASCII_RAMP) - 1))
            row_str.append(ASCII_RAMP[idx])
        lines.append("".join(row_str))

    # Build monochrome SVG text lines
    w = 340
    char_w = w / cols
    char_h = char_w * 2.0
    h = int(rows * char_h) + 40

    svg_parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">',
        f'<rect width="{w}" height="{h}" fill="#F4F4F0" rx="8"/>',
        f'<g font-family="ui-monospace, \'Geist Mono\', monospace" font-size="{char_h * 0.85:.2f}" fill="#131313">',
    ]

    for idx, line in enumerate(lines):
        y_pos = 24 + idx * char_h
        escaped = line.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        svg_parts.append(
            f'<text x="10" y="{y_pos:.1f}" textLength="{w-20}" lengthAdjust="spacing" xml:space="preserve">{escaped}</text>'
        )

    svg_parts.append("</g></svg>")

    with open(OUT_SVG, "w", encoding="utf-8") as f:
        f.write("\n".join(svg_parts))
    print(f"Rendered processed portrait to {OUT_SVG}")
    return True

def main():
    if os.path.exists(SOURCE_PHOTO):
        print(f"Found source photo at {SOURCE_PHOTO}")
        success = process_photo(SOURCE_PHOTO)
        if not success:
            generate_scientific_placeholder_svg()
    else:
        print(f"Source photo not found at {SOURCE_PHOTO}")
        print("Generating editorial scientific multimodal silhouette placeholder...")
        generate_scientific_placeholder_svg()
        print("\n[NOTE FOR USER]: To use your actual face, save your photograph as 'assets/profile-photo.jpg'")
        print("and run 'python scripts/process_portrait.py'.")

if __name__ == "__main__":
    main()
