#!/usr/bin/env python3
"""One-shot build of every generated page plus the static CSS bundle.

Order matters: pages are generated from site_lib (shared head), then the
Tailwind CSS is re-scanned so classes used by freshly generated pages are
included, WebP <picture> wrappers are added, and finally the sitemap is
written from the actual files on disk.

Existing pages (index, gallery, 404, the legacy service pages) are NOT
regenerated here — they are maintained by tools/apply_partials.py. Run:

  python3 tools/apply_partials.py   # updates the legacy pages in place
  python3 tools/build_all.py        # regenerates generated pages + assets
"""
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)


def run(cmd):
    print(">>", " ".join(cmd))
    subprocess.run(cmd, cwd=ROOT, check=True)


def main():
    run([sys.executable, "tools/service_pages.py"])
    run([sys.executable, "tools/support_pages.py"])
    run([sys.executable, "tools/guides_pages.py"])
    run(["npx", "tailwindcss", "-i", "./assets/css/tailwind-input.css",
         "-o", "./assets/css/tailwind.css", "--minify"])
    run([sys.executable, "tools/add_webp.py"])
    run([sys.executable, "tools/build_sitemap.py"])
    print("build_all complete.")


if __name__ == "__main__":
    main()