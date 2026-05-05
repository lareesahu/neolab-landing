# NeoLabCare Luxury Email Templates (Void Aesthetic)

FOUNDER_NOTIFICATION_HTML = """
<!DOCTYPE html>
<html>
<head>
<style>
  body { background-color: #0A0A0A; color: #F5F5F0; font-family: 'Inter', -apple-system, sans-serif; margin: 0; padding: 0; }
  .container { max-width: 600px; margin: 0 auto; padding: 40px 20px; }
  .header { border-bottom: 1px solid #2E2E2E; padding-bottom: 20px; margin-bottom: 30px; }
  .logo { font-size: 14px; letter-spacing: 4px; text-transform: uppercase; color: #F5F5F0; font-weight: 300; }
  .badge { background: #C8B89A; color: #0A0A0A; padding: 4px 12px; font-size: 10px; font-weight: 600; text-transform: uppercase; border-radius: 2px; margin-bottom: 10px; display: inline-block; }
  h1 { font-size: 24px; font-weight: 300; margin: 0 0 20px; color: #F5F5F0; }
  .card { background: #141414; border: 1px solid #2E2E2E; padding: 30px; border-radius: 4px; margin-bottom: 30px; }
  .field { margin-bottom: 15px; }
  .label { font-size: 10px; color: #666; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 4px; }
  .value { font-size: 14px; color: #F5F5F0; }
  .btn { display: inline-block; background: #F5F5F0; color: #0A0A0A; padding: 16px 32px; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 2px; text-decoration: none; border-radius: 2px; margin-top: 20px; }
  .footer { font-size: 10px; color: #444; margin-top: 40px; text-align: center; letter-spacing: 1px; }
</style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div class="logo">NEOLABCARE</div>
    </div>
    <div class="badge">New Application</div>
    <h1>Creator Partnership Request</h1>
    <div class="card">
      <div class="field">
        <div class="label">Creator Name</div>
        <div class="value">{{name}}</div>
      </div>
      <div class="field">
        <div class="label">Email</div>
        <div class="value">{{email}}</div>
      </div>
      <div class="field">
        <div class="label">Platform & Reach</div>
        <div class="value">{{platform}} — {{audience_size}} followers</div>
      </div>
      <div class="field">
        <div class="label">Niche</div>
        <div class="value">{{niche}}</div>
      </div>
      <div class="field">
        <div class="label">Reason for Fit</div>
        <div class="value">{{fit_reason}}</div>
      </div>
    </div>
    <a href="{{approve_url}}" class="btn">Approve Application</a>
    <div class="footer">
      NEOLABCARE INTERNAL SYSTEM &copy; 2026
    </div>
  </div>
</body>
</html>
"""

CREATOR_RECEIVED_HTML = """
<!DOCTYPE html>
<html>
<head>
<style>
  body { background-color: #0A0A0A; color: #F5F5F0; font-family: 'Inter', -apple-system, sans-serif; margin: 0; padding: 0; }
  .container { max-width: 600px; margin: 0 auto; padding: 60px 20px; text-align: center; }
  .header { margin-bottom: 50px; }
  .logo { font-size: 16px; letter-spacing: 6px; text-transform: uppercase; color: #F5F5F0; font-weight: 300; }
  h1 { font-size: 28px; font-weight: 300; margin: 0 0 20px; color: #F5F5F0; letter-spacing: -0.5px; }
  p { font-size: 16px; color: #999; line-height: 1.6; margin-bottom: 30px; }
  .divider { width: 40px; height: 1px; background: #C8B89A; margin: 40px auto; }
  .footer { font-size: 10px; color: #444; margin-top: 60px; letter-spacing: 2px; text-transform: uppercase; }
</style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div class="logo">NEOLABCARE</div>
    </div>
    <h1>Application Received.</h1>
    <p>Hi {{first_name}}, thank you for your interest in the NeoLabCare Creator Partner Program. We have received your application and our team is currently reviewing your profile.</p>
    <p>We review applications within 48–72 hours. If your audience is a fit for our Founding Batch, we will reach out with your private creator code and referral link.</p>
    <div class="divider"></div>
    <div class="footer">
      Lab-Fresh. Made to Order. Dispatched within 7 days.
    </div>
  </div>
</body>
</html>
"""

CREATOR_APPROVED_HTML = """
<!DOCTYPE html>
<html>
<head>
<style>
  body { background-color: #0A0A0A; color: #F5F5F0; font-family: 'Inter', -apple-system, sans-serif; margin: 0; padding: 0; }
  .container { max-width: 600px; margin: 0 auto; padding: 60px 20px; }
  .header { border-bottom: 1px solid #2E2E2E; padding-bottom: 30px; margin-bottom: 40px; text-align: center; }
  .logo { font-size: 16px; letter-spacing: 6px; text-transform: uppercase; color: #F5F5F0; font-weight: 300; }
  h1 { font-size: 32px; font-weight: 300; margin: 0 0 20px; color: #F5F5F0; text-align: center; }
  .card { background: #141414; border: 1px solid #C8B89A; padding: 40px; border-radius: 4px; margin-bottom: 40px; text-align: center; }
  .code-label { font-size: 10px; color: #C8B89A; text-transform: uppercase; letter-spacing: 3px; margin-bottom: 15px; }
  .code-value { font-size: 36px; font-weight: 600; color: #F5F5F0; letter-spacing: 4px; margin-bottom: 20px; }
  .details { font-size: 14px; color: #999; line-height: 1.8; margin-bottom: 30px; }
  .btn { display: inline-block; background: #F5F5F0; color: #0A0A0A; padding: 18px 36px; font-size: 12px; font-weight: 600; text-transform: uppercase; letter-spacing: 2px; text-decoration: none; border-radius: 2px; width: 100%; box-sizing: border-box; text-align: center; }
  .footer { font-size: 10px; color: #444; margin-top: 60px; text-align: center; letter-spacing: 2px; text-transform: uppercase; }
</style>
</head>
<body>
  <div class="container">
    <div class="header">
      <div class="logo">NEOLABCARE</div>
    </div>
    <h1>You're Approved.</h1>
    <div class="card">
      <div class="code-label">Your Creator Code</div>
      <div class="code-value">{{discount_code}}</div>
      <div class="details">
        Your code unlocks the <strong>Founding Price ($99)</strong> for your audience and tracks your <strong>15% commission</strong> on every confirmed sale.
      </div>
      <a href="{{dashboard_url}}" class="btn">Access Partner Dashboard</a>
    </div>
    <div class="details" style="text-align: center;">
      <strong>Your Referral Link:</strong><br>
      <span style="color: #C8B89A;">{{referral_link}}</span>
    </div>
    <div class="footer">
      NEOLABCARE &copy; 2026 — Private Partner Access
    </div>
  </div>
</body>
</html>
"""
