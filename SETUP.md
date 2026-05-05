# Creator Affiliate Pipeline — Setup Guide

Everything below is a one-time setup. Estimated time: ~20 minutes.

---

## Step 1 — Add two tabs to your Google Sheet

**Link:** https://docs.google.com/spreadsheets/d/1sBoEdScXkdI4mzO422qB1viAqnuemh7XeRJDuOF8ZnA

1. Open the sheet
2. Click the **+** button at the bottom left to add a new tab
3. Rename it exactly: `Creators`
4. Add another tab, rename it exactly: `Commissions`
5. No headers needed — the server writes its own rows

- [ ] `Creators` tab created
- [ ] `Commissions` tab created

---

## Step 2 — Set environment variables in Render

**Link:** https://dashboard.render.com → service **neolabcare-webhook** → **Environment** tab

Add these variables:

### `APPROVAL_SECRET`
Generate a random secret here and paste it in:
https://generate-secret.vercel.app/64

### `WEBHOOK_BASE_URL`
Your webhook server's public URL. To find it: in Render, click the **neolabcare-webhook** service — the URL is shown at the top. Copy it exactly, no trailing slash.
Example: `https://neolabcare-webhook.onrender.com`

### `FOUNDER_EMAIL`
Already defaults to `lareesa@neolab.care` — only add this if you want a different address.

### `GMAIL_USER`
The Gmail address used to send notifications (e.g., `neolabcare@gmail.com`).

### `GMAIL_APP_PASSWORD`
A Gmail App Password (NOT your regular password). [Generate one here](https://myaccount.google.com/apppasswords).

- [ ] `APPROVAL_SECRET` set in Render
- [ ] `WEBHOOK_BASE_URL` confirmed and set in Render
- [ ] `GMAIL_USER` set in Render
- [ ] `GMAIL_APP_PASSWORD` set in Render
- [ ] **Save Changes** clicked in Render (service redeploys automatically, ~2 min)

---

## Step 3 — Verify the server is working

Once Render finishes redeploying, open this in your browser (replace with your actual URL):

```
https://neolabcare-webhook.onrender.com/health
```

You should see: `ok`

- [ ] `/health` returns `ok`

---

## Step 4 — Register the Shopify order webhook

This tells the server when a creator's discount code is used at checkout.

**Link:** https://admin.shopify.com/store/neolab-care/settings/notifications

1. Scroll to the bottom → **Webhooks** section
2. Click **Create webhook**
3. Set:
   - **Event:** `Order creation`
   - **Format:** `JSON`
   - **URL:** `https://neolabcare-webhook.onrender.com/shopify-order`
4. Click **Save**
5. Shopify shows a **webhook signing secret** — copy it
6. Go back to Render → **neolabcare-webhook** → **Environment**
7. Add: `SHOPIFY_WEBHOOK_SECRET` = the secret you just copied
8. Save → Render redeploys

- [ ] Shopify webhook created (Event: Order creation)
- [ ] `SHOPIFY_WEBHOOK_SECRET` added to Render
- [ ] Render redeployed

---

## Step 5 — Test the full flow end to end

1. Open https://neolab.care/creator-partner.html in an incognito window
2. Fill out the form with a test name (e.g. "Test Creator") and your own email
3. Submit — you should receive two emails:
   - One to `lareesa@neolab.care` with all application details + an **approve link**
 89. One "application received" confirmation email sent to the test email via Gmail
90. Click the approve link in the founder email
91. You should see a green confirmation page
92. One approval email sent to the creator with their code and dashboard link via Gmail
93. (Optional) If Shopify API is not set up, you'll see a reminder to create the code manually on the confirmation page.

- [ ] Test application submitted
- [ ] Founder email received with approve link
- [ ] Approve link loads a green confirmation page
- [ ] Creator approval email received with code + dashboard link
- [ ] Shopify reminder email received

---

## Step 6 — Create each Shopify discount code (manual, ~30 sec per creator)

Each time you approve a creator, you'll receive an email telling you which code to create.

**Link:** https://admin.shopify.com/store/neolab-care/discounts/new

1. Select **Amount off products** → **Discount code**
2. Enter the code from the email (e.g. `SARAH99`)
3. Value: `50%`
4. Applies to: **All products**
5. Customer eligibility: **All customers**
6. Usage limits: check **Limit to one use per customer**
7. No expiry date
8. Click **Save discount**

- [ ] First discount code created in Shopify

---

## Later — Shopify Admin API (removes the manual step above)

Once set up, discount codes are created automatically the moment you approve a creator.

**Link:** https://admin.shopify.com/store/neolab-care/settings/apps/development

1. Click **Create an app** → name it `NeolabCare Backend`
2. Click **Configure Admin API scopes**
3. Enable: `write_price_rules`, `write_discount_codes`, `read_orders`
4. Click **Save** → **Install app** → **Install**
5. Copy the **Admin API access token** (shown once — save it somewhere safe)
6. Go to Render → **neolabcare-webhook** → **Environment**
7. Add:
   - `SHOPIFY_ADMIN_TOKEN` = the token you copied
   - `SHOPIFY_STORE` = `neolab-care.myshopify.com`
8. Save → discount codes now auto-create on every approval

- [ ] Shopify private app created with correct scopes
- [ ] `SHOPIFY_ADMIN_TOKEN` added to Render
- [ ] `SHOPIFY_STORE` = `neolab-care.myshopify.com` added to Render

---

## How it works (once live)

| Step | What happens |
|------|-------------|
| Creator applies at `/creator-partner.html` | Form POSTs to webhook → row added to `Creators` sheet → founder gets email with approve link → creator gets confirmation |
| Founder clicks approve link | Sheet row updates to Approved → creator emailed their code + referral link + dashboard → founder reminded to create Shopify discount code |
| Fan visits `neolab.care/?ref=sarah` | Referral banner appears, CTA links to checkout with `?discount=SARAH99` pre-applied |
| Fan checks out | Shopify fires order webhook → commission row added to `Commissions` sheet |
| Creator visits `neolab.care/partner-dashboard.html?code=SARAH99` | Live stats: orders, revenue, confirmed and pending commission |
| Monthly | Founder reviews `Commissions` sheet, sends payout to creator's nominated account |
