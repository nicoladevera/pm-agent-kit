# Sprint Planning Standards

What makes a good sprint plan and a healthy backlog. Use this to evaluate sprint plans, assess backlog readiness, or generate sprint planning artifacts. The planning analog to `story-structure.md` — that file covers individual stories; this file covers the sprint-level container they live in.

Planning is caring. Showing up to sprint planning with a prepared backlog, assessed capacity, and drafted goals demonstrates respect for the team's time. The PM has already done the thinking; the team builds on it.

---

## Sprint Goals

### Goals Are Outcomes, Not Story Lists

A sprint goal answers "what will be true at the end of this sprint that isn't true now?" — not "which stories will we complete." "Increase feature activation rate for new users to 60% within the first 7 days" is a goal. "Complete stories PMT-101 through PMT-108" is a to-do list.

**What a good sprint goal looks like:**
- States the outcome the sprint is driving toward
- Is specific enough that you can tell at sprint end whether you achieved it
- Connects to a product or business objective the team understands
- 1-3 goals per sprint. More than 3 means the sprint has no focus.

**Red flag:** Sprint goals that are just the story titles rephrased. Goals that could apply to any sprint ("deliver quality work on time"). Goals that can't be evaluated at sprint end.

---

### Preparation as Respect

The PM arrives at planning with thinking already done. The backlog is refined. Dependencies are identified. Capacity is assessed. The team's collaborative time produces decisions, not discovery.

**Before planning, the PM should have:**
- A draft plan with proposed goals and stories
- Capacity assessed (who's available, who's not, realistic allocation)
- Backlog stories refined — AC written, scope clear, dependencies flagged
- Carryover from last sprint identified with reasons
- Open questions that need team input listed explicitly

**Red flag:** Planning meetings that start with "let's look at the backlog and see what we can fit." The PM opening Jira for the first time during the meeting. Stories being refined during planning instead of before it.

---

## Capacity

### Honest Capacity Planning

100% utilization is fiction. Capacity planning accounts for the real constraints: PTO, on-call rotations, carryover load, meetings and overhead, ramp-up time on new areas. The gap between planned capacity and actual capacity is where sprint commitments die.

**Capacity math should include:**
- Available person-days (total days minus PTO, holidays, on-call)
- Overhead deduction (meetings, code review, support rotation — typically 20-30% depending on team norms)
- Carryover load (stories in progress consume capacity even if they "started last sprint")
- Ramp-up cost for new team members or unfamiliar areas

**Red flag:** Sprint planned at full capacity with no buffer. Carryover treated as "free" because work already started. PTO discovered mid-sprint. On-call rotation not factored in.

---

## Backlog Health

### Readiness Indicators

Not every story in the backlog is ready for a sprint. Assess each story before selecting it:

| Signal | Ready | Not Ready |
|--------|-------|-----------|
| **Acceptance criteria** | Written, specific, testable (per `acceptance-criteria.md`) | Missing, vague, or untestable |
| **Scope** | Clear what's in and out | Ambiguous boundaries, "and eventually" language |
| **Dependencies** | Identified with owners and status | Unknown or unresolved cross-team dependencies |
| **Sizing** | Right-sized for one sprint (per `story-structure.md`) | Too large (8+ AC, multi-service), or too small (single AC with no context) |
| **Context** | Description provides enough for an implementer to start | Missing "why" or "where it fits" |

### Staleness

Stories that have been in the backlog for 3+ sprints untouched are stale. They represent one of three things:
1. **Not actually important** — remove them or deprioritize explicitly
2. **Blocked by something unnamed** — identify and surface the blocker
3. **Poorly defined** — needs refinement before it's pickable

Don't let stale stories accumulate. They create backlog noise and make planning harder.

### Split and Merge Signals

**Split when:**
- AC span different user flows or services
- Story touches both feature and data/analytics work
- More than 8-10 AC (usually multiple stories bundled)
- Natural phased rollout or multi-market considerations

**Merge when:**
- Two tiny stories are always worked together and can't be demonstrated independently
- Stories share the same AC surface area and were over-split

See `story-structure.md` for detailed splitting standards.

---

## Dependencies

### Surface Before Sprint Start

Cross-team dependencies should be visible before the sprint begins — not discovered when someone gets stuck mid-sprint. For each dependency:

- **What** depends on **what** — name both stories, both teams
- **Owner** — who is responsible for the blocking work
- **Status** — committed, in progress, at risk, or unknown
- **Timeline risk** — what happens to the sprint if this dependency slips

The PM who mobilizes 9 teams across 18 microservices does it by knowing every dependency before anyone asks. That's the standard.

**Red flag:** Dependencies discovered during standup. Cross-team asks made for the first time mid-sprint. "I didn't know they needed that from us."

---

## Data in Sprint Planning

### Data Requirements Are Sprint Requirements

Instrumentation, events, dashboards, and schema changes are planned during the sprint, not deferred to "after launch." Data stories are separated from feature stories and sequenced appropriately (per `story-structure.md`).

**During planning, check:**
- Do feature stories have corresponding data stories?
- Are event schemas defined (event names, payloads, field types)?
- Is dashboard work scoped (what questions the dashboard answers)?
- Is the data team aware and capacity-allocated?

**Red flag:** "We'll figure out tracking later." Feature stories with "track this event" as a final AC. Data work treated as optional stretch goal.

---

## Carryover

### Carryover Is a Signal

Every carryover story deserves a brief assessment: why did it carry over? The answer matters because it tells you whether to adjust the next sprint:

| Reason | What it means | What to do |
|--------|--------------|------------|
| **Scope underestimated** | Story was bigger than expected | Re-estimate, possibly split |
| **Blocked** | External dependency, environment issue, review bottleneck | Resolve the blocker before re-committing |
| **Started late** | Other work took priority mid-sprint | Examine sprint discipline |
| **Scope crept** | Requirements expanded during the sprint | Tighten scope controls |
| **Capacity gap** | Team smaller than planned (PTO, on-call, unplanned work) | Adjust capacity model |

Recurring carryover — the same type of overrun sprint after sprint — means the planning model is broken, not that the team is slow. Name the pattern. "This is the third sprint in a row with carryover from scope underestimation. We need to change how we estimate."

**Red flag:** Carryover reported without explanation. The same stories carrying over multiple sprints. Carryover treated as normal rather than investigated.

---

## Sprint Health During Execution

### Leading Indicators

Don't wait until sprint end to assess whether the sprint is on track. Watch these during the sprint:

- **Burndown trajectory** — is the rate of completion consistent with the sprint timeline?
- **Stories in progress vs. completed** — too many in progress with few completed late in the sprint signals risk
- **Blocked items** — anything blocked for more than a day needs escalation
- **Scope changes** — stories added or expanded mid-sprint erode the commitment
- **Dependency status** — are external dependencies tracking to their timelines?

---

## Using These Standards

**For sprint planning (`sprint-plan` skill):** Generate sprint plans that satisfy these standards. Goals are outcomes. Capacity is honest. Stories are assessed for readiness. Dependencies are surfaced. Carryover is explained.

**For backlog refinement (`sprint-plan` analyze mode):** Assess the backlog against the readiness indicators. Flag stories that aren't ready. Recommend splits, merges, and removals. Surface stale items.

**For status assessment (`status-update` skill):** Use the sprint health indicators to assess delivery state mid-sprint. Compare actual progress against the sprint plan.
