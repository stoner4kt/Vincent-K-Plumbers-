#!/usr/bin/env python3
"""Generate WebP variants for every site image.

For each `images/<cat>/<name>.jpg` (with its optional `-640.jpg` sibling)
this writes a same-dimensions `.webp` file next to it:
  images/<cat>/<name>.jpg          -> images/<cat>/<name>.webp
  images/<cat>/<name>-640.jpg      -> images/<cat>/<name>-640.webp

Idempotent: existing .webp files that are older than their source are rebuilt.
Regenerate with:  python3 tools/build_images.py
"""
import os
import sys

from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
IMG_DIR = os.path.join(ROOT, "images")


def webp_path(jpg_path):
    return os.path.splitext(jpg_path)[0] + ".webp"


def convert(jpg_path):
    src_mtime = os.path.getmtime(jpg_path)
    dst = webp_path(jpg_path)
    if os.path.exists(dst) and os.path.getmtime(dst) >= src_mtime:
        return False
    im = Image.open(jpg_path)
    im = im.convert("RGB")
    im.save(dst, "WEBP", quality=80, method=4)
    return True


def main():
    if not os.path.isdir(IMG_DIR):
        sys.exit(f"images dir not found: {IMG_DIR}")
    built = skipped = 0
    for root, _dirs, files in os.walk(IMG_DIR):
        for name in sorted(files):
            if not name.lower().endswith(".jpg"):
                continue
            jpg = os.path.join(root, name)
            if convert(jpg):
                built += 1
            else:
                skipped += 1
    print(f"webp: built={built} skipped(up-to-date)={skipped}")


if __name__ == "__main__":
    main()