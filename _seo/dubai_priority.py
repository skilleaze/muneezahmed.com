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



def cs(slug, name, result):
    return f'<a href="/case-studies/{slug}">{name}</a>: {result}'


PAGES["dubai/digital-marketing.html"]["quick"] = ("Digital marketing in Dubai works best as one plan across Google Search, Instagram, Snapchat, TikTok and LinkedIn, run in Arabic and English, "
    "converting on WhatsApp and timed around Ramadan and the fourth quarter. Muneez Ahmed runs it senior-led for UAE businesses, with an average 6.2x return on ad spend across 50+ clients.")
PAGES["dubai/digital-marketing-consultant.html"]["quick"] = ("A digital marketing consultant in Dubai audits your channels, fixes tracking and wasted ad spend, and sets a 90-day growth plan, then oversees "
    "execution by your team or agency. Muneez Ahmed works this way with UAE founders and marketing teams, usually finding quick wins within the first month.")

PAGES["dubai/ai-consultant.html"] = dict(
  title="Best AI Consultant in Dubai & AI Consulting UAE | Muneez Ahmed",
  quick=("Muneez Ahmed is an AI consultant in Dubai who helps UAE businesses find where AI pays off and then builds it: WhatsApp AI agents, workflow automation, "
         "custom CRM and ERP, and AI forecasting. AI consulting engagements start with a two-week audit, ship the first working system within four to ten weeks "
         "and are designed to comply with the UAE Personal Data Protection Law."),
  faqs=[
   ("What does AI consulting in the UAE include?", "An audit of where time and money are lost, a ranked list of AI use cases with expected payback, a 90-day roadmap, and hands-on implementation of the first systems, such as WhatsApp agents, automations or a custom CRM, plus training so your team uses them."),
   ("How is an AI consultant different from an AI agency?", "An agency usually sells a team and a platform. An independent AI consultant stays vendor-neutral, picks the tools that fit your processes and data, and is personally accountable for the result."),
  ])

PAGES["dubai/digital-marketing-specialist.html"] = dict(
  title="Best Digital Marketing Specialist in Dubai | Muneez Ahmed",
  h1="Best Digital Marketing Specialist in Dubai",
  quick=("Muneez Ahmed is a Dubai-based digital marketing specialist who plans and runs Google Ads, Meta, Snapchat, TikTok and LinkedIn campaigns, SEO and conversion tracking "
         "for UAE businesses. Clients average a 6.2x return on ad spend across 50+ businesses, including 12x for Kaye &amp; Co Real Estate and 10x for Dubai Smile Dental."),
  section=(
   '<section class="sec sec-alt"><div class="narrow"><h2 class="h2">What a digital marketing specialist in Dubai does</h2>'
   '<p class="lead">Hands-on execution across the channels that bring UAE customers, measured on leads and sales rather than clicks.</p>'
   + art("Specialist, consultant or agency?",
         "A digital marketing specialist builds and runs the campaigns: ad accounts, keywords, audiences, creative tests, landing pages and tracking. "
         'A <a href="/dubai/digital-marketing-consultant">digital marketing consultant</a> sets strategy and oversees others. An agency adds a team for volume. '
         "If your problem is that campaigns are not performing, you need a specialist who works inside the accounts every week.")
   + art("Skills to look for in Dubai", "The UAE market rewards a specific mix of skills:")
   + table(["Skill", "Why it matters in Dubai"], [
       ["Google Ads Search &amp; Performance Max", "Captures high-intent searches for clinics, property, B2B and home services"],
       ["Meta, Snapchat and TikTok ads", "Snapchat and TikTok reach younger UAE and Saudi audiences that Meta alone misses"],
       ["Arabic and English campaigns", "Separate ad sets and landing pages for each language outperform mixed creative"],
       ["GA4, server-side tracking and Consent Mode", "Accurate data after iOS privacy changes and consent rules"],
       ["WhatsApp and CRM integration", "Most UAE enquiries arrive on WhatsApp and must be tracked back to the ad"],
       ["SEO and Google Business Profile", "Long-term traffic that does not stop when the ad budget does"],
     ])
   + art("Results from UAE and GCC clients", "Verified results from recent work:")
   + checklist([
       cs("kaye-co", "Kaye &amp; Co Real Estate", "12x ROAS and $420K in commission revenue from off-plan and secondary leads"),
       cs("lana-life-care", "Lana Life Care", "12x ROAS and $180K revenue for a Dubai home healthcare provider"),
       cs("dubai-smile-dental", "Dubai Smile Dental", "10x ROAS and 300% more patient appointments"),
       cs("al-barsha-fitness", "Al Barsha Fitness", "8x ROAS and 400+ new memberships"),
       cs("yallatoys", "Yallatoys, Qatar", "8x ROAS for a leading toy retailer"),
     ])
   + art("What a digital marketing specialist costs in Dubai",
         "You pay two things: the ad budget, which goes directly to Google, Meta, Snapchat or TikTok in AED, and a fee for managing the campaigns. "
         "Fees depend on the number of channels and campaigns. You get one proposal after a free call, with scope, timeline and total agreed before work starts.")
   + art("How to hire the right specialist", "Check these five things before you hire:")
   + checklist([
       "Case studies with real numbers, ideally in your industry and the UAE",
       "Ad accounts, pixels and analytics set up in your company's name",
       "Tracking fixed first, so every lead from WhatsApp, calls and forms is counted",
       "Weekly or monthly reports on leads, sales and cost per acquisition",
       "Knowledge of UAE rules: Advertiser Permits for creators, DHA rules for health ads and Trakheesi permits for property ads",
     ])
   + '<p class="muted" style="margin-top:1.5rem">Related: <a href="/dubai/digital-marketing">digital marketing services in Dubai</a> &middot; <a href="/dubai/performance-marketing">performance marketing specialist</a> &middot; <a href="/dubai/google-ads">Google Ads expert</a> &middot; <a href="/dubai/seo">SEO</a> &middot; <a href="/dubai/social-media-marketing">social media marketing</a></p>'
   + "</div></section>"),
  faqs=[
   ("What does a digital marketing specialist do?", "Plans, builds and optimises campaigns on Google, Meta, Snapchat, TikTok and LinkedIn, sets up tracking, improves landing pages and reports on the leads and sales each channel brings."),
   ("How much does a digital marketing specialist cost in Dubai?", "It depends on the channels and number of campaigns. Ad spend is paid directly to the platforms, and management is quoted in one proposal after a free discovery call."),
   ("Should I hire a freelance specialist or an agency in Dubai?", "A senior specialist suits most small and mid-sized businesses: one expert works on your account directly. Agencies suit very large budgets that need a big production team."),
   ("Which industries have you worked with in the UAE?", "Real estate, healthcare and dental clinics, home healthcare, fitness, retail and e-commerce, education and B2B services, with case studies for each on this site."),
  ])

PAGES["dubai/performance-marketing.html"] = dict(
  title="Performance Marketing Specialist in Dubai | 6.2x ROAS",
  h1="Performance Marketing Specialist in Dubai",
  quick=("Performance marketing means paying for advertising that is measured on sales and leads, not reach. As a performance marketing specialist in Dubai, "
         "Muneez Ahmed runs Google, Meta, Snapchat and TikTok campaigns tracked back to revenue in your CRM, with an average 6.2x return on ad spend across 50+ businesses."),
  section=(
   '<section class="sec sec-alt"><div class="narrow"><h2 class="h2">How performance marketing works</h2>'
   '<p class="lead">Every dirham of ad spend is tracked to a lead or sale, and budget moves every week to whatever returns the most.</p>'
   + art("The numbers that matter", "Performance marketing is judged on a short list of metrics:")
   + table(["Metric", "What it tells you"], [
       ["ROAS (return on ad spend)", "Revenue earned for every 1 AED spent on ads"],
       ["CPL / CPA", "What each lead or each sale costs"],
       ["CAC", "Total cost to win a customer, including management and tools"],
       ["LTV", "What a customer is worth over time, which sets how much you can afford to pay for one"],
       ["Conversion rate", "How many visitors become leads or buyers, usually the cheapest number to improve"],
     ])
   + art("Tracking that still works in 2026",
         "Browser privacy changes and consent rules hide a large share of conversions from ad platforms. Reliable performance marketing needs GA4 with server-side tagging, "
         "Meta Conversions API, Google enhanced conversions, offline conversion imports from your CRM and a way to tie WhatsApp enquiries back to the ad that produced them. "
         "Without this, platforms optimise on guesswork.")
   + art("Results across e-commerce and lead generation", "A selection of verified results:")
   + checklist([
       cs("kaye-co", "Kaye &amp; Co Real Estate, Dubai", "12x ROAS and $420K in commission revenue"),
       cs("sassind-melbourne", "Sassind, Melbourne", "10.36x ROAS and $162,249 in revenue"),
       cs("house-of-jersey", "House of Jersey", "10x ROAS and &#8377;85.84 lakh in annual revenue"),
       cs("lark-ellen-farm", "Lark Ellen Farm", "9.17x ROAS and $172,000 in revenue"),
       cs("flavored-pb-co", "Flavored PB Co", "6.73x ROAS from a seven-campaign Google Ads setup"),
       cs("house-of-nutrition", "House of Nutrition", "4.08x ROAS and $131,299 from catalogue sales campaigns"),
     ])
   + art("Choosing a performance marketing specialist",
         "Ask to see results in revenue, not clicks, and ask how conversions are tracked. A good specialist will want access to your CRM and sales numbers, "
         "will test creative every few weeks, and will tell you when a channel should be switched off.")
   + '<p class="muted" style="margin-top:1.5rem">Related: <a href="/dubai/digital-marketing-specialist">digital marketing specialist in Dubai</a> &middot; <a href="/dubai/google-ads">Google Ads</a> &middot; <a href="/dubai/facebook-ads">Facebook &amp; Instagram ads</a> &middot; <a href="/dubai/ppc">PPC</a> &middot; <a href="/case-studies">all case studies</a></p>'
   + "</div></section>"),
  faqs=[
   ("What is a performance marketing specialist?", "A specialist who runs paid advertising judged only on measurable outcomes such as leads, sales, cost per acquisition and return on ad spend, and who moves budget to whatever performs best."),
   ("What ROAS can I expect in Dubai?", "It depends on your margins, prices and market. Across 50+ client businesses the average has been 6.2x, with individual results from about 4x to 12x, but no honest specialist can guarantee a number before seeing your data."),
   ("How long does performance marketing take to work?", "Tracking fixes and wasted-spend cuts often show results in the first few weeks. Campaigns usually need four to eight weeks of data to optimise fully."),
   ("Which platforms do you run?", "Google Search, Performance Max, Shopping and YouTube, Meta (Facebook and Instagram), Snapchat, TikTok and LinkedIn."),
  ])



PAGES["dubai/real-estate-marketing.html"] = dict(
  title="Real Estate Marketing in Dubai | Muneez Ahmed",
  quick=("Real estate marketing in Dubai works best when Google Search captures active buyers, Meta, Snapchat and TikTok launch off-plan projects to investors, and every lead gets a WhatsApp reply within minutes. "
         "Muneez Ahmed runs these campaigns for Dubai developers and brokerages within Trakheesi and RERA rules; for Kaye &amp; Co Real Estate they returned 12x ad spend and $420K in commission."))

PAGES["dubai/website-development.html"] = dict(
  title="Website Development in Dubai | Shopify, WordPress & React",
  quick=("Website development in Dubai should deliver a fast, bilingual-ready site that turns visitors into WhatsApp enquiries and sales, with tracking, SEO and UAE payment options built in. "
         "Muneez Ahmed builds Shopify, WordPress and custom React sites for UAE businesses, including e-commerce that has generated verified sales such as &euro;69,048 for Compass Jewelry."),
  section=(
   '<section class="sec sec-alt"><div class="narrow"><h2 class="h2">Building a website that sells in the UAE</h2>'
   '<p class="lead">A good website is a sales tool first: fast, easy to act on, and measured.</p>'
   + art("Shopify, WordPress or custom?", "The right platform depends on what the site has to do:")
   + table(["Platform", "Best for", "Trade-off"], [
       ["Shopify", "Online stores that need to launch quickly and scale", "Monthly platform and app fees"],
       ["WordPress", "Service businesses, content and SEO-led sites", "Needs good hosting and regular updates"],
       ["Custom (React / Next.js)", "Portals, dashboards, bookings and anything bespoke", "Higher build cost, full flexibility"],
     ])
   + art("What every UAE business website needs", "These are built in, not added later:")
   + checklist([
       "A WhatsApp button and click-to-call on every page, tracked as conversions",
       "Fast loading on mobile, where most UAE visitors browse",
       "Arabic and right-to-left layout support where your customers need it",
       "UAE payment options for online sales, such as local card gateways and buy-now-pay-later",
       "GA4, conversion tracking and a cookie consent setup that respects the UAE Personal Data Protection Law",
       "Technical SEO from day one: clean URLs, schema markup, sitemaps and fast Core Web Vitals",
     ])
   + art("Results",
         '<a href="/case-studies/compass-jewelry">Compass Jewelry</a> went from no online presence to &euro;69,048 in verified sales and 2,800+ orders, and '
         '<a href="/case-studies/yallatoys">Yallatoys</a> in Qatar moved to a seamless web and mobile shopping experience. See all <a href="/case-studies">case studies</a>.')
   + art("How a website project runs",
         "It starts with a short call about goals, then a fixed proposal with scope, timeline and total. Design comes first so you see the site before it is built, then development, testing on real devices, launch and a handover so your team can edit content without a developer.")
   + '<p class="muted" style="margin-top:1.5rem">Related: <a href="/dubai/web-design">web design in Dubai</a> &middot; <a href="/dubai/ai-website-development">AI-powered websites</a> &middot; <a href="/dubai/seo">SEO services</a> &middot; <a href="/dubai/digital-marketing-specialist">digital marketing specialist</a></p>'
   + "</div></section>"),
  faqs=[
   ("How much does a website cost in Dubai?", "It depends on the platform, number of pages and features such as e-commerce or bookings. You receive one fixed proposal with scope, timeline and total after a free call."),
   ("Should I choose Shopify or WordPress?", "Shopify suits online stores that want to launch fast. WordPress suits service businesses and content-led SEO. Custom React builds suit portals and bespoke features."),
   ("Can my website support Arabic?", "Yes. Sites can be built bilingual with right-to-left Arabic layouts where your customers need them."),
   ("Will my website be ready for SEO and ads?", "Yes. Technical SEO, schema markup, GA4 and conversion tracking for forms, calls and WhatsApp are set up before launch."),
  ])

AUTHOR = ('<section class="sec" style="padding:2.5rem 0"><div class="narrow"><div class="card row" style="gap:1.25rem;align-items:flex-start;flex-wrap:nowrap">'
          '<img src="/images/muneez-ahmed-192.png" alt="Muneez Ahmed" width="72" height="72" loading="lazy" style="width:72px;height:72px;border-radius:50%;object-fit:cover;flex-shrink:0">'
          '<div><p class="muted" style="font-size:.8rem;text-transform:uppercase;letter-spacing:.08em;margin:0 0 .25rem">About the author</p>'
          '<p style="margin:0 0 .5rem"><strong>Muneez Ahmed</strong> is an AI &amp; growth consultant based in Dubai and co-founder of '
          '<a href="https://www.skilleaze.com/" rel="noopener" target="_blank">Skilleaze</a> and <a href="https://strattiq.com/" rel="noopener" target="_blank">StrattIQ</a>. '
          'He has scaled 50+ businesses with an average 6.2x return on ad spend, and was recognised with Google Ads Partner Excellence and the Meta Marketing Partner Award in 2024.</p>'
          '<p class="muted" style="font-size:.875rem;margin:0"><a href="https://www.linkedin.com/in/mrmnz/" rel="noopener" target="_blank">LinkedIn</a> &middot; '
          '<a href="/case-studies">Case studies</a> &middot; <a href="/awards">Awards</a> &middot; Last updated <time datetime="' + TODAY + '">25 November 2026</time></p></div></div></div></section>')


def quick_box(text):
    return ('<section class="sec" style="padding:2rem 0 0"><div class="narrow"><div class="card" style="border-left:4px solid var(--primary)">'
            '<p style="font-size:.8rem;text-transform:uppercase;letter-spacing:.08em;color:var(--primary);font-weight:700;margin:0 0 .5rem">Quick answer</p>'
            f'<p style="margin:0;line-height:1.7;font-size:1.05rem">{text}</p></div></div></section>')


def run():
    for path, cfg in PAGES.items():
        s = open(path, encoding="utf-8").read()
        for tag in ("dxb", "dxbfaq", "dxbq", "dxba"):
            s = re.sub(rf"<!--{tag}:start-->.*?<!--{tag}:end-->", "", s, flags=re.S)
        old = re.search(r"<title>(.*?)</title>", s).group(1)
        new = cfg["title"].replace("&", "&amp;")
        if old != new:
            s = s.replace(old, new)
            s = s.replace(old.replace("&amp;", "&"), cfg["title"])
        if cfg.get("h1"):
            s = re.sub(r'(<h1 class="h1"[^>]*>)[^<]*(</h1>)', lambda m: m.group(1) + cfg["h1"] + m.group(2), s, count=1)
        if cfg.get("quick"):
            i = s.index("</section>", s.index('<section class="hero"')) + len("</section>")
            s = s[:i] + "<!--dxbq:start-->" + quick_box(cfg["quick"]) + "<!--dxbq:end-->" + s[i:]
        if cfg.get("section"):
            m = re.search(r'(<section class="sec"><div class="narrow"><h2 class="h2">[^<]*what to know</h2>.*?</section>)', s, re.S)
            s = s[:m.end()] + "<!--dxb:start-->" + cfg["section"] + "<!--dxb:end-->" + s[m.end():]
        if cfg.get("faqs"):
            items = "".join(f'<details class="faq"><summary>{q}<i data-lucide="plus" style="width:18px;height:18px"></i></summary><p>{a}</p></details>' for q, a in cfg["faqs"])
            s = s.replace('<div class="faqs">', '<div class="faqs"><!--dxbfaq:start-->' + items + "<!--dxbfaq:end-->", 1)
        # author box goes right before the FAQ section
        k = s.find('<section class="sec"><div class="narrow"><h2 class="h2">Frequently asked questions')
        if k > 0:
            s = s[:k] + "<!--dxba:start-->" + AUTHOR + "<!--dxba:end-->" + s[k:]
        faqs = cfg.get("faqs", [])

        def patch(mm):
            d = json.loads(mm.group(1))
            g = d["@graph"] if "@graph" in d else [d]
            names = {q for q, _ in faqs}
            for n in g:
                if n.get("@type") == "FAQPage" and faqs:
                    n["mainEntity"] = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}} for q, a in faqs] + [x for x in n["mainEntity"] if x["name"] not in names]
                if n.get("@type") == "WebPage":
                    n["dateModified"] = TODAY
                    n["author"] = {"@id": "https://www.muneezahmed.com/#person"}
                    if cfg.get("quick"):
                        n["abstract"] = re.sub("<[^>]+>", "", cfg["quick"])
            if faqs and not any(n.get("@type") == "FAQPage" for n in g):
                g.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": re.sub("<[^>]+>", "", a)}} for q, a in faqs]})
            return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False, separators=(",", ":")) + "</script>"
        s = re.sub(r'<script type="application/ld\+json">(.*?)</script>', patch, s, count=1, flags=re.S)
        open(path, "w", encoding="utf-8").write(s)
        print("updated", path)


if __name__ == "__main__":
    run()
