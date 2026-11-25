#!/usr/bin/env python3
"""Deep content for the priority Dubai digital-marketing pages.
Run from repo root: python3 _seo/dubai_priority.py  (idempotent, uses <!--dxb:...--> markers)
"""
import json, re

TODAY = "2026-11-25"
P = 'class="muted" style="line-height:1.75;font-size:1.05rem"'


def art(h3, *paras):
    return f'<article style="margin-top:2rem"><h3 class="h3">{h3}</h3>' + "".join(f"<p {P}{' style2' if i else ''}>{p}</p>".replace('1.05rem" style2','1.05rem;margin-top:1rem"') for i, p in enumerate(paras)) + "</article>"


def table(head, rows):
    th = "".join(f"<th>{c}</th>" for c in head)
    tr = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="tbl-wrap"><table class="tbl"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'


def checklist(items):
    return '<ul class="list" style="margin-top:1rem">' + "".join(
        f'<li><i data-lucide="check" style="width:18px;height:18px"></i><span>{i}</span></li>' for i in items) + "</ul>"


PAGES = {
 "dubai/digital-marketing.html": dict(
  title="Digital Marketing Services in Dubai (2026) | Muneez Ahmed",
  section=(
   '<section class="sec sec-alt"><div class="narrow"><h2 class="h2">Digital marketing in Dubai: a practical guide</h2>'
   f'<p class="lead">What actually works for UAE businesses in 2026, from channel choice to the rules that apply to your ads.</p>'
   + art("Which channels work in the UAE",
         "There is no single best channel. The right mix depends on how your customers buy. As a starting point:")
   + table(["Channel", "Best for in Dubai", "Watch out for"], [
       ["Google Search &amp; Performance Max", "High-intent demand: clinics, real estate, B2B services, home services, e-commerce", "Broad match wasting budget on irrelevant searches"],
       ["Instagram &amp; Facebook", "Consumer brands, hospitality, beauty, fashion, e-commerce", "Creative fatigue; refresh every few weeks"],
       ["Snapchat", "Reaching younger UAE and Saudi audiences", "Needs vertical video made for the platform"],
       ["TikTok", "Product discovery and impulse purchases", "Hard to measure without proper pixel and event setup"],
       ["LinkedIn", "B2B, free-zone companies, recruitment, professional services", "Higher cost per click; needs tight targeting"],
     ])
   + art("Arabic and English, planned separately",
         "Most Dubai residents are expatriates and English is the working language of business, but Arabic matters for Emirati customers and the wider GCC. Campaigns perform better with separate Arabic and English ad sets, landing pages and keywords rather than mixed or machine-translated creative. For some segments, Hindi, Urdu, Malayalam or Tagalog creative reaches communities that English ads miss.")
   + art("WhatsApp is where leads convert",
         "In the UAE, many customers would rather send a WhatsApp message than fill in a form. Click-to-WhatsApp ads, a fast reply time and an automatic link between WhatsApp and your CRM often raise conversion rates more than any change to the ads themselves. I set this up as part of the campaign, not as an extra.")
   + art("Plan around the Dubai calendar",
         "Demand in Dubai is seasonal. Ramadan shifts about eleven days earlier each year and changes when people browse and buy, with activity moving into the evening. Many residents travel in July and August, so some sectors slow down. The fourth quarter is the busiest stretch, with White Friday sales in November and the Dubai Shopping Festival from December into January. Budgets and creative should be planned around these dates, not spread evenly across the year.")
   + art("Advertising rules that apply in Dubai",
         "Three sets of rules catch businesses out. Since February 2026, anyone publishing promotional content on social media in the UAE, including creators you pay or gift products to, needs an Advertiser Permit, now issued by the National Media Authority, and brands are expected to check that the creators they work with hold one. Healthcare providers must follow Dubai Health Authority standards for medical advertising, which ban claims such as &ldquo;the best&rdquo;, &ldquo;100%&rdquo; or &ldquo;guaranteed results&rdquo;. Property ads in Dubai need a Trakheesi permit from the Dubai Land Department before they go live.",
         "Customer data used for remarketing and CRM campaigns falls under the UAE Personal Data Protection Law, so consent and data handling are set up properly from the first campaign.")
   + art("What digital marketing costs in Dubai",
         "There are always two parts: the media budget you pay directly to Google, Meta, Snapchat or TikTok in AED, and the fee for strategy and management. Rather than fixed packages, you get one proposal after a discovery call that covers both, based on your targets and margins.",
         "My advice: fund one or two channels properly before adding more. A channel without enough budget never collects enough data to optimise, and the money is wasted.")
   + art("How to choose a digital marketing partner in Dubai", "Ask these questions before you sign:")
   + checklist([
       "Will the ad accounts, pixels and analytics be in my company's name?",
       "Who actually manages my account day to day, and how senior are they?",
       "Do reports show leads, sales and cost per acquisition, or only clicks and impressions?",
       "How are WhatsApp and phone enquiries tracked back to campaigns?",
       "What happens if results are not on track after 90 days?",
     ])
   + '<p class="muted" style="margin-top:1.5rem">Related: <a href="/dubai/digital-marketing-consultant">digital marketing consultant in Dubai</a> &middot; <a href="/dubai/performance-marketing">performance marketing</a> &middot; <a href="/dubai/google-ads">Google Ads</a> &middot; <a href="/dubai/seo">SEO</a> &middot; <a href="/dubai/social-media-marketing">social media marketing</a> &middot; <a href="/case-studies">case studies</a></p>'
   + "</div></section>"),
  faqs=[
   ("Which digital marketing channel is best for a Dubai business?", "It depends on how your customers buy. Google Search captures people already looking for your service; Instagram, Snapchat and TikTok create demand; LinkedIn suits B2B. Most businesses do best starting with one or two channels and expanding once they are profitable."),
   ("Should my ads be in Arabic or English?", "Usually both, as separate campaigns. English reaches most of Dubai's population; Arabic matters for Emirati and wider GCC audiences. Mixed or machine-translated ads tend to underperform."),
   ("Do influencers I work with need a permit in the UAE?", "Yes. Since February 2026, anyone publishing promotional content on social media in the UAE needs an Advertiser Permit, and brands are expected to check that the creators they work with hold one."),
   ("When is the busiest season for marketing in Dubai?", "The fourth quarter, with White Friday in November and the Dubai Shopping Festival from December into January. Ramadan and the summer months change behaviour and need their own plans."),
  ]),
 "dubai/digital-marketing-consultant.html": dict(
  title="Digital Marketing Consultant in Dubai | Muneez Ahmed",
  section=(
   '<section class="sec sec-alt"><div class="narrow"><h2 class="h2">Hiring a digital marketing consultant in Dubai: what to expect</h2>'
   '<p class="lead">A senior consultant gives you strategy and oversight without the cost of a full-time marketing head or a large agency retainer.</p>'
   + art("Consultant, agency or in-house hire?", "Each option suits a different stage. A quick comparison:")
   + table(["", "Consultant", "Agency", "In-house hire"], [
       ["Seniority", "Senior expert on your account", "Often senior in the pitch, junior in delivery", "Depends on who you can hire"],
       ["Cost structure", "Project or monthly advisory fee", "Monthly retainer plus media", "Salary, visa and benefits"],
       ["Speed to start", "Days", "Weeks", "Months to recruit"],
       ["Best for", "Fixing performance, setting strategy, overseeing an agency", "High-volume production across many channels", "Long-term, full-time marketing workload"],
     ])
   + art("What the first 30 days look like",
         "Week one is access and tracking: Google Analytics 4, conversion events, ad accounts, CRM and WhatsApp. Week two is a channel and funnel audit to find where money is wasted. Weeks three and four turn that into a 90-day plan with quick wins first, so improvements show up in the first month rather than at the end of a long project.")
   + art("The audit checklist", "Every audit covers the basics that most often hold results back:")
   + checklist([
       "Tracking: are leads, calls and WhatsApp chats measured, and do the numbers match your CRM?",
       "Search terms: how much budget goes on searches that never convert?",
       "Creative: when was each ad last refreshed, and which messages actually sell?",
       "Landing pages: mobile speed, clarity of the offer and the number of steps to enquire",
       "Lead handling: how quickly the team replies and how many leads turn into customers",
       "Compliance: consent for data use, Advertiser Permits for creators and sector rules for health or property ads",
     ])
   + art("Signs your agency is not performing",
         "Reports that focus on clicks and impressions instead of leads and revenue, no admin access to your own ad accounts, the same creative running for months, and cost per lead rising without a clear explanation. A consultant can review the work independently and either fix the relationship or plan a clean handover.")
   + art("Track record",
         'I have scaled 50+ businesses with an average client return on ad spend of 6.2x, and received recognition including Google Ads Partner Excellence and the Meta Marketing Partner Award in 2024. See the <a href="/case-studies">case studies</a> and <a href="/awards">awards</a> for detail.')
   + '<p class="muted" style="margin-top:1.5rem">Related: <a href="/dubai/digital-marketing">digital marketing services in Dubai</a> &middot; <a href="/dubai/performance-marketing">performance marketing</a> &middot; <a href="/dubai/google-ads">Google Ads expert</a> &middot; <a href="/dubai/ai-marketing">AI marketing</a> &middot; <a href="/dubai/ai-consultant">AI consultant in Dubai</a></p>'
   + "</div></section>"),
  faqs=[
   ("How much does a digital marketing consultant cost in Dubai?", "It depends on scope. An audit and 90-day plan is usually a fixed-fee project, and ongoing work is a monthly advisory fee. You receive one clear proposal after a free discovery call."),
   ("Can a consultant work alongside our existing agency?", "Yes. A common setup is a consultant who sets strategy and reviews the agency's work each month, so you get senior oversight without replacing the team."),
   ("What should a digital marketing audit include?", "Tracking accuracy, wasted ad spend, creative performance, landing page conversion, lead handling speed and compliance with UAE advertising rules."),
   ("How soon will we see results?", "Quick wins from fixing tracking and wasted spend often show within the first month. Larger gains from new channels and creative usually build over 60 to 90 days."),
  ]),
}


def run():
    for path, cfg in PAGES.items():
        s = open(path, encoding="utf-8").read()
        s = re.sub(r"<!--dxb:start-->.*?<!--dxb:end-->", "", s, flags=re.S)
        s = re.sub(r"<!--dxbfaq:start-->.*?<!--dxbfaq:end-->", "", s, flags=re.S)
        old = re.search(r"<title>(.*?)</title>", s).group(1)
        new = cfg["title"].replace("&", "&amp;")
        if old != new:
            s = s.replace(old, new)
            s = s.replace(old.replace("&amp;", "&"), cfg["title"])
        m = re.search(r'(<section class="sec"><div class="narrow"><h2 class="h2">[^<]*what to know</h2>.*?</section>)', s, re.S)
        s = s[:m.end()] + "<!--dxb:start-->" + cfg["section"] + "<!--dxb:end-->" + s[m.end():]
        items = "".join(f'<details class="faq"><summary>{q}<i data-lucide="plus" style="width:18px;height:18px"></i></summary><p>{a}</p></details>' for q, a in cfg["faqs"])
        s = s.replace('<div class="faqs">', '<div class="faqs"><!--dxbfaq:start-->' + items + "<!--dxbfaq:end-->", 1)

        def patch(mm):
            d = json.loads(mm.group(1))
            g = d["@graph"] if "@graph" in d else [d]
            names = {q for q, _ in cfg["faqs"]}
            for n in g:
                if n.get("@type") == "FAQPage":
                    n["mainEntity"] = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}} for q, a in cfg["faqs"]] + [x for x in n["mainEntity"] if x["name"] not in names]
                if n.get("@type") == "WebPage":
                    n["dateModified"] = TODAY
            if not any(n.get("@type") == "FAQPage" for n in g):
                g.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in cfg["faqs"]]})
            return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False, separators=(",", ":")) + "</script>"
        s = re.sub(r'<script type="application/ld\+json">(.*?)</script>', patch, s, count=1, flags=re.S)
        open(path, "w", encoding="utf-8").write(s)
        print("updated", path)


if __name__ == "__main__":
    run()
