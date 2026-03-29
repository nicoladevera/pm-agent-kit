# Evaluation Rubric — data-analysis (Metric Interpretation)

**Target input:** `evals/data-analysis/sample-input-02.md`
**Skill under test:** `skills/data-analysis/SKILL.md`
**Purpose:** Determine whether `data-analysis` correctly interprets a DAU/WAU ratio decline by decomposing the ratio into its components, identifying the true driver (WAU growth outpaced DAU growth), avoiding the "engagement collapsed" misread, and calibrating confidence appropriately for correlational data with two overlapping events.

## Coverage

**This rubric tests:** Metric interpretation analysis type — ratio decomposition, trend analysis, candidate explanation ranking.
**Not covered here:** Anomaly investigation with funnel analysis (`rubric.md`), Cohort analysis (`rubric-cohort.md`).

---

## Analysis Type Classification

The PM asks "what does this mean?" with an 8-week ratio time series. There is no anomaly (the ratio declined gradually, not suddenly), no funnel (no step-by-step conversion data), and no cohort comparison (no user groups being compared). This is metric interpretation: establishing context, assessing the movement, and ranking candidate explanations.

**Pass:** Classified as metric interpretation.
**Fail:** Classified as anomaly investigation (the ratio drop is a trend to interpret, not an unexpected spike or cliff); or classified as funnel analysis despite no funnel data being present.

---

## Ratio Decomposition (Critical Test)

The single most important analytical move in this input is decomposing DAU/WAU into its numerator (DAU) and denominator (WAU) and assessing each separately. A ratio can decline because the numerator fell, the denominator grew, or both. In this case:

- WAU grew from ~181K (weeks 1–4 baseline) to ~200K (weeks 6–8) — a ~10% increase, driven by the App Store promotion
- DAU fell from ~76K (baseline) to ~62K (weeks 6–8) — a ~18% decline, which may partially reflect the push notification reduction

A PM or executive who reads "DAU/WAU dropped from 0.42 to 0.31" without this decomposition is likely to conclude "engagement collapsed." The correct reading is more nuanced: WAU grew (which is positive), but DAU declined, and the ratio reflects both dynamics simultaneously. An analysis that doesn't separate these is not answering the question.

**Pass:** Analysis explicitly decomposes WAU and DAU as separate time series. Identifies that WAU grew from ~181K to ~200K while DAU dropped from ~76K to ~62K. States the primary insight: "The ratio declined because WAU grew while DAU fell — this is a user mix shift and daily engagement story, not an engagement collapse." Shows the calculations.

**Fail:** Treats the ratio decline as equivalent to "engagement dropped" without decomposing numerator and denominator separately. Or attributes the full decline to the push notification change without addressing the WAU growth story. Or restates the ratio numbers without doing the decomposition work.

---

## The App Store Promotion as Primary Structural Driver

The week 5 WAU spike from ~182K to 210K (a ~28K increase, roughly 15%) is the primary structural event in this dataset. Users acquired via the App Store promotion are new to the product — new users have lower daily engagement than established users, because they haven't yet built a habit. This is a mix effect: when a large cohort of lower-engagement new users enters the WAU denominator, the ratio drops even if existing user behavior is unchanged.

This is the highest-value insight the analysis can produce. Framing the ratio decline as "primarily a mix effect from new user acquisition" is meaningfully different from "engagement declined" — the former is potentially good news (growth), the latter implies product quality degraded.

**Pass:** Identifies the week 5 WAU spike as correlated with the App Store promotion. Explains the mix effect: newly acquired users are weekly-active (they downloaded and opened the app) but are unlikely to be daily-active in their first weeks, which mechanically dilutes the ratio. Frames this as a natural consequence of growth, not evidence of engagement failure.

**Fail:** Ignores the WAU growth story entirely. Or treats the promotion as a red herring and attributes the ratio decline primarily to the push notification change. Or describes the promotion without connecting it to the ratio mechanics.

---

## Push Notification Reduction: Contributing Factor, Not Primary Cause

The push notification frequency reduction (week 6) likely contributed to the DAU decline. Fewer push notifications = fewer triggered app opens = lower DAU. This is a plausible and important hypothesis.

However, it cannot be the primary explanation for the full ratio story:
- The ratio was already declining in week 5 (0.42 → 0.39) before the push notification change went live
- The WAU growth from the promotion was already distorting the denominator before week 6
- The two events happened back-to-back, making clean attribution impossible from this data alone

Naming push notification reduction as the sole or primary cause is a plausible-sounding wrong answer. The analysis must hedge appropriately and call out the confounding timing.

**Pass:** Names push notification reduction as a likely contributing factor to DAU decline in weeks 6–8. Explicitly distinguishes it from the primary cause (WAU growth from the promotion). Hedges the causal claim: "The timing is consistent but confounded — to confirm, segment by notification opt-in status and compare DAU trends between opted-in and opted-out users."

**Fail:** Names push notification reduction as the primary or sole cause, ignoring the promotion timing and WAU growth. Or dismisses push notification reduction as irrelevant. Or treats both events as equally unresolved without ranking their likely contributions.

---

## Confidence Calibration

This analysis has two overlapping events (promotion + push notification change) happening in consecutive weeks, with no control group and no cohort-level breakout. The correlation is strong but the attribution is inherently uncertain.

The data does support medium confidence for the following specific claims:
- WAU grew due to the App Store promotion — the timing is unambiguous
- The ratio drop is structurally explained by WAU growing faster than DAU — this is arithmetic, not correlation
- Push notification reduction likely contributed to DAU decline — timing is consistent

What cannot be stated with high confidence: the exact contribution of the push notification change to the DAU decline, since the two events are simultaneous and there's no control.

**Pass:** States medium confidence. Names both confounders explicitly. Calls out that the events' close timing makes it impossible to fully separate their effects with this data. Names what would increase confidence (segment by notification preference to isolate push notification effect; compare new-user cohort DAU vs. returning-user DAU to isolate mix effect).

**Fail:** States high confidence without caveats. Or hedges everything so thoroughly that no directional insight is offered. Or conflates the arithmetic certainty (ratio decomposition) with the causal uncertainty (attribution between events).

---

## Answer to the Board Question

The PM states explicitly: "I'm presenting this to the board next week." The analysis must give her a clear, defensible framing she can take into that room — not a hedge-everything summary that leaves her more uncertain than before.

A board-ready framing:
- Leads with the ratio decomposition (WAU grew, DAU declined — these are two separate stories)
- Names the primary driver (new user acquisition via App Store promotion creates a mix effect on the ratio)
- Acknowledges the push notification change as a contributing factor worth investigating
- States what monitoring to continue (new-user DAU cohort over the next 4–6 weeks; DAU by notification preference)
- Gives the board a defensible read: "The ratio decline is primarily a growth story — we acquired more weekly-active users, which dilutes the daily engagement ratio by design. DAU is declining, which bears watching — the push notification change may have contributed and we're investigating."

**Pass:** Provides an explicit board-ready framing with the above elements. Does not leave the PM to construct the narrative herself from a list of bullet points.

**Fail:** Leaves the PM with "it's complicated" without a usable narrative. Or gives a narrative that overstates certainty (e.g., "the push notification change caused the engagement drop" as a board-ready statement without caveats). Or focuses entirely on investigation steps without giving the PM something to say next week.

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| Analysis type classification (metric interpretation) | 5% | Classified as metric interpretation, not anomaly investigation |
| Ratio decomposition (WAU vs. DAU separated) | 25% | WAU and DAU analyzed separately; primary insight named ("mix effect, not engagement collapse") |
| Promotion identified as primary structural driver | 20% | Week 5 WAU spike connected to promotion; mix effect explained |
| Push notification as contributing factor, not primary cause | 20% | Named as contributing factor; distinguished from promotion story; causal hedge applied |
| Confidence calibrated with named confounders | 15% | Medium confidence stated; both events named as confounders; investigation path specified |
| Board-ready framing provided | 10% | Explicit narrative the PM can take to the board, with defensible framing |
| Output format compliance | 5% | Matches declared output format; Agent Block populated; context note present |
