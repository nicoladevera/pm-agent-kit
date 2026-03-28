---
skill: prd-draft
type: Generator
tier: 1
approval: draft-confirm
context-required: []
context-optional:
  - company/facts/product.md
  - company/facts/customers.md
  - company/norms/team-process.md
degradation: proceed-with-caveat
---

# prd-draft

Draft a PRD from a problem statement, user context, and constraints. The skill's job is to impose structure on rough thinking — not to require structured input.

The same quality criteria that `doc-review` evaluates against are the criteria this skill generates toward. A prd-draft output should be good enough that the PM spends time sharpening the thinking, not formatting the document.

---

## What It Accepts

Any form of rough input:
- A problem description in plain language
- Meeting notes or a Slack thread
- Bullet points or rough notes
- A verbal download captured as text
- A partial draft that needs structure

The input does not need to be organized. This skill produces the organization.

---

## Intake

Before drafting, confirm alignment on the three things that most determine PRD quality: the problem, who it's for, and what success looks like.

### Signals to Check

- **Problem or pain point:** Is a specific user problem stated, or does the input lead with a solution?
- **User segment:** Is there a named audience (even rough), or is it implicit/absent?
- **Success definition:** Is there any signal of what "working" looks like — a metric, a behavior change, a business outcome?
- **Scope signal:** Is there any indication of what's in vs. out, or is the scope unbounded?

### Adaptive Response

**Rich input** (problem stated, user segment named, success hinted, scope bounded): Restate in 1-2 sentences and proceed. Example: "Got it — the problem is [X] for [user segment], success looks like [Y], scoped to [Z]. Drafting now."

**Moderate input** (some signals present, some gaps): Ask up to 3 targeted questions on the gaps. Examples:
- "Who's the primary user segment — [inferred option A] or [option B]?"
- "What does success look like here — are we measuring [metric A], [behavior B], or something else?"
- "Is [adjacent capability] in scope, or should I keep this focused on [core capability]?"

**Thin input** (a sentence, a solution without a problem, or a vague area): Present a structured interpretation:

> **Here's what I'm hearing — correct me where I'm wrong:**
>
> - **Problem:** [Translated to a problem statement, even if input was solution-first]
> - **Who's affected:** [Best inference from context]
> - **Success looks like:** [Best inference — or "I don't have a read on this yet"]
> - **Scope:** [What I'd include / exclude based on the input]
>
> Should I draft from this, or does anything need adjusting?

---

## Instructions

### 1. Read the input fully

Understand the problem, the user context, the constraints, and any solution hints the PM has provided. Don't start structuring until you've absorbed the full input. Note what's present and what's missing.

### 2. Load reference files

Read these files — they define what the output must satisfy:
- `references/prd-quality-criteria.md` — Generate toward all 9 criteria
- `references/acceptance-criteria.md` — AC must meet these standards (Given/When/Then, agent-implementable)
- `references/agent-readable-output.md` — Agent Block format and shared enum vocabulary

### 3. Load company context (if available)

If `company/facts/product.md` exists and is substantive, read it for product landscape and existing functionality. This helps the PRD reference adjacent systems and avoid re-specifying what already exists.

If `company/facts/customers.md` exists and is substantive, read it for customer segments, pain points, jobs-to-be-done, and buyer vs. user dynamics. This grounds user stories in actual customer context rather than inferred segments.

If `company/norms/team-process.md` exists and is substantive, read it for how PRDs are expected to work at this company — what sections are standard, what level of detail engineering expects.

If either file exists but is still a stub template, treat it as unavailable and say so in the output.

If neither substantive file is available, proceed — note the absence in the output.

### 4. Generate the PRD

Produce a complete draft satisfying all 9 criteria from `references/prd-quality-criteria.md`. Every section should contain real content, not placeholders. Where the input doesn't provide enough to write a strong section, write the best version you can and flag what's thin.

Structure the output with every section the quality criteria require:
- Context
- Problem Statement
- Objectives
- Definitions
- Proposed Solution
- Scope (In Scope / Out of Scope)
- Product Experience (Happy Path / Sad Path)
- Acceptance Criteria
- Success Metrics (Outcomes / KPI Definitions / Product Health)
- Data Requirements
- Dependencies
- Open Questions
- Assumptions

### 5. Write Context, Problem Statement, and Objectives — in that order

These are three distinct sections with three distinct jobs. Get each one right before moving to requirements.

**Context** — why this work is happening now. The market or business condition making it urgent. Quantified data where available (adoption rates, failure rates, support burden). This is the stakeholder-facing justification layer. It should stand on its own without the problem statement.

**Problem Statement** — the user-centered pain. Name the specific user segment, describe the gap or frustration in concrete terms, quantify the impact where possible. No solution in this section. If the PM's input started with a solution ("we should build X"), translate it back: "users are experiencing Y, which causes Z."

**Objectives** — the directional business goals this product is expected to achieve. These are not metrics — they're intent. "Reduce support escalations," "achieve regulatory compliance," "align with competitor behavior." Objectives are what stakeholders read to understand why this matters; Success Metrics are how they'll evaluate whether it happened.

### 6. Write the Definitions section for any domain-specific terminology

If the product introduces or depends on terms with precise technical meanings, define them in a table before the requirements sections. This prevents silent misinterpretation by agents implementing from the document.

A term needs a definition if:
- It has a product-specific meaning that differs from everyday usage ("minimum payment" means something precise in lending)
- It's a system state or concept with a specific scope ("draw," "cycle," "installment")
- Two readers could reasonably interpret it differently

Format: a two-column table (Term | Definition). If no domain-specific terms exist, omit the section and note that in Assumptions.

### 7. Write acceptance criteria in Given/When/Then format

Every AC must meet the standards in `references/acceptance-criteria.md`:
- Given/When/Then structure
- Specific enough for an agent to implement without follow-up questions
- Boundary conditions declared
- Error states specified as separate AC
- Data tracking AC included (not deferred)

### 8. Build the Product Experience table before writing Acceptance Criteria

The Product Experience table is the primary behavioral specification. It exhaustively enumerates every meaningful state the user or system can be in, what happens in that state, and what edge cases or considerations apply. Acceptance Criteria are the verification layer on top — they confirm the behaviors the Product Experience table specifies.

Structure the section with two sub-tables:

**Happy Path** — the primary flow from the user's perspective, state by state. Each row is one state or action. Be specific: what the user sees, what the system does, what events fire.

**Sad Path** — failure modes, error states, system unavailability, invalid inputs, and edge cases. Each row is one failure scenario. Specify the expected behavior — not "system handles gracefully" but the actual user-facing and system-level response.

Table format for both:
| Action / State | Expected Experience | Considerations |
|---|---|---|

**Considerations** captures: differences between user types, timing dependencies, rollback behavior, data implications, comms triggers, or anything that would cause an engineer to pause and ask "wait, what happens if...?"

A complete Product Experience table means an engineer or coding agent can implement the feature without follow-up questions on behavior. A thin one means they'll fill in gaps with plausible-but-unintended choices.

**For complex products with multiple subsystems:** Consider adding a Functional Requirements section (FR-01, FR-02... grouped by subsystem, each with P0/P1/P2 priority) as a complement or alternative to ACs. FRs describe system capabilities; ACs describe verifiable behavioral scenarios. When a product has 5+ independent subsystems, FRs organize the requirements better than a flat AC list.

### 9. Flag assumptions explicitly

Anything the skill inferred rather than received as input goes in the Assumptions section. Be specific: "Assumed success metric target of 20% reduction based on comparable feature benchmarks" not "Made some assumptions about metrics."

The PM should be able to scan the Assumptions section and quickly confirm or correct each one.

### 10. Assign priorities and populate the Agent Block

Assign a priority to each Success Metric:
- **P0** — must-hit for launch; without it, the release decision is unclear
- **P1** — important but not launch-blocking; tracked and reviewed post-launch
- **P2** — nice-to-have or longer-horizon; tracked but not decision-driving

Group Acceptance Criteria by feature area or scenario group, labeling each group with its priority tier (the tier of the highest-priority AC in that group).

Populate the Agent Block:
- `prd_status`: always Draft unless the PM specifies otherwise
- `problem_severity`: High if the problem statement quantifies significant user impact or revenue risk; Medium if meaningful but bounded; Low if speculative or not yet quantified
- `p0_metric_count`: count of P0 rows in the Success Metrics Outcomes table
- `critical_dependency_count`: count of dependency rows with High risk

---

## Output Format

```markdown
# PRD: [Title]

**Author:** [PM name — leave as placeholder if unknown]
**Status:** Draft
**Date:** [Current date]

<!-- AGENT BLOCK -->
```yaml
agent_block:
  skill: prd-draft
  prd_status: [Draft / Review / Approved]
  problem_severity: [High / Medium / Low]
  p0_metric_count: [integer]
  critical_dependency_count: [integer — count of dependencies with High risk]
```
<!-- /AGENT BLOCK -->

---

## Context

[Why this work is happening now. The business or market condition making it urgent. Quantified data where available. Link to brief or prior work if available.]

---

## Problem Statement

[Specific user segment. Concrete pain or gap. Quantified impact where possible. No solution smuggled into the framing.]

---

## Objectives

- [Directional business goal — not a metric, an intent]
- [Directional business goal]

---

## Definitions

| Term | Definition |
|------|------------|
| [Term] | [Precise meaning in the context of this product] |

*(Omit this section if the product introduces no domain-specific terminology. Note the omission in Assumptions.)*

---

## Proposed Solution

[What to build. How it addresses the problem. Key features or capabilities.]

### User Flow

[Step-by-step flow from the user's perspective]

---

## Scope

### In Scope
- [Specific capability 1]
- [Specific capability 2]

### Out of Scope
- [Explicitly excluded item 1]
- [Explicitly excluded item 2]

---

## Product Experience

### Happy Path

| Action / State | Expected Experience | Considerations |
|---|---|---|
| [State or action] | [What the user sees / system does] | [Edge cases, user type differences, timing, comms triggers] |

### Sad Path

| Action / State | Expected Experience | Considerations |
|---|---|---|
| [Failure scenario] | [Expected behavior — specific, not "handles gracefully"] | [Recovery path, logging, fallback behavior] |

---

## Acceptance Criteria

**[Feature area or scenario group — P0]**
- **Given** [precondition], **When** [action], **Then** [expected result]
- **Given** [precondition], **When** [action], **Then** [expected result]

**[Feature area or scenario group — P1]**
- **Given** [precondition], **When** [action], **Then** [expected result]

---

## Success Metrics

### Outcomes

| Metric | Priority | Baseline | Target | Timeframe | Data Source |
|--------|----------|----------|--------|-----------|-------------|
| [Metric] | [P0 / P1 / P2] | [Current value] | [Target value] | [When] | [Where measured] |

### KPI Definitions

| Metric | How Calculated | Segmentation Needed |
|--------|----------------|---------------------|
| [Metric name] | [Numerator / Denominator or formula] | [Dimensions to slice by — time, user segment, etc.] |

### Product Health

| Signal | What It Measures | Threshold |
|--------|-----------------|-----------|
| [Error rate / latency / failure count] | [What goes wrong if this degrades] | [Value that warrants attention] |

---

## Data Requirements

### Events
| Event Name | Trigger | Payload Fields |
|------------|---------|----------------|
| [event_name] | [When it fires] | [field: type, field: type] |

### Dashboards / Monitoring
- [What needs to be visible and where]

---

## Dependencies

| Dependency | Owner | Status | Risk |
|------------|-------|--------|------|
| [What] | [Who] | [Current state] | [What happens if delayed] |

---

## Open Questions

| # | Question | Area | Owner |
|---|----------|------|-------|
| 1 | [Unresolved question — include why it matters] | [Domain area] | [Who resolves it] |

### Resolved Questions

| # | Question | Resolution |
|---|----------|------------|
| 1 | [What was asked] | [What was decided] |

*(Omit Resolved Questions if empty.)*

---

## Assumptions

- [Assumption 1 — what was inferred and why]
- [Assumption 2]

> **Context note:** [State which substantive company files were loaded, which files were absent, and which files existed but were stub templates and therefore skipped. Note what the draft might miss without that context.]
```

---

## Quality Bar

The draft should meet these tests:

- **Could you run doc-review on this and get a meaningful review?** The output should be substantive enough that doc-review has real content to evaluate — not so perfect that the review is trivial, not so thin that the review is just "everything is missing."
- **Does it satisfy all 9 quality criteria?** Every section should contain real content. Thin sections are acceptable if flagged; missing sections are not.
- **Is it a real first draft, not a template?** The output should contain specific content drawn from the input — not generic placeholder text like "[describe the problem here]."
- **Are assumptions flagged?** Everything the skill inferred should be visible and correctable.
- **Would the PM save time?** The draft should reduce the PM's work to editing and sharpening — not to writing the PRD from scratch after reading a template.
