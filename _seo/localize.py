#!/usr/bin/env python3
"""Adds unique, factual local content to every city and city x service page.

Run from the repo root:  python3 _seo/localize.py
Idempotent: everything it adds sits between <!--loc:...--> markers and is
replaced on each run. Data lives in _seo/countries.py and _seo/cities.json.
"""
import glob, hashlib, html, json, os, re, sys

sys.path.insert(0, os.path.dirname(__file__))
from countries import C  # noqa: E402

ROOT = os.getcwd()
CITIES = json.load(open(os.path.join(os.path.dirname(__file__), "cities.json")))
DST = {"united-states", "canada", "united-kingdom", "ireland", "norway", "switzerland", "serbia",
       "new-zealand", "chile", "israel", "lebanon", "egypt", "australia"}
SERVICES = {
    "ai-consulting": "AI consulting", "ai-automation": "AI automation", "ai-chatbots": "AI agents and chatbots",
    "custom-crm-erp": "custom CRM and ERP development", "digital-marketing": "digital marketing",
    "google-ads": "Google Ads management", "performance-marketing": "performance marketing", "seo": "SEO",
}
NO_DST_CITIES = {"brisbane", "gold-coast", "perth", "darwin", "phoenix", "honolulu"}
ICON = {"time": "clock", "lang": "languages", "cur": "banknote", "msg": "message-circle", "search": "search",
        "social": "megaphone", "law": "shield-check", "week": "calendar"}


def h(seed, n):
    return int(hashlib.md5(seed.encode()).hexdigest(), 16) % n


def the(c):
    return "the " + c if c in {"United States", "United Kingdom", "United Arab Emirates", "Netherlands", "Philippines", "Czech Republic", "Dominican Republic", "Maldives"} else c


def pick(seed, options):
    return options[h(seed, len(options))]


def join(xs):
    xs = list(xs)
    return xs[0] if len(xs) == 1 else ", ".join(xs[:-1]) + " and " + xs[-1]


def e(s):
    return html.escape(s, quote=False)


def hm(x):
    x %= 24
    return f"{int(x):02d}:{int(round((x - int(x)) * 60)):02d}"


# ---------------------------------------------------------------- facts
def facts(key):
    ci = CITIES[key]
    co = C[ci["country_slug"]]
    city, off = ci["city"], ci["offset"]
    f = dict(ci=ci, co=co, city=city, country=ci["country"], country_the=the(ci["country"]))
    if off == 0:
        f["tz"] = f"{city} shares Dubai's time zone, so the whole working day overlaps."
        f["tz_short"] = "Same time as Dubai"
        f["overlap"] = 9
    else:
        a = abs(off)
        hrs = f"{a:g} hour" + ("" if a == 1 else "s")
        rel = "ahead of" if off > 0 else "behind"
        ov = max(0.0, 9 - a)
        f["overlap"] = ov
        f["tz_short"] = f"{hrs} {rel} Dubai"
        your10 = hm(10 - off)
        if ov >= 4:
            tail = f"a standard 9:00 to 18:00 day overlaps by about {ov:g} hours, so live calls are easy to schedule."
        elif ov > 0:
            tail = f"a standard 9:00 to 18:00 day overlaps by only about {ov:g} hours, so calls go at the start or end of your day and the rest runs asynchronously."
        else:
            tail = "working days do not overlap, so I keep a fixed weekly call at the edge of your day and handle everything else in writing."
        f["tz"] = f"{city} is {hrs} {rel} Dubai: 10:00 in {city} is {your10} in Dubai, and {tail}"
        if ci["country_slug"] in DST and ci["city_slug"] not in NO_DST_CITIES:
            f["tz"] += " The gap moves by an hour when daylight saving time changes."
    f["lang"] = join(co["lang"])
    f["english_only"] = co["lang"] == ["English"]
    f["cur"] = co["cur"]
    f["cur_txt"] = "USD" if co.get("usd_native") else f"{co['cur']} or USD"
    f["msg"] = join(co["msg"])
    f["msg1"] = co["msg"][0]
    f["search"] = co.get("search") or "Google is the dominant search engine"
    f["social"] = join(co["social"])
    f["law"] = co["law"]
    f["law_txt"] = co["law"] or "local data-protection rules"
    f["week"] = ("Sunday to Thursday" if co.get("fri_sat") else
                 "Sunday to Friday, with Saturday off" if co.get("sat_only") else "Monday to Friday")
    f["eu"] = co.get("eu") or ci["country_slug"] in {"united-kingdom", "norway", "iceland", "switzerland"}
    return f


# ---------------------------------------------------------------- service paragraphs
CHANNEL = {
    "WhatsApp": "the WhatsApp Business Platform", "LINE": "a LINE Official Account",
    "KakaoTalk": "a Kakao Talk channel", "WeChat": "a WeChat Official Account", "Zalo": "a Zalo Official Account",
    "Telegram": "a Telegram bot", "Viber": "Viber business messaging", "Facebook Messenger": "Messenger through Meta's API",
    "SMS": "SMS and website chat", "imo": "WhatsApp and Messenger",
}


def law_para(f, seed):
    if f["law"]:
        return pick(seed, [
            f"Anything that touches customer or employee data in {f['city']} has to respect {f['law']}. I settle what data each system may see, where it is processed and how long it is kept before the first pilot, not after.",
            f"Data protection in {f['country_the']} is governed by {f['law']}. Consent, access controls and data location are designed in from day one, so legal review is a formality rather than a blocker.",
            f"Compliance is part of the build, not an afterthought: personal data in {f['country_the']} falls under {f['law']}, and every workflow I deliver documents what it collects and why.",
        ])
    return (f"Where data-protection rules in {f['country_the']} are still developing, I apply GDPR-grade practice by default: "
            "minimal data, clear access controls and documented processing, so nothing needs rework if the rules tighten.")


def lang_para(f, svc_word, seed):
    if f["english_only"]:
        return pick(seed, [
            f"Most {f['city']} teams and customers work in English, so the effort goes into accuracy instead of translation: grounding {svc_word} in your own data, terminology and tone of voice.",
            f"With English as the working language in {f['city']}, the priority is precision, using your own documents, prices and policies so nothing generic reaches a customer.",
        ])
    return pick(seed, [
        f"Business in {f['city']} runs in {f['lang']}, so {svc_word} is planned and tested " + ("in each language your customers use" if len(f["co"]["lang"]) > 1 else f"in {f['lang']} from the start") + ", not translated at the end.",
        f"Your customers in {f['city']} write in {f['lang']}. I test {svc_word} with real examples " + ("in each language" if len(f["co"]["lang"]) > 1 else f"in {f['lang']}") + " before launch, because tone and terminology matter as much as accuracy.",
    ])


def service_paras(svc, f, seed):
    ci, co, city = f["ci"], f["co"], f["city"]
    ch = CHANNEL.get(f["msg1"], f["msg1"])
    P = []
    if svc == "ai-consulting":
        P.append(f"{ci['why']} In {city}, the AI use cases that pay off first usually sit in {ci['industries']}, where volumes are high and processes repeat every day.")
        P.append(lang_para(f, "every AI use case", seed + "l"))
        P.append(law_para(f, seed + "w"))
    elif svc == "ai-automation":
        P.append(f"Customers in {city} mostly reach businesses through {f['msg']}, so many automations start there: capturing enquiries, routing them to the right person and logging every conversation in your CRM without copy-paste.")
        P.append(f"Invoices, payment reminders and reports are set up in {f['cur']}" + ("" if co.get("usd_native") else ", with USD alongside where you bill internationally")
                 + f", and schedules follow a {f['week']} working week.")
        P.append(law_para(f, seed + "w"))
    elif svc == "ai-chatbots":
        P.append(f"A chatbot only works if it lives where customers already message. In {city} that is {f['msg']}, " + ("so assistants are built for SMS and website chat, sharing one knowledge base." if ch == CHANNEL['SMS'] else f"so assistants are usually built on {ch}, with your website chat connected to the same knowledge base."))
        P.append(lang_para(f, "the assistant", seed + "l"))
        P.append(law_para(f, seed + "w"))
    elif svc == "custom-crm-erp":
        P.append(f"Systems for {city} companies handle {f['cur']} natively" + ("" if co.get("usd_native") else " alongside USD and other trading currencies")
                 + f", follow a {f['week']} working week for SLAs and reminders, and plug into {f['msg1']} so sales and support conversations land on the right record.")
        P.append(("Screens, documents and notifications are built in English." if f["english_only"] else
                  f"Screens, documents and customer notifications can be delivered in {f['lang']}."))
        P.append(law_para(f, seed + "w"))
    elif svc == "digital-marketing":
        P.append(f"The channel mix in {city} is not a copy of a global template. Here, {f['social']} carry most of the paid and organic reach, and most enquiries end up on {f['msg1']}. On search, {f['search'][0].lower() + f['search'][1:] if not f['search'].startswith('Google') else f['search']}.")
        P.append(lang_para(f, "campaign creative", seed + "l"))
        if f["eu"]:
            P.append("Tracking is set up with a proper cookie consent banner and Google Consent Mode v2, which Google requires for personalised advertising to users in the EEA and UK.")
        else:
            P.append(law_para(f, seed + "w"))
    elif svc == "google-ads":
        if co.get("china"):
            P.append(f"{f['search']}. For {city} companies selling to mainland Chinese buyers, Baidu advertising replaces Google Ads; for exporters and firms targeting overseas customers, Google Ads remains the main search channel and is run from outside the mainland.")
        else:
            extra = {"south-korea": " Naver search ads are often added alongside Google for Korean-language demand.",
                     "czech-republic": " For Czech-language demand, Seznam's Sklik is worth testing next to Google.",
                     "japan": " Because Yahoo! JAPAN search runs on Google technology, strong Google SEO and Ads cover most of the market, with Yahoo! JAPAN ads as an optional addition.",
                     "kazakhstan": " For Russian-speaking audiences, Yandex Direct can complement Google.",
                     "uzbekistan": " For Russian-speaking audiences, Yandex Direct can complement Google."}.get(ci["country_slug"], "")
            P.append(f"{f['search']} in {f['country_the']}, so Google Ads is the main paid search channel for {city} businesses.{extra}")
        P.append(f"Campaigns are billed in {f['cur']}, targeted around {ci['neighborhoods']} and the wider {city} area where it makes sense, and written in "
                 + ("English" if f["english_only"] else f"the languages people actually search in ({f['lang']})")
                 + (". Call and lead-form assets turn clicks into conversations." if f["msg1"] in ("SMS", "iMessage") else f". Call and {f['msg1']} click-to-chat assets turn clicks into conversations."))
        P.append("Conversion tracking uses Google Consent Mode v2, required for personalised ads in the EEA and UK." if f["eu"] else law_para(f, seed + "w"))
    elif svc == "performance-marketing":
        P.append(f"In {city}, budgets usually split across Google and {f['social']}. Every channel is judged on the same numbers: cost per qualified lead or sale, and return on ad spend in {f['cur']}.")
        P.append(lang_para(f, "ad creative", seed + "l"))
        P.append("Server-side tracking and Consent Mode v2 keep measurement reliable under EEA and UK consent rules." if f["eu"] else law_para(f, seed + "w"))
    elif svc == "seo":
        slug = ci["country_slug"]
        if slug == "china":
            P.append("Ranking in mainland China means optimising for Baidu: Simplified Chinese content, fast loading from inside China, and an ICP filing if the site is hosted on the mainland. For international audiences, Google SEO runs in parallel.")
        elif slug == "south-korea":
            P.append("In South Korea, SEO covers Google and Naver. Naver favours its own properties, so a Naver Blog and Smart Place listing sit alongside your website.")
        else:
            P.append(f"{f['search']} in {f['country_the']}. Local rankings in {city} depend on a complete Google Business Profile, consistent business details across local directories and pages that answer what people in {ci['neighborhoods']} actually search for.")
        if f["english_only"]:
            P.append(f"A {co['tld']} domain or a country folder on your main domain tells search engines which market a page serves. Content is written for how people in {city} phrase searches, not for a global audience.")
        else:
            P.append(f"Content is planned for searches in {f['lang']}, with hreflang tags so each language version ranks in the right market and a clear choice between a {co['tld']} domain and country folders on your main site.")
        P.append(law_para(f, seed + "w"))
    return P


# ---------------------------------------------------------------- blocks
def rows(f, svc):
    r = [("time", "Time difference", f["tz_short"] + (f", ~{f['overlap']:g}h overlap" if 0 < f["overlap"] < 9 else "")),
         ("lang", "Business languages", f["lang"]),
         ("cur", "Quotes and billing", f["cur_txt"]),
         ("msg", "How customers message", f["msg"]),
         ("search", "Search", f["search"]),
         ("social", "Key platforms", f["social"]),
         ("law", "Data protection", f["law_txt"][0].upper() + f["law_txt"][1:]),
         ("week", "Working week", f["week"])]
    order = {"seo": ["search", "lang"], "google-ads": ["search", "cur"], "ai-chatbots": ["msg", "lang"],
             "performance-marketing": ["social", "cur"], "digital-marketing": ["social", "search"],
             "custom-crm-erp": ["cur", "law"], "ai-automation": ["msg", "week"], "ai-consulting": ["law", "lang"]}[svc]
    return sorted(r, key=lambda x: order.index(x[0]) if x[0] in order else 9)


def facts_block(f, svc, v):
    rs = rows(f, svc)
    if v == 0:
        items = "".join(f'<div><dt>{e(lab)}</dt><dd>{e(val)}</dd></div>' for _, lab, val in rs)
        return f'<dl class="loc-dl">{items}</dl>'
    if v == 1:
        items = "".join(f'<div class="card loc-card"><div class="ico"><i data-lucide="{ICON[k]}" style="width:18px;height:18px"></i></div>'
                        f'<h3 class="h3">{e(lab)}</h3><p class="muted">{e(val)}</p></div>' for k, lab, val in rs[:6])
        return f'<div class="grid loc-grid" style="--min:230px">{items}</div>'
    items = "".join(f'<li><i data-lucide="{ICON[k]}" style="width:18px;height:18px"></i><span><strong>{e(lab)}:</strong> {e(val)}</span></li>' for k, lab, val in rs)
    return f'<ul class="list loc-list">{items}</ul>'


def local_section(key, svc, label):
    f = facts(key)
    seed = key + svc
    v = h(seed + "layout", 3)
    city = f["city"]
    title = pick(seed + "t", [
        f"{label}: the local details",
        f"What's different about {SERVICES[svc]} in {city}",
        f"{city} at a glance for {SERVICES[svc]}",
        f"Working with {city} businesses: practical details",
    ])
    intro = pick(seed + "i", [
        f"The basics that shape how {SERVICES[svc]} projects run for {city} businesses, from time zones to data rules.",
        f"Before any work starts, these local factors decide channels, tools and schedules for {city} clients.",
        f"A short, factual brief on {city} and {f['country_the']}, and how each point changes the plan.",
    ])
    paras = service_paras(svc, f, seed)
    paras.insert(1 if v != 2 else 0, f["tz"])
    prose = "".join(f'<p class="muted" style="line-height:1.75;font-size:1.05rem;margin-top:1rem">{e(p)}</p>' for p in paras)
    sub = pick(seed + "s", [f"How this shapes {SERVICES[svc]} in {city}", f"What it means for your project", f"Putting it into practice in {city}"])
    block = facts_block(f, svc, v)
    prose += home_link(svc, seed)
    alt = " sec-alt" if v == 1 else ""
    if v == 2:
        inner = (f'<div class="wrap grid" style="--min:340px;gap:3rem;align-items:start"><div><h2 class="h2">{e(title)}</h2><p class="lead">{e(intro)}</p>{prose}</div>'
                 f'<aside class="card">{block}</aside></div>')
    else:
        inner = (f'<div class="{"narrow" if v == 0 else "wrap"}"><h2 class="h2">{e(title)}</h2><p class="lead" style="margin-bottom:1.5rem">{e(intro)}</p>{block}'
                 f'<h3 class="h3" style="margin-top:2rem">{e(sub)}</h3>{prose}</div>')
    return f'<!--loc:start--><section class="sec{alt} loc loc-v{v}">{inner}</section><!--loc:end-->', f, v


HOME = {"ai": ("/dubai/ai-consultant", ["working with an AI consultant in Dubai", "AI consulting in Dubai", "my work as an AI consultant in Dubai"]),
        "digital-marketing": ("/dubai/digital-marketing", ["digital marketing services in Dubai", "digital marketing in Dubai", "my digital marketing work in Dubai"]),
        "seo": ("/dubai/digital-marketing-specialist", ["hiring a digital marketing specialist in Dubai", "my work as a digital marketing specialist in Dubai", "digital marketing specialist services in Dubai"]),
        "perf": ("/dubai/performance-marketing", ["hiring a performance marketing specialist in Dubai", "performance marketing in Dubai", "my work as a performance marketing specialist in Dubai"])}


def home_link(svc, seed):
    key = ("ai" if svc in ("ai-consulting", "ai-automation", "ai-chatbots", "custom-crm-erp") else
           "seo" if svc == "seo" else "perf" if svc in ("google-ads", "performance-marketing") else "digital-marketing")
    url, anchors = HOME[key]
    a = pick(seed + "home", anchors)
    lead = pick(seed + "homel", ["I'm based in Dubai and work with clients worldwide. More about", "Home base is Dubai, where most of my clients are. Read about", "Delivered from Dubai, the same way I work with UAE clients. Read more on"])
    return f'<p class="muted" style="margin-top:1rem">{lead} <a href="{url}">{a}</a>.</p>'


def local_faqs(f, svc, key):
    city = f["city"]
    q = []
    q.append((pick(key + "fq1", [f"What time are calls for {city} clients?", f"How do you handle the time difference with {city}?"]), f["tz"]))
    if svc in ("ai-chatbots", "ai-automation", "custom-crm-erp"):
        q.append((f"Which messaging apps do you integrate with in {city}?",
                  f"Mostly {f['msg']}, since that is where {city} customers contact businesses. Integrations connect to your CRM and website chat so every conversation is recorded."))
    elif svc in ("seo", "google-ads"):
        q.append((f"Which search engines matter in {f['country_the']}?", f["search"] + ". Strategy and budgets are planned around that."))
    else:
        q.append((f"Which platforms work best for {city} businesses?", f"Usually Google plus {f['social']}, with {f['msg1']} as the conversation channel. The final mix depends on your audience and margins."))
    q.append((f"Is my data handled in line with the rules in {f['country_the']}?",
              (f"Yes. Work is set up to comply with {f['law']}, with documented data flows and access limited to what each system needs." if f["law"]
               else f"Yes. I follow GDPR-grade practice by default: minimal data, documented processing and strict access controls.")))
    return q


# ---------------------------------------------------------------- page fixes
def fix_common(s, f, svc):
    s = re.sub(r"in ([A-Z]{3}) or \1(?=[,<\"])", r"in \1", s)
    s = re.sub(r"quoted after a discovery call, in [A-Z]{3}(?: or USD)?", f"quoted after a discovery call, in {f['cur_txt']}", s)
    s = re.sub(r"(?<=\bin )(?=(United States|United Kingdom|United Arab Emirates|Netherlands|Philippines|Czech Republic|Dominican Republic|Maldives)\b)", "the ", s)
    s = re.sub(r"\b[A-Z]{3} or USD(?= after a free discovery| with scope|, with scope)", f["cur_txt"], s)
    s = re.sub(r"\ba ai\b", "an AI", s)
    s = re.sub(r"\ba (ai|seo) ", lambda m: "an " + m.group(1).upper() + " ", s)
    if svc is None:
        return s
    for old, new in PHRASES.items():
        s = re.sub(rf"(?<=invest in ){re.escape(old)}(?=</h3>)", new, s)
        s = re.sub(rf"(?<=, ){re.escape(old)}(?= is a way| means)", new, s)
    return s


PHRASES = {"ai consulting": "AI consulting", "seo &amp; ai search": "SEO &amp; AI search", "google ads management": "Google Ads management",
           "custom crm &amp; erp development": "custom CRM &amp; ERP development", "ai agents &amp; chatbots": "AI agents &amp; chatbots",
           "ai &amp; business automation": "AI &amp; business automation"}


def strip_markers(s):
    s = re.sub(r"<!--loc:start-->.*?<!--loc:end-->", "", s, flags=re.S)
    s = re.sub(r"<!--locfaq:start-->.*?<!--locfaq:end-->", "", s, flags=re.S)
    s = re.sub(r"\n\n(?=<section class=\"sec sec-alt\"><div class=\"wrap\"><div class=\"row\" style=\"justify-content:space-between)", "\n\n", s)
    return s


def add_faq(s, qs):
    html_q = "".join(f'<details class="faq"><summary>{e(q)}<i data-lucide="plus" style="width:18px;height:18px"></i></summary><p>{e(a)}</p></details>' for q, a in qs)
    s = s.replace('<div class="faqs">', f'<div class="faqs"><!--locfaq:start-->{html_q}<!--locfaq:end-->', 1)

    def patch(m):
        d = json.loads(m.group(1))
        for node in d.get("@graph", []):
            if node.get("@type") == "FAQPage":
                existing = {x["name"] for x in node["mainEntity"]}
                node["mainEntity"] = [x for x in node["mainEntity"] if not x.get("_loc")]
                new = [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in qs]
                names = {q for q, _ in qs}
                node["mainEntity"] = new + [x for x in node["mainEntity"] if x["name"] not in names and not x["name"].startswith(("What time are calls", "How do you handle the time difference", "Which messaging apps", "Which search engines matter", "Which platforms work best", "Is my data handled"))]
            if node.get("@type") == "WebPage":
                node["dateModified"] = TODAY
        return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False, separators=(",", ":")) + "</script>"
    s = re.sub(r'<script type="application/ld\+json">(.*?)</script>', patch, s, count=1, flags=re.S)
    return s


def fix_jsonld_currency(s, f):
    return re.sub(r"in [A-Z]{3}(?: or USD)?, with scope", f"in {f['cur_txt']}, with scope", s)


def set_variant(s, v):
    s = re.sub(r'<body( data-v="\d")?>', f'<body data-v="{v}">', s, count=1)
    return s


TESTI_IMG = re.compile(r'<img src="(?:\.\./)*images/t-(\w+)\.png" alt="([^"]+)"[^>]*>')


def initials(s):
    def rep(m):
        name = m.group(2)
        ini = "".join(w[0] for w in re.sub(r"^Dr\.\s*", "", name).split()[:2]).upper()
        return f'<span class="avatar" aria-hidden="true">{ini}</span>'
    return TESTI_IMG.sub(rep, s)


def process_service(path, key, svc):
    s = open(path, encoding="utf-8").read()
    s = strip_markers(s)
    m = re.search(r'<span class="pill">([^·<]*) ·', s)
    label = (m.group(1).strip() if m else SERVICES[svc]).replace("&amp;", "&")
    sec, f, v = local_section(key, svc, label)
    s = fix_common(s, f, svc)
    s = fix_jsonld_currency(s, f)
    anchors = [r'(<section class="sec"><div class="narrow"><h2 class="h2">[^<]*what to know</h2>.*?</section>)',
               r'(<section class="sec sec-alt"><div class="wrap"><h2 class="h2">What you get</h2>.*?</section>)',
               r'(</div></section>\n\n<section class="sec sec-alt"><div class="wrap"><div class="row" style="justify-content:space-between;margin-bottom:2rem"><h2 class="h2" style="margin:0">What clients say)']
    pos = h(key + svc + "pos", 3)
    if pos < 2:
        s, n = re.subn(anchors[pos], lambda mm: mm.group(1) + sec, s, count=1, flags=re.S)
    else:
        s, n = re.subn(r'(<section class="sec sec-alt"><div class="wrap"><div class="row" style="justify-content:space-between;margin-bottom:2rem"><h2 class="h2" style="margin:0">What clients say)',
                       lambda mm: sec + mm.group(1), s, count=1)
    if not n:
        s = s.replace("<main>", "<main>", 1).replace('<section class="sec sec-alt"><div class="wrap"><h2 class="h2">What you get</h2>', sec + '<section class="sec sec-alt"><div class="wrap"><h2 class="h2">What you get</h2>', 1)
    s = add_faq(s, local_faqs(f, svc, key))
    s = set_variant(s, v)
    s = initials(s)
    open(path, "w", encoding="utf-8").write(s)


# ---------------------------------------------------------------- city hub pages
def process_hub(path, key):
    s = open(path, encoding="utf-8").read()
    s = strip_markers(s)
    f = facts(key)
    s = fix_common(s, f, None)
    ci, city = f["ci"], f["city"]
    v = h(key + "hub", 3)
    title = pick(key + "ht", [f"Doing business in {city}: what I plan around", f"{city} at a glance", f"Working with {city} companies"])
    paras = [
        f"{ci['why']} The strongest demand for AI, automation and growth work comes from {ci['industries']}, with many clients based in {ci['neighborhoods']}.",
        f["tz"],
        f"Customers here mostly reach businesses through {f['msg']}. {f['search']} in {f['country_the']}. Paid and organic reach usually comes from Google plus {f['social']}.",
        (f"Personal data is governed by {f['law']}, so every system and campaign is set up to comply from the start." if f["law"]
         else "I apply GDPR-grade data practice by default, so systems stay compliant as local rules develop."),
        f"Work is quoted in {f['cur_txt']}" + (f", delivered in English" if f["english_only"] else f", with content and interfaces available in {f['lang']}") + f", on a {f['week']} schedule.",
    ]
    if v == 1:
        paras = paras[1:] + paras[:1]
    prose = "".join(f'<p class="muted" style="line-height:1.75;font-size:1.05rem;margin-top:1rem">{e(p)}</p>' for p in paras)
    block = facts_block(f, "ai-consulting", v)
    sec = (f'<!--loc:start--><section class="sec{" sec-alt" if v == 1 else ""} loc loc-v{v}"><div class="wrap grid" style="--min:340px;gap:3rem;align-items:start">'
           f'<div><h2 class="h2">{e(title)}</h2>{prose}</div><aside class="card">{block}</aside></div></section>'
           + hub_faq(f, key) + '<!--loc:end-->')
    s = s.replace("</main>", sec + "</main>", 1)
    s = set_variant(s, v)
    s = add_hub_schema(s, f, key)
    open(path, "w", encoding="utf-8").write(s)


def hub_qs(f):
    city = f["city"]
    return [(f"Do you work with businesses in {city}?", f"Yes. I work with {city} companies remotely from Dubai on AI, automation, custom software and performance marketing. " + f["tz"]),
            (f"Which messaging and ad platforms matter in {city}?", f"Customers mostly use {f['msg']}. For reach, Google plus {f['social']} cover most of the market."),
            (f"How are {city} projects priced?", f"Every engagement is quoted in {f['cur_txt']} after a free discovery call, with scope, timeline and total agreed before work begins.")]


def hub_faq(f, key):
    items = "".join(f'<details class="faq"><summary>{e(q)}<i data-lucide="plus" style="width:18px;height:18px"></i></summary><p>{e(a)}</p></details>' for q, a in hub_qs(f))
    return f'<section class="sec sec-alt"><div class="narrow"><h2 class="h2">Questions from {e(f["city"])} businesses</h2><div class="faqs">{items}</div></div></section>'


def add_hub_schema(s, f, key):
    def patch(m):
        d = json.loads(m.group(1))
        g = d.setdefault("@graph", []) if "@graph" in d else None
        if g is None:
            d = {"@context": "https://schema.org", "@graph": [{k: v for k, v in d.items() if k != "@context"}]}
            g = d["@graph"]
        g[:] = [n for n in g if n.get("@type") != "FAQPage"]
        g.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in hub_qs(f)]})
        for n in g:
            if n.get("@type") == "WebPage":
                n["dateModified"] = TODAY
        return '<script type="application/ld+json">' + json.dumps(d, ensure_ascii=False, separators=(",", ":")) + "</script>"
    return re.sub(r'<script type="application/ld\+json">(.*?)</script>', patch, s, count=1, flags=re.S)


TODAY = os.environ.get("SEO_DATE", "2026-11-25")

if __name__ == "__main__":
    done = 0
    for key in CITIES:
        hub = key + ".html"
        if os.path.exists(hub):
            process_hub(hub, key); done += 1
        for svc in SERVICES:
            p = f"{key}/{svc}.html"
            if os.path.exists(p):
                process_service(p, key, svc); done += 1
    print("updated", done, "pages")
