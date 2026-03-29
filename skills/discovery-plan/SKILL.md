---
skill: discovery-plan
type: Generator
tier: 4
approval: draft-confirm
context-required: []
context-optional:
  - company/facts/product.md
  - company/facts/customers.md
  - company/interfaces/data-sources.md
degradation: proceed-with-caveat
---

# discovery-plan

Plan what to learn before committing to a solution: map assumptions, rank them by the cost of being wrong, select research methods, define evidence thresholds, and sequence the work. The discovery plan sits upstream of everything — it earns the PRD by validating the problem, grounds the business case with real evidence, and gives the roadmap prioritization something better than opinions to sequence against.

Discovery planning is not research execution. This skill produces the plan — what assumptions to test, how to test them, what "good enough" evidence looks like, and in what order. The PM executes the research (or delegates it), then feeds the results into downstream skills.

---

## What It Accepts

Any form of problem area or initiative context:
- A problem statement or hypothesis about user behavior (structured or rough)
- A proposed initiative that hasn't been validated yet
- A business case or PRD draft where the evidence is thin and the PM knows it
- Rough notes, Slack threads, or verbal downloads about an area the team wants to explore
- A list of open questions the PM wants to answer before committing
- Existing artifacts from `knowledge/` — user feedback syntheses, data analyses, competitive snapshots — that surface gaps in understanding
- A combination of the above

The input does not need to be structured. This skill identifies what's assumed, what's known, and what's missing — then builds a plan to close the gaps that matter most.

---

## Intake

A discovery plan built on the wrong framing wastes research cycles — the team validates something that didn't need validating while the real risk goes unexamined. Confirm the problem space and the decision the discovery serves before planning.

### Signals to Check

- **Problem area or initiative:** Is there a clear problem space, or is the input a vague "we should look into X"?
- **What's already known:** Does the PM mention existing data, prior research, user feedback, or competitive signals? Or is this greenfield?
- **Decision to inform:** What decision will this discovery feed? A PRD? A business case? A prioritization call? If there's no named decision, the research risks producing interesting findings that change nothing.
- **Timeline constraints:** Is there a deadline driving this? A planning cycle? A window of opportunity?
- **Available research resources:** Does the PM have access to users, data infrastructure, research tools, or budget? Constraints narrow the method menu.

### Adaptive Response

**Rich input** (problem area clear, some evidence cited, decision named): Restate the problem space and the decision the discovery serves. Confirm one inference — the most consequential one (e.g., which assumption type seems riskiest). Example: "The question is whether enterprise users are churning because of onboarding complexity or something else entirely, and this feeds the decision on whether to invest in an onboarding redesign. I'll focus the plan on validating the problem before testing solutions. Proceeding."

**Moderate input** (problem area present but decision or evidence unclear): Ask up to 3 targeted questions. Examples:
- "What decision does this discovery need to inform — are you deciding whether to invest in this area, or have you already committed and need to know how to build it?"
- "What evidence already exists — any user feedback, support data, analytics, or prior research I should account for?"
- "Are there timeline or resource constraints — a planning deadline, available research participants, or budget limits?"

**Thin input** (a topic, a vague area, or "we should do discovery on X"): Present a structured interpretation:

> **Here's how I'd frame this — tell me what needs adjusting:**
>
> - **Problem space:** [Translated from the input — what the team is trying to understand]
> - **Decision this feeds:** [Best inference — what decision the discovery results would inform]
> - **What seems known vs. assumed:** [Separating existing evidence from beliefs]
> - **Research constraints:** [Any inferred limitations — timeline, access, resources]
>
> Anything off? I'll adjust before building the plan.

---

## Instructions

### 1. Read the input fully

Absorb all context before structuring. Understand what problem space the PM wants to explore, what's already known, what's assumed, and what decision the discovery needs to inform. Note what evidence exists and what's missing.

### 2. Load reference files

Read these files:
- `references/discovery-methods.md` — Assumption taxonomy, risk ranking framework, method menu, evidence thresholds, research operations standards, bias awareness
- `references/pm-smell-test.md` — Check for smells 1 (missing why), 2 (no way to measure success), and 7 (solution without a problem)
- `references/agent-readable-output.md` — Agent Block format and shared enum vocabulary

### 3. Load company context (if available)

If `company/facts/product.md` exists and is substantive, read it for product landscape, key metrics, and current focus areas. This grounds assumption mapping in the actual product context rather than generic inference.

If `company/facts/customers.md` exists and is substantive, read it for customer segments, ICP definitions, and known pain points. This enables sharper segment-specific research design and prevents studying the wrong users.

If `company/interfaces/data-sources.md` exists and is substantive, read it for available analytics tools, feedback channels, and data infrastructure. This directly constrains which methods are feasible — you can't recommend data mining if there's no data warehouse.

If any of these files exist but are still stub templates, treat them as unavailable and say so in the context note.

### 4. Extract the problem space

Establish what the team is trying to understand and why it matters now. Per the Problem-First operating heuristic from `CLAUDE.md`:

- If the PM's input leads with a solution ("we should build X and need to validate it"), reframe around the problem the solution is meant to address. Discovery that starts with "validate our solution" is confirmation bias by design.
- Name the decision this discovery serves. If the PM hasn't named one, infer it and flag for confirmation. Discovery without a named decision produces shelf-ware.
- Note what existing evidence is available — prior user feedback syntheses, data analyses, competitive signals, support data. These narrow what still needs to be learned.

### 5. Map assumptions

List every assumption embedded in the current understanding of the problem space. Use the assumption taxonomy from `references/discovery-methods.md`:

- **User assumptions** — who the user is, what they need, how they behave
- **Problem assumptions** — whether the problem exists, its severity, its scope
- **Solution assumptions** — whether a proposed approach would work (only if a solution is already being considered)
- **Viability assumptions** — business model, unit economics, regulatory, operational capacity

For each assumption:
- State it as a testable claim, not a vague area ("Enterprise users find onboarding complex" not "Onboarding might be a problem")
- Note the current evidence level: validated (direct evidence), inferred (adjacent data), or assumed (no evidence)
- Surface hidden assumptions — assumptions embedded in the framing itself

An assumption map with fewer than 5 entries for a non-trivial initiative signals incomplete extraction. Push harder.

### 6. Risk-rank assumptions

Apply the cost-of-being-wrong framework from `references/discovery-methods.md`:

For each assumption, assess:
- **Consequence** — if wrong, does the initiative fail, underperform, or just need adjustment?
- **Reversibility** — if we proceed on this assumption and it's wrong, can we course-correct cheaply?
- **Dependency** — do other assumptions depend on this one?
- **Current confidence** — strong signal, weak signal, or none?

Use the prioritization matrix: high-consequence / low-confidence assumptions are the plan's priority. Explicitly deprioritize low-consequence assumptions and note why.

The ranking is the most important judgment in the entire skill. A plan that tests easy, comfortable assumptions while ignoring hard, consequential ones has failed at its primary job.

### 7. Select methods

For each high-priority assumption, recommend a research method from the menu in `references/discovery-methods.md`. For each selection:

- Name the method and why it fits this assumption type
- Name what alternative methods were considered and why they're less appropriate
- Note constraints that influenced the choice (no existing data rules out data mining; no production traffic rules out A/B tests)
- Follow the method selection logic: qualitative before quantitative, match evidence strength to stakes, check constraints

Do not default to interviews for every assumption. Different assumption types need different methods. If the plan uses only one method, justify why.

### 8. Define evidence criteria

For each research activity, define what "validated" and "invalidated" look like before the research starts. Per `references/discovery-methods.md` evidence thresholds:

- **Success criteria:** What result would make you proceed with confidence? Be specific — "users describe the same pain point" is vague; "5+ of 8 interviewees independently describe workflow friction in the first-14-day period" is testable.
- **Failure criteria:** What result would make you stop or pivot? This is equally important and frequently omitted.
- **Ambiguous result plan:** What happens if the results are mixed? More research? Proceed with caveats? Escalate the decision?

Evidence criteria must be defined before the research runs, not after. Post-hoc criteria are confirmation bias with extra steps.

### 9. Sequence the plan

Order research activities by:

1. **Dependency** — test assumptions that gate other assumptions first. If the problem doesn't exist, solution testing is moot.
2. **Information value** — front-load research that could change everything. If the first study invalidates the core problem assumption, the rest of the plan may not be needed.
3. **Efficiency** — group activities that share participants, infrastructure, or timing. An interview that covers both user and problem assumptions is better than two separate studies.

Show the sequence visually — an ordered list with dependencies noted. Name decision points: "If [assumption] is invalidated at this stage, stop and reassess before proceeding."

### 10. Estimate scope

For each research activity:
- Participant count (with rationale from `references/discovery-methods.md` research operations standards)
- Timeline (recruiting + execution + analysis)
- Resource requirements (tools, budget, recruiting channels, internal stakeholder time)
- Total plan duration (accounting for sequential dependencies and parallel activities)

Be honest about what the plan requires. A plan that needs 30 interview participants, 3 weeks, and a dedicated researcher is not the same commitment as one that needs 5 data queries and a week.

### 11. Run the smell test

Check for:
- **Smell 1 (Missing Why):** Does the plan establish why this discovery matters? Is the decision it informs clearly named?
- **Smell 2 (No Way to Measure Success):** Does every research activity have success/failure criteria? Will you know when you're done?
- **Smell 7 (Solution Without a Problem):** Is the plan validating a problem, or is it designed to confirm a predetermined solution?

### 12. Populate the Agent Block

After completing the smell test, fill in the Agent Block:
- `assumption_count`: total assumptions mapped
- `high_priority_count`: assumptions ranked as high-priority for testing
- `methods_used`: list of distinct research methods recommended
- `estimated_duration`: total plan duration in weeks
- `decision_informed`: the decision this discovery plan feeds
- `highest_risk_assumption`: the single assumption with the highest cost-of-being-wrong

### 13. Flag open items

List everything the PM needs to resolve before executing the plan:
- Recruiting channels or participant access not yet confirmed
- Data sources that need to be verified as available and reliable
- Budget or resource approvals needed
- Stakeholder alignment on research goals
- Timeline dependencies on external events (planning cycles, launches, deadlines)
- Assumptions the plan doesn't cover and why (too low-priority, or requires a method the team can't access)

Open items are a feature of the plan, not a failure. A discovery plan that claims to need nothing resolved is either trivial or dishonest.

---

## Output Format

````markdown
## Discovery Plan: [Problem Area or Initiative Name]

**Status:** Draft
**Date:** [Current date]
**Decision informed:** [The specific decision this discovery feeds — e.g., "Whether to invest in onboarding redesign for enterprise users"]

<!-- AGENT BLOCK -->
```yaml
agent_block:
  skill: discovery-plan
  assumption_count: [integer]
  high_priority_count: [integer]
  methods_used: ["method1", "method2"]
  estimated_duration: "[N weeks]"
  decision_informed: "[One sentence — what decision this feeds]"
  highest_risk_assumption: "[One sentence — the assumption with the highest cost-of-being-wrong]"
```
<!-- /AGENT BLOCK -->

---

### Problem Space

[What the team is trying to understand. Why it matters now. What decision this discovery serves. What's already known vs. what's assumed. Framed around the problem, not a proposed solution.]

---

### Assumptions Map

| # | Assumption | Type | Current evidence | Confidence | Cost if wrong | Priority |
|---|-----------|------|-----------------|------------|---------------|----------|
| 1 | [Testable claim] | [User / Problem / Solution / Viability] | [Validated / Inferred / Assumed — with basis] | [High / Medium / Low] | [High / Medium / Low — what happens] | [Test / Verify / Monitor / Skip] |
| 2 | ... | ... | ... | ... | ... | ... |

**Hidden assumptions surfaced:** [Any assumptions embedded in the framing itself that the PM may not have recognized]

---

### Research Plan

#### Study 1: [Name — tied to the assumption(s) it tests]

**Assumption(s) tested:** #[N], #[N]
**Method:** [Method name] — [Why this method over alternatives]
**Participants:** [Count, segment, recruiting approach]
**Evidence criteria:**
- **Validated if:** [Specific, pre-defined success criteria]
- **Invalidated if:** [Specific, pre-defined failure criteria]
- **Ambiguous if:** [What happens with mixed results]

**Timeline:** [Duration — recruiting + execution + analysis]
**Resources needed:** [Tools, budget, stakeholder time]

#### Study 2: [Name]

[Same structure]

[Repeat for each research activity]

---

### Sequence

[Ordered list or visual showing the research sequence with dependencies and decision points]

1. **[Study name]** — [Duration]. Tests [assumption #s]. *Decision point: if [assumption] is invalidated, reassess [what].*
2. **[Study name]** — [Duration]. Depends on results from Study 1. Tests [assumption #s].
3. ...

**Total estimated duration:** [N weeks]
**Parallel activities:** [Any studies that can run simultaneously]

---

### Resource Requirements

| Resource | Need | Status |
|----------|------|--------|
| [Participant access] | [Details] | [Confirmed / Needed] |
| [Data infrastructure] | [Details] | [Confirmed / Needed] |
| [Research tools] | [Details] | [Confirmed / Needed] |
| [Budget] | [Details] | [Confirmed / Needed] |
| [Stakeholder time] | [Details] | [Confirmed / Needed] |

---

### Open Items

- [Recruiting channels or access not yet confirmed]
- [Data sources that need verification]
- [Budget or approval dependencies]
- [Timeline dependencies on external events]
- [Assumptions not covered by this plan and why]

---

### Smell Test

- **Smell 1 (Missing Why):** [Finding — or "Clear — decision informed is named and the discovery purpose is established"]
- **Smell 2 (No Way to Measure Success):** [Finding — or "Clear — all research activities have pre-defined success/failure criteria"]
- **Smell 7 (Solution Without a Problem):** [Finding — or "Clear — plan validates the problem before testing solutions"]

> **Context note:** [State which substantive company files were loaded, which were absent, and which were stub templates. Note how missing context may have affected the quality of assumption mapping, method selection, or participant targeting.]
````

---

## Quality Bar

- **Does the plan validate the problem before testing solutions?** Problem assumptions are tested before solution assumptions. The sequence reflects this — if the problem doesn't exist, solution testing doesn't happen.
- **Are assumptions stated as testable claims?** Each assumption is specific enough that research could confirm or refute it. "Onboarding might be a problem" is not testable. "Enterprise users with 10+ seats experience onboarding friction in the first 14 days" is.
- **Does the risk ranking reflect consequence, not comfort?** The highest-priority assumptions are the ones with the highest cost of being wrong — not the ones that are easiest or most interesting to test.
- **Are methods matched to assumption types?** Different assumptions call for different methods. The plan doesn't default to interviews for everything or surveys for everything. Each method selection has a rationale.
- **Are evidence criteria pre-defined?** Success, failure, and ambiguous result plans are stated before research begins. The team will know when they're done and what the results mean.
- **Is the plan connected to a decision?** The discovery serves a named decision. The output feeds a specific downstream artifact (PRD, business case, prioritization rationale). Research without a decision context is shelf-ware.
- **Is the scope realistic?** Participant counts, timelines, and resource needs are honest. A plan that requires resources the team doesn't have is aspirational, not actionable.
- **Does the sequence reflect dependencies?** Gating assumptions are tested first. Decision points are named. The plan doesn't treat all research as parallelizable when results from one study should inform the next.

---

## Save

After producing the artifact, write it to `knowledge/discovery-plans/` using the naming convention: `YYYY-MM-DD-feature-or-area-discovery-plan.md`, where the date is the plan creation date and the slug describes the problem area or initiative. Report the saved file path in the conversation.
