"""Guides / blog section: index page plus five full starter articles."""
import build_pages as B
import site_lib as L
from content import GUIDES


def simple_hero(title, subtitle):
    return f'''<section class="relative hero-bg text-white overflow-hidden">
      <div class="absolute inset-0 blueprint-grid pointer-events-none"></div>
      <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 pt-14 pb-14 sm:pb-16">
        <div class="max-w-3xl">
          <h1 class="font-display text-3xl sm:text-4xl lg:text-5xl font-extrabold tracking-tight leading-[1.08]">{title}</h1>
          <p class="text-slate-300 text-base sm:text-lg mt-4 max-w-2xl leading-relaxed">{subtitle}</p>
        </div>
      </div>
    </section>'''


def article(content_html, slug, title, desc, breadcrumb_label):
    url = f"{L.SITE}/guides/{slug}.html"
    head = L.head(title, desc, url)
    body = f'''{simple_hero(title, desc)}
    <section class="py-14 sm:py-16">
      <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8">
        <nav aria-label="Breadcrumb" class="text-xs text-slate-400 mb-6"><ol class="flex flex-wrap items-center gap-2">
          <li><a href="/" class="hover:text-sky-300 transition-colors">Home</a></li>
          <li aria-hidden="true" class="text-slate-500">/</li>
          <li><a href="guides.html" class="hover:text-sky-300 transition-colors">Guides</a></li>
          <li aria-hidden="true" class="text-slate-500">/</li>
          <li aria-current="page" class="text-slate-200">{breadcrumb_label}</li>
        </ol></nav>
        <article class="prose-custom space-y-6 text-slate-700 leading-relaxed text-[15px] sm:text-base">
{content_html}
        </article>
        <div class="mt-12 rounded-3xl bg-gradient-to-r from-sky-600 to-sky-800 text-white p-7 sm:p-9 flex flex-col sm:flex-row items-center justify-between gap-5">
          <div>
            <h2 class="font-display text-xl sm:text-2xl font-extrabold">Need a hand with this?</h2>
            <p class="text-sky-100 text-sm mt-1">Call or WhatsApp Vincent K Plumbers — we respond fast.</p>
          </div>
          <a href="tel:+27681343276" onclick="trackConversion('phone_click', {{location: 'guide_cta'}})" class="px-6 py-3.5 rounded-xl bg-white text-slate-900 hover:bg-slate-100 font-extrabold whitespace-nowrap transition">Call 068 134 3276</a>
        </div>
      </div>
    </section>''' + B.related_links_grid([("Back to guides", "guides.html", "Browse all articles."),
                                          ("Blocked Drains", "blocked-drains-johannesburg.html", "Fast drain clearing."),
                                          ("Leak Detection", "leak-detection-johannesburg.html", "Find hidden leaks.")])
    ld = [L.webpage_schema(url, title, desc),
          L.breadcrumb_schema([("Home", f"{L.SITE}/"), ("Guides", f"{L.SITE}/guides.html"), (breadcrumb_label, url)])]
    head = head.replace("</head>", "\n".join(L.json_ld(x) for x in ld) + "\n</head>")
    return B.page(head, body)


def guides_index():
    url = f"{L.SITE}/guides.html"
    title = "Plumbing Guides & Tips | Vincent K Plumbers Johannesburg"
    desc = "Practical plumbing guides for Johannesburg homeowners: geysers, hidden leaks, blocked drains, plumbing emergencies and more. From Vincent K Plumbers."
    cards = ""
    for slug, label, cat in GUIDES:
        cards += (f'<a href="guides/{slug}.html" class="service-card group bg-white rounded-2xl border border-slate-200 p-7 flex flex-col hover:border-sky-300">'
                  f'<span class="w-11 h-11 rounded-xl bg-sky-50 text-sky-700 flex items-center justify-center mb-4 group-hover:bg-sky-600 group-hover:text-white transition-colors">'
                  f'<svg class="w-6 h-6" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6.042A8.967 8.967 0 006 3.75c-1.052 0-2.062.18-3 .512v14.25A8.987 8.987 0 016 18c2.305 0 4.408.867 6 2.292m0-14.25a8.966 8.966 0 016-2.292c1.052 0 2.062.18 3 .512v14.25A8.987 8.987 0 0018 18a8.967 8.967 0 00-6 2.292m0-14.25v14.25"/></svg></span>'
                  f'<h2 class="font-display text-lg font-extrabold text-slate-900 group-hover:text-sky-700 transition-colors">{label}</h2>'
                  f'<p class="text-sm text-slate-600 mt-2 flex-1">{SUMMARY[slug]}</p>'
                  f'<span class="mt-4 inline-flex items-center gap-1.5 text-sm font-bold text-sky-700">Read the guide'
                  f'<svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2.2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M13 7l5 5m0 0l-5 5m5-5H6"/></svg></span></a>')
    body = f'''{simple_hero("Plumbing Guides &amp; Tips for Johannesburg", "Straightforward, practical advice written for local homeowners — from geyser failures and hidden leaks to blocked drains and plumbing emergencies.")}
    <section class="py-14 sm:py-16">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="max-w-2xl mb-10 reveal">
          <span class="text-xs font-bold uppercase tracking-widest text-sky-600">Free advice</span>
          <h2 class="font-display text-2xl sm:text-3xl font-extrabold text-slate-900 mt-1">Starter guides for Johannesburg homeowners</h2>
          <p class="text-slate-600 mt-2 text-sm sm:text-base">Written by the team that does the work. No jargon, no scare tactics — just what to look for and what to do.</p>
        </div>
        <div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-5">{cards}</div>
      </div>
    </section>''' + B.faq_section([
        ("Do you charge for advice?", "No. If you call with a question, we help you understand what you are dealing with before any work is booked."),
        ("Can I use these guides to fix it myself?", "Some small jobs are DIY-friendly for confident homeowners, but anything involving gas, live wiring or municipal water lines is best left to a qualified person. You are welcome to ask us first."),
        ("What if I am not sure which service I need?", "Call 068 134 3276 and describe the problem. We will point you to the right service and help you decide the next step."),
    ]) + B.quote_cta_section()
    head = L.head(title, desc, url)
    ld = [L.webpage_schema(url, title, desc),
          L.breadcrumb_schema([("Home", f"{L.SITE}/"), ("Guides", url)])]
    head = head.replace("</head>", "\n".join(L.json_ld(x) for x in ld) + "\n</head>")
    return B.page(head, body)


# ---------------------------------------------------------------- article bodies
def _p(*paras):
    return "\n".join(f"<p>{x}</p>" for x in paras)


def _h2(text):
    return f"<h2 class=\"font-display text-xl sm:text-2xl font-extrabold text-slate-900 mt-10 mb-3\">{text}</h2>"


def _h3(text):
    return f"<h3 class=\"font-display text-lg font-extrabold text-slate-900 mt-8 mb-2\">{text}</h3>"


def _ul(items):
    return "<ul class=\"list-disc pl-5 space-y-2 text-slate-700\">" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"


def _note():
    return "<p class=\"text-sm text-amber-800 bg-amber-50 border border-amber-200 rounded-xl p-4\">If you suspect a geyser failure right now, switch the geyser off at the isolator or mains and call <strong>068 134 3276</strong>.</p>"


def article_signs_geyser():
    body = article(
        f"""{_h2("Why geysers fail")}
{_p("In South African conditions, the hard water, pressure spikes and the sheer heat in the roof space all work against an electric geyser. Most geyser problems do not happen without warning — the signs are there for anyone who knows what to look for. Catching them early is the difference between a R500 repair and a flooded ceiling.")}
{_h2("The warning signs to take seriously")}
{_ul([
    "Water that is suddenly not as hot as it used to be, or that runs out quickly.",
    "A rumbling, popping or hissing sound from inside the tank — usually sediment heating up and boiling.",
    "Rust-coloured water from the hot taps, which points to the inside of the tank corroding.",
    "A visibly wet or rusted drip tray, or water staining around the geyser.",
    "A heavily corroded or dripping temperature / pressure relief valve.",
    "The geyser drip tray filling regularly even when you are not using hot water.",
])}
{_h3("The geyser is leaking. What now?")}
{_p("A geyser that is actually leaking from the tank cannot be patched safely. The moment a steel tank starts weeping, it has corroded through, and it will only get worse. Switch the water and power off and have it assessed — the correct fix is a replacement, fitted with a fresh drip tray and safety valves.")}
{_h2("What to do before it goes")}
{_ul([
    "Keep the drip tray clear and the relief valve discharge pipe unblocked.",
    "Have the element, thermostat and sacrificial anode checked if the geyser is older than about five years.",
    "If you hear rumbling, book a flush and sediment check rather than waiting.",
    "Know where your geyser isolator is before you need it in an emergency.",
])}
{_note()}
{_h2("Geyser repair vs replacement")}
{_p("If the tank is sound, most faults are repairable: a dead element, a tripped thermostat, a worn relief valve. If the tank itself is leaking or badly corroded, replacement is the honest recommendation. A good plumber will tell you which without pushing either option — ask for a straight answer and a written quote.")}
{_p("Need an opinion on your geyser? Call 068 134 3276 and describe what you are seeing — we will help you decide whether to repair or replace.")}""",
        "signs-your-geyser-is-about-to-burst", "Signs your geyser is about to burst | Vincent K Plumbers",
        "Warning signs your geyser is about to burst: lukewarm water, rumbling, rust, a wet drip tray. Know what to do before it floods your ceiling.",
        "Signs your geyser is about to burst")
    return body


def article_hidden_leak():
    body = article(
        f"""{_h2("How a hidden leak hides")}
{_p("A hidden leak is water escaping somewhere you cannot see it: inside a wall, under a concrete slab, or in a garden pipe. It can run for weeks or months before anyone notices, wasting thousands of litres and quietly damaging the structure of the house.")}
{_h2("Five signs you may have a hidden leak")}
{_ul([
    "Your water bill jumps even though your usage has not changed.",
    "The water meter keeps turning when every tap and appliance is off.",
    "A patch of wall or floor is permanently damp, even in a dry spell.",
    "Tiles feel warm in one spot, or grout keeps cracking and lifting.",
    "Paving sinks, or a patch of garden is unusually lush and soggy.",
])}
{_h2("How to check your meter yourself")}
{_p("A quick test: note the meter reading, turn off all taps and any automatic irrigation, flush toilets and make sure nothing is running. Wait 30 minutes and read the meter again. If it moved, water is going somewhere it should not be.")}
{_h3("Then check the usual suspects")}
{_ul([
    "Toilet cisterns — a slowly weeping valve is one of the most common silent leaks.",
    "The geyser overflow pipe dripping onto the roof.",
    "Outside taps and irrigation valves that are not sealing fully.",
])}
{_h2("Finding a leak without breaking everything")}
{_p("Once the obvious suspects are ruled out, a hidden leak in the walls, slab or garden needs proper locating. Acoustic listening, moisture meters and careful pressure testing pinpoint where the water is running. Only then is the smallest necessary opening made for the repair.")}
{_p("This is exactly what leak detection is for. If your meter test or the signs above point to a hidden leak, call 068 134 3276 — the sooner it is found, the less damage it does and the cheaper it is to fix.")}""",
        "how-to-find-a-hidden-leak", "How to find a hidden water leak | Vincent K Plumbers",
        "How to find a hidden water leak: check your meter, watch for damp walls and warm tiles, and know when to call a leak detection plumber in Johannesburg.",
        "How to find a hidden water leak")
    return body


def article_blocked_drain():
    body = article(
        f"""{_h2("Why drains block in the first place")}
{_p("A drain does not usually block overnight. It is a build-up over time — the last bit of fat from the pan, a nappy or wipe the flush could not handle, or roots slowly growing into an old clay pipe. Once the pipe narrows enough, the next thing you pour down it becomes the final straw.")}
{_h2("The main causes")}
{_ul([
    "Cooking fats and oils that cool and harden inside the pipe.",
    "Hair, soap scum and toilet paper that snag in a rough pipe.",
    "Flushable wipes and sanitary products that do not actually break down.",
    "Tree roots growing into older clay or concrete pipes.",
    "A collapsed or displaced pipe section that catches everything.",
    "Foreign objects — from toys to jewellery — that get flushed or dropped.",
])}
{_h2("What to do when your drain blocks")}
{_ul([
    "Stop using the sink, toilet or drain immediately.",
    "Do not keep flushing in the hope it clears — you may overflow it.",
    "Try a plunger for a single sink or toilet blockage, with the overflow covered.",
    "Avoid dumping chemical drain cleaners down repeatedly; they can damage pipes.",
])}
{_h3("When it is the main drain")}
{_p("If multiple fixtures back up at once, or water rises in the gully or manhole outside, the blockage is in the main drain or sewer line — not in one fixture. This needs proper clearing with drain rods or high-pressure jetting, and the cause needs to be identified so it does not return.")}
{_h2("Clearing the line properly")}
{_p("Professional drain clearing starts by locating the blockage, then clearing it with the right tool and confirming the line runs freely. Where the pipe itself is damaged by roots or collapse, the line is repaired rather than only rodded. It costs more upfront, but it stops the blockage coming back every few months.")}
{_p("If your drains are slow or backing up, call 068 134 3276 before it becomes a full sewage emergency.")}""",
        "blocked-main-drain-causes-and-what-to-do", "Blocked main drain: causes & what to do | Vincent K Plumbers",
        "Blocked main drain? Learn the common causes — fat, roots, wipes, collapsed pipes — and exactly what to do before it becomes a sewer emergency.",
        "Blocked main drain: causes and what to do")
    return body


def article_solar_vs_gas():
    body = article(
        f"""{_h2("The three options")}
{_p("If your electric geyser is at the end of its life, you have three practical routes in South Africa: replace it with a new electric geyser, switch to gas, or install solar. Each suits a different budget, home and lifestyle. Here is a straight comparison.")}
{_h3("Electric geysers")}
{_ul([
    "Lowest upfront cost and easiest to install in most homes.",
    "Running costs are high, and they stop when the grid stops.",
    "Best choice when budget is the main concern and load shedding is managed.",
])}
{_h3("Gas geysers")}
{_ul([
    "Heats water on demand and works during load shedding.",
    "Ideal for households that need hot water regardless of the grid.",
    "Running cost depends on gas and usage; requires good ventilation and flueing.",
])}
{_h3("Solar geysers")}
{_ul([
    "Uses free solar energy during the day, cutting running costs substantially in Gauteng.",
    "Produces most of your daytime hot water and works through load shedding (the tank stores heated water).",
    "Higher upfront cost, but the system pays back over time in reduced usage.",
])}
{_h2("Which one suits your home?")}
{_p("There is no single right answer. It comes down to how many people are in the house, how much hot water you use, when you use it, your roof situation and your budget. A shower-heavy family in the mornings may favour gas or a well-sized solar system with an electric backup; a couple with a small tank may barely notice a modern electric geyser's costs.")}
{_h2("Get an honest comparison for your property")}
{_p("We install electric, gas and solar systems and retrofit solar kits onto existing geysers. Because we do all three, we can compare them honestly for your specific home rather than selling you whatever brand we happen to stock.")}
{_p("Call 068 134 3276 to talk through your hot water options, or see our gas and solar installation pages for what's included.")}""",
        "solar-vs-electric-vs-gas-geysers", "Solar vs electric vs gas geysers | Vincent K Plumbers",
        "Solar vs electric vs gas geysers: upfront cost, running costs, load-shedding performance and which hot water system suits a Johannesburg home.",
        "Solar vs electric vs gas geysers")
    return body


def article_emergency():
    body = article(
        f"""{_h2("Stay calm, then act")}
{_p("Not every plumbing issue is an emergency, but when water is pouring out of a pipe, a geyser or a ceiling, every minute matters. The first steps you take decide how much damage is done.")}
{_h2("Step 1 — Stop the water")}
{_ul([
    "Find the main stopcock (usually outside near the boundary or under a sink) and turn it off.",
    "For a geyser leak or burst geyser pipe, turn off the water supply to the geyser and switch off the geyser at its own isolator or at the DB board.",
    "Do not put your hand in standing water near any electrical switch or appliance.",
])}
{_h2("Step 2 — Reduce the damage")}
{_ul([
    "Switch off power to affected rooms if water is near sockets or switches.",
    "Move valuables, electronics and furniture out of the water's path.",
    "Place a bucket or container under a manageable drip to slow floor damage.",
    "Clear the area so the plumber can get straight to the problem.",
])}
{_h2("Step 3 — Call a plumber")}
{_p("Call 068 134 3276. Describe what is happening, whether the water is off, and where the problem is. A good plumber will talk you through isolating the water on the phone and come prepared for the likely cause.")}
{_h2("When is it a true emergency?")}
{_ul([
    "Burst pipes — water escaping from a pipe, especially in the ceiling or walls.",
    "A geyser leaking or burst — hundreds of litres of stored, heated water.",
    "Sewage backing up into the home, toilets, baths or showers.",
    "Water leaking near electrical fittings, plugs or the DB board.",
])}
{_h2("After the emergency")}
{_p("Once the leak is stopped and repaired, dry the area out properly and document the damage with photos. If you claim on insurance, your policy will usually want a clear record of what happened and what was repaired. A written statement of the plumbing work carried out helps.")}
{_p("Keep our number where you can find it in a hurry: <strong>068 134 3276</strong> (call or WhatsApp).")}""",
        "what-to-do-in-a-plumbing-emergency", "What to do in a plumbing emergency | Vincent K Plumbers",
        "What to do in a plumbing emergency in Johannesburg: stop the water, cut the power, reduce damage and call 068 134 3276. A simple step-by-step.",
        "What to do in a plumbing emergency")
    return body


def fix_subdir_links(content):
    """Rewrite relative URLs in pages nested under guides/ to ../ form."""
    import re as _re
    content = content.replace('href="assets/', 'href="../assets/')
    content = content.replace('src="assets/', 'src="../assets/')
    content = content.replace('href="images/', 'href="../images/')
    content = content.replace('src="images/', 'src="../images/')
    content = content.replace('href="site.webmanifest"', 'href="../site.webmanifest"')
    # root-level page links
    for slug, _label, _cat in GUIDES:
        content = content.replace(f'href="guides/{slug}.html"', f'href="{slug}.html"')
    content = content.replace('href="guides.html"', 'href="../guides.html"')
    root_pages = ["index.html", "gallery.html", "about.html", "contact.html",
                  "reviews.html", "service-areas.html", "blocked-drains-johannesburg.html",
                  "geyser-repair-johannesburg.html", "geyser-replacement-johannesburg.html",
                  "leak-detection-johannesburg.html", "solar-geyser-installation-gauteng.html",
                  "burst-pipe-repair-johannesburg.html", "bathroom-renovations-johannesburg.html",
                  "waterproofing-johannesburg.html", "plumbing-johannesburg.html",
                  "gas-geyser-installation-johannesburg.html", "paving-johannesburg.html",
                  "irrigation-johannesburg.html", "water-purification-johannesburg.html"]
    for p in root_pages:
        # exact and hash-anchored variants
        content = content.replace(f'href="{p}"', f'href="../{p}"')
        content = content.replace(f'href="{p}#', f'href="../{p}#')
    return content


SUMMARY = {
    "signs-your-geyser-is-about-to-burst": "Lukewarm water, rumbling, rust, a wet drip tray — spot the warning signs before the tank bursts.",
    "how-to-find-a-hidden-leak": "High water bill or damp walls? How to test your meter and find a hidden leak before it damages your home.",
    "blocked-main-drain-causes-and-what-to-do": "Fat, roots, wipes and collapsed pipes — the common causes of a blocked main drain and what to do.",
    "solar-vs-electric-vs-gas-geysers": "A plain-language comparison of upfront cost, running costs and load shedding for hot water systems.",
    "what-to-do-in-a-plumbing-emergency": "A simple step-by-step for a burst pipe or geyser leak — what to do in the first few minutes.",
}

ARTICLES = [
    ("signs-your-geyser-is-about-to-burst", article_signs_geyser),
    ("how-to-find-a-hidden-leak", article_hidden_leak),
    ("blocked-main-drain-causes-and-what-to-do", article_blocked_drain),
    ("solar-vs-electric-vs-gas-geysers", article_solar_vs_gas),
    ("what-to-do-in-a-plumbing-emergency", article_emergency),
]


def build_all():
    B.write("guides.html", guides_index())
    import os
    os.makedirs(os.path.join(B.ROOT, "guides"), exist_ok=True)
    for slug, fn in ARTICLES:
        B.write(f"guides/{slug}.html", fix_subdir_links(fn()))
    print(f"guides_pages: 1 index + {len(ARTICLES)} articles written")


if __name__ == "__main__":
    build_all()