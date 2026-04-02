---
name: roadmap-prioritization
description: Compares initiative candidates, sequences work, and produces prioritization rationale with explicit trade-offs. Use when asked to "prioritize the roadmap", "help me decide what to build next", "compare these initiatives", "sequence our work", or "roadmap planning".
metadata:
  type: Generator
  tier: 4
  approval: draft-confirm
  context-required: []
  context-optional:
    - company/facts/product.md
    - company/facts/team.md
    - company/facts/customers.md
    - company/norms/decisions.md
  degradation: proceed-with-caveat
---

# roadmap-prioritization

Compare candidate initiatives, sequence work, manage opportunity cost, and explain why A beats B. This is the middle layer between strategy (business cases, competitive intelligence, discovery results) and execution (PRDs, sprint plans, task generation). The output is not a roadmap document — it's the prioritization rationale: which bets, in what order, and why. The roadmap document itself is a communication artifact that `presentation-deck` can produce downstream.

The core question is never "is this valuable?" — everything on a candidate list has some value. The question is: "Given these goals, these constraints, and this evidence, what is the best sequence and what are we choosing not to do?"

---

## What It Accepts

Any form of initiative comparison context:
- A list of candidate initiatives with varying levels of detail (business cases, rough pitches, one-liners)
- Business cases from `knowledge/business-cases/`
- Discovery plan results from `knowledge/discovery-plans/`
- OKRs, strategic themes, or planning goals that the roadmap should serve
- Capacity or resource constraints
- Stakeholder input — who's pushing for what and why
- Data analyses, user feedback syntheses, or competitive snapshots that inform the comparison
- A combination of the above

The input can be messy and uneven — some candidates will have full business cases, others will be a sentence from a stakeholder. The skill normalizes the comparison and flags evidence gaps.

---

## Intake

A prioritization rationale built on unstated goals or missing constraints produces confident recommendations that don't survive contact with reality. Confirm the comparison frame before sequencing.

### Signals to Check

- **Candidates:** Are the candidate initiatives named? Or does the PM need help generating the candidate list?
- **Goals/OKRs:** What is the team optimizing for? Revenue growth, retention, platform capability, market expansion? If goals aren't stated, the prioritization has no anchor.
- **Constraints:** Is capacity stated? Are there timeline constraints, stakeholder commitments, or dependency blockers?
- **Evidence quality:** For each candidate, what evidence exists? Business cases, user research, data analysis — or gut feel?
- **Audience:** Who will see this rationale? The team (for alignment), leadership (for approval), cross-functional stakeholders (for coordination)?

### Adaptive Response

**Rich input** (candidates listed, goals stated, constraints named, evidence referenced): Restate the comparison frame. Confirm the most consequential inference — usually the primary optimization goal. Example: "Comparing [N] candidates against [stated goals], with [capacity constraint]. I'll assess evidence quality per candidate and sequence based on impact, dependencies, and time sensitivity. Proceeding."

**Moderate input** (candidates present but goals or constraints unclear): Ask up to 3 targeted questions. Examples:
- "What's the primary goal this quarter — revenue growth, retention, reducing tech debt, or something else? The ranking changes depending on what you're optimizing for."
- "What's the realistic engineering capacity for new work this quarter? Or should I flag capacity as an open item?"
- "Are there any commitments already made — things leadership has promised or dependencies other teams are counting on?"

**Thin input** (a vague area, or "help me prioritize our roadmap"): Present a structured interpretation:

> **Here's how I'd frame this — tell me what needs adjusting:**
>
> - **Candidates I see:** [Extracted from whatever context was provided]
> - **Goals (inferred):** [Best inference of what the team is optimizing for]
> - **Constraints (inferred):** [Any capacity, timeline, or commitment constraints visible]
> - **Evidence quality:** [Quick read on which candidates have strong evidence vs. thin evidence]
>
> Anything off? Especially the goals — the ranking depends heavily on what we're optimizing for. I'll adjust before prioritizing.

---

## Instructions

### 1. Read the input fully

Absorb all initiative context, goals, constraints, and stakeholder dynamics before structuring. Understand what's being compared, what the team is optimizing for, and what evidence exists for each candidate. Note unevenness — some candidates will have business cases, others will have a single sentence.

### 2. Load reference files

Read these files:
- `references/prioritization-judgment.md` — Opportunity cost framework, candidate comparison anatomy, sequencing heuristics, framework traps, stakeholder communication patterns, constraint-based prioritization
- `references/business-case-standards.md` — Impact sizing frameworks and evidence quality standards (for evaluating candidates that have business cases)
- `references/decision-frameworks.md` — Reversibility assessment, options quality, recommendation standards
- `references/pm-smell-test.md` — Check for smells 1 (missing why), 5 (false precision), and 14 (options not considered)
- `references/agent-readable-output.md` — Agent Block format and shared enum vocabulary

### 3. Load company context (if available)

If `company/facts/product.md` exists and is substantive, read it for product landscape, strategic focus, and current priorities. This grounds the comparison in the actual product context.

If `company/facts/team.md` exists and is substantive, read it for team structure, capacity, and ownership. This informs constraint-based prioritization and dependency assessment.

If `company/facts/customers.md` exists and is substantive, read it for customer segments, ICP definitions, and known pain points. This enables more specific impact assessment per candidate.

If `company/norms/decisions.md` exists and is substantive, read it for how the company evaluates and approves priorities — decision criteria, approval process, and planning cadence.

If any of these files exist but are still stub templates, treat them as unavailable and say so in the context note.

### 4. Catalog candidates

For each candidate initiative, build a consistent profile using the comparison anatomy from `references/prioritization-judgment.md`:

- **Problem:** What problem does this solve? For whom?
- **Evidence quality:** Validated (research/data), Inferred (adjacent data), Assumed (gut feel), or None
- **Expected impact:** What happens if this succeeds? (range if possible)
- **Estimated cost:** Engineering, opportunity cost, ongoing maintenance
- **Dependencies:** What does this depend on? What does it unlock?
- **Reversibility:** One-way door or two-way door?
- **Time sensitivity:** Closing window, competitive pressure, regulatory deadline?
- **Cost of waiting:** What happens if we do this next quarter instead?

When the input is uneven — some candidates have full business cases, others have a sentence — normalize by building the same profile for each. Flag where the profile is inferred vs. stated. The unevenness itself is information: a well-evidenced candidate should be weighted differently than one running on assumption.

### 5. Identify goals and constraints

Establish the optimization frame:

- **Goals:** What is the team optimizing for? Name the specific OKRs, strategic themes, or success criteria. If goals aren't stated in the input, infer from context and flag for confirmation.
- **Capacity constraints:** How much engineering capacity is available for new work? Account for overhead, maintenance, and support. If not stated, flag as an open item — the prioritization changes significantly based on capacity.
- **Existing commitments:** Are there promises already made, dependencies other teams are counting on, or stakeholder expectations that constrain the solution space?
- **Tech debt allocation:** Is there a reserved allocation for tech debt and infrastructure? If not, recommend one — making tech debt compete with features in the same prioritization guarantees it always loses.

### 6. Compare candidates

Structured comparison across all candidates on the same dimensions. Per `references/prioritization-judgment.md`:

- Compare on problem severity, evidence quality, expected impact, cost, dependencies, reversibility, time sensitivity, and cost of waiting
- Flag where evidence quality differs — a gut-feel initiative should not compete on equal footing with one backed by production data and user research
- Name the trade-offs explicitly: choosing A means not doing B, and here's what that costs
- If a scoring framework (RICE, WSJF, etc.) would be useful as a structured discussion tool, use it — but don't let the score become the answer. Show the reasoning alongside or instead of the numbers.

### 7. Apply sequencing heuristics

After comparison, determine the order using the sequencing heuristics from `references/prioritization-judgment.md`:

1. **Dependencies** — what gates what? Enabling dependencies override raw priority.
2. **Learning value** — what reduces uncertainty for later decisions? Front-load research and discovery when evidence quality is uneven.
3. **Reversibility** — two-way doors before one-way doors, all else being equal.
4. **Time sensitivity** — closing windows override other heuristics, but verify the window is real.
5. **Context-switching cost** — prefer completing one initiative before starting the next.

Show the sequencing logic — don't just present the final order. The reader should understand why #2 is sequenced before #1 if that's the recommendation.

### 8. Produce recommendation

State the recommended sequence directly. For each initiative in the recommended order:
- Why this position (what makes it the right priority relative to alternatives)
- What it depends on (prerequisites, evidence quality)
- What you lose by waiting (cost of delay, if any)
- What it unlocks (downstream initiatives or decisions)

For initiatives recommended for deferral, use the framing patterns from `references/prioritization-judgment.md`: "not now, not never," "conditional yes," "evidence gap," or "different bet." Each deferred initiative should have a clear path to reconsideration.

### 9. Name what's cut

Explicitly state what's NOT being done and why. Per `references/prioritization-judgment.md`, this is as important as what IS being done. For each cut or deferred initiative:
- Name it specifically
- State why it's deprioritized (lower impact, weaker evidence, dependency on something else, capacity constraint)
- Name what would change the decision (new evidence, freed capacity, changed goals)

A prioritization rationale without a "what we're not doing" section hasn't prioritized — it's made a list.

### 10. Stress-test the sequence

Pressure-test the recommended prioritization from three angles:

#### Premortem
*"It's 6 months from now and this prioritization was wrong. What happened?"*

Generate 3-5 specific failure modes. For each:
- State the failure scenario concretely (e.g., "We prioritized the retention initiative but the real problem was acquisition — retention was a symptom, not the cause")
- Assess likelihood and impact
- Note whether the sequencing has any built-in hedges against this failure

#### Blindspot Check
*"What am I not seeing? What assumptions is this prioritization built on?"*

Identify at least 2 unexamined assumptions:
- Goal assumptions (are we optimizing for the right thing?)
- Evidence assumptions (is the evidence quality assessment accurate?)
- Constraint assumptions (is the capacity estimate realistic? Are the dependencies correct?)
- Market assumptions (will the competitive landscape hold still while we execute?)

#### Conviction Assessment
*"How confident am I in this sequence? What would change it?"*

State a conviction level (1-10) with rationale. Name 2-3 specific conditions that would change the recommended sequence. Distinguish between changes that would reorder initiatives vs. changes that would add or remove candidates entirely.

### 11. Run the smell test

Check for:
- **Smell 1 (Missing Why):** Does the rationale establish why this sequence serves the stated goals? Would someone outside the team understand the logic?
- **Smell 5 (False Precision):** Are impact estimates presented honestly given the evidence quality? Or are rough guesses presented as precise forecasts?
- **Smell 14 (Options Not Considered):** Are all candidates compared fairly? Is the "what we're not doing" section honest?

### 12. Populate the Agent Block

After completing the smell test, fill in the Agent Block:
- `candidate_count`: total initiatives compared
- `recommended_count`: initiatives recommended for the current period
- `deferred_count`: initiatives explicitly deferred or cut
- `confidence`: conviction level (1-10) from the stress test
- `primary_goal`: the primary optimization goal the sequence serves
- `highest_risk`: the biggest risk to the recommended sequence (from the premortem)
- `evidence_gaps`: number of candidates with Assumed or None evidence quality

### 13. Flag open items

List everything the PM needs to resolve:
- Capacity data that needs validation
- Evidence gaps that should be filled before committing (connect to `discovery-plan` where appropriate)
- Stakeholder alignment needed — whose buy-in is required for the sequence?
- Dependencies on other teams that haven't been confirmed
- Commitments that may conflict with the recommended sequence
- Decisions the prioritization depends on but hasn't resolved

---

## Output Format

````markdown
## Prioritization Rationale: [Planning Period or Context — e.g., "Q2 2026 Roadmap" or "Platform vs. Growth Investment"]

**Status:** Draft
**Date:** [Current date]
**Candidates compared:** [N initiatives]
**Primary goal:** [What the team is optimizing for — stated directly]

<!-- AGENT BLOCK -->
```yaml
agent_block:
  skill: roadmap-prioritization
  candidate_count: [integer]
  recommended_count: [integer]
  deferred_count: [integer]
  confidence: [1-10]
  primary_goal: "[One sentence — what the sequence optimizes for]"
  highest_risk: "[One sentence — biggest risk to the sequence]"
  evidence_gaps: [integer — candidates with Assumed or None evidence]
```
<!-- /AGENT BLOCK -->

---

### Goals and Constraints

**Optimizing for:** [Named goals, OKRs, or strategic themes]

**Capacity:** [Available engineering capacity for new work — after overhead, maintenance, support. State the assumption.]

**Existing commitments:** [Promises or dependencies that constrain the solution space]

**Tech debt allocation:** [Reserved capacity, if any — or recommendation to reserve it]

---

### Candidate Comparison

#### [Initiative 1 Name]

| Dimension | Assessment |
|-----------|-----------|
| Problem | [What problem, for whom, how severe] |
| Evidence quality | [Validated / Inferred / Assumed / None — with basis] |
| Expected impact | [Range if possible — revenue, users, retention, strategic value] |
| Estimated cost | [Engineering + opportunity cost + ongoing] |
| Dependencies | [What it depends on; what it unlocks] |
| Reversibility | [One-way door / Two-way door] |
| Time sensitivity | [Closing window? Competitive pressure?] |
| Cost of waiting | [What happens if deferred one quarter?] |

[Repeat for each candidate]

---

### Recommended Sequence

**1. [Initiative Name]** — [Why this is #1. What it depends on. What it unlocks. Cost of delay.]

**2. [Initiative Name]** — [Why #2. How it relates to #1. Dependencies and unlocks.]

**3. [Initiative Name]** — [Why #3. Sequencing rationale.]

[Continue for all recommended initiatives]

---

### What We're Not Doing

#### [Deferred Initiative Name]
**Why not now:** [Specific reason — lower impact, weaker evidence, dependency, capacity constraint]
**What would change this:** [Condition for reconsideration — new evidence, freed capacity, changed goals]
**Framing:** [Not now/not never | Conditional yes | Evidence gap | Different bet]

[Repeat for each deferred or cut initiative]

---

### Stress Test

#### Premortem
*"It's 6 months from now and this prioritization was wrong. What happened?"*

1. [Failure mode 1] — [Likelihood. Impact. Whether the sequence hedges against it.]
2. [Failure mode 2] — ...
3. [Failure mode 3] — ...

#### Blindspot Check
*"What am I not seeing?"*

- **[Assumption category]:** [Unexamined assumption. What happens if it's wrong.]
- **[Assumption category]:** [Unexamined assumption. What happens if it's wrong.]

#### Conviction
**Confidence level:** [1-10] — [Brief rationale]
**What would change the sequence:**
- [Condition 1 — what changes and how]
- [Condition 2 — what changes and how]

---

### Open Items

- [Capacity data that needs validation]
- [Evidence gaps — candidates that need discovery before committing]
- [Stakeholder alignment needed]
- [Cross-team dependencies not yet confirmed]
- [Decisions this prioritization depends on]

---

### Smell Test

- **Smell 1 (Missing Why):** [Finding — or "Clear — goals stated, sequence rationale transparent"]
- **Smell 5 (False Precision):** [Finding — or "Clear — impact estimates calibrated to evidence quality"]
- **Smell 14 (Options Not Considered):** [Finding — or "Clear — all candidates compared; what's not being done is named"]

> **Context note:** [State which substantive company files were loaded, which were absent, and which were stub templates. Note how missing context may have affected the quality of impact assessment, capacity estimation, or dependency mapping.]
````

---

## Quality Bar

- **Does the rationale explain why A beats B?** Each recommended initiative is compared against the alternatives, not evaluated in isolation. The reader understands why this sequence, not just what the sequence is.
- **Is evidence quality visibly weighted?** Candidates backed by production data and research are treated differently from those backed by stakeholder conviction or assumption. The weighting is transparent.
- **Is the "what we're not doing" section substantive?** Deferred initiatives have specific reasons, reconsideration conditions, and honest framing. Not a perfunctory "these didn't make the cut."
- **Does the sequence reflect dependencies and learning value?** The order accounts for what gates what, what reduces uncertainty for later decisions, and what has closing windows — not just raw priority.
- **Is the stress test specific to this prioritization?** The premortem surfaces failure modes specific to this sequence (not generic risks). The blindspot check names assumptions the sequence is built on. Conviction is calibrated to evidence quality.
- **Would a VP read this and understand the trade-offs?** The rationale is self-contained. A reader who disagrees can point to exactly where they disagree — the goals, the evidence assessment, the sequencing logic, or the trade-offs.
- **Does the comparison handle unevenness honestly?** When candidates have different evidence levels, the rationale names the gap rather than normalizing it. "Invest in discovery before committing" is a valid recommendation for low-evidence candidates.
- **Are constraints stated explicitly?** Capacity, commitments, tech debt allocation, and dependency chains are visible. The reader understands what's driving the constraints, not just the conclusions.

---

## Save

After producing the artifact, write it to `knowledge/roadmaps/` using the naming convention: `YYYY-QN-prioritization-rationale.md`, where the quarter reflects the planning period. For non-quarterly prioritization exercises, use `YYYY-MM-DD-context-prioritization-rationale.md`. Report the saved file path in the conversation.
