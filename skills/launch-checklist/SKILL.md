---
skill: launch-checklist
type: Generator
tier: 3
approval: draft-confirm
context-required: []
context-optional:
  - company/norms/launch-process.md
  - company/norms/communication.md
  - company/facts/product.md
  - company/facts/customers.md
  - company/facts/team.md
degradation: proceed-with-caveat
---

# launch-checklist

Generate a launch checklist for a feature, calibrated to the launch type and covering every dimension that applies. The checklist is the coordination artifact — it turns "are we ready to ship?" from a feeling into a verifiable state.

---

## What It Accepts

Any form of launch context:
- A feature description or PRD (structured or rough)
- A Slack thread about an upcoming launch
- A bullet list of what's shipping and when
- A reference to an existing PRD in `knowledge/prds/`
- A combination of the above

The input does not need to be complete. This skill identifies what's present and flags what's missing.

---

## Intake

Launch type is already required. Intake adds risk appetite — how cautious vs. aggressive the rollout should be — because it changes checklist depth, rollback trigger sensitivity, and monitoring intensity.

### Signals to Check

- **Launch type:** Stated? (Already required — if missing, the existing ask in step 4 handles this.)
- **Risk appetite / rollback tolerance:** Does the input signal how conservative the launch should be? Look for: phased rollout mentions, feature flag strategy, "we need to be careful" vs. "ship it fast," prior incident context.
- **Rollback mechanism:** Is there a stated rollback path (feature flag, deployment rollback, etc.)?

### Adaptive Response

**Rich input** (launch type stated, risk appetite clear, rollback mechanism mentioned): Confirm and proceed. Example: "GA launch, conservative rollout (phased behind feature flag), rollback via flag. Generating the checklist."

**Moderate input** (launch type stated, but risk appetite or rollback unclear): Ask 1-2 targeted questions. Examples:
- "How conservative should this rollout be — phased percentage ramp, or full deploy with a kill switch, or big-bang?"
- "If something goes wrong, what's the rollback mechanism — feature flag, deployment rollback, or something else?"

**Thin input** (feature description with no launch context): The existing launch-type ask fires first. Once type is established, if risk appetite is still unclear:

> **A few assumptions I'll bake into the checklist — flag anything that's off:**
>
> - **Risk appetite:** [Conservative / Moderate / Aggressive — inferred from launch type and context]
> - **Rollback approach:** [Feature flag / Deployment rollback / Manual — inferred]
> - **Monitoring intensity:** [Standard for this launch type / Elevated because of X]
>
> These affect how tight the rollback triggers are and how heavy the monitoring section is. Adjust?

Note: The existing launch-type ask in step 4 of Instructions remains unchanged. Intake handles what it doesn't cover.

---

## Instructions

### 1. Read the input fully

Understand what's launching, who it affects, what systems are involved, and what the timeline looks like. Note what the input provides and what it leaves out — the gaps are as important as the content.

### 2. Load reference files

Read these files:
- `references/launch-readiness.md` — Launch readiness dimensions and standards by launch type
- `references/pm-smell-test.md` — Check for smells 2 (no way to measure success), 3 (missing owners), and 11 (no data plan)
- `references/agent-readable-output.md` — Agent Block format and shared enum vocabulary

### 3. Load company context (if available)

If `company/norms/launch-process.md` exists and is substantive, read it for how this company categorizes launches, who approves what, and what's expected per launch type.

If `company/norms/communication.md` exists and is substantive, read it for communication channel conventions and stakeholder preferences.

If `company/facts/product.md` exists and is substantive, read it for product landscape context — adjacent features, what already exists.

If `company/facts/customers.md` exists and is substantive, read it for customer segments and pain points — helps identify which segments are affected by the launch and what their specific readiness needs might be.

If `company/facts/team.md` exists and is substantive, read it for team structure, stakeholders who need to be informed, and support/on-call structure.

If any of these files exist but are still stub templates, treat them as unavailable and say so in the context note.

### 4. Determine launch type

Identify the launch type from the input: **Internal**, **Alpha**, **Beta**, or **GA**.

Look for explicit statements ("this is a beta launch"), audience descriptions ("rolling out to all users" = GA, "internal testing only" = Internal), or rollout mechanisms ("behind a feature flag for 10% of users" = Beta).

If the launch type is ambiguous from the input, ask: "What launch type is this — Internal, Alpha, Beta, or GA?"

The launch type determines checklist depth. Internal is the lightest. GA is the most thorough. See `references/launch-readiness.md` for what each type requires.

### 5. Generate checklist across all dimensions

For each dimension in `references/launch-readiness.md`, generate checklist items appropriate to the launch type:

- **Documentation** — What needs to be written or updated
- **Internal Communication** — Who inside the company needs to know
- **External Communication** — How users learn about the launch
- **Support Enablement** — How support is prepared
- **Monitoring and Alerting** — What you're watching
- **Data and Analytics** — How you'll measure success
- **Rollback Plan** — How you undo it if needed
- **Dependencies** — What must be in place first
- **Legal and Compliance** — Regulatory or policy requirements (mark N/A when not applicable)

For each checklist item, include:
- **Description:** What needs to happen
- **Owner:** Who is responsible (name a role or person if inferable from the input or company context; mark TBD if not)
- **Due:** When it needs to be done relative to launch date (e.g., "L-5 days", "Launch day", "L+1 week")

Do not pad the checklist with items that don't apply to this launch type. An internal launch with 40 items is over-scoped. A GA launch with 8 items is under-scoped. Match depth to type.

### 6. Generate rollback plan

Create a dedicated rollback section with:
- **Mechanism:** How the launch is reversed (feature flag, deployment rollback, etc.)
- **Trigger criteria:** Quantitative thresholds that warrant rollback (error rate, latency, conversion drop). These must be numbers, not vibes.
- **Steps:** Ordered steps to execute the rollback
- **Authorization:** Who decides to roll back
- **Communication:** Who gets told if rollback happens, and how

If the input doesn't provide enough information to specify trigger criteria, flag this as an open item the PM must resolve.

### 7. Generate success criteria

Define how the team will know the launch worked:
- **1-day check:** What to look for immediately (errors, basic adoption, system health)
- **1-week check:** Early signal (adoption trend, user feedback, support ticket volume)
- **1-month check:** Outcome metrics (success metrics from the PRD, retention, satisfaction)

Each criterion needs: a metric, a target, a timeframe, and a data source. If targets can't be set from the input, flag them as needing PM input.

### 8. Run the smell test

Check for:
- **Smell 2 (No Way to Measure Success)** — Are success criteria defined with targets? Or is success assumed?
- **Smell 3 (Missing Owners)** — Does every checklist item and every rollback step have a named owner? "TBD" is acceptable as a flag; absence is not.
- **Smell 11 (No Data Plan)** — Is instrumentation on the checklist? Are events and metrics specified? Or is data deferred to "after launch"?

### 9. Flag open items

List anything the PM needs to resolve before the launch is ready. These are gaps the checklist surfaced — missing information, unresolved decisions, items that need owner assignment. Open items are a feature of the checklist, not a failure of it.

---

## Output Format

````markdown
## Launch Checklist: [Feature Name]

**Launch type:** [Internal / Alpha / Beta / GA]
**Target date:** [Date, if provided — "TBD" if not]
**Launch owner:** [PM or whoever owns the launch — "TBD" if not specified]

<!-- AGENT BLOCK -->
```yaml
agent_block:
  skill: launch-checklist
  launch_type: [Internal / Alpha / Beta / GA]
  overall_readiness: [Ready / At Risk / Not Ready]
  unowned_item_count: [integer — checklist items with no assigned owner]
  success_criteria_defined: [Yes / No]
  rollback_plan_defined: [Yes / No]
```
<!-- /AGENT BLOCK -->

---

**Launch timeline** *(always include; adjust day markers to match actual schedule)*

```
L-5    L-3    L-1    L     L+1    L+3
 |      |      |     |      |      |
[Flags] [Docs] [RC] [Go]  [Mon] [Review]
         |
      [Rollback
        tested]
```

---

### Pre-Launch

#### Documentation
- [ ] [Item] — Owner: [Who]. Due: [When].
- [ ] ...

#### Internal Communication
- [ ] [Item] — Owner: [Who]. Due: [When].
- [ ] ...

#### External Communication
- [ ] [Item] — Owner: [Who]. Due: [When].
- [ ] ...
<!-- Omit this section entirely for Internal launches. -->

#### Support Enablement
- [ ] [Item] — Owner: [Who]. Due: [When].
- [ ] ...
<!-- Omit this section for Internal launches. Light for Alpha. -->

#### Monitoring and Alerting
- [ ] [Item] — Owner: [Who]. Due: [When].
- [ ] ...

#### Data and Analytics
- [ ] [Item] — Owner: [Who]. Due: [When].
- [ ] ...

#### Dependencies
- [ ] [Item] — Owner: [Who]. Due: [When]. Status: [Confirmed / In Progress / TBD].
- [ ] ...

#### Legal and Compliance
- [ ] [Item] — Owner: [Who]. Due: [When].
<!-- Mark "N/A for this launch" if not applicable. Do not silently omit. -->

---

### Rollback Plan

**Mechanism:** [How the launch is reversed]

**Trigger criteria:**
- [Metric] > [Threshold] (e.g., error rate > 2%, p95 latency > 500ms, conversion drop > 10%)

**Steps:**
1. [Step]
2. [Step]

**Authorization:** [Who decides to roll back]
**Communication on rollback:** [Who gets told, how]
**Data implications:** [What happens to data created during the launch window]

**Rollback decision tree** *(always include)*

```
[Metric exceeds threshold]
         |
  [Notify on-call lead]
         |
   ┌─────┴──────┐
[Auto-rollback] [Manual review]
  (flag set)    (ambiguous case)
```

---

### Success Criteria

| Timeframe | Metric | Target | Data Source |
|-----------|--------|--------|-------------|
| Day 1 | [Metric] | [Target] | [Source] |
| Week 1 | [Metric] | [Target] | [Source] |
| Month 1 | [Metric] | [Target] | [Source] |

---

### Post-Launch Review

- [ ] Schedule post-launch review for [date relative to launch]
- [ ] Prepare data summary comparing actuals to success criteria
- [ ] Document learnings and follow-up work

---

### Open Items

- [Gap or unresolved decision that the PM needs to address before launch]
- [Missing owner that needs assignment]
- [Information needed to set rollback thresholds or success targets]

---

### Smell Test

- **Smell 2 (No Way to Measure Success):** [Finding or "Clear — success criteria defined with targets"]
- **Smell 3 (Missing Owners):** [Finding or "Clear — all items have owners"]
- **Smell 11 (No Data Plan):** [Finding or "Clear — instrumentation and metrics on the checklist"]

> **Context note:** [State the identified launch type and how it was determined. State which substantive company files were loaded, which were absent, and which were stub templates. Note what the checklist might miss without company-specific launch process context.]
````

---

## Quality Bar

- **Does the checklist cover all applicable dimensions for the launch type?** Nothing forgotten. Every dimension from the reference is addressed or explicitly marked N/A.
- **Is checklist depth calibrated to the launch type?** An internal launch isn't burdened with GA-level items. A GA launch isn't missing critical external communication or support enablement.
- **Does every item have an owner?** No orphaned items. "TBD" is acceptable as a flag — but it shows up in the Open Items section, not silently.
- **Is the rollback plan specific?** Quantitative trigger criteria, not "if things go badly." Named authorization. Ordered steps. Communication plan.
- **Are success criteria measurable?** Metrics with targets and timeframes, not "track adoption." Data sources named.
- **Is monitoring on the checklist, not deferred?** Day-one monitoring is a launch prerequisite, not a follow-up task.
- **Would the PM feel confident nothing falls through the cracks?** The checklist is the coordination artifact. If the PM can hand it to the team and everyone knows what they own and when it's due, it's working.

---

## Save

After producing the artifact, write it to `knowledge/launch-checklists/` using the naming convention: `feature-name-launch-checklist.md`, where `feature-name` is a lowercase hyphenated slug derived from the feature name. Report the saved file path in the conversation.
