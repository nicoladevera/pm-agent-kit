# Evaluation Rubric — data-analysis (Cohort Analysis)

**Target input:** `evals/data-analysis/sample-input-03.md`
**Skill under test:** `.claude/skills/data-analysis/SKILL.md`
**Purpose:** Determine whether `data-analysis` correctly reads retention curves across cohorts, surfaces the LTV inversion (paid social has the highest early retention but the lowest LTV), connects the analysis to a specific product/marketing decision (CAC allocation), and names the confounder (service type mix may differ by acquisition source).

## Coverage

**This rubric tests:** Cohort analysis — multi-source retention comparison with LTV implications.
**Not covered here:** Anomaly investigation with funnel analysis (`rubric.md`), Metric interpretation (`rubric-metric.md`).

---

## Analysis Type Classification

The PM asks to compare behavior across user groups defined by acquisition source — three distinct cohorts, same metric, same time window. This is cohort analysis.

**Pass:** Classified as cohort analysis.
**Fail:** Classified as funnel analysis (no funnel is present — the D1/D7/D30/D90 data is a retention curve, not a step-by-step conversion funnel) or metric interpretation (there is no single metric to interpret — the question is about relative differences across groups).

---

## The Retention Curve Inversion (Critical Test)

The most important insight in this dataset: paid social leads at D1 (52%) and D7 (38%), then collapses to 8% at D90. Referral starts lower at D1 (61% — actually highest, but similar-ish) and holds at 31% at D90. The "inversion" isn't that paid social starts high and referral starts low — it's that paid social's D90 is a fraction of referral's D90, meaning the early-stage advantage evaporates entirely.

More critically: the PM has been optimizing paid social campaigns for D1 conversions (first booking). The optimization is selecting exactly for users who book once and disappear. The dashboard metric is actively working against long-term value.

**Pass:** Names the inversion explicitly with specific numbers: "Paid social has the highest D7 retention of the three sources (38%) but the lowest D90 retention (8% vs. 18% organic, 31% referral). The paid social retention curve drops 44 points from D7 to D90; referral drops 21 points over the same window." Connects this directly to the optimization problem: "Your Meta campaigns are optimized for D1 bookings — this is selecting for users who are likely to book once and churn, which is exactly what the data shows."

**Fail:** Notes that all three cohorts have different retention curves without calling out the inversion or its implication for the optimization strategy. Or reports the numbers without naming which direction the inversion runs. Or acknowledges the optimization issue without connecting it to the specific retention pattern in the data.

---

## LTV Calculation

The input provides two of the three inputs needed for a lifetime value estimate: average jobs booked by D90 and average order value per booking. Multiplying these gives a D90 revenue-per-customer estimate that is directly comparable across cohorts — and the comparison is stark.

Expected calculations:
- Paid social: 1.3 jobs × $95 = **$123.50 LTV by D90**
- Organic search: 2.1 jobs × $120 = **$252.00 LTV by D90**
- Referral: 3.4 jobs × $130 = **$442.00 LTV by D90**

The referral cohort generates approximately 3.6x the LTV of the paid social cohort by D90. This is the number that should anchor the CAC budget recommendation.

An analysis that reports retention curves without computing LTV leaves the PM without the number she needs for the budget review. "Referral retains better" is less useful than "referral generates $442 per customer by D90 vs. $124 for paid social."

**Pass:** Calculates approximate LTV per cohort (jobs × order value). Identifies the ~3.6x gap between referral and paid social. Notes that this is a D90 estimate, not lifetime value, since the data window is 90 days.

**Fail:** Notes retention differences without computing LTV. Or uses only one component (jobs booked or order value) without combining them. Or correctly identifies the LTV gap but doesn't state the actual numbers.

---

## Connected to the CAC Decision

The PM's explicit question is where to put CAC budget. The analysis should give her a directional recommendation she can bring to the budget review — not just a data summary.

**Pass:** Provides a directional recommendation with three components:
1. **Shift toward referral:** The referral program ($20 credit per referred customer) has a dramatically lower cost of acquisition than paid social ($45K/month for 3,200 customers = ~$14 CAC not counting platform fees) and produces the highest LTV cohort. Increasing referral program investment is the highest-ROI move the data supports.
2. **Reconsider paid social optimization target:** If paid social is retained as a channel, shift the campaign optimization objective from D1 bookings to D30 bookings (or LTV-correlated signals). Optimizing for early conversions is demonstrably selecting for low-retention users.
3. **Organic search:** Low direct cost, strong retention (D90 = 18%, LTV = $252). Worth investing in SEO-adjacent activities if the channel can be amplified without large spend.

**Fail:** Describes the data without connecting to the CAC allocation question. Or recommends "more testing" without a directional recommendation. Or makes a recommendation without tying it to the specific LTV numbers in the data.

---

## The Confounder: Service Type Mix

Different acquisition channels likely attract customers looking for different types of jobs. Paid social campaigns targeting broad audiences may skew toward customers looking for one-time services (move-out cleaning, single handyman job). Referral customers may skew toward customers already planning recurring services (regular cleaning, ongoing lawn maintenance) — because they were referred by someone currently using the service, who may themselves be a recurring customer.

If this confounder is real, the LTV difference between cohorts may reflect service type preference and intended use case, not acquisition channel quality per se. A customer who found the app via Facebook intending a one-time deep clean isn't a lower-quality customer — they're a different customer type. Distinguishing these two explanations affects the recommendation.

**Pass:** Names this as a confounder. "The LTV and retention differences between cohorts may reflect service type mix — referral customers may be more likely to book recurring services while paid social customers may skew toward one-time jobs. To confirm, segment each cohort by first job type (recurring vs. one-time) and check whether the retention gap persists within the same service category."

**Fail:** Treats the cohort difference as definitive proof that paid social acquires worse customers, without noting that service type intent may explain part or all of the gap. Or mentions service type in passing without calling it out as a confounder that affects the recommendation.

---

## Confidence Calibration

The three cohorts have substantially different sample sizes: paid social (n=3,200), organic search (n=1,800), and referral (n=620). A 5x difference between the largest and smallest cohort is not trivial — at D90, the referral cohort's 31% retention represents roughly 192 customers, while paid social's 8% represents roughly 256 customers. The directional finding (referral retains better) is consistent with the data, but the specific percentage estimates for the smaller cohort are noisier.

**Pass:** Notes the sample size inequality explicitly. Treats paid social findings (n=3,200) as high confidence. Treats referral findings (n=620) as directionally reliable but notes the smaller sample means individual percentage estimates could shift with a larger cohort. Does not refuse to make a recommendation on this basis — directional confidence is sufficient for a budget reallocation decision.

**Fail:** Treats all three cohorts as equally confident despite the 5x sample size difference. Or uses the sample size issue to avoid making a recommendation (over-hedging). Or doesn't address sample size at all.

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| Analysis type classification (cohort analysis) | 5% | Classified as cohort analysis, not funnel or metric interpretation |
| Retention curve inversion identified and named | 25% | Inversion stated with specific numbers; optimization misalignment named |
| LTV calculation performed per cohort | 20% | Jobs × order value calculated for all 3 cohorts; gap quantified |
| Analysis connected to CAC allocation decision | 20% | Directional recommendation on referral, paid social optimization, and organic |
| Service type confounder named | 15% | Mix effect hypothesis stated; investigation path specified |
| Confidence calibrated to sample size differences | 10% | Paid social high confidence; referral directional with caveat; recommendation still given |
| Output format compliance | 5% | Matches declared output format; Agent Block populated; context note present |
