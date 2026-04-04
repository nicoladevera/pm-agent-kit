---
name: data-analysis
description: Interprets product data and metrics in context, classifying analysis type and producing calibrated insights. Use when asked to "analyze this data", "what does this metric mean", "interpret these numbers", "help me understand this trend", or "analyze this funnel drop-off".
metadata:
  type: Analyzer
  tier: 3
  approval: draft-confirm
  context-required: []
  context-optional:
    - company/facts/product.md
    - company/facts/customers.md
    - company/facts/glossary.md
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

## Intake

The most common failure in data analysis is answering the wrong question precisely. Confirm the actual question and what decision it informs before analyzing.

### Signals to Check

- **Specific question:** Is the PM asking a clear, answerable question, or providing data and expecting the agent to figure out what to ask?
- **Decision context:** Does the input say what decision or action the analysis will inform?
- **Data provided:** Is data included (pasted, referenced, described), or is this a question-only request?

### Adaptive Response

**Rich input** (specific question stated, decision context clear, data provided): Restate the question and proceed. Example: "Question: why did [metric] drop [X%] last [period]. This informs whether to [decision]. Analyzing the provided data now."

**Moderate input** (data provided but question vague, or clear question but no decision context): Ask 1-2 targeted questions. Examples:
- "I see the data — what's the specific question? Are you asking why [metric] changed, whether it's concerning, or what to do about it?"
- "What decision does this analysis inform? Knowing that helps me focus on what matters most."

**Thin input** (data dump with no question, or a vague "look at this"): Present a structured interpretation:

> **Here's what I think the question is — correct me:**
>
> - **Question:** [Inferred from the data and context — e.g., "Why did activation drop 15% week-over-week?"]
> - **Analysis type:** [Metric interpretation / Funnel analysis / Cohort analysis / Anomaly investigation]
> - **Decision this informs:** [Best inference — e.g., "Whether to investigate further or treat as normal variance"]
>
> Is that the right question? I want to make sure I'm answering the thing you actually need to know.

---

## Instructions

### 1. Read the input fully

Understand the question being asked and what data is available. Separate the question (what the PM wants to know) from the data (what evidence exists). If the question is implicit in the data ("here's our funnel, what's going on?"), make the question explicit before analyzing.

### 2. Load reference files

Read these files:
- `references/data-interpretation.md` — Metric interpretation heuristics, funnel analysis standards, cohort patterns, anomaly investigation framework, correlation vs. causation guardrails, data quality flags, confidence levels
- `references/pm-smell-test.md` — Check for smells 2 (no way to measure success) and 5 (false precision)
- `references/agent-readable-output.md` — Agent Block format and shared enum vocabulary
- `references/visualization-standards.md` — Chart selection by analysis type, insight-first titling, annotation standards, comparison anchors, label discipline, style rules, technical save pattern

### 3. Load company context (if available)

If `company/facts/product.md` exists and is substantive, read it for product areas and feature landscape. This helps interpret metrics in context (e.g., a drop in "activation" means something different depending on what activation means for this product).

If `company/facts/customers.md` exists and is substantive, read it for customer segment definitions. This helps frame cohort analysis using actual segment definitions rather than inferred ones.

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

**When numeric data is provided, run calculations programmatically.** Do not estimate arithmetic. For funnel math, growth rate deltas, percentage changes, cohort comparisons, and statistical computations — execute the calculation in code (Python) and show the result. Estimation introduces exactly the false precision that Smell 5 flags. If the data is too messy to compute directly, name what's wrong with it before approximating.

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

### 6.5. Generate visualizations

When numeric data is provided, always produce 1–3 charts as PNG files. The chart is not decoration — it should make the key finding visually obvious without requiring the reader to parse the prose. Run programmatically in Python (matplotlib). Do not sketch or estimate.

Load and apply `references/visualization-standards.md` for all chart decisions: type selection, titling, annotation, comparison anchors, label placement, color, and save pattern.

**Chart type by analysis type:**

| Analysis type | Primary chart | Secondary (if a second finding warrants it) |
|--------------|--------------|----------------------------------------------|
| Metric interpretation | Line/time-series with the key movement annotated | Bar showing magnitude vs. baseline |
| Funnel analysis | Horizontal waterfall — absolute users at each stage | Segmented bar at the biggest drop-off step |
| Cohort analysis | Grouped bar (cohorts × metric, same time window) | Dot plot or heatmap for retention over time |
| Anomaly investigation | Time series with the anomaly window highlighted | Breakdown bar showing which segment drives the scope |

Save pattern and naming convention: see `references/visualization-standards.md`.

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

### 10. Sort hypotheses and populate the Agent Block

Sort the Hypotheses table by Rank (1 = most likely) before output. If the data doesn't clearly distinguish likelihood between hypotheses, state the tied ranks and explain in the Limitations section rather than forcing an ordering.

Populate the Agent Block:
- `analysis_type`: from the classification in step 4
- `finding`: the key finding in one sentence (the first sentence of the Key Finding section)
- `confidence`: the categorical confidence level from the Key Finding section
- `top_hypothesis`: the row number of the Rank 1 hypothesis
- `recommended_action`: one of Pull more data / Run experiment / Act on finding / Monitor — the primary next step from step 9
- `sample_size_adequate`: Yes if sample size was assessed as sufficient in step 5; No if a size constraint was identified; Unknown if size wasn't determinable

---

## Output Format

````markdown
## Data Analysis: [Question or Topic]

**Analysis type:** [Metric interpretation / Funnel analysis / Cohort analysis / Anomaly investigation]

<!-- AGENT BLOCK -->
```yaml
agent_block:
  skill: data-analysis
  analysis_type: [Metric interpretation / Funnel analysis / Cohort analysis / Anomaly investigation]
  finding: "[One sentence summary of the key finding]"
  confidence: [High / Medium / Low]
  top_hypothesis: [integer — rank 1 hypothesis number]
  recommended_action: [Pull more data / Run experiment / Act on finding / Monitor]
  sample_size_adequate: [Yes / No / Unknown]
  charts:
    - knowledge/data-analyses/YYYY-MM-DD-slug-chart.png
```
<!-- /AGENT BLOCK -->

---

### Question

[Restate the question clearly. If the question was implicit, make it explicit.]

---

### Key Finding

**Finding:** [1-2 sentences. The answer, stated directly.]
**Confidence:** [High / Medium / Low] — [One sentence on what drives this confidence level — sample size, data quality, or evidence strength]
**Top Hypothesis:** Hypothesis #[N] — [brief label from the Hypotheses table below]
**Recommended Action:** [Pull more data / Run experiment / Act on finding / Monitor]

---

### Analysis

[Structured analysis appropriate to the type.

For metric interpretation: context (baseline, variance, seasonality), the movement, candidate explanations.
For funnel analysis: stage-by-stage data, drop-off analysis, segmentation findings.
For cohort analysis: cohort definitions, comparison table, divergence analysis.
For anomaly investigation: characterization (timing, magnitude, scope, shape), hypotheses.

Show the work. Include tables, calculations, and comparisons as appropriate.]

---

### Visualizations

![Insight-first title stating the key finding](./YYYY-MM-DD-slug-chart.png)
*Chart 1: [One sentence — what the chart shows and what the reader should conclude. Cite the reference line or comparison anchor used.]*

![Second insight-first title](./YYYY-MM-DD-slug-chart_2.png)
*Chart 2: [Caption.] — Omit this entry if only one chart was produced.*

---

### Hypotheses

| Rank | # | Hypothesis | Evidence For | Evidence Against | Likelihood |
|------|---|-----------|-------------|-----------------|------------|
| 1 | [#] | [Most likely hypothesis] | [What supports it] | [What contradicts it] | [High / Medium / Low] |
| 2 | [#] | [Second most likely] | [Evidence for] | [Evidence against] | [Likelihood] |

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
````

---

## Quality Bar

- **Does the analysis answer the actual question asked?** Not a related question, not a broader analysis that buries the answer. The PM asked something specific — the key finding addresses it directly.
- **Is the key finding stated up front?** The reader knows the answer within the first section. Supporting analysis follows, not precedes, the conclusion.
- **Are hypotheses ranked by likelihood with evidence?** Not a brainstorm list. Each hypothesis has evidence for and against, and a likelihood assessment. The PM knows which explanation to bet on and why.
- **Are limitations stated honestly?** The analysis says what it can't tell you, not just what it can. Sample size, confounders, data quality — all named.
- **Is confidence calibrated to the data?** High confidence requires strong data. Medium confidence is stated when caveats exist. Low confidence is used when the data is thin. The PM knows how much to trust the finding.
- **Would a data-literate PM trust this analysis?** The reasoning is visible, the math is sound, confounders are addressed, and the conclusion follows from the evidence.
- **Does every chart title state the insight?** A chart titled "Metric by Segment" has failed. The title makes the finding obvious before a single data point is read.

---

## Save

After producing the artifact, write it to `knowledge/data-analyses/` using the naming convention: `YYYY-MM-DD-analysis-slug.md`, where `YYYY-MM-DD` is today's date and `analysis-slug` is a lowercase hyphenated slug derived from the question or topic.

Save each PNG to the same directory: `knowledge/data-analyses/`. Naming: `YYYY-MM-DD-analysis-slug-chart.png`. Append `_2`, `_3` for additional charts from the same analysis.

Report all saved file paths (both `.md` and `.png` files) in the conversation.
