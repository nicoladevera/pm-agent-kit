# Apex Pro Launch — Go-to-Market Plan

**Date:** March 2026
**Status:** Draft v1

---

## Market Context

The mid-market B2B analytics space is consolidating. Three competitors have launched premium tiers in the last 18 months, and two of them (DataVault and InsightHub) are pulling enterprise-adjacent customers out of our pipeline. We're seeing it in deal reviews — prospects who would have signed with us a year ago are now asking for capabilities we only offer through custom SOWs: advanced permissioning, dedicated compute, and audit-grade logging.

At the same time, our existing Growth-tier customers are hitting ceilings. The top 15% by usage are generating 40% of support tickets, mostly around rate limits and export restrictions. Three of our largest Growth accounts have asked directly about a higher tier. We've been saying "soon" for two quarters.

The gap is clear: we have a segment of customers who need more than Growth but don't want (or can't afford) a full Enterprise contract. Apex Pro fills that gap.

---

## Product Overview

Apex Pro sits between Growth ($299/mo) and Enterprise (custom pricing). It includes:

- **Advanced permissioning** — role-based access with custom roles, SSO enforcement, and audit logs
- **Dedicated compute** — isolated query processing with guaranteed SLAs (99.9% uptime, <2s p95 query time)
- **Extended data retention** — 24 months vs. Growth's 6 months
- **Priority support** — 4-hour response SLA, named account manager for accounts >$15K ARR
- **API rate limits** — 10x Growth tier limits, burst capacity available

This is not a repackaging of Enterprise. Enterprise includes custom integrations, on-prem deployment options, and dedicated CSM. Apex Pro is self-serve with premium guardrails.

---

## Pricing

Three structures were evaluated:

| Option | Price Point | Rationale |
|--------|------------|-----------|
| Flat rate | $799/mo | Simple, easy to communicate. Risk: underprices heavy-usage customers. |
| Usage-based | $499/mo + compute overages | Aligns cost with value. Risk: unpredictable bills create friction. |
| **Tiered (recommended)** | $699/mo (base) / $999/mo (plus) | Base includes core features; Plus adds dedicated compute and extended SLAs. Captures willingness-to-pay without sticker shock. |

The tiered model was chosen because it mirrors what DataVault and InsightHub charge for comparable capability sets (their mid-tier ranges from $650–$1,100/mo based on public pricing pages). It also gives us an upsell path within Apex Pro itself, which our Growth → Enterprise jump currently lacks.

The base tier targets teams of 10–25 users. The Plus tier targets teams of 25–75 with heavier compute needs. Both include a 14-day free trial with full feature access.

---

## Channel Strategy

Five channels will be activated for the Apex Pro launch:

**Direct sales outreach** — The sales team will run targeted campaigns against existing Growth accounts that meet the Apex Pro ICP: >$5K current ARR, >10 active users, and at least one support ticket about rate limits or permissions in the last 90 days.

**Product-led growth** — In-app upgrade prompts when Growth users hit rate limits, attempt to create custom roles, or exceed retention windows. Contextual, not interruptive.

**Partner channel** — Our three SI partners (Meridian, Cloudbridge, Northpoint) will include Apex Pro in their implementation packages. Enablement materials needed.

**Events** — Apex Pro will be featured at DataConnect (April) and AnalyticsSummit (June). Both events draw our target buyer.

**Content marketing** — Thought leadership series on "scaling analytics teams without scaling costs." Blog posts, one gated whitepaper, case study from beta customer.

---

## Timeline

| Phase | Dates | Key Activities |
|-------|-------|---------------|
| Beta | March 15 – April 15 | 8 hand-selected accounts, usage monitoring, feedback sessions |
| Soft launch | April 16 – April 30 | Open to existing Growth accounts via invite |
| GA | May 1 | Public launch, all channels activated |
| Post-launch review | May 15 | Metrics review, channel performance, tier mix analysis |

---

## Risks

- **Cannibalization** — Some Enterprise prospects may choose Apex Pro instead, reducing average deal size. Mitigation: clear feature differentiation and sales team training on positioning.
- **Support load** — Priority support SLA may strain current team. Mitigation: hire two additional support engineers before GA (req approved, sourcing in progress).
- **Beta feedback scope** — If beta customers surface feature gaps, we may need to delay GA. Acceptance: delay is acceptable up to 2 weeks; beyond that, launch with known gaps and a published roadmap.
