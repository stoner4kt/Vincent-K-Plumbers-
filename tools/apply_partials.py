#!/usr/bin/env python3
"""Apply the shared header/footer partials to the hand-written existing pages
(index, gallery, 404, service pages) and standardise their analytics stub.

This exists so the large pre-existing pages stay consistent with the newly
generated ones after the header/footer were centralised.
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PARTIALS = os.path.join(ROOT, "_partials")


def read(name):
    with open(os.path.join(PARTIALS, name), encoding="utf-8") as f:
        return f.read()


def write_file(name, content):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(content)


HEADER = read("header.html")
HEADER_GALLERY = read("header-gallery.html")
FOOTER = read("footer.html")


GS_STUB = """  <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
  <script>
    var VKP_GA4_ID = '[GA4-MEASUREMENT-ID]';
    if (VKP_GA4_ID.indexOf('[GA4') !== 0) {
      (function (w, d, s) {
        var g = d.createElement(s); g.async = true;
        g.src = 'https://www.googletagmanager.com/gtag/js?id=' + VKP_GA4_ID;
        var f = d.getElementsByTagName(s)[0]; f.parentNode.insertBefore(g, f);
      })(window, document, 'script');
      window.dataLayer = window.dataLayer || [];
      function gtag() { dataLayer.push(arguments); }
      gtag('js', new Date());
      gtag('config', VKP_GA4_ID, { 'anonymize_ip': true, 'send_page_view': true });
      function trackConversion(eventName, details) {
        gtag('event', eventName, Object.assign({
          'event_category': 'lead_conversion',
          'business_name': 'Vincent K Plumbers'
        }, details || {}));
      }
    }
  </script>"""


def apply_to(content, header_partial, sub_path=""):
    """Replace header and footer blocks inside a full HTML page."""
    # Header block: from '<body' up to and including '<main ...>'
    m_body = re.search(r"<body[^>]*>", content)
    m_main = re.search(r"<main[^>]*>", content)
    # Footer + mobile bar + lightbox block: from '<footer' to the site.js script
    m_footer = content.rfind("<footer")
    m_script = content.rfind('<script src="assets/js/site.js" defer></script>')
    if not (m_body and m_main and m_footer != -1 and m_script != -1):
        raise ValueError("could not locate blocks to replace")

    # Preserve the existing head (everything before <body>)
    head = content[: m_body.start()]

    body_tag = content[m_body.start(): m_body.end()]
    main_tag = content[m_main.start(): m_main.end()]

    main_content = content[m_main.end(): m_footer]
    tail = content[m_script:]

    new = head + body_tag + "\n" + header_partial + "\n  " + main_tag + "\n" + main_content + FOOTER + "\n" + tail.lstrip()
    return new


def standardise_analytics(content):
    # Replace the old inline gtag block (with the CDN script tag) with the stub.
    pattern = re.compile(
        r'<script async src="https://www\.googletagmanager\.com/gtag/js\?id=[^"]+"></script>\s*'
        r'<script>\s*window\.dataLayer.*?</script>',
        re.S)
    if pattern.search(content):
        content = pattern.sub(GS_STUB, content)
    return content


def main():
    # Hand-written pages whose body header/footer should track the partials.
    targeted = {
        "index.html": HEADER,
        "gallery.html": HEADER_GALLERY,
        "404.html": HEADER,
        "plumbing-johannesburg.html": HEADER,
        "geyser-replacement-johannesburg.html": HEADER,
        "leak-detection-johannesburg.html": HEADER,
        "gas-geyser-installation-johannesburg.html": HEADER,
        "paving-johannesburg.html": HEADER,
        "irrigation-johannesburg.html": HEADER,
        "water-purification-johannesburg.html": HEADER,
    }
    for name, header_partial in targeted.items():
        path = os.path.join(ROOT, name)
        content = open(path, encoding="utf-8").read()
        content = standardise_analytics(content)
        new = apply_to(content, header_partial)
        write_file(name, new)
        print("applied partials:", name)


if __name__ == "__main__":
    main()