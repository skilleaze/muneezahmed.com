#!/usr/bin/env python3
"""Builds admin/pages.json: an SEO inventory of every page, shown on /admin -> SEO pages.
Run from the repo root after changing pages:  python3 _seo/build_pages.py
"""
import glob, html, json, re

BASE = "https://www.muneezahmed.com/"
locs = set()
for sm in glob.glob("sitemap*.xml"):
    locs |= set(re.findall(r"<loc>([^<]+)</loc>", open(sm, encoding="utf-8").read()))


def kind(p):
    if p.startswith("/dubai/") or p == "/dubai":
        return "Dubai"
    if p.startswith("/case-studies"):
        return "Case study"
    if p.startswith("/blog"):
        return "Blog"
    if p.startswith("/services"):
        return "Service"
    if p.startswith("/proposal") or p == "/404":
        return "Private"
    n = p.strip("/").count("/")
    if n == 0 and "-" not in p.strip("/") and p != "/" or p in ("/", "/services", "/industries", "/awards", "/case-studies", "/privacy-policy", "/terms", "/other-pages"):
        return "Core"
    return "City page" if n == 1 else "City service" if n == 2 else "Core"


rows = []
for f in sorted(glob.glob("**/*.html", recursive=True)):
    if f.startswith(("admin/", "_seo/")):
        continue
    s = open(f, encoding="utf-8", errors="ignore").read()
    path = "/" if f == "index.html" else "/" + f[:-5]
    t = re.search(r"<title>(.*?)</title>", s, re.S)
    title = html.unescape(t.group(1).strip()) if t else ""
    d = re.search(r'<meta\s+name="description"\s+content="(.*?)"', s, re.S)
    desc = html.unescape(d.group(1)) if d else ""
    body = re.sub(r"<(script|style|nav|footer|header)[^>]*>.*?</\1>", " ", s, flags=re.S)
    words = len(re.sub(r"<[^>]+>", " ", body).split())
    h1 = len(re.findall(r"<h1[\s>]", s))
    noindex = bool(re.search(r'noindex', s[:6000])) or path.startswith('/proposal')
    canon = 'rel="canonical"' in s
    schema = "application/ld+json" in s
    faq = '"FAQPage"' in s
    insm = (BASE + path.lstrip("/")) in locs or (path == "/" and BASE in locs)
    iss = []
    if noindex: pass
    elif not title: iss.append("No title")
    elif len(title) > 62: iss.append("Title too long")
    if noindex: iss = []
    if noindex: pass
    elif not desc: iss.append("No description")
    elif not 70 <= len(desc) <= 165: iss.append("Description length")
    if noindex: rows.append({"p": path, "k": "Private", "t": title, "tl": len(title), "dl": len(desc), "w": words, "h1": h1, "ix": 0, "sm": 0, "sc": 1 if schema else 0, "fq": 0, "i": []}); continue
    if h1 == 0 and "{{" not in s: iss.append("No H1")
    if h1 > 1: iss.append("Several H1s")
    if not canon: iss.append("No canonical")
    if not schema: iss.append("No schema")
    if words < 300 and "{{" not in s: iss.append("Thin content")
    if not noindex and not insm: iss.append("Not in sitemap")
    rows.append({"p": path, "k": kind(path), "t": title, "tl": len(title), "dl": len(desc), "w": words, "h1": h1,
                 "ix": 0 if noindex else 1, "sm": 1 if insm else 0, "sc": 1 if schema else 0, "fq": 1 if faq else 0, "i": iss})

json.dump({"built": __import__("datetime").date.today().isoformat(), "pages": rows}, open("admin/pages.json", "w", encoding="utf-8"),
          ensure_ascii=False, separators=(",", ":"))
print(len(rows), "pages;", sum(1 for r in rows if r["i"]), "with issues")
