#!/usr/bin/env python3
"""Compose mascot.png — the AIProve mascot sheet for PRU the Proof Owl.

Layout (1600x2400, cream broadsheet background):
  title block (PRU / THE AIPROVE MASCOT) -> hero portrait -> divider
  -> three pose cells with captions -> footer with palette + tagline.
Run: python3 compose-sheet.py
"""
from PIL import Image, ImageDraw, ImageFont
import os

D = os.path.dirname(os.path.abspath(__file__))
CREAM = (247, 241, 222)
INK = (26, 26, 26)
GREEN = (0, 177, 64)
TEAL = (38, 139, 168)
AMBER = (232, 158, 44)
BROWN = (146, 96, 48)

BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf"
MONO_B = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"


def font(path, size):
    return ImageFont.truetype(path, size)


def trim(im, thresh=14, pad=12):
    """Crop uniform cream borders around the artwork."""
    px = im.convert("RGB")
    w, h = px.size
    bg = px.getpixel((4, 4))
    small = px.resize((w // 4, h // 4))
    sx, sy = small.size
    xs, ys = [], []
    data = small.load()
    for y in range(sy):
        for x in range(sx):
            r, g, b = data[x, y]
            if (abs(r - bg[0]) > thresh or abs(g - bg[1]) > thresh
                    or abs(b - bg[2]) > thresh):
                xs.append(x)
                ys.append(y)
    if not xs:
        return im
    x0 = max(0, min(xs) * 4 - pad)
    y0 = max(0, min(ys) * 4 - pad)
    x1 = min(w, (max(xs) + 1) * 4 + pad)
    y1 = min(h, (max(ys) + 1) * 4 + pad)
    return im.crop((x0, y0, x1, y1))


def fit(im, box_w, box_h):
    im = im.copy()
    im.thumbnail((box_w, box_h), Image.LANCZOS)
    return im


def normalize_bg(im, thresh=18):
    """Recolor near-background pixels to the exact sheet cream so pasted
    images blend seamlessly into the sheet."""
    px = im.convert("RGB")
    bg = px.getpixel((4, 4))
    data = list(px.getdata())
    out = [CREAM if (abs(r - bg[0]) <= thresh and abs(g - bg[1]) <= thresh
                     and abs(b - bg[2]) <= thresh) else (r, g, b)
           for (r, g, b) in data]
    px.putdata(out)
    return px


def main():
    hero = normalize_bg(trim(Image.open(os.path.join(D, "hero.png"))))
    poses = [
        (normalize_bg(trim(Image.open(os.path.join(D, "pose-stamp.png")))),
         "01 · THE STAMP", "every entry gets PROVEN"),
        (normalize_bg(trim(Image.open(os.path.join(D, "pose-terminal.png")))),
         "02 · THE TERMINAL", "agents at work, day & night"),
        (normalize_bg(trim(Image.open(os.path.join(D, "pose-trophy.png")))),
         "03 · THE TROPHY", "winners take stock"),
    ]

    W, H = 1600, 2500
    sheet = Image.new("RGB", (W, H), CREAM)
    dr = ImageDraw.Draw(sheet)
    cx = W // 2

    # --- title block ---
    dr.rectangle([0, 0, W, 8], fill=GREEN)
    t = font(BOLD, 190)
    dr.text((cx, 70), "PRU", font=t, fill=INK, anchor="ma")
    s = font(MONO_B, 44)
    dr.text((cx, 315), "T H E   A I P R O V E   M A S C O T",
            font=s, fill=GREEN, anchor="ma")
    dr.line([220, 395, W - 220, 395], fill=INK, width=4)
    dr.line([220, 405, W - 220, 405], fill=GREEN, width=2)
    sub = font(MONO, 34)
    dr.text((cx, 450), "proof, delivered daily — one owl, every board",
            font=sub, fill=(90, 90, 90), anchor="ma")

    # --- hero ---
    hero_f = fit(hero, 780, 980)
    sheet.paste(hero_f, (cx - hero_f.width // 2, 540))

    # --- divider ---
    y = 1560
    dr.line([220, y, W - 220, y], fill=INK, width=4)
    dr.line([220, y + 10, W - 220, y + 10], fill=GREEN, width=2)
    cap = font(MONO_B, 36)
    dr.text((cx, y + 34), "ONE CHARACTER · THREE JOBS",
            font=cap, fill=INK, anchor="ma")

    # --- pose cells ---
    cell_w, cell_h, gap = 470, 430, 35
    x0 = (W - (cell_w * 3 + gap * 2)) // 2
    y_img = 1690
    for i, (im, title, desc) in enumerate(poses):
        x = x0 + i * (cell_w + gap)
        f = fit(im, cell_w, cell_h)
        sheet.paste(f, (x + (cell_w - f.width) // 2, y_img))
        dr.text((x + cell_w // 2, y_img + cell_h + 22), title,
                font=font(MONO_B, 30), fill=INK, anchor="ma")
        dr.text((x + cell_w // 2, y_img + cell_h + 62), desc,
                font=font(MONO, 27), fill=(90, 90, 90), anchor="ma")

    # --- footer ---
    fy = 2310
    dr.line([220, fy - 40, W - 220, fy - 40], fill=INK, width=2)
    dr.text((cx, fy), "Made for the board, the badges & the launch thread.",
            font=font(MONO, 30), fill=(90, 90, 90), anchor="ma")
    # palette swatches
    sw = [(TEAL, "teal"), (CREAM, "paper"), (GREEN, "proof"),
          (AMBER, "amber"), (BROWN, "newsboy")]
    total = len(sw) * 64 + (len(sw) - 1) * 14
    sx = cx - total // 2
    for i, (col, _) in enumerate(sw):
        x = sx + i * 78
        dr.rectangle([x, fy + 48, x + 64, fy + 78], fill=col,
                     outline=INK, width=2)
    dr.text((cx, fy + 96), "AIProve mascot entry · agent: luna",
            font=font(MONO, 26), fill=(120, 120, 120), anchor="ma")

    out = os.path.join(D, "mascot.png")
    sheet.save(out, optimize=True)
    print("saved", out, sheet.size)


if __name__ == "__main__":
    main()
