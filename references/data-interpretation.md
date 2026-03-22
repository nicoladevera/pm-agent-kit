# Data Interpretation Standards

What makes a data analysis useful for product decisions. Use this to interpret metrics, analyze funnels, compare cohorts, investigate anomalies, and turn product questions into data insights. The analytical counterpart to `feedback-analysis.md` — that file covers qualitative signal from users; this file covers quantitative signal from behavior.

Data interpretation is not reporting. Reporting says "activation dropped 12%." Interpretation says "activation dropped 12%, concentrated in mobile web, coinciding with the March 10 deploy, and it's likely the new onboarding flow introduced a regression in the bank-linking step." The number is the starting point, not the answer.

---

## Metric Interpretation

### Context Before Conclusion

A metric movement means nothing without context. Before interpreting any metric change, establish:

- **Baseline:** What is the normal range for this metric? What was it last period, last month, same time last year?
- **Variance:** How much does this metric normally fluctuate? A 5% drop in a metric that swings ±8% weekly is noise. A 5% drop in a metric that hasn't moved more than 1% in six months is a fire.
- **Time window:** Over what period did the change occur? A gradual decline over 4 weeks has different causes than a sudden drop overnight.
- **Seasonality:** Does this metric have known seasonal patterns? (End of month, holidays, payroll cycles, school calendar, etc.)

**Red flag:** Interpreting a metric movement without establishing baseline or variance. Treating any decline as a problem or any increase as a win without asking "is this within normal range?"

---

### Magnitude and Significance

Not every change is meaningful. Assess:

| Question | How to evaluate |
|----------|----------------|
| **Is it statistically significant?** | For metrics with sufficient sample size: is the change larger than the expected variance? For small samples: flag that significance can't be determined. |
| **Is it practically significant?** | Even a statistically significant change might not matter in business terms. A 0.3% conversion improvement on a low-traffic flow may not be worth investigating. |
| **Is it sustained or transient?** | A one-day spike followed by a return to baseline is different from a level shift that persists. Look at the shape, not just the magnitude. |

**Red flag:** Reporting a statistically insignificant change as a finding. Conversely, dismissing a large practical change because the p-value is borderline. Both extremes are wrong — use judgment.

---

## Funnel Analysis

### Every Funnel Has a Story

A funnel converts users from one state to another through a series of steps. The analysis should tell the story of where users succeed, where they drop off, and why.

**For each funnel stage:**
- **Conversion rate:** What percentage of users advance to the next step?
- **Drop-off rate:** What percentage of users leave at this step?
- **Absolute numbers:** Percentages alone can hide small-sample issues. Always include counts.
- **Benchmark:** Is this conversion rate normal? Compare to prior periods, industry benchmarks, or internal targets.

**Where to focus:**
- **The biggest absolute drop-off** — where the most users are lost, regardless of percentage
- **The biggest percentage drop-off** — the step with the worst conversion, regardless of volume
- **The most changed step** — if comparing periods, which step deteriorated or improved the most?

These three lenses often point to different steps. Name all three and explain which matters most for the current question.

**Red flag:** Analyzing only percentage conversion without absolute numbers. Focusing on the first step of the funnel when the real problem is at step 4. Comparing funnels across periods without controlling for traffic mix changes.

---

### Segmentation Reveals Causes

An aggregate funnel hides segment-level stories. When a funnel underperforms, segment by:

- **Platform:** Mobile vs. desktop vs. mobile web — different experiences, different conversion patterns
- **Cohort:** New users vs. returning users — onboarding vs. retention issues
- **Source:** Organic vs. paid vs. referral — traffic quality affects conversion
- **Geography:** If applicable — localization, payment methods, and regulations vary

If the overall funnel drops 10% but the drop is concentrated in mobile web, the problem isn't "the funnel is broken" — it's "something is wrong with the mobile web experience at step X."

---

## Cohort Analysis

### Define, Compare, Explain

Cohort analysis compares the same metric across different groups of users to identify meaningful differences.

**Types of cohorts:**
- **Time-based:** Users who signed up in Week 1 vs. Week 2 vs. Week 3 — useful for measuring whether product changes improve outcomes for newer users
- **Behavior-based:** Users who completed onboarding vs. users who skipped it — useful for measuring the impact of a specific behavior
- **Attribute-based:** Free vs. paid users, mobile vs. desktop users — useful for understanding segment differences

**For each cohort comparison:**
1. **Define the cohorts clearly** — what distinguishes them, how they were selected, sample sizes
2. **Compare the metric** — same metric, same timeframe, different cohorts
3. **Identify meaningful differences** — is the difference large enough to matter? Is it consistent over time?
4. **Hypothesize what drives the difference** — is it selection bias, a product difference, a behavioral pattern, or something else?

**Red flag:** Comparing cohorts with very different sample sizes without acknowledging the statistical limitations. Attributing a cohort difference to a specific cause without ruling out confounders. Ignoring survivorship bias (users still active at week 8 are different from users who churned at week 2).

---

## Anomaly Investigation

### Characterize Before Hypothesizing

When a metric behaves unexpectedly, characterize the anomaly before generating explanations:

1. **Timing:** When exactly did the anomaly start? Is it sudden (cliff) or gradual (drift)?
2. **Magnitude:** How far from the expected range? Is it outside historical variance?
3. **Scope:** Is it global or concentrated in a specific segment, platform, geography, or user cohort?
4. **Shape:** Is it a one-time spike/dip, a level shift, or an ongoing trend?

### Hypothesis Generation

After characterizing, generate candidate explanations ranked by likelihood:

| Category | Examples | How to investigate |
|----------|---------|-------------------|
| **Product changes** | Deploy, feature flag flip, config change, A/B test | Check deploy log, feature flag state, experiment assignment |
| **External factors** | Marketing campaign, press coverage, competitor action, seasonal pattern | Check marketing calendar, external events |
| **Data quality** | Tracking break, event schema change, sampling error, pipeline delay | Check event volumes, schema versions, pipeline health |
| **Infrastructure** | Outage, latency spike, CDN issue, third-party service degradation | Check incident logs, status pages, latency dashboards |

**Investigation order:** Rule out data quality first (cheapest to check, most embarrassing to miss). Then check product changes (most likely cause of sudden changes). Then external factors. Infrastructure last unless there are obvious signals.

**Red flag:** Jumping to a hypothesis without characterizing the anomaly. Investigating a hypothesis that doesn't match the anomaly's timing or scope. Not considering data quality as a possible explanation.

---

## Correlation vs. Causation

### When to Claim, When to Hedge, When to Experiment

| Confidence level | When to use | How to state it |
|-----------------|-------------|-----------------|
| **Causal claim** | Randomized experiment with sufficient sample size and runtime. Or: a change was deployed to 100% of users and the metric shifted immediately in the expected direction with no confounders. | "The deploy caused the drop" / "The experiment shows X improves Y by Z%" |
| **Strong correlation** | The metric change coincides with a known event, the direction is consistent, and confounders have been reasonably ruled out. | "The drop is most likely caused by X, based on [timing, segment concentration, and ruling out alternatives]" |
| **Suggestive correlation** | The metric change coincides with a known event, but confounders haven't been ruled out or the evidence is indirect. | "The drop may be related to X, but we can't confirm without [additional analysis / an experiment]" |
| **Speculative** | A plausible explanation with no direct evidence. | "One hypothesis is X, but this would need to be validated with [data / experiment]" |

**Red flag:** Claiming causation from observational data. Hedging everything into uselessness ("it might possibly perhaps be related to..."). The right approach is honest calibration: state the evidence, state the confidence level, state what would increase confidence.

---

## Data Quality Flags

### Name the Limitations

Every analysis has limitations. Name them explicitly rather than hoping the reader notices:

| Issue | What to flag | Why it matters |
|-------|-------------|---------------|
| **Small sample size** | "This analysis covers N users, which limits our ability to detect small effects" | Small samples produce noisy metrics. A 20% swing in a 50-user sample is not the same as in a 50,000-user sample. |
| **Selection bias** | "Users who [criteria] may not be representative of all users" | Analyzing only users who reached step 5 tells you nothing about users who dropped at step 2. |
| **Survivorship bias** | "This cohort only includes users still active at [time], excluding those who churned earlier" | Surviving users are systematically different from churned users. Treating them as representative leads to wrong conclusions. |
| **Missing data** | "X% of events are missing [field], which may affect the accuracy of [calculation]" | Incomplete data can skew metrics in non-obvious ways. |
| **Confounders** | "During this period, [other change] also occurred, which may have affected the metric" | Multiple things happening simultaneously make it impossible to attribute a change to a single cause without isolation. |

**Red flag:** An analysis that states findings without any limitations section. Every analysis has limitations — if you can't name them, you haven't thought carefully enough about what could be wrong.

---

## Confidence Levels

### State What You Know and How Well You Know It

For every key finding, state a confidence level:

| Level | When to use |
|-------|-------------|
| **High confidence** | The data is clean, the sample is large, the finding is robust across segments, and confounders have been reasonably ruled out. |
| **Medium confidence** | The data supports the finding but there are meaningful caveats — small sample, short time window, possible confounders. |
| **Low confidence** | The finding is directionally suggestive but not reliable — small sample, noisy data, or significant confounders present. |
| **Cannot determine** | The data is insufficient to answer the question. State what data would be needed. |

**Red flag:** All findings stated at the same confidence level. High confidence with a 50-user sample. Low confidence on a clear, well-supported finding. Match the confidence to the evidence.

---

## Using These Standards

**For data analysis (`data-analysis` skill):** Establish context before interpreting. Characterize anomalies before hypothesizing. Segment to find causes. State confidence honestly. Name limitations. The analysis answers the PM's question, not a related question.

**For interpreting data in other skills:** When metrics or data appear as input to other skills (e.g., in a status update, a sprint plan, or a business case), apply these standards to assess data quality and appropriate confidence. Don't amplify weak data into strong claims.
