"""Generate the PWA icons (PNG) without external libraries.

Run:  python tools/make_icons.py
Writes web/icons/*.png
Motif: a 180-degree dome over a horizon line with a play triangle inside.
"""
import math, os, struct, zlib

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "web", "icons")

BG_TOP = (30, 58, 138)     # #1e3a8a
BG_BOT = (12, 18, 40)      # #0c1228
DOME = (125, 186, 255)     # light blue
PLAY = (255, 255, 255)


def clamp(v, a=0.0, b=1.0):
    return a if v < a else b if v > b else v


def sd_round_box(px, py, cx, cy, hw, hh, r):
    qx = abs(px - cx) - hw + r
    qy = abs(py - cy) - hh + r
    return math.hypot(max(qx, 0), max(qy, 0)) + min(max(qx, qy), 0) - r


def sd_segment(px, py, ax, ay, bx, by):
    pax, pay, bax, bay = px - ax, py - ay, bx - ax, by - ay
    h = clamp((pax * bax + pay * bay) / (bax * bax + bay * bay))
    return math.hypot(pax - bax * h, pay - bay * h)


def sd_triangle(px, py, pts):
    d = min(sd_segment(px, py, *pts[i], *pts[(i + 1) % 3]) for i in range(3))
    # inside test via edge signs
    s = []
    for i in range(3):
        (ax, ay), (bx, by) = pts[i], pts[(i + 1) % 3]
        s.append((bx - ax) * (py - ay) - (by - ay) * (px - ax))
    inside = all(v >= 0 for v in s) or all(v <= 0 for v in s)
    return -d if inside else d


def sd_dome(px, py, cx, cy, r, t):
    """Upper half circle arc + horizon line, stroke half-width t."""
    if py <= cy:
        arc = abs(math.hypot(px - cx, py - cy) - r)
    else:
        arc = min(math.hypot(px - (cx - r), py - cy), math.hypot(px - (cx + r), py - cy))
    line = sd_segment(px, py, cx - r - 0.06, cy, cx + r + 0.06, cy)
    return min(arc, line) - t


def blend(dst, src, a):
    return tuple(d + (s - d) * a for d, s in zip(dst, src))


def render(size, rounded):
    px_size = 1.0 / size
    rows = []
    for y in range(size):
        row = bytearray([0])  # filter type 0
        v = (y + 0.5) / size
        for x in range(size):
            u = (x + 0.5) / size
            # background
            bg = blend(BG_TOP, BG_BOT, v)
            if rounded:
                a_bg = clamp(0.5 - sd_round_box(u, v, 0.5, 0.5, 0.46, 0.46, 0.2) / px_size)
            else:
                a_bg = 1.0
            col = bg
            # dome
            a = clamp(0.5 - sd_dome(u, v, 0.5, 0.65, 0.30, 0.026) / px_size)
            col = blend(col, DOME, a)
            # play triangle
            tri = [(0.455, 0.44), (0.455, 0.60), (0.59, 0.52)]
            a = clamp(0.5 - (sd_triangle(u, v, tri) - 0.012) / px_size)
            col = blend(col, PLAY, a)
            row += bytes([int(round(c)) for c in col] + [int(round(a_bg * 255))])
        rows.append(bytes(row))
    return rows


def write_png(path, size, rows):
    def chunk(tag, data):
        return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", zlib.crc32(tag + data) & 0xFFFFFFFF)
    raw = b"".join(rows)
    png = b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", size, size, 8, 6, 0, 0, 0)) \
        + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b"")
    with open(path, "wb") as f:
        f.write(png)


if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    jobs = [("icon-192.png", 192, True), ("icon-512.png", 512, True),
            ("icon-maskable-512.png", 512, False), ("apple-touch-icon.png", 180, False)]
    for name, size, rounded in jobs:
        write_png(os.path.join(OUT, name), size, render(size, rounded))
        print("wrote", name)
