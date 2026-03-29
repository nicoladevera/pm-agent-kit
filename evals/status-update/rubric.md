# Evaluation Rubric — status-update

**Target input:** `evals/status-update/sample-input-01.md`
**Skill under test:** `skills/status-update/SKILL.md`
**Purpose:** Determine whether `status-update` catches risks the data implies but doesn't state, calibrates correctly for a VP audience, and leads with assessment over activity.

## Coverage

**This rubric tests:** Draft mode — produces a VP-calibrated status communication.
**Not covered here:** Analyze mode (internal delivery state assessment, no audience) — see `rubric-analyze.md`.

---

## Mode Detection

The input requests "write me the weekly update for Carlos (VP Engineering)." This is **draft mode** with Carlos as the stated audience.

**Pass:** Produces a VP-calibrated status communication. **Fail:** Produces an internal assessment (analyze mode) or a team-level update.

---

## Risks the Skill Must Infer

The input contains data that implies risks nobody explicitly named. These are the core test of whether the skill adds PM judgment beyond what's stated:

| # | Risk | Must Catch? | What good detection looks like |
|---|------|-------------|-------------------------------|
| 1 | **Velocity risk** — Day 8 of 10, only 8 of 23 points done (35%). Even if the 10 in-progress/review points clear, that leaves 5 points (PMT-206) not started. The sprint goal ("ship installment schedule for Mexico") is at risk. | Yes | Names the velocity gap explicitly. "On day 8, 35% of committed work is done" — not just "some stories are still in progress." |
| 2 | **Localization blocker threatens the sprint goal** — PMT-206 is blocked on an external team that's unresponsive. Sarah has already proposed a fallback (ship English-only, patch next sprint). But the sprint goal is "ship for Mexico" — shipping English-only to a Spanish-speaking market is arguably not meeting the goal. | Yes | Surfaces this as a sprint goal risk, not just a ticket blocker. Connects the blocker to the Mexico launch question Carlos is asking. |
| 3 | **Mexico launch timeline risk (bigger picture)** — Installment visibility is 1 of 3 required features. The other two (payment reminders, loan restructuring) haven't started. Even if this sprint ships cleanly, June 30 looks tight for all three features. The VP is asking "are we going to hit June 30?" and the honest answer is "this feature is on track, but the overall launch has risk." | Yes | Doesn't just report sprint status — connects to Carlos's actual question about the June 30 launch. Flags the broader timeline concern. |
| 4 | **Data team dependency** — PMT-207 analytics events are waiting on data team schema confirmation. This is minor but it's a cross-team dependency that could slip. | Should flag | Mentions this as a low-severity dependency. Doesn't inflate it, but doesn't ignore it either. |

---

## VP Audience Calibration

Carlos is VP Engineering. He wants to know about the Mexico launch timeline. The update should be calibrated accordingly:

| Check | Pass | Fail |
|-------|------|------|
| **Lead with assessment** | "Sprint 14 is at risk for its stated goal" or "Installment visibility is on track with one caveat" — reader knows the state in sentence one | Leads with "This week the team completed PMT-201 and PMT-202..." |
| **Strategic framing** | Connects sprint status to Mexico launch timeline — Carlos's actual question | Reports sprint tickets without connecting to the launch timeline |
| **Right detail level** | Ticket numbers referenced but not the focus. Workstream-level status with key risks. | Line-by-line ticket status report that reads like a standup summary |
| **"Needs from you" section** | If Carlos can help (e.g., escalate localization team priority, make a call on English-only fallback), ask explicitly | No asks, or asks buried in the body |
| **Risk prominence** | Risks in the first half of the update, before wins | Risks at the bottom after a list of completed work |

---

## Smell Detection

| Smell | Should detect? | What to look for |
|-------|---------------|-----------------|
| **Smell 6 (Activity as Progress)** | Yes | The input lists 8 completed points. The skill should report this as context for the assessment, not as the point of the update. "We completed 8 of 23 points" is not "we're on track." |
| **Smell 12 (Risk Buried)** | Yes — in its own output | The localization blocker and velocity gap should be prominent, not mentioned in passing. |
| **Smell 4 (Audience Mismatch)** | Yes — in its own output | The output should be VP-level, not engineer-level. |

---

## Quality Checks

### Assessment Quality
Does the internal analysis (which informs the draft) correctly assess the sprint as "at risk"? The data clearly shows: 35% complete on day 8, a blocker on a sprint-goal-critical story, and a broader timeline concern.

**Pass:** Assesses sprint as "at risk" and explains why. **Fail:** Assesses as "on track" or "minor concerns."

### Honest Answer to the VP's Question
Carlos asked "are we going to hit June 30?" The skill should address this directly, not dodge it. The honest answer: "Installment visibility will likely ship this sprint or early next. But the full Mexico launch (3 features) has timeline risk because payment reminders and loan restructuring haven't started."

**Pass:** Addresses the June 30 question directly with an honest assessment. **Fail:** Only reports sprint status without connecting to the launch timeline.

### Fallback Framing
Sarah proposed shipping English-only and patching localization next sprint. The update should present this as an option for Carlos to weigh in on — not assume the decision is made.

**Pass:** Presents the English-only fallback as an option with trade-offs. **Fail:** Either ignores the fallback or presents it as decided.

---

## Overall Assessment

**Would Carlos read this update and know exactly where things stand — including things nobody told him explicitly?**

- Does he know the sprint is at risk and why?
- Does he know the localization team is unresponsive and there's a fallback option?
- Does he know the broader Mexico launch has timeline risk beyond this sprint?
- Does he know what he needs to do (if anything)?

**Pass threshold:** Correctly identifies draft mode with VP audience, assesses sprint as "at risk," catches all 3 must-catch risks (velocity, localization, Mexico timeline), addresses the June 30 question honestly, and leads with assessment not activity.

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| Mode and audience detection | 10% | Draft mode identified; VP audience calibrated |
| Risks correctly inferred | 30% | All 3 must-catch risks surfaced (velocity, localization, Mexico timeline) |
| VP audience calibration | 20% | Leads with assessment; strategic framing; right detail level; explicit ask |
| Honest answer to VP's question | 15% | June 30 question addressed directly with honest assessment |
| Fallback framing | 10% | English-only fallback presented as option, not assumed decided |
| Smell detection | 10% | Avoids Activity as Progress, Risk Buried, Audience Mismatch in its own output |
| Output format compliance | 5% | Matches declared format; context note present |
