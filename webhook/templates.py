"""
NeoLabCare Email Templates — World-Class Edition

LOGO RULE (PERMANENT, NON-NEGOTIABLE):
  Always use the actual SVG logo. NEVER use text, spans, or CSS to fake the logo.
  Logo URL: https://www.neolabcare.com/assets/logo-dark.svg  (dark fill, for white bg)
  Logo URL: https://www.neolabcare.com/assets/logo.svg       (white fill, for dark bg)

Design:
  - White background — works universally on iOS Mail, Gmail, Outlook, Apple Mail
  - Real SVG logo via <img> tag — no CDN dependency issues, served from brand domain
  - Fully table-based layout with 100% inline CSS — nothing stripped by email clients
  - Editorial luxury: Aesop / Le Labo aesthetic — generous whitespace, typographic hierarchy
  - Gold accent: #C8A96E — used sparingly
"""

_FONT       = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"
_GOLD       = "#C8A96E"
_BLACK      = "#0A0A0A"
_WHITE      = "#FFFFFF"
_BG         = "#F2EFE9"
_MUTED      = "#888880"
_BORDER     = "#E4E0D8"
_BODY_TEXT  = "#3A3A38"

# The actual brand logo — dark fill SVG served from brand domain
# For white-background emails. Never substitute with text.
LOGO_DARK_URL  = "https://www.neolabcare.com/assets/logo-dark.svg"
LOGO_WHITE_URL = "https://www.neolabcare.com/assets/logo.svg"

_LOGO_IMG = (
    f'<img src="{LOGO_DARK_URL}" alt="NeolabCare" '
    f'width="140" height="auto" border="0" '
    f'style="display:block;width:140px;height:auto;max-width:140px;">'
)


def _shell(body_html: str) -> str:
    """Wraps body in a world-class email shell with white card on warm grey background."""
    return f"""<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="color-scheme" content="light only">
  <meta name="supported-color-schemes" content="light only">
  <!--[if !mso]><!-->
  <style>
    :root {{ color-scheme: light only; supported-color-schemes: light only; }}
    body {{ margin:0!important; padding:0!important; background-color:{_BG}!important; }}
    @media only screen and (max-width:620px) {{
      .card {{ width:100%!important; border-radius:0!important; }}
      .pad {{ padding:32px 24px!important; }}
      .logo-cell {{ padding:28px 24px 24px!important; }}
      .foot {{ padding:20px 24px!important; }}
    }}
  </style>
  <!--<![endif]-->
</head>
<body style="margin:0;padding:0;background-color:{_BG};" bgcolor="{_BG}">
<table width="100%" cellpadding="0" cellspacing="0" border="0"
       style="background-color:{_BG};min-height:100%;" bgcolor="{_BG}">
  <tr>
    <td align="center" valign="top" style="padding:48px 16px;">

      <!-- Card -->
      <table class="card" width="580" cellpadding="0" cellspacing="0" border="0"
             style="background-color:{_WHITE};border-radius:3px;
                    box-shadow:0 2px 12px rgba(0,0,0,0.07);overflow:hidden;"
             bgcolor="{_WHITE}">

        <!-- Logo Header -->
        <tr>
          <td class="logo-cell" align="left" valign="middle"
              style="padding:32px 48px 28px;border-bottom:1px solid {_BORDER};">
            <table width="100%" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td valign="middle">{_LOGO_IMG}</td>
                <td align="right" valign="middle">
                  <span style="font-family:{_FONT};font-size:9px;font-weight:600;
                               letter-spacing:2.5px;text-transform:uppercase;
                               color:{_GOLD};">Creator Partner Program</span>
                </td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- Body -->
        <tr>
          <td class="pad" style="padding:40px 48px;">
            {body_html}
          </td>
        </tr>

        <!-- Footer -->
        <tr>
          <td class="foot"
              style="padding:22px 48px;border-top:1px solid {_BORDER};
                     background-color:#FAFAF8;" bgcolor="#FAFAF8">
            <p style="margin:0;font-family:{_FONT};font-size:10px;font-weight:400;
                       color:#BBBBBB;line-height:1.6;letter-spacing:0.3px;">
              NeolabCare &nbsp;&middot;&nbsp;
              <a href="mailto:hello@neolab.care"
                 style="color:#BBBBBB;text-decoration:none;">hello@neolab.care</a>
              &nbsp;&middot;&nbsp;
              <a href="https://neolabcare.com"
                 style="color:#BBBBBB;text-decoration:none;">neolabcare.com</a>
            </p>
            <p style="margin:5px 0 0;font-family:{_FONT};font-size:9px;font-weight:300;
                       color:#CCCCCC;letter-spacing:0.2px;">
              &copy; 2026 NeolabCare. All rights reserved.
            </p>
          </td>
        </tr>

      </table>
      <!-- /Card -->

    </td>
  </tr>
</table>
</body>
</html>"""


# ── Template 1: Founder Notification ─────────────────────────────────────────
def _founder_notification(name, email, platform, followers, niche, reason, approve_url, **kw):
    body = f"""
    <!-- Label -->
    <p style="margin:0 0 8px;font-family:{_FONT};font-size:9px;font-weight:700;
               letter-spacing:3px;text-transform:uppercase;color:{_GOLD};">
      New Application
    </p>

    <!-- Headline -->
    <h1 style="margin:0 0 28px;font-family:{_FONT};font-size:24px;font-weight:600;
                letter-spacing:-0.02em;color:{_BLACK};line-height:1.25;">
      Creator Partnership Request
    </h1>

    <!-- Applicant Card -->
    <table width="100%" cellpadding="0" cellspacing="0" border="0"
           style="background-color:#FAFAF8;border:1px solid {_BORDER};
                  border-radius:2px;margin-bottom:28px;"
           bgcolor="#FAFAF8">
      <tr><td style="padding:0 24px;">

        <!-- Name -->
        <table width="100%" cellpadding="0" cellspacing="0" border="0">
          <tr><td style="padding:20px 0 16px;border-bottom:1px solid {_BORDER};">
            <p style="margin:0 0 4px;font-family:{_FONT};font-size:9px;font-weight:700;
                       letter-spacing:2.5px;text-transform:uppercase;color:{_MUTED};">Creator Name</p>
            <p style="margin:0;font-family:{_FONT};font-size:16px;font-weight:600;
                       color:{_BLACK};letter-spacing:-0.01em;">{name}</p>
          </td></tr>
          <!-- Email -->
          <tr><td style="padding:16px 0;border-bottom:1px solid {_BORDER};">
            <p style="margin:0 0 4px;font-family:{_FONT};font-size:9px;font-weight:700;
                       letter-spacing:2.5px;text-transform:uppercase;color:{_MUTED};">Email</p>
            <p style="margin:0;font-family:{_FONT};font-size:14px;font-weight:400;color:{_BLACK};">
              <a href="mailto:{email}" style="color:{_BLACK};text-decoration:none;">{email}</a>
            </p>
          </td></tr>
          <!-- Platform -->
          <tr><td style="padding:16px 0;border-bottom:1px solid {_BORDER};">
            <p style="margin:0 0 4px;font-family:{_FONT};font-size:9px;font-weight:700;
                       letter-spacing:2.5px;text-transform:uppercase;color:{_MUTED};">Platform &amp; Reach</p>
            <p style="margin:0;font-family:{_FONT};font-size:14px;font-weight:400;color:{_BLACK};">
              {platform} &mdash; <strong style="font-weight:600;">{followers}</strong> followers
            </p>
          </td></tr>
          <!-- Niche -->
          <tr><td style="padding:16px 0;border-bottom:1px solid {_BORDER};">
            <p style="margin:0 0 4px;font-family:{_FONT};font-size:9px;font-weight:700;
                       letter-spacing:2.5px;text-transform:uppercase;color:{_MUTED};">Niche / Content Type</p>
            <p style="margin:0;font-family:{_FONT};font-size:14px;font-weight:400;color:{_BLACK};">{niche}</p>
          </td></tr>
          <!-- Reason -->
          <tr><td style="padding:16px 0 20px;">
            <p style="margin:0 0 4px;font-family:{_FONT};font-size:9px;font-weight:700;
                       letter-spacing:2.5px;text-transform:uppercase;color:{_MUTED};">Why NeolabCare</p>
            <p style="margin:0;font-family:{_FONT};font-size:14px;font-weight:300;
                       color:{_BODY_TEXT};line-height:1.75;">{reason}</p>
          </td></tr>
        </table>

      </td></tr>
    </table>

    <!-- CTA -->
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom:10px;">
      <tr>
        <td align="center">
          <!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml"
            href="{approve_url}" style="height:52px;v-text-anchor:middle;width:280px;"
            arcsize="4%" fillcolor="#0A0A0A" strokecolor="#0A0A0A">
            <w:anchorlock/>
            <center style="color:#ffffff;font-family:sans-serif;font-size:11px;font-weight:bold;
              letter-spacing:2.5px;text-transform:uppercase;">APPROVE APPLICATION</center>
          </v:roundrect><![endif]-->
          <!--[if !mso]><!-->
          <a href="{approve_url}"
             style="display:inline-block;background-color:{_BLACK};color:{_WHITE};
                    font-family:{_FONT};font-size:11px;font-weight:700;
                    letter-spacing:2.5px;text-transform:uppercase;text-decoration:none;
                    padding:17px 52px;border-radius:2px;min-width:220px;text-align:center;
                    -webkit-text-size-adjust:none;">
            Approve Application
          </a>
          <!--<![endif]-->
        </td>
      </tr>
    </table>
    <p style="margin:0;font-family:{_FONT};font-size:10px;font-weight:300;
               color:{_MUTED};text-align:center;letter-spacing:0.2px;">
      Clicking this link approves the creator and triggers their welcome email.
    </p>
    """
    return _shell(body)


# ── Template 2: Creator — Application Received ───────────────────────────────
def _creator_received(first_name, **kw):
    body = f"""
    <!-- Label -->
    <p style="margin:0 0 8px;font-family:{_FONT};font-size:9px;font-weight:700;
               letter-spacing:3px;text-transform:uppercase;color:{_GOLD};">
      Application Received
    </p>

    <!-- Headline -->
    <h1 style="margin:0 0 8px;font-family:{_FONT};font-size:24px;font-weight:600;
                letter-spacing:-0.02em;color:{_BLACK};line-height:1.25;">
      Hi {first_name}, we've got your application.
    </h1>

    <!-- Gold rule -->
    <div style="width:28px;height:2px;background-color:{_GOLD};margin:16px 0 24px;"></div>

    <p style="margin:0 0 16px;font-family:{_FONT};font-size:15px;font-weight:300;
               color:{_BODY_TEXT};line-height:1.8;">
      Thank you for applying to the NeolabCare Creator Partner Program.
      We've received your application and are reviewing your profile personally.
    </p>
    <p style="margin:0 0 32px;font-family:{_FONT};font-size:15px;font-weight:300;
               color:{_BODY_TEXT};line-height:1.8;">
      If your profile is a strong fit, you'll hear from us within
      <strong style="font-weight:600;color:{_BLACK};">48&ndash;72 hours</strong>.
    </p>

    <!-- What Happens Next -->
    <table width="100%" cellpadding="0" cellspacing="0" border="0"
           style="background-color:#FAFAF8;border:1px solid {_BORDER};
                  border-left:3px solid {_GOLD};border-radius:2px;margin-bottom:32px;"
           bgcolor="#FAFAF8">
      <tr><td style="padding:22px 24px;">
        <p style="margin:0 0 12px;font-family:{_FONT};font-size:9px;font-weight:700;
                   letter-spacing:2.5px;text-transform:uppercase;color:{_GOLD};">
          What Happens Next
        </p>
        <p style="margin:0 0 8px;font-family:{_FONT};font-size:13px;font-weight:300;
                   color:{_BODY_TEXT};line-height:1.7;">
          &rarr;&nbsp; We review applications within
          <strong style="font-weight:600;color:{_BLACK};">48&ndash;72 hours</strong>
        </p>
        <p style="margin:0 0 8px;font-family:{_FONT};font-size:13px;font-weight:300;
                   color:{_BODY_TEXT};line-height:1.7;">
          &rarr;&nbsp; Founding Batch is
          <strong style="font-weight:600;color:{_BLACK};">limited to 50 creators</strong>
        </p>
        <p style="margin:0;font-family:{_FONT};font-size:13px;font-weight:300;
                   color:{_BODY_TEXT};line-height:1.7;">
          &rarr;&nbsp; If approved, you receive your
          <strong style="font-weight:600;color:{_BLACK};">private creator code + 15% commission</strong>
        </p>
      </td></tr>
    </table>

    <p style="margin:0;font-family:{_FONT};font-size:13px;font-weight:300;
               color:{_MUTED};line-height:1.7;">
      Questions? Reply to this email or reach us at
      <a href="mailto:hello@neolab.care"
         style="color:{_BLACK};font-weight:500;text-decoration:none;">hello@neolab.care</a>
    </p>
    """
    return _shell(body)


# ── Template 3: Creator — Approved ───────────────────────────────────────────
def _creator_approved(first_name, discount_code, referral_link, dashboard_url, **kw):
    body = f"""
    <!-- Label -->
    <p style="margin:0 0 8px;font-family:{_FONT};font-size:9px;font-weight:700;
               letter-spacing:3px;text-transform:uppercase;color:{_GOLD};">
      You're Approved
    </p>

    <!-- Headline -->
    <h1 style="margin:0 0 8px;font-family:{_FONT};font-size:24px;font-weight:600;
                letter-spacing:-0.02em;color:{_BLACK};line-height:1.25;">
      Welcome to the Founding Batch.
    </h1>

    <!-- Gold rule -->
    <div style="width:28px;height:2px;background-color:{_GOLD};margin:16px 0 24px;"></div>

    <p style="margin:0 0 28px;font-family:{_FONT};font-size:15px;font-weight:300;
               color:{_BODY_TEXT};line-height:1.8;">
      Hi {first_name}, you've been selected as a NeolabCare Creator Partner.
      Below are your credentials — keep them private, they're unique to you.
    </p>

    <!-- Code Card — dark background -->
    <table width="100%" cellpadding="0" cellspacing="0" border="0"
           style="background-color:{_BLACK};border-radius:2px;margin-bottom:4px;"
           bgcolor="{_BLACK}">
      <tr><td style="padding:28px 32px 24px;">
        <p style="margin:0 0 6px;font-family:{_FONT};font-size:9px;font-weight:700;
                   letter-spacing:3px;text-transform:uppercase;color:{_GOLD};">
          Your Creator Code
        </p>
        <p style="margin:0 0 16px;font-family:{_FONT};font-size:38px;font-weight:700;
                   letter-spacing:0.1em;color:{_WHITE};line-height:1;">
          {discount_code}
        </p>
        <p style="margin:0;font-family:{_FONT};font-size:13px;font-weight:300;
                   color:rgba(245,245,240,0.6);line-height:1.7;">
          Share this code with your audience. They get
          <strong style="color:{_WHITE};font-weight:600;">50% off</strong>
          the Founding Price &nbsp;&middot;&nbsp;
          You earn <strong style="color:{_GOLD};font-weight:600;">15% commission</strong>
          on every confirmed order.
        </p>
      </td></tr>
    </table>

    <!-- Referral Link -->
    <table width="100%" cellpadding="0" cellspacing="0" border="0"
           style="background-color:#FAFAF8;border:1px solid {_BORDER};
                  border-top:none;border-radius:0 0 2px 2px;margin-bottom:28px;"
           bgcolor="#FAFAF8">
      <tr><td style="padding:16px 24px;">
        <p style="margin:0 0 4px;font-family:{_FONT};font-size:9px;font-weight:700;
                   letter-spacing:2.5px;text-transform:uppercase;color:{_MUTED};">
          Your Referral Link
        </p>
        <a href="{referral_link}"
           style="font-family:{_FONT};font-size:13px;font-weight:400;color:{_BLACK};
                  word-break:break-all;text-decoration:underline;
                  text-decoration-color:{_GOLD};">
          {referral_link}
        </a>
      </td></tr>
    </table>

    <!-- Dashboard CTA -->
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom:10px;">
      <tr>
        <td align="center">
          <!--[if mso]><v:roundrect xmlns:v="urn:schemas-microsoft-com:vml"
            href="{dashboard_url}" style="height:52px;v-text-anchor:middle;width:280px;"
            arcsize="4%" fillcolor="#0A0A0A" strokecolor="#0A0A0A">
            <w:anchorlock/>
            <center style="color:#ffffff;font-family:sans-serif;font-size:11px;font-weight:bold;
              letter-spacing:2.5px;text-transform:uppercase;">VIEW YOUR DASHBOARD</center>
          </v:roundrect><![endif]-->
          <!--[if !mso]><!-->
          <a href="{dashboard_url}"
             style="display:inline-block;background-color:{_BLACK};color:{_WHITE};
                    font-family:{_FONT};font-size:11px;font-weight:700;
                    letter-spacing:2.5px;text-transform:uppercase;text-decoration:none;
                    padding:17px 52px;border-radius:2px;min-width:220px;text-align:center;
                    -webkit-text-size-adjust:none;">
            View Your Dashboard
          </a>
          <!--<![endif]-->
        </td>
      </tr>
    </table>
    <p style="margin:0 0 32px;font-family:{_FONT};font-size:10px;font-weight:300;
               color:{_MUTED};text-align:center;letter-spacing:0.2px;">
      Live stats: orders, revenue, confirmed and pending commission.
    </p>

    <!-- How it works -->
    <table width="100%" cellpadding="0" cellspacing="0" border="0"
           style="border-top:1px solid {_BORDER};">
      <tr><td style="padding-top:24px;">
        <p style="margin:0 0 12px;font-family:{_FONT};font-size:9px;font-weight:700;
                   letter-spacing:2.5px;text-transform:uppercase;color:{_GOLD};">
          How It Works
        </p>
        <p style="margin:0 0 7px;font-family:{_FONT};font-size:13px;font-weight:300;
                   color:{_BODY_TEXT};line-height:1.7;">
          &rarr;&nbsp; Share your link or code with your audience
        </p>
        <p style="margin:0 0 7px;font-family:{_FONT};font-size:13px;font-weight:300;
                   color:{_BODY_TEXT};line-height:1.7;">
          &rarr;&nbsp; They get 50% off the Founding Price
        </p>
        <p style="margin:0 0 7px;font-family:{_FONT};font-size:13px;font-weight:300;
                   color:{_BODY_TEXT};line-height:1.7;">
          &rarr;&nbsp; You earn 15% on every confirmed order
        </p>
        <p style="margin:0;font-family:{_FONT};font-size:13px;font-weight:300;
                   color:{_BODY_TEXT};line-height:1.7;">
          &rarr;&nbsp; Monthly payouts to your nominated account
        </p>
      </td></tr>
    </table>
    """
    return _shell(body)


# ── Public API ────────────────────────────────────────────────────────────────
def render(template_name: str, context: dict) -> str:
    if template_name == "founder_notification":
        return _founder_notification(**context)
    elif template_name == "creator_received":
        return _creator_received(**context)
    elif template_name == "creator_approved":
        return _creator_approved(**context)
    raise ValueError(f"Unknown template: {template_name}")


# ── Legacy shim — server.py uses _render_template(templates.XYZ_HTML, ctx) ───
class _T:
    def __init__(self, name): self.name = name
    def __str__(self): return f"__TEMPLATE__{self.name}__"

FOUNDER_NOTIFICATION_HTML = _T("founder_notification")
CREATOR_RECEIVED_HTML     = _T("creator_received")
CREATOR_APPROVED_HTML     = _T("creator_approved")
