"""
NeolabCare Webhook Server

Routes:
  GET  /health                 health check
  POST /submit                 tester feedback → Google Sheets + Web3Forms
  POST /creator-application    creator partner form → Creators sheet + emails
  GET  /approve-creator?token= founder approval link → sheet update + emails
  POST /shopify-order          Shopify order webhook → Commissions sheet
  GET  /creator-stats?code=    dashboard data endpoint (JSON)
"""
import os, json, time, datetime, hmac, hashlib, urllib.request, urllib.parse
_utcnow = lambda: datetime.datetime.now(datetime.timezone.utc)
from http.server import HTTPServer, BaseHTTPRequestHandler

# ── Config ────────────────────────────────────────────────────────────────────
SHEET_ID             = os.environ.get("SHEET_ID", "1sBoEdScXkdI4mzO422qB1viAqnuemh7XeRJDuOF8ZnA")
GOOGLE_SA_KEY        = os.environ.get("GOOGLE_SA_KEY", "")
APPROVAL_SECRET      = os.environ.get("APPROVAL_SECRET", "change-me-in-render")
WEBHOOK_BASE_URL     = os.environ.get("WEBHOOK_BASE_URL", "https://neolabcare-webhook.onrender.com")
FOUNDER_EMAIL        = os.environ.get("FOUNDER_EMAIL", "lareesa@neolab.care")
GMAIL_USER           = "neolabcare@gmail.com"
GMAIL_APP_PASSWORD   = "nnbvkgtomsmdutpm" # Hardcoded to bypass Render env var bug
SHOPIFY_STORE        = os.environ.get("SHOPIFY_STORE", "")        # e.g. neolab-care.myshopify.com
SHOPIFY_ADMIN_TOKEN  = os.environ.get("SHOPIFY_ADMIN_TOKEN", "")  # shpat_... — set in Render dashboard
SHOPIFY_WEBHOOK_SECRET = os.environ.get("SHOPIFY_WEBHOOK_SECRET", "")
PORT                 = int(os.environ.get("PORT", 8080))
COMMISSION_RATE      = 0.15

# Load templates
try:
    import templates
except ImportError:
    class templates:
        FOUNDER_NOTIFICATION_HTML = "Name: {{name}}<br>Email: {{email}}<br><a href='{{approve_url}}'>Approve</a>"
        CREATOR_RECEIVED_HTML = "Hi {{first_name}}, application received."
        CREATOR_APPROVED_HTML = "Hi, you're approved. Code: {{discount_code}}"

# Sheet ranges
RESPONSES_RANGE   = "Responses!A:U"
CREATORS_RANGE    = "Creators!A:R"
COMMISSIONS_RANGE = "Commissions!A:G"


# ── Google Sheets auth (service account JWT) ──────────────────────────────────
def _get_access_token():
    """Obtain a short-lived OAuth2 token from a service-account JSON key."""
    import base64
    try:
        key_data = json.loads(GOOGLE_SA_KEY)
    except Exception:
        return None

    now = int(time.time())
    header  = base64.urlsafe_b64encode(json.dumps({"alg": "RS256", "typ": "JWT"}).encode()).rstrip(b"=")
    payload = base64.urlsafe_b64encode(json.dumps({
        "iss":   key_data["client_email"],
        "scope": "https://www.googleapis.com/auth/spreadsheets",
        "aud":   "https://oauth2.googleapis.com/token",
        "exp":   now + 3600,
        "iat":   now,
    }).encode()).rstrip(b"=")

    try:
        from cryptography.hazmat.primitives import hashes, serialization
        from cryptography.hazmat.primitives.asymmetric import padding
        private_key = serialization.load_pem_private_key(key_data["private_key"].encode(), password=None)
        sig = private_key.sign(header + b"." + payload, padding.PKCS1v15(), hashes.SHA256())
        sig_b64 = base64.urlsafe_b64encode(sig).rstrip(b"=")
    except Exception as e:
        print(f"JWT sign error: {e}")
        return None

    jwt_token = (header + b"." + payload + b"." + sig_b64).decode()
    body = urllib.parse.urlencode({
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "assertion": jwt_token,
    }).encode()
    req = urllib.request.Request("https://oauth2.googleapis.com/token", data=body, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            return json.loads(r.read())["access_token"]
    except Exception as e:
        print(f"Token exchange error: {e}")
        return None


# ── Google Sheets helpers ─────────────────────────────────────────────────────
def _sheet_append(range_name: str, row: list) -> bool:
    token = _get_access_token()
    if not token:
        print("No token — skipping sheet append")
        return False
    url = (f"https://sheets.googleapis.com/v4/spreadsheets/{SHEET_ID}"
           f"/values/{urllib.parse.quote(range_name)}:append"
           f"?valueInputOption=RAW&insertDataOption=INSERT_ROWS")
    body = json.dumps({"values": [row]}).encode()
    req = urllib.request.Request(url, data=body, method="POST",
                                  headers={"Authorization": f"Bearer {token}",
                                           "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            print(f"Sheet append OK ({range_name}): {r.status}")
            return True
    except Exception as e:
        print(f"Sheet append error ({range_name}): {e}")
        return False


def _sheet_read(range_name: str) -> list:
    token = _get_access_token()
    if not token:
        return []
    url = (f"https://sheets.googleapis.com/v4/spreadsheets/{SHEET_ID}"
           f"/values/{urllib.parse.quote(range_name)}")
    req = urllib.request.Request(url, headers={"Authorization": f"Bearer {token}"})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            return json.loads(r.read()).get("values", [])
    except Exception as e:
        print(f"Sheet read error ({range_name}): {e}")
        return []


def _sheet_update(range_name: str, values: list) -> bool:
    token = _get_access_token()
    if not token:
        return False
    url = (f"https://sheets.googleapis.com/v4/spreadsheets/{SHEET_ID}"
           f"/values/{urllib.parse.quote(range_name)}?valueInputOption=RAW")
    body = json.dumps({"values": values}).encode()
    req = urllib.request.Request(url, data=body, method="PUT",
                                  headers={"Authorization": f"Bearer {token}",
                                           "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            print(f"Sheet update OK ({range_name}): {r.status}")
            return True
    except Exception as e:
        print(f"Sheet update error ({range_name}): {e}")
        return False


# ── Email (Gmail SMTP) ──────────────────────────────────────────────────────────
CC_EMAIL = "lareesahu@gmail.com"  # Always CC this address on every email

def _send_email(subject: str, recipient_email: str, html_content: str) -> bool:
    """Send professional HTML emails via Gmail SMTP, always CC lareesahu@gmail.com."""
    import smtplib
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    if not GMAIL_APP_PASSWORD:
        print("[EMAIL] GMAIL_APP_PASSWORD not set. Cannot send email.")
        return False

    msg = MIMEMultipart("alternative")
    msg["Subject"] = subject
    msg["From"] = f"NeoLabCare <{GMAIL_USER}>"
    msg["To"] = recipient_email
    msg["Cc"] = CC_EMAIL

    msg.attach(MIMEText(html_content, "html"))

    recipients = list({recipient_email, CC_EMAIL})  # deduplicate in case they're the same
    try:
        # Debugging: log the connection attempt
        print(f"[EMAIL] Connecting to smtp.gmail.com:587 for {recipient_email}...")
        
        server = smtplib.SMTP("smtp.gmail.com", 587, timeout=20)
        server.set_debuglevel(1) # Enable verbose SMTP logging in Render console
        server.starttls()
        server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
        server.sendmail(GMAIL_USER, recipients, msg.as_string())
        server.quit()
        
        print(f"[EMAIL] SUCCESS: '{subject}' to {recipient_email}")
        return True
    except Exception as e:
        print(f"[EMAIL] FAILED: {type(e).__name__}: {e}")
        return False


def _render_template(template: str, context: dict) -> str:
    """Simple string replacement for templates (replaces {{key}} with value)."""
    res = template
    for k, v in context.items():
        res = res.replace("{{" + k + "}}", str(v))
    return res


# ── Token + code helpers ──────────────────────────────────────────────────────
def _make_token(email: str, ts: str) -> str:
    msg = f"{email}:{ts}".encode()
    return hmac.new(APPROVAL_SECRET.encode(), msg, hashlib.sha256).hexdigest()


def _derive_code(name: str) -> str:
    first = name.strip().split()[0] if name.strip() else "CREATOR"
    return first.upper()[:8] + "99"


# ── Approval page HTML ────────────────────────────────────────────────────────
def _html_page(title: str, message: str, error: bool = False) -> str:
    accent = "#cc4444" if error else "#C8B89A"
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} | NeoLabCare</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500&display=swap" rel="stylesheet">
<style>
:root{{--bg:#0A0A0A;--layer:#141414;--text:rgba(245,245,240,.94);--muted:rgba(245,245,240,.52);--border:rgba(200,184,154,.18);}}
*{{box-sizing:border-box;margin:0;padding:0;}}
body{{background:var(--bg);color:var(--text);font-family:Poppins,sans-serif;min-height:100vh;display:flex;align-items:center;justify-content:center;padding:40px 20px;-webkit-font-smoothing:antialiased;}}
.card{{background:var(--layer);border:1px solid var(--border);border-radius:2px;padding:52px 48px;max-width:500px;width:100%;text-align:center;}}
.lbl{{font-size:10px;letter-spacing:3px;text-transform:uppercase;color:{accent};display:block;margin-bottom:24px;}}
h1{{font-size:1.35rem;font-weight:500;margin-bottom:14px;}}
p{{font-size:0.85rem;color:var(--muted);line-height:1.75;}}
strong{{color:var(--text);}}
</style>
</head>
<body><div class="card">
<span class="lbl">NeoLabCare Creator Partner Program</span>
<h1>{title}</h1>
<p>{message}</p>
</div></body></html>"""


# ── Legacy: tester feedback sheet append ─────────────────────────────────────
def append_to_sheet(data: dict) -> bool:
    row = [
        _utcnow().strftime("%Y-%m-%d %H:%M UTC"),
        data.get("name", ""), data.get("age", ""), data.get("gender", ""),
        data.get("skinType", ""), data.get("routine", ""), data.get("concern", ""),
        data.get("firstImpression", ""), data.get("fineLines", ""), data.get("firmness", ""),
        data.get("hydration", ""), data.get("smoothness", ""), data.get("oilControl", ""),
        data.get("gentle", ""), data.get("postShave", ""), data.get("noticed", ""),
        data.get("replaceRoutine", ""), data.get("overallQuality", ""),
        data.get("testimonial", ""), data.get("interview", ""), data.get("email", ""),
    ]
    return _sheet_append(RESPONSES_RANGE, row)


# ── HTTP handler ──────────────────────────────────────────────────────────────
class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        print(fmt % args)

    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, X-Shopify-Hmac-Sha256")

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def _json(self, status: int, data: dict):
        resp = json.dumps(data).encode()
        self.send_response(status)
        self._cors()
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(resp)))
        self.end_headers()
        self.wfile.write(resp)

    def _html(self, status: int, html: str):
        resp = html.encode()
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(resp)))
        self.end_headers()
        self.wfile.write(resp)

    # ── GET ───────────────────────────────────────────────────────────────────
    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        path   = parsed.path
        params = {k: v[0] for k, v in urllib.parse.parse_qs(parsed.query).items()}

        if path == "/health":
            self.send_response(200)
            self._cors()
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"ok")

        elif path == "/approve-creator":
            self._handle_approve_creator(params.get("token", ""))

        elif path == "/creator-stats":
            self._handle_creator_stats(params.get("code", ""))

        elif path == "/test-email":
            import urllib.request as _ur
            payload = {"access_key": WEB3FORMS_KEY, "subject": "NeoLabCare test",
                       "from_name": "NeoLabCare", "email": FOUNDER_EMAIL,
                       "message": "Test from webhook server."}
            _req = _ur.Request("https://api.web3forms.com/submit",
                               data=urllib.parse.urlencode(payload).encode(), method="POST",
                               headers={"Content-Type": "application/x-www-form-urlencoded",
                                        "Origin": "https://neolab.care",
                                        "Referer": "https://neolab.care/",
                                        "User-Agent": "Mozilla/5.0"})
            try:
                with _ur.urlopen(_req, timeout=15) as _r:
                    _resp = json.loads(_r.read())
                self._json(200, {"email_success": _resp.get("success"), "w3f_response": _resp})
            except Exception as _e:
                self._json(200, {"email_success": False, "error": str(_e)})

        elif path == "/test-sheet":
            rows = _sheet_read(CREATORS_RANGE)
            self._json(200, {
                "sheet_reachable": True,
                "creators_count": len(rows),
                "google_sa_key_set": bool(GOOGLE_SA_KEY),
            })

        else:
            self.send_response(404)
            self.end_headers()

    # ── POST ──────────────────────────────────────────────────────────────────
    def do_POST(self):
        path   = urllib.parse.urlparse(self.path).path
        length = int(self.headers.get("Content-Length", 0))
        raw    = self.rfile.read(length)

        try:
            data = json.loads(raw)
        except Exception:
            self._json(400, {"success": False, "message": "Invalid JSON"})
            return

        if path == "/submit":
            sheet_ok = append_to_sheet(data)
            w3f_ok   = forward_to_web3forms(data)
            self._json(200, {"success": sheet_ok or w3f_ok, "sheet": sheet_ok, "email": w3f_ok})

        elif path == "/creator-application":
            self._handle_creator_application(data)

        elif path == "/shopify-order":
            self._handle_shopify_order(raw, data)

        else:
            self._json(404, {"error": "Not found"})

    # ── Route: POST /creator-application ─────────────────────────────────────
    def _handle_creator_application(self, data: dict):
        name  = data.get("full_name", "").strip()
        email = data.get("email", "").strip()
        if not name or not email:
            self._json(400, {"success": False, "message": "Name and email are required"})
            return

        ts            = _utcnow().strftime("%Y-%m-%d %H:%M UTC")
        discount_code = _derive_code(name)
        token         = _make_token(email, ts)
        approve_url   = f"{WEBHOOK_BASE_URL}/approve-creator?token={token}"

        # Creators sheet row (columns A–R)
        row = [
            ts, name, email,
            data.get("country", ""),
            data.get("platform", ""),
            data.get("profile_url", ""),
            data.get("audience_size", ""),
            data.get("niche", ""),
            data.get("avg_views", ""),
            data.get("audience_countries", ""),
            data.get("prior_promotions", ""),
            data.get("fit_reason", ""),
            data.get("payout_method", ""),
            data.get("payout_email", ""),
            data.get("shipping_address", ""),
            "Pending",        # col P — Status
            discount_code,    # col Q — DiscountCode
            token,            # col R — ApprovalToken
        ]
        _sheet_append(CREATORS_RANGE, row)

        # ── Email notifications (Gmail Server-side) ──────────────────────────
        # 1. Notify Founder
        founder_html = _render_template(templates.FOUNDER_NOTIFICATION_HTML, {
            "name": name, "email": email, 
            "platform": data.get("platform", ""), 
            "audience_size": data.get("audience_size", ""), 
            "niche": data.get("niche", ""), 
            "fit_reason": data.get("fit_reason", ""), 
            "approve_url": approve_url
        })
        s1 = _send_email(f"New Creator Application — {name}", FOUNDER_EMAIL, founder_html)
        
        # 2. Notify Creator
        creator_html = _render_template(templates.CREATOR_RECEIVED_HTML, {
            "first_name": name.split()[0] if name.strip() else "there"
        })
        s2 = _send_email("Application Received — NeoLabCare", email, creator_html)

        # Return status
        self._json(200, {"success": True, "emails_sent": s1 and s2, "debug": {"founder": s1, "creator": s2}})

    # ── Route: GET /approve-creator ───────────────────────────────────────────
    def _handle_approve_creator(self, token: str):
        if not token:
            self._html(400, _html_page("Missing Token", "No approval token was provided.", error=True))
            return

        rows = _sheet_read(CREATORS_RANGE)
        target_idx = None
        creator    = None

        for i, row in enumerate(rows):
            while len(row) < 18:
                row.append("")
            if row[17] == token:          # col R = ApprovalToken
                target_idx = i
                creator    = row
                break

        if target_idx is None:
            self._html(404, _html_page(
                "Link Not Found",
                "This approval link is invalid or has already been used. "
                "Check the Creators sheet in Google Sheets to verify the creator's status.",
                error=True,
            ))
            return

        name          = creator[1]
        email         = creator[2]
        discount_code = creator[16]   # col Q
        status        = creator[15]   # col P

        if status == "Approved":
            self._html(200, _html_page(
                "Already Approved",
                f"{name} ({email}) is already an approved creator partner "
                f"with code <strong>{discount_code}</strong>.",
            ))
            return

        # Update Status → Approved in the sheet
        sheet_row = target_idx + 1   # Sheets is 1-indexed
        _sheet_update(f"Creators!P{sheet_row}", [["Approved"]])

        ref_slug       = discount_code[:-2].lower()   # SARAH99 → sarah
        referral_link  = f"https://neolab.care/?ref={ref_slug}"
        dashboard_link = f"https://neolab.care/partner-dashboard.html?code={discount_code}"

        # ── Shopify discount code creation ────────────────────────────────────
        if SHOPIFY_ADMIN_TOKEN and SHOPIFY_STORE:
            try:
                # Step 1: Create Price Rule
                price_rule_payload = {
                    "price_rule": {
                        "title": f"Creator Code: {discount_code}",
                        "target_type": "line_item",
                        "target_selection": "all",
                        "allocation_method": "across",
                        "value_type": "percentage",
                        "value": "-50.0",
                        "customer_selection": "all",
                        "starts_at": _utcnow().isoformat(),
                        "usage_limit": None
                    }
                }
                pr_req = urllib.request.Request(
                    f"https://{SHOPIFY_STORE}/admin/api/2024-01/price_rules.json",
                    data=json.dumps(price_rule_payload).encode(),
                    method="POST",
                    headers={
                        "X-Shopify-Access-Token": SHOPIFY_ADMIN_TOKEN,
                        "Content-Type": "application/json"
                    }
                )
                with urllib.request.urlopen(pr_req, timeout=15) as pr_res:
                    pr_data = json.loads(pr_res.read())
                    price_rule_id = pr_data["price_rule"]["id"]
                
                # Step 2: Create Discount Code
                discount_payload = {
                    "discount_code": {
                        "code": discount_code
                    }
                }
                dc_req = urllib.request.Request(
                    f"https://{SHOPIFY_STORE}/admin/api/2024-01/price_rules/{price_rule_id}/discount_codes.json",
                    data=json.dumps(discount_payload).encode(),
                    method="POST",
                    headers={
                        "X-Shopify-Access-Token": SHOPIFY_ADMIN_TOKEN,
                        "Content-Type": "application/json"
                    }
                )
                with urllib.request.urlopen(dc_req, timeout=15) as dc_res:
                    print(f"[SHOPIFY] Auto-created discount code '{discount_code}' (ID: {price_rule_id})")
            except Exception as e:
                print(f"[SHOPIFY] Error auto-creating code '{discount_code}': {e}")
        else:
            print(f"[SHOPIFY] No token — create code '{discount_code}' manually in Shopify Admin "
                  f"(50% off all products, unlimited uses, no expiry)")

        # Build email bodies — browser will fire these via Web3Forms (avoids server 403)
        creator_msg = json.dumps(
            f"Hi {name},\n\n"
            f"You're in. Welcome to the NeoLabCare Creator Partner Program.\n\n"
            f"Your creator code:  {discount_code}\n"
            f"Your referral link: {referral_link}\n\n"
            f"Share your link with your audience. When they use code {discount_code} "
            f"at checkout, they save 50% on their first bottle. "
            f"You earn 15% commission on every confirmed sale.\n\n"
            f"Track your stats:\n{dashboard_link}\n\n"
            f"Commission clears 7 days after the customer receives their order "
            f"(no refund or dispute). Payouts sent monthly.\n\n"
            f"Questions? Reply to this email.\n\n— NeoLabCare"
        )
          # Send Approval Email to Creator via Gmail (Server-side)
        creator_approved_html = _render_template(templates.CREATOR_APPROVED_HTML, {
            "discount_code": discount_code,
            "referral_link": referral_link,
            "dashboard_url": dashboard_link
        })
        _send_email("You're Approved — NeoLabCare Creator Partner Program", email, creator_approved_html)

        shopify_note = (
            f" Please create discount code <strong>{discount_code}</strong> in Shopify Admin."
        ) if not (SHOPIFY_ADMIN_TOKEN and SHOPIFY_STORE) else ""

        page_html = _html_page(
            "Creator Approved",
            f"{name} has been approved and emailed their creator code, "
            f"referral link, and dashboard.{shopify_note}",
        )
        self._html(200, page_html)

    # ── Route: POST /shopify-order ────────────────────────────────────────────
    def _handle_shopify_order(self, raw: bytes, data: dict):
        import base64
        if SHOPIFY_WEBHOOK_SECRET:
            sig      = self.headers.get("X-Shopify-Hmac-Sha256", "")
            computed = base64.b64encode(
                hmac.new(SHOPIFY_WEBHOOK_SECRET.encode(), raw, hashlib.sha256).digest()
            ).decode()
            if sig != computed:
                self._json(401, {"error": "Invalid webhook signature"})
                return

        discount_codes = data.get("discount_codes", [])
        if not discount_codes:
            self._json(200, {"success": True, "message": "No discount code — skipped"})
            return

        order_code = discount_codes[0].get("code", "").upper()
        rows       = _sheet_read(CREATORS_RANGE)
        creator_email = ""
        for row in rows:
            while len(row) < 18:
                row.append("")
            if row[16].upper() == order_code:
                creator_email = row[2]
                break

        if not creator_email:
            print(f"[ORDER] No creator matched for code {order_code}")
            self._json(200, {"success": True, "message": "Code not matched to a creator"})
            return

        order_id    = str(data.get("id", ""))
        order_total = float(data.get("total_price", 0))
        commission  = round(order_total * COMMISSION_RATE, 2)
        ts          = _utcnow().strftime("%Y-%m-%d %H:%M UTC")

        _sheet_append(COMMISSIONS_RANGE, [
            ts, order_id, order_code, creator_email,
            order_total, commission, "pending",
        ])
        print(f"[ORDER] Logged commission ${commission} for {order_code} ({creator_email})")
        self._json(200, {"success": True})

    # ── Route: GET /creator-stats ─────────────────────────────────────────────
    def _handle_creator_stats(self, code: str):
        if not code:
            self._json(400, {"error": "No code provided", "found": False})
            return

        code  = code.upper()
        rows  = _sheet_read(CREATORS_RANGE)
        creator = None

        for row in rows:
            while len(row) < 18:
                row.append("")
            if row[16].upper() == code:
                creator = row
                break

        if not creator:
            self._json(404, {"error": "Creator not found", "found": False})
            return

        name     = creator[1]
        status   = creator[15]
        ref_slug = code[:-2].lower()   # SARAH99 → sarah

        comm_rows          = _sheet_read(COMMISSIONS_RANGE)
        orders             = []
        total_revenue      = 0.0
        confirmed_comm     = 0.0
        pending_comm       = 0.0
        now                = _utcnow()

        for row in comm_rows:
            while len(row) < 7:
                row.append("")
            if row[2].upper() != code:
                continue
            try:
                amt  = float(row[4])
                comm = float(row[5])
            except (ValueError, IndexError):
                continue

            # Treat orders older than 14 days as confirmed (proxy: dispatch + delivery + 7-day window)
            try:
                order_date  = datetime.datetime.strptime(row[0], "%Y-%m-%d %H:%M UTC")
                effective_status = "confirmed" if (now - order_date).days >= 14 else "pending"
            except Exception:
                effective_status = row[6] if row[6] else "pending"

            total_revenue += amt
            if effective_status == "confirmed":
                confirmed_comm += comm
            else:
                pending_comm += comm

            orders.append({
                "date":      row[0],
                "order_id":  row[1],
                "amount":    amt,
                "commission": comm,
                "status":    effective_status,
            })

        self._json(200, {
            "found":               True,
            "name":                name,
            "code":                code,
            "referral_link":       f"https://neolab.care/?ref={ref_slug}",
            "dashboard_link":      f"https://neolab.care/partner-dashboard.html?code={code}",
            "status":              status,
            "total_orders":        len(orders),
            "total_revenue":       round(total_revenue, 2),
            "confirmed_commission": round(confirmed_comm, 2),
            "pending_commission":  round(pending_comm, 2),
            "orders":              sorted(orders, key=lambda x: x["date"], reverse=True)[:20],
        })


if __name__ == "__main__":
    print(f"Starting NeolabCare webhook on port {PORT}")
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
