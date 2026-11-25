# SEO tooling (not deployed — see .vercelignore)

- `localize.py` adds factual local context, local FAQs (+ FAQPage schema), a layout variant and a Dubai link to every city hub and city × service page. Data: `countries.py`, `cities.json`.
- `dubai_priority.py` holds the long-form guides on `/dubai/digital-marketing` and `/dubai/digital-marketing-consultant`.

Both are idempotent (content sits between `<!--loc:-->` / `<!--dxb:-->` markers). Edit the data or text, then run from the repo root:

    python3 _seo/localize.py && python3 _seo/dubai_priority.py
