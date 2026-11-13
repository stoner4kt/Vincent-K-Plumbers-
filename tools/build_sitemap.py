#!/usr/bin/env python3
"""Generate sitemap.xml from the actual HTML files present at the repo root
and under guides/, with today's lastmod date."""
import datetime
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://vincentplumbing.co.za"


def slugify(name):
    if name == "index.html":
        return ""
    return name


def main():
    today = datetime.date.today().isoformat()
    urls = []
    # Root pages first (home first), then guides.
    htmls = [f for f in os.listdir(ROOT) if f.endswith(".html") and not f.startswith(".")]
    htmls.sort(key=lambda f: (f != "index.html", f))
    for f in htmls:
        path = os.path.join(ROOT, f)
        # lastmod from git would be nice; use newest mtime
        mtime = datetime.datetime.fromtimestamp(os.path.getmtime(path)).date().isoformat()
        urls.append((f"{SITE}/{f if f != 'index.html' else ''}", mtime))

    guides_dir = os.path.join(ROOT, "guides")
    guides = sorted(os.listdir(guides_dir)) if os.path.isdir(guides_dir) else []
    for g in guides:
        if not g.endswith(".html"):
            continue
        mtime = datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(guides_dir, g))).date().isoformat()
        urls.append((f"{SITE}/guides/{g}", mtime))

    lines = ['<?xml version="1.0" encoding="UTF-8"?>',
             '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for loc, mtime in urls:
        lines.append("  <url>")
        lines.append(f"    <loc>{loc}</loc>")
        lines.append(f"    <lastmod>{mtime}</lastmod>")
        lines.append("  </url>")
    lines.append("</urlset>")

    with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"sitemap: {len(urls)} URLs written")


if __name__ == "__main__":
    main()