"""
NeolabCare Feedback Webhook
Receives POST from the feedback form, appends a row to Google Sheets,
and proxies the submission to Web3Forms.
"""
import os, json, time, datetime, urllib.request, urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler

SHEET_ID = os.environ.get("SHEET_ID", "1sBoEdScXkdI4mzO422qB1viAqnuemh7XeRJDuOF8ZnA")
SHEET_RANGE = "Responses!A:S"
GOOGLE_SA_KEY = os.environ.get("GOOGLE_SA_KEY", "")   # JSON string of service-account key
WEB3FORMS_KEY = os.environ.get("WEB3FORMS_KEY", "fe35df41-5c1c-4519-9513-f9a227fcffe4")
PORT = int(os.environ.get("PORT", 8080))

# ── Google Sheets auth (service account) ────────────────────────────────────
def _get_access_token():
    """Obtain a short-lived OAuth2 token from a service-account JSON key."""
    import base64, hashlib, hmac
    try:
        key_data = json.loads(GOOGLE_SA_KEY)
    except Exception:
        return None

    # Build JWT
    now = int(time.time())
    header = base64.urlsafe_b64encode(json.dumps({"alg":"RS256","typ":"JWT"}).encode()).rstrip(b"=")
    payload = base64.urlsafe_b64encode(json.dumps({
        "iss": key_data["client_email"],
        "scope": "https://www.googleapis.com/auth/spreadsheets",
        "aud": "https://oauth2.googleapis.com/token",
        "exp": now + 3600,
        "iat": now
    }).encode()).rstrip(b"=")

    # Sign with RSA-SHA256 via cryptography lib (installed in requirements.txt)
    try:
        from cryptography.hazmat.primitives import hashes, serialization
        from cryptography.hazmat.primitives.asymmetric import padding
        private_key = serialization.load_pem_private_key(
            key_data["private_key"].encode(), password=None)
        sig = private_key.sign(header + b"." + payload, padding.PKCS1v15(), hashes.SHA256())
        sig_b64 = base64.urlsafe_b64encode(sig).rstrip(b"=")
    except Exception as e:
        print(f"JWT sign error: {e}")
        return None

    jwt = (header + b"." + payload + b"." + sig_b64).decode()

    # Exchange JWT for access token
    body = urllib.parse.urlencode({
        "grant_type": "urn:ietf:params:oauth:grant-type:jwt-bearer",
        "assertion": jwt
    }).encode()
    req = urllib.request.Request("https://oauth2.googleapis.com/token",
                                  data=body, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            return json.loads(r.read())["access_token"]
    except Exception as e:
        print(f"Token exchange error: {e}")
        return None


def append_to_sheet(data: dict):
    """Append one row of feedback data to the Google Sheet."""
    token = _get_access_token()
    if not token:
        print("No token — skipping sheet append")
        return False

    row = [
        datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC"),
        data.get("name", ""),
        data.get("age", ""),
        data.get("skinType", ""),
        data.get("routine", ""),
        data.get("concern", ""),
        data.get("firstImpression", ""),
        data.get("fineLines", ""),
        data.get("firmness", ""),
        data.get("hydration", ""),
        data.get("smoothness", ""),
        data.get("oilControl", ""),
        data.get("gentle", ""),
        data.get("postShave", ""),
        data.get("noticed", ""),
        data.get("replaceRoutine", ""),
        data.get("overallQuality", ""),
        data.get("testimonial", ""),
        data.get("email", ""),
    ]

    url = (f"https://sheets.googleapis.com/v4/spreadsheets/{SHEET_ID}"
           f"/values/{urllib.parse.quote(SHEET_RANGE)}:append"
           f"?valueInputOption=RAW&insertDataOption=INSERT_ROWS")
    body = json.dumps({"values": [row]}).encode()
    req = urllib.request.Request(url, data=body, method="POST",
                                  headers={"Authorization": f"Bearer {token}",
                                           "Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            print(f"Sheet append OK: {r.status}")
            return True
    except Exception as e:
        print(f"Sheet append error: {e}")
        return False


def forward_to_web3forms(data: dict):
    """Forward submission to Web3Forms so the email notification still fires."""
    payload = {
        "access_key": WEB3FORMS_KEY,
        "subject": "NeolabCare Tester Feedback — " + data.get("name", "Anonymous"),
        "from_name": "NeolabCare Feedback Form",
        "ccemail": "lareesa@neolab.care",
        **data
    }
    body = json.dumps(payload).encode()
    req = urllib.request.Request("https://api.web3forms.com/submit",
                                  data=body, method="POST",
                                  headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            resp = json.loads(r.read())
            print(f"Web3Forms: {resp}")
            return resp.get("success", False)
    except Exception as e:
        print(f"Web3Forms error: {e}")
        return False


# ── HTTP handler ─────────────────────────────────────────────────────────────
class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        print(fmt % args)

    def _cors(self):
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")

    def do_OPTIONS(self):
        self.send_response(204)
        self._cors()
        self.end_headers()

    def do_GET(self):
        if self.path == "/health":
            self.send_response(200)
            self.send_header("Content-Type", "text/plain")
            self.end_headers()
            self.wfile.write(b"ok")
        else:
            self.send_response(404)
            self.end_headers()

    def do_POST(self):
        if self.path != "/submit":
            self.send_response(404)
            self.end_headers()
            return

        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length)
        try:
            data = json.loads(raw)
        except Exception:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'{"success":false,"message":"Invalid JSON"}')
            return

        sheet_ok = append_to_sheet(data)
        w3f_ok   = forward_to_web3forms(data)

        resp = json.dumps({
            "success": True,
            "sheet": sheet_ok,
            "email": w3f_ok
        }).encode()

        self.send_response(200)
        self._cors()
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(resp)))
        self.end_headers()
        self.wfile.write(resp)


if __name__ == "__main__":
    print(f"Starting webhook on port {PORT}")
    HTTPServer(("0.0.0.0", PORT), Handler).serve_forever()
