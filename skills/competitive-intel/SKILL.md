---
skill: competitive-intel
type: Analyzer
tier: 3
approval: draft-confirm
context-required: []
context-optional:
  - company/facts/competitors.md
  - company/facts/product.md
  - company/norms/communication.md
degradation: proceed-with-caveat
---

# competitive-intel

Analyze competitive signals and produce intelligence that informs product decisions. Two modes: **Monitor** (what changed in the competitive landscape?) and **Deep Dive** (how does a specific competitor approach a specific problem?). Same knowledge base, different depth.

---

## What It Accepts

Any form of competitive information:
- Competitor news, press releases, or announcements (pasted)
- Product teardown notes or screenshots (described)
- A specific question ("How does CompetitorX handle onboarding?")
- Customer feedback mentioning competitors
- G2/Capterra reviews or comparison data
- Job postings, funding announcements, partnership news
- A collection of competitive signals over a period
- A previous competitive-intel synthesis (for longitudinal tracking)
- A combination of the above

---

## Modes

This skill operates in two modes. The PM selects the mode through how they invoke it.

### Monitor

Synthesize recent competitive signals into a landscape snapshot. What moved, what it means, what (if anything) we should do.

**Triggered by:** "what's new with competitors," "competitive update," "what changed in the market," "competitive landscape check," or input that's a batch of competitive signals without a specific question about a specific competitor.

### Deep Dive

Analyze a specific competitor's approach to a specific area. Their solution, positioning, strengths, weaknesses, what we can learn, and what it means for us.

**Triggered by:** "how does [competitor] handle [area]," "analyze [competitor]'s approach to [topic]," "competitive deep dive on [competitor]," "compare our [feature] to [competitor]'s," or a specific question about a specific competitor's approach.

**Requires:** A named competitor and a specific area or problem to analyze. If either is missing, ask: "Which competitor, and what specific area or problem should I analyze?"

**Default:** If the mode is ambiguous, ask: "Do you want a competitive landscape update, or a deep dive on a specific competitor's approach to a specific problem?"

---

## Intake

Applies to **Deep Dive mode only.** Monitor mode has clear enough scope from the input signals — no intake needed.

A competitive deep dive without a decision context produces interesting reading instead of actionable intelligence. Confirm what decision the analysis will inform.

### Signals to Check

- **Competitor:** Named? (Already required for Deep Dive — if missing, the existing ask handles this.)
- **Area or problem:** Specified? (Already required for Deep Dive — if missing, the existing ask handles this.)
- **Decision context:** Does the input say what product decision, positioning question, or strategic choice this deep dive will inform?

### Adaptive Response

**Rich input** (competitor named, area specified, decision context clear): Confirm and proceed. Example: "Deep dive on [Competitor]'s approach to [area], informing our [decision]. Proceeding."

**Moderate input** (competitor and area provided, but no decision context): Ask one targeted question:
- "What decision will this inform — are you evaluating whether to build something similar, thinking about repositioning, or assessing urgency on a current initiative?"

**Thin input** (just a competitor name, or "analyze CompetitorX"): The existing competitor+area ask fires first. Once both are established, if decision context is still absent:

> **To make this actionable, here's what I'd focus the analysis on — adjust if needed:**
>
> - **Lens:** [What seems most relevant — e.g., "How their approach compares to what we're planning for Q3"]
> - **Decision this could inform:** [Best inference — e.g., "Whether our current positioning still differentiates"]
>
> Want me to run with that framing?

---

## Instructions

### Shared Steps (Both Modes)

#### 1. Read the input fully

Absorb all competitive information before classifying or analyzing. Understand what's provided — news, product observations, customer feedback, data — and what the PM is trying to learn.

#### 2. Load reference files

Read these files:
- `references/competitive-analysis.md` — Signal classification, monitoring framework, deep dive structure, source reliability, implications framework, reactivity check
- `references/pm-smell-test.md` — Check for smells 5 (false precision), 14 (options not considered), and 15 (recency bias in analysis)
- `references/agent-readable-output.md` — Agent Block format and shared enum vocabulary

#### 3. Load company context (if available)

If `company/facts/competitors.md` exists and is substantive, read it for the baseline competitive landscape — known competitors, market segments, our advantages and gaps, tracking sources.

If `company/facts/product.md` exists and is substantive, read it for our product positioning, features, and user segments. This is essential for the "compared to us" dimension of any competitive analysis.

If `company/norms/communication.md` exists and is substantive, read it for how competitive intelligence is shared internally — who cares, what format, what level of detail.

If any of these files exist but are still stub templates, treat them as unavailable and say so in the context note.

#### 4. Determine mode

Identify Monitor or Deep Dive from the invocation. If ambiguous, ask.

---

### Monitor Mode

#### 5. Catalog and classify signals

For each competitive signal in the input, classify it per `references/competitive-analysis.md`:

- **Noise** — Routine activity. Minor UI changes, blog posts, small additions that don't change the competitive picture.
- **Signal** — Meaningful change. New pricing tier, significant feature launch, new market entry, major partnership.
- **Strategic shift** — Fundamental direction change. ICP pivot, platform play, pricing model change, major acquisition.

State the classification explicitly for each signal. Don't leave the reader guessing which ones matter.

#### 6. Analyze significant signals

For each signal or strategic shift:
- **What happened:** State the factual change
- **What it means:** Interpret the competitive significance
- **Action warranted?** Respond / Monitor / Ignore (per `references/competitive-analysis.md` reactivity framework)
- **Threat Severity:** High (directly threatens current revenue, user base, or positioning), Medium (meaningful competitive pressure but manageable), or Low (worth noting but not threatening)
- **Urgency:** Immediate (days) — response needed within days; Near-term (1-2 sprints) — address within 1-2 sprints; Strategic (quarter+) — factor into quarterly planning; None — no action needed

If the input includes information about the source (press release vs. product teardown vs. customer mention), note the source reliability.

After completing all signal analysis, populate the Monitor mode Agent Block: count high-severity signals, count signals with Action: Respond, and set max_urgency to the most urgent action signal across all signals.

#### 7. Assess overall landscape

Step back from individual signals and assess the landscape direction:
- **Overall:** Stable / Shifting / Disrupting
- **Key trend:** The single most important pattern across all signals
- **Market direction:** Is the competitive set consolidating, fragmenting, or being disrupted?

#### 8. Compare to prior snapshot

If a previous competitive-intel synthesis is provided, note what changed:
- New signals that weren't present before
- Signals that escalated (noise → signal, signal → strategic shift)
- Previously flagged items that resolved or de-escalated

If no prior snapshot exists, state "First monitoring snapshot — no prior baseline for comparison."

#### 9. Run the smell test (Monitor mode)

- **Smell 15 (Recency Bias)** — Is one recent, loud signal dominating your analysis? A competitor's flashy launch announcement doesn't automatically outweigh a quieter pricing change that's strategically more important. Weight by significance, not by recency.
- **Smell 5 (False Precision)** — Are you stating competitor strategy as fact when it's inference? "CompetitorX is pivoting to enterprise" is a strong claim. If the evidence is two enterprise-focused job postings, state it as a hypothesis, not a conclusion.

---

### Deep Dive Mode

#### 5. Identify competitor and area

Name the competitor and the specific area or problem being analyzed. If the PM provided both, proceed. If either is missing, ask.

#### 6. Analyze their approach

Follow the deep dive framework in `references/competitive-analysis.md`:

- **Their approach:** What they built, how it works, who it's for, how they position it. Base this on observable evidence (product teardown, documentation, customer reports), not marketing claims.
- **Strengths:** Where their approach genuinely works well. Be honest — if they're better at something, say so.
- **Weaknesses:** Where their approach falls short. Be specific — cite evidence, not assumptions.

#### 7. Compare to our approach

Go beyond feature comparison to philosophical comparison:
- What trade-offs did they make vs. what trade-offs did we make?
- Where are we genuinely stronger? Where are they genuinely stronger?
- What are the meaningful differences in approach, not just feature presence?

If `company/facts/product.md` is available, ground the comparison in our actual product. If not, note that the comparison is limited by unavailable product context.

#### 8. Identify learnings

What can we learn from their approach? This is not "copy this feature." It's:
- Principles or techniques worth considering
- Problems they've validated that we hypothesized about
- Approaches that surprised us — either positively or negatively
- What their user reception tells us about the problem space

#### 9. Assess strategic implications

Per the implications framework in `references/competitive-analysis.md`:
- **Product:** Does this change what we should build or when?
- **Positioning:** Does this change how we differentiate?
- **Urgency:** Does this increase or decrease urgency on any current initiative?
- **Risk:** Does this introduce a new risk?

If all answers are "no," say so. "No action needed" is a valid conclusion.

After writing the four-dimension prose assessment, translate each to a structured enum for the Agent Block:
- `product_implication`: Act now (build or accelerate something) / Watch (monitor for when it becomes actionable) / No change
- `positioning_implication`: Differentiate (sharpen differentiation) / Adjust (update positioning) / Holds (current positioning still works)
- `urgency`: Immediate (days) / Near-term (1-2 sprints) / Strategic (quarter+) / None
- `risk_level`: High / Medium / Low / None

#### 10. Run the smell test (Deep Dive mode)

- **Smell 14 (Options Not Considered)** — Is the deep dive only evaluating whether we should react to the competitor? Consider also: what can we learn from them? What did they validate for us? What did they get wrong that we should avoid?
- **Smell 5 (False Precision)** — Are claims about the competitor's strategy sourced or inferred? Distinguish observable facts (they launched X, their pricing page says Y) from inferences (they appear to be targeting Z). State the basis for each claim.

---

## Output Format

### Monitor Mode

```markdown
## Competitive Update: [Period or Description]

### Summary

[Overall landscape assessment in 2-3 sentences. Most significant development. Landscape direction: Stable / Shifting / Disrupting.]

<!-- AGENT BLOCK -->
```yaml
agent_block:
  skill: competitive-intel
  mode: Monitor
  landscape_status: [Stable / Shifting / Disrupting]
  high_severity_signal_count: [integer]
  respond_action_count: [integer — number of signals with Action: Respond]
  max_urgency: [Immediate (days) / Near-term (1-2 sprints) / Strategic (quarter+) / None]
```
<!-- /AGENT BLOCK -->

---

### Significant Signals

#### [Competitor Name]

| Signal | Classification | Source |
|--------|---------------|--------|
| [What happened] | [Signal / Strategic shift] | [Where you learned this] |

**What it means:** [Interpretation — competitive significance]
**Action:** [Respond / Monitor / Ignore] — [Why]
**Threat Severity:** [High / Medium / Low]
**Urgency:** [Immediate (days) / Near-term (1-2 sprints) / Strategic (quarter+)]

---

[Repeat per competitor with significant signals]

---

### Noise (Noted, No Action)

- **[Competitor]:** [What happened] — [Why it's noise]
- ...

---

### Landscape Assessment

**Overall:** [Stable / Shifting / Disrupting]
**Key trend:** [The most important pattern across all signals]
**Market direction:** [Consolidating / Fragmenting / Being disrupted / Stable]

---

### Changes Since Last Update

- [What shifted since the last competitive snapshot — or "First monitoring snapshot, no prior baseline"]

---

### Recommended Actions

- [Specific actions if warranted — or "No action needed based on current signals"]

---

### Smell Test

- **Smell 15 (Recency Bias):** [Finding — or "Balanced — no single signal dominating the analysis"]
- **Smell 5 (False Precision):** [Finding — or "Clear — claims distinguished as observed vs. inferred"]

> **Context note:** [State which substantive company files were loaded, which were absent, and which were stub templates. Note what the analysis might miss without competitive baseline context.]
```

### Deep Dive Mode

```markdown
## Competitive Deep Dive: [Competitor] — [Area/Problem]

### Summary

[2-3 sentences. How they approach this area. Their key strength. Their key weakness. What it means for us.]

---

### Their Approach

[What they built. How it works. Who it's for. How they position it. Ground this in evidence — product observations, documentation, user reports — not marketing claims.]

---

### Strengths

- **[Strength]** — [Evidence. Why this matters.]
- ...

### Weaknesses

- **[Weakness]** — [Evidence. Why this matters.]
- ...

---

### Comparison to Our Approach

| Dimension | Them | Us | Assessment |
|-----------|------|-----|-----------|
| [Relevant dimension] | [Their approach] | [Our approach] | [Who's stronger and why] |
| ... | ... | ... | ... |

**Philosophical difference:** [The underlying trade-off or design philosophy that explains the different approaches — not just "they have X, we don't"]

---

### What We Can Learn

- [Principle or technique worth considering — not "copy this feature"]
- [What they validated that we hypothesized about]
- ...

---

### Strategic Implications

- **Product:** [Change what we build or when? Or no change needed.]
- **Positioning:** [Change how we differentiate? Or current positioning holds.]
- **Urgency:** [Increase or decrease urgency on any initiative? Or no change.]
- **Risk:** [New risk introduced? Or no new risk.]

**Bottom line:** [One sentence — what to do with this intelligence]

<!-- AGENT BLOCK -->
```yaml
agent_block:
  skill: competitive-intel
  mode: Deep Dive
  competitor: "[Competitor name]"
  area: "[Area analyzed]"
  product_implication: [Act now / Watch / No change]
  positioning_implication: [Differentiate / Adjust / Holds]
  urgency: [Immediate (days) / Near-term (1-2 sprints) / Strategic (quarter+) / None]
  risk_level: [High / Medium / Low / None]
  bottom_line: "[Repeat of Bottom line sentence]"
```
<!-- /AGENT BLOCK -->

---

### Smell Test

- **Smell 14 (Options Not Considered):** [Finding — or "Analysis considered learning from them, not just reacting"]
- **Smell 5 (False Precision):** [Finding — or "Clear — observed facts and inferences distinguished"]

> **Context note:** [State which substantive company files were loaded, which were absent, and which were stub templates. Note what the analysis might miss without product context for comparison.]
```

---

## Quality Bar

- **Does monitoring mode distinguish signal from noise?** Not everything a competitor does matters. The analysis explicitly classifies each signal and dismisses noise. The PM knows what to pay attention to and what to ignore.
- **Does the deep dive go beyond feature comparison?** It analyzes approach, positioning, trade-offs, and strategic implications — not just "they have X, we don't." The PM understands the competitor's thinking, not just their feature list.
- **Are claims sourced or flagged as inference?** Observable facts are stated as facts. Inferences about strategy are flagged as inferences with the basis noted. The PM can assess the reliability of each claim.
- **Would this change how the PM thinks about the competitive landscape?** The analysis informs decisions — positioning, roadmap, urgency — not just "here's what competitors did." If no action is needed, it says so.
- **Is reactivity checked?** The analysis doesn't recommend panic in response to a single competitor move. It assesses whether action, noting, or ignoring is the right response. Pattern matters more than recency.
- **Is the analysis honest about our position?** Where the competitor is genuinely stronger, the analysis says so. Competitive intelligence that only highlights competitor weaknesses is cheerleading, not intelligence.
