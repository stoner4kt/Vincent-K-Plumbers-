#!/usr/bin/env python3
"""Assemble final HTML pages for the Vincent K Plumbers site.

This is a *build aid*, not a runtime dependency. It composes the shared
header/footer partials with per-page `head` JSON-LD and body sections so the
site stays consistent. The generated files are committed and served statically.

Usage:  python3 tools/build_pages.py
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import site_lib as L

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def read_partial(name):
    with open(os.path.join(ROOT, "_partials", name), encoding="utf-8") as f:
        return f.read()


HEADER = read_partial("header.html")
HEADER_GAL = read_partial("header-gallery.html")
FOOTER = read_partial("footer.html")


def page(head_html, body, header=HEADER):
    return (head_html + header + "\n  <main id=\"top\">\n" + body + "\n  </main>\n" + FOOTER +
            '\n  <script src="assets/js/site.js" defer></script>\n</body>\n</html>\n')


def write(filename, content):
    path = os.path.join(ROOT, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", filename)


SERVICE_AREAS = ["Klipfontein View", "Midrand", "Waterfall City", "Halfway House", "Vorna Valley",
                 "Noordwyk", "Kyalami", "Carlswald", "Glen Austin", "President Park", "Rabie Ridge",
                 "Ivory Park", "Tembisa", "Allandale", "Buccleuch", "Diepsloot", "Sunninghill",
                 "Lonehill", "Fourways", "Bryanston", "Sandton", "Woodmead", "Randburg", "Rosebank",
                 "Johannesburg CBD", "Edenvale", "Bedfordview", "Kempton Park", "Germiston",
                 "Alberton", "Roodepoort", "Soweto", "Centurion", "Olievenhoutbosch"]


def service_cards():
    """A grid of links to every service page, used inside more content."""
    items = [
        ("Blocked Drains", "blocked-drains-johannesburg.html", "Drain clearing"),
        ("Leak Detection", "leak-detection-johannesburg.html", "Leak detection"),
        ("Geyser Repair", "geyser-repair-johannesburg.html", "Geyser repair"),
        ("Geyser Replacement", "geyser-replacement-johannesburg.html", "Geyser replacement"),
        ("Solar Geyser Installation", "solar-geyser-installation-gauteng.html", "Solar geysers"),
        ("Burst Pipe Repair", "burst-pipe-repair-johannesburg.html", "Burst pipes"),
        ("Bathroom Renovations", "bathroom-renovations-johannesburg.html", "Bathroom plumbing"),
        ("Waterproofing", "waterproofing-johannesburg.html", "Waterproofing"),
        ("Gas Geyser Installation", "gas-geyser-installation-johannesburg.html", "Gas geysers"),
        ("General Plumbing & Repairs", "plumbing-johannesburg.html", "General plumbing"),
        ("Paving & Brick Laying", "paving-johannesburg.html", "Paving"),
        ("Irrigation Systems", "irrigation-johannesburg.html", "Irrigation"),
        ("Water Purification", "water-purification-johannesburg.html", "Water purification"),
    ]
    cards = []
    for name, href, _kw in items:
        cards.append(
            f'<a href="{href}" class="service-card group bg-white rounded-2xl border border-slate-200 p-6 flex flex-col hover:border-sky-300">'
            f'<span class="w-11 h-11 rounded-xl bg-sky-50 text-sky-700 flex items-center justify-center mb-4 group-hover:bg-sky-600 group-hover:text-white transition-colors">'
            f'<svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M12 2.25A6.75 6.75 0 0012 15.75a6.75 6.75 0 000-13.5zM12 15.75v6M8.25 21.75h7.5"/></svg></span>'
            f'<h3 class="font-display font-extrabold text-lg text-slate-900">{name}</h3>'
            f'<p class="text-sm text-slate-600 mt-2 flex-1">{_kw} for homes and businesses across Johannesburg and Midrand.</p>'
            f'<span class="mt-4 inline-flex items-center gap-1.5 text-sm font-bold text-sky-700">View service'
            f'<svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M13 7l5 5m0 0l-5 5m5-5H6"/></svg></span></a>')
    return "\n".join(cards)


def trust_strip():
    return ('''<section class="bg-white border-b border-slate-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        <div class="grid grid-cols-2 lg:grid-cols-4 gap-6">
          <div class="flex flex-col lg:flex-row items-center gap-3">
            <div class="w-11 h-11 rounded-xl bg-sky-50 text-sky-600 flex items-center justify-center shrink-0"><svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M3.75 13.5l10.5-11.25L12 10.5h8.25L9.75 21.75 12 13.5H3.75z"/></svg></div>
            <div class="text-center lg:text-left">
              <p class="font-display font-extrabold text-slate-900 text-base sm:text-lg">Local Johannesburg Plumber</p>
              <p class="text-xs text-slate-500">Based in Klipfontein View, Midrand</p>
            </div>
          </div>
          <div class="flex flex-col lg:flex-row items-center gap-3">
            <div class="w-11 h-11 rounded-xl bg-sky-50 text-sky-600 flex items-center justify-center shrink-0"><svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M6.429 9.75L2.25 12l4.179 2.25m0-4.5l5.571 3 5.571-3m-11.142 0L2.25 7.5 12 2.25l9.75 5.25-4.179 2.25m0 0L21.75 12l-4.179 2.25m0 0l-4.179 2.25L8.25 16.5m9.321-2.25L21.75 16.5 12 21.75 2.25 16.5l4.179-2.25"/></svg></div>
            <div class="text-center lg:text-left">
              <p class="font-display font-extrabold text-slate-900 text-base sm:text-lg">Emergency Plumbing</p>
              <p class="text-xs text-slate-500">Same-day dispatch for urgent jobs</p>
            </div>
          </div>
          <div class="flex flex-col lg:flex-row items-center gap-3">
            <div class="w-11 h-11 rounded-xl bg-sky-50 text-sky-600 flex items-center justify-center shrink-0"><svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z"/></svg></div>
            <div class="text-center lg:text-left">
              <p class="font-display font-extrabold text-slate-900 text-base sm:text-lg">Leak Detection</p>
              <p class="text-xs text-slate-500">Find hidden leaks before digging</p>
            </div>
          </div>
          <div class="flex flex-col lg:flex-row items-center gap-3">
            <div class="w-11 h-11 rounded-xl bg-sky-50 text-sky-600 flex items-center justify-center shrink-0"><svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6v12m-3-2.818l.879.659c1.171.879 3.07.879 4.242 0 1.172-.879 1.172-2.303 0-3.182C13.536 12.219 12.768 12 12 12c-.725 0-1.45-.22-2.003-.659-1.106-.879-1.106-2.303 0-3.182s2.9-.879 4.006 0l.415.33M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg></div>
            <div class="text-center lg:text-left">
              <p class="font-display font-extrabold text-slate-900 text-base sm:text-lg">Transparent Pricing</p>
              <p class="text-xs text-slate-500">Clear quote before work starts</p>
            </div>
          </div>
        </div>
      </div>
    </section>''')


def include_card_section(title, subtitle, cards):
    return (f'<section class="py-14 bg-white border-y border-slate-200">'
            f'<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">'
            f'<div class="flex items-end justify-between gap-4 mb-8 reveal">'
            f'<div><span class="text-xs font-bold uppercase tracking-widest text-sky-600">One team, more than one trade</span>'
            f'<h2 class="font-display text-2xl sm:text-3xl font-extrabold text-slate-900 mt-1">{title}</h2>'
            f'<p class="text-slate-600 mt-2 text-sm sm:text-base max-w-2xl">{subtitle}</p></div>'
            f'<a href="index.html#services" class="hidden sm:inline-flex text-sm font-bold text-sky-700 hover:text-sky-900">All services &rarr;</a>'
            f'</div><div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-5">{cards}</div></div></section>')


def quote_cta_section():
    return ('''<section class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-16">
      <div class="rounded-3xl bg-gradient-to-r from-sky-600 to-sky-800 text-white p-8 sm:p-12 flex flex-col lg:flex-row items-center justify-between gap-8 shadow-xl reveal">
        <div class="text-center lg:text-left max-w-2xl">
          <h2 class="font-display text-2xl sm:text-4xl font-extrabold">Ready to solve your plumbing, gas or paving project?</h2>
          <p class="text-sky-100 mt-2 text-sm sm:text-base">Speak directly with the team that will do the work. Honest advice, upfront pricing and fast scheduling across Midrand and Johannesburg.</p>
        </div>
        <div class="flex flex-col sm:flex-row gap-3.5 shrink-0 w-full sm:w-auto">
          <a href="tel:+27681343276" onclick="trackConversion('phone_click', {location: 'bottom_cta'})" class="px-7 py-4 rounded-xl bg-white text-slate-900 hover:bg-slate-100 font-extrabold text-center shadow-lg transition">Call 068 134 3276</a>
          <a href="https://wa.me/27681343276?text=Hi%20Vincent%20K%20Plumbers%2C%20I%20would%20like%20a%20quote." target="_blank" rel="noopener noreferrer" onclick="trackConversion('whatsapp_click', {location: 'bottom_cta'})" class="px-7 py-4 rounded-xl bg-orange-600 hover:bg-orange-500 text-white font-extrabold text-center shadow-lg transition">WhatsApp Us</a>
        </div>
      </div>
    </section>''')


def quote_form_section(service_name):
    """A compact quote request form used at the bottom of service pages."""
    return f'''<section id="quote-form" class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pb-16">
      <div class="rounded-3xl border border-slate-200 bg-white shadow-xl overflow-hidden grid lg:grid-cols-2 reveal">
        <div class="bg-[#0B1623] text-white p-8 sm:p-12 flex flex-col justify-between">
          <div>
            <span class="inline-block px-3 py-1 rounded-full bg-sky-500/20 text-sky-300 text-xs font-bold uppercase tracking-wider">Get a quote</span>
            <h2 class="font-display text-2xl sm:text-3xl font-extrabold mt-4">Request a free quote for {service_name.lower()}</h2>
            <p class="text-slate-300 text-sm sm:text-base mt-3 leading-relaxed">Tell us what is happening and we will come back to you with a straight answer and a written quote. Prefer to talk? Call <a href="tel:+27681343276" class="text-sky-300 font-bold hover:text-sky-100" onclick="trackConversion('phone_click', {{location: 'quote_form'}})">068 134 3276</a>.</p>
          </div>
          <ul class="mt-8 space-y-3 text-sm text-slate-300">
            {L.check_item("We respond fast, usually the same day")}
            {L.check_item("No pressure and no call centre")}
            {L.check_item("Written quote before any work")}
          </ul>
        </div>
        <div class="p-8 sm:p-12">
          <form id="lead-form" name="quote-request" method="POST" action="/?success=true" data-netlify="true" netlify-honeypot="bot-field" class="space-y-3.5" novalidate>
            <p class="hidden" aria-hidden="true"><label>Don't fill this out if you're human: <input name="bot-field" /></label></p>
            <div>
              <label for="customer-name" class="block text-xs font-bold uppercase tracking-wide text-slate-500 mb-1.5">Your name</label>
              <input type="text" id="customer-name" name="name" required autocomplete="name" placeholder="e.g. Thabo Mokoena" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 text-sm focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition" />
            </div>
            <div class="grid sm:grid-cols-2 gap-3.5">
              <div>
                <label for="customer-phone" class="block text-xs font-bold uppercase tracking-wide text-slate-500 mb-1.5">Phone</label>
                <input type="tel" id="customer-phone" name="phone" required autocomplete="tel" placeholder="e.g. 082 123 4567" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 text-sm focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition" />
              </div>
              <div>
                <label for="customer-area" class="block text-xs font-bold uppercase tracking-wide text-slate-500 mb-1.5">Suburb</label>
                <input type="text" id="customer-area" name="area" required autocomplete="address-level2" placeholder="e.g. Midrand" class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 text-sm focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition" />
              </div>
            </div>
            <input type="hidden" id="service-hidden" name="service" value="{service_name}" />
            <div>
              <label for="customer-message" class="block text-xs font-bold uppercase tracking-wide text-slate-500 mb-1.5">How can we help?</label>
              <textarea id="customer-message" name="message" rows="3" placeholder="e.g. No hot water — the geyser is leaking into the drip tray." class="w-full px-3.5 py-2.5 rounded-xl border border-slate-300 text-sm focus:outline-none focus:ring-2 focus:ring-sky-500 focus:border-sky-500 transition"></textarea>
            </div>
            <button type="submit" class="w-full py-3.5 rounded-xl bg-orange-600 hover:bg-orange-500 text-white font-extrabold text-sm transition cursor-pointer">Request my free quote</button>
            <p id="form-feedback" class="hidden text-xs font-semibold rounded-lg p-3"></p>
          </form>
        </div>
      </div>
    </section>'''


def how_it_works_section(steps, title="From first call to finished job"):
    lis = []
    for i, (h, p) in enumerate(steps, 1):
        lis.append(
            f'<div class="reveal"><div class="flex items-center gap-3">'
            f'<span class="w-10 h-10 rounded-full bg-sky-600 text-white flex items-center justify-center font-display font-extrabold shrink-0">{i}</span>'
            f'<h3 class="font-display font-bold text-slate-900">{h}</h3></div>'
            f'<p class="text-sm text-slate-600 leading-relaxed mt-2">{p}</p></div>')
    return (f'<section class="py-14 sm:py-16">\n<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">'
            f'<div class="max-w-2xl mb-10 reveal"><span class="text-xs font-bold uppercase tracking-widest text-sky-600">Simple process</span>'
            f'<h2 class="font-display text-2xl sm:text-3xl font-extrabold text-slate-900 mt-1">{title}</h2></div>'
            f'<div class="grid sm:grid-cols-2 lg:grid-cols-4 gap-6">' + "".join(lis) + '</div></div></section>')


def faq_section(qas):
    items = []
    for idx, (q, a) in enumerate(qas):
        open_attr = ' aria-expanded="true"' if idx == 0 else ' aria-expanded="false"'
        rot = ' rotate-180' if idx == 0 else ''
        hidden = "" if idx == 0 else " hidden"
        items.append(
            f'<div class="faq-item bg-white border border-slate-200 rounded-2xl overflow-hidden">'
            f'<button type="button" class="faq-btn w-full px-5 sm:px-6 py-4 text-left flex items-center justify-between gap-4 font-display font-bold text-slate-900 cursor-pointer"{open_attr}>'
            f'<span>{q}</span><svg class="w-5 h-5 text-sky-600 shrink-0 transition-transform{rot}" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M19 9l-7 7-7-7"/></svg></button>'
            f'<div class="faq-panel{hidden} px-5 sm:px-6 pb-5 text-sm text-slate-600 leading-relaxed">{a}</div></div>')
    return (f'<section id="faq" class="py-16 max-w-4xl mx-auto px-4 sm:px-6 lg:px-8">'
            f'<div class="text-center mb-10 reveal"><span class="text-xs font-bold uppercase tracking-widest text-sky-600">Quick Answers</span>'
            f'<h2 class="font-display text-2xl sm:text-3xl font-extrabold text-slate-900 mt-1">Frequently asked questions</h2></div>'
            f'<div class="space-y-3 reveal">' + "".join(items) + '</div></section>')


def intros_then_whats_included(intro_paras, included_items, cta_loc, cta_label="Get a free quote"):
    paras = "".join(f'<p class="text-slate-600 leading-relaxed">{p}</p>' for p in intro_paras)
    checks = "".join(L.check_item(i) for i in included_items)
    return f'''<section class="py-14 sm:py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid lg:grid-cols-12 gap-10 items-start">
          <div class="lg:col-span-7 space-y-4 reveal">
            <span class="text-xs font-bold uppercase tracking-widest text-sky-600">What you get</span>
            <h2 class="font-display text-2xl sm:text-3xl font-extrabold text-slate-900">A local plumber who arrives when promised</h2>
            {paras}
          </div>
          <div class="lg:col-span-5 reveal">
            <div class="bg-white rounded-2xl border border-slate-200 p-6 sm:p-7 shadow-sm">
              <h2 class="font-display font-extrabold text-lg text-slate-900">What is included</h2>
              <ul class="mt-4 space-y-3 text-sm text-slate-700">{checks}</ul>
              <a href="tel:+27681343276" onclick="trackConversion('phone_click', {{location: '{cta_loc}'}})" class="mt-5 w-full inline-flex items-center justify-center gap-2 px-5 py-3 rounded-xl bg-[#0B1623] hover:bg-sky-700 text-white font-bold text-sm transition">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/></svg> {cta_label}
              </a>
            </div>
          </div>
        </div>
      </div>
    </section>'''


def related_links_grid(related):
    """related: list of (name, href, blurb)"""
    cards = []
    for name, href, blurb in related:
        cards.append(
            f'<a href="{href}" class="service-card group bg-white rounded-2xl border border-slate-200 p-6 flex flex-col hover:border-sky-300">'
            f'<span class="w-11 h-11 rounded-xl bg-sky-50 text-sky-700 flex items-center justify-center mb-4 group-hover:bg-sky-600 group-hover:text-white transition-colors">'
            f'<svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M13 7l5 5m0 0l-5 5m5-5H6"/></svg></span>'
            f'<h3 class="font-display font-extrabold text-lg text-slate-900">{name}</h3>'
            f'<p class="text-sm text-slate-600 mt-2 flex-1">{blurb}</p>'
            f'<span class="mt-4 inline-flex items-center gap-1.5 text-sm font-bold text-sky-700">View service'
            f'<svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M13 7l5 5m0 0l-5 5m5-5H6"/></svg></span></a>')
    return (f'<section class="py-14 bg-white border-y border-slate-200">'
            f'<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">'
            f'<div class="flex items-end justify-between gap-4 mb-8 reveal">'
            f'<div><span class="text-xs font-bold uppercase tracking-widest text-sky-600">Keep exploring</span>'
            f'<h2 class="font-display text-2xl sm:text-3xl font-extrabold text-slate-900 mt-1">Related services</h2></div>'
            f'<a href="index.html#services" class="hidden sm:inline-flex text-sm font-bold text-sky-700 hover:text-sky-900">All services &rarr;</a></div>'
            f'<div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-5">' + "".join(cards) + '</div></div></section>')