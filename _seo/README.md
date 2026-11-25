# SEO tooling (not deployed — see .vercelignore)

- `localize.py` adds factual local context, local FAQs (+ FAQPage schema), a layout variant and a Dubai link to every city hub and city × service page. Data: `countries.py`, `cities.json`.
- `dubai_priority.py` holds the long-form guides on `/dubai/digital-marketing` and `/dubai/digital-marketing-consultant`.

Both are idempotent (content sits between `<!--loc:-->` / `<!--dxb:-->` markers). Edit the data or text, then run from the repo root:

    python3 _seo/localize.py && python3 _seo/dubai_priority.py
- `home_static.py` writes a `<noscript>` copy of the homepage (the live homepage is drawn by JavaScript). Re-run after editing homepage content.
- `build_pages.py` rebuilds `admin/pages.json`, the page inventory shown on /admin → SEO pages. Re-run after adding or editing pages.

## Admin dashboard (/admin)

- Visits are recorded by `/ma-track.js` (on every page) into Supabase table `ma_events` (project ojshkwpvkzrkiwannqkk).
- Login is checked by the `ma_admin_login` database function; the password is stored only as a bcrypt hash in `ma_admin`, never in this repo. To change it, run in Supabase SQL editor:
  `update ma_admin set pass_hash = extensions.crypt('NEW-PASSWORD', extensions.gen_salt('bf')) where username = 'admin';`
- Google keywords come from the `ma-gsc` Edge Function, which reads Search Console with the shared `GSC_SERVICE_ACCOUNT` secret. Add that service account's email as a user on the muneezahmed.com property in Search Console.

## IndexNow (Bing, Yandex; feeds ChatGPT search and Copilot)

Key file: /a0d3828d81b0a6890408ba270260167a.txt (key also in `_seo/indexnow.key`). After a deploy, POST the changed URLs to https://api.indexnow.org/indexnow with {"host":"www.muneezahmed.com","key":"a0d3828d81b0a6890408ba270260167a","keyLocation":"https://www.muneezahmed.com/a0d3828d81b0a6890408ba270260167a.txt","urlList":[...]}.
