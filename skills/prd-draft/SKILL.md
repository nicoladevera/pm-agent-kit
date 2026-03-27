---
skill: prd-draft
type: Generator
tier: 1
approval: draft-confirm
context-required: []
context-optional:
  - company/facts/product.md
  - company/norms/process.md
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
- `references/prd-quality-criteria.md` — Generate toward all 8 criteria
- `references/acceptance-criteria.md` — AC must meet these standards (Given/When/Then, agent-implementable)
- `references/agent-readable-output.md` — Agent Block format and shared enum vocabulary

### 3. Load company context (if available)

If `company/facts/product.md` exists and is substantive, read it for product landscape, existing functionality, and user segments. This helps the PRD reference adjacent systems and avoid re-specifying what already exists.

If `company/norms/process.md` exists and is substantive, read it for how PRDs are expected to work at this company — what sections are standard, what level of detail engineering expects.

If either file exists but is still a stub template, treat it as unavailable and say so in the output.

If neither substantive file is available, proceed — note the absence in the output.

### 4. Generate the PRD

Produce a complete draft satisfying all 8 criteria from `references/prd-quality-criteria.md`. Every section should contain real content, not placeholders. Where the input doesn't provide enough to write a strong section, write the best version you can and flag what's thin.

Structure the output with every section the quality criteria require:
- Problem Statement
- Success Metrics
- Proposed Solution
- Scope (In Scope / Out of Scope)
- Edge Cases
- Acceptance Criteria
- Data Requirements
- Dependencies
- Open Questions
- Assumptions

### 5. Write the problem statement first and strongest

The problem statement is the foundation. Get it right before writing everything else. It should:
- Name the specific user segment affected
- Describe the pain or gap in concrete terms
- Quantify the impact where possible (even rough numbers)
- Stand on its own without referencing the proposed solution

If the PM's input started with a solution ("we should build X"), translate it back to the problem ("users are experiencing Y, which causes Z").

### 6. Write acceptance criteria in Given/When/Then format

Every AC must meet the standards in `references/acceptance-criteria.md`:
- Given/When/Then structure
- Specific enough for an agent to implement without follow-up questions
- Boundary conditions declared
- Error states specified as separate AC
- Data tracking AC included (not deferred)

### 7. Flag assumptions explicitly

Anything the skill inferred rather than received as input goes in the Assumptions section. Be specific: "Assumed success metric target of 20% reduction based on comparable feature benchmarks" not "Made some assumptions about metrics."

The PM should be able to scan the Assumptions section and quickly confirm or correct each one.

### 8. Assign priorities and populate the Agent Block

Assign a priority to each Success Metric:
- **P0** — must-hit for launch; without it, the release decision is unclear
- **P1** — important but not launch-blocking; tracked and reviewed post-launch
- **P2** — nice-to-have or longer-horizon; tracked but not decision-driving

Group Acceptance Criteria by feature area or scenario group, labeling each group with its priority tier (the tier of the highest-priority AC in that group).

Populate the Agent Block:
- `prd_status`: always Draft unless the PM specifies otherwise
- `problem_severity`: High if the problem statement quantifies significant user impact or revenue risk; Medium if meaningful but bounded; Low if speculative or not yet quantified
- `p0_metric_count`: count of P0 rows in the Success Metrics table
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

## Problem Statement

[Specific user segment. Concrete pain or gap. Quantified impact where possible. No solution smuggled into the framing.]

---

## Success Metrics

| Metric | Priority | Baseline | Target | Timeframe | Data Source |
|--------|----------|----------|--------|-----------|-------------|
| [Metric 1] | [P0 / P1 / P2] | [Current value] | [Target value] | [When] | [Where measured] |
| [Metric 2] | ... | ... | ... | ... | ... |

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

## Edge Cases

| Scenario | Expected Behavior |
|----------|-------------------|
| [Edge case 1] | [What the system does] |
| [Edge case 2] | [What the system does] |

---

## Acceptance Criteria

**[Feature area or scenario group — P0]**
- **Given** [precondition], **When** [action], **Then** [expected result]
- **Given** [precondition], **When** [action], **Then** [expected result]

**[Feature area or scenario group — P1]**
- **Given** [precondition], **When** [action], **Then** [expected result]

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

1. [Genuine unresolved question with context on why it matters]
2. [Question]

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
- **Does it satisfy all 8 quality criteria?** Every section should contain real content. Thin sections are acceptable if flagged; missing sections are not.
- **Is it a real first draft, not a template?** The output should contain specific content drawn from the input — not generic placeholder text like "[describe the problem here]."
- **Are assumptions flagged?** Everything the skill inferred should be visible and correctable.
- **Would the PM save time?** The draft should reduce the PM's work to editing and sharpening — not to writing the PRD from scratch after reading a template.
