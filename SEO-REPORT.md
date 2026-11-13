# Vincent K Plumbers — SEO & Conversion Report

Date of work: 2026-11-13
Scope: static HTML site → SEO, performance and conversion-focused rebuild.
Repo: `github.com/stoner4kt/Vincent-K-Plumbers-`

---

## 1. Stack & build setup (as found)

- **Stack:** pure static HTML + Tailwind (previously the Tailwind **CDN browser runtime**),
  Google Fonts (Inter + Plus Jakarta Sans), a single `assets/js/site.js`, custom
  `assets/css/site.css`.
- **Deploy:** static hosting (Netlify-ready: HTML forms via `name="quote-request"`,
  `data-netlify`, honeypot). No server‑side framework.
- **Change:** Tailwind CDN was **removed** and replaced with a **compiled static
  `assets/css/tailwind.css`** built by the Tailwind v4 CLI (dev dependency, justified for
  the build-time CSS). Pages now carry one `<link>` to the compiled CSS + `site.css`,
  no render-blocking CDN script.

---

## 2. What changed

### Site structure
- **Homepage** (`index.html`) targets *"plumber Johannesburg" / "emergency plumber Johannesburg"*.
- **Service pages (one keyword each, unique H1, 300+ words, How It Works + FAQ + CTA + related links):**
  1. `blocked-drains-johannesburg.html` — *blocked drain Johannesburg*
  2. `leak-detection-johannesburg.html` — *leak detection Johannesburg* (preserved existing)
  3. `geyser-repair-johannesburg.html` — *geyser repair Johannesburg*
  4. `geyser-replacement-johannesburg.html` — *geyser replacement* (preserved existing)
  5. `solar-geyser-installation-gauteng.html` — *solar geyser installation Gauteng*
  6. `burst-pipe-repair-johannesburg.html` — *burst pipe repair Johannesburg*
  7. `bathroom-renovations-johannesburg.html` — *bathroom renovation plumber Johannesburg*
  8. `waterproofing-johannesburg.html` — *waterproofing Johannesburg*
  Plus the pre-existing `plumbing`, `gas-geyser-installation`, `paving`, `irrigation`,
  `water-purification` pages were updated (header/footer/analytics/CSS).
- **Support pages:** `service-areas.html`, `about.html`, `contact.html`, `reviews.html`.
- **Guides:** `guides.html` + 5 full articles under `guides/`:
  signs your geyser is about to burst · how to find a hidden leak · blocked main drain
  causes · solar vs electric vs gas geysers · what to do in a plumbing emergency.
- **Suburb pages:** deliberately **not generated**. The owner hasn't confirmed a fixed,
  shortlist of suburbs; placeholder duplicated-template pages were removed rather than
  shipped.

### Build tooling (`tools/`)
- `content.py`, `service_pages.py`, `support_pages.py`, `guides_pages.py`,
  `apply_partials.py`, `add_webp.py`, `build_sitemap.py`, `build_all.py`, `site_lib.py`,
  `build_pages.py`. All committed; the HTML output is committed and served statically.

### On-page SEO
- Unique `<title>` (≤ 60 chars) + meta description (120–165 chars) on every page.
- One `<h1>` per page, logical H2/H3. `<html lang="en-ZA">` everywhere.
- Descriptive, keyword-aware alt text on all images; `width`/`height` attributes;
  `loading="lazy"` + `decoding="async"` below the fold; hero preloaded with
  `fetchpriority="high"`.
- **WebP:** all images that have a `.webp` sibling are now served via
  `<picture><source type="image/webp" srcset="…"/><img …/></picture>` with the original
  JPEG as fallback (175 WebP files generated).
- Canonical, Open Graph and Twitter Card tags on every page.
- Lowercase hyphenated URLs; breadcrumbs on inner pages; descriptive anchor text.
- `robots.txt` + **auto-generated `sitemap.xml`** (26 URLs, regenerated from files on disk).

### Structured data (JSON-LD)
- Homepage: `Plumber` (subtype of `LocalBusiness`) — name, url, telephone,
  `areaServed` (Johannesburg + confirmed area list), description, placeholder
  `sameAs` for Google Business Profile / Facebook / ProCompare.
- Service pages: `Service` + `FAQPage` (real FAQs on the page) + `BreadcrumbList`.
- Support/guide pages: `WebPage` + `BreadcrumbList` (+ `Article`/`FAQPage` where relevant).
- **No** `aggregateRating` / `Review` schema anywhere (no verified reviews available) —
  added only when real reviews are displayed (see TODO in `reviews.html`).
- All JSON-LD validated as syntactically valid (0 invalid blocks across 26 pages).

### Conversion optimisation
- Sticky **mobile call + WhatsApp** bar on every page.
- Phone number visible in utility bar, header, hero CTA, footer and mobile sticky bar.
- **CTA above the fold** on every page; quote-request **form** with name, phone,
  suburb, service and message on the homepage and embedded (service pre-selected) on
  every service page.
- Form: client-side validation (`novalidate` + JS), **spam protection** via Netlify
  honeypot `bot-field` (`data-netlify="true"`), `aria-busy` states, friendly errors.
- **Click tracking hooks** via `trackConversion(eventName, details)` on calls,
  WhatsApp, service-quote clicks and form submits. No hard-coded analytics ID: the GA4
  ID lives in one placeholder (`VKP_GA4_ID` in the head stub) — see placeholders below.
- Trust strip uses **only verifiable facts** (local plumber, Midrand base, same-day
  dispatch for urgent jobs is a service stated by the owner in the original site).

### Technical / performance / accessibility
- **Static compiled CSS** (no CDN JS runtime). Fonts preconnected.
- Lazy loading + responsive `sizes` + native `aspect` via width/height → no CLS.
- Colour contrast, visible `:focus-visible` outlines, semantic landmarks
  (`<header>/<main>/<footer>/<nav>/<section>`), labelled form fields, keyboard-friendly
  dropdowns (JS toggles `aria-expanded`).
- Custom `404.html` with `noindex, follow` (and a way back to the homepage).
- HTTPS/redirect handling is the host's concern (Netlify defaults to HTTPS and
  redirects `http→https`; a `_redirects` can be added per host if needed).

---

## 3. Before / after checklist

| Item | Before | After |
|---|---|---|
| Tailwind | CDN runtime script | compiled `assets/css/tailwind.css` |
| Per-service landing pages | 5 | 13 (8 core + existing) |
| Guides | none | 1 index + 5 articles |
| Service Areas / About / Contact / Reviews | — | ✓ 4 new pages |
| `<html lang>` | — | `en-ZA` everywhere |
| Titles ≤60 / desc 120–165 | mixed | ✓ all pages |
| Canonical / OG / Twitter | partial | ✓ all pages |
| JSON-LD per page | homepage + few | ✓ all 26 pages, validated |
| WebP delivery | none (JPEG only) | `<picture>` + WebP where available |
| Sitemap | static, stale | auto-generated, 26 URLs |
| Sticky mobile call/WhatsApp | sticky bar | ✓ preserved + tracking |
| Quote form on service pages | none | ✓ embedded with pre-selected service |
| Spam protection | — | Netlify honeypot |
| Click tracking hooks | partial | `trackConversion` everywhere, GA4 ID placeholder |
| 404 custom | yes | preserved, `noindex` |

---

## 4. Placeholders you must fill in

1. **GA4 measurement ID** — replace `[GA4-MEASUREMENT-ID]` in `assets/js/site.js`-adjacent
   head stub `var VKP_GA4_ID = '[GA4-MEASUREMENT-ID]';` (appears in every page head and in
   `tools/site_lib.py` `GS_SCRIPT` so builds keep it). Set the value in one place then
   rebuild, or edit the heads directly.
2. **`sameAs` links** in the homepage `Plumber` JSON-LD — currently `[VERIFY]` placeholders
   for **Google Business Profile**, **Facebook**, **ProCompare**. Fill with real profile URLs.
3. **Testimonials / reviews** — `reviews.html` renders an empty state with a TODO. Add real
   reviews (only then add `Review`/`aggregateRating` JSON-LD).
4. **Suburb pages** — confirm the list of suburbs you actually serve; generate one unique
   page per suburb (no swapped-template pages). `tools/content.py` `SERVICE_AREAS` /
   `service-areas.html` already list candidate areas — prune to what you confirm.
5. **Opening hours** — homepage `Plumber` JSON-LD has an openingHours placeholder if
   unknown.
6. **Any real certification / licence / award** claims — do **not** add until verified.
7. **Address for NAP consistency** — if you DO want a physical address shown, replace the
   service-area copy in footer + `Plumber` schema; otherwise keep the service-area approach
   (no fake address displayed).
8. **`[PHONE]`** — the repo number `068 134 3276` / `+27681343276` was found and used
   consistently everywhere; if it ever changes, update in `tools/site_lib.py` (`PHONE`,
   `PHONE_INTL`) and rebuild.

---

## 5. Off-site tasks (you)

**Google Business Profile**
- Claim/verify the profile (https://share.google/71GsegnOVWnSnEVxC).
- Complete NAP: **Vincent K Plumbers**, phone **068 134 3276**, service area Johannesburg/
  Midrand. Add real photos/Videos (already hosted on the site).
- Encourage reviews (link shortener), respond to every review.
- Link GBP to the website.

**Citations / directories**
- ProCompare, Snupit, Yellow Pages SA, Facebook — ensure NAP matches the site exactly.
- Consider HelloPeter (SA trust signal).

**Review requests**
- Ask every job for a Google review (QR/link). Only display on the site once real.

**Google Search Console**
- Verify the domain (`vincentplumbing.co.za`).
- Submit `https://vincentplumbing.co.za/sitemap.xml`.
- Submit new pages for indexing; watch impressions for the primary keywords.

**Google Analytics**
- Add the GA4 ID (placeholder section above), enable enhanced measurement or wire the
  existing `trackConversion` events into conversions.

---

## 6. QA results (at time of writing)

- 26 pages; 0 broken relative links; 0 invalid JSON-LD blocks.
- All pages reachable from the homepage; every core service page is linked from header,
  footer, homepage grid and service pages (≈25 inbound links each).
- Only intentionally-unlinked page: `404.html` (error page, `noindex`).