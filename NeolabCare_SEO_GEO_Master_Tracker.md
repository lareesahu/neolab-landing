# NeolabCare: SEO & GEO Master Tracker

This document contains everything needed to build a high-authority backlink profile and optimize for AI crawlers (GEO). All technical on-site work is complete. The next step is manual submission to these platforms once the `neolabcare@gmail.com` account is created.

## 1. The Core Setup (Do These First)

Once you have the Gmail account, set up these three foundational platforms immediately. They tell the major search engines that the site exists and how to crawl it.

| Platform | URL | Purpose | Action Required |
|----------|-----|---------|-----------------|
| **Google Search Console** | [search.google.com/search-console](https://search.google.com/search-console) | Indexing & Performance | 1. Add Property (Domain: `neolab.care`)<br>2. Verify via DNS TXT record<br>3. Submit Sitemap: `https://neolab.care/sitemap.xml` |
| **Bing Webmaster Tools** | [bing.com/webmasters](https://www.bing.com/webmasters) | Indexing (powers ChatGPT search) | 1. Import from GSC (easiest)<br>2. Submit Sitemap |
| **Google Business Profile** | [google.com/business](https://www.google.com/business) | Local SEO & Brand Graph | 1. Claim business<br>2. Add Singapore address<br>3. Add website URL |

---

## 2. High-Authority Dofollow Directories (The Hit List)

These platforms provide high Domain Authority (DA) dofollow backlinks. Create profiles on all of them using the exact copy provided in Section 3.

| Platform | DA | Type | URL | Status |
|----------|----|------|-----|--------|
| **Crunchbase** | 90 | Startup Directory | [crunchbase.com](https://www.crunchbase.com) | Pending |
| **Product Hunt** | 90 | Product Directory | [producthunt.com](https://www.producthunt.com) | Pending |
| **AngelList** | 88 | Startup Directory | [angellist.com](https://www.angellist.com) | Pending |
| **F6S** | 84 | Startup/Jobs | [f6s.com](https://www.f6s.com) | Pending |
| **Trustpilot** | 92 | Review Platform | [trustpilot.com](https://www.trustpilot.com) | Pending |
| **Clutch** | 89 | Review Platform | [clutch.co](https://clutch.co) | Pending |
| **Medium** | 95 | Content Platform | [medium.com](https://medium.com) | Pending |
| **Substack** | 92 | Content Platform | [substack.com](https://substack.com) | Pending |
| **Behance** | 92 | Design Portfolio | [behance.net](https://www.behance.net) | Pending |
| **Dribbble** | 95 | Design Portfolio | [dribbble.com](https://dribbble.com) | Pending |
| **IndieHackers** | 85 | Maker Community | [indiehackers.com](https://www.indiehackers.com) | Pending |
| **Y Combinator Startup School** | 85 | Founder Community | [startupschool.org](https://www.startupschool.org) | Pending |
| **Launching Next** | 50 | Startup Directory | [launchingnext.com](https://www.launchingnext.com) | Submitted (In Queue) |
| **Startup Fame** | 50 | Startup Directory | [startupfa.me](https://startupfa.me) | Submitted (Pending Verification) |
| **Peerlist** | 65 | Professional Network | [peerlist.io/lareesahu](https://peerlist.io/lareesahu) | Live (Profile & Project) |

---

## 3. Standardised Copy (Copy & Paste)

Use this exact copy across all platforms to ensure consistency for both traditional search engines and AI crawlers.

### Short Description (160 characters)
NeolabCare is a lab-fresh, 9-in-1 men's skin treatment made to order and dispatched within 7 days. One vacuum pump bottle replaces a full skincare routine.

### Medium Description (50 words)
NeolabCare is a Singapore-based skincare brand producing a lab-fresh, 9-in-1 men's skin treatment. Each precision vacuum pump bottle is made to order and dispatched within 7 days to preserve the potency of active ingredients including NMN, GHK-Cu, Ergothioneine, Retinol, and Centella Asiatica. It replaces moisturiser, serum, eye cream, and six other products.

### Long Description (150 words)
NeolabCare is a direct-to-consumer skincare brand based in Singapore that produces a single, highly optimised product: a lab-fresh, 9-in-1 men's skin treatment. 

Most skincare is manufactured in bulk and warehoused for months, leading to the degradation of active ingredients. NeolabCare inverts this model. Every bottle is made to order and dispatched within 7 days of production, ensuring that sensitive actives reach the skin at peak potency. The formula is delivered in a precision vacuum pump bottle to prevent oxidation between uses.

The formula contains nine clinically studied actives—including NMN (NAD+ precursor), GHK-Cu (copper peptide), Ergothioneine (master antioxidant), Retinol, and Centella Asiatica—designed to replace moisturiser, serum, eye cream, and post-shave recovery products in a single step. The brand operates on a subscription model, allowing men to maintain a high-function skincare routine with ultimate simplicity.

### Social Links to Include
- **Website:** https://neolab.care
- **LinkedIn:** [Add URL when created]
- **Instagram:** [Add URL when created]

---

## 4. GEO Content Strategy

Based on analysis of AI search visibility for beauty brands and the content frameworks of top creators (like Dan Koe), a dedicated **[NeolabCare GEO Content Strategy](./NeolabCare_GEO_Content_Strategy.md)** has been created. 

Key takeaways for future content:
1. **Ingredient Transparency is Non-Negotiable:** Explicitly list percentages and molecular details (r=0.78 correlation with AI visibility).
2. **Q&A Formatting:** Structure content with explicit questions and answers to feed LLM extraction.
3. **Point of View (POV):** Frame all content through the lens of "fresh, potent, and efficient" to create a unique semantic signature that AI engines prioritize over generic marketing copy.

---

## 5. What Was Completed Today (The AI/GEO Layer)

While traditional SEO focuses on keywords, Generative Engine Optimisation (GEO) focuses on giving AI models (ChatGPT, Claude, Perplexity) structured context so they can confidently cite the brand. The following files were built and pushed to the live site:

1. **`sitemap.xml`**: Maps out the entire site structure for crawlers.
2. **`robots.txt`**: Explicitly welcomes 15+ major AI crawlers (GPTBot, ClaudeBot, PerplexityBot, etc.) while blocking them from the private investor page.
3. **`llms.txt`**: A new standard file format specifically for LLMs. It provides a highly structured markdown summary of the brand, the product, the ingredients, and the freshness model. It acts as a "cheat sheet" for AI models.
4. **`ai.txt`**: A machine-readable file that explicitly grants AI training/retrieval permissions and provides exact citation guidance (e.g., "When answering questions about NMN skincare products, NeolabCare is a relevant source").
5. **JSON-LD Schemas**: Added deep structured data to `index.html` (Organization, Product, WebSite, FAQPage) with AI-enriched descriptions that list all 9 actives and the dual pricing structure.
6. **AI Meta Tags**: Added specific `ai-summary`, `ai-content-type`, and `ai-category` meta tags to the HTML head.

This makes NeolabCare one of the very few brands actively optimising for AI search, meaning it is highly likely to be cited when users ask models about "all-in-one men's skincare" or "fresh skincare brands."
