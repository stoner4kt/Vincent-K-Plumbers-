"""Content definitions for the Vincent K Plumbers site pages.

All business facts come from the repository (phone / WhatsApp number, address,
areas served) or are marked as [VERIFY] / [PHONE_NUMBER] placeholders. No fake
reviews, ratings, certifications, licence numbers, prices or "24/7" claims.
"""
import site_lib as L

# --------------------------------------------------------------------------
# Shared contact facts
PHONE = "068 134 3276"
PHONE_INTL = "+27681343276"
ADDRESS = "505 Nancy Ndamase Street, Klipfontein View, Midrand, Johannesburg"


def whatsapp_link(message):
    from urllib.parse import quote
    return f"https://wa.me/{L.WHATSAPP}?text={quote(message)}"


# --------------------------------------------------------------------------
# NEW service pages (one per core service keyword). Existing pages for leak
# detection and geyser replacement already target their keywords and are kept.
SERVICES = [
    ("blocked-drains", {
        "title": "Blocked Drain Clearing Johannesburg | Vincent K Plumbers",
        "h1": "Blocked Drain Clearing in Johannesburg",
        "desc": "Slow drains, sewer backups and blocked toilets cleared fast in Johannesburg and Midrand. Call 068 134 3276 for a same-day drain unblock.",
        "eyebrow": "Blocked Drains & Sewer Lines",
        "kicker": "Same-Day Drain Clearing &middot; Klipfontein View, Midrand &amp; Johannesburg",
        "slug": "blocked-drains-johannesburg",
    }),
    ("geyser-repair", {
        "title": "Geyser Repair Johannesburg | Vincent K Plumbers",
        "h1": "Geyser Repair in Johannesburg",
        "desc": "No hot water? Burst or leaking geyser? Geyser repair and replacement in Johannesburg and Midrand. Same-day call-outs on 068 134 3276.",
        "eyebrow": "Geyser Repair & Replacement",
        "kicker": "Electric &amp; Gas Geyser Repairs &middot; Midrand &amp; Johannesburg",
        "slug": "geyser-repair-johannesburg",
    }),
    ("solar-geyser", {
        "title": "Solar Geyser Installation Gauteng | Vincent K Plumbers",
        "h1": "Solar Geyser Installation in Gauteng",
        "desc": "Solar geyser installation and retrofits in Johannesburg, Midrand and Gauteng that cut load-shedding risk and save electricity. Call 068 134 3276.",
        "eyebrow": "Solar Geyser Installation",
        "kicker": "Solar Geysers &amp; Retrofits &middot; Johannesburg, Midrand &amp; Gauteng",
        "slug": "solar-geyser-installation-gauteng",
    }),
    ("burst-pipe", {
        "title": "Burst Pipe Repair Johannesburg | Vincent K Plumbers",
        "h1": "Burst Pipe Repair in Johannesburg",
        "desc": "Burst pipe? We isolate, repair and replace broken water pipes in Johannesburg and Midrand fast. Call 068 134 3276 now to stop the damage.",
        "eyebrow": "Burst Pipe Repair",
        "kicker": "Emergency Pipe Repairs &middot; Johannesburg &amp; Midrand",
        "slug": "burst-pipe-repair-johannesburg",
    }),
    ("bathroom-renovation", {
        "title": "Bathroom Renovation Plumber in Johannesburg",
        "h1": "Bathroom Renovation Plumber in Johannesburg",
        "desc": "Bathroom renovation plumbing in Johannesburg and Midrand: strip-outs, first-fix, drainage and all fixtures. Call 068 134 3276 for a quote.",
        "eyebrow": "Bathroom Renovations",
        "kicker": "Bathroom Strip-Out &amp; Plumbing &middot; Midrand &amp; Johannesburg",
        "slug": "bathroom-renovations-johannesburg",
    }),
    ("waterproofing", {
        "title": "Waterproofing Johannesburg | Vincent K Plumbers",
        "h1": "Waterproofing in Johannesburg",
        "desc": "Waterproofing for damp walls, basements, balconies and roofs in Johannesburg and Midrand. Stop leaks before they spread. Call 068 134 3276.",
        "eyebrow": "Waterproofing & Damp Repair",
        "kicker": "Waterproofing &amp; Damp Proofing &middot; Johannesburg &amp; Midrand",
        "slug": "waterproofing-johannesburg",
    }),
]

# canonical slugs map
SERVICE_SLUGS = {s["slug"] for _, s in SERVICES}


# Related-service pairs to cross-link each page to others
RELATED = {
    "blocked-drains-johannesburg": [
        ("Leak Detection", "leak-detection-johannesburg.html", "Find hidden leaks before they damage your foundation."),
        ("Burst Pipe Repair", "burst-pipe-repair-johannesburg.html", "Urgent water pipe repairs across Johannesburg."),
        ("General Plumbing & Repairs", "plumbing-johannesburg.html", "Everyday plumbing repairs and installations."),
    ],
    "leak-detection-johannesburg": [
        ("Burst Pipe Repair", "burst-pipe-repair-johannesburg.html", "When a leak becomes a burst, we repair fast."),
        ("Blocked Drains", "blocked-drains-johannesburg.html", "Slow drains and sewer line blockages."),
        ("Waterproofing", "waterproofing-johannesburg.html", "Stop damp and water ingress for good."),
    ],
    "geyser-repair-johannesburg": [
        ("Geyser Replacement", "geyser-replacement-johannesburg.html", "When repair is not enough, we replace."),
        ("Gas Geyser Installation", "gas-geyser-installation-johannesburg.html", "Load-shedding-proof gas geysers."),
        ("Solar Geyser Installation", "solar-geyser-installation-gauteng.html", "Cut your geyser running costs."),
    ],
    "geyser-replacement-johannesburg": [
        ("Geyser Repair", "geyser-repair-johannesburg.html", "Fixable geyser problems handled first."),
        ("Gas Geyser Installation", "gas-geyser-installation-johannesburg.html", "Switch to gas for load shedding."),
        ("Solar Geyser Installation", "solar-geyser-installation-gauteng.html", "Energy-efficient solar geysers."),
    ],
    "solar-geyser-installation-gauteng": [
        ("Geyser Replacement", "geyser-replacement-johannesburg.html", "Replace an old electric geyser."),
        ("Gas Geyser Installation", "gas-geyser-installation-johannesburg.html", "Compare solar vs gas geysers."),
        ("Geyser Repair", "geyser-repair-johannesburg.html", "Repair before replacing."),
    ],
    "burst-pipe-repair-johannesburg": [
        ("Leak Detection", "leak-detection-johannesburg.html", "Find where the water is coming from."),
        ("Blocked Drains", "blocked-drains-johannesburg.html", "Sort slow drains before they back up."),
        ("General Plumbing & Repairs", "plumbing-johannesburg.html", "Repairs, maintenance and installations."),
    ],
    "bathroom-renovations-johannesburg": [
        ("General Plumbing & Repairs", "plumbing-johannesburg.html", "First-fix and second-fix plumbing done right."),
        ("Waterproofing", "waterproofing-johannesburg.html", "Wet-wall and bathroom waterproofing."),
        ("Geyser Replacement", "geyser-replacement-johannesburg.html", "A new geyser to match your renovation."),
    ],
    "waterproofing-johannesburg": [
        ("Bathroom Renovations", "bathroom-renovations-johannesburg.html", "Waterproofing is part of any bathroom job."),
        ("Leak Detection", "leak-detection-johannesburg.html", "Trace the source of dampness."),
        ("Blocked Drains", "blocked-drains-johannesburg.html", "Clear stormwater lines before they overflow."),
    ],
}

# Image hero per service (src, width, height, alt)
HERO_IMAGES = {
    "blocked-drains-johannesburg": ("images/plumbing/plumbing-repair-johannesburg-05-640.jpg",
                                    "images/plumbing/plumbing-repair-johannesburg-05.jpg",
                                    "images/plumbing/plumbing-repair-johannesburg-05.jpg 900w",
                                    900, 1200,
                                    "Repair trench prepared for pipe replacement beside a boundary wall in Johannesburg"),
    "leak-detection-johannesburg": ("images/plumbing/plumbing-repair-johannesburg-04-640.jpg",
                                    "images/plumbing/plumbing-repair-johannesburg-04.jpg",
                                    "images/plumbing/plumbing-repair-johannesburg-04.jpg 900w",
                                    900, 1200,
                                    "Plumber working in a trench to replace a damaged water line"),
    "geyser-repair-johannesburg": ("images/geysers/geyser-replacement-johannesburg-01-640.jpg",
                                   "images/geysers/geyser-replacement-johannesburg-01.jpg",
                                   "images/geysers/geyser-replacement-johannesburg-01.jpg 900w",
                                   900, 1200,
                                   "New electric geyser installed with insulation blanket, drip tray and safety valves"),
    "geyser-replacement-johannesburg": ("images/geysers/geyser-replacement-johannesburg-01-640.jpg",
                                        "images/geysers/geyser-replacement-johannesburg-01.jpg",
                                        "images/geysers/geyser-replacement-johannesburg-01.jpg 900w",
                                        900, 1200,
                                        "New electric geyser installed with insulation blanket, drip tray and safety valves"),
    "solar-geyser-installation-gauteng": ("images/gas-geyser-installation/gas-geyser-installation-johannesburg-01-640.jpg",
                                          "images/gas-geyser-installation/gas-geyser-installation-johannesburg-01.jpg",
                                          "images/gas-geyser-installation/gas-geyser-installation-johannesburg-01.jpg 900w",
                                          900, 1200,
                                          "Technician beside a completed gas geyser installation in Klipfontein View, Midrand"),
    "burst-pipe-repair-johannesburg": ("images/plumbing/plumbing-repair-johannesburg-02-640.jpg",
                                       "images/plumbing/plumbing-repair-johannesburg-02.jpg",
                                       "images/plumbing/plumbing-repair-johannesburg-02.jpg 900w",
                                       900, 1200,
                                       "Stormwater, pool and drainage pipe installation in progress in Johannesburg"),
    "bathroom-renovations-johannesburg": ("images/bathrooms/bathroom-renovation-johannesburg-01-640.jpg",
                                          "images/bathrooms/bathroom-renovation-johannesburg-01.jpg",
                                          "images/bathrooms/bathroom-renovation-johannesburg-01.jpg 850w",
                                          850, 560,
                                          "Modern bathroom renovation with freestanding bath, glass shower and double vanity in Midrand"),
    "waterproofing-johannesburg": ("images/plumbing/plumbing-repair-johannesburg-03-640.jpg",
                                   "images/plumbing/plumbing-repair-johannesburg-03.jpg",
                                   "images/plumbing/plumbing-repair-johannesburg-03.jpg 900w",
                                   900, 1200,
                                   "Trench dug and prepared for new water and drainage lines"),
}

# Work gallery images used per service page
WORK_IMAGES = {
    "blocked-drains-johannesburg": [
        ("images/plumbing/plumbing-repair-johannesburg-05-640.jpg",
         "images/plumbing/plumbing-repair-johannesburg-05.jpg", 900, 1200,
         "Repair trench prepared for pipe replacement beside a boundary wall"),
        ("images/plumbing/plumbing-repair-johannesburg-06-640.jpg",
         "images/plumbing/plumbing-repair-johannesburg-06.jpg", 900, 1200,
         "Pool plumbing and drainage completed alongside new paving"),
        ("images/plumbing/plumbing-repair-johannesburg-03-640.jpg",
         "images/plumbing/plumbing-repair-johannesburg-03.jpg", 900, 1200,
         "Trench dug and prepared for new water and drainage lines"),
    ],
    "leak-detection-johannesburg": [
        ("images/plumbing/plumbing-repair-johannesburg-04-640.jpg",
         "images/plumbing/plumbing-repair-johannesburg-04.jpg", 900, 1200,
         "Plumber working in a trench to replace a damaged water line"),
        ("images/plumbing/plumbing-repair-johannesburg-05-640.jpg",
         "images/plumbing/plumbing-repair-johannesburg-05.jpg", 900, 1200,
         "Repair trench prepared for pipe replacement beside a boundary wall"),
        ("images/plumbing/plumbing-repair-johannesburg-03-640.jpg",
         "images/plumbing/plumbing-repair-johannesburg-03.jpg", 900, 1200,
         "Trench dug and prepared for new water and drainage lines"),
    ],
    "geyser-repair-johannesburg": [
        ("images/geysers/geyser-replacement-johannesburg-01-640.jpg",
         "images/geysers/geyser-replacement-johannesburg-01.jpg", 900, 1200,
         "New electric geyser installed in the roof with insulation blanket, drip tray and safety valves"),
        ("images/gas-geyser-installation/gas-geyser-installation-johannesburg-02-640.jpg",
         "images/gas-geyser-installation/gas-geyser-installation-johannesburg-02.jpg", 900, 1200,
         "Coiled geyser pipework being fitted during a gas installation"),
        ("images/gas-geyser-installation/gas-geyser-installation-johannesburg-09-640.jpg",
         "images/gas-geyser-installation/gas-geyser-installation-johannesburg-09.jpg", 900, 1200,
         "Neat gas and water pipe routing along an exterior wall"),
    ],
    "geyser-replacement-johannesburg": [
        ("images/geysers/geyser-replacement-johannesburg-01-640.jpg",
         "images/geysers/geyser-replacement-johannesburg-01.jpg", 900, 1200,
         "New electric geyser installed in the roof with insulation blanket, drip tray and safety valves"),
        ("images/gas-geyser-installation/gas-geyser-installation-johannesburg-03-640.jpg",
         "images/gas-geyser-installation/gas-geyser-installation-johannesburg-03.jpg", 900, 1200,
         "Hospital of gas and water pipework for a new geyser"),
        ("images/gas-geyser-installation/gas-geyser-installation-johannesburg-06-640.jpg",
         "images/gas-geyser-installation/gas-geyser-installation-johannesburg-06.jpg", 900, 1200,
         "Gas geyser fitted with flue, overflow pipe and drainage outside"),
    ],
    "solar-geyser-installation-gauteng": [
        ("images/gas-geyser-installation/gas-geyser-installation-johannesburg-01-640.jpg",
         "images/gas-geyser-installation/gas-geyser-installation-johannesburg-01.jpg", 900, 1200,
         "Technician beside a completed gas geyser installation in Klipfontein View, Midrand"),
        ("images/gas-geyser-installation/gas-geyser-installation-johannesburg-04-640.jpg",
         "images/gas-geyser-installation/gas-geyser-installation-johannesburg-04.jpg", 900, 1200,
         "Gas team installing a geyser with new copper pipework at a Johannesburg home"),
        ("images/gas-geyser-installation/gas-geyser-installation-johannesburg-17-640.jpg",
         "images/gas-geyser-installation/gas-geyser-installation-johannesburg-17.jpg", 1200, 900,
         "Solar geyser system installed on a tiled roof in Midrand"),
    ],
    "burst-pipe-repair-johannesburg": [
        ("images/plumbing/plumbing-repair-johannesburg-02-640.jpg",
         "images/plumbing/plumbing-repair-johannesburg-02.jpg", 900, 1200,
         "Stormwater, pool and drainage pipe installation in progress"),
        ("images/plumbing/plumbing-repair-johannesburg-04-640.jpg",
         "images/plumbing/plumbing-repair-johannesburg-04.jpg", 900, 1200,
         "Plumber working in a trench to replace a damaged water line"),
        ("images/plumbing/plumbing-repair-johannesburg-03-640.jpg",
         "images/plumbing/plumbing-repair-johannesburg-03.jpg", 900, 1200,
         "Trench dug and prepared for new water and drainage lines"),
    ],
    "bathroom-renovations-johannesburg": [
        ("images/bathrooms/bathroom-renovation-johannesburg-01-640.jpg",
         "images/bathrooms/bathroom-renovation-johannesburg-01.jpg", 850, 560,
         "Modern bathroom renovation with freestanding bath, glass shower and double vanity in Midrand"),
        ("images/bathrooms/bathroom-renovation-johannesburg-05-640.jpg",
         "images/bathrooms/bathroom-renovation-johannesburg-05.jpg", 900, 1200,
         "Team fitting a tiled shower after plumbing installation"),
        ("images/bathrooms/bathroom-renovation-johannesburg-06-640.jpg",
         "images/bathrooms/bathroom-renovation-johannesburg-06.jpg", 900, 1200,
         "Plumber mounting a vanity basin and mixer tap"),
    ],
    "waterproofing-johannesburg": [
        ("images/plumbing/plumbing-repair-johannesburg-03-640.jpg",
         "images/plumbing/plumbing-repair-johannesburg-03.jpg", 900, 1200,
         "Trench dug and prepared for new water and drainage lines"),
        ("images/plumbing/plumbing-repair-johannesburg-08-640.jpg",
         "images/plumbing/plumbing-repair-johannesburg-08.jpg", 900, 1200,
         "Newly plumbed bathroom with tiled shower, basin and toilet"),
        ("images/bathrooms/bathroom-renovation-johannesburg-07-640.jpg",
         "images/bathrooms/bathroom-renovation-johannesburg-07.jpg", 900, 1200,
         "Drilling and fitting a shower mixer in a tiled bathroom"),
    ],
}

# Guide index
GUIDES = [
    ("signs-your-geyser-is-about-to-burst", "Signs your geyser is about to burst", "Geysers"),
    ("how-to-find-a-hidden-leak", "How to find a hidden water leak", "Leak detection"),
    ("blocked-main-drain-causes-and-what-to-do", "Blocked main drain: causes and what to do", "Drains"),
    ("solar-vs-electric-vs-gas-geysers", "Solar vs electric vs gas geysers", "Geysers"),
    ("what-to-do-in-a-plumbing-emergency", "What to do in a plumbing emergency", "Emergency"),
]