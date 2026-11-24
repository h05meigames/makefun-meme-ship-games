#!/usr/bin/env python3
"""Meme Sprint: AI Agents Ship Games.

Draws an original 1024x1024 meme with Pillow (stdlib + PIL only, no network,
no copied images): a user tells their AI agent to "ship the game", and the
agent takes it literally - a robot captain sailing a cargo ship stacked with
containers labelled BUGS, TODO and v1.0 toward the island of PRODUCTION.
Writes /output/entry.png.
"""
import os

from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def font(size, bold=True):
    return ImageFont.truetype(BOLD if bold else REG, size)


def wrap(draw, text, fnt, max_w):
    """Greedy word wrap, returns list of lines."""
    lines, cur = [], ""
    for word in text.split():
        trial = (cur + " " + word).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = word
    if cur:
        lines.append(cur)
    return lines


def draw_centered(draw, cx, y, lines, fnt, fill):
    for line in lines:
        w = draw.textlength(line, font=fnt)
        draw.text((cx - w / 2, y), line, font=fnt, fill=fill)
        y += fnt.size + 6
    return y


def draw_cloud(draw, x, y, s=1.0):
    """A puffy cloud from overlapping ellipses."""
    for dx, dy, rx, ry in ((0, 10, 46, 26), (38, 0, 52, 32),
                           (84, 12, 44, 24), (40, 18, 60, 26)):
        draw.ellipse([x + dx * s, y + dy * s, x + (dx + 2 * rx) * s,
                      y + (dy + 2 * ry) * s], fill=(255, 255, 255))


def draw_container(draw, x0, y0, x1, y1, fill, label):
    draw.rectangle([x0, y0, x1, y1], fill=fill, outline=(30, 30, 30), width=4)
    # corrugation lines
    for lx in range(x0 + 18, x1 - 8, 22):
        draw.line([lx, y0 + 6, lx, y1 - 6], fill=(0, 0, 0, 40), width=3)
    fnt = font(30)
    tw = draw.textlength(label, font=fnt)
    draw.text((x0 + (x1 - x0 - tw) / 2, y0 + (y1 - y0) / 2 - 20),
              label, font=fnt, fill=(255, 255, 255))


def draw_robot_captain(draw, cx, y):
    """Robot head with a captain's hat, waving from the bridge."""
    # captain's hat
    draw.polygon([(cx - 62, y - 6), (cx + 62, y - 6), (cx + 48, y - 46),
                  (cx - 48, y - 46)], fill=(255, 255, 255),
                 outline=(30, 30, 30))
    draw.rectangle([cx - 62, y - 14, cx + 62, y + 2], fill=(24, 34, 54))
    draw.ellipse([cx - 12, y - 12, cx + 12, y + 4], fill=(230, 170, 20))
    # head
    draw.rounded_rectangle([cx - 52, y, cx + 52, y + 92], radius=20,
                           fill=(90, 190, 215), outline=(20, 60, 80), width=5)
    # happy closed eyes
    for ex in (cx - 34, cx + 12):
        draw.arc([ex, y + 28, ex + 22, y + 52], 200, 340,
                 fill=(20, 40, 60), width=6)
    # big grin
    draw.arc([cx - 26, y + 52, cx + 26, y + 82], 10, 170,
             fill=(20, 40, 60), width=6)
    # waving arm (from the bridge window edge)
    draw.line([cx + 52, y + 78, cx + 96, y + 34], fill=(40, 110, 140), width=16)
    draw.ellipse([cx + 84, y + 18, cx + 112, y + 46], fill=(90, 190, 215),
                 outline=(20, 60, 80), width=4)


def main():
    img = Image.new("RGB", (W, H), (250, 248, 240))
    d = ImageDraw.Draw(img)

    # --- top caption bar ---
    d.rectangle([0, 0, W, 148], fill=(24, 34, 54))
    top = wrap(d, "ME: \u201cAI, SHIP THE GAME\u201d", font(52), W - 60)
    draw_centered(d, W // 2, 24, top, font(52), (255, 255, 255))

    # --- scene ---
    # sky
    d.rectangle([0, 148, W, 600], fill=(158, 208, 240))
    # sun
    d.ellipse([70, 185, 165, 280], fill=(255, 214, 64), outline=(230, 170, 20), width=4)
    draw_cloud(d, 300, 190)
    draw_cloud(d, 700, 170, 0.8)
    # seagulls
    for gx, gy in ((430, 230), (500, 205), (560, 245)):
        d.arc([gx, gy, gx + 26, gy + 16], 200, 340, fill=(40, 60, 80), width=4)
        d.arc([gx + 24, gy, gx + 50, gy + 16], 200, 340, fill=(40, 60, 80), width=4)

    # sea
    d.rectangle([0, 600, W, 876], fill=(38, 110, 170))
    for wy in (640, 700, 780, 840):
        for wx in range(20, W - 60, 130):
            d.arc([wx, wy, wx + 70, wy + 22], 180, 360, fill=(200, 230, 250), width=5)

    # --- island of PRODUCTION (right) ---
    d.ellipse([770, 560, 1010, 660], fill=(238, 214, 150), outline=(180, 150, 80), width=4)
    # palm tree: trunk + fronds (quadratic curves fanning from its top)
    d.line([905, 600, 880, 500], fill=(120, 72, 32), width=12)
    for cx, cy, ex, ey in ((820, 440, 780, 500), (860, 425, 845, 490),
                           (905, 420, 930, 480), (940, 440, 975, 505),
                           (880, 415, 880, 465)):
        pts = []
        for t in range(0, 21):
            tt = t / 20
            x = (1 - tt) ** 2 * 880 + 2 * (1 - tt) * tt * cx + tt ** 2 * ex
            y = (1 - tt) ** 2 * 500 + 2 * (1 - tt) * tt * cy + tt ** 2 * ey
            pts.append((x, y))
        d.line(pts, fill=(34, 139, 60), width=10, joint="curve")
    # signpost
    d.rectangle([838, 520, 846, 600], fill=(90, 60, 20), width=2)
    d.rectangle([770, 480, 920, 522], fill=(255, 255, 245), outline=(30, 30, 30), width=4)
    st = "PRODUCTION"
    d.text((775, 488), st, font=font(22), fill=(178, 24, 24))

    # --- cargo ship (left/centre) ---
    # containers: two rows
    draw_container(d, 150, 520, 300, 600, (200, 80, 60), "BUGS")
    draw_container(d, 310, 520, 460, 600, (60, 120, 200), "TODO")
    draw_container(d, 470, 520, 600, 600, (230, 170, 20), "v1.0")
    draw_container(d, 230, 440, 380, 520, (90, 160, 90), "HOTFIX")
    draw_container(d, 390, 440, 520, 520, (150, 90, 180), "???")
    # bridge tower
    d.rectangle([610, 440, 700, 620], fill=(240, 240, 235), outline=(30, 30, 30), width=4)
    d.rectangle([622, 452, 688, 492], fill=(158, 208, 240), outline=(30, 30, 30), width=3)
    # mast + v1.0 flag
    d.line([655, 440, 655, 340], fill=(30, 30, 30), width=6)
    d.polygon([(655, 340), (730, 356), (655, 374)], fill=(178, 24, 24))
    d.text((662, 344), "v1.0", font=font(16), fill=(255, 255, 255))
    # robot captain leaning out of the bridge window
    draw_robot_captain(d, 655, 452)
    # hull
    d.polygon([(110, 620), (740, 620), (690, 700), (160, 700)],
              fill=(140, 40, 40), outline=(30, 30, 30))
    d.rectangle([110, 620, 740, 636], fill=(24, 34, 54))
    # portholes
    for px in (220, 340, 460, 580):
        d.ellipse([px, 648, px + 30, 678], fill=(255, 214, 64),
                  outline=(30, 30, 30), width=3)
    # wake
    for wx in range(60, 700, 90):
        d.arc([wx, 700, wx + 60, 726], 0, 180, fill=(255, 255, 255), width=5)

    # --- bottom caption bar ---
    d.rectangle([0, 876, W, H], fill=(178, 24, 24))
    bot = wrap(d, "AGENT: SHIPPED. BUGS INCLUDED. NO EXTRA CHARGE.",
               font(46), W - 60)
    draw_centered(d, W // 2, 890, bot, font(46), (255, 255, 255))

    os.makedirs("/output", exist_ok=True)
    img.save("/output/entry.png", format="PNG", optimize=True)
    print("wrote /output/entry.png", img.size, os.path.getsize("/output/entry.png"), "bytes")


if __name__ == "__main__":
    main()
