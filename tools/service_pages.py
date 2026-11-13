"""Service page builders for the Vincent K Plumbers site.

Each service page gets: hero with H1 + CTA, intro + "what is included",
core-service detail, how-it-works, project gallery (property photos),
FAQ, related services, and a closing quote CTA, plus the full JSON-LD stack
(LocalBusiness, WebPage, Service, FAQPage, BreadcrumbList).
"""
import json as _json

import build_pages as B
import site_lib as L
from content import SERVICES, RELATED, HERO_IMAGES, WORK_IMAGES


def service_page(spec):
    slug = spec["slug"]
    url = f"{L.SITE}/{slug}.html"
    hero = HERO_IMAGES[slug]
    img_src, img_full, img_srcset_raw, img_w, img_h, img_alt = hero
    img_srcset = f"{img_src} 640w, {img_full} {img_w}w"
    rel = RELATED[slug]
    works = WORK_IMAGES[slug]

    faqs = FAQS[slug]
    steps = STEPS[slug]
    core = CORE[slug]

    inner = [
        L.hero_section(
            kicker=spec["kicker"],
            h1=spec["h1"],
            intro=INTROS[slug],
            cta_phone_loc="service_hero",
            wa_msg=f"Hi Vincent K Plumbers, I need help with {spec['eyebrow']}.",
            image_src=img_src,
            image_srcset=img_srcset,
            image_alt=img_alt,
            image_w=img_w,
            image_h=img_h,
            points=POINTS[slug],
            breadcrumb_label=spec["eyebrow"],
        ),
        B.trust_strip(),
        B.intros_then_whats_included(INTRO_PARAS[slug], INCLUDED[slug], cta_loc="service_included"),
        core_section(core),
        B.how_it_works_section(steps),
        work_section(works, spec["eyebrow"]),
        areas_teaser(spec["eyebrow"]),
        B.faq_section(faqs),
        B.related_links_grid(rel),
        B.quote_form_section(spec["eyebrow"]),
    ]
    body = "\n    ".join(inner)

    head = L.head(spec["title"], spec["desc"], url,
                  og_image=f"{L.SITE}/images/brand/logo.jpg")
    ld = [
        L.local_business_schema(),
        L.webpage_schema(url, spec["title"], spec["desc"]),
        L.service_schema(spec["eyebrow"], spec["eyebrow"], INTROS[slug], url,
                         f"{L.SITE}/{img_full}"),
        L.breadcrumb_schema([("Home", f"{L.SITE}/"), ("Services", f"{L.SITE}/#services"), (spec["eyebrow"], url)]),
        L.faq_schema(faqs),
    ]
    ld_html = "\n".join(L.json_ld(x) for x in ld if x)
    head_page = head.replace("</head>", ld_html + "\n</head>")
    return B.page(head_page, body)


def core_section(core):
    cards = []
    for h, p in core:
        cards.append(
            f'<div class="reveal"><div class="flex items-start gap-3"><span class="w-10 h-10 rounded-xl bg-sky-600 text-white flex items-center justify-center shrink-0 mt-0.5">'
            f'<svg class="w-5 h-5" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M12 3l8 4.5v9L12 21l-8-4.5v-9L12 3z"/></svg></span>'
            f'<div><h3 class="font-display font-extrabold text-slate-900">{h}</h3><p class="text-sm text-slate-600 leading-relaxed mt-1">{p}</p></div></div></div>')
    return (f'<section class="py-14 sm:py-16 bg-white border-y border-slate-200">'
            f'<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">'
            f'<div class="max-w-2xl mb-10 reveal"><span class="text-xs font-bold uppercase tracking-widest text-sky-600">What we do</span>'
            f'<h2 class="font-display text-2xl sm:text-3xl font-extrabold text-slate-900 mt-1">The jobs Johannesburg homes call us for</h2></div>'
            f'<div class="grid md:grid-cols-2 gap-x-10 gap-y-8">' + "".join(cards) + '</div></div></section>')


def work_section(works, eyebrow_name):
    figs = []
    for src640, srcfull, w, h, alt in works:
        figs.append(
            f'<figure class="gallery-item reveal"><img src="{src640}" srcset="{src640} 640w, {srcfull} {w}w" sizes="(min-width: 1024px) 30vw, (min-width: 640px) 45vw, 100vw" width="{w}" height="{h}" alt="{alt}" loading="lazy" decoding="async" class="w-full h-full object-cover" />'
            f'<span class="gallery-zoom-hint">'
            f'<svg class="w-4 h-4" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24" aria-hidden="true"><path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-4.35-4.35m1.85-5.4a7.25 7.25 0 11-14.5 0 7.25 7.25 0 0114.5 0zM10 8v4m0 0v4m0-4H6m4 0h4"/></svg></span>'
            f'<figcaption class="gallery-caption">{alt}</figcaption></figure>')
    return (f'<section id="work" class="py-14 sm:py-16 bg-slate-50 border-y border-slate-200">'
            f'<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">'
            f'<div class="flex flex-col md:flex-row md:items-end justify-between gap-4 mb-10 reveal">'
            f'<div class="max-w-2xl"><span class="text-xs font-bold uppercase tracking-widest text-sky-600">Real projects</span>'
            f'<h2 class="font-display text-2xl sm:text-3xl font-extrabold text-slate-900 mt-1">Recent {eyebrow_name} work in Johannesburg &amp; Midrand</h2>'
            f'<p class="text-slate-600 mt-2 text-sm sm:text-base">Photos from actual sites. Tap any image to view it full size.</p></div>'
            f'<a href="gallery.html" class="inline-flex items-center gap-2 text-sm font-bold text-sky-700 hover:text-sky-900">See the full gallery &rarr;</a></div>'
            f'<div class="grid sm:grid-cols-2 lg:grid-cols-3 gap-5">' + "".join(figs) + '</div></div></section>')


def areas_teaser(service_name):
    suburbs = "Klipfontein View, Midrand, Waterfall City, Halfway House, Vorna Valley, Noordwyk, Kyalami, Carlswald, Sandton, Fourways, Bryanston, Randburg, Centurion and greater Johannesburg"
    return (f'<section id="areas" class="py-14 max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">'
            f'<div class="bg-gradient-to-br from-sky-50 to-slate-100 rounded-3xl p-7 sm:p-11 border border-sky-100 reveal">'
            f'<div class="grid lg:grid-cols-12 gap-8 items-center">'
            f'<div class="lg:col-span-5"><span class="text-xs font-bold uppercase tracking-widest text-sky-700">Service coverage</span>'
            f'<h2 class="font-display text-2xl sm:text-3xl font-extrabold text-slate-900 mt-2">Where we handle {service_name.lower()}</h2>'
            f'<p class="text-slate-600 text-sm sm:text-base mt-3">Our team leaves from Klipfontein View, Midrand every morning and travels across {suburbs}.</p>'
            f'<a href="service-areas.html" class="inline-flex items-center gap-2 mt-5 text-sm font-bold text-sky-700 hover:text-sky-900">See all areas served &rarr;</a></div>'
            f'<div class="lg:col-span-7"><ul class="flex flex-wrap gap-2.5">' +
            "".join(f'<li class="px-3.5 py-2 rounded-xl bg-white border border-slate-200 text-xs sm:text-sm font-semibold text-slate-800 shadow-2xs">{s.strip()}</li>'
                    for s in suburbs.split(",")[:22]) +
            '</ul></div></div></div></section>')


# ---------------- Per-service copy ----------------
POINTS = {
    "blocked-drains-johannesburg": [
        ("Same-day clearing", "Most blockages cleared in one visit"),
        ("No guesswork", "We locate the blockage first"),
        ("Sewer & stormwater", "Homes, complexes and businesses"),
    ],
    "leak-detection-johannesburg": [
        ("Non-destructive first", "Minimal breaking and digging"),
        ("Hidden leaks found", "Walls, slabs, gardens and pools"),
        ("Quiet big bills", "Stop wasting water and money"),
    ],
    "geyser-repair-johannesburg": [
        ("Fast diagnosis", "Common faults fixed same day"),
        ("Real spares", "Elements, valves and thermostats"),
        ("Repair first, replace later", "Honest advice either way"),
    ],
    "geyser-replacement-johannesburg": [
        ("Safety always", "Drip tray, valves and vacuum breakers"),
        ("Same-day replacements", "When yours bursts"),
        ("Electric, gas or solar", "The right geyser for your home"),
    ],
    "solar-geyser-installation-gauteng": [
        ("Cut running costs", "Use the sun, not the grid"),
        ("Load-shedding friendly", "Hot water when Eskom drops"),
        ("Retrofits available", "Upgrade an old geyser"),
    ],
    "burst-pipe-repair-johannesburg": [
        ("Fast isolation", "Stop the water, stop the damage"),
        ("Proper repairs", "Not a quick patch and hope"),
        ("Clean up included", "We leave the site tidy"),
    ],
    "bathroom-renovations-johannesburg": [
        ("Full plumbing scope", "First-fix, drainage and second-fix"),
        ("Work with your team", "Plumbers, tilers and builders"),
        ("One accountable team", "From strip-out to testing"),
    ],
    "waterproofing-johannesburg": [
        ("Damp walls & basements", "Stop moisture at the source"),
        ("Roofs & balconies", "Waterproofing that lasts"),
        ("For renovations", "Wet-wall and shower trays"),
    ],
}

INTROS = {
    "blocked-drains-johannesburg": ("A slow drain never fixes itself. From a blocked kitchen sink to a full sewer backup, "
                                     "our team clears blockages in Johannesburg and Midrand fast — and finds out why it blocked so it does not happen again next week."),
    "leak-detection-johannesburg": ("A hidden leak can waste thousands of litres a month, lift your municipal bill and quietly "
                                     "undermine your foundations. We find the leak first — with acoustic and moisture testing — then repair the smallest area possible."),
    "geyser-repair-johannesburg": ("No hot water before work is no way to start the day. We diagnose and repair geysers across "
                                    "Johannesburg and Midrand, from elements and thermostats to pressure valves and leaking tanks — fast."),
    "geyser-replacement-johannesburg": ("When a geyser bursts, every hour counts. We replace electric, gas and solar geysers in "
                                         "Johannesburg and Midrand with drip trays, pressure control valves and vacuum breakers fitted the right way."),
    "solar-geyser-installation-gauteng": ("Rising electricity prices and load shedding make solar geysers a smart choice in Gauteng. "
                                           "We install complete solar systems and retrofit kits across Johannesburg, Midrand and surrounding areas."),
    "burst-pipe-repair-johannesburg": ("A burst pipe can flood a ceiling or erode your foundation in hours. We respond fast in "
                                        "Johannesburg and Midrand, isolate the line, repair or replace the pipe properly and confirm it holds."),
    "bathroom-renovations-johannesburg": ("A bathroom renovation lives or dies by its plumbing. We handle the full plumbing scope "
                                           "for Midrand and Johannesburg renovations — strip-out, first-fix, drainage and every fixture — so the final tiling sits on solid work."),
    "waterproofing-johannesburg": ("Damp walls, musty smells and peeling paint usually mean water is getting in where it should not. "
                                    "We find the entry point and waterproof the source — walls, basements, balconies and roofs across Johannesburg and Midrand."),
}

INTRO_PARAS = {
    "blocked-drains-johannesburg": [
        "Most plumbing problems get worse the longer they are left. A slow drain becomes a fully blocked line, and a blocked sewer becomes a health hazard in your garden or your home. Our team clears blockages properly — sinks, baths, toilets, gully traps, sewer lines and stormwater — rather than pushing the problem further down the pipe.",
        "We carry the tools to handle the stubborn blockages Johannesburg properties throw at us: roots in old clay lines, fat build-ups and collapsed pipe sections. Where the line is damaged, we tell you honestly and quote to repair the section, not just rod it blind.",
    ],
    "leak-detection-johannesburg": [
        "A hidden leak is easy to miss. The water meter keeps turning with everything switched off, a patch of wall stays damp, a tile feels warm, or paving starts to sink where a pipe runs underneath. Left alone, a slab leak can undermine a foundation and a garden leak can carry topsoil away.",
        "We start with non-destructive acoustic and moisture testing to pinpoint the leak, then open exactly the area needed. That means less breaking, less dust, less cost and a smaller repair.",
    ],
    "geyser-repair-johannesburg": [
        "Most geyser faults are repairable and a good deal cheaper than a new installation. No hot water, water that only gets lukewarm, a tripping isolator, a rumbling tank or a weeping relief valve all have specific causes — and most are diagnosed on the first visit.",
        "We work on electric, gas and solar geysers, and we carry common spares so many repairs are finished the same day. If the tank itself is leaking or the unit is simply at the end of its life, we will tell you straight and quote a replacement.",
    ],
    "geyser-replacement-johannesburg": [
        "A burst geyser dumps hundreds of litres into your ceiling, so the faster the replacement, the less collateral damage. We arrive with the fittings and safety components to do the job properly on the spot, and we test it before we leave.",
        "Every replacement includes a drip tray, pressure control valve, vacuum breaker and the correct pipework, installed to the standards Johannesburg homeowners expect. We replace electric, gas and solar geysers, and we match the right size to your household.",
    ],
    "solar-geyser-installation-gauteng": [
        "Gauteng gets some of the best solar radiation in the country, which makes a solar geyser a genuinely practical choice for hot water. A well-sized solar system covers most of your hot water needs during the day and can cut your geyser's electricity draw dramatically.",
        "We install complete systems — solar panels, tank and pipework — as well as retrofit kits that bolt onto your existing geyser. We size the system for the number of people in your home and make sure it is installed and commissioned correctly.",
    ],
    "burst-pipe-repair-johannesburg": [
        "A burst pipe is the most urgent call a plumber gets. Whether it is a geyser pipe in the ceiling, a supply line in the garden or a main line under the lawn, the first job is always the same: stop the water, then work out the cleanest repair.",
        "We repair or replace the damaged section with the right pipe and fittings, pressure test the line, and make good surface damage where we had to dig. You get one accountable team from the moment we arrive.",
    ],
    "bathroom-renovations-johannesburg": [
        "Plumbing is the backbone of any bathroom: if the first-fix is wrong, the tiling, fixtures and finish all suffer. We do the strip-out, the new pipe runs for the bath, shower, basin and toilet, the drainage, and the second-fix installation of every fixture.",
        "We work alongside your tiler and builder, or we coordinate the whole bathroom project for you. Because the same team plums and finishes, there is nobody to point fingers at if something is not right.",
    ],
    "waterproofing-johannesburg": [
        "Water that gets into a wall, a basement or a ceiling cavity keeps coming back until the entry point is sealed properly. Painting over a damp patch never lasts. We identify where the water is entering and apply the right waterproofing system for the surface.",
        "We waterproof wet walls in bathrooms, shower trays, balconies, basements, retaining walls and roof sections — the areas where Johannesburg homes leak most. Where the damage is already done, we talk you through the repair and the waterproofing together.",
    ],
}

INCLUDED = {
    "blocked-drains-johannesburg": [
        "Blockage located before we start",
        "Drains, toilets and sewer lines cleared",
        "High-pressure jetting on stubborn lines",
        "Root and fat build-up advice",
        "Honest report if your pipe needs repair",
        "Site cleaned and lids replaced",
    ],
    "leak-detection-johannesburg": [
        "Acoustic and moisture testing first",
        "Smallest possible breaking for access",
        "Leak repaired and line tested",
        "Wall, floor and paving made good",
        "Report on what caused the leak",
        "Advice to stop it happening again",
    ],
    "geyser-repair-johannesburg": [
        "Fault diagnosed before we quote",
        "Elements, thermostats and valves",
        "Relief valve and vacuum breaker checks",
        "Pressure tested after the repair",
        "Honest advice on repair vs replace",
    ],
    "geyser-replacement-johannesburg": [
        "Old geyser removed and disposed",
        "New geyser correctly sized for your home",
        "Drip tray, pressure valve and vacuum breaker",
        "Pipework connected and insulated",
        "System tested before we leave",
    ],
    "solar-geyser-installation-gauteng": [
        "Free site assessment and sizing",
        "Solar panels, tank and pipework on a roof",
        "Retrofit kits for existing geysers",
        "Commissioned and filled before handover",
        "Guidance on maintenance and freeze protection",
    ],
    "burst-pipe-repair-johannesburg": [
        "Water isolated and damage contained",
        "Damaged section cut out and replaced",
        "Line pressure tested after repair",
        "Trench and surface made good",
        "Advice on insurance claims if applicable",
    ],
    "bathroom-renovations-johannesburg": [
        "Strip-out of the old bathroom",
        "First-fix pipework in walls and floors",
        "Drainage for bath, shower, basin and toilet",
        "Second-fix fixtures and fittings",
        "Leak and pressure testing before finish",
    ],
    "waterproofing-johannesburg": [
        "Moisture source identified first",
        "Correct system for the surface type",
        "Wet walls, shower trays and balconies",
        "Roof and retaining wall waterproofing",
        "Surface made good after repairs",
    ],
}

STEPS = {
    "blocked-drains-johannesburg": [
        ("Tell us what is happening", "Sink, toilet, gully or sewer line — and since when."),
        ("Get a time slot", "Most blockages are cleared same day."),
        ("Locate the blockage", "CCTV or drain rodding to find the cause."),
        ("Clear and advise", "We clear the line and tell you how to stop it recurring."),
    ],
    "leak-detection-johannesburg": [
        ("Describe the symptom", "High bill, damp wall, warm floor or running meter."),
        ("Book the testing", "We find the leak before any breaking."),
        ("Pinpoint and repair", "We open the smallest area to fix it."),
        ("Test and make good", "Line tested, surface repaired, mess cleared."),
    ],
    "geyser-repair-johannesburg": [
        ("Tell us the symptom", "No hot water, lukewarm water or a leaking tank."),
        ("Book a visit", "Most repairs are same-day call-outs."),
        ("Diagnose", "We test the element, thermostat, valves and wiring."),
        ("Repair and test", "Fixed right the first time and pressure tested."),
    ],
    "geyser-replacement-johannesburg": [
        ("Call the moment it bursts", "Tell us the size and where the geyser is."),
        ("We bring the fittings", "Drip tray, valves, pipework and tools."),
        ("Remove and replace", "Old geyser out, new geyser correctly fitted."),
        ("Test and finish", "Refilled, tested and the ceiling tidied."),
    ],
    "solar-geyser-installation-gauteng": [
        ("Get a site assessment", "We size the system for your household."),
        ("Choose the system", "Complete install or a retrofit kit."),
        ("Install the system", "Panels, tank and pipework done properly."),
        ("Commission and hand over", "Filled, tested and explained to you."),
    ],
    "burst-pipe-repair-johannesburg": [
        ("Call us now", "The sooner the water is off, the less damage."),
        ("Isolate the line", "We close the right valve to stop the flow."),
        ("Repair the pipe", "Damage section cut out and replaced properly."),
        ("Test and restore", "Pressure tested and surfaces made good."),
    ],
    "bathroom-renovations-johannesburg": [
        ("Plan the layout", "We advise on plumbing runs and drainage."),
        ("Strip out", "Old bathroom removed down to the structure."),
        ("First-fix", "Pipework and drainage installed in walls/floors."),
        ("Second-fix & test", "Fixtures fitted, leak tested, job finished."),
    ],
    "waterproofing-johannesburg": [
        ("Find the moisture source", "We trace where the water is entering."),
        ("Prepare the surface", "Old coatings and loose material removed."),
        ("Apply the system", "The right waterproofing for the surface."),
        ("Test and advise", "Water-tested and maintenance explained."),
    ],
}

CORE = {
    "blocked-drains-johannesburg": [
        ("Blocked toilets", "A toilet that backs up is a health risk, not just an inconvenience. We clear the blockage and disinfect the area."),
        ("Blocked sinks & basins", "Fat, soap and food build up in kitchen and bathroom drains over time. We clear them and advise on prevention."),
        ("Sewer line blockages", "Roots, collapsed pipes and foreign objects block sewer lines. We locate the cause and clear or repair the line."),
        ("Stormwater drains", "Leaves, silt and debris block stormwater lines, flooding driveways and garages. We rod and jet them clear."),
    ],
    "leak-detection-johannesburg": [
        ("Slab leaks", "A pipe under your concrete floor can leak for months before it surfaces. We find it without tearing the whole floor up."),
        ("Wall leaks", "Damp patches and peeling paint on walls often mean a pipe inside the wall is weeping. We trace it precisely."),
        ("Garden leaks", "A soggy patch, sinking paving or lush grass over a pipe run usually means a supply line is leaking underground."),
        ("Pool & irrigation leaks", "We find leaks in pool plumbing and irrigation zones that quietly waste thousands of litres a month."),
    ],
    "geyser-repair-johannesburg": [
        ("No hot water", "Usually a dead element, a tripped thermostat or a faulty isolator. We test the circuit and fix it same day."),
        ("Lukewarm water", "A failing element, scaled up thermostat or a mixing valve issue. We find which and replace the part."),
        ("Leaking / dripping tank", "A weeping relief valve is a simple fix; a leaking tank means replacement. We tell you which and quote honestly."),
        ("Rumbling / popping", "Sediment in the tank. We flush the system and advise on sacrificial anodes."),
    ],
    "geyser-replacement-johannesburg": [
        ("Burst & severely leaking geysers", "The classic emergency. We remove the old unit, install a correctly sized replacement and test it."),
        ("Old, inefficient units", "A 15-year-old geyser costs more to keep. Replacing it with a modern insulated unit pays back in running costs."),
        ("Too-small or too-big units", "We size the replacement to your household's hot water demand so you are not waiting or wasting."),
        ("Relocations", "Moving a geyser out of the ceiling or to a more sensible spot as part of a renovation."),
    ],
    "solar-geyser-installation-gauteng": [
        ("Complete solar systems", "Solar panels, tank and pipework installed as a full system for your roof and household size."),
        ("Retrofit kits", "Adding a solar panel to your existing electric geyser to cut running costs without replacing it."),
        ("Geyser conversions", "Converting an electric geyser setup to solar as part of a home efficiency upgrade."),
        ("Maintenance & repairs", "Gutters, sensors, anti-freeze checks and repairs to keep your solar system producing."),
    ],
    "burst-pipe-repair-johannesburg": [
        ("Ceiling & roof-space bursts", "Geyser connection pipes fail often. We repair them before more water destroys your ceiling."),
        ("Underground supply bursts", "A burst line under the lawn or driveway. We excavate, repair and backfill properly."),
        ("Wall-embedded pipes", "Copper or plastic pipes running inside walls. We access, repair the section and restore the surface."),
        ("Gate valve & isolator failures", "Sometimes it is the valve that failed, not the pipe. We replace the fitting and repair the line."),
    ],
    "bathroom-renovations-johannesburg": [
        ("Full strip-out & refit", "We remove the old suite and install a complete new bathroom, handling every plumbing step."),
        ("First-fix plumbing", "New pipe runs for the shower, bath, basin and toilet, installed inside the structure."),
        ("Drainage", "Correct falls, traps and connections so the new fixtures drain reliably."),
        ("Second-fix fixtures", "Toilets, basins, mixers and showers installed and leak-tested ready for use."),
    ],
    "waterproofing-johannesburg": [
        ("Wet walls & shower trays", "We waterproof wet walls and shower trays as part of bathroom renovations."),
        ("Basement & retaining walls", "Damp basements and leaking retaining walls sealed from the outside-in."),
        ("Balconies & roofs", "Waterproofing systems for exposed balconies and roof sections that leak into rooms below."),
        ("Damp & mould repair", "Where water has already damaged plaster, we repair the surface after sealing the source."),
    ],
}

FAQS = {
    "blocked-drains-johannesburg": [
        ("Why does my drain keep blocking?", "Most recurring blockages have a cause: roots getting into an old clay line, a belly in the pipe where fat or sand settles, or a pipe that has collapsed. We locate the cause rather than only clearing the symptom."),
        ("How do you clear a blocked sewer line?", "We start by locating the blockage with a drain rod or CCTV camera, then clear it with the right tool — rods, blades or high-pressure jetting — and confirm the line flows."),
        ("Is a blocked toilet an emergency?", "Any sewage backup is urgent for hygiene reasons. Call 068 134 3276 so we can clear it before it spreads."),
        ("Can you clear a blocked stormwater drain in my driveway?", "Yes. Leaves, silt and debris often block stormwater lines. We rod and jet them clear and check the outfall."),
        ("How much does it cost to unblock a drain in Johannesburg?", "We quote per job after confirming what the blockage is — you get a written quote before we start. No flat call-out surprises."),
    ],
    "leak-detection-johannesburg": [
        ("How do I know I have a hidden leak?", "The classic signs: your water bill jumps, the meter keeps turning with everything off, a wall or floor stays damp, a tile feels warm, or paving sinks above a pipe run."),
        ("Do you find leaks without breaking walls and floors?", "Usually, yes. We start with acoustic and moisture testing to pinpoint the leak, then open only the smallest area needed for the repair."),
        ("Can you fix the leak after finding it?", "Yes. Finding and fixing is one job — we repair the pipe, test it and make good the surface."),
        ("Will a slab leak damage my foundation?", "Left long enough, yes. Water under a concrete slab can erode the ground beneath and cause settlement. Call us early."),
        ("Do you do moisture testing for insurance claims?", "We provide a clear report of what we found and fixed, which homeowners often use when claiming for water damage."),
    ],
    "geyser-repair-johannesburg": [
        ("Why is my geyser not heating water?", "Usually a dead element, a tripped thermostat or a faulty switch. We test the circuit and replace the failed part, often same day."),
        ("Why does my geyser only give lukewarm water?", "Common causes are a failing element, a scaled-up thermostat or a mixing valve set wrong. We diagnose and fix the actual cause."),
        ("My geyser is leaking — can it be repaired?", "If the tank itself is leaking, it cannot be patched safely. A dripping relief valve can be fixed; a leaking tank needs replacement. We tell you which."),
        ("How long should a geyser last?", "A well-maintained electric geyser typically lasts 8 to 12 years in South Africa. Beyond that, replacement is usually more reliable than repeated repairs."),
        ("Do you repair gas geysers too?", "Yes. We repair and service gas geysers, including thermocouple, burner and regulator issues."),
    ],
    "geyser-replacement-johannesburg": [
        ("How quickly can you replace a burst geyser?", "We treat burst geysers as priority call-outs in Johannesburg and Midrand. Phone 068 134 3276 and we will get to you as fast as we can, often the same day."),
        ("What is included in a geyser replacement?", "A correctly sized geyser, drip tray, pressure control valve, vacuum breaker, connection pipework and testing before we leave. We also remove the old unit."),
        ("Should I replace with electric, gas or solar?", "It depends on your budget, load-shedding risk and running costs. We talk you through the options honestly so you choose what suits your home."),
        ("Can you move my geyser during replacement?", "Yes. As part of a renovation we relocate geysers, including moving them out of the ceiling or into a safer spot."),
        ("Do you install the drip tray and safety valves?", "Always. A geyser without the correct safety components is a leak waiting to happen."),
    ],
    "solar-geyser-installation-gauteng": [
        ("How much can I save with a solar geyser in Gauteng?", "Gauteng has strong solar radiation, so a well-sized system covers most daytime hot water demand. Running savings depend on usage and your current system — we assess your home and show you the picture before you commit."),
        ("Do solar geysers work during load shedding?", "Yes. A good solar geyser produces hot water from the sun during the day, so you are far less dependent on the grid when Eskom drops."),
        ("Can I add a solar panel to my existing electric geyser?", "Yes. A retrofit kit adds a solar panel to your current geyser tank. It is a budget-friendly way to cut costs without replacing the whole system."),
        ("Do you install solar geysers on any roof type?", "We install on tile, IBR and flat roofs. The mounting, orientation and tank position are planned per property."),
        ("Are solar geysers reliable in Joburg winters?", "Yes, with correct sizing and freeze protection. Our systems are commissioned properly and we advise on maintenance so they keep producing through winter."),
    ],
    "burst-pipe-repair-johannesburg": [
        ("What should I do first when a pipe bursts?", "Turn off the water at the main stopcock or the geyser isolator, switch off the geyser power, and call 068 134 3276. We will talk you through isolating the line while we come to you."),
        ("How fast can you get to a burst pipe?", "Burst pipes are an emergency priority for our team in Johannesburg and Midrand — we aim to be there the same day."),
        ("Do you repair the damage or just the pipe?", "We repair the pipe as the priority, then make good the surface we had to break — whether that is plaster, tiling or a trench in the garden."),
        ("Will my insurance cover a burst pipe?", "Water damage from a sudden burst is often covered on South African home insurance. We provide a clear statement of what we did, which helps with claims."),
        ("Why do pipes burst in Johannesburg?", "The most common causes are age, poor quality previous repairs, pressure spikes, and movement in the ground or building. We fix the cause, not just the symptom."),
    ],
    "bathroom-renovations-johannesburg": [
        ("Do you do first-fix and second-fix plumbing?", "Yes. We handle the whole plumbing scope: strip-out, first-fix pipework in the walls and floors, drainage, and second-fix installation of toilets, basins, mixers and showers."),
        ("Can you work alongside my tiler and builder?", "Absolutely. We coordinate with your team so the plumbing and tiling sequence works, or we can arrange the full bathroom project."),
        ("How long does a bathroom renovation take?", "It depends on scope. We plan a realistic schedule with you before starting, so you know exactly what to expect."),
        ("Do you waterproof the shower before tiling?", "Yes. Wet-wall and shower-tray waterproofing is part of the job we do before tiling starts."),
        ("What type of bathroom is covered?", "Full renovations, guest bathrooms, en-suites, and complete new bathrooms in extensions — any size."),
    ],
    "waterproofing-johannesburg": [
        ("Why does my wall stay damp no matter what?", "Because the water is entering from somewhere that has not been sealed — a pipe leak, rising damp, a failed damp-proof course, or water pooling against the wall. We find the entry point first."),
        ("Can you stop a leaking basement from flooding?", "Yes. We waterproof basement and retaining walls from the correct side and install drainage where the water is coming from."),
        ("Do you waterproof roofs and balconies?", "Yes. We apply suitable roof and balcony waterproofing systems and test them so leaks into rooms below stop."),
        ("Is waterproofing needed before a bathroom renovation?", "For showers and wet walls, yes. It prevents damp problems inside the finished bathroom."),
        ("Will you fix damp damage too?", "After sealing the source, we repair the affected plaster or coating so the wall looks clean again."),
    ],
}


def build_all():
    written = 0
    for _slug_id, spec in SERVICES:
        write_file = f"{spec['slug']}.html"
        B.write(write_file, service_page(spec))
        written += 1
    print(f"\nservice_pages: {written} service pages written")


if __name__ == "__main__":
    build_all()