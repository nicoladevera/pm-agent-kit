# Prioritization Input — Q3 Roadmap Planning

Hey, I need help prioritizing our Q3 roadmap. We have 5 candidates and roughly 2 engineering teams (8 engineers total) for the quarter. Here's what's on the table.

---

## Goal

Our company OKR for H2 is "Increase net revenue retention from 95% to 105%." The VP has also mentioned wanting to "lay the groundwork for enterprise" but that's not a formal OKR — more of a strategic theme she keeps bringing up.

---

## Candidate 1: Smart Notification Engine

**What:** Replace our batch email system with a real-time notification engine — in-app, push, and email — with user-configurable preferences and ML-based send-time optimization.

**Why:** We ran a user feedback synthesis last month. "Too many emails / notification fatigue" was the #2 theme (after "reporting is too slow"). 34% of churned users mentioned notification overload in their exit survey. The CSM team says mid-market accounts are especially vocal about this.

**Evidence:** User feedback synthesis (cross-channel, 6 months of data), exit survey data, CSM qualitative signal.

**Cost estimate:** ~3 engineers for 10-12 weeks. Requires a new messaging infrastructure (we're on a legacy batch system today).

---

## Candidate 2: Reporting Performance Overhaul

**What:** Rebuild the reporting engine for sub-2-second response times on dashboards that currently take 15-30 seconds to load. The #1 complaint in our feedback synthesis.

**Why:** Reporting speed was the #1 theme in our user feedback synthesis. 42% of support tickets about "slowness" trace back to reporting. We've lost 3 competitive deals in the past quarter where the prospect specifically cited reporting speed in their decision.

**Evidence:** User feedback synthesis (#1 theme), support ticket analysis, 3 named lost deals (from CRM), competitive intel showing two competitors market "instant dashboards."

**Cost estimate:** ~4 engineers for 8-10 weeks. Requires database architecture changes (this is partially a tech debt problem — the current schema wasn't designed for the query patterns we now need).

---

## Candidate 3: Self-Serve Enterprise SSO

**What:** Add SAML/OIDC SSO support so enterprise prospects can complete procurement without a manual integration. Currently we handle SSO on a case-by-case basis with engineering involvement.

**Why:** The VP of Product keeps pushing this. She says we're losing enterprise deals because IT teams won't approve us without standard SSO. Sales says 4 deals in the past 2 quarters stalled at procurement because of SSO.

**Evidence:** VP says it's critical. Sales has 4 anecdotal deal losses (no formal win/loss analysis). No user research with enterprise buyers. No data on how many prospects drop off at procurement vs. other stages.

**Cost estimate:** ~2 engineers for 6-8 weeks, but there's a dependency — our auth system needs refactoring first, which is another 3-4 weeks of work.

---

## Candidate 4: API v2 and Developer Platform

**What:** Ship a public REST API (v2) with documentation, rate limiting, and a developer portal. Our current API is internal-only and undocumented.

**Why:** Our CEO got excited about this at a conference. A few power users have asked for API access. There's a vague notion that "platforms always win" and this could open up an integration ecosystem. No business case has been built.

**Evidence:** CEO enthusiasm. 3 feature requests from power users in the past year. No market research, no business case, no sizing of the integration opportunity.

**Cost estimate:** Unknown — nobody's scoped this. The CEO thinks "a few weeks" but the engineering lead estimates 12-16 weeks for a production-quality public API with proper auth, rate limiting, docs, and a developer portal.

---

## Candidate 5: Automated Churn Prediction

**What:** Build an ML model that identifies accounts at risk of churning 30 days before renewal, with automated alerts to CSMs and suggested interventions.

**Why:** Our CSM team currently relies on gut feel for churn risk. They catch about 40% of churn before it happens. If we could increase that to 70%+, the retention impact would be significant — even saving 10% of would-churn accounts is meaningful at our ACV.

**Evidence:** We have 3 years of account health data. The data science team did a quick feasibility study — they believe a predictive model is buildable with reasonable accuracy (AUC > 0.8). No formal business case, but the data team is confident in the technical feasibility.

**Cost estimate:** ~2 engineers + 1 data scientist for 8-10 weeks. The data scientist is a shared resource with the analytics team.

---

## Constraints

- 8 engineers total, but realistically 6-7 are available for new work after maintenance and support rotation
- 1 data scientist, shared with analytics team (maybe 60% availability for product work)
- Q3 is 13 weeks
- We've soft-committed to 2 enterprise prospects that SSO will be available "by end of summer"
- The VP of Product is the key decision-maker; the CEO weighs in on strategic direction

---

## What I Need

Which of these should we build, in what order, and why? I want a clear rationale I can bring to the VP that shows the trade-offs honestly. She'll push on the SSO and enterprise angle — I need to be ready for that conversation.
