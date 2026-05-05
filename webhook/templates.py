"""
NeoLabCare Email Templates — World-Class Edition
Caelum Standard · NeolabCare Brand System · Native Dark/Light Mode

LOGO RULE (PERMANENT, NON-NEGOTIABLE):
  NEVER use text, spans, or CSS to simulate the NeolabCare logo.
  Always use the actual SVG files:
    Light mode: https://www.neolabcare.com/assets/logo-dark.svg  (dark fill on white bg)
    Dark mode:  https://www.neolabcare.com/assets/logo.svg       (white fill on dark bg)

Dark/Light Mode Implementation:
  - Uses @media (prefers-color-scheme: dark) in <style> block
  - Uses .logo-light / .logo-dark classes to swap logo variants
  - Uses data-ogsc for Outlook dark mode compatibility
  - Default (light) is fully functional without CSS support
"""

_FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"

# Brand tokens
_GOLD        = "#C8A96E"
_BLACK       = "#0A0A0A"
_WHITE       = "#FFFFFF"
_VOID_BG     = "#0A0A0A"
_VOID_CARD   = "#111111"
_VOID_BORDER = "#1E1E1E"
_VOID_TEXT   = "rgba(245,245,240,0.94)"
_VOID_MUTED  = "rgba(245,245,240,0.52)"
_LIGHT_BG    = "#F2EFE9"
_LIGHT_CARD  = "#FFFFFF"
_LIGHT_BORDER= "#E4E0D8"
_LIGHT_TEXT  = "#0A0A0A"
_LIGHT_MUTED = "#888880"
_LIGHT_BODY  = "#3A3A38"

LOGO_LIGHT_URL = "https://www.neolabcare.com/assets/logo-dark.svg"   # dark ink, for white bg
LOGO_DARK_URL  = "https://www.neolabcare.com/assets/logo.svg"         # white ink, for dark bg


def _shell(body_html: str) -> str:
    """
    World-class email shell with native OS dark/light mode switching.
    Technique: @media prefers-color-scheme + dual logo + CSS class overrides.
    Compatible with: Apple Mail, iOS Mail, Gmail (web), Outlook (partial), Samsung Mail.
    """
    return f"""<!DOCTYPE html>
<html lang="en" xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="x-apple-disable-message-reformatting">
  <!--[if !mso]><!-->
  <meta name="color-scheme" content="light dark">
  <meta name="supported-color-schemes" content="light dark">
  <!--<![endif]-->
  <title>NeolabCare</title>
  <style>
    /* ── Reset ── */
    * {{ box-sizing: border-box; }}
    body, table, td, a {{ -webkit-text-size-adjust: 100%; -ms-text-size-adjust: 100%; }}
    table, td {{ mso-table-lspace: 0pt; mso-table-rspace: 0pt; }}
    img {{ -ms-interpolation-mode: bicubic; border: 0; display: block; }}
    body {{ margin: 0 !important; padding: 0 !important; }}

    /* ── Light mode defaults (also fallback) ── */
    body, .email-bg {{ background-color: {_LIGHT_BG} !important; }}
    .email-card {{ background-color: {_LIGHT_CARD} !important; }}
    .email-header {{ border-bottom: 1px solid {_LIGHT_BORDER} !important; }}
    .email-footer {{ background-color: #FAFAF8 !important; border-top: 1px solid {_LIGHT_BORDER} !important; }}
    .email-divider {{ background-color: {_LIGHT_BORDER} !important; }}
    .text-primary {{ color: {_LIGHT_TEXT} !important; }}
    .text-body {{ color: {_LIGHT_BODY} !important; }}
    .text-muted {{ color: {_LIGHT_MUTED} !important; }}
    .text-gold {{ color: {_GOLD} !important; }}
    .text-footer {{ color: #AAAAAA !important; }}
    .info-card {{ background-color: #FAFAF8 !important; border: 1px solid {_LIGHT_BORDER} !important; }}
    .info-card-accent {{ border-left: 3px solid {_GOLD} !important; }}
    .field-divider {{ background-color: {_LIGHT_BORDER} !important; }}
    .code-card {{ background-color: {_BLACK} !important; }}
    .code-text {{ color: {_WHITE} !important; }}
    .code-sub {{ color: rgba(245,245,240,0.6) !important; }}
    .ref-card {{ background-color: #FAFAF8 !important; border: 1px solid {_LIGHT_BORDER} !important; }}
    .cta-btn {{ background-color: {_BLACK} !important; color: {_WHITE} !important; }}
    .logo-light {{ display: block !important; }}
    .logo-dark  {{ display: none  !important; }}

    /* ── Dark mode overrides ── */
    @media (prefers-color-scheme: dark) {{
      body, .email-bg {{ background-color: {_VOID_BG} !important; }}
      .email-card {{ background-color: {_VOID_CARD} !important; }}
      .email-header {{ border-bottom: 1px solid {_VOID_BORDER} !important; }}
      .email-footer {{ background-color: #0D0D0D !important; border-top: 1px solid {_VOID_BORDER} !important; }}
      .email-divider {{ background-color: {_VOID_BORDER} !important; }}
      .text-primary {{ color: {_VOID_TEXT} !important; }}
      .text-body {{ color: {_VOID_MUTED} !important; }}
      .text-muted {{ color: rgba(245,245,240,0.36) !important; }}
      .text-gold {{ color: {_GOLD} !important; }}
      .text-footer {{ color: rgba(245,245,240,0.28) !important; }}
      .info-card {{ background-color: #161616 !important; border: 1px solid {_VOID_BORDER} !important; }}
      .info-card-accent {{ border-left: 3px solid {_GOLD} !important; }}
      .field-divider {{ background-color: {_VOID_BORDER} !important; }}
      .code-card {{ background-color: #161616 !important; border: 1px solid {_GOLD} !important; }}
      .code-text {{ color: {_VOID_TEXT} !important; }}
      .code-sub {{ color: {_VOID_MUTED} !important; }}
      .ref-card {{ background-color: #161616 !important; border: 1px solid {_VOID_BORDER} !important; }}
      .cta-btn {{ background-color: {_VOID_TEXT} !important; color: {_BLACK} !important; }}
      .logo-light {{ display: none  !important; }}
      .logo-dark  {{ display: block !important; }}
    }}

    /* ── Responsive ── */
    @media only screen and (max-width: 620px) {{
      .email-card {{ width: 100% !important; border-radius: 0 !important; }}
      .email-pad  {{ padding: 32px 24px !important; }}
      .email-hdr  {{ padding: 28px 24px 24px !important; }}
      .email-ftr  {{ padding: 20px 24px !important; }}
    }}
  </style>
</head>
<body class="email-bg" style="margin:0;padding:0;background-color:{_LIGHT_BG};">
<!--[if mso | IE]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center"><![endif]-->
<table class="email-bg" width="100%" cellpadding="0" cellspacing="0" border="0"
       style="background-color:{_LIGHT_BG};min-height:100%;">
  <tr>
    <td align="center" valign="top" style="padding:48px 16px;">

      <!-- Card -->
      <table class="email-card" width="580" cellpadding="0" cellspacing="0" border="0"
             style="background-color:{_LIGHT_CARD};border-radius:3px;
                    box-shadow:0 1px 8px rgba(0,0,0,0.08);overflow:hidden;max-width:580px;width:100%;">

        <!-- Header -->
        <tr>
          <td class="email-header email-hdr"
              style="padding:32px 48px 28px;border-bottom:1px solid {_LIGHT_BORDER};">
            <table width="100%" cellpadding="0" cellspacing="0" border="0">
              <tr>
                <td valign="middle">
                  <!-- Light mode logo (dark ink) -->
                  <img class="logo-light"
                       src="{LOGO_LIGHT_URL}"
                       alt="NeolabCare" width="130" height="auto" border="0"
                       style="display:block;width:130px;height:auto;max-width:130px;">
                  <!-- Dark mode logo (white ink) -->
                  <img class="logo-dark"
                       src="{LOGO_DARK_URL}"
                       alt="NeolabCare" width="130" height="auto" border="0"
                       style="display:none;width:130px;height:auto;max-width:130px;">
                </td>
                <td align="right" valign="middle">
                  <span class="text-gold"
                        style="font-family:{_FONT};font-size:9px;font-weight:600;
                               letter-spacing:2.5px;text-transform:uppercase;color:{_GOLD};">
                    Creator Partner Program
                  </span>
                </td>
              </tr>
            </table>
          </td>
        </tr>

        <!-- Body -->
        <tr>
          <td class="email-pad" style="padding:40px 48px;">
            {body_html}
          </td>
        </tr>

        <!-- Footer -->
        <tr>
          <td class="email-footer email-ftr"
              style="padding:22px 48px;border-top:1px solid {_LIGHT_BORDER};
                     background-color:#FAFAF8;">
            <p class="text-footer"
               style="margin:0;font-family:{_FONT};font-size:10px;font-weight:400;
                      color:#AAAAAA;line-height:1.6;letter-spacing:0.3px;">
              NeolabCare &nbsp;&middot;&nbsp;
              <a href="mailto:hello@neolab.care"
                 style="color:inherit;text-decoration:none;">hello@neolab.care</a>
              &nbsp;&middot;&nbsp;
              <a href="https://neolabcare.com"
                 style="color:inherit;text-decoration:none;">neolabcare.com</a>
            </p>
            <p class="text-footer"
               style="margin:5px 0 0;font-family:{_FONT};font-size:9px;font-weight:300;
                      color:#AAAAAA;letter-spacing:0.2px;">
              &copy; 2026 NeolabCare. All rights reserved.
            </p>
          </td>
        </tr>

      </table>
      <!-- /Card -->

    </td>
  </tr>
</table>
<!--[if mso | IE]></td></tr></table><![endif]-->
</body>
</html>"""


# ── Template 1: Founder Notification ─────────────────────────────────────────
def _founder_notification(name, email, platform, followers, niche, reason, approve_url, **kw):
    body = f"""
    <p class="text-gold"
       style="margin:0 0 8px;font-family:{_FONT};font-size:9px;font-weight:700;
              letter-spacing:3px;text-transform:uppercase;color:{_GOLD};">
      New Application
    </p>
    <h1 class="text-primary"
        style="margin:0 0 28px;font-family:{_FONT};font-size:24px;font-weight:600;
               letter-spacing:-0.02em;color:{_LIGHT_TEXT};line-height:1.25;">
      Creator Partnership Request
    </h1>

    <!-- Applicant Card -->
    <table class="info-card" width="100%" cellpadding="0" cellspacing="0" border="0"
           style="background-color:#FAFAF8;border:1px solid {_LIGHT_BORDER};
                  border-radius:2px;margin-bottom:28px;">
      <tr><td style="padding:0 24px;">

        <!-- Name -->
        <table width="100%" cellpadding="0" cellspacing="0" border="0">
          <tr><td style="padding:20px 0 16px;">
            <table width="100%" cellpadding="0" cellspacing="0" border="0">
              <tr><td>
                <p class="text-muted" style="margin:0 0 4px;font-family:{_FONT};font-size:9px;
                   font-weight:700;letter-spacing:2.5px;text-transform:uppercase;color:{_LIGHT_MUTED};">
                  Creator Name</p>
                <p class="text-primary" style="margin:0;font-family:{_FONT};font-size:16px;
                   font-weight:600;color:{_LIGHT_TEXT};letter-spacing:-0.01em;">{name}</p>
              </td></tr>
            </table>
            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:16px;">
              <tr><td class="field-divider" height="1"
                      style="background-color:{_LIGHT_BORDER};font-size:0;line-height:0;">&nbsp;</td></tr>
            </table>
          </td></tr>

          <!-- Email -->
          <tr><td style="padding:16px 0;">
            <p class="text-muted" style="margin:0 0 4px;font-family:{_FONT};font-size:9px;
               font-weight:700;letter-spacing:2.5px;text-transform:uppercase;color:{_LIGHT_MUTED};">
              Email</p>
            <p class="text-primary" style="margin:0;font-family:{_FONT};font-size:14px;
               font-weight:400;color:{_LIGHT_TEXT};">
              <a href="mailto:{email}" style="color:inherit;text-decoration:none;">{email}</a>
            </p>
            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:16px;">
              <tr><td class="field-divider" height="1"
                      style="background-color:{_LIGHT_BORDER};font-size:0;line-height:0;">&nbsp;</td></tr>
            </table>
          </td></tr>

          <!-- Platform -->
          <tr><td style="padding:16px 0;">
            <p class="text-muted" style="margin:0 0 4px;font-family:{_FONT};font-size:9px;
               font-weight:700;letter-spacing:2.5px;text-transform:uppercase;color:{_LIGHT_MUTED};">
              Platform &amp; Reach</p>
            <p class="text-primary" style="margin:0;font-family:{_FONT};font-size:14px;
               font-weight:400;color:{_LIGHT_TEXT};">
              {platform} &mdash; <strong style="font-weight:600;">{followers}</strong> followers
            </p>
            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:16px;">
              <tr><td class="field-divider" height="1"
                      style="background-color:{_LIGHT_BORDER};font-size:0;line-height:0;">&nbsp;</td></tr>
            </table>
          </td></tr>

          <!-- Niche -->
          <tr><td style="padding:16px 0;">
            <p class="text-muted" style="margin:0 0 4px;font-family:{_FONT};font-size:9px;
               font-weight:700;letter-spacing:2.5px;text-transform:uppercase;color:{_LIGHT_MUTED};">
              Niche / Content Type</p>
            <p class="text-primary" style="margin:0;font-family:{_FONT};font-size:14px;
               font-weight:400;color:{_LIGHT_TEXT};">{niche}</p>
            <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-top:16px;">
              <tr><td class="field-divider" height="1"
                      style="background-color:{_LIGHT_BORDER};font-size:0;line-height:0;">&nbsp;</td></tr>
            </table>
          </td></tr>

          <!-- Reason -->
          <tr><td style="padding:16px 0 20px;">
            <p class="text-muted" style="margin:0 0 4px;font-family:{_FONT};font-size:9px;
               font-weight:700;letter-spacing:2.5px;text-transform:uppercase;color:{_LIGHT_MUTED};">
              Why NeolabCare</p>
            <p class="text-body" style="margin:0;font-family:{_FONT};font-size:14px;
               font-weight:300;color:{_LIGHT_BODY};line-height:1.75;">{reason}</p>
          </td></tr>
        </table>

      </td></tr>
    </table>

    <!-- CTA -->
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom:10px;">
      <tr><td align="center">
        <!--[if mso]>
        <v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" href="{approve_url}"
          style="height:52px;v-text-anchor:middle;width:280px;" arcsize="4%"
          fillcolor="#0A0A0A" strokecolor="#0A0A0A">
          <w:anchorlock/>
          <center style="color:#ffffff;font-family:sans-serif;font-size:11px;
            font-weight:bold;letter-spacing:2.5px;text-transform:uppercase;">
            APPROVE APPLICATION</center>
        </v:roundrect>
        <![endif]-->
        <!--[if !mso]><!-->
        <a class="cta-btn" href="{approve_url}"
           style="display:inline-block;background-color:{_BLACK};color:{_WHITE};
                  font-family:{_FONT};font-size:11px;font-weight:700;
                  letter-spacing:2.5px;text-transform:uppercase;text-decoration:none;
                  padding:17px 52px;border-radius:2px;min-width:220px;text-align:center;">
          Approve Application
        </a>
        <!--<![endif]-->
      </td></tr>
    </table>
    <p class="text-muted"
       style="margin:0;font-family:{_FONT};font-size:10px;font-weight:300;
              color:{_LIGHT_MUTED};text-align:center;letter-spacing:0.2px;">
      Clicking this link approves the creator and triggers their welcome email.
    </p>
    """
    return _shell(body)


# ── Template 2: Creator — Application Received ───────────────────────────────
def _creator_received(first_name, **kw):
    body = f"""
    <p class="text-gold"
       style="margin:0 0 8px;font-family:{_FONT};font-size:9px;font-weight:700;
              letter-spacing:3px;text-transform:uppercase;color:{_GOLD};">
      Application Received
    </p>
    <h1 class="text-primary"
        style="margin:0 0 8px;font-family:{_FONT};font-size:24px;font-weight:600;
               letter-spacing:-0.02em;color:{_LIGHT_TEXT};line-height:1.25;">
      Hi {first_name}, we've got your application.
    </h1>

    <!-- Gold rule -->
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:16px 0 24px;">
      <tr><td width="28" height="2" bgcolor="{_GOLD}"
              style="background-color:{_GOLD};font-size:0;line-height:0;">&nbsp;</td>
          <td style="font-size:0;line-height:0;">&nbsp;</td></tr>
    </table>

    <p class="text-body"
       style="margin:0 0 16px;font-family:{_FONT};font-size:15px;font-weight:300;
              color:{_LIGHT_BODY};line-height:1.8;">
      Thank you for applying to the NeolabCare Creator Partner Program.
      We've received your application and are reviewing your profile personally.
    </p>
    <p class="text-body"
       style="margin:0 0 32px;font-family:{_FONT};font-size:15px;font-weight:300;
              color:{_LIGHT_BODY};line-height:1.8;">
      If your profile is a strong fit, you'll hear from us within
      <strong class="text-primary" style="font-weight:600;color:{_LIGHT_TEXT};">48&ndash;72 hours</strong>.
    </p>

    <!-- What Happens Next -->
    <table class="info-card info-card-accent" width="100%" cellpadding="0" cellspacing="0" border="0"
           style="background-color:#FAFAF8;border:1px solid {_LIGHT_BORDER};
                  border-left:3px solid {_GOLD};border-radius:2px;margin-bottom:32px;">
      <tr><td style="padding:22px 24px;">
        <p class="text-gold"
           style="margin:0 0 12px;font-family:{_FONT};font-size:9px;font-weight:700;
                  letter-spacing:2.5px;text-transform:uppercase;color:{_GOLD};">
          What Happens Next
        </p>
        <p class="text-body"
           style="margin:0 0 8px;font-family:{_FONT};font-size:13px;font-weight:300;
                  color:{_LIGHT_BODY};line-height:1.7;">
          &rarr;&nbsp; We review applications within
          <strong class="text-primary" style="font-weight:600;color:{_LIGHT_TEXT};">48&ndash;72 hours</strong>
        </p>
        <p class="text-body"
           style="margin:0 0 8px;font-family:{_FONT};font-size:13px;font-weight:300;
                  color:{_LIGHT_BODY};line-height:1.7;">
          &rarr;&nbsp; Founding Batch is
          <strong class="text-primary" style="font-weight:600;color:{_LIGHT_TEXT};">limited to 50 creators</strong>
        </p>
        <p class="text-body"
           style="margin:0;font-family:{_FONT};font-size:13px;font-weight:300;
                  color:{_LIGHT_BODY};line-height:1.7;">
          &rarr;&nbsp; If approved, you receive your
          <strong class="text-primary" style="font-weight:600;color:{_LIGHT_TEXT};">private creator code + 15% commission</strong>
        </p>
      </td></tr>
    </table>

    <p class="text-muted"
       style="margin:0;font-family:{_FONT};font-size:13px;font-weight:300;
              color:{_LIGHT_MUTED};line-height:1.7;">
      Questions? Reply to this email or reach us at
      <a href="mailto:hello@neolab.care"
         class="text-primary"
         style="color:{_LIGHT_TEXT};font-weight:500;text-decoration:none;">
        hello@neolab.care</a>
    </p>
    """
    return _shell(body)


# ── Template 3: Creator — Approved ───────────────────────────────────────────
def _creator_approved(first_name, discount_code, referral_link, dashboard_url, **kw):
    body = f"""
    <p class="text-gold"
       style="margin:0 0 8px;font-family:{_FONT};font-size:9px;font-weight:700;
              letter-spacing:3px;text-transform:uppercase;color:{_GOLD};">
      You're Approved
    </p>
    <h1 class="text-primary"
        style="margin:0 0 8px;font-family:{_FONT};font-size:24px;font-weight:600;
               letter-spacing:-0.02em;color:{_LIGHT_TEXT};line-height:1.25;">
      Welcome to the Founding Batch.
    </h1>

    <!-- Gold rule -->
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin:16px 0 24px;">
      <tr><td width="28" height="2" bgcolor="{_GOLD}"
              style="background-color:{_GOLD};font-size:0;line-height:0;">&nbsp;</td>
          <td style="font-size:0;line-height:0;">&nbsp;</td></tr>
    </table>

    <p class="text-body"
       style="margin:0 0 28px;font-family:{_FONT};font-size:15px;font-weight:300;
              color:{_LIGHT_BODY};line-height:1.8;">
      Hi {first_name}, you've been selected as a NeolabCare Creator Partner.
      Below are your credentials — keep them private, they're unique to you.
    </p>

    <!-- Code Card — always dark regardless of mode -->
    <table class="code-card" width="100%" cellpadding="0" cellspacing="0" border="0"
           style="background-color:{_BLACK};border-radius:2px 2px 0 0;margin-bottom:0;">
      <tr><td style="padding:28px 32px 24px;">
        <p class="text-gold"
           style="margin:0 0 6px;font-family:{_FONT};font-size:9px;font-weight:700;
                  letter-spacing:3px;text-transform:uppercase;color:{_GOLD};">
          Your Creator Code
        </p>
        <p class="code-text"
           style="margin:0 0 16px;font-family:{_FONT};font-size:38px;font-weight:700;
                  letter-spacing:0.1em;color:{_WHITE};line-height:1;">
          {discount_code}
        </p>
        <p class="code-sub"
           style="margin:0;font-family:{_FONT};font-size:13px;font-weight:300;
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
    <table class="ref-card" width="100%" cellpadding="0" cellspacing="0" border="0"
           style="background-color:#FAFAF8;border:1px solid {_LIGHT_BORDER};
                  border-top:none;border-radius:0 0 2px 2px;margin-bottom:28px;">
      <tr><td style="padding:16px 24px;">
        <p class="text-muted"
           style="margin:0 0 4px;font-family:{_FONT};font-size:9px;font-weight:700;
                  letter-spacing:2.5px;text-transform:uppercase;color:{_LIGHT_MUTED};">
          Your Referral Link
        </p>
        <a class="text-primary" href="{referral_link}"
           style="font-family:{_FONT};font-size:13px;font-weight:400;color:{_LIGHT_TEXT};
                  word-break:break-all;text-decoration:underline;
                  text-decoration-color:{_GOLD};">
          {referral_link}
        </a>
      </td></tr>
    </table>

    <!-- Dashboard CTA -->
    <table width="100%" cellpadding="0" cellspacing="0" border="0" style="margin-bottom:10px;">
      <tr><td align="center">
        <!--[if mso]>
        <v:roundrect xmlns:v="urn:schemas-microsoft-com:vml" href="{dashboard_url}"
          style="height:52px;v-text-anchor:middle;width:280px;" arcsize="4%"
          fillcolor="#0A0A0A" strokecolor="#0A0A0A">
          <w:anchorlock/>
          <center style="color:#ffffff;font-family:sans-serif;font-size:11px;
            font-weight:bold;letter-spacing:2.5px;text-transform:uppercase;">
            VIEW YOUR DASHBOARD</center>
        </v:roundrect>
        <![endif]-->
        <!--[if !mso]><!-->
        <a class="cta-btn" href="{dashboard_url}"
           style="display:inline-block;background-color:{_BLACK};color:{_WHITE};
                  font-family:{_FONT};font-size:11px;font-weight:700;
                  letter-spacing:2.5px;text-transform:uppercase;text-decoration:none;
                  padding:17px 52px;border-radius:2px;min-width:220px;text-align:center;">
          View Your Dashboard
        </a>
        <!--<![endif]-->
      </td></tr>
    </table>
    <p class="text-muted"
       style="margin:0 0 32px;font-family:{_FONT};font-size:10px;font-weight:300;
              color:{_LIGHT_MUTED};text-align:center;letter-spacing:0.2px;">
      Live stats: orders, revenue, confirmed and pending commission.
    </p>

    <!-- How it works -->
    <table width="100%" cellpadding="0" cellspacing="0" border="0">
      <tr><td class="email-divider" height="1"
              style="background-color:{_LIGHT_BORDER};font-size:0;line-height:0;">&nbsp;</td></tr>
    </table>
    <table width="100%" cellpadding="0" cellspacing="0" border="0">
      <tr><td style="padding-top:24px;">
        <p class="text-gold"
           style="margin:0 0 12px;font-family:{_FONT};font-size:9px;font-weight:700;
                  letter-spacing:2.5px;text-transform:uppercase;color:{_GOLD};">
          How It Works
        </p>
        <p class="text-body" style="margin:0 0 7px;font-family:{_FONT};font-size:13px;
           font-weight:300;color:{_LIGHT_BODY};line-height:1.7;">
          &rarr;&nbsp; Share your link or code with your audience
        </p>
        <p class="text-body" style="margin:0 0 7px;font-family:{_FONT};font-size:13px;
           font-weight:300;color:{_LIGHT_BODY};line-height:1.7;">
          &rarr;&nbsp; They get 50% off the Founding Price
        </p>
        <p class="text-body" style="margin:0 0 7px;font-family:{_FONT};font-size:13px;
           font-weight:300;color:{_LIGHT_BODY};line-height:1.7;">
          &rarr;&nbsp; You earn 15% on every confirmed order
        </p>
        <p class="text-body" style="margin:0;font-family:{_FONT};font-size:13px;
           font-weight:300;color:{_LIGHT_BODY};line-height:1.7;">
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
