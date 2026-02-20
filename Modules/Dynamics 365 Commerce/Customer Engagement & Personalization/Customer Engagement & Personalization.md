# Customer Engagement & Personalization Module - Knowledge Source

> This file is the central knowledge hub for **Customer Engagement & Personalization** within Dynamics 365 Commerce.

---


---


> **Microsoft Learn Reference:** [Customer Engagement & Personalization](https://learn.microsoft.com/en-us/dynamics365/commerce/personalized-recommendations)

## Module Overview

Customer engagement and personalization capabilities in Dynamics 365 Commerce provide AI-driven product recommendations, personalized content, customer segmentation, and targeted marketing. These features leverage customer data to deliver tailored shopping experiences across all commerce channels.

### Key Capabilities

| Capability | Description |
|------------|-------------|
| **Product Recommendations** | AI-powered recommendations (similar, trending, frequently bought together) |
| **Personalized Content** | Deliver targeted content based on customer segments and behavior |
| **Customer Segmentation** | Create customer segments based on purchase history and attributes |
| **Ratings & Reviews** | Enable customer ratings and reviews for products |
| **Wish Lists** | Allow customers to save items for future purchase |
| **Email Marketing Integration** | Connect with email marketing for personalized campaigns |
| **Customer Insights Integration** | Leverage Dynamics 365 Customer Insights for unified customer profiles |
| **A/B Testing** | Test different content and promotion strategies for optimization |

---

## 📁 Folder Contents

### Data Migration Framework (DMF) Templates

> **No DMF templates exist for this module.** Personalization features are configured through Commerce headquarters and site builder.

---

### Process Catalogue References

- **Process Catalogue (JSON):** `../../../Business Process/ProcessCatalogue.json`
- **Process Catalogue (Flat):** `../../../Business Process/ProcessCatalogue_flat.json`

Key Customer Engagement & Personalization-related business process areas:
- **Product recommendations** (AI-driven personalization)
- **Customer loyalty programs** (loyalty schemes, earn/redeem)
- **Customer attributes & segmentation** (targeted marketing)
- **Clienteling** (in-store customer engagement)

---

## Microsoft Learn Sources

### Primary Learning Path

| Resource | URL |
|----------|-----|
| **Work with customer engagement features in Dynamics 365 Commerce** | https://learn.microsoft.com/en-us/training/paths/work-customer-engagement-commerce/ |

### Additional Documentation

| Resource | URL |
|----------|-----|
| Product recommendations overview | https://learn.microsoft.com/en-us/dynamics365/commerce/product-recommendations |
| Enable product recommendations | https://learn.microsoft.com/en-us/dynamics365/commerce/enable-product-recommendations |
| Personalized recommendations | https://learn.microsoft.com/en-us/dynamics365/commerce/personalized-recommendations |
| "Shop similar looks" recommendations | https://learn.microsoft.com/en-us/dynamics365/commerce/shop-similar-looks |
| Loyalty overview | https://learn.microsoft.com/en-us/dynamics365/commerce/set-up-customer-loyalty-program |
| Loyalty schemes and reward points | https://learn.microsoft.com/en-us/dynamics365/commerce/loyalty-schemes |
| Customer attributes | https://learn.microsoft.com/en-us/dynamics365/commerce/dev-itpro/customer-attributes |
| Clienteling | https://learn.microsoft.com/en-us/dynamics365/commerce/clienteling-overview |
| Gift cards | https://learn.microsoft.com/en-us/dynamics365/commerce/gift-card |
| Affiliations and customer groups | https://learn.microsoft.com/en-us/dynamics365/commerce/affiliations-overview |
| Email marketing integration | https://learn.microsoft.com/en-us/dynamics365/commerce/email-marketing |

---

## 4-Phase Configuration Sequence

### Phase 1: Prerequisites

| Prerequisite | Menu Path | Purpose |
|--------------|-----------|---------|
| Commerce channels | Retail and Commerce > Channels | Active retail channels |
| Customer master | Accounts receivable > Customers | Customer records |
| Product catalog | Retail and Commerce > Catalogs | Published product catalogs |
| Azure AI service | Azure portal | For AI-driven recommendations |

### Phase 2: Loyalty Program Setup

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Loyalty programs | Retail and Commerce > Customers > Loyalty > Loyalty programs | Program definitions |
| Loyalty schemes | Retail and Commerce > Customers > Loyalty > Loyalty schemes | Earn/redeem rules |
| Reward points | Retail and Commerce > Customers > Loyalty > Reward points | Point type definitions |
| Loyalty tiers | (Within loyalty program) | Tier levels (Silver, Gold, etc.) |
| Loyalty cards | Retail and Commerce > Customers > Loyalty > Loyalty cards | Card number sequences |

### Phase 3: Personalization & Recommendations

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Enable recommendations | Commerce > Product recommendations > Enable | Turn on AI recommendations |
| Configure recommendation lists | Commerce > Product recommendations > Recommendation lists | Trending, picks for you, etc. |
| Customer attributes | (Within customer or channel setup) | Custom attribute definitions |
| Affiliations | Retail and Commerce > Customers > Affiliation | Customer grouping for pricing |
| Clienteling settings | (Within POS functionality profile) | Enable clienteling in POS |

### Phase 4: Distribution & Activation

| Task | Menu Path | Purpose |
|------|-----------|---------|
| Run distribution schedule | Retail and Commerce > IT > Distribution schedule | Sync loyalty and customer data |
| Configure email triggers | Commerce > Email notifications | Loyalty and marketing emails |
| Gift card setup | Retail and Commerce > Products > Gift cards | Digital/physical gift cards |

---

## Loyalty Program Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                     LOYALTY PROGRAM ARCHITECTURE                         │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│  LOYALTY PROGRAM (e.g., "Rewards Club")                                  │
│  ┌─────────────────────────────────────────────────────────┐            │
│  │                                                           │            │
│  │  LOYALTY SCHEMES                                          │            │
│  │  ┌───────────────────────────────────────────┐           │            │
│  │  │ Earn Rules:                                 │           │            │
│  │  │  • 1 point per $1 spent                     │           │            │
│  │  │  • 2x points on specific categories          │           │            │
│  │  │  • Bonus points on promotions                │           │            │
│  │  │                                              │           │            │
│  │  │ Redeem Rules:                                │           │            │
│  │  │  • 100 points = $1 discount                  │           │            │
│  │  │  • Point thresholds for rewards              │           │            │
│  │  └───────────────────────────────────────────┘           │            │
│  │                                                           │            │
│  │  TIERS                                                    │            │
│  │  ┌─────────┐  ┌──────────┐  ┌────────────┐              │            │
│  │  │ Bronze   │  │ Silver    │  │ Gold        │              │            │
│  │  │ 0 pts    │  │ 500 pts   │  │ 2000 pts    │              │            │
│  │  │ 1x earn  │  │ 1.5x earn │  │ 2x earn     │              │            │
│  │  └─────────┘  └──────────┘  └────────────┘              │            │
│  │                                                           │            │
│  │  CHANNELS: All stores, Online, Call center                │            │
│  └─────────────────────────────────────────────────────────┘            │
│                                                                          │
│  AI RECOMMENDATIONS                                                      │
│  ┌─────────────────────────────────────────────────────────┐            │
│  │ • "Trending" — Popular products                           │            │
│  │ • "Picks for you" — Personalized per customer             │            │
│  │ • "Frequently bought together" — Basket analysis          │            │
│  │ • "Shop similar looks" — Visual AI                        │            │
│  │ • "People also like" — Collaborative filtering            │            │
│  └─────────────────────────────────────────────────────────┘            │
│                                                                          │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Key Menu Items

| Menu Item Name | Display Text | Category |
|----------------|--------------|----------|
| `RetailLoyaltyPrograms` | Loyalty programs | Loyalty |
| `RetailLoyaltySchemes` | Loyalty schemes | Loyalty |
| `RetailLoyaltyRewardPoints` | Reward points | Loyalty |
| `RetailLoyaltyCards` | Loyalty cards | Loyalty |
| `RetailProductRecommendations` | Product recommendations | Personalization |
| `RetailAffiliation` | Affiliations | Customer |
| `RetailClienteling` | Clienteling | POS |
| `RetailGiftCard` | Gift cards | Products |

---

## Critical Configuration Rules

### ⚠️ Sequence Dependencies

1. **Loyalty program** must exist before schemes can be created
2. **Reward point types** must be defined before earn/redeem rules
3. **Loyalty schemes** must be associated with channels
4. **Loyalty cards** must be issued (or auto-generated) for customers to earn
5. **AI recommendations** require Azure AI service and sufficient transaction data
6. **Distribution schedule** must be run after any loyalty configuration changes
7. **Clienteling** requires POS functionality profile configuration

### ⚠️ Common Errors

| Error | Cause | Resolution |
|-------|-------|------------|
| "Loyalty card not found" | Card not issued or not synced | Issue card and run distribution |
| "Points not earned" | Scheme not active or channel mismatch | Verify scheme activation and channel |
| "Recommendations not showing" | Insufficient data or service not enabled | Enable service and wait for model training |
| "Tier upgrade not applied" | Tier evaluation not run | Run loyalty tier evaluation batch |
| "Gift card balance error" | Card not activated or depleted | Check card status and balance |

---

## Business Process Catalogue Reference

> Cross-reference with the **Business Process Catalogue** — showing end-to-end processes that involve the **Customer Engagement & Personalization** module.

### Order to cash

*73 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze sales performance | 1 | — |
| Develop sales policies | 15 | — |
| Manage accounts receivable | 20 | — |
| Manage credit and collections | 2 | — |
| Manage sales orders | 35 | — |

### Concept to market

*13 related process items identified in the Business Process Catalogue.*

| Process Area | Item Count | Sample Reference |
|-------------|-----------|-----------------|
| Analyze marketing operations | 2 | — |
| Manage marketing campaigns | 10 | — |
| Prepare marketing campaigns | 1 | — |

