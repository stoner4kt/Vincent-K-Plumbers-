#!/usr/bin/env python3
"""Wrap JPEG <img> tags in <picture> with a WebP <source> where a .webp
sibling exists. Keeps the original <img> as fallback so browsers without
WebP support still render the site."""
import glob
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def webp_exists(ref):
    """Return True when ref (a .jpg URL) has a .webp sibling on disk.

    HTML files in guides/ use ../-prefixed URLs; strip one level so the
    path still resolves against the repo root.
    """
    clean = ref.split("?")[0]
    if clean.startswith("../"):
        clean = clean[3:]
    path = os.path.normpath(os.path.join(ROOT, clean))
    return path.endswith(".jpg") and os.path.exists(path[:-4] + ".webp")


def build_source(src, srcset):
    """Create a <source type=image/webp ...> from a jpg src/srcset."""
    attrs = []
    if srcset:
        cands = []
        for part in srcset.split(","):
            part = part.strip()
            if not part:
                continue
            bits = part.rsplit(" ", 1)
            if len(bits) == 2:
                url, size = bits
            else:
                url, size = part, ""
            if url.endswith(".jpg"):
                url = url[:-4] + ".webp"
            cands.append((url + " " + size).strip())
        attrs.append('srcset="' + ", ".join(cands) + '"')
    else:
        if src.endswith(".jpg"):
            attrs.append('src="' + src[:-4] + '.webp"')
    return "<source type=\"image/webp\" " + " ".join(attrs) + " />"


def transform(content):
    out = []
    pos = 0
    inside_picture = False
    for m in re.finditer(r"<picture\b[^>]*>|</picture\s*>|<img\b[^>]*>", content):
        tok = m.group(0)
        if tok.startswith("<picture"):
            inside_picture = True
            out.append(content[pos:m.start()])
            out.append(tok)
            pos = m.end()
        elif tok.startswith("</picture"):
            inside_picture = False
            out.append(content[pos:m.start()])
            out.append(tok)
            pos = m.end()
        else:
            tag = tok
            start, end = m.span()
            src = re.search(r'\bsrc\s*=\s*"([^"]+)"', tag)
            srcset = re.search(r'\bsrcset\s*=\s*"([^"]+)"', tag)
            ref = (src.group(1) if src else "")
            st = (srcset.group(1) if srcset else "")
            use_webp = (ref and ref.endswith(".jpg") and webp_exists(ref)
                        and not inside_picture)
            out.append(content[pos:start])
            if use_webp:
                out.append("<picture>\n      ")
                out.append(build_source(ref, st))
                out.append("\n      ")
                out.append(tag)
                out.append("\n    </picture>")
            else:
                out.append(tag)
            pos = end
    out.append(content[pos:])
    return "".join(out)


def main():
    changed = 0
    for f in sorted(glob.glob(os.path.join(ROOT, "*.html")) +
                    glob.glob(os.path.join(ROOT, "guides", "*.html"))):
        content = open(f, encoding="utf-8").read()
        new = transform(content)
        if new != content:
            open(f, "w", encoding="utf-8").write(new)
            changed += 1
            print("wrapped:", os.path.relpath(f, ROOT))
    print("done, files changed:", changed)


if __name__ == "__main__":
    main()