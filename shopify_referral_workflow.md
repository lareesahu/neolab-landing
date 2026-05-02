# Shopify Referral & Coupon Automation Workflow (App-less)

This document outlines a strategy for implementing a creator-led referral program on Shopify without requiring custom apps. It leverages Shopify's native "Discount Links" to automatically apply discounts when customers arrive via a creator's unique referral URL.

## 1. Overview: The "Link-to-Discount" Strategy

The core idea is to connect the `?ref=` parameter on the NeolabCare landing page (`index.html`) directly to a Shopify Discount Link. When a customer clicks a creator's referral link (e.g., `neolab.care/?ref=CREATORNAME`), the landing page detects the `ref` parameter and displays the appropriate messaging (e.g., "Private Creator Access" banner, dynamic pricing).

Crucially, the final Call-to-Action (CTA) on the landing page will direct the customer to the Shopify product page using a **Shopify Discount Link**. This link will automatically apply the pre-configured discount at checkout, ensuring a seamless experience for the customer and accurate tracking for the creator.

## 2. Shopify Setup: Creating the Discount

### Step-by-Step Guide:

1.  **Log in to your Shopify Admin.**
2.  Navigate to **Discounts**.
3.  Click **Create discount**.
4.  Select **Automatic discount**.
5.  **Discount Name:** Give it a clear name (e.g., `CREATOR_LAUNCH_40_PERCENT`).
6.  **Discount Type:** Choose `Percentage`.
7.  **Discount Value:** Enter `40` (for 40% off).
8.  **Applies to:** Select `Specific products` and choose the NeolabCare 30ml and 50ml SKUs.
9.  **Minimum purchase requirements:** Set as needed (e.g., `Minimum purchase amount` of $99).
10. **Customer eligibility:** Select `All customers` or `Specific customer segments` if you have a pre-defined segment for referred customers.
11. **Usage limits:** Set `Maximum number of times this discount can be used` (e.g., `One use per customer`).
12. **Active dates:** Define the start and end dates for the campaign.
13. **Save discount.**

## 3. Generating Shopify Discount Links

Once the automatic discount is created, Shopify will generate a unique URL that applies this discount when clicked.

### How to get the Discount Link:

1.  After saving the automatic discount, you will see a section titled **
### How to get the Discount Link:

1.  After saving the automatic discount, you will see a section titled **Shareable link** or similar. Copy this link.
2.  The link will look something like: `https://yourstore.myshopify.com/discount/CREATOR_LAUNCH_40_PERCENT?redirect=/products/neolabcare-9-in-1-skincare`

## 4. Integrating with the NeolabCare Landing Page (`index.html`)

Currently, the `index.html` page detects the `?ref=` parameter. The next step is to modify the Call-to-Action (CTA) buttons on `index.html` to point to these Shopify Discount Links.

### Implementation Steps:

1.  **Identify CTAs:** Locate all primary CTA buttons on `index.html` that lead to the product purchase (e.g., "Reserve Now," "Get Access").
2.  **Dynamic Link Generation (Frontend):**
    *   When a user lands on `index.html` with a `?ref=CREATORNAME` parameter, store `CREATORNAME` in a JavaScript variable.
    *   Construct the Shopify Discount Link dynamically using this `CREATORNAME`.
    *   Example (pseudo-code):
        ```javascript
        const urlParams = new URLSearchParams(window.location.search);
        const refCode = urlParams.get('ref');

        if (refCode) {
            // Assuming a single discount for all creators for simplicity in Phase 1
            const shopifyDiscountCode = 'CREATOR_LAUNCH_40_PERCENT'; // This should match your Shopify discount
            const shopifyProductUrl = 'https://neolab-care.myshopify.com/products/neolabcare-9-in-1-skincare';
            const discountLink = `${shopifyProductUrl}?discount=${shopifyDiscountCode}`;

            // Update all relevant CTA buttons to point to this discountLink
            document.querySelectorAll('.cta-button').forEach(button => {
                button.href = discountLink;
            });

            // Optionally, you can also append the refCode to the discountLink for tracking purposes in Shopify if you use a custom app for tracking
            // const trackingDiscountLink = `${shopifyProductUrl}?discount=${shopifyDiscountCode}&ref=${refCode}`;
        }
        ```
3.  **Update CTA `href` attributes:** Ensure the `href` attributes of your CTA buttons are updated to use the dynamically generated `discountLink`.

## 5. Tracking & Analytics

While this "app-less" method simplifies discount application, tracking creator performance requires a bit more manual effort or a simple custom solution.

### Options for Tracking:

1.  **Shopify Sales Reports (Manual):**
    *   Filter sales reports by the specific discount code (`CREATOR_LAUNCH_40_PERCENT`). This will show all sales where the discount was applied.
    *   If you create unique discount codes per creator (e.g., `CREATORNAME_40`), you can filter by each creator's code.
2.  **Google Analytics / Shopify Analytics:**
    *   Ensure your Google Analytics is properly set up on both your landing page and Shopify store.
    *   You can track conversions that originate from the `?ref=` parameter by setting up custom dimensions or events.
    *   Shopify Analytics will show sales attributed to specific discount codes.
3.  **Custom Backend for Partner Dashboard:**
    *   For the `partner-dashboard.html` to be functional, you will need a backend system that pulls sales data from Shopify (via API) and attributes it to specific creators based on the `ref` code or unique discount codes.

## Conclusion

This workflow provides a robust, low-overhead solution for launching your creator referral program. By leveraging Shopify's native discount links, you can offer automatic discounts and track sales without immediate reliance on complex third-party apps. As your program scales, you can then consider more advanced API integrations for automated tracking and personalized dashboards.
