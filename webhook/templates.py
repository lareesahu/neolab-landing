# NeoLabCare Luxury Email Templates
# Logo: https://files.manuscdn.com/user_upload_by_module/session_file/310519663379624584/YdRBXUpuMceVgsRG.png

LOGO_URL = "https://files.manuscdn.com/user_upload_by_module/session_file/310519663379624584/YdRBXUpuMceVgsRG.png"

FOUNDER_NOTIFICATION_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>New Creator Application</title>
</head>
<body style="margin:0;padding:0;background-color:#0A0A0A;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#0A0A0A;">
    <tr>
      <td align="center" style="padding:48px 20px;">
        <table width="600" cellpadding="0" cellspacing="0" border="0" style="max-width:600px;width:100%;">

          <!-- Logo Header -->
          <tr>
            <td align="center" style="padding-bottom:40px;border-bottom:1px solid #1E1E1E;">
              <img src="{LOGO_URL}" alt="NeolabCare" width="56" height="auto" style="display:block;margin:0 auto 16px;" />
              <div style="font-size:9px;letter-spacing:5px;text-transform:uppercase;color:#666;font-weight:400;">Creator Partner Program</div>
            </td>
          </tr>

          <!-- Badge + Title -->
          <tr>
            <td style="padding:36px 0 24px;">
              <table cellpadding="0" cellspacing="0" border="0">
                <tr>
                  <td style="background:#C8B89A;padding:5px 14px;border-radius:2px;">
                    <span style="font-size:9px;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:#0A0A0A;">New Application</span>
                  </td>
                </tr>
              </table>
              <div style="font-size:26px;font-weight:300;color:#F5F5F0;margin-top:16px;letter-spacing:-0.5px;line-height:1.3;">Creator Partnership Request</div>
            </td>
          </tr>

          <!-- Info Card -->
          <tr>
            <td style="background:#111111;border:1px solid #222222;border-radius:4px;padding:32px;">
              <table width="100%" cellpadding="0" cellspacing="0" border="0">
                <tr>
                  <td style="padding-bottom:20px;border-bottom:1px solid #1A1A1A;">
                    <div style="font-size:9px;letter-spacing:2px;text-transform:uppercase;color:#555;margin-bottom:6px;">Creator Name</div>
                    <div style="font-size:16px;color:#F5F5F0;font-weight:500;">{{name}}</div>
                  </td>
                </tr>
                <tr>
                  <td style="padding:20px 0;border-bottom:1px solid #1A1A1A;">
                    <div style="font-size:9px;letter-spacing:2px;text-transform:uppercase;color:#555;margin-bottom:6px;">Email</div>
                    <div style="font-size:14px;color:#C8B89A;">{{email}}</div>
                  </td>
                </tr>
                <tr>
                  <td style="padding:20px 0;border-bottom:1px solid #1A1A1A;">
                    <div style="font-size:9px;letter-spacing:2px;text-transform:uppercase;color:#555;margin-bottom:6px;">Platform &amp; Reach</div>
                    <div style="font-size:14px;color:#F5F5F0;">{{platform}} &mdash; <strong style="color:#F5F5F0;">{{audience_size}}</strong> followers</div>
                  </td>
                </tr>
                <tr>
                  <td style="padding:20px 0;border-bottom:1px solid #1A1A1A;">
                    <div style="font-size:9px;letter-spacing:2px;text-transform:uppercase;color:#555;margin-bottom:6px;">Niche / Content Type</div>
                    <div style="font-size:14px;color:#F5F5F0;">{{niche}}</div>
                  </td>
                </tr>
                <tr>
                  <td style="padding:20px 0 0;">
                    <div style="font-size:9px;letter-spacing:2px;text-transform:uppercase;color:#555;margin-bottom:6px;">Why NeolabCare</div>
                    <div style="font-size:14px;color:#F5F5F0;line-height:1.7;">{{fit_reason}}</div>
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- CTA Button -->
          <tr>
            <td style="padding:32px 0 0;">
              <table width="100%" cellpadding="0" cellspacing="0" border="0">
                <tr>
                  <td align="center" style="background:#F5F5F0;border-radius:3px;">
                    <a href="{{approve_url}}" style="display:block;padding:18px 32px;font-size:11px;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:#0A0A0A;text-decoration:none;">Approve Application</a>
                  </td>
                </tr>
              </table>
              <div style="font-size:11px;color:#444;text-align:center;margin-top:12px;">Clicking this link will approve the creator and trigger their welcome email.</div>
            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td style="padding:48px 0 0;border-top:1px solid #1A1A1A;margin-top:40px;">
              <div style="font-size:9px;letter-spacing:3px;text-transform:uppercase;color:#333;text-align:center;">NeolabCare Internal &mdash; Founder Access Only &mdash; 2026</div>
            </td>
          </tr>

        </table>
      </td>
    </tr>
  </table>
</body>
</html>
""".replace("{LOGO_URL}", LOGO_URL)


CREATOR_RECEIVED_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Application Received</title>
</head>
<body style="margin:0;padding:0;background-color:#0A0A0A;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#0A0A0A;">
    <tr>
      <td align="center" style="padding:64px 20px;">
        <table width="560" cellpadding="0" cellspacing="0" border="0" style="max-width:560px;width:100%;">

          <!-- Logo -->
          <tr>
            <td align="center" style="padding-bottom:56px;">
              <img src="{LOGO_URL}" alt="NeolabCare" width="64" height="auto" style="display:block;margin:0 auto;" />
            </td>
          </tr>

          <!-- Headline -->
          <tr>
            <td align="center" style="padding-bottom:24px;">
              <div style="font-size:32px;font-weight:300;color:#F5F5F0;letter-spacing:-1px;line-height:1.2;">Application Received.</div>
            </td>
          </tr>

          <!-- Body -->
          <tr>
            <td align="center" style="padding-bottom:40px;">
              <div style="font-size:15px;color:#777;line-height:1.8;max-width:420px;margin:0 auto;">
                Hi {{first_name}}, thank you for applying to the NeolabCare Creator Partner Program. We have received your application and are reviewing your profile.
              </div>
            </td>
          </tr>

          <!-- Divider -->
          <tr>
            <td align="center" style="padding-bottom:40px;">
              <table cellpadding="0" cellspacing="0" border="0">
                <tr>
                  <td width="40" height="1" style="background:#C8B89A;font-size:0;line-height:0;">&nbsp;</td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- Timeline -->
          <tr>
            <td style="background:#111111;border:1px solid #1E1E1E;border-radius:4px;padding:32px 36px;">
              <div style="font-size:9px;letter-spacing:3px;text-transform:uppercase;color:#C8B89A;margin-bottom:16px;">What Happens Next</div>
              <div style="font-size:13px;color:#888;line-height:2;">
                &rarr;&nbsp; We review applications within <strong style="color:#F5F5F0;">48–72 hours</strong><br>
                &rarr;&nbsp; Founding Batch is <strong style="color:#F5F5F0;">limited to 50 creators</strong><br>
                &rarr;&nbsp; If approved, you receive your <strong style="color:#F5F5F0;">private creator code + 15% commission</strong>
              </div>
            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td align="center" style="padding-top:56px;">
              <div style="font-size:9px;letter-spacing:3px;text-transform:uppercase;color:#333;">Lab-Fresh &nbsp;&middot;&nbsp; Made to Order &nbsp;&middot;&nbsp; Dispatched within 7 days</div>
            </td>
          </tr>

        </table>
      </td>
    </tr>
  </table>
</body>
</html>
""".replace("{LOGO_URL}", LOGO_URL)


CREATOR_APPROVED_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>You're Approved</title>
</head>
<body style="margin:0;padding:0;background-color:#0A0A0A;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif;">
  <table width="100%" cellpadding="0" cellspacing="0" border="0" style="background-color:#0A0A0A;">
    <tr>
      <td align="center" style="padding:64px 20px;">
        <table width="560" cellpadding="0" cellspacing="0" border="0" style="max-width:560px;width:100%;">

          <!-- Logo -->
          <tr>
            <td align="center" style="padding-bottom:48px;border-bottom:1px solid #1A1A1A;">
              <img src="{LOGO_URL}" alt="NeolabCare" width="64" height="auto" style="display:block;margin:0 auto 16px;" />
              <div style="font-size:9px;letter-spacing:5px;text-transform:uppercase;color:#555;">Creator Partner Program</div>
            </td>
          </tr>

          <!-- Headline -->
          <tr>
            <td align="center" style="padding:48px 0 36px;">
              <div style="font-size:11px;letter-spacing:4px;text-transform:uppercase;color:#C8B89A;margin-bottom:16px;">Founding Batch</div>
              <div style="font-size:36px;font-weight:300;color:#F5F5F0;letter-spacing:-1px;">You're Approved.</div>
            </td>
          </tr>

          <!-- Code Card -->
          <tr>
            <td style="background:#111111;border:1px solid #C8B89A;border-radius:4px;padding:40px;text-align:center;">
              <div style="font-size:9px;letter-spacing:4px;text-transform:uppercase;color:#C8B89A;margin-bottom:16px;">Your Creator Code</div>
              <div style="font-size:42px;font-weight:700;color:#F5F5F0;letter-spacing:6px;margin-bottom:24px;font-variant-numeric:tabular-nums;">{{discount_code}}</div>
              <div style="font-size:13px;color:#666;line-height:1.9;margin-bottom:32px;">
                Share this code with your audience.<br>
                They get the <strong style="color:#F5F5F0;">Founding Price ($99)</strong> &nbsp;&middot;&nbsp; You earn <strong style="color:#F5F5F0;">15% commission</strong> on every confirmed sale.
              </div>
              <table width="100%" cellpadding="0" cellspacing="0" border="0">
                <tr>
                  <td align="center" style="background:#F5F5F0;border-radius:3px;">
                    <a href="{{dashboard_url}}" style="display:block;padding:18px 32px;font-size:11px;font-weight:700;letter-spacing:3px;text-transform:uppercase;color:#0A0A0A;text-decoration:none;">Access Partner Dashboard</a>
                  </td>
                </tr>
              </table>
            </td>
          </tr>

          <!-- Referral Link -->
          <tr>
            <td style="padding:32px 0 0;text-align:center;">
              <div style="font-size:9px;letter-spacing:3px;text-transform:uppercase;color:#555;margin-bottom:10px;">Your Referral Link</div>
              <div style="font-size:13px;color:#C8B89A;word-break:break-all;">{{referral_link}}</div>
            </td>
          </tr>

          <!-- Footer -->
          <tr>
            <td align="center" style="padding-top:56px;border-top:1px solid #1A1A1A;margin-top:40px;">
              <div style="font-size:9px;letter-spacing:3px;text-transform:uppercase;color:#333;">NeolabCare &mdash; Private Partner Access &mdash; 2026</div>
            </td>
          </tr>

        </table>
      </td>
    </tr>
  </table>
</body>
</html>
""".replace("{LOGO_URL}", LOGO_URL)
