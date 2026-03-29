# Evaluation Rubric — business-case

**Target input:** `evals/business-case/sample-input-01.md`
**Skill under test:** `skills/business-case/SKILL.md`
**Purpose:** Determine whether `business-case` correctly extracts a problem from solution-flavored input, sizes impact honestly with stated assumptions, generates genuine alternatives, produces a complete cost model, and delivers a stress test that adds value beyond the risk assessment.
**Coverage:** Single mode — full skill coverage.

---

## Problem Statement Quality

The input leads with "we should build a self-service cancellation flow" — a solution, not a problem. The business case must translate this back to the underlying problem.

**Good problem statement:** "40% of support tickets are cancellation-related, costing ~480 agent-hours per month, with a CSAT of 2.1/5 for these interactions. Users who signed up in 30 seconds must email support and wait 6 hours to cancel."

**Bad problem statement:** "We need to build a self-service cancellation flow to reduce support burden." (This is a solution masquerading as a problem.)

**Pass:** Problem stated independently from the solution. Quantified with the data provided (2,400 tickets × 12 min = 480 hours/month; CSAT 2.1/5). User perspective included. **Fail:** Problem section leads with or depends on the proposed solution.

---

## Impact Sizing

The input provides enough data for bottom-up sizing but deliberately presents impact vaguely ("save a lot of support time"). The skill must do the actual math.

### Expected sizing approach: Bottom-Up

Current data available:
- 2,400 cancellation tickets/month × 12 min = 480 agent-hours/month
- 8 agents × ~173 hours/month = ~1,384 total agent-hours
- 480/1,384 = ~35% of support capacity consumed by cancellations
- If self-service handles 70-85% of cancellation tickets (reasonable assumption to state), that frees 336-408 agent-hours/month
- At $65K/year per agent (~$31.25/hour fully loaded), that's $10,500-$12,750/month in reclaimed capacity
- Or: could serve same ticket volume with fewer agents, saving 2-3 headcount worth of capacity

### Critical tests:

**The skill must present a range, not a single number.** Conservative (lower adoption rate) / Expected (moderate adoption) / Optimistic (high adoption) with the adoption assumption stated.

**The skill must state the key assumption:** What percentage of cancellation tickets will self-service capture? This is the single most important variable, and it must be named.

**The skill should include strategic value beyond cost savings:** CSAT improvement, user experience quality, competitive expectation (self-service is table stakes in fintech).

**Pass:** Range presented. Adoption rate assumption stated explicitly. Math is correct. Strategic value included alongside quantitative impact. **Fail:** Single number presented. Adoption rate assumed without stating it. "Save a lot of support time" accepted without quantification.

---

## Cost Model Completeness

The input provides no cost estimates. The skill must construct a reasonable model and flag assumptions.

### Expected cost categories:

- **Engineering:** Design + development + QA for mobile-first self-service flow with compliance disclosures. The input mentions compliance requirements (disclosure screens) and mobile-first — both add complexity.
- **Opportunity cost:** The input explicitly names the referral program and analytics dashboard as competing priorities. The cost model must name these.
- **Ongoing maintenance:** Support for edge cases, compliance updates as regulations change, monitoring.
- **Infrastructure:** Minimal for a UI flow, but payment processing integration may have costs.

### Critical tests:

**Opportunity cost must be named.** The input gives this on a platter — referral program and analytics dashboard. If the cost model omits opportunity cost, it failed the most important test.

**Compliance cost must be flagged.** Legal review, disclosure flow implementation, and ongoing compliance maintenance are non-trivial in regulated financial services.

**Pass:** Multi-quarter view. Opportunity cost names the referral program and analytics dashboard. Compliance costs included. Assumptions flagged as needing PM validation. **Fail:** Only engineering build cost. No opportunity cost. Single-quarter view.

---

## Alternatives Quality

The input proposes only one option (build self-service) and doesn't mention alternatives. The skill must generate them.

### Expected alternatives (at minimum):

1. **Build self-service** (the recommendation) — Full flow with compliance
2. **Partial automation** — Automate the identity verification and plan lookup steps but keep a human in the loop for the final cancellation confirmation. Lower compliance risk, faster to build, but doesn't fully eliminate agent time.
3. **Hire more agents** — Address the volume problem with headcount rather than automation. Faster to execute, no engineering cost, but doesn't improve CSAT or user experience.
4. **Do nothing** — Accept current cost and CSAT. Reallocate engineering to referral program or analytics instead.

### Critical tests:

**"Do nothing" must be honestly evaluated.** It's a genuine option — the PM mentioned two other priorities competing for engineering time. "Do nothing on cancellation, build the referral program instead" might be the right answer.

**At least one alternative must have a genuine advantage.** Partial automation is faster and lower compliance risk. Hiring agents has zero engineering cost. These aren't strawmen.

**Pass:** At least 2 genuine alternatives + do nothing. Each has real pros, not just cons. Do nothing evaluated honestly with the competing priorities named. **Fail:** Alternatives are strawmen. Do nothing dismissed in one sentence. Only the recommended option has a positive framing.

---

## Stress Test Novelty

The stress test must surface insights beyond what's already in the risk assessment.

### Expected premortem failure modes (not exhaustive):

- Adoption is lower than expected because users don't discover the self-service flow (discoverability problem)
- Compliance requirements are more complex than expected, causing delays and scope creep
- Users start cancelling more frequently because the friction of contacting support was actually serving as a retention mechanism (this is the non-obvious one)
- Engineering timeline slips and the feature launches after the VP's patience runs out

### Expected blindspots:

- **Retention assumption:** The current friction may be an accidental retention mechanism. Some percentage of users who start the cancellation process and encounter a 6-hour wait may decide not to cancel. Self-service removes that friction — cancellation rates might increase.
- **Data assumption:** The 40% figure and 12-minute average may be rough. What's the source? Is it consistent month over month?

### Critical tests:

**The retention-friction blindspot is the key test.** If the stress test catches that removing cancellation friction might increase cancellation rates, it's working. This is the non-obvious insight that a strong PM would flag.

**Pass:** Premortem has 3+ specific failure modes (not generic). Blindspot catches the retention-friction dynamic or another genuinely non-obvious assumption. Conviction is calibrated (probably 6-8, not 10). **Fail:** Stress test repeats the risk assessment in different words. Blindspot is generic ("we might be wrong about the numbers"). Conviction is 10 with no conditions.

---

## Recommendation Clarity

**Pass:** Recommendation stated directly in the opening line. Reasoning is transparent. Trade-offs (opportunity cost, compliance risk) acknowledged. Confidence level stated with conditions. **Fail:** Recommendation is hedged ("consider building..."). Trade-offs omitted. No confidence level.

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| Problem statement quality | 15% | Problem-first, quantified, solution not smuggled in |
| Impact sizing honesty | 20% | Range presented, bottom-up approach named, adoption assumption explicit, math correct |
| Alternatives genuineness | 15% | 2+ genuine alternatives + do nothing; each with real pros; do nothing honestly evaluated with competing priorities |
| Cost model completeness | 15% | Multi-quarter, opportunity cost names competing priorities, compliance costs included |
| Stress test novelty | 15% | Premortem has specific failure modes; blindspot catches retention-friction dynamic (or equivalent non-obvious insight); conviction calibrated |
| Recommendation clarity | 10% | Stated directly, trade-offs acknowledged, confidence level with conditions |
| Output format compliance | 10% | Matches format; context note present; smell test completed |
