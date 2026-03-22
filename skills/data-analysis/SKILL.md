---
skill: data-analysis
type: Analyzer
tier: 3
approval: draft-confirm
context-required: []
context-optional:
  - company/facts/product.md
  - company/interfaces/data-sources.md
degradation: proceed-with-caveat
---

# data-analysis

Answer a data question in product context. The skill's job is to turn a product question and data into an insight — not to restate numbers, but to interpret what they mean and what to do about them. The analysis type adapts to the question: metric interpretation, funnel analysis, cohort comparison, or anomaly investigation.

---

## What It Accepts

Any combination of a question and data:
- A data question ("Why did signups drop 15% last week?")
- Pasted data (CSV, table, dashboard export, or described data)
- A metric and context ("Our activation rate is 23% — is that good?")
- Funnel numbers at each stage
- Cohort data with a comparison question
- A question without data (skill describes what data is needed and what the expected answer shape looks like)
- A combination of the above

The input does not need to be clean or complete. This skill works with what's provided and names what's missing.

---

## Instructions

### 1. Read the input fully

Understand the question being asked and what data is available. Separate the question (what the PM wants to know) from the data (what evidence exists). If the question is implicit in the data ("here's our funnel, what's going on?"), make the question explicit before analyzing.

### 2. Load reference files

Read these files:
- `references/data-interpretation.md` — Metric interpretation heuristics, funnel analysis standards, cohort patterns, anomaly investigation framework, correlation vs. causation guardrails, data quality flags, confidence levels
- `references/pm-smell-test.md` — Check for smells 2 (no way to measure success) and 5 (false precision)

### 3. Load company context (if available)

If `company/facts/product.md` exists and is substantive, read it for product areas, user segments, and feature landscape. This helps interpret metrics in context (e.g., a drop in "activation" means something different depending on what activation means for this product).

If `company/interfaces/data-sources.md` exists and is substantive, read it for data infrastructure context — what tools track what, known limitations, key dashboards.

If any of these files exist but are still stub templates, treat them as unavailable and say so in the context note.

### 4. Classify the analysis type

Determine the analysis type from the question and data:

| Type | Triggered by |
|------|-------------|
| **Metric interpretation** | "What does this number mean?" "Why did X change?" "Is this good or bad?" |
| **Funnel analysis** | Funnel data provided, or question about conversion/drop-off |
| **Cohort analysis** | Comparison between user groups, or question about how different segments behave |
| **Anomaly investigation** | Something unexpected happened — a spike, drop, or unusual pattern |

State the classification at the top of the output. If the question spans multiple types (e.g., "our funnel conversion dropped — investigate the anomaly"), name the primary type and note the secondary.

### 5. Check data sufficiency

If data is provided, assess whether it's sufficient to answer the question:
- Is the sample size large enough to draw conclusions?
- Is the time window appropriate for the question?
- Are the right segments or dimensions available?
- Are there obvious data quality issues (missing values, inconsistencies)?

If only a question is provided without data, describe:
- What data would be needed to answer the question
- What query or analysis to run (at the level of "pull daily active users segmented by platform for the last 30 days")
- What the expected shape of the answer looks like
- What tools or dashboards to check (if company context is available)

### 6. Analyze

Run the analysis appropriate to the type. Follow the standards in `references/data-interpretation.md`:

**For metric interpretation:**
- Establish context: baseline, historical range, variance, seasonality
- Assess the movement: magnitude, significance (statistical and practical), duration
- Identify candidate explanations: product changes, external factors, data quality issues
- Rank explanations by likelihood with evidence for and against each

**For funnel analysis:**
- Map funnel stages with conversion rate, drop-off rate, and absolute numbers at each step
- Identify the biggest drop-off (by absolute loss, by percentage, and by change vs. prior period)
- Segment the funnel to find where the problem is concentrated (platform, cohort, source, geography)
- Hypothesize root causes for the most significant drop-offs

**For cohort analysis:**
- Define cohorts clearly (what distinguishes them, sample sizes)
- Compare the metric across cohorts, same timeframe
- Identify meaningful differences (practical, not just statistical)
- Hypothesize what drives the divergence, noting confounders

**For anomaly investigation:**
- Characterize first: timing (when), magnitude (how much), scope (where), shape (sudden vs. gradual)
- Rule out data quality issues before other hypotheses
- Generate candidate explanations ranked by likelihood
- Recommend investigation steps to confirm or rule out the top hypothesis

### 7. Run the smell test

Check for:
- **Smell 2 (No Way to Measure Success)** — Is the question answerable with the available data? If the data provided can't actually answer the question asked, say so. A plausible-sounding analysis of the wrong data is worse than admitting the data is insufficient.
- **Smell 5 (False Precision)** — Are you stating findings with more confidence than the data supports? A finding from 50 users is directional. A finding from 50,000 users is robust. Match precision to sample size.

### 8. State limitations

Name every meaningful limitation of the analysis:
- Sample size constraints
- Time window limitations
- Confounders that couldn't be ruled out
- Data quality issues observed
- What the analysis can't tell you

This is not a formality. An analysis without stated limitations is an analysis the PM can't properly evaluate.

### 9. Recommend next steps

Based on the analysis, recommend what to do next:
- **Additional data to pull:** What would make the analysis stronger?
- **Experiment to run:** If the hypothesis needs causal validation
- **Action to take:** If the finding is strong enough to act on
- **Monitor:** If the signal is real but not yet actionable

---

## Output Format

```markdown
## Data Analysis: [Question or Topic]

**Analysis type:** [Metric interpretation / Funnel analysis / Cohort analysis / Anomaly investigation]

---

### Question

[Restate the question clearly. If the question was implicit, make it explicit.]

---

### Key Finding

[1-2 sentences. The answer, stated directly. Confidence level: High / Medium / Low.]

---

### Analysis

[Structured analysis appropriate to the type.

For metric interpretation: context (baseline, variance, seasonality), the movement, candidate explanations.
For funnel analysis: stage-by-stage data, drop-off analysis, segmentation findings.
For cohort analysis: cohort definitions, comparison table, divergence analysis.
For anomaly investigation: characterization (timing, magnitude, scope, shape), hypotheses.

Show the work. Include tables, calculations, and comparisons as appropriate.]

---

### Hypotheses

| # | Hypothesis | Evidence For | Evidence Against | Likelihood |
|---|-----------|-------------|-----------------|------------|
| 1 | [Hypothesis] | [What supports it] | [What contradicts it] | [High / Medium / Low] |
| 2 | [Hypothesis] | [Evidence for] | [Evidence against] | [Likelihood] |

---

### Limitations

- [Named limitation with explanation of how it affects the analysis]
- [Named limitation]

---

### Recommended Next Steps

1. [What to do next — additional data, experiment, action, or monitoring]
2. [Second recommendation]

---

### Smell Test

- **Smell 2 (No Way to Measure):** [Can the available data actually answer the question? Finding or "Clear — data is sufficient for the question asked"]
- **Smell 5 (False Precision):** [Is confidence calibrated to sample size and data quality? Finding or "Clear — confidence levels match the evidence"]

> **Context note:** [State which substantive company files were loaded, which were absent, and which were stub templates. Note what the analysis might miss without product context or data source context.]
```

---

## Quality Bar

- **Does the analysis answer the actual question asked?** Not a related question, not a broader analysis that buries the answer. The PM asked something specific — the key finding addresses it directly.
- **Is the key finding stated up front?** The reader knows the answer within the first section. Supporting analysis follows, not precedes, the conclusion.
- **Are hypotheses ranked by likelihood with evidence?** Not a brainstorm list. Each hypothesis has evidence for and against, and a likelihood assessment. The PM knows which explanation to bet on and why.
- **Are limitations stated honestly?** The analysis says what it can't tell you, not just what it can. Sample size, confounders, data quality — all named.
- **Is confidence calibrated to the data?** High confidence requires strong data. Medium confidence is stated when caveats exist. Low confidence is used when the data is thin. The PM knows how much to trust the finding.
- **Would a data-literate PM trust this analysis?** The reasoning is visible, the math is sound, confounders are addressed, and the conclusion follows from the evidence.
