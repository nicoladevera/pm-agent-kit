# Evaluation Rubric — sprint-plan

**Target input:** `evals/sprint-plan/sample-input-01.md`
**Skill under test:** `.claude/skills/sprint-plan/SKILL.md`
**Purpose:** Determine whether `sprint-plan` produces realistic goals, catches backlog issues, handles capacity honestly, and respects dependencies.

## Coverage

**This rubric tests:** Draft mode — produces a full sprint plan with goals, capacity math, and story selection.
**Not covered here:** Analyze mode (backlog health assessment only) — see `rubric-analyze.md`.

---

## Mode Detection

The input requests "plan the next sprint." This is **draft mode** — produce a sprint plan, not just a backlog health assessment.

**Pass:** Produces a sprint plan with goals, capacity, selected stories, and sequence. **Fail:** Produces only a backlog health report without a plan.

---

## Backlog Issues the Skill Must Catch

| # | Issue | Must Catch? | What good detection looks like |
|---|-------|-------------|-------------------------------|
| 1 | **PMT-302 is too large** — 12 AC for one story. Per `story-structure.md`, this should be split. The scheduling engine likely has natural break points (scheduling logic, retry logic, multi-channel routing). | Yes | Flags PMT-302 as a split candidate with suggested split approach. Does not include the unsplit story in the sprint plan. |
| 2 | **PMT-305, PMT-307, PMT-308 have no AC** — Three stories with no acceptance criteria. Not sprint-ready. | Yes | Flags all three as needing refinement. Defers them to the "Not Ready" section with specific action items. |
| 3 | **PMT-306 has partial AC** — Missing error handling AC. Per `acceptance-criteria.md`, error states should be separate AC, not implied. | Yes | Flags the AC gap specifically (missing error handling) and recommends what needs to be added before it's sprint-ready. |
| 4 | **PMT-502 is stale** — In the backlog for 4 sprints. The skill should flag this per `sprint-planning.md` staleness criteria and recommend: reprioritize, remove, or rewrite. | Yes | Names the staleness explicitly ("4 sprints in backlog") and recommends a disposition. |
| 5 | **Missing data stories** — The notification service has no analytics/instrumentation stories. PMT-207 (from Sprint 14 carryover) covers installment schedule analytics, but there's nothing for notification system events. | Should flag | Notes the gap. Recommends creating data stories for notification delivery tracking before the notification system ships. |

---

## Capacity Assessment

Realistic capacity math is a core test:

| Factor | Expected treatment |
|--------|-------------------|
| **Dev Patel** — 8 days, minus ~25% overhead = ~6 effective days | Should be treated as reduced capacity |
| **James Wu** — 6 days, first week on-call (~50%) = ~3-4 effective days | Should be treated as significantly reduced |
| **Ana Torres** — 3 days, design work only | Should be noted as limited; no heavy implementation work |
| **Sarah Chen** — 10 days but ~60% IC = ~6 effective days | Split between lead duties and coding |
| **Raj Sharma** — First sprint, needs onboarding/pairing | Should be treated as near-zero independent output for week 1, ramping in week 2. His capacity consumes some of Sarah's (pairing). |

**Total realistic capacity:** Roughly 20-24 effective person-days (not the nominal 37 days if everyone were full-time)

**Pass:** Capacity math accounts for PTO, on-call, split time, new engineer ramp-up, and overhead. Total is in the 20-25 range. **Fail:** Uses nominal days without adjustment, or treats Raj as full capacity.

---

## Sprint Goals

The plan should state 1-2 goals that are outcomes, not task lists:

| Check | Pass | Fail |
|-------|------|------|
| **Outcome-oriented** | "Complete installment schedule visibility for Mexico" and "Lay the foundation for the notification service" | "Complete PMT-206, PMT-204, PMT-207, PMT-301, PMT-303" |
| **Evaluable** | At sprint end, you can tell whether the goal was met | "Make progress on notifications" — can't evaluate |
| **Connected to Q2 priorities** | Goals trace back to Carlos's stated priorities | Goals don't reference the Q2 context |
| **Realistic** | Goals match the capacity math — don't overcommit | Goals assume all notification work completes in one sprint |

---

## Story Selection and Sequencing

Expected selection (approximately):

**Must include:**
- Sprint 14 carryover (PMT-206, PMT-204, PMT-207) — already in progress
- PMT-301 (notification schema) — foundation, must come first
- PMT-501 (bug fix) — quick, high-value

**Should include (capacity permitting):**
- PMT-303 or PMT-304 (push or in-app delivery) — depends on PMT-301, can start mid-sprint
- PMT-401 (loan restructuring scaffolding) — independent track, good for Raj's ramp-up

**Should NOT include:**
- PMT-302 (too large, needs splitting)
- PMT-305, PMT-307, PMT-308 (no AC)
- PMT-306 (partial AC, depends on PMT-302 which needs splitting)
- PMT-402 (depends on PMT-401)

**Pass:** Selects stories that match capacity, respect dependencies, and defer unready work with reasons. **Fail:** Stuffs everything in, ignores dependencies, or includes unready stories.

### Implementation Sequence

**Pass:** PMT-301 first (foundation), carryover in parallel, new work after PMT-301 ships. Raj starts with PMT-401 or PMT-501 (independent, good for onboarding). **Fail:** No sequence, or sequence that ignores dependencies.

---

## Carryover Assessment

The plan should assess why Sprint 14 items carried over:

| Story | Expected assessment |
|-------|-------------------|
| PMT-206 | Blocked — external dependency (localization team). Not a planning failure. Note: Kenya launch ends March 31, strings may arrive in Sprint 15 week 2. |
| PMT-204 | Started late — design handoff happened mid-sprint. Partially complete. |
| PMT-207 | Blocked — waiting on data team schema confirmation. Minor — expected to resolve Monday. |

**Pass:** Each carryover item has a reason and an impact assessment on Sprint 15 capacity. **Fail:** Carryover listed without explanation.

---

## Smell Detection

| Smell | Should detect? | What to look for |
|-------|---------------|-----------------|
| **Smell 1 (Missing the "Why")** | In its own output | Sprint goals should state why they matter, not just what they are |
| **Smell 2 (No Way to Measure)** | In its own output | Sprint goals should be evaluable at sprint end |
| **Overstuffed sprint** | In its own assessment | With ~22 effective person-days and significant carryover + ramp-up, the sprint can't absorb everything Carlos wants |

---

## Overall Assessment

**Would the team know exactly what they're committing to — and is it realistic?**

- Are sprint goals outcomes, not task lists?
- Is capacity honest (accounting for PTO, on-call, new engineer ramp-up)?
- Are unready stories deferred with clear reasons?
- Are dependencies respected in the sequence?
- Would a PM feel confident walking into sprint planning with this document?

**Pass threshold:** Catches PMT-302 sizing issue, flags all 3 no-AC stories, identifies PMT-502 staleness, produces realistic capacity math (~20-24 person-days), states outcome-oriented goals, and defers unready work with action items.

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| Mode detection | 5% | Draft mode identified; sprint plan produced (not just backlog assessment) |
| Backlog issues caught | 20% | PMT-302 flagged for splitting; PMT-305/307/308 deferred as no-AC; PMT-306 partial-AC gap named; PMT-502 staleness called out |
| Capacity assessment | 20% | PTO, on-call, new engineer ramp-up, and overhead accounted for; total in 20-24 range |
| Sprint goals quality | 15% | Outcome-oriented, evaluable at sprint end, connected to Q2 priorities, realistic against capacity |
| Story selection and sequencing | 15% | Correct stories in / deferred; dependencies respected; implementation sequence logical |
| Carryover assessment | 10% | Each carryover item has a reason and impact assessment on Sprint 15 capacity |
| Smell detection | 10% | Sprint goals state why they matter (not just what); goals are evaluable at sprint end; plan isn't overstuffed given realistic capacity |
| Output format compliance | 5% | Matches declared format; context note present |
