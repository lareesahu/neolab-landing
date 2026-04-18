# Investor Deck Page — NeolabCare (`investors.html`)

## Context
NeolabCare LLC (US-incorporated), pre-launch prestige skincare startup. World's first lab-fresh, 9-in-1 skin treatment on a subscription model. Raising **$500K–$1M** (pre-seed/angel). Page is **unlisted** (no nav link), investor contact via **embedded form** → Web3Forms.

---

## Stack & Brand
- Pure HTML + CSS + vanilla JS. New file: `investors.html`
- Fonts: Poppins + Noto Serif Display (same Google Fonts link)
- Colors: `--bg:#0A0A0A` · `--accent:#C8B89A` · `--text:rgba(245,245,240,.94)` · `--layer:#141414` · `--border:rgba(200,184,154,.10)`
- Patterns: section numbers, `.rv` scroll-reveal, `.lbl` labels, `.rule` gold dividers, `.h-section` italic serif headings, stat cards, comparison grid — **exact same classes as index.html**

---

## 10 Sections

| # | Section | Key Content |
|---|---|---|
| 01 | **Hero** | "The $60B skincare market has a freshness problem." · 3 stat cards: $60B market, 43% CAGR, $299 AOV · dual CTAs |
| 02 | **The Problem** | 5–7 product routines + ingredient degradation · 3 pain cards: Complexity, Degradation, No Subscription Intelligence |
| 03 | **The Solution** | 9-in-1 · made-to-order · GMP · vacuum pump · differentiator chips (same `.fn-chip` pattern) |
| 04 | **Market (TAM/SAM/SOM)** | TAM $60B · SAM $17B men's skincare (8.4% CAGR) · SOM $850M subscription · "Why Now" callout |
| 05 | **Traction** | 100% 5-star beta ratings · 3 testimonials (Daniel, Cong Huang, Murray) · Indiegogo badge · GMP badge |
| 06 | **Business Model** | AOV $299 · COGS ~$60–80 · >75% gross margin · LTV $1,196 · CAC <$80 · Payback <1 month |
| 07 | **Competitive Moat** | `.cmp-grid` comparison: The Market vs NeolabCare · 4 moat pillars |
| 08 | **Roadmap** | `.ft-line` timeline: Q2 2026 → Q3 2026 → Q4 2026 → 2027 |
| 09 | **Team** | Placeholder founder cards + trust badges: GMP Certified · Peer-Reviewed · Indiegogo Backed |
| 10 | **The Ask** | "Raising $500K–$1M" · 3 use-of-proceeds items · embedded contact form → Web3Forms |

---

## Reused Patterns (no new CSS invented)
- All CSS variables from `index.html`
- `.rv/.rvl/.rvr` + IntersectionObserver JS (fire-once, threshold 0.06)
- `.lbl`, `.rule`, `.h-section`, `.body-lg`, `.sec`, `.wrap`, `.sec-num`
- `.fn-chip` → solution differentiators
- `.ft-line/.ft-node` → roadmap timeline
- `.cmp-grid/.cmp-card` → competitive moat
- `.testimonial-card` → traction quotes
- Stat card: big `3rem` gold number + `11px` uppercase label
- Web3Forms key: `fe35df41-5c1c-4519-9513-f9a227fcffe4`

---

## Files
- **Create:** `/home/user/neolab-landing/investors.html`
- **Reference only:** `index.html`, `dashboard.html`, `feedback.html`
- **No changes** to `index.html` (page is unlisted)
