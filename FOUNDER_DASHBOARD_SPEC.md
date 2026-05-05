# NeolabCare Founder Dashboard — Engineering Spec

**Target Audience:** Claude (or any AI Agent)  
**Goal:** Build a secure, front-end heavy founder dashboard (`founder-dashboard.html`) that pulls data from the existing Python webhook server and Google Sheets to manage the Creator Partner Program.

---

## 1. Aesthetic & UI Rules (The "Caelum Standard")
- **Theme:** Void Aesthetic (Dark mode only).
- **Background:** `#0A0A0A`. Cards: `#111111`. Borders: `1px solid #1E1E1E`.
- **Accent:** Sand Gold (`#C8A96E`). Use sparingly for primary actions or highlights.
- **Typography:** `Poppins` for all UI text. 
- **Logo:** MUST use `<img src="assets/logo.svg" width="140" height="auto">`. NEVER use text/spans for the logo.
- **Layout:** Centered max-width container (`1024px`). Clean grid, generous padding (`32px` inside cards).

---

## 2. Authentication (Simple Token Gate)
The dashboard must be protected from public view. Since we don't have a database with user accounts, we will use a simple URL token gate.
- **Access URL:** `founder-dashboard.html?token=YOUR_FOUNDER_SECRET`
- **Logic:** On page load, JS checks if `URLSearchParams.get('token')` matches a hardcoded constant (or better, an env var passed via a new endpoint). If it fails, `document.body.innerHTML = 'Unauthorized';`.

---

## 3. Required API Endpoints (Backend Work)
Claude needs to add these to `webhook/server.py`:

1.  **`GET /founder-stats?token=...`**
    - Reads the `Creators` and `Commissions` sheets.
    - Returns JSON aggregating:
        - Total Creators (Approved vs Pending)
        - Total Revenue (Sum of all orders)
        - Total Commission Owed (Sum of pending commissions)
        - Array of all creators with their individual stats.
        - Array of recent orders/commissions.

2.  **`POST /mark-commission-paid`**
    - Accepts `{"order_id": "...", "creator_code": "...", "token": "..."}`
    - Updates the specific row in the `Commissions` sheet from `Pending` to `Paid`.

---

## 4. Frontend Layout & Components

### Section A: Top Nav
- Left: SVG Logo.
- Right: "Founder Access" label (muted text) + Logout button (clears URL token).

### Section B: Global KPI Cards (Grid of 4)
1.  **Total Revenue:** `$X,XXX`
2.  **Active Creators:** `XX` (Approved) / `YY` (Pending)
3.  **Pending Payouts:** `$XXX` (Commission owed but not paid)
4.  **Total Paid Out:** `$XXX` (Commission already marked paid)

### Section C: Creator Management Table
- **Columns:** Name, Code, Status (Pending/Approved), Audience Size, Revenue Driven, Commission Owed.
- **Actions:** 
    - If Pending: "Review Application" (Links to the existing `approve-creator` flow).
    - If Approved: "Copy Code" button.

### Section D: Commission Payout Ledger
- **Columns:** Date, Order ID, Creator Code, Order Value, Commission (15%), Status (Pending/Paid).
- **Actions:**
    - If Pending: "Mark as Paid" button. Triggers the `POST /mark-commission-paid` endpoint, updates UI to "Paid" on success.

---

## 5. Development Steps for Claude
1.  **Backend:** Add the `/founder-stats` and `/mark-commission-paid` routes to `server.py`. Ensure they validate the founder token.
2.  **Frontend HTML/CSS:** Create `founder-dashboard.html` strictly following the Void aesthetic rules.
3.  **Frontend JS:** Fetch data from `/founder-stats` on load, populate the KPIs and tables dynamically.
4.  **Interactions:** Wire up the "Mark as Paid" buttons to hit the backend and refresh the row state without a full page reload.

**Claude:** Do not deviate from the design system. Keep borders hairline (1px), use Poppins, and ensure the logo is the SVG file.
