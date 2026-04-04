# Evaluation Rubric — business-case (Consumer Marketplace: Price Guarantee)

**Target input:** `evals/business-case/sample-input-02.md`
**Skill under test:** `.claude/skills/business-case/SKILL.md`
**Purpose:** Determine whether `business-case` correctly flips the solution-first input to a problem-first frame, builds a cost model that includes guarantee liability, surfaces the retention-friction blindspot, and treats the "do nothing" alternative honestly.

**Coverage:** Single mode — full skill coverage.

---

## Problem-First Translation

The PM leads with the solution ("We should build a Best Price Guarantee"). The business case must translate this back to the underlying problem.

**Good problem statement:** "Booking leakage — customers discovering pros on-platform and then contracting directly — is the #3 cited reason for non-return among churned customers (31% of survey respondents). With $24M GMV and 23% repeat booking rate, each percentage point of repeat-booking erosion represents approximately $[X] in foregone annual GMV. The platform is functioning as a discovery layer rather than a transaction layer for a meaningful share of its highest-value customers."

**Bad problem statement:** "We need to build a Best Price Guarantee to stop customers from going around us." (This is a solution disguised as a problem — it leads with the mechanism, not the gap.)

**Pass:** Problem stated independently of the proposed solution. Quantified using the data provided (GMV, repeat booking rate, churn survey findings). The guarantee is not mentioned in the Problem section. A reader who stopped after the Problem section would understand the gap without having any idea what the proposed solution is. **Fail:** Problem section opens with or depends on the guarantee as framing. The 31% churn survey finding is not used to size the scope of the problem.

---

## Cost Model Including Guarantee Liability

The PM never mentions the cost of redeeming guarantees. The input only describes the mechanism ("we absorb the difference"). A complete cost model must address this as the primary ongoing cost, not just engineering time.

**What the cost model must include:**

- **Engineering build cost:** Design + development + QA for the submission, verification, and reimbursement workflow. This is a one-time cost.
- **Guarantee liability — the key missing cost:** The ongoing cost of actually honoring the guarantee. This requires:
  - An estimate of redemption rate: what percentage of eligible customers will actually claim the guarantee? This is the single most important unknown.
  - A per-redemption cost model: if average booking is $185 and the typical direct price discount is X%, each redemption costs the platform Y dollars.
  - A volume estimate: if Z% of [repeat bookings] claim the guarantee, total annual liability is approximately $[range].
- **Operations cost:** Who verifies the claims? A human review step (screenshot verification) has a labor cost per claim.
- **Opportunity cost:** Named initiatives that compete for the same engineering resources.

**Pass:** Cost model includes guarantee liability with at minimum a Conservative / Expected / Optimistic range of redemption rates, a per-redemption cost estimate based on the $185 average booking value, and an explicit acknowledgment that redemption rate is the key assumption the business case is most sensitive to. Engineering build cost is present but is not the dominant cost discussion. **Fail:** Cost model covers only engineering build time. Guarantee liability (the ongoing cost of matching prices) is omitted or treated as negligible without justification.

---

## Retention-Friction Blindspot

The PM assumes the guarantee will improve repeat booking rate among the customers it attracts. This assumption has a non-obvious failure mode: a price guarantee may attract price-sensitive customers who are low-lifetime-value, not high-LTV. A customer who books once to capture a price match and then leaves is worse than a customer who never booked at all (if the platform absorbed a price-match cost on that booking).

**What good handling looks like:**

The business case explicitly asks: "Who is this guarantee attracting?" The retention benefit assumes the guarantee retains customers who were going to leave. But it may also attract new customers who are primarily motivated by price guarantees — these customers may book with the guarantee once, then continue looking for lower prices directly. The guarantee could increase the volume of low-LTV customers rather than improving retention of high-LTV ones.

Specifically names the dynamic: **"The guarantee functions as a price floor for price-sensitive buyers. Price-sensitive buyers have lower expected LTV (more likely to leave for any lower-price alternative). The guarantee may be better at attracting this segment than retaining high-LTV repeat customers — who are more likely motivated by trust, familiarity, and convenience than by price matching."**

May recommend: testing the guarantee with a small cohort of at-risk customers (those who previously churned and cited price as the reason) before full rollout, to distinguish retention of high-LTV customers from acquisition of low-LTV price-shoppers.

**Pass:** The retention-friction dynamic is named explicitly and with specificity. The business case does not simply accept "guarantee → improved retention" as given. The distinction between retaining high-LTV customers vs. attracting low-LTV price-shoppers is drawn. **Fail:** Retention benefit taken at face value with no analysis of who the guarantee attracts or whether those customers have high expected LTV.

---

## Genuine Alternatives (Not Strawmen)

The PM dismissed "do nothing" in one sentence: "that doesn't solve the leakage problem." This is a conclusion without analysis. The business case must evaluate alternatives honestly.

**Minimum required alternatives:**

1. **Best Price Guarantee (recommended option):** The proposed solution. Pros: directly addresses the stated churn reason; signals price confidence. Cons: ongoing liability, attracts price-sensitive buyers, potential moral hazard (pros may be incentivized to offer lower direct prices knowing the platform will match).

2. **Pro loyalty incentives (genuine alternative):** Instead of matching customer-facing prices, incentivize pros to keep bookings on-platform — e.g., reduced take rate for pros who maintain a high on-platform booking rate, or preferential search placement. Pros: addresses the root cause (pros going around the platform) rather than patching the symptom (customers taking the lower price). Lower liability risk. Cons: harder to enforce, requires pro relationship management, slower impact.

3. **Customer loyalty program (genuine alternative):** Address repeat booking decline through a separate loyalty program — points, credits, or exclusive benefits for repeat platform bookings. Pros: improves retention without creating price-match liability; differentiates on value beyond price. Cons: does not directly address price leakage; customers can still find the same pro cheaper directly.

4. **Do nothing:** What is the actual annual cost of continued booking leakage? If 31% of churned customers cite price leakage and the platform has 23% repeat bookings, what does a 1-2% annual erosion of that repeat rate cost in GMV terms? State this honestly — "do nothing" has a quantifiable cost that should inform whether the guarantee's expected ROI justifies its liability.

**Pass:** At least 2 genuine alternatives with honest trade-offs. At least one alternative (pro loyalty incentives or equivalent) has a genuine advantage over the guarantee in at least one dimension. "Do nothing" is assessed with a GMV cost estimate, not dismissed in one sentence. Each alternative closes with a Verdict. **Fail:** Alternatives are strawmen — listed only to be dismissed. "Do nothing" not quantified. Only the guarantee has a positive framing.

---

## Confidence Level Calibrated to Evidence

The PM expressed "clearly the right call." The business case should reflect what the evidence actually supports.

**What the evidence actually is:**
- Churn survey showing 31% of non-returning customers cited "found pro cheaper directly" — this is directional signal from a survey, not causal proof that a price guarantee would have retained them.
- No A/B test data on the guarantee's effect on retention.
- No data on the redemption rate (the central variable in the cost model).
- No data on whether the customers citing price as a churn reason are high-LTV or low-LTV.

**Pass:** Confidence level is stated in the 4-6 range (medium confidence) with explicit acknowledgment of: (a) churn survey is self-reported and directional, not causal; (b) no redemption rate data exists; (c) LTV of price-sensitive customers is unknown; (d) the retention-friction dynamic hasn't been tested. States what would increase confidence (cohort test, redemption rate data, LTV analysis of price-citing churners). **Fail:** Confidence level matches the PM's high-confidence framing (7+) without acknowledging the quality limitations of the underlying evidence. Or states "clearly the right call" in any form without conditions.

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| Problem-first translation (not solution-first) | 15% | Problem stated independently of the guarantee; GMV and churn data used to size the gap; guarantee not mentioned in Problem section |
| Cost model includes guarantee liability | 20% | Redemption rate named as key variable; per-redemption cost estimated; Conservative/Expected/Optimistic range presented; engineering cost is not the primary cost discussion |
| Retention-friction blindspot named | 20% | Price-sensitive buyer vs. high-LTV customer distinction drawn; guarantee may attract low-LTV buyers; cohort test or validation step recommended |
| Genuine alternatives with honest trade-offs and verdicts | 20% | At least 2 genuine alternatives (pro loyalty or customer loyalty program, or equivalent); do nothing quantified with GMV cost estimate; each alternative closes with a Verdict |
| Confidence level calibrated to evidence quality | 15% | Confidence 4-6 range; survey data limitations named; redemption rate uncertainty named; what would change the recommendation stated |
| Output format compliance | 10% | Problem / Impact Sizing / Cost Model / Alternatives / Recommendation / Stress Test / Smell Test / Agent Block all present; context note included |
