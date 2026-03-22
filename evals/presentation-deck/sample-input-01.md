# Presentation Deck Input — Exec Review for Self-Service Cancellation

I need to present the self-service cancellation business case to my VP, Sarah, next Thursday. She has a 30-minute slot and needs to decide whether to fund this for Q2.

---

## The Business Case (summarized)

**Problem:** 40% of our support tickets (2,400/month) are cancellation-related, costing ~480 agent-hours/month at a CSAT of 2.1/5. Users who signed up in 30 seconds must email support and wait 6 hours to cancel.

**Impact:** Bottom-up sizing based on current volume. If self-service captures 75% of cancellation tickets:
- Reclaims ~360 agent-hours/month ($11,250/month in capacity)
- Projected CSAT improvement from 2.1 to 3.8+ for cancellation interactions
- ~$135K/year in reclaimed support capacity
- Strategic: self-service cancellation is table stakes in fintech; we're behind

**Proposed solution:** Mobile-first self-service flow for cancellation, pause, and modification. Includes compliance disclosure screens per legal requirements.

**Cost:** ~$180K estimated (engineering: $120K build + $15K/quarter maintenance, compliance review: $10K, infrastructure: minimal). Opportunity cost: delays referral program by one quarter.

**Risks:**
- Compliance complexity may expand scope (Medium likelihood, High impact)
- Self-service may increase cancellation rates by removing friction (Medium likelihood, Medium impact)
- Engineering estimate may be optimistic for mobile + compliance (Medium likelihood, Medium impact)

**Alternatives considered:**
- Partial automation (faster, lower risk, but doesn't fully solve the problem)
- Hire 2 more agents ($130K/year, no CSAT improvement)
- Do nothing (accept current state, build referral program instead)

**Recommendation:** Build the self-service flow. Payback period is ~16 months on cost savings alone; strategic value (CSAT, competitive positioning) tips the balance. Two-way door — feature flag allows rollback if cancellation rates spike.

---

## What I Know About Sarah

- She's skeptical about projects that increase technical debt — she was burned last quarter when a rushed feature caused a week of production incidents
- She values data-driven arguments over qualitative reasoning
- She'll want to know the impact on our Q2 OKRs (one of which is "reduce support cost per user by 15%")
- She typically asks "what's the biggest risk?" and wants to hear you've thought about it, not that there are no risks
- She decides quickly if the data is clear; she stalls if she feels the analysis is hand-wavy

---

## What I Need

Can you draft a presentation narrative for this exec review? I want to make sure the argument lands. Sarah needs to decide whether to fund this and deprioritize the referral program.
