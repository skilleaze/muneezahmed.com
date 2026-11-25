// Supabase Edge Function "ma-ga4": Google Analytics 4 history for the muneezahmed.com admin dashboard.
// Auth: ma_admin_login (verify_jwt OFF on purpose). Secret: GSC_SERVICE_ACCOUNT (shared service account).
// GA4 property 500523357 (measurement ID G-1FSNC44H0K); MA_GA4_PROPERTY can override it.
// Body: { user, pass, from, to, clean?: boolean, custom?: [{ dims, mets, limit, filter }] }
//   clean  -> excludes likely bot traffic (data-centre cities, unknown US cities, crawler screen sizes).
//   custom -> admin-only ad-hoc reports (read-only).
const CORS = { "Access-Control-Allow-Origin": "*", "Access-Control-Allow-Headers": "authorization, x-client-info, apikey, content-type", "Access-Control-Allow-Methods": "POST, OPTIONS" };
const json = (b: unknown, s = 200) => new Response(JSON.stringify(b), { status: s, headers: { ...CORS, "Content-Type": "application/json" } });
const b64u = (u: Uint8Array) => btoa(String.fromCharCode(...u)).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
const PROPERTY = "500523357";
// Likely bots: cloud data-centre towns (AWS, Microsoft, Google, Meta), unknown US cities, and screen sizes
// only crawlers report. Found from this property's own data (Nov 2026).
const BOT_CITIES = ["Ashburn", "Boardman", "Council Bluffs", "The Dalles", "Moses Lake", "Quincy", "Prineville", "Lanzhou",
  "Des Moines", "Flint Hill", "Boydton", "Forest City", "Altoona", "Fort Worth", "Gallatin", "Los Lunas", "Papillion",
  "Eagle Mountain", "Henrico", "Sandston", "Lenoir", "Pryor", "Clarksville", "Aspen", "Glenview"];
const BOT_SCREENS = ["800x600", "2000x2000", "1024x1024", "1080x600"];
async function token(sa: { client_email: string; private_key: string }) {
  const now = Math.floor(Date.now() / 1000);
  const enc = (o: unknown) => b64u(new TextEncoder().encode(JSON.stringify(o)));
  const unsigned = enc({ alg: "RS256", typ: "JWT" }) + "." + enc({ iss: sa.client_email, scope: "https://www.googleapis.com/auth/analytics.readonly", aud: "https://oauth2.googleapis.com/token", iat: now, exp: now + 3600 });
  const pem = sa.private_key.replace(/-----[^-]+-----/g, "").replace(/\s+/g, "");
  const der = Uint8Array.from(atob(pem), (c) => c.charCodeAt(0));
  const key = await crypto.subtle.importKey("pkcs8", der, { name: "RSASSA-PKCS1-v1_5", hash: "SHA-256" }, false, ["sign"]);
  const sig = new Uint8Array(await crypto.subtle.sign("RSASSA-PKCS1-v1_5", key, new TextEncoder().encode(unsigned)));
  const r = await fetch("https://oauth2.googleapis.com/token", { method: "POST", headers: { "Content-Type": "application/x-www-form-urlencoded" },
    body: "grant_type=urn%3Aietf%3Aparams%3Aoauth%3Agrant-type%3Ajwt-bearer&assertion=" + unsigned + "." + b64u(sig) });
  const j = await r.json();
  if (!j.access_token) throw new Error("Google sign-in failed: " + JSON.stringify(j).slice(0, 200));
  return j.access_token as string;
}
Deno.serve(async (req) => {
  if (req.method === "OPTIONS") return new Response("ok", { headers: CORS });
  let email = "";
  try {
    const { user, pass, from, to, clean, custom } = await req.json();
    const SUPA = Deno.env.get("SUPABASE_URL")!, ANON = Deno.env.get("SUPABASE_ANON_KEY")!;
    const ok = await fetch(SUPA + "/rest/v1/rpc/ma_admin_login", { method: "POST", headers: { apikey: ANON, Authorization: "Bearer " + ANON, "Content-Type": "application/json" },
      body: JSON.stringify({ p_user: user, p_pass: pass }) }).then((r) => r.json()).catch(() => false);
    if (ok !== true) return json({ error: "Wrong username or password" }, 401);
    const raw = Deno.env.get("GSC_SERVICE_ACCOUNT") || "";
    if (!raw) return json({ setup: true });
    const sa = JSON.parse(raw); email = sa.client_email;
    const tk = await token(sa);
    const prop = Deno.env.get("MA_GA4_PROPERTY") || PROPERTY;
    const dr = [{ startDate: from, endDate: to }];
    const botFilter = { andGroup: { expressions: [
      { notExpression: { filter: { fieldName: "city", inListFilter: { values: BOT_CITIES } } } },
      { notExpression: { filter: { fieldName: "screenResolution", inListFilter: { values: BOT_SCREENS } } } },
      { notExpression: { andGroup: { expressions: [{ filter: { fieldName: "city", stringFilter: { value: "(not set)" } } }, { filter: { fieldName: "country", stringFilter: { value: "United States" } } }] } } },
    ] } };
    const rep = (dimensions: string[], metrics: string[], limit = 50, orderBy?: unknown, filter?: unknown) => ({ dateRanges: dr, dimensions: dimensions.map((name) => ({ name })), metrics: metrics.map((name) => ({ name })), limit,
      ...(orderBy ? { orderBys: [orderBy] } : {}), ...((filter || clean) ? { dimensionFilter: filter && clean ? { andGroup: { expressions: [filter, botFilter] } } : (filter || botFilter) } : {}) });
    const byMetric = (m: string) => ({ metric: { metricName: m }, desc: true });
    const call = async (requests: unknown[]) => {
      const r = await fetch("https://analyticsdata.googleapis.com/v1beta/properties/" + prop + ":batchRunReports", { method: "POST", headers: { Authorization: "Bearer " + tk, "Content-Type": "application/json" }, body: JSON.stringify({ requests }) });
      const j = await r.json();
      if (j.error) throw new Error("Analytics Data API: " + (j.error.message || "error"));
      return (j.reports || []).map((rp: any) => (rp.rows || []).map((row: any) => ({ d: (row.dimensionValues || []).map((x: any) => x.value), m: (row.metricValues || []).map((x: any) => +x.value) })));
    };
    if (Array.isArray(custom) && custom.length) {
      const reqs = custom.slice(0, 5).map((c: any) => rep(c.dims || [], c.mets || ["sessions"], Math.min(+c.limit || 50, 500), c.mets && c.mets[0] ? byMetric(c.mets[0]) : undefined, c.filter));
      return json({ property: prop, custom: await call(reqs) });
    }
    const [a, b] = await Promise.all([
      call([rep([], ["activeUsers", "newUsers", "sessions", "engagedSessions", "screenPageViews", "averageSessionDuration", "eventCount"], 1),
            rep(["date"], ["activeUsers", "sessions", "screenPageViews"], 1000, { dimension: { dimensionName: "date" } }),
            rep(["pagePath"], ["screenPageViews", "activeUsers", "userEngagementDuration"], 50, byMetric("screenPageViews")),
            rep(["sessionDefaultChannelGroup", "sessionSource"], ["sessions", "engagedSessions", "activeUsers"], 30, byMetric("sessions")),
            rep(["country"], ["activeUsers", "sessions"], 20, byMetric("activeUsers"))]),
      call([rep(["deviceCategory"], ["activeUsers"], 5, byMetric("activeUsers")),
            rep(["eventName"], ["eventCount"], 25, byMetric("eventCount")),
            rep(["city"], ["activeUsers"], 15, byMetric("activeUsers")),
            rep(["landingPage"], ["sessions", "engagedSessions"], 30, byMetric("sessions"))]),
    ]);
    return json({ property: prop, account: email, clean: !!clean, totals: a[0][0] ? a[0][0].m : null, daily: a[1], pages: a[2], sources: a[3], countries: a[4], devices: b[0], events: b[1], cities: b[2], landing: b[3] });
  } catch (e) { return json({ error: String((e as Error).message || e), account: email }, 500); }
});
