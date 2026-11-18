#!/usr/bin/env python3
"""
Portrait Processing Pipeline for Shashwat Upadhyay (Master Revision V3.2).

Generates a crisp 2x-retina editorial cobalt-and-navy halftone studio portrait from
the user's uploaded artwork/photo with:
- Sharp Lanczos + unsharp detail clarity (420x520 embedded into 210x260 viewBox)
- Rich S-curve ink tonal ramp (Midnight Navy #081133 -> Cobalt #1E46E8 -> Electric Blue #4C82FF)
- Cool studio radial vignette + subtle architectural dot grid backdrop
- Silky translucent scanline hairline + diagonal glass reflection sweep + pulsing reticles
"""

import os
import base64
import cv2
import numpy as np
from PIL import Image, ImageFilter

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
    display_w, display_h = 210, 260
    # 2x Retina rendering for razor-sharp stipple/halftone clarity
    render_w, render_h = display_w * 2, display_h * 2
    im = Image.open(source_path)

    if stype == "ascii":
        # Crop bust and head cleanly centered with generous headroom
        crop = im.crop((135, 90, 889, 955))
        resized = crop.resize((render_w, render_h), Image.Resampling.LANCZOS)
        # Mild unsharp mask so halftone stippling & facial details pop crisply
        sharpened = resized.filter(ImageFilter.UnsharpMask(radius=1.2, percent=135, threshold=3))
        gray = np.array(sharpened.convert("L"), dtype=np.float32)

        # Normalize ink density: background paper is ~245-250, ink strokes are darker
        raw_ink = np.clip((244.0 - gray) / 175.0, 0.0, 1.0)
        # Boost midtone contrast with smooth power curve so facial features are rich & never washed out
        ink = np.power(raw_ink, 0.72)

        # Clean alpha channel (eliminate faint paper noise < 0.06)
        alpha_f = np.clip((ink - 0.05) / 0.95, 0.0, 1.0)
        alpha = np.clip(np.power(alpha_f, 0.85) * 255.0, 0, 255).astype(np.uint8)

        # Vectorized 3-stop editorial ink palette:
        # Light stipple -> Electric Blue (#4C82FF)
        # Midtone features -> Rich Cobalt (#1E46E8)
        # Deep hair/eye shadows -> Deep Midnight Navy (#07102E)
        c_light = np.array([76.0, 130.0, 255.0], dtype=np.float32)   # #4C82FF
        c_mid = np.array([30.0, 70.0, 232.0], dtype=np.float32)      # #1E46E8
        c_deep = np.array([7.0, 16.0, 46.0], dtype=np.float32)       # #07102E

        rgb = np.zeros((render_h, render_w, 3), dtype=np.float32)
        low_mask = ink < 0.45
        t_low = np.clip(ink / 0.45, 0.0, 1.0)[..., None]
        t_high = np.clip((ink - 0.45) / 0.55, 0.0, 1.0)[..., None]

        rgb_low = (1.0 - t_low) * c_light + t_low * c_mid
        rgb_high = (1.0 - t_high) * c_mid + t_high * c_deep
        rgb = np.where(low_mask[..., None], rgb_low, rgb_high)

        rgba = np.zeros((render_h, render_w, 4), dtype=np.uint8)
        rgba[..., :3] = np.clip(rgb, 0, 255).astype(np.uint8)
        rgba[..., 3] = alpha

        # Ultra-fine subtle editorial micro-scanlines (every 4th retina row = 2px display, subtle 0.90)
        rgba[::4, :, 3] = (rgba[::4, :, 3].astype(np.float32) * 0.90).astype(np.uint8)

        # Soft bottom bust fade so shoulders blend smoothly above the status pill
        fade_start = int(render_h * 0.82)
        fade_rows = render_h - fade_start
        fade_curve = np.linspace(1.0, 0.25, fade_rows, dtype=np.float32)[:, None]
        rgba[fade_start:, :, 3] = (rgba[fade_start:, :, 3].astype(np.float32) * fade_curve).astype(np.uint8)

        out_im = Image.fromarray(rgba, mode="RGBA")
        out_im.save(OUT_PNG, optimize=True)
        print(f"Saved 2x-retina transparent ASCII portrait PNG: {OUT_PNG}")

    else:
        # Photo pipeline (fallback)
        if stype == "avatar":
            crop = im.crop((170, 30, 350, 260))
        else:
            w, h = im.size
            side = min(w, h)
            cx, cy = w // 2, int(h * 0.45)
            crop = im.crop((max(0, cx - side // 2), max(0, cy - side // 2),
                            min(w, cx + side // 2), min(h, cy + side // 2)))

        crop = crop.resize((render_w, render_h), Image.Resampling.LANCZOS)
        gray_np = np.array(crop.convert("L"))
        clahe = cv2.createCLAHE(clipLimit=2.2, tileGridSize=(8, 8))
        enhanced_np = clahe.apply(gray_np)
        p3, p97 = np.percentile(enhanced_np, (4, 96))
        stretched = np.clip((enhanced_np - p3) / max(1.0, (p97 - p3)) * 255.0, 0, 255).astype(np.float32)
        norm = stretched / 255.0

        c_dark = np.array([7, 16, 46], dtype=np.float32)
        c_mid = np.array([37, 84, 255], dtype=np.float32)
        c_high = np.array([245, 249, 255], dtype=np.float32)

        t1 = np.clip(norm / 0.5, 0.0, 1.0)[..., None]
        t2 = np.clip((norm - 0.5) / 0.5, 0.0, 1.0)[..., None]
        rgb = np.where((norm < 0.5)[..., None], (1 - t1) * c_dark + t1 * c_mid, (1 - t2) * c_mid + t2 * c_high)
        out_im = Image.fromarray(np.clip(rgb, 0, 255).astype(np.uint8))
        out_im.save(OUT_PNG, optimize=True)
        print(f"Saved processed photo portrait PNG: {OUT_PNG}")

    with open(OUT_PNG, "rb") as pf:
        b64_png = base64.b64encode(pf.read()).decode("utf-8")

    # Self-contained SVG with studio radial backdrop, blueprint dot grid,
    # silky translucent scanline, diagonal glass sheen, and pulsing corner reticles
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {display_w} {display_h}" width="{display_w}" height="{display_h}">
  <defs>
    <style>
      @keyframes portrait-scan {{
        0% {{ transform: translateY(-28px); opacity: 0; }}
        12% {{ opacity: 0.9; }}
        82% {{ opacity: 0.9; }}
        100% {{ transform: translateY({display_h + 10}px); opacity: 0; }}
      }}
      @keyframes glass-sheen {{
        0%, 100% {{ transform: translateX(-260px) skewX(-22deg); opacity: 0; }}
        12% {{ opacity: 0.45; }}
        32% {{ transform: translateX(300px) skewX(-22deg); opacity: 0; }}
      }}
      @keyframes reticle-breathe {{
        0%, 100% {{ stroke-opacity: 0.95; }}
        50% {{ stroke-opacity: 0.4; }}
      }}
      @keyframes halo-pulse {{
        0%, 100% {{ opacity: 0.55; }}
        50% {{ opacity: 0.85; }}
      }}
      .scanline-sweep {{
        animation: portrait-scan 5.5s cubic-bezier(0.45, 0, 0.55, 1) infinite;
      }}
      .portrait-sheen {{
        animation: glass-sheen 7.5s ease-in-out infinite;
      }}
      .reticle {{
        animation: reticle-breathe 3.2s ease-in-out infinite;
      }}
      .studio-halo {{
        animation: halo-pulse 4.5s ease-in-out infinite;
      }}
      @media (prefers-reduced-motion: reduce) {{
        .scanline-sweep, .portrait-sheen, .reticle, .studio-halo {{ animation: none !important; }}
      }}
    </style>
    <clipPath id="port-clip">
      <rect width="{display_w}" height="{display_h}" rx="10"/>
    </clipPath>
    <radialGradient id="studio-bg" cx="50%" cy="42%" r="65%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="68%" stop-color="#F2F5FF"/>
      <stop offset="100%" stop-color="#E2E9FF"/>
    </radialGradient>
    <radialGradient id="cobalt-halo" cx="50%" cy="40%" r="48%">
      <stop offset="0%" stop-color="#315EFF" stop-opacity="0.16"/>
      <stop offset="65%" stop-color="#7DDFFF" stop-opacity="0.06"/>
      <stop offset="100%" stop-color="#315EFF" stop-opacity="0"/>
    </radialGradient>
    <pattern id="port-dots" width="12" height="12" patternUnits="userSpaceOnUse">
      <circle cx="1.5" cy="1.5" r="0.7" fill="#315EFF" fill-opacity="0.18"/>
    </pattern>
    <linearGradient id="scan-grad" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#315EFF" stop-opacity="0"/>
      <stop offset="72%" stop-color="#315EFF" stop-opacity="0.14"/>
      <stop offset="96%" stop-color="#7DDFFF" stop-opacity="0.45"/>
      <stop offset="100%" stop-color="#7DDFFF" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="sheen-grad" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0"/>
      <stop offset="50%" stop-color="#FFFFFF" stop-opacity="0.7"/>
      <stop offset="100%" stop-color="#FFFFFF" stop-opacity="0"/>
    </linearGradient>
  </defs>

  <g clip-path="url(#port-clip)">
    <!-- Cool Editorial Studio Backdrop -->
    <rect width="{display_w}" height="{display_h}" fill="url(#studio-bg)"/>
    <rect width="{display_w}" height="{display_h}" fill="url(#port-dots)"/>
    <circle class="studio-halo" cx="{display_w / 2:.1f}" cy="{display_h * 0.42:.1f}" r="96" fill="url(#cobalt-halo)"/>

    <!-- Crisp 2x-Retina Duotone Portrait Artwork -->
    <image href="data:image/png;base64,{b64_png}" x="0" y="0" width="{display_w}" height="{display_h}" preserveAspectRatio="xMidYMid meet"/>

    <!-- Subtle Silky Cyan Laser Scan Sweep -->
    <g class="scanline-sweep">
      <rect x="0" y="0" width="{display_w}" height="24" fill="url(#scan-grad)"/>
      <line x1="0" y1="23.5" x2="{display_w}" y2="23.5" stroke="#315EFF" stroke-opacity="0.55" stroke-width="0.9"/>
    </g>

    <!-- Diagonal Glassmorphic Sheen Sweep -->
    <rect class="portrait-sheen" x="0" y="-20" width="54" height="{display_h + 40}" fill="url(#sheen-grad)"/>

    <!-- Precision Frame & Pulsing Corner Reticles -->
    <rect x="0.75" y="0.75" width="{display_w - 1.5}" height="{display_h - 1.5}" rx="10" fill="none" stroke="#315EFF" stroke-width="1" stroke-opacity="0.32"/>
    <g class="reticle" fill="none" stroke="#315EFF" stroke-width="2" stroke-linecap="round">
      <path d="M 1 16 L 1 1 L 16 1"/>
      <path d="M {display_w - 16} 1 L {display_w - 1} 1 L {display_w - 1} 16"/>
      <path d="M 1 {display_h - 16} L 1 {display_h - 1} L 16 {display_h - 1}"/>
      <path d="M {display_w - 16} {display_h - 1} L {display_w - 1} {display_h - 1} L {display_w - 1} {display_h - 16}"/>
    </g>

    <!-- Sleek Dark Glass Status Pill -->
    <rect x="10" y="{display_h - 26}" width="106" height="17" rx="4" fill="#08112E" fill-opacity="0.88" stroke="#315EFF" stroke-opacity="0.45" stroke-width="0.7"/>
    <circle cx="19" cy="{display_h - 17.5}" r="2.3" fill="#7DDFFF"/>
    <text x="27" y="{display_h - 14.5}" font-family="'Geist Mono', monospace" font-size="8" font-weight="600" fill="#E8F4FF" letter-spacing="0.8">SHASHWAT // AI</text>
  </g>
</svg>
"""

    with open(OUT_SVG, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print(f"Saved 2x-retina editorial studio portrait SVG: {OUT_SVG}")


if __name__ == "__main__":
    process_portrait()
