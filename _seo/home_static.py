#!/usr/bin/env python3
"""Writes a <noscript> copy of the homepage's real content into index.html.

The homepage is drawn by JavaScript, so crawlers that don't run JS (Bing at times,
AI crawlers, link previews) only saw {{ placeholders }}. This runs the page's own
logic in Node, reads the same data the page shows, and writes it as plain HTML
between <!--home-static:start/end--> markers. Visitors with JavaScript never see it.

Run from the repo root after editing homepage content:  python3 _seo/home_static.py
"""
import html, json, re, subprocess

SRC = open("index.html", encoding="utf-8").read()
logic = re.search(r'<script type="text/x-dc" data-dc-script[^>]*>(.*?)</script>', SRC, re.S).group(1)
stub = """globalThis.window={innerWidth:1280,matchMedia:()=>({matches:false,addEventListener(){},removeEventListener(){}}),addEventListener(){},removeEventListener(){},localStorage:{getItem(){return null},setItem(){}},location:{hash:'',pathname:'/'},scrollTo(){}};
globalThis.React={createElement:(t,p,...ch)=>({t,p,ch}),Fragment:'F',useState:v=>[v,()=>{}],useEffect(){},useRef:()=>({current:null}),useMemo:f=>f(),createRef:()=>({current:null})};
globalThis.document={documentElement:{dataset:{}},addEventListener(){},removeEventListener(){},querySelector(){return null},getElementById(){return null},body:{style:{}}};
globalThis.localStorage=window.localStorage;globalThis.matchMedia=window.matchMedia;
class DCLogic{constructor(p){this.props=p||{};this.state={}}setState(o,cb){Object.assign(this.state,typeof o==='function'?o(this.state):o);cb&&cb();}}
"""
run = stub + logic + """
const v=new Component({}).renderVals();const o={};for(const [k,x] of Object.entries(v)){if(typeof x!=='function')o[k]=x;}
process.stdout.write(JSON.stringify(o));"""
V = json.loads(subprocess.run(["node", "-e", run], capture_output=True, text=True, check=True).stdout)
e = lambda s: html.escape(str(s or ""), quote=True)


def ul(items):
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


parts = [
    "<h2>Muneez Ahmed – AI &amp; Growth Consultant in Dubai</h2>",
    "<p>I help businesses implement AI, automate operations, run on custom software and grow with data-driven performance marketing. Based in Dubai, working with clients in the UAE and worldwide.</p>",
    "<h2>Results</h2>" + ul(f"<strong>{e(s['value'])}</strong> {e(s['label'])} – {e(s.get('description'))}" for s in V.get("aboutStats", [])),
    "<h2>What I do</h2>" + ul(f"<strong>{e(s['title'])}</strong>: {e(s['description'])}" for s in V.get("aiServices", [])),
    "<h2>How I work</h2>" + ul(f"<strong>{e(s['title'])}</strong>: {e(s['text'])}" for s in V.get("aiSteps", [])),
    "<h2>Data-driven performance marketing</h2>" + ul(f"<strong>{e(s['title'])}</strong>: {e(s['description'])}" for s in V.get("services", [])),
    "<h2>Industries I work with</h2>" + ul(f'<a href="{e(i["href"])}">{e(i["name"])}</a> – {e(i["description"])}' for i in V.get("visibleIndustries", []) if i.get("href")),
    "<h2>Core expertise</h2>" + ul(f'<a href="{e(s["href"])}">{e(s["name"])}</a>' for s in V.get("skills", []) if s.get("href")),
    "<h2>Awards and recognition</h2>" + ul(f"{e(a['title'])} – {e(a['platform'])}, {e(a['year'])}" for a in {x["title"]: x for x in V.get("awardsLoop", [])}.values()),
    "<h2>Case studies</h2>" + ul(f'<a href="/case-studies/{e(c["id"])}">{e(c["title"])}</a> ({e(c.get("category"))}, {e(c.get("client"))}): {e(c.get("description"))}' for c in V.get("visibleCases", [])),
    "<h2>Pricing</h2>" + ul(f"<strong>{e(p['title'])}</strong>: {e(p['text'])}" for p in V.get("philosophy", [])),
    "<h2>Ventures</h2>" + ul(f'<a href="{e(v["href"])}">{e(v["name"])}</a> – {e(v.get("description"))}' for v in V.get("ventures", [])),
    "<h2>Contact</h2>" + ul((f'{e(c["title"])}: <a href="{e(c["href"])}">{e(c["value"])}</a>' if c.get("href") else f'{e(c["title"])}: {e(c["value"])}') for c in V.get("contactCards", [])),
    '<p><a href="/dubai/ai-consultant">AI consultant in Dubai</a> · <a href="/dubai/digital-marketing">Digital marketing in Dubai</a> · <a href="/services">All services</a> · <a href="/case-studies">Case studies</a> · <a href="/awards">Awards</a> · <a href="/other-pages">All locations</a></p>',
]
block = '<!--home-static:start--><noscript><div style="max-width:960px;margin:0 auto;padding:24px;font-family:Inter,system-ui,sans-serif;line-height:1.6">' + "".join(parts) + "</div></noscript><!--home-static:end-->"
out = re.sub(r"<!--home-static:start-->.*?<!--home-static:end-->", "", SRC, flags=re.S)
out = out.replace("</x-dc>", "</x-dc>" + block, 1)
open("index.html", "w", encoding="utf-8").write(out)
print("homepage static copy:", len(re.sub(r"<[^>]+>", " ", block).split()), "words")
