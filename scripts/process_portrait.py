#!/usr/bin/env python3
"""
Portrait Processing Pipeline for Shashwat Upadhyay.

Generates a premium blue-duotone scanline portrait from real photo and illustration sources.
Source Priority:
  1. assets/user_uploaded_ascii.jpg (user uploaded ASCII halftone portrait)
  2. assets/user_uploaded_photo.jpg (user uploaded direct photo)
  3. assets/profile-photo.jpg (if user supplies manual photo)
  4. assets/github-avatar.png (genuine avatar photo in repository)
"""

import os
import sys
import base64
import cv2
import numpy as np
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, "..")
ASSETS = os.path.join(ROOT, "assets")

USER_ASCII = os.path.join(ASSETS, "user_uploaded_ascii.jpg")
USER_PHOTO = os.path.join(ASSETS, "user_uploaded_photo.jpg")
MANUAL_PHOTO = os.path.join(ASSETS, "profile-photo.jpg")
FALLBACK_AVATAR = os.path.join(ASSETS, "github-avatar.png")

OUT_PNG = os.path.join(ASSETS, "shashwat-portrait.png")
OUT_SVG = os.path.join(ASSETS, "shashwat-portrait.svg")

def get_source_image():
    if os.path.exists(USER_ASCII):
        print(f"Using user-uploaded ASCII portrait: {USER_ASCII}")
        return USER_ASCII, "ascii"
    elif os.path.exists(USER_PHOTO):
        print(f"Using user-uploaded real photo: {USER_PHOTO}")
        return USER_PHOTO, "photo"
    elif os.path.exists(MANUAL_PHOTO):
        print(f"Using manual profile photo: {MANUAL_PHOTO}")
        return MANUAL_PHOTO, "photo"
    elif os.path.exists(FALLBACK_AVATAR):
        print(f"Using genuine avatar photo: {FALLBACK_AVATAR}")
        return FALLBACK_AVATAR, "avatar"
    else:
        raise FileNotFoundError("No source portrait image found in assets.")

def process_portrait():
    source_path, stype = get_source_image()
    target_w, target_h = 210, 260
    im = Image.open(source_path)

    if stype == "ascii":
        # User uploaded ASCII halftone portrait
        # Crop bust and head centered: (140, 100, 884, 950)
        crop = im.crop((140, 100, 884, 950))
        resized = crop.resize((target_w, target_h), Image.Resampling.LANCZOS)
        resized_gray = np.array(resized.convert('L')).astype(np.float32)

        # Invert: background is ~247 (near white), ink is dark
        ink_density = np.clip((247.0 - resized_gray) / 190.0, 0.0, 1.0)
        alpha = np.clip(ink_density ** 0.85 * 255.0, 0, 255).astype(np.uint8)

        # Cobalt & Navy color palette
        c_cobalt = np.array([49, 94, 255], dtype=np.float32)   # #315EFF Electric Cobalt
        c_mid = np.array([30, 62, 184], dtype=np.float32)      # #1E3EB8
        c_deep = np.array([7, 11, 25], dtype=np.float32)       # #070B19 Deep Midnight Navy

        rgba = np.zeros((target_h, target_w, 4), dtype=np.uint8)
        for y in range(target_h):
            for x in range(target_w):
                d = ink_density[y, x]
                if d < 0.4:
                    t = d / 0.4
                    col = (1 - t) * c_cobalt + t * c_mid
                else:
                    t = (d - 0.4) / 0.6
                    col = (1 - t) * c_mid + t * c_deep
                rgba[y, x, :3] = np.clip(col, 0, 255).astype(np.uint8)
                rgba[y, x, 3] = alpha[y, x]

        # Scanlines
        for y in range(0, target_h, 2):
            rgba[y, :, 3] = (rgba[y, :, 3] * 0.78).astype(np.uint8)

        out_im = Image.fromarray(rgba, mode="RGBA")
        out_im.save(OUT_PNG)
        print(f"Saved transparent ASCII portrait PNG: {OUT_PNG}")

    else:
        # Photo pipeline (webcam, DSLR, or avatar)
        if stype == "avatar":
            crop = im.crop((170, 30, 350, 260))
        else:
            w, h = im.size
            side = min(w, h)
            cx, cy = w // 2, int(h * 0.45)
            crop = im.crop((max(0, cx - side // 2), max(0, cy - side // 2),
                            min(w, cx + side // 2), min(h, cy + side // 2)))

        crop = crop.resize((target_w, target_h), Image.Resampling.LANCZOS)
        gray = crop.convert('L')
        gray_np = np.array(gray)
        clahe = cv2.createCLAHE(clipLimit=2.2, tileGridSize=(8, 8))
        enhanced_np = clahe.apply(gray_np)

        p3, p97 = np.percentile(enhanced_np, (4, 96))
        stretched = np.clip((enhanced_np - p3) / max(1.0, (p97 - p3)) * 255.0, 0, 255).astype(np.float32)

        Y, X = np.ogrid[:target_h, :target_w]
        center_x, center_y = target_w * 0.52, target_h * 0.42
        dist = np.sqrt(((X - center_x) / (target_w * 0.55)) ** 2 + ((Y - center_y) / (target_h * 0.55)) ** 2)
        vignette = np.clip(1.0 - (dist - 0.45) * 1.4, 0.25, 1.0)
        norm = (stretched * vignette) / 255.0

        c_dark = np.array([7, 11, 25], dtype=np.float32)
        c_mid = np.array([37, 84, 255], dtype=np.float32)
        c_cyan = np.array([125, 223, 255], dtype=np.float32)
        c_high = np.array([255, 255, 255], dtype=np.float32)

        duotone = np.zeros((target_h, target_w, 3), dtype=np.uint8)
        for y in range(target_h):
            for x in range(target_w):
                l = norm[y, x]
                if l < 0.38:
                    t = l / 0.38
                    col = (1 - t) * c_dark + t * c_mid
                elif l < 0.75:
                    t = (l - 0.38) / 0.37
                    col = (1 - t) * c_mid + t * c_cyan
                else:
                    t = (l - 0.75) / 0.25
                    col = (1 - t) * c_cyan + t * c_high
                duotone[y, x] = np.clip(col, 0, 255).astype(np.uint8)

        for y in range(0, target_h, 2):
            duotone[y] = (duotone[y] * 0.68).astype(np.uint8)

        out_im = Image.fromarray(duotone)
        out_im.save(OUT_PNG)
        print(f"Saved processed photo portrait PNG: {OUT_PNG}")

    # Generate Self-Contained SVG with animated blue scan sweep
    with open(OUT_PNG, "rb") as pf:
        b64_png = base64.b64encode(pf.read()).decode("utf-8")

    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {target_w} {target_h}" width="{target_w}" height="{target_h}">
  <defs>
    <style>
      @keyframes portrait-scan {{
        0% {{ transform: translateY(0); opacity: 0; }}
        15% {{ opacity: 0.85; }}
        85% {{ opacity: 0.85; }}
        100% {{ transform: translateY({target_h}px); opacity: 0; }}
      }}
      .scanline-sweep {{
        animation: portrait-scan 5s cubic-bezier(0.4, 0, 0.2, 1) infinite;
      }}
      @media (prefers-reduced-motion: reduce) {{
        .scanline-sweep {{ animation: none !important; display: none; }}
      }}
    </style>
    <clipPath id="port-clip">
      <rect width="{target_w}" height="{target_h}" rx="8"/>
    </clipPath>
    <linearGradient id="scan-grad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#315EFF" stop-opacity="0"/>
      <stop offset="50%" stop-color="#7DDFFF" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#315EFF" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <g clip-path="url(#port-clip)">
    <!-- Actual Processed Duotone Artwork -->
    <image href="data:image/png;base64,{b64_png}" width="{target_w}" height="{target_h}" preserveAspectRatio="xMidYMid meet"/>

    <!-- Subtle animated blue light scan bar -->
    <g class="scanline-sweep">
      <rect x="0" y="0" width="{target_w}" height="14" fill="url(#scan-grad)"/>
      <line x1="0" y1="7" x2="{target_w}" y2="7" stroke="#7DDFFF" stroke-width="1.2"/>
    </g>

    <!-- Border & Technical Corner Ticks -->
    <rect x="0.5" y="0.5" width="{target_w-1}" height="{target_h-1}" rx="8" fill="none" stroke="#315EFF" stroke-width="1" stroke-opacity="0.3"/>
    <path d="M 0 16 L 0 0 L 16 0" fill="none" stroke="#315EFF" stroke-width="1.8"/>
    <path d="M {target_w-16} 0 L {target_w} 0 L {target_w} 16" fill="none" stroke="#315EFF" stroke-width="1.8"/>
    <path d="M 0 {target_h-16} L 0 {target_h} L 16 {target_h}" fill="none" stroke="#315EFF" stroke-width="1.8"/>
    <path d="M {target_w-16} {target_h} L {target_w} {target_h} L {target_w} {target_h-16}" fill="none" stroke="#315EFF" stroke-width="1.8"/>

    <!-- Status Metadata Badge -->
    <rect x="8" y="{target_h-22}" width="96" height="15" rx="3" fill="#070B19" fill-opacity="0.85"/>
    <text x="14" y="{target_h-11}" font-family="'Geist Mono', monospace" font-size="8" font-weight="600" fill="#7DDFFF" letter-spacing="0.8">SHASHWAT // AI</text>
  </g>
</svg>
"""

    with open(OUT_SVG, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Saved processed portrait SVG: {OUT_SVG}")

if __name__ == "__main__":
    process_portrait()
