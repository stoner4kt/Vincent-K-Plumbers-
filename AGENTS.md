# Vincent K Plumbers — repository notes

Static marketing website for Vincent K Plumbers, a plumbing / gas / paving business based in
Klipfontein View, Midrand, serving Johannesburg and Gauteng, South Africa.

## Structure

```
index.html                                 home / landing page
gallery.html                               project gallery + brand asset downloads
404.html                                   404 page
<service-slug>.html                        one page per service (7 total)
assets/css/site.css                        shared styles (Tailwind utility + custom classes)
assets/js/site.js                          mobile menu, dropdown, filters, FAQ, form, lightbox
images/<category>/                         optimised photos, each with a 640px `-640.jpg` variant
images/video-posters/                      poster frames for every video
images/brand/                              logo-mark, logo, logo-light, favicon, icons, og-image
videos/<category>/                         16 original site videos (~137 MB)
sitemap.xml / robots.txt / site.webmanifest
```

Service pages: `gas-geyser-installation-johannesburg`, `geyser-replacement-johannesburg`,
`plumbing-johannesburg`, `leak-detection-johannesburg`, `paving-johannesburg`,
`irrigation-johannesburg`, `water-purification-johannesburg`.

## Styling conventions

- Keep the existing theme: navy `#0B1623` / `#07111C` backgrounds, sky `#0284C7` accents,
  orange `#EA580C` for primary CTAs.
- Fonts: Plus Jakarta Sans for headings, Inter for body — both loaded from Google Fonts.
- Tailwind is loaded from the CDN browser build, so utility classes work without a build step.
- Each page repeats the utility bar, header, footer, mobile sticky bar and lightbox markup.

## Content rules

- Never use stock photography. Everything on the site comes from the owner's own photos/videos.
- Write location-aware copy (Johannesburg, Midrand, Sandton, Centurion) but keep it honest —
  no invented statistics, awards, or review counts.
- Phone number `068 134 3276` / `+27681343276` and WhatsApp `27681343276` appear in the
  utility bar, header, hero CTAs, footer and mobile sticky bar.

## SEO requirements

Every page needs: unique `<title>` (≤60 chars), meta description (120–160 chars), keywords,
canonical, Open Graph + Twitter tags, one `<h1>`, descriptive image `alt` text, and JSON-LD
(`Plumber`/`LocalBusiness`, `WebPage`, `Service`, `BreadcrumbList`, `FAQPage`).
New pages must be added to `sitemap.xml` and linked from the header dropdown, mobile menu and
footer so nothing is orphaned.

## Image pipeline

Photos live at 1200px max on the long edge with a matching `-640.jpg` sibling used by `srcset`.
After adding a photo, generate the thumbnail, then reference both in the `<img srcset>`.

Google Business Profile: https://share.google/Ruq5u5RT56MqOVg0n
Site URL used in metadata: https://vincentplumbing.co.za
