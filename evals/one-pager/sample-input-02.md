# One-Pager Input — API Integration Business Case Compression

I wrote a business case for a new partner API integration and it's in pretty good shape. But now I need a one-pager version of it for the Head of Partnerships — she's not going to read a 4-page business case, but she needs to understand the opportunity well enough to give me feedback on whether her team would want to co-invest engineering resources from their side.

**Audience:** Head of Partnerships
**Ask:** Feedback — would her team want to co-invest?

Here's the business case:

---

## Business Case: Partner API Integration — Vendor Catalog Sync

**Status:** Draft
**Date:** 2026-03-15
**Recommendation:** Invest in a bi-directional API integration with VendorHub's catalog system to eliminate manual data entry for the 340+ customers who use both platforms.

### Problem / Opportunity

Customers who use both our platform and VendorHub (our most common adjacent tool — 38% of accounts with 50+ seats) currently maintain product catalogs in both systems manually. This creates three measurable problems:

1. **Data entry duplication:** Customers report 4-6 hours/week of manual catalog sync work per location. For multi-location operators (avg 3.2 locations for VendorHub overlap accounts), this compounds to 12-19 hours/week.
2. **Data drift:** Manual sync leads to discrepancies. Our support data shows 23% of catalog-related support tickets from VendorHub users cite "inventory counts don't match what VendorHub shows." These tickets take 2.3x longer to resolve than average because the root cause is always a sync mismatch that requires checking both systems.
3. **Competitive vulnerability:** Two competitors (FreshTrack and InventoryPro) launched VendorHub integrations in Q4 2025. Three churned accounts in Q1 2026 cited "better integration with our existing tools" as the primary reason for switching. Our win/loss data from sales shows "integrations" as the #2 objection in enterprise deals, after pricing.

The overlap segment (340+ accounts) represents $2.1M in ARR and has 15% higher expansion revenue potential than non-overlap accounts (based on seat growth trajectory).

### Impact Sizing

**Approach:** Bottom-up from existing customer data

| Dimension | Conservative | Expected | Optimistic | Assumptions |
|-----------|-------------|----------|------------|-------------|
| Retention improvement | 2% reduction in churn for overlap segment | 4% reduction | 6% reduction | Based on "integration" being a top-3 churn reason |
| ARR protected | $42K/yr | $84K/yr | $126K/yr | Applied to $2.1M overlap ARR |
| Support cost reduction | 15% fewer catalog tickets | 25% fewer | 35% fewer | VendorHub users generate 340 catalog tickets/quarter |
| Expansion revenue | $50K incremental | $100K incremental | $150K incremental | Based on reduced friction enabling upsell conversations |
| New customer acquisition | 5 deals/yr unblocked | 10 deals/yr | 15 deals/yr | Based on "integrations" as #2 sales objection |

**Expected total annual impact:** $280K-$460K (retention + support savings + expansion + new deals)

### Proposed Solution

Bi-directional API integration with VendorHub's catalog system:
- **Inbound sync:** VendorHub catalog changes (new items, price updates, discontinued items) automatically reflected in our system
- **Outbound sync:** Inventory count updates from our system pushed to VendorHub
- **Conflict resolution:** When both systems update the same field, use timestamp-based resolution with manual review queue for conflicts
- **Scope:** Catalog items, pricing, inventory counts. Out of scope: purchase orders, vendor contacts, invoicing.

Depends on VendorHub's Partner API (currently in beta, GA expected Q2 2026). We'd be an early integration partner, which may provide co-marketing benefits.

### Cost Model

| Cost Category | One-Time | Ongoing (Quarterly) | Notes |
|---------------|----------|---------------------|-------|
| Engineering | 6-8 weeks (2 engineers) | 0.5 engineer for maintenance | Assumes VendorHub API is stable at GA |
| Infrastructure | $2K setup | $500/quarter | API hosting, webhook infrastructure |
| Opportunity cost | Delays notification system by 3-4 weeks | — | Notification system is P1, not P0 |
| QA/Testing | 2 weeks | Included in maintenance | Integration testing with VendorHub sandbox |

**Total estimated investment:** $80K-$110K (engineering time + infra), ongoing ~$15K/quarter

### Risk Assessment

| Risk | Category | Likelihood | Impact | Mitigation |
|------|----------|-----------|--------|------------|
| VendorHub API delays beyond Q2 | Technical | Medium | High | Build against beta API; scope initial release to inbound-only if outbound isn't ready |
| Low customer adoption of sync feature | Adoption | Low | Medium | 340+ accounts already use both tools — the demand signal is strong; beta with top 10 overlap accounts |
| API rate limits constrain multi-location sync | Technical | Medium | Medium | Batch sync architecture; negotiate higher limits as early partner |
| VendorHub changes API without notice | Technical | Low | High | Version pinning, webhook monitoring, contractual API stability clause |

**Reversibility:** Two-way door — integration can be turned off without data loss. Customer catalogs remain in both systems independently.

### Alternatives Considered

**Option A: Build the integration (Recommended)** — Full bi-directional sync. Addresses all three problems. Highest ROI but requires VendorHub API dependency.

**Option B: CSV import/export tool** — Manual but structured data transfer. Lower cost (~2 weeks engineering). Reduces data entry time but doesn't eliminate drift or real-time sync. Verdict: Right as a stopgap if VendorHub API is delayed beyond Q3, but not the target solution.

**Option C: Do nothing** — Accept the manual workflow. Competitive gap widens as FreshTrack and InventoryPro integrations mature. Churn risk increases. Verdict: Viable only if VendorHub overlap segment stops growing — but it's our fastest-growing segment.

### Recommendation

Build the bi-directional integration, starting with inbound sync (VendorHub → us) and adding outbound sync when VendorHub's API supports it. The overlap segment is large ($2.1M ARR), growing, and increasingly at risk. Two competitors have already moved. The investment is moderate (6-8 weeks) relative to the ARR protected and the competitive positioning value.

### Stress Test

#### Premortem
1. VendorHub's API never reaches GA — we've invested 6-8 weeks against a beta that gets abandoned. Mitigation: inbound-only scope is still valuable on its own and uses only publicly available data feeds.
2. Customers don't adopt because they've built their own sync workflows (spreadsheets, scripts). Mitigation: beta with 10 accounts to validate demand before full rollout.
3. Integration quality issues (sync conflicts, data corruption) damage trust with high-value accounts. Mitigation: conflict resolution queue with manual review; staged rollout.

#### Blindspot Check
- **Market assumption:** We assume VendorHub will remain the dominant adjacent tool. If a competitor displaces VendorHub, this integration loses value.
- **Data assumption:** The 38% overlap figure comes from self-reported CRM data, not system-level verification. Actual overlap may be higher or lower.

#### Conviction
**Confidence level:** 7/10 — Strong demand signal (overlap size, churn data, sales objections). Main uncertainty is VendorHub API timeline. What would lower confidence: VendorHub API delayed past Q3, or overlap segment growth flattens.
