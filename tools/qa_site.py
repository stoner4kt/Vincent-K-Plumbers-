#!/usr/bin/env python3
"""Validate local links, JSON-LD, sitemap coverage and the review/GA4 safeguards."""
from __future__ import annotations

import json
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SITE = "https://vincentplumbing.co.za"
errors: list[str] = []
html_files = sorted(p for p in ROOT.rglob("*.html")
                    if ".git" not in p.parts and "node_modules" not in p.parts and "_partials" not in p.parts)
indexable: set[Path] = set()
inbound: dict[str, int] = {}
jsonld_count = 0

for page in html_files:
    source = page.read_text(encoding="utf-8")
    noindex = bool(re.search(
        r'<meta\s+name=["\']robots["\']\s+content=["\'][^"\']*noindex',
        source, re.I
    ))
    if page.name != "404.html" and not noindex:
        indexable.add(page)

    for raw in re.findall(
        r'<script\s+type=["\']application/ld\+json["\']\s*>([\s\S]*?)</script>',
        source, re.I
    ):
        jsonld_count += 1
        try:
            json.loads(raw)
        except json.JSONDecodeError as exc:
            errors.append(f"{page.relative_to(ROOT)}: invalid JSON-LD ({exc})")

    for href in re.findall(r'\bhref\s*=\s*["\']([^"\']+)["\']', source, re.I):
        href = href.strip()
        if not href or href.startswith(("#", "mailto:", "tel:", "javascript:", "data:")):
            continue
        parsed = urlsplit(href)
        if parsed.scheme and parsed.scheme not in ("http", "https"):
            continue
        if parsed.netloc and parsed.netloc.lower() not in ("vincentplumbing.co.za", "www.vincentplumbing.co.za"):
            continue
        path_part = unquote(parsed.path)
        if not path_part:
            continue
        if path_part.startswith("/"):
            target = (ROOT / path_part.lstrip("/"))
        else:
            target = page.parent / path_part
        if target.is_dir() or path_part.endswith("/"):
            target = target / "index.html"
        target = target.resolve()
        if not target.exists():
            errors.append(f"{page.relative_to(ROOT)}: broken href {href}")
        elif target.suffix == ".html":
            try:
                target_rel = target.relative_to(ROOT).as_posix()
            except ValueError:
                target_rel = ""
            if target_rel in {p.relative_to(ROOT).as_posix() for p in indexable} and target != page:
                inbound[target_rel] = inbound.get(target_rel, 0) + 1

sitemap_path = ROOT / "sitemap.xml"
try:
    sitemap = ET.parse(sitemap_path).getroot()
    ns = {"sm": "http://www.sitemaps.org/schemas/sitemap/0.9"}
    sitemap_urls = {
        (node.text or "").strip()
        for node in sitemap.findall("sm:url/sm:loc", ns)
    }
except (ET.ParseError, OSError) as exc:
    sitemap_urls = set()
    errors.append(f"sitemap.xml: cannot parse ({exc})")

expected_urls = set()
for page in indexable:
    rel = page.relative_to(ROOT).as_posix()
    expected_urls.add(SITE + ("/" if rel == "index.html" else "/" + rel))

if sitemap_urls != expected_urls:
    missing = sorted(expected_urls - sitemap_urls)
    extra = sorted(sitemap_urls - expected_urls)
    errors.append(f"sitemap mismatch: missing={missing}; extra={extra}")

indexable_relpaths = {p.relative_to(ROOT).as_posix() for p in indexable}
for rel in sorted(indexable_relpaths):
    if rel != "index.html" and inbound.get(rel, 0) == 0:
        errors.append(f"{rel}: indexable page has no internal inbound link")

reviews = (ROOT / "reviews.html").read_text(encoding="utf-8")
if "Reviews coming soon" not in reviews:
    errors.append("reviews.html: expected the Coming Soon state")
if '"aggregateRating"' in reviews or '"@type": "Review"' in reviews:
    errors.append("reviews.html: review/rating schema must not be published without verified reviews")

service_areas = (ROOT / "service-areas.html").read_text(encoding="utf-8")
for region in "ABCDEFG":
    if f"Region {region}" not in service_areas:
        errors.append(f"service-areas.html: missing Region {region}")

site_lib = (ROOT / "tools" / "site_lib.py").read_text(encoding="utf-8")
if "[GA4-MEASUREMENT-ID]" not in site_lib or "window.trackConversion = function () {};" not in site_lib:
    errors.append("tools/site_lib.py: GA4 placeholder or safe tracking fallback missing")

print(f"HTML pages: {len(html_files)}")
print(f"Indexable HTML pages: {len(indexable)}")
print(f"JSON-LD blocks parsed: {jsonld_count}")
print(f"Sitemap URLs: {len(sitemap_urls)}")
print(f"Broken links / schema / sitemap / reachability issues: {len(errors)}")
if errors:
    for error in errors:
        print("FAIL:", error)
    sys.exit(1)
print("Site QA passed.")
