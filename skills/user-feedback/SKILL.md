---
skill: user-feedback
type: Analyzer
tier: 3
approval: draft-confirm
context-required: []
context-optional:
  - company/facts/product.md
  - company/facts/competitors.md
  - company/interfaces/data-sources.md
degradation: proceed-with-caveat
---

# user-feedback

Cluster and synthesize customer feedback into themes with frequency, severity, trend, and representative quotes. The skill's job is to turn a pile of feedback into product signal — not to summarize what customers said, but to identify what they need.

---

## What It Accepts

Any form of customer feedback:
- Pasted support tickets (batch)
- NPS or satisfaction survey verbatims
- App store reviews
- User interview notes or transcripts
- Slack or community channel messages
- Sales call notes or CRM feedback
- A previous user-feedback synthesis (for longitudinal comparison)
- A combination of the above

The input does not need to be organized or pre-categorized. This skill produces the organization.

---

## Instructions

### 1. Read all input before analyzing

Absorb the full feedback corpus before producing any output. Understand the volume, the sources, the date range, and the general territory before clustering. Premature clustering misses connections.

### 2. Load reference files

Read these files:
- `references/feedback-analysis.md` — Clustering standards, severity framework, signal vs. noise, quote selection, source channel weighting
- `references/pm-smell-test.md` — Check for smells 5 (false precision) and 15 (recency bias in analysis)
- `references/agent-readable-output.md` — Agent Block format and shared enum vocabulary

### 3. Load company context (if available)

If `company/facts/product.md` exists and is substantive, read it for product areas, user segments, and existing features. This helps map themes to product context and distinguish feedback about your product from feedback about adjacent systems.

If `company/facts/competitors.md` exists and is substantive, read it for competitive landscape. Customer feedback that mentions competitors or alternatives is a specific kind of signal worth calling out.

If `company/interfaces/data-sources.md` exists and is substantive, read it for feedback channel context — what channels exist, known biases, and volume expectations.

If any of these files exist but are still stub templates, treat them as unavailable and say so in the context note.

### 4. Catalog the input

Before clustering, inventory what you have:
- **Total items:** How many discrete feedback items
- **Source channels:** Which channels are represented (support, NPS, reviews, interviews, etc.)
- **Date range:** Earliest and latest dates if available
- **User segments:** If identifiable from the data (new users, power users, enterprise, SMB, etc.)

This catalog goes into the output. It frames the scope and limitations of the synthesis.

### 5. Cluster into themes

Group feedback by underlying need or problem, not by surface feature request. Apply the clustering standards from `references/feedback-analysis.md`:

- "I want dark mode" + "the app hurts my eyes at night" = same theme (visual comfort)
- "Can't find payment history" + "where are my receipts" = same theme (payment history discoverability)

Each theme must meet three criteria:
- **Minimum frequency:** At least 2-3 items converging on the same issue
- **Internal coherence:** Items genuinely relate to the same underlying need
- **Distinctness:** Theme is meaningfully different from other themes

Name themes as the underlying problem, not the requested solution: "Payment history is not discoverable" not "Users want a receipt button."

### 6. Assess each theme

For each theme, determine:

- **Frequency:** How many feedback items map to this theme
- **Severity:** User impact level (Blocking / Painful / Annoying / Cosmetic) per `references/feedback-analysis.md`
- **Scope:** How widespread the issue is (Widespread / Moderate / Isolated)
- **Trend:** If a prior synthesis is provided: Growing / Stable / Declining / New. If no prior synthesis: state "No baseline — first analysis."
- **Source distribution:** Which channels this theme appears in (helps assess whether it's a real cross-channel signal or channel-specific noise)

### 7. Select representative quotes

For each theme, select 2-3 quotes that:
- Represent the typical expression of the theme (not the most extreme)
- Illustrate the theme clearly enough to stand on their own
- Come from different channels or user segments when possible
- Are attributed to source channel and date (if available)

Per `references/feedback-analysis.md` — representative, not dramatic.

### 8. Distinguish signal from noise

Explicitly flag items or themes that are likely noise:

- **Edge cases:** Issues affecting a very narrow use case or tiny user segment
- **Misattributed:** Feedback about infrastructure, third-party services, or systems outside the product's control
- **Personal preference:** Requests that reflect individual taste rather than product problems
- **Power-user specific:** Issues that only affect a sophisticated minority and don't generalize

Also flag: low-frequency but high-severity items that could be easy to dismiss but represent real risk (e.g., data loss, security concerns, billing errors).

### 9. Map themes to product context

If `company/facts/product.md` is available and substantive:
- Connect each theme to a product area
- Note if the theme maps to an existing backlog item or active project
- Flag themes that represent unrecognized needs (no current work addresses them)

If product context isn't available, skip this step and note the limitation.

### 10. Run the smell test

Check for:
- **Smell 5 (False Precision)** — Are you stating frequency or severity with more confidence than the data supports? A theme with 3 mentions in a 15-item sample is directional, not definitive. State confidence honestly.
- **Smell 15 (Recency Bias)** — If longitudinal data exists, are you giving disproportionate weight to the most recent feedback? A declining theme that appeared in 2 items this period but was prominent last period might still matter.

### 11. Prioritize and recommend

Rank themes by impact: **frequency × severity × trend**. A growing, painful, widespread theme outranks a stable, annoying, isolated one.

For the top themes, recommend a next step:
- **Investigate further:** The signal is strong but the cause isn't clear
- **Add to backlog:** The problem is well-understood and solution space is knowable
- **Escalate:** The severity or trend warrants immediate PM attention
- **Monitor:** The signal is real but not yet actionable — track it in the next cycle

---

## Output Format

```markdown
## Feedback Synthesis: [Date Range or Description]

<!-- AGENT BLOCK -->
```yaml
agent_block:
  skill: user-feedback
  theme_count: [integer]
  high_severity_theme_count: [integer — themes with severity Blocking or Painful]
  recommended_action_count: [integer]
  data_quality: [High / Medium / Low]
```
<!-- /AGENT BLOCK -->

### Summary

[Total items analyzed. Source channels. Number of themes identified. The 2-3 most significant themes in one sentence each. Biggest overall signal.]

---

### Themes

#### 1. [Theme Name] — Severity: [Blocking/Painful/Annoying/Cosmetic] | Frequency: [N mentions] | Scope: [Widespread/Moderate/Isolated] | Trend: [Growing/Stable/Declining/New/No baseline]

**What users are saying:** [1-2 sentence synthesis of the theme — the underlying need, not the surface request]

**Representative quotes:**
- "[Quote]" — [Channel, date if available]
- "[Quote]" — [Channel]
- "[Quote]" — [Channel]

**Source distribution:** [Support: N | NPS: N | Reviews: N | Interviews: N | Other: N]

**Product connection:** [Which product area. Existing backlog item? Active project? Known gap? Or "No current work addresses this."]

---

[Repeat for each theme, ordered by priority (frequency × severity × trend)]

---

### Signal vs. Noise

**Likely noise:**
- [Theme or items identified as edge cases, misattributed, or personal preference — with brief explanation of why]

**Low-frequency, high-severity (watch closely):**
- [Items that are rare but represent serious risk — data loss, billing errors, security concerns]

---

### Recommended Actions

1. **[Top priority theme]** — Action: [Investigate / Add to backlog / Escalate / Monitor]. Why: [frequency × severity × trend assessment].
2. **[Second priority]** — Action: [type]. Why: [assessment].
3. **[Third priority]** — Action: [type]. Why: [assessment].

---

### Data Quality Notes

- **Total items:** [N]
- **Source channels:** [list with counts per channel]
- **Date range:** [range, or "not specified"]
- **User segments represented:** [if identifiable, or "not identifiable from the data"]
- **Limitations:** [Small sample, single channel, no longitudinal baseline, channel bias, etc.]

---

### Smell Test

- **Smell 5 (False Precision):** [Finding — are confidence levels appropriate for the sample size?]
- **Smell 15 (Recency Bias):** [Finding — or "No prior synthesis available for comparison" / "Longitudinal balance checked"]

> **Context note:** [State which substantive company files were loaded, which were absent, and which were stub templates. Note what the synthesis might miss without product context or feedback channel context.]
```

---

## Quality Bar

- **Do themes represent product problems, not feature requests?** "Payment history is not discoverable" beats "Users want a receipt button." The synthesis identifies the need, not just the ask.
- **Are frequency and severity assessed, not just listed?** Every theme has a number and a severity level with justification. Not just "several users mentioned this."
- **Are representative quotes actually representative?** Not cherry-picked for drama or softness. The quotes give an honest picture of how users express the theme.
- **Does the synthesis distinguish signal from noise?** Edge cases, misattributed issues, and personal preferences are explicitly flagged. The PM knows what to act on and what to ignore.
- **Is source channel bias acknowledged?** The synthesis doesn't treat support tickets and NPS verbatims as equivalent without noting their different biases.
- **Would the PM trust this enough to take it to a prioritization discussion?** The themes, evidence, and recommended actions are strong enough to inform product decisions — not just a restatement of what customers said.
