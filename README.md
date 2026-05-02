# NeolabCare Landing Page - Developer Handover

This repository contains the frontend assets for the NeolabCare landing page, designed with a "Void" luxury aesthetic. It is structured to support a Phase 1: Creator-Led Private Launch, incorporating referral-aware functionality and a dedicated Creator Partner application portal.

## Project Structure

- `index.html`: The main landing page, featuring dynamic content based on referral parameters.
- `investors.html`: The investor overview page, updated with detailed unit economics and scalability insights.
- `creator-partner.html`: The application portal for Creator Partners.
- `partner-dashboard.html`: A placeholder for the Creator Partner dashboard.
- `assets/`: Contains images, fonts, and other static assets.

## Design System: "Void" Luxury Aesthetic

The project adheres to a minimalist, high-contrast "Void" aesthetic. Key design tokens (colors, typography, spacing) are defined in the `<style>` block of each HTML file. Developers should maintain this consistency across all new additions.

## Referral Logic (`index.html`)

The `index.html` page is designed to be referral-aware. It checks for a `?ref=` query parameter in the URL. If present, it triggers:

1.  A "Private Creator Access" banner.
2.  Dynamic pricing adjustments (though the backend integration for this is pending).

**Integration Point:** The `?ref=` parameter is intended to be linked with Shopify's discount functionality. When a user arrives via a creator's referral link (e.g., `neolab.care/?ref=CREATORNAME`), a pre-configured Shopify discount should be automatically applied at checkout.

## Creator Partner Application (`creator-partner.html`)

This page provides a form for potential Creator Partners to apply. 

**Integration Point:** The form currently acts as a frontend shell. To capture applications, it needs to be connected to a backend system (e.g., a CRM, email marketing platform like Klaviyo/Mailchimp, or a simple database like Airtable/Google Sheets). The form submission logic needs to be implemented.

## Partner Dashboard (`partner-dashboard.html`)

This is a placeholder page intended for Creator Partners to track their referrals and earnings.

**Integration Point:** This page requires significant backend development to pull data from Shopify (sales attributed to specific referral codes) and present it to the respective creators. User authentication and data security will be critical for this section.

## Shopify Integration (Next Steps)

To fully enable the referral program and dynamic pricing:

1.  **Shopify Discount Links:** Configure Shopify to generate unique "Discount Links" that automatically apply a discount when clicked. These links should incorporate the `?ref=` parameter logic.
2.  **Product Page:** The main product page is located at: `https://neolab-care.myshopify.com/products/neolabcare-9-in-1-skincare`.
3.  **API Connections:** For advanced features like real-time dashboard data or automated coupon generation, consider using Shopify's API for custom integrations.

## Developer Guidelines

-   **Maintain "Void" Aesthetic:** Adhere strictly to the established design system.
-   **Mobile-First Development:** Ensure all new features are fully responsive.
-   **Performance:** Optimize assets and code for fast loading times.
-   **Security:** Implement secure practices, especially when handling user data or API keys.

For any questions or further development, please refer to this documentation and the inline comments within the HTML files.
