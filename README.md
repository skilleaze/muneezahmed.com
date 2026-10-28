# muneezahmed.com — static site

Plain HTML/CSS/JS. No build step, no npm.

## Deploy (Vercel)
1. Replace everything in your GitHub repo with the contents of this folder (index.html must be at the repo root).
2. Vercel → Project → Settings → Build & Deployment:
   - Framework Preset: **Other**
   - Build Command: *(empty)*
   - Output Directory: *(empty / `.`)*
   - Install Command: *(empty)*
   - Root Directory: *(empty)*
3. Redeploy.

`vercel.json` serves clean URLs (`/dubai/ai-consultant` → `dubai/ai-consultant.html`) and holds all redirects.

## Structure (344 pages in sitemap.xml)
- `index.html` — homepage (your exact design; needs `support.js` + `uploads/` next to it)
- `dubai.html`, `dubai/*.html` — 45 Dubai keyword pages
- `services.html`, `services/*.html` — 6 worldwide service pages
- `case-studies.html`, `case-studies/*.html` — 15 case studies
- `industries.html`, `awards.html`
- `{country}/{city}.html`, `{country}/{city}/{service}.html` — 30 cities × 8 services
- `privacy-policy.html`, `terms.html`, `404.html`
- `assets/`, `images/`, `og-image.png`, `sitemap.xml`, `robots.txt`, `vercel.json` (all redirects)

## Search Console
Submit `https://www.muneezahmed.com/sitemap-index.xml`.

## To do
- Google Analytics: replace `G-XXXXXXXXXX` in every page head with your Measurement ID (find & replace across the folder).
- Old blog, case-study, service and industry pages are temporarily redirected (non-permanent) to the closest new page until they are rebuilt.

## Releasing more cities
All 219 cities are built (219 × 9 = 1,971 city pages). Wave 1 (30 cities) is live in sitemap.xml. Waves 2 and 3 exist but send a `noindex` header so Google skips them.

To release a wave:
1. In `vercel.json` → `headers`, delete the `X-Robots-Tag` entries for that wave's cities (wave 2 = the first 40 X-Robots-Tag entries, wave 3 = the rest).
2. In `sitemap-index.xml`, add: `<sitemap><loc>https://www.muneezahmed.com/sitemap-cities-waveN.xml</loc></sitemap>`
3. Push, then resubmit `sitemap-index.xml` in Search Console.

Release wave 2 only after most wave 1 pages show as indexed with impressions in Search Console.

Wave 2 (40 cities): Chicago, Austin, Boston, Vancouver, Paris, Berlin, Amsterdam, Dublin, Zurich, Madrid, Milan, Stockholm, Hong Kong, Tokyo, Cairo, Lagos, Johannesburg, Nairobi, Seattle, Dallas, Houston, Atlanta, Washington DC, Montreal, Munich, Frankfurt, Lisbon, Barcelona, Istanbul, Karachi, Lahore, Kolkata, Ahmedabad, Kuala Lumpur, Bangkok, Jakarta, Auckland, Cape Town, Geneva, Noida

Wave 3 (149 cities): Las Vegas, Denver, Calgary, Mexico City, São Paulo, Buenos Aires, Bogotá, Santiago, Birmingham, Edinburgh, Hamburg, Brussels, Vienna, Copenhagen, Oslo, Helsinki, Warsaw, Prague, Athens, Amman, Beirut, Dhaka, Colombo, Jaipur, Chandigarh, Ho Chi Minh City, Manila, Seoul, Shanghai, Taipei, Brisbane, Perth, Casablanca, Accra, Kigali, Philadelphia, Phoenix, San Diego, San Jose, Orlando, Tampa, Nashville, Charlotte, Minneapolis, Detroit, Portland, Salt Lake City, Raleigh, Honolulu, Ottawa, Edmonton, Monterrey, Guadalajara, Lima, Rio de Janeiro, Panama City, San José, Montevideo, Santo Domingo, Leeds, Glasgow, Bristol, Liverpool, Cambridge, Cork, Lyon, Marseille, Nice, Cologne, Düsseldorf, Stuttgart, Rotterdam, The Hague, Eindhoven, Basel, Luxembourg City, Rome, Turin, Valencia, Málaga, Porto, Kraków, Budapest, Bucharest, Sofia, Belgrade, Zagreb, Tallinn, Riga, Vilnius, Limassol, Valletta, Reykjavik, Ankara, Tbilisi, Baku, Almaty, Tashkent, Tel Aviv, Erbil, Mecca, Medina, Al Ain, Salalah, Al Wakrah, Indore, Lucknow, Coimbatore, Thiruvananthapuram, Visakhapatnam, Nagpur, Surat, Goa, Bhubaneswar, Kathmandu, Malé, Islamabad, Jurong, Penang, Phuket, Hanoi, Bali, Cebu, Shenzhen, Beijing, Guangzhou, Osaka, Busan, Adelaide, Gold Coast, Canberra, Wellington, Christchurch, Alexandria, Tunis, Algiers, Marrakech, Rabat, Dakar, Abidjan, Abuja, Addis Ababa, Dar es Salaam, Kampala, Port Louis, Durban, Lusaka, Gaborone, Luanda
