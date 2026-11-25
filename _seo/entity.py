#!/usr/bin/env python3
"""Enriches the Muneez Ahmed Person entity (schema.org) on every page, so search engines
and AI assistants can identify and describe him consistently. Idempotent.
Run from the repo root:  python3 _seo/entity.py
"""
import glob, json, re

PERSON = {
    "description": "Dubai-based AI and growth consultant helping businesses implement AI, automate operations, run on custom CRM and ERP software and grow with data-driven performance marketing.",
    "email": "hello@muneezahmed.com",
    "telephone": "+971586388362",
    "knowsAbout": ["Artificial intelligence consulting", "AI agents and chatbots", "WhatsApp AI automation", "Business process automation",
                   "Custom CRM development", "ERP systems", "Business dashboards", "Performance marketing", "Google Ads", "Meta advertising",
                   "Search engine optimization", "Digital marketing strategy"],
    "award": ["Digital Marketing Excellence – Dubai Business Awards (2024)", "Performance Marketing Award – Dubai Digital Awards (2024)",
              "Google Ads Partner Excellence – Google (2024)", "Meta Marketing Partner Award – Meta (2024)",
              "Performance Marketing Champion – India SME Awards (2023)", "Digital Innovation Award – UAE Marketing Awards (2024)",
              "Best ROI Performance – Middle East Marketing Summit (2024)", "Marketing Excellence Certificate – Google Marketing Platform (2024)"],
    "hasOccupation": {"@type": "Occupation", "name": "AI & Growth Consultant",
                      "occupationLocation": {"@type": "City", "name": "Dubai"}},
    "sameAs": ["https://www.linkedin.com/in/mrmnz/", "https://portfolio.muneezahmed.com/"],
}


def patch(m):
    try:
        d = json.loads(m.group(1))
    except ValueError:
        return m.group(0)
    nodes = d.get("@graph", [d]) if isinstance(d, dict) else []
    hit = False
    for n in nodes:
        if isinstance(n, dict) and n.get("@type") == "Person" and n.get("@id") == "https://www.muneezahmed.com/#person":
            for k, v in PERSON.items():
                if k == "sameAs":
                    n[k] = list(dict.fromkeys((n.get(k) or []) + v))
                else:
                    n[k] = v
            hit = True
    if not hit:
        return m.group(0)
    return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False, separators=(",", ":")) + "</script>"


n = 0
for f in glob.glob("**/*.html", recursive=True):
    if f.startswith(("admin/", "_seo/", "proposal/")):
        continue
    s = open(f, encoding="utf-8").read()
    t = re.sub(r'<script type="application/ld\+json">(.*?)</script>', patch, s, flags=re.S)
    if t != s:
        open(f, "w", encoding="utf-8").write(t)
        n += 1
print("Person entity enriched on", n, "pages")
