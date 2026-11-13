"""Shared helpers for generating static pages for the Vincent K Plumbers site."""
import json
import re

SITE = "https://vincentplumbing.co.za"
PHONE = "068 134 3276"
PHONE_INTL = "+27681343276"
WHATSAPP = "27681343276"
BUSINESS = "Vincent K Plumbers"
LOGO = "images/brand/logo.jpg"
LOGO_URL = f"{SITE}/{LOGO}"
GEO_META = f"""  <meta name="geo.region" content="ZA-GP" />
  <meta name="geo.placename" content="Klipfontein View, Midrand, Johannesburg" />
  <meta name="geo.position" content="-26.0206;28.1518" />
  <meta name="ICBM" content="-26.0206, 28.1518" />
  <meta name="business:contact_data:street_address" content="505 Nancy Ndamase Street" />
  <meta name="business:contact_data:locality" content="Midrand" />
  <meta name="business:contact_data:region" content="Gauteng" />
  <meta name="business:contact_data:postal_code" content="1685" />
  <meta name="business:contact_data:country_name" content="South Africa" />
  <meta name="business:contact_data:phone_number" content="{PHONE_INTL}" />"""

GS_SCRIPT = """  <link rel="stylesheet" href="assets/css/tailwind.css" />
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


def json_ld(obj):
    return f'<script type="application/ld+json">\n{json.dumps(obj, indent=2, ensure_ascii=False)}\n  </script>'


def area_served(extra=None):
    base = ["Johannesburg", "Midrand", "Sandton", "Centurion", "Klipfontein View", "Waterfall City",
            "Halfway House", "Vorna Valley", "Noordwyk", "Kyalami", "Carlswald", "Fourways", "Randburg"]
    if extra:
        base = base + [x for x in extra if x not in base]
    return [{"@type": "City", "name": n} if n in ("Johannesburg", "Midrand", "Sandton", "Centurion")
            else {"@type": "Place", "name": n} for n in base]


def opening_hours():
    return [
        {"@type": "OpeningHoursSpecification",
         "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"],
         "opens": "07:00", "closes": "19:00"},
        {"@type": "OpeningHoursSpecification", "dayOfWeek": "Sunday", "opens": "08:00", "closes": "16:00"},
    ]


def local_business_schema():
    return {
        "@context": "https://schema.org",
        "@type": ["Plumber", "LocalBusiness"],
        "@id": f"{SITE}/#business",
        "name": BUSINESS,
        "alternateName": "Vincent K Plumbers Midrand",
        "description": ("Plumbing, gas geyser installation, geyser replacement, leak detection, paving, "
                        "brick laying, irrigation and water purification services in Midrand and Johannesburg, South Africa."),
        "url": f"{SITE}/",
        "logo": LOGO_URL,
        "image": [LOGO_URL],
        "telephone": PHONE_INTL,
        "priceRange": "$$",
        "currenciesAccepted": "ZAR",
        "paymentAccepted": "Cash, EFT, Bank Transfer, Card",
        "address": {"@type": "PostalAddress", "streetAddress": "505 Nancy Ndamase Street",
                    "addressLocality": "Midrand", "addressRegion": "Gauteng", "postalCode": "1685",
                    "addressCountry": "ZA"},
        "geo": {"@type": "GeoCoordinates", "latitude": -26.0206, "longitude": 28.1518},
        "hasMap": "https://www.google.com/maps/search/?api=1&query=Vincent+K+Plumbers+505+Nancy+Ndamase+Street+Klipfontein+View+Midrand+Johannesburg",
        "areaServed": area_served(),
        "openingHoursSpecification": opening_hours(),
        "sameAs": ["https://www.facebook.com/share/1CLg3WnacX/", "https://share.google/71GsegnOVWnSnEVxC"],
        "hasOfferCatalog": {
            "@type": "OfferCatalog",
            "name": "Plumbing, gas, leak detection and outdoor property services",
            "itemListElement": [
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Gas Geyser Installation",
                 "url": f"{SITE}/gas-geyser-installation-johannesburg.html"}},
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Geyser Replacement & Repair",
                 "url": f"{SITE}/geyser-replacement-johannesburg.html"}},
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "General Plumbing & Repairs",
                 "url": f"{SITE}/plumbing-johannesburg.html"}},
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Leak Detection",
                 "url": f"{SITE}/leak-detection-johannesburg.html"}},
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Paving & Brick Laying",
                 "url": f"{SITE}/paving-johannesburg.html"}},
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Irrigation Systems",
                 "url": f"{SITE}/irrigation-johannesburg.html"}},
                {"@type": "Offer", "itemOffered": {"@type": "Service", "name": "Water Purification",
                 "url": f"{SITE}/water-purification-johannesburg.html"}},
            ],
        },
    }


def website_schema():
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": f"{SITE}/#website",
        "url": f"{SITE}/",
        "name": BUSINESS,
        "inLanguage": "en-ZA",
        "publisher": {"@id": f"{SITE}/#business"},
    }


def webpage_schema(url, name, description):
    return {
        "@context": "https://schema.org",
        "@type": "WebPage",
        "url": url,
        "name": name,
        "description": description,
        "inLanguage": "en-ZA",
        "isPartOf": {"@id": f"{SITE}/#website"},
        "about": {"@id": f"{SITE}/#business"},
        "publisher": {"@id": f"{SITE}/#business"},
    }


def breadcrumb_schema(items):
    return {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [{"@type": "ListItem", "position": i + 1, "name": name, "item": url}
                            for i, (name, url) in enumerate(items)],
    }


def faq_schema(qas):
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}}
                       for q, a in qas],
    }


def service_schema(name, service_type, description, url, image, extra_areas=None):
    return {
        "@context": "https://schema.org",
        "@type": "Service",
        "name": name,
        "serviceType": service_type,
        "description": description,
        "url": url,
        "image": image,
        "provider": {"@id": f"{SITE}/#business"},
        "areaServed": area_served(extra_areas),
        "availableChannel": {
            "@type": "ServiceChannel",
            "servicePhone": {"@type": "ContactPoint", "telephone": PHONE_INTL,
                             "contactType": "customer service", "areaServed": "ZA",
                             "availableLanguage": ["English", "Zulu", "Sotho", "Afrikaans"]},
            "serviceUrl": url,
        },
        "offers": {"@type": "Offer", "priceCurrency": "ZAR",
                   "availability": "https://schema.org/InStock", "url": url,
                   "description": "Free written quote after an on-site assessment."},
    }


def head(title, description, canonical, og_title=None, og_desc=None, og_image=LOGO_URL, og_type="website",
         noindex=False, extra_ld=None, ga=True):
    og_title = og_title or title
    og_desc = og_desc or description
    robots = "noindex, follow" if noindex else "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"
    parts = ['<!DOCTYPE html>', '<html lang="en-ZA" class="scroll-smooth">', '<head>',
             '  <meta charset="UTF-8" />', '  <meta name="viewport" content="width=device-width, initial-scale=1.0" />',
             '  <meta http-equiv="X-UA-Compatible" content="IE=edge" />', '',
             f'  <title>{title}</title>', f'  <meta name="description" content="{description}" />',
             f'  <meta name="keywords" content="plumber Johannesburg, plumber Midrand, plumber near me, emergency plumber Johannesburg, {description[:60]}" />',
             '  <meta name="author" content="Vincent K Plumbers" />',
             f'  <meta name="robots" content="{robots}" />',
             f'  <link rel="canonical" href="{canonical}" />', '',
             GEO_META, '',
             '  <meta property="og:type" content="website" />',
             '  <meta property="og:locale" content="en_ZA" />',
             '  <meta property="og:site_name" content="Vincent K Plumbers" />',
             f'  <meta property="og:title" content="{og_title}" />',
             f'  <meta property="og:description" content="{og_desc}" />',
             f'  <meta property="og:image" content="{og_image}" />',
             '  <meta property="og:image:width" content="640" />',
             '  <meta property="og:image:height" content="640" />',
             '  <meta property="og:image:alt" content="Vincent K Plumbers — plumbing, gas geysers and paving in Johannesburg" />',
             f'  <meta property="og:url" content="{canonical}" />', '',
             '  <meta name="twitter:card" content="summary_large_image" />',
             f'  <meta name="twitter:title" content="{og_title}" />',
             f'  <meta name="twitter:description" content="{og_desc}" />',
             f'  <meta name="twitter:image" content="{og_image}" />', '',
             f'  <link rel="icon" type="image/jpeg" href="{LOGO}" />',
             f'  <link rel="apple-touch-icon" href="{LOGO}" />',
             '  <link rel="manifest" href="site.webmanifest" />',
             '  <meta name="theme-color" content="#0B1623" />', '',
             '  <link rel="preconnect" href="https://fonts.googleapis.com" />',
             '  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />',
             '  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&amp;family=Plus+Jakarta+Sans:wght@600;700;800&amp;display=swap" rel="stylesheet" />',
             '  <link rel="stylesheet" href="assets/css/site.css" />']
    if ga:
        parts.append(GS_SCRIPT)
    parts.append('</head>')
    return "\n".join(parts) + "\n"


def breadcrumb_nav(label):
    return (f'<nav aria-label="Breadcrumb" class="text-xs text-slate-400 mb-5"><ol class="flex flex-wrap items-center gap-2">'
            f'<li><a href="/" class="hover:text-sky-300 transition-colors">Home</a></li>'
            f'<li aria-hidden="true" class="text-slate-500">/</li>'
            f'<li aria-current="page" class="text-slate-200">{label}</li></ol></nav>')


def cta_call_button(location):
    return (f'<a href="tel:{PHONE_INTL}" onclick="trackConversion(\'phone_click\', {{location: \'{location}\'}})" '
            f'class="inline-flex items-center justify-center gap-2.5 px-6 py-4 rounded-xl bg-orange-600 hover:bg-orange-500 text-white font-bold shadow-lg shadow-orange-600/30 transition-all">'
            f'<svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg> '
            f'Call {PHONE}</a>')


def wa_button(location, message):
    wa_msg = message.replace(' ', '%20').replace('&', '%26').replace(',', '%2C').replace("'", '').replace('-', ' ')
    return (f'<a href="https://wa.me/{WHATSAPP}?text={wa_msg}" target="_blank" rel="noopener noreferrer" '
            f'onclick="trackConversion(\'whatsapp_click\', {{location: \'{location}\'}})" '
            f'class="inline-flex items-center justify-center gap-2.5 px-6 py-4 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold shadow-lg shadow-emerald-600/25 transition-all">'
            f'<svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path d="M12.031 2c-5.516 0-9.969 4.453-9.969 9.969 0 1.766.469 3.484 1.344 5l-1.406 5.156 5.281-1.391c1.469.797 3.109 1.219 4.75 1.219 5.516 0 9.969-4.453 9.969-9.969S17.547 2 12.031 2z"/></svg> '
            f'WhatsApp</a>')


def check_item(text):
    return (f'<li class="flex items-start gap-3"><span class="mt-0.5 w-5 h-5 rounded-full bg-emerald-100 text-emerald-700 flex items-center justify-center shrink-0">'
            f'<svg class="w-3 h-3" fill="none" stroke="currentColor" stroke-width="3" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7"/></svg></span>'
            f'<span>{text}</span></li>')


def hero_section(kicker, h1, intro, cta_phone_loc, wa_msg, image_src, image_srcset, image_alt,
                 image_w, image_h, points, breadcrumb_label=None):
    bc = breadcrumb_nav(breadcrumb_label) if breadcrumb_label else ""
    pts = "".join(
        f'<div class="flex items-start gap-2.5"><span class="w-8 h-8 rounded-lg bg-white/10 text-sky-300 flex items-center justify-center shrink-0">'
        f'<svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg></span>'
        f'<span><span class="block text-sm font-bold text-white leading-tight">{p[0]}</span><span class="block text-xs text-slate-400 mt-0.5">{p[1]}</span></span></div>'
        for p in points)
    return f'''<section class="relative hero-bg text-white overflow-hidden">
      <div class="absolute inset-0 blueprint-grid pointer-events-none"></div>
      <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-8 pb-14 sm:pb-16">
        {bc}
        <div class="grid lg:grid-cols-12 gap-10 lg:gap-12 items-center">
          <div class="lg:col-span-6 space-y-5">
            <span class="inline-flex items-center gap-2 px-3.5 py-1.5 rounded-full bg-white/10 border border-white/15 text-xs sm:text-sm font-medium text-sky-200">
              <svg class="w-4 h-4 text-orange-400 shrink-0" fill="currentColor" viewBox="0 0 20 20" aria-hidden="true"><path fill-rule="evenodd" d="M5.05 4.05a7 7 0 119.9 9.9L10 18.9l-4.95-4.95a7 7 0 010-9.9zM10 11a2 2 0 100-4 2 2 0 000 4z" clip-rule="evenodd"/></svg>
              {kicker}
            </span>
            <h1 class="font-display text-3xl sm:text-4xl lg:text-5xl font-extrabold tracking-tight leading-[1.08]">{h1}</h1>
            <p class="text-slate-300 text-base sm:text-lg max-w-2xl leading-relaxed">{intro}</p>
            <div class="flex flex-col sm:flex-row gap-3.5 pt-1">
              {cta_call_button(cta_phone_loc)}
              {wa_button('service_hero', wa_msg)}
            </div>
            <div class="grid sm:grid-cols-3 gap-4 pt-5 border-t border-white/10">
              {pts}
            </div>
          </div>
          <div class="lg:col-span-6">
            <div class="hero-shot aspect-[4/3] sm:aspect-[16/11]">
              <img src="{image_src}" srcset="{image_srcset}" sizes="(min-width: 1024px) 48vw, 100vw" width="{image_w}" height="{image_h}" alt="{image_alt}" fetchpriority="high" class="w-full h-full object-cover"  />
            </div>
          </div>
        </div>
      </div>
    </section>'''


def section_wrapper(content, bg="white", extra_class=""):
    bg_map = {"white": "bg-white", "slate": "bg-slate-50", "navy": "bg-[#0B1623]"}
    return f'<section class="py-14 sm:py-16 {bg_map.get(bg, bg)} border-y border-slate-200 {extra_class}">\n{content}\n    </section>'