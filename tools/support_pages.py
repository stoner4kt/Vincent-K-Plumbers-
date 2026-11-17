"""Support pages: service areas, about, contact, reviews, and suburb pages."""
import build_pages as B
import site_lib as L
from build_pages import SERVICE_AREAS


def trust_strip():
    return B.trust_strip()


def simple_hero(title, subtitle, breadcrumb_label=None):
    bc = ""
    if breadcrumb_label:
        bc = (f'<nav aria-label="Breadcrumb" class="text-xs text-slate-400 mb-5"><ol class="flex flex-wrap items-center gap-2">'
              f'<li><a href="/" class="hover:text-sky-300 transition-colors">Home</a></li>'
              f'<li aria-hidden="true" class="text-slate-500">/</li>'
              f'<li aria-current="page" class="text-slate-200">{breadcrumb_label}</li></ol></nav>')
    return f'''<section class="relative hero-bg text-white overflow-hidden">
      <div class="absolute inset-0 blueprint-grid pointer-events-none"></div>
      <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-14 pb-14 sm:pb-16">
        {bc}
        <div class="max-w-3xl">
          <h1 class="font-display text-3xl sm:text-4xl lg:text-5xl font-extrabold tracking-tight leading-[1.08]">{title}</h1>
          <p class="text-slate-300 text-base sm:text-lg mt-4 max-w-2xl leading-relaxed">{subtitle}</p>
          <div class="flex flex-col sm:flex-row gap-3.5 mt-7">
            {L.cta_call_button('support_hero')}
            <a href="https://wa.me/27681343276?text=Hi%20Vincent%20K%20Plumbers%2C%20I%20would%20like%20a%20quote." target="_blank" rel="noopener noreferrer"
               onclick="trackConversion('whatsapp_click', {{location: 'support_hero'}})"
               class="inline-flex items-center justify-center gap-2.5 px-6 py-4 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold shadow-lg shadow-emerald-600/25 transition-all">
              <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path d="M12.031 2c-5.516 0-9.969 4.453-9.969 9.969 0 1.766.469 3.484 1.344 5l-1.406 5.156 5.281-1.391c1.469.797 3.109 1.219 4.75 1.219 5.516 0 9.969-4.453 9.969-9.969S17.547 2 12.031 2z"/></svg>
              WhatsApp Us
            </a>
          </div>
        </div>
      </div>
    </section>'''


def service_areas_page():
    url = f"{L.SITE}/service-areas.html"
    title = "Johannesburg Plumber Service Areas | Vincent K Plumbers"
    desc = "Vincent K Plumbers serves all seven Johannesburg regions, Midrand and surrounding Gauteng areas. Call 068 134 3276 to arrange plumbing service."
    chips = "".join(
        f'<li class="px-3.5 py-2 rounded-xl bg-white border border-slate-200 text-xs sm:text-sm font-semibold text-slate-800 shadow-2xs">{a}</li>'
        for a in SERVICE_AREAS
    )
    regions = [
        ("Region A — Midrand &amp; the North", "Midrand, Diepsloot, Ivory Park, Fourways, Sunninghill and Woodmead"),
        ("Region B — Randburg &amp; Northcliff", "Randburg, Northcliff, Rosebank, Bryanston and surrounding neighbourhoods"),
        ("Region C — Roodepoort &amp; the West", "Roodepoort, Florida, Northgate and Bram Fischerville"),
        ("Region D — Soweto", "Soweto, Diepkloof, Doornkop, Dube, Meadowlands and Orlando"),
        ("Region E — Sandton &amp; Alexandra", "Sandton, Alexandra, Wynberg, Norwood, Morningside and nearby suburbs"),
        ("Region F — Inner City &amp; Johannesburg South", "Johannesburg CBD, Newtown, Fordsburg, Mayfair, Berea, Hillbrow, Glenvista and Southgate"),
        ("Region G — Johannesburg Deep South", "Lenasia, Ennerdale, Orange Farm, Eldorado Park, Protea, Lawley and surrounding localities"),
    ]
    region_cards = "".join(
        f'<article class="rounded-2xl border border-slate-200 bg-white p-5 shadow-sm">'
        f'<h3 class="font-display text-base sm:text-lg font-extrabold text-slate-900">{name}</h3>'
        f'<p class="text-sm text-slate-600 mt-2 leading-relaxed">{areas}</p></article>'
        for name, areas in regions
    )
    body = simple_hero(
        "Plumber Serving Johannesburg &amp; Surrounding Areas",
        "Vincent K Plumbers is based in Klipfontein View, Midrand and provides plumbing and related property services throughout Johannesburg and nearby Gauteng areas.",
        breadcrumb_label="Service Areas"
    ) + trust_strip() + f''' 
    <section class="py-14 sm:py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="max-w-3xl mb-9 reveal">
          <span class="text-xs font-bold uppercase tracking-widest text-sky-600">Johannesburg-wide coverage</span>
          <h2 class="font-display text-2xl sm:text-3xl font-extrabold text-slate-900 mt-1">Plumbing services across all seven Johannesburg regions</h2>
          <p class="text-slate-600 mt-3 text-sm sm:text-base leading-relaxed">We serve homes and businesses throughout the City of Johannesburg, including its seven administrative regions. The localities below are examples of the areas within each region, not a suburb-by-suburb limit on coverage.</p>
        </div>
        <div class="grid md:grid-cols-2 xl:grid-cols-3 gap-4">{region_cards}</div>
      </div>
    </section>
    <section class="py-14 bg-slate-50 border-y border-slate-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="max-w-3xl mb-8 reveal">
          <span class="text-xs font-bold uppercase tracking-widest text-sky-600">Johannesburg &amp; nearby Gauteng</span>
          <h2 class="font-display text-2xl sm:text-3xl font-extrabold text-slate-900 mt-1">Areas we serve</h2>
          <p class="text-slate-600 mt-2 text-sm sm:text-base">Our coverage also includes surrounding areas such as Tembisa, Edenvale, Bedfordview, Kempton Park, Germiston, Alberton and Centurion.</p>
        </div>
        <ul class="flex flex-wrap gap-2.5">{chips}</ul>
        <p class="text-sm text-slate-600 mt-5"><a class="font-bold text-sky-700 hover:text-sky-900" href="waterproofing-johannesburg.html">View waterproofing services across Johannesburg &rarr;</a></p>
        <p class="text-sm text-slate-600 mt-6">Not sure which region your street falls in? Call or WhatsApp <a class="font-bold text-sky-700" href="tel:+27681343276">068 134 3276</a> and provide your suburb or address so we can arrange the right service.</p>
      </div>
    </section>
    <section class="py-14 bg-white border-b border-slate-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid lg:grid-cols-12 gap-8 items-center">
          <div class="lg:col-span-7 reveal">
            <span class="text-xs font-bold uppercase tracking-widest text-sky-600">Based in Klipfontein View</span>
            <h2 class="font-display text-2xl sm:text-3xl font-extrabold text-slate-900 mt-1">A Midrand base serving Greater Johannesburg</h2>
            <p class="text-slate-600 text-sm sm:text-base mt-3 leading-relaxed">Our business is based at 505 Nancy Ndamase Street in Klipfontein View, Midrand. From this base, we take bookings across Johannesburg and nearby Gauteng communities.</p>
            <p class="text-slate-600 text-sm sm:text-base mt-3 leading-relaxed">We provide plumbing, geyser, drain, leak detection, paving, irrigation and water purification services. Each service page explains the work available and how to request a quote.</p>
            <a href="index.html#contact" class="inline-flex items-center gap-2 mt-5 text-sm font-bold text-sky-700 hover:text-sky-900">See our contact details and map &rarr;</a>
          </div>
          <div class="lg:col-span-5 reveal">
            <div class="rounded-2xl overflow-hidden border border-slate-200 shadow-lg bg-slate-900 h-72">
              <iframe title="Vincent K Plumbers service area map - Klipfontein View, Midrand, Johannesburg" src="https://maps.google.com/maps?q=Vincent%20K%20Plumbers%2C%20505%20Nancy%20Ndamase%20Street%2C%20Klipfontein%20View%2C%20Midrand%2C%20Johannesburg%2C%20South%20Africa&amp;t=&amp;z=10&amp;ie=UTF8&amp;iwloc=&amp;output=embed" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
            </div>
          </div>
        </div>
      </div>
    </section>''' + B.related_links_grid([
        ("Blocked Drains", "blocked-drains-johannesburg.html", "Drain clearing across Johannesburg."),
        ("Geyser Repair", "geyser-repair-johannesburg.html", "Geyser diagnosis and repairs."),
        ("Bathroom Renovations", "bathroom-renovations-johannesburg.html", "Bathroom plumbing and installation."),
        ("Waterproofing", "waterproofing-johannesburg.html", "Damp, wet walls and water ingress.")
    ]) + B.quote_cta_section()
    head = L.head(title, desc, url)
    ld = [L.local_business_schema(), L.webpage_schema(url, title, desc),
          L.breadcrumb_schema([("Home", f"{L.SITE}/"), ("Service Areas", url)])]
    head = head.replace("</head>", "\n".join(L.json_ld(x) for x in ld) + "\n</head>")
    return B.page(head, body)

def suburb_page_placeholder(slug, suburb, primary_service, note):
    url = f"{L.SITE}/{slug}.html"
    title = f"Plumber in {suburb} | Vincent K Plumbers"
    desc = f"Plumbing, geysers, drains and more in {suburb}, Johannesburg. Call 068 134 3276 for a plumber near you. [VERIFY: confirm coverage]"
    h1 = f"Plumber in {suburb}, Johannesburg"
    body = f'''{simple_hero(h1, f"Looking for a plumber in {suburb}? Vincent K Plumbers serves {suburb} and surrounding Johannesburg suburbs for plumbing repairs, geysers, blocked drains and more.", breadcrumb_label=suburb)}
    {trust_strip()}
    <section class="py-14 sm:py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid lg:grid-cols-12 gap-10 items-start">
          <div class="lg:col-span-7 space-y-4 reveal">
            <span class="text-xs font-bold uppercase tracking-widest text-sky-600">Local coverage</span>
            <h2 class="font-display text-2xl sm:text-3xl font-extrabold text-slate-900 mt-1">Plumbing help close to home in {suburb}</h2>
            <p class="text-slate-600 leading-relaxed">[VERIFY coverage] We regularly work in {suburb}. If you live in the area and need a plumber, you are close to our Midrand base — which usually means a faster response.</p>
            <p class="text-slate-600 leading-relaxed">We handle {primary_service}, plus emergency call-outs, geyser repairs and general plumbing for homes and small businesses. Call 068 134 3276 to confirm we cover your exact street.</p>
            <div class="pt-4">
              <a href="tel:+27681343276" onclick="trackConversion('phone_click', {{location: 'suburb_page'}})" class="inline-flex items-center gap-2 px-6 py-4 rounded-xl bg-orange-600 hover:bg-orange-500 text-white font-bold shadow-lg transition">Call {L.PHONE}</a>
            </div>
          </div>
          <div class="lg:col-span-5 reveal">
            <div class="bg-white rounded-2xl border border-slate-200 p-6 sm:p-7 shadow-sm">
              <h2 class="font-display font-extrabold text-lg text-slate-900">Services we offer near you</h2>
              <ul class="mt-4 space-y-3 text-sm text-slate-700">
                {L.check_item("Emergency plumbing & burst pipes")}
                {L.check_item("Blocked drains and sewer lines")}
                {L.check_item("Leak detection and repairs")}
                {L.check_item("Geyser repair and replacement")}
                {L.check_item("Gas and solar geyser installation")}
                {L.check_item("Bathroom renovation plumbing")}
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>''' + B.how_it_works_section([
        ("Call or WhatsApp", "Tell us the problem and your street in " + suburb + "."),
        ("We confirm coverage", "We confirm we cover your area and a time slot."),
        ("Diagnose and quote", "We quote before any work starts."),
        ("Complete and test", "Fixed properly and tested before we leave."),
    ]) + B.related_links_grid([
        ("Blocked Drains", "blocked-drains-johannesburg.html", "Fast drain clearing."),
        ("Leak Detection", "leak-detection-johannesburg.html", "Find hidden leaks."),
        ("Geyser Repair", "geyser-repair-johannesburg.html", "Hot water, fixed."),
    ]) + B.quote_cta_section()
    head = L.head(title, desc, url)
    ld = [L.local_business_schema(), L.webpage_schema(url, title, desc),
          L.breadcrumb_schema([("Home", f"{L.SITE}/"), ("Service Areas", f"{L.SITE}/service-areas.html"), (suburb, url)])]
    head = head.replace("</head>", "\n".join(L.json_ld(x) for x in ld) + "\n</head>")
    return B.page(head, body)


def about_page():
    url = f"{L.SITE}/about.html"
    title = "About Vincent K Plumbers | Plumber in Midrand & Johannesburg"
    desc = "Meet Vincent K Plumbers: a local plumbing and construction team based in Klipfontein View, Midrand. Honest quotes, tidy work. Call 068 134 3276."
    body = simple_hero("About Vincent K Plumbers", "We are a hands-on plumbing, gas and construction team based in Klipfontein View, Midrand, serving Johannesburg and Gauteng.", breadcrumb_label="About") + trust_strip() + f'''
    <section class="py-14 sm:py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid lg:grid-cols-12 gap-10 items-start">
          <div class="lg:col-span-7 space-y-4 reveal">
            <span class="text-xs font-bold uppercase tracking-widest text-sky-600">Who we are</span>
            <h2 class="font-display text-2xl sm:text-3xl font-extrabold text-slate-900 mt-1">A local team that does the work itself</h2>
            <p class="text-slate-600 leading-relaxed">Vincent K Plumbers is a local service business based at 505 Nancy Ndamase Street in Klipfontein View, Midrand. We do plumbing, gas geyser installation and repair, leak detection, blocked drain clearing, paving, irrigation and water purification for homes and small businesses across Johannesburg and Midrand.</p>
            <p class="text-slate-600 leading-relaxed">[VERIFY: number of years in business / 22+ years experience — use only if the owner confirms] When you call, you speak to the team that will do the work. We give written quotes, arrive prepared, and clean up after ourselves.</p>
            <p class="text-slate-600 leading-relaxed">Our photos and videos on this site are from real Johannesburg properties we have worked on. We do not use stock images.</p>
            <div class="pt-4">
              <a href="tel:+27681343276" onclick="trackConversion('phone_click', {{location: 'about_page'}})" class="inline-flex items-center gap-2 px-6 py-4 rounded-xl bg-orange-600 hover:bg-orange-500 text-white font-bold shadow-lg transition">Call {L.PHONE}</a>
            </div>
          </div>
          <div class="lg:col-span-5 reveal">
            <div class="bg-white rounded-2xl border border-slate-200 p-6 sm:p-7 shadow-sm">
              <h2 class="font-display font-extrabold text-lg text-slate-900">What you can count on</h2>
              <ul class="mt-4 space-y-3 text-sm text-slate-700">
                {L.check_item("Written quotes before work starts")}
                {L.check_item("The team that answers is the team on site")}
                {L.check_item("Tidy, pressure-tested workmanship")}
                {L.check_item("Honest advice — repair vs replace")}
                {L.check_item("Site cleaned before we leave")}
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>''' + B.quote_cta_section() + B.related_links_grid([
        ("Service Areas", "service-areas.html", "Everywhere we work."),
        ("Project Gallery", "gallery.html", "Real work, real photos."),
        ("Reviews", "reviews.html", "What clients say."),
    ])
    head = L.head(title, desc, url)
    ld = [L.local_business_schema(), L.webpage_schema(url, title, desc),
          L.breadcrumb_schema([("Home", f"{L.SITE}/"), ("About", url)])]
    head = head.replace("</head>", "\n".join(L.json_ld(x) for x in ld if x) + "\n</head>")
    return B.page(head, body)


def contact_page():
    url = f"{L.SITE}/contact.html"
    title = "Contact Vincent K Plumbers | Plumber Johannesburg"
    desc = "Contact Vincent K Plumbers for plumbing, geyser, drain and construction work in Johannesburg. Call or WhatsApp 068 134 3276, or request a quote online."
    body = simple_hero("Contact Vincent K Plumbers", "Call, WhatsApp or send a quote request — whichever is easiest. We reply directly, not through a call centre.", breadcrumb_label="Contact") + trust_strip() + f'''
    <section class="py-14 sm:py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid lg:grid-cols-12 gap-10">
          <div class="lg:col-span-5 space-y-5 reveal">
            <h2 class="font-display text-2xl sm:text-3xl font-extrabold text-slate-900">Talk to us directly</h2>
            <div class="bg-white rounded-2xl border border-slate-200 p-6 shadow-sm">
              <ul class="space-y-4 text-sm">
                <li class="flex items-start gap-3">
                  <svg class="w-5 h-5 text-orange-500 shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg>
                  <div><p class="font-bold text-slate-900">Phone</p><a href="tel:+27681343276" class="text-slate-600 hover:text-sky-700">068 134 3276</a></div>
                </li>
                <li class="flex items-start gap-3">
                  <svg class="w-5 h-5 text-emerald-600 shrink-0 mt-0.5" fill="currentColor" viewBox="0 0 24 24" aria-hidden="true"><path d="M12.031 2c-5.516 0-9.969 4.453-9.969 9.969 0 1.766.469 3.484 1.344 5l-1.406 5.156 5.281-1.391c1.469.797 3.109 1.219 4.75 1.219 5.516 0 9.969-4.453 9.969-9.969S17.547 2 12.031 2z"/></svg>
                  <div><p class="font-bold text-slate-900">WhatsApp</p><a href="https://wa.me/27681343276?text=Hi%20Vincent%20K%20Plumbers%2C%20I%20would%20like%20a%20quote." target="_blank" rel="noopener noreferrer" class="text-slate-600 hover:text-sky-700">Chat on WhatsApp</a></div>
                </li>
                <li class="flex items-start gap-3">
                  <svg class="w-5 h-5 text-sky-500 shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/><path stroke-linecap="round" stroke-linejoin="round" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
                  <div><p class="font-bold text-slate-900">Address</p><p class="text-slate-600">505 Nancy Ndamase Street, Klipfontein View, Midrand, Johannesburg</p></div>
                </li>
                <li class="flex items-start gap-3">
                  <svg class="w-5 h-5 text-amber-500 shrink-0 mt-0.5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                  <div><p class="font-bold text-slate-900">Hours</p><p class="text-slate-600">Mon–Sat 07:00–19:00 · Sun 08:00–16:00</p></div>
                </li>
              </ul>
            </div>
          </div>
          <div class="lg:col-span-7 reveal">
            <div class="rounded-2xl overflow-hidden border border-slate-200 shadow-lg bg-slate-900 h-96">
              <iframe title="Vincent K Plumbers location map - 505 Nancy Ndamase Street, Klipfontein View, Midrand, Johannesburg" src="https://maps.google.com/maps?q=Vincent%20K%20Plumbers%2C%20505%20Nancy%20Ndamase%20Street%2C%20Klipfontein%20View%2C%20Midrand%2C%20Johannesburg%2C%20South%20Africa&t=&z=14&ie=UTF8&iwloc=&output=embed" width="100%" height="100%" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
            </div>
          </div>
        </div>
      </div>
    </section>''' + B.quote_cta_section()
    head = L.head(title, desc, url)
    ld = [L.local_business_schema(), L.webpage_schema(url, title, desc),
          L.breadcrumb_schema([("Home", f"{L.SITE}/"), ("Contact", url)])]
    head = head.replace("</head>", "\n".join(L.json_ld(x) for x in ld) + "\n</head>")
    return B.page(head, body)


def reviews_page():
    url = f"{L.SITE}/reviews.html"
    title = "Reviews | Vincent K Plumbers Johannesburg"
    desc = "Verified customer reviews for Vincent K Plumbers in Johannesburg and Midrand will appear here as they become available. Contact us on 068 134 3276."
    body = simple_hero("Client Reviews", "We value honest feedback. This page will grow as we collect verified reviews from real clients.", breadcrumb_label="Reviews") + trust_strip() + f'''
    <section class="py-14 sm:py-16">
      <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="rounded-3xl border-2 border-dashed border-slate-300 p-10 text-center reveal">
          <span class="mx-auto w-16 h-16 rounded-2xl bg-sky-50 text-sky-600 flex items-center justify-center">
            <svg class="w-8 h-8" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M11.48 3.499a.562.562 0 011.04 0l2.125 5.111a.563.563 0 00.475.345l5.518.442c.499.04.701.663.321.988l-4.204 3.602a.563.563 0 00-.182.557l1.285 5.385a.562.562 0 01-.84.61l-4.725-2.885a.563.563 0 00-.586 0L6.982 20.54a.562.562 0 01-.84-.61l1.285-5.386a.562.562 0 00-.182-.557l-4.204-3.602a.563.563 0 01.321-.988l5.518-.442a.563.563 0 00.475-.345L11.48 3.5z"/></svg>
          </span>
          <h2 class="font-display text-2xl sm:text-3xl font-extrabold text-slate-900 mt-4">Reviews coming soon</h2>
          <p class="text-slate-600 mt-3 text-sm sm:text-base max-w-xl mx-auto">We are collecting verified customer feedback before publishing reviews. No testimonials or star ratings are displayed yet. Please check back soon.</p>
          <div class="flex flex-wrap justify-center gap-3 mt-6">
            <a href="https://share.google/71GsegnOVWnSnEVxC" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 px-5 py-3 rounded-xl bg-slate-100 hover:bg-sky-50 text-slate-800 hover:text-sky-700 font-bold text-sm transition">Visit our Google Business Profile</a>
            <a href="https://www.facebook.com/share/1CLg3WnacX/" target="_blank" rel="noopener noreferrer" class="inline-flex items-center gap-2 px-5 py-3 rounded-xl bg-slate-100 hover:bg-sky-50 text-slate-800 hover:text-sky-700 font-bold text-sm transition">Find us on Facebook</a>
          </div>
        </div>
        <p class="text-center text-xs text-slate-500 mt-6">Note: we do not display fabricated reviews or star ratings. Every testimonial on this site must be real and verifiable.</p>
      </div>
    </section>''' + B.quote_cta_section()
    head = L.head(title, desc, url)
    ld = [L.local_business_schema(), L.webpage_schema(url, title, desc),
          L.breadcrumb_schema([("Home", f"{L.SITE}/"), ("Reviews", url)])]
    head = head.replace("</head>", "\n".join(L.json_ld(x) for x in ld) + "\n</head>")
    return B.page(head, body)


def build_all():
    files = {
        "service-areas.html": service_areas_page,
        "about.html": about_page,
        "contact.html": contact_page,
        "reviews.html": reviews_page,
    }
    for name, fn in files.items():
        B.write(name, fn())
    print(f"support_pages: {len(files)} support pages written")


if __name__ == "__main__":
    build_all()