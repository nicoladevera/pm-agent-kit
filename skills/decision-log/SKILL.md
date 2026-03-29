---
skill: decision-log
type: Generator
tier: 2
approval: draft-confirm
context-required: []
context-optional:
  - company/norms/decisions.md
  - company/facts/team.md
  - company/facts/product.md
degradation: proceed-with-caveat
---

# decision-log

Capture a decision that's been made or structure a decision that needs to be made. A decision log that someone can't understand six months later failed at its only job. An escalation brief is a decision log for a decision that hasn't been made yet.

---

## What It Accepts

Any form of input that contains or implies a decision:
- A description of a decision that was already made
- A problem that needs a decision (context, options, constraints)
- Meeting notes where a decision was reached
- A Slack thread debating options
- A verbal download about a tricky call

The input does not need to be structured. This skill imposes structure while preserving the substance.

---

## Instructions

### 1. Read the input fully

Understand the situation before structuring anything. Identify: what is the decision (or what decision is needed)? Who is involved? What options exist or were considered? What reasoning is present?

### 2. Determine the mode

The mode depends on the input, not on a flag:

- **Capture** — A decision has already been made. The input contains the outcome, even if it's buried in discussion. Your job: extract the decision, the reasoning, and the alternatives that were considered.
- **Structure** — A decision needs to be made. The input describes a problem or a choice facing the PM. Your job: frame the decision, lay out options, assess reversibility, and state a recommendation if the input provides enough signal.

If the input is ambiguous — it's unclear whether a decision was reached — ask: "Was this decided, or is this still pending?"

### 3. Load reference files

Read these files:
- `references/decision-frameworks.md` — Decision anatomy, options quality, reversibility assessment, escalation signals
- `references/pm-smell-test.md` — Check for Decision and Strategy Smells 14 (options not considered) and 15 (recency bias)
- `references/pushback-and-negotiation.md` — For escalation framing in Structure mode
- `references/agent-readable-output.md` — Agent Block format and shared enum vocabulary

### 4. Load company context (if available)

If `company/norms/decisions.md` exists and is substantive, read it for how decisions are made and documented at this company — authority levels, escalation paths, RFC/ADR conventions.

If `company/facts/team.md` exists and is substantive, read it for who the key decision-makers and stakeholders are.

If `company/facts/product.md` exists and is substantive, read it for product context that informs the decision.

If any of these files exist but are still stub templates, treat them as unavailable and say so in the output.

If no substantive company context is available, proceed — note the absence in the output.

### 5. For capture mode: extract the decision structure

From the input, extract:
- **The decision** — What was decided. State it as a clear, unambiguous sentence.
- **The decider** — Who made the call. Not "the team" — a person.
- **The context** — Why this decision was needed. What prompted it.
- **The options considered** — What alternatives were on the table, including any that were rejected. If the input doesn't mention alternatives, flag the gap: "No alternatives discussed in the input — consider documenting what else was considered."
- **The rationale** — Why this option was chosen over the others.
- **Implications** — What changes as a result. Who needs to know. What downstream work this creates.

### 6. For structure mode: frame the decision

- **Frame the question** — State the decision as a specific, answerable question. Problem-first, not solution-first: "How do we reduce first-payment miss rates?" not "Should we build a notification system?"
- **Lay out options** — At least 2 genuine alternatives. Always consider "do nothing" as an explicit option. For each option: what it involves, pros, cons, and reversibility.
- **Assess reversibility** — Is this a one-way door or a two-way door? Name it explicitly.
- **State a recommendation** — If the input provides enough signal, come with a point of view. State it directly. Name the reasoning. Acknowledge what's given up. If there isn't enough signal for a recommendation, say so and name what information would be needed.
- **Name the decider and timeline** — Who should make this decision and by when. If the input doesn't specify, flag it.

**For escalation decisions** — where the decision needs executive ownership or crosses organizational levels — frame as a fork per `references/pushback-and-negotiation.md`: name the paths, the consequences of each, and the specific commitment being asked for. Don't escalate as complaint; escalate as "here's the fork and here's who needs to choose."

### 7. Run the smell test

Check for:
- **Smell 14 (Options Not Considered)** — Is the decision presented as the only option? Are alternatives genuinely explored or are they strawmen?
- **Smell 15 (Recency Bias)** — Is the decision driven by what just happened rather than a durable pattern?
- **Missing "why"** — Is the reasoning clear, or does the log just record what was decided without explaining why?

### 8. Surface open items

List anything unresolved: downstream decisions this creates, information that's still needed, stakeholders who need to be informed.

### 9. Populate the Agent Block

Fill in the Agent Block fields from the completed log:
- `decision_status`: matches the Status field (Decided / Pending)
- `decision`: the one-sentence statement from the Decision section
- `confidence`: the conviction level from the Rationale — if not explicitly stated, infer from evidence strength (strong evidence with clear rationale = 7–9, mixed evidence = 5–6, thin evidence or speculation = 3–4)
- `reversibility`: from the Options table Reversibility column for the chosen option
- `primary_tradeoff`: the key con from the Options table for the chosen option, stated as one sentence

---

## Output Format

````markdown
## Decision Log: [Decision Title]

**Status:** Decided / Pending
**Date:** [Decision date or target decision date]
**Decider:** [Who made or should make this decision]

<!-- AGENT BLOCK -->
```yaml
agent_block:
  skill: decision-log
  decision_status: [Decided / Pending]
  decision: "[One sentence — what was decided or recommended]"
  confidence: [1-10]
  reversibility: [One-way door / Two-way door]
  primary_tradeoff: "[One sentence — what was given up by choosing this option]"
```
<!-- /AGENT BLOCK -->

---

### Context

[Why this decision matters. What prompted it. What's at stake. 2-3 sentences that orient a reader who has no background.]

---

### Decision

[For capture mode: What was decided. One clear statement.]
[For structure mode: What is recommended. One clear statement with reasoning.]

---

### Options Considered

| Option | Pros | Cons | Reversibility |
|--------|------|------|---------------|
| [Option 1 — chosen/recommended] | [What you gain] | [What it costs or risks] | [One-way / Two-way door] |
| [Option 2] | ... | ... | ... |
| [Do nothing] | ... | ... | ... |

**Decision fork** *(include when 3 or more options were considered or the trade-off is non-obvious; omit if the table above makes the fork self-evident)*

```
                 [Decision Point]
                /        |        \
        [Option 1]  [Option 2]  [Do Nothing]
        CHOSEN      [Key diff]  Accepted
                                risk: [X]
```

Label the differentiating factor on each branch (cost, speed, risk, reversibility).

---

### Rationale

[Why this option over the others. What criteria mattered most. What trade-offs were accepted.]

---

### Implications

- [What changes as a result of this decision]
- [Who needs to know]
- [What downstream work this creates or unblocks]

---

### Open Items

- [Anything still unresolved — follow-up decisions, missing information, stakeholders to inform]

> **Context note:** [State which substantive company files were loaded, which files were absent, and which files existed but were stub templates and therefore skipped. Note what the log might miss without that context.]
````

---

## Quality Bar

- **Could someone understand this six months from now?** The decision, the reasoning, and the alternatives are clear to a reader with no prior context.
- **Are alternatives genuinely considered?** At least 2 real options with honest trade-offs — not strawmen designed to make the chosen option look good.
- **Is the reasoning specific to this decision?** Not generic decision-making advice, but the actual factors that drove this particular choice.
- **Is reversibility assessed?** The reader knows whether this is a one-way door requiring careful consideration or a two-way door where speed matters more than deliberation.
- **If pending: is the path to resolution clear?** Who decides, by when, and what information they need. The brief is ready for the decider to decide, not to investigate.

---

## Save

After producing the artifact, write it to `knowledge/decisions/` using the naming convention: `YYYY-MM-DD-decision-slug.md`, where `YYYY-MM-DD` is today's date and `decision-slug` is a lowercase hyphenated slug derived from the decision title. Report the saved file path in the conversation.
