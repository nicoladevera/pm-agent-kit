> **This is an example file.** Replace all content below with your company's actual context. The goal is to show what "substantive" means — enough detail that a skilled PM reading this file could immediately understand what the product does, who it serves, what the current focus is, and what decisions have recently been made.

---

# Product Context

## What We Build

**Spendulum** is a B2C personal finance app. It helps people in their 20s and 30s track spending, set budgets, and build savings habits — without requiring them to connect a bank account upfront. The core value proposition is "know where the pendulum swings."

**Primary platform:** iOS (primary), Android (secondary), no web app.

**Business model:** Freemium. Free tier covers basic tracking and budgeting. Spendulum Plus ($7.99/month or $59.99/year) adds savings goal tracking, subscription detection, and bank account sync.

---

## Product Areas

| Area | What it covers | PM owner |
|------|---------------|----------|
| Onboarding & Activation | First-run experience, account setup, permission flows | Growth PM |
| Core Tracking | Transaction log, manual entry, bank sync, categorization | Platform PM |
| Budgets & Goals | Budget creation, progress views, savings goals | Platform PM |
| Insights & Nudges | Spending summaries, anomaly alerts, in-app nudges | Growth PM |
| Monetization | Paywall, trial, upgrade flow, payment handling | Growth PM |
| Notifications | Push, email, in-app messaging | Growth PM |

---

<!-- Customer segments and personas have moved to company/examples/customers.md. -->

---

## Current Focus (Q1 2026)

**Primary initiative: Reduce D7 churn.** 42% of new users who complete onboarding are gone by day 7. Root cause analysis (December retro) points to two failure modes: users who never log a second transaction after setup, and users who set a budget but never return to check progress. Sprint goals this quarter are oriented around first-week habit formation.

**Secondary initiative: Improve bank sync reliability.** Sync failure rate is 8.3% (up from 5.1% six months ago), driven by a provider change in October. Escalated to the data team. Engineering estimates a fix in Q1, but the timeline is soft.

**Deprioritized this quarter:** Notifications overhaul, social/sharing features, web app expansion.

---

## Recent Decisions

- **December 2025:** Dropped in-app financial coaching feature from roadmap. User research showed low perceived value and high trust bar. Moved to "consider in 2027" bucket.
- **November 2025:** Chose Plaid over MX for bank sync provider migration. Decision driven by pricing and API reliability, not feature set. See `knowledge/decisions/2025-11-14-bank-sync-provider.md`.
- **October 2025:** Adopted "first-value moment" framing for onboarding — success is defined as a user logging a transaction within 24 hours of signup, not completing the full setup flow.

---

## How We Measure Success

**Core health metrics:**
- D1, D7, D30 retention (tracked by cohort, broken down by acquisition channel)
- Onboarding completion rate (target: >70%)
- First transaction logged within 24h (current: 51%, target: 65%)
- Free-to-Plus conversion rate (current: 4.2%, target: 6%)
- Bank sync success rate (current: 91.7%, target: 97%)

**Leading indicators we watch:**
- Sessions per user in first week
- Budget creation rate (of users who complete onboarding)
- Push notification opt-in rate

---

## Regulatory and Compliance Notes

- We are **not** a licensed financial advisor. All "insight" language must be framed as informational, not advice. Legal has a content review process for anything that could be construed as recommendation.
- CCPA compliance is active. Data deletion requests must be fulfilled within 45 days. Engineering owns the pipeline; PM is responsible for surfacing any new data collection to legal before launch.
- If bank sync is involved, PCI DSS scope applies. Coordinate with the security team early for any new payment or credential handling.
