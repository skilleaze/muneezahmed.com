#!/usr/bin/env python3
"""Builds new Dubai pages from the site's own template (head, header, testimonials, CTA, footer
are copied from an existing Dubai page). Run from repo root: python3 _seo/new_pages.py
Then run dubai_priority.py (quick answer + author box) and entity.py (Person schema)."""
import html, json, re

BASE = "https://www.muneezahmed.com"
TEMPLATE = "dubai/ai-for-real-estate.html"
P = 'class="muted" style="line-height:1.75;font-size:1.05rem"'


def art(h3, *paras):
    return f'<article style="margin-top:2rem"><h3 class="h3">{h3}</h3>' + "".join(f"<p {P}>{p}</p>" for p in paras) + "</article>"


def table(head, rows):
    th = "".join(f"<th>{c}</th>" for c in head)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="tbl-wrap"><table class="tbl"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'


def cards(items):
    return '<div class="grid">' + "".join(f'<div class="card"><div class="ico"><i data-lucide="check" style="width:20px;height:20px"></i></div><h3 class="h3">{t}</h3><p class="muted">{d}</p></div>' for t, d in items) + "</div>"


def checklist(items):
    return '<ul class="list" style="margin-top:1rem">' + "".join(f'<li><i data-lucide="check" style="width:18px;height:18px"></i><span>{i}</span></li>' for i in items) + "</ul>"


PAGES = {
 "dubai/real-estate-marketing.html": dict(
  title="Real Estate Marketing in Dubai | Muneez Ahmed",
  desc="Real estate marketing in Dubai: off-plan launch campaigns, buyer leads from Google and Meta, WhatsApp follow-up and Trakheesi-compliant ads.",
  keywords="real estate marketing dubai, real estate marketer dubai, property marketing dubai, off plan marketing dubai, real estate lead generation dubai, real estate digital marketing uae",
  pill="Real Estate Marketing · Dubai",
  h1="Real Estate Marketing in Dubai",
  crumb="Real Estate Marketing in Dubai",
  lead="Buyer and investor leads for Dubai developers and brokerages, from off-plan launches to ready and secondary listings. Campaigns run on Google, Meta, Snapchat and TikTok, with every enquiry followed up on WhatsApp and tracked to commission.",
  service="Real Estate Marketing",
  problems=["Portal leads are shared with five other agencies before you call back.",
            "Off-plan launch budgets go on clicks that never become site visits.",
            "Agents chase cold leads while serious buyers wait hours for a WhatsApp reply."],
  body=(
   '<section class="sec"><div class="narrow"><h2 class="h2">How real estate marketing works in Dubai</h2>'
   + art("Off-plan launches vs ready and secondary listings",
         "Off-plan campaigns sell a project and a payment plan, usually to investors in the UAE and abroad, so they lean on Meta, Snapchat, TikTok and YouTube video with lead forms and a fast WhatsApp follow-up. "
         "Ready and secondary listings sell a specific home to people already searching, so Google Search and the property portals do most of the work, supported by remarketing.")
   + art("Which channels bring buyers", "A typical mix for a Dubai developer or brokerage:")
   + table(["Channel", "Best for", "Watch out for"], [
       ["Google Search", "Buyers searching by community, project or developer", "Generic keywords like \"property Dubai\" are expensive and broad"],
       ["Meta (Facebook &amp; Instagram)", "Off-plan launches, investors abroad, retargeting site visitors", "Instant forms bring volume; add qualifying questions to protect quality"],
       ["Snapchat and TikTok", "Younger UAE and Saudi buyers, launch awareness", "Needs native vertical video, not resized brochures"],
       ["Property portals", "Ready and secondary listings, rentals", "Leads are often sent to several agencies at once"],
       ["WhatsApp", "Where almost every buyer conversation ends up", "Slow replies lose leads to faster competitors"],
     ])
   + art("Lead quality beats lead volume",
         "Cheap leads are easy; buyers are not. Campaigns ask the questions that matter to an agent: budget, timeline, cash or mortgage, and whether the buyer is an investor or an end user. "
         "Scoring and routing happen automatically, so the best leads reach an agent on WhatsApp within minutes, and the rest go into a nurture sequence instead of being forgotten.")
   + art("Rules every Dubai property ad must follow",
         "Property ads in Dubai need a Trakheesi advertising permit from the Dubai Land Department before they go live, and off-plan projects may only be marketed once they are registered with the escrow account department. "
         "Brokers need a valid RERA licence, and individuals promoting property on their own social accounts need a UAE Advertiser Permit. Customer data used in retargeting falls under the UAE Personal Data Protection Law. "
         "Compliance is checked before launch, so campaigns are not paused halfway through a sales window.")
   + art("Result: Kaye &amp; Co Real Estate",
         'For <a href="/case-studies/kaye-co">Kaye &amp; Co Real Estate</a>, qualified lead generation for off-plan projects and secondary listings produced a 12x return on ad spend and $420K in commission revenue.')
   + "</div></section>"
   + '<section class="sec sec-alt"><div class="wrap"><h2 class="h2">What you get</h2><p class="lead" style="margin-bottom:2.5rem">Strategy, campaigns and follow-up run by one senior specialist.</p>'
   + cards([("Launch campaigns", "Off-plan launch plans across Meta, Snapchat, TikTok and YouTube."),
            ("Buyer search campaigns", "Google Search by community, developer and project, in English and Arabic."),
            ("Landing pages", "Fast project pages with floor plans, payment plans and a WhatsApp button."),
            ("Lead qualification", "Budget, timeline and finance questions, scored automatically."),
            ("WhatsApp and CRM", "Instant replies, agent routing and every lead logged in your CRM."),
            ("Reporting on commission", "Cost per qualified lead, viewings and deals, not just clicks.")])
   + "</div></section>"
   + '<section class="sec"><div class="narrow"><h2 class="h2">Related</h2><p ' + P + '>'
   + '<a href="/dubai/ai-for-real-estate">AI and CRM for real estate</a> &middot; <a href="/dubai/performance-marketing">performance marketing specialist in Dubai</a> &middot; '
   + '<a href="/dubai/google-ads">Google Ads</a> &middot; <a href="/dubai/facebook-ads">Facebook &amp; Instagram ads</a> &middot; <a href="/dubai/whatsapp-ai-chatbot">WhatsApp AI chatbot</a> &middot; <a href="/case-studies/kaye-co">Kaye &amp; Co case study</a></p></div></section>'),
  faqs=[
   ("How do you generate real estate leads in Dubai?", "With Google Search for buyers already looking, Meta, Snapchat and TikTok for off-plan launches and investors, and portals for listings, all followed up instantly on WhatsApp and tracked in a CRM."),
   ("Do Dubai property ads need a permit?", "Yes. Property ads in Dubai need a Trakheesi advertising permit from the Dubai Land Department, and off-plan projects can only be advertised once registered with escrow."),
   ("Can you market off-plan projects to overseas investors?", "Yes. Campaigns can target investors in markets such as India, the UK, Europe and the GCC, with creative and landing pages for each audience."),
   ("What results have you achieved for real estate?", "Kaye & Co Real Estate in Dubai achieved a 12x return on ad spend and $420K in commission revenue from off-plan and secondary leads."),
   ("Do you work with brokerages and developers?", "Both. Developers usually need launch campaigns; brokerages usually need a steady flow of qualified buyer and seller leads."),
  ],
  quick=("Real estate marketing in Dubai works best when Google Search captures active buyers, Meta, Snapchat and TikTok launch off-plan projects to investors, and every lead gets a WhatsApp reply within minutes. "
         "Muneez Ahmed runs these campaigns for Dubai developers and brokerages within Trakheesi and RERA rules; for Kaye &amp; Co Real Estate they returned 12x ad spend and $420K in commission."),
 ),
}


def build(path, c):
    t = open(TEMPLATE, encoding="utf-8").read()
    head, rest = t.split("<main>", 1)
    main_old, foot = rest.split("</main>", 1)
    url = BASE + "/" + path[:-5]
    # head
    old_title = re.search(r"<title>(.*?)</title>", head).group(1)
    old_desc = re.search(r'<meta name="description" content="(.*?)"', head).group(1)
    old_url = re.search(r'<link rel="canonical" href="(.*?)"', head).group(1)
    T, D = html.escape(c["title"], quote=False), html.escape(c["desc"], quote=True)
    head = head.replace(old_title, T).replace(old_desc, D).replace(old_url, url)
    head = re.sub(r'<meta name="keywords" content="[^"]*"', f'<meta name="keywords" content="{c["keywords"]}"', head)
    graph = [
        {"@type": "WebPage", "name": c["title"], "url": url, "description": c["desc"], "inLanguage": "en", "primaryImageOfPage": BASE + "/og-image.png",
         "dateModified": "2026-11-25", "about": {"@id": BASE + "/#person"}},
        {"@type": "ProfessionalService", "name": "Muneez Ahmed – " + c["h1"], "url": url, "description": c["desc"], "image": BASE + "/og-image.png", "priceRange": "$$",
         "serviceType": c["service"], "areaServed": ["Dubai", "United Arab Emirates"], "provider": {"@id": BASE + "/#person"}},
        {"@type": "Person", "@id": BASE + "/#person", "name": "Muneez Ahmed", "jobTitle": "AI & Growth Consultant", "url": BASE, "image": BASE + "/images/muneez-ahmed.png",
         "sameAs": ["https://www.linkedin.com/in/mrmnz/"], "address": {"@type": "PostalAddress", "addressLocality": "Dubai", "addressCountry": "AE"}},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in c["faqs"]]},
        {"@type": "BreadcrumbList", "itemListElement": [{"@type": "ListItem", "position": 1, "name": "Home", "item": BASE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Dubai", "item": BASE + "/dubai"}, {"@type": "ListItem", "position": 3, "name": c["crumb"], "item": url}]},
    ]
    head = re.sub(r'<script type="application/ld\+json">.*?</script>',
                  lambda m: '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, separators=(",", ":")) + "</script>", head, count=1, flags=re.S)
    # reuse hero aside, testimonials and CTA from the template
    aside = re.search(r'<aside class="card profile">.*?</aside>', main_old, re.S).group(0)
    testi = re.search(r'<section class="sec sec-alt"><div class="wrap"><div class="row" style="justify-content:space-between;margin-bottom:2rem"><h2 class="h2" style="margin:0">What clients say.*?</section>', main_old, re.S).group(0)
    cta = re.search(r'<section class="sec cta">.*?</section>', main_old, re.S).group(0)
    trust = re.search(r'<div class="trust">.*?</div></div>', main_old, re.S).group(0)
    hero = (f'<section class="hero"><div class="glow"></div><div class="wrap hero-grid">\n<div>\n'
            f'<nav class="crumbs" aria-label="Breadcrumb"><a href="/">Home</a><span>/</span><a href="/dubai">Dubai</a><span>/</span><span aria-current="page">{c["crumb"]}</span></nav>\n'
            f'<span class="pill">{c["pill"]}</span>\n<h1 class="h1" style="margin:1.25rem 0">{c["h1"]}</h1>\n<p class="lead">{c["lead"]}</p>\n'
            '<div class="row" style="margin-top:2rem"><a class="btn btn-p" href="/#contact"><i data-lucide="calendar" style="width:18px;height:18px"></i>Book a Strategy Call</a>'
            '<a class="btn btn-o" href="https://wa.me/971586388362" target="_blank" rel="noopener"><i data-lucide="message-circle" style="width:18px;height:18px"></i>WhatsApp</a></div>\n'
            f'{trust}\n</div>\n{aside}\n</div></section>')
    familiar = ('<section class="sec sec-alt"><div class="wrap"><h2 class="h2">Sound familiar?</h2><div class="grid" style="--min:260px">'
                + "".join(f'<div class="card row" style="align-items:flex-start;flex-wrap:nowrap"><span style="color:var(--primary);display:flex"><i data-lucide="alert-circle" style="width:20px;height:20px"></i></span><p>{p}</p></div>' for p in c["problems"])
                + "</div></div></section>")
    faq = ('<section class="sec"><div class="narrow"><h2 class="h2">Frequently asked questions</h2><div class="faqs">'
           + "".join(f'<details class="faq"{" open" if i == 0 else ""}><summary>{html.escape(q, quote=False)}<i data-lucide="plus" style="width:18px;height:18px"></i></summary><p>{html.escape(a, quote=False)}</p></details>' for i, (q, a) in enumerate(c["faqs"]))
           + "</div></div></section>")
    main = "\n".join([hero, familiar, c["body"], testi, faq, cta])
    open(path, "w", encoding="utf-8").write(head + "<main>\n" + main + "\n</main>" + foot)
    print("built", path)


if __name__ == "__main__":
    for p, c in PAGES.items():
        build(p, c)
