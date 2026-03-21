# Evaluation Rubric — meeting-brief

**Target input:** `eval/meeting-brief/sample-input-01.md`
**Skill under test:** `skills/meeting-brief/SKILL.md`
**Purpose:** Determine whether `meeting-brief` imposes structure on an overloaded meeting, surfaces decisions, and produces a brief that makes 90 minutes productive instead of chaotic.

---

## Key Challenges in This Input

This meeting has four problems the brief should address:

| # | Challenge | What a good brief does |
|---|-----------|----------------------|
| 1 | **Overloaded agenda** — Sprint review + Q2 planning + notification decision + design review in 90 minutes. This is too much for one meeting. | Names the time pressure explicitly. Proposes a time allocation that's honest about what fits. May recommend deferring one topic or splitting into two meetings. |
| 2 | **Hidden decision** — The notification service decision from the Slack thread is on the agenda but not framed as a decision. It could consume 30+ minutes if not structured. | Surfaces this as an explicit decision with options, decider, and required inputs (Sarah's resource plan). Links back to the prior context. |
| 3 | **Mixed audiences** — Carlos (VP) cares about board-level timelines and commitments. Ana needs tactical design sign-off. The brief needs to acknowledge that not all attendees need to be present for all topics. | Identifies which attendees are relevant for which topics. May suggest an ordering that lets people drop off early. |
| 4 | **Ana's request came late** — Design review was added via DM, not on the original invite. Other attendees may not know it's on the agenda. | Includes it in the structured agenda so it's not a surprise. Notes that it was added after the original invite. |

---

## Attendee Stakes

The brief should identify specific stakes for each attendee, not just repeat their titles:

| Attendee | Expected stake | Must catch? |
|----------|---------------|-------------|
| **Carlos Reyes (VP Eng)** | Needs honest timelines for the board. Cares about Mexico launch, notification system, installment visibility. Wants commitments he can relay upward. | Yes |
| **Maria Gonzalez (PM Lead)** | Running the meeting. Needs it to produce decisions, not just discussion. Owns the Q2 roadmap narrative. | Yes |
| **Sarah Chen (Eng Lead)** | Has the notification service resource plan. Knows the capacity trade-off (notification build = pause loan restructuring). Needs a decision so she can plan. | Yes |
| **Dev Patel (Backend)** | Would be assigned full-time to notification service if build is chosen. Directly affected by the capacity decision. | Should catch |
| **Ana Torres (Design)** | Needs 10 minutes for design sign-off on installment screens. Risk of her work slipping if not reviewed. | Should catch |
| **James Wu (SRE)** | Infrastructure work required if notification service is built. Has ops perspective on build vs. buy. | Should catch |

**Pass:** Stakes are specific to this meeting, not generic role descriptions. **Fail:** "Carlos cares about engineering" or "Sarah leads the engineering team."

---

## Decisions on the Table

The brief must surface at least two decisions explicitly:

| Decision | Must surface? | Key details |
|----------|--------------|-------------|
| **Notification service: build, buy, or hybrid** | Yes | Options known from Slack thread. Sarah has resource plan with trade-off (pauses loan restructuring). Carlos likely the decider given resource implications. |
| **Q2 commitments / timelines** | Yes | Carlos needs board-ready timelines for Mexico launch, notification system, installment visibility. This is an alignment + commitment decision. |
| **Design sign-off on installment screens** | Should surface | Quick decision (10 min) but needs explicit time allocation or it gets squeezed. |

---

## Quality Checks

### Meeting Objective
Does the brief state a clear objective? Something like "Align on Q2 commitments for the board, make the notification service decision, and review Sprint 14 delivery." If the objective tries to cover everything, the brief should acknowledge the tension.

**Pass:** Clear, realistic objective that acknowledges the time pressure. **Fail:** Generic "review sprint and discuss priorities" or unrealistic objective that pretends everything fits.

### Time Allocation
Does the brief propose a time split? With 90 minutes and 4 topics, realistic allocation matters:

- Sprint review: 15-20 min (compressed)
- Notification service decision: 20-25 min (structured, not open debate)
- Q2 priority alignment: 30-35 min (Carlos's priority)
- Design review: 10 min (Ana's ask)
- Buffer: 5-10 min

**Pass:** Proposes times that add up to 90 minutes, with appropriate weighting. **Fail:** No time allocation, or times that don't reflect priority (e.g., 30 min sprint review, 15 min Q2 planning).

### Pre-Read Identification
Does the brief identify what attendees should review before the meeting?

Expected pre-reads:
- Sarah's notification service resource plan
- Sprint 14 board/burndown
- Ana's installment schedule mocks
- Any existing Q2 planning docs

**Pass:** At least 3 pre-reads identified. **Fail:** No pre-read section or generic "review the agenda."

### Structure vs. Vague Agenda
The original agenda is "Sprint review, Q2 priorities, notification service decision." Does the brief transform this into a structured agenda where each item has status, open questions, and decision-needed flags?

**Pass:** Each agenda item has concrete context, not just a topic name. **Fail:** Brief just restates "Sprint review" without adding context about what's being reviewed or what questions it should answer.

---

## Overall Assessment

**Would attendees arrive at this meeting ready to decide in 90 minutes?**

- Does Carlos know exactly what commitments he's being asked to make?
- Does Sarah know her resource plan will be discussed and what decision it feeds?
- Does Ana know she has 10 minutes and when in the agenda?
- Does Maria have a structure that prevents the meeting from becoming a 90-minute open discussion?

**Pass threshold:** Surfaces all 3 decisions, provides specific attendee stakes (not role descriptions), proposes a time allocation, identifies at least 3 pre-reads, and acknowledges the overloaded agenda honestly.
