---
skill: sprint-plan
type: Generator + Analyzer
tier: 2
approval: draft-confirm
context-required: []
context-optional:
  - company/norms/process.md
  - company/facts/team.md
  - company/facts/product.md
degradation: proceed-with-caveat
---

# sprint-plan

Draft sprint goals from priorities and capacity, and/or assess backlog health for sprint readiness. Planning is caring — the PM arrives at planning with thinking already done so the team's collaborative time produces decisions, not discovery.

---

## What It Accepts

Any form of planning input:
- A backlog (list of stories or tickets, possibly with priority and estimates)
- Team capacity information (who's available, PTO, on-call)
- Current sprint status (carryover items, in-progress work)
- Priorities from leadership, product goals, or OKRs
- A previous sprint plan for continuity
- A combination of the above

The input does not need to be complete. Missing capacity or priorities can be flagged rather than assumed.

---

## Modes

This skill operates in two modes. The PM selects the mode through how they invoke it.

### Analyze

Assess backlog health. Flag stories that aren't sprint-ready: missing AC, unclear scope, dependency risks, oversized stories, split/merge candidates, stale items. Produce a backlog health report the PM uses to prepare for planning.

**Triggered by:** "refine this backlog," "check backlog readiness," "what needs work before planning," "assess these stories," or any request focused on backlog quality rather than sprint composition.

### Draft

Analyze the backlog first (same process as Analyze mode), then produce a sprint plan with goals, selected stories, capacity allocation, and dependency notes. The analysis informs story selection; unready stories are deferred with reasons.

**Triggered by:** "plan the next sprint," "draft sprint goals," "what should we commit to," or any request that asks for a sprint plan or sprint goals.

**Default:** If the mode is ambiguous, ask: "Do you want a backlog health check, or a sprint plan for the next sprint?"

---

## Instructions

### Shared Steps (Both Modes)

#### 1. Read the input fully

Understand the full picture: what stories exist, what state they're in, what the priorities are, what capacity looks like, and what carried over from last sprint. Don't start assessing individual stories until you've absorbed the context.

#### 2. Load knowledge files

Read these files:
- `knowledge/sprint-planning.md` — Sprint goals, capacity, backlog health, carryover standards
- `knowledge/story-structure.md` — Story scoping, splitting, sizing standards
- `knowledge/acceptance-criteria.md` — AC standards for assessing story readiness
- `knowledge/pm-smell-test.md` — Check for smells 1 (missing the "why") and 2 (no way to measure success)

#### 3. Load company context (if available)

If `company/norms/process.md` exists, read it for sprint cadence, planning process, definition of done, and how the team works.

If `company/facts/team.md` exists, read it for team composition, velocity history, and who owns what.

If `company/facts/product.md` exists, read it for product context that informs priority decisions.

If these don't exist, proceed — note the absence in the output.

#### 4. Assess each story for readiness

For each story or ticket in the input, evaluate:

- **Acceptance criteria** — Are they written? Do they meet the standards in `acceptance-criteria.md`? (Given/When/Then, specific, testable, boundary conditions, error states)
- **Scope** — Is the boundary clear? Is there "and eventually" language that bleeds into future work?
- **Sizing** — Is it right-sized per `story-structure.md`? (One deployable unit, completable in one sprint, 8-10 AC max)
- **Dependencies** — Are cross-team or cross-story dependencies identified with owners?
- **Context** — Does the description provide enough for an implementer to start without reading the full PRD?

#### 5. Flag backlog issues

Identify:
- **Not ready** — Stories missing AC, unclear scope, unresolved dependencies
- **Split candidates** — Stories that are too large (8+ AC, multi-service, multi-flow)
- **Merge candidates** — Tiny stories that are always worked together
- **Stale items** — Stories in the backlog 3+ sprints untouched — are they still relevant?
- **Missing data stories** — Feature work without corresponding analytics/instrumentation stories

For each issue, state what's wrong and what the fix looks like.

#### 6. Assess carryover (if present)

If carryover items are in the input:
- Name each carryover story
- Assess why it carried over: scope underestimation, blocked, started late, scope crept, capacity gap
- Note the impact on the next sprint's capacity
- If the same type of carryover is recurring, call the pattern

#### 7. Surface dependency risks

Map dependencies across stories and across teams:
- What depends on what
- Who owns the blocking work
- Whether the dependency is tracking to timeline
- What happens to the sprint if the dependency slips

### Analyze Mode: Produce the Backlog Health Report

Output the assessment using the Analyze Mode format below.

### Additional Steps for Draft Mode

#### 8. Set sprint goals

State 1-3 sprint goals. Each goal:
- Is an outcome, not a story list: "Reduce first-payment miss rate to under 10%" not "Complete PMT-101 through PMT-108"
- Connects to a product or business objective
- Is evaluable at sprint end — you can tell whether it was achieved
- Has the "why" stated: why this goal matters for this sprint

If the input doesn't provide enough context for meaningful goals, state the best goals you can and flag what's assumed.

#### 9. Select stories for the sprint

Choose stories that serve the sprint goals, respecting capacity:

- **Capacity math** — Available person-days minus overhead (meetings, code review, support — typically 20-30%), minus carryover load, minus ramp-up for new areas. State the math.
- **Priority** — Stories that directly serve sprint goals first. Then dependencies that unblock future work. Then maintenance/tech debt if capacity allows.
- **Readiness** — Only select stories that passed the readiness assessment. Stories that need refinement go in the "Not Ready" section with action items.

#### 10. Suggest implementation sequence

Order stories within the sprint:
- Foundation stories first (other stories depend on them)
- Parallel tracks identified (stories that can be worked simultaneously)
- Data stories sequenced appropriately (can often parallel feature work)
- Dependencies respected (don't start what's blocked)

#### 11. Run the smell test on the plan

Check:
- **Smell 1 (Missing the "Why")** — Do sprint goals state why they matter?
- **Smell 2 (No Way to Measure Success)** — Can you tell at sprint end whether the goals were met?
- **Activity as goal** — Are the goals outcomes or task lists?
- **Overstuffed sprint** — Is the planned work realistic given capacity? Better to commit to less and finish it than to overcommit and carry over.

---

## Output Format

### Analyze Mode

```markdown
## Backlog Health Report

### Summary

[X stories assessed. Y ready for sprint, Z need work. Top issues.]

---

### Ready for Sprint

| Story | AC Quality | Scope | Dependencies | Notes |
|-------|------------|-------|--------------|-------|
| [Story title] | [Good / Needs work] | [Clear / Vague] | [None / Named] | [...] |

---

### Needs Refinement

1. **[Story]** — Issue: [Missing AC / Scope unclear / Too large / Dependency unresolved]. Fix: [What needs to happen before this is sprint-ready].
2. **[Story]** — ...

---

### Split Candidates

- **[Story]** — Why: [Too many AC / Multi-service / Multi-flow]. Suggested split: [How to break it up].

---

### Merge Candidates

- **[Story A] + [Story B]** — Why: [Always worked together / Same feature surface / Too small independently].

---

### Stale Items

- **[Story]** — In backlog since [date/sprint count]. Recommendation: [Reprioritize / Remove / Rewrite].

---

### Dependency Map

| Story | Depends On | Owner | Status | Risk |
|-------|-----------|-------|--------|------|
| [Story] | [What] | [Who] | [On track / At risk / Unknown] | [Timeline impact] |

---

### Missing Data Stories

- [Feature stories without corresponding analytics/instrumentation stories]

> **Context note:** [Whether company context was loaded. What the assessment might miss without it.]
```

### Draft Mode

```markdown
## Sprint Plan: [Sprint Name/Number]

### Sprint Goals

1. **[Goal]** — [Why this matters. What outcome we're targeting.]
2. **[Goal]** — [...]

---

### Capacity

| Team Member | Available Days | Notes |
|-------------|---------------|-------|
| [Name] | [X of Y] | [PTO / On-call / Full] |

**Total capacity:** [X person-days available] (after [Y]% overhead deduction)

---

### Selected Stories

| # | Story | Size | Goal | Assignee | Dependencies |
|---|-------|------|------|----------|--------------|
| 1 | [Title] | [Points/Size] | [Which goal] | [Who, if known] | [What, or "None"] |
| 2 | ... | ... | ... | ... | ... |

---

### Not Ready (Deferred)

- **[Story]** — Reason: [Needs refinement / Blocked / Missing AC]. Action: [What needs to happen and by when].

---

### Carryover

- **[Story]** — Carried over because: [Reason]. Sprint impact: [How much capacity it consumes].

---

### Implementation Sequence

1. **First:** [Foundation stories — others depend on these]
2. **Then (parallel):** [Stories that can be worked simultaneously]
3. **Alongside:** [Data stories]
4. **Last:** [Stories dependent on earlier work]

---

### Risks

- [Sprint-level risks: capacity tight, key dependency, scope uncertainty, new team member ramp-up]

---

### Sprint Health Indicators

- [How to know mid-sprint if we're on track. What to watch. When to be concerned.]

> **Context note:** [Whether company context was loaded. What the plan might miss without it.]
```

---

## Quality Bar

- **Do sprint goals state outcomes, not activity?** "Reduce miss rate" not "Complete stories." Goals are evaluable at sprint end.
- **Is capacity accounted for realistically?** Not 100% utilization. PTO, on-call, overhead, and carryover are factored in.
- **Are backlog issues specific and actionable?** Each issue names what's wrong and what the fix looks like. The PM can act on every flag without follow-up.
- **Would the team know exactly what they're committing to?** Scope is clear. Stories are ready. Dependencies are visible. Nothing is ambiguous.
- **Does the plan respect dependencies?** Foundation work is sequenced first. Blocked work isn't committed. Cross-team asks are flagged.
