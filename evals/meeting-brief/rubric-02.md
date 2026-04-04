# Evaluation Rubric — meeting-brief (Consumer E-Commerce: Checkout Redesign Review)

**Target input:** `evals/meeting-brief/sample-input-02.md`
**Skill under test:** `.claude/skills/meeting-brief/SKILL.md`
**Purpose:** Determine whether `meeting-brief` surfaces all 3 explicit decisions, correctly maps attendee stakes to specific topics, flags the overloaded agenda (5 items, 45 min), and recommends removing or async-ing the FYI item.

**Coverage:** Single mode — full skill coverage.

---

## Key Challenges in This Input

This meeting has four problems the brief should address:

| # | Challenge | What a good brief does |
|---|-----------|------------------------|
| 1 | **Overloaded agenda** — 5 items in 45 minutes with 3 decisions to make. Even 4 substantive items would be tight. | Names the time pressure explicitly. Proposes a time allocation that's honest about what fits in 45 minutes. |
| 2 | **Hidden conflict** — Sam wants promo code in scope; Maya has unpublished feasibility concerns; PM hasn't surfaced either concern publicly. Both need structured space. | Frames the promo code discussion as a scoping decision with a known advocate (Sam) and maps it to the timeline risk Maya hasn't said publicly. |
| 3 | **Unshared data** — Alex has abandonment analysis directly relevant to the design decision but no one else has seen it. | Flags Alex's data as a pre-read to distribute before the meeting. Not to be revealed live. |
| 4 | **FYI item on the agenda** — "General team update" is not a decision or discussion item. | Calls it out as async and removes it from the 45-minute agenda. |

---

## Meeting Objective

The brief must state the objective as an outcome, not an activity.

**Pass:** Objective framed as: "By the end of this meeting, we will have a decision on the checkout design direction (approve/revise/reject), a scoping decision on promo code entry (in or out for launch), and either a confirmed Q3 timeline or an explicit acknowledgment of timeline risk." (Exact wording may vary — the key is that it names all three decisions as the output.)

**Fail:** Objective stated as "review the checkout redesign" or "discuss the upcoming checkout launch" — these are activities, not outcomes. If the objective could be satisfied by having a 45-minute conversation with no decisions, it has failed.

---

## Attendee Stakes

The brief must map each attendee's specific stake in this meeting — not their title or generic role description.

| Attendee | Their specific stake (must be in the brief) | Must catch? |
|----------|---------------------------------------------|-------------|
| Maya Chen | Holds an unpublished feasibility concern about address autocomplete and order summary animation complexity. Her buy-in on the Q3 timeline is required — and she can't give it honestly until she has space to surface the concern. | Yes |
| Jordan Park | Presenting the design for the first time to the full group. Wants actionable feedback and a direction, not another meeting. Needs the outcome to be a clear approve/revise/reject call. | Yes |
| Sam Rivera | Advocating for promo code entry before launch. Her June campaign depends on it. She will push for it — the brief should name this as a known dynamic, not let it be a surprise. | Yes |
| Alex Torres | Has abandonment data showing the address entry step (a redesigned component) is the highest-dropout mobile step. This data should inform the design decision. She needs to share it as a pre-read, not reveal it live. | Yes |
| PM | Needs all three decisions. Owns the agenda. At risk of the meeting getting consumed by the promo code debate without resolving the design direction. | Should catch |

**Pass:** Stakes are specific to this meeting and these topics. Maya's unpublished concern is named. Alex's pre-read data is called out as something to distribute in advance.
**Fail:** Generic descriptions like "Maya cares about engineering feasibility" or "Sam is interested in the launch." Stakes that could apply to any meeting.

---

## Three Decisions Surfaced

All three decisions must appear as explicit, named decision points — not buried inside discussion topics.

| Decision | Must appear as explicit decision? | Key details |
|----------|-----------------------------------|-------------|
| Design direction: approve / revise / reject Jordan's checkout flow | Yes | Decider: PM (with input from group). Required input: Jordan's design + Maya's feasibility read. |
| Promo code scope: in or out for Q3 launch | Yes | Options known (add it vs. defer it). Sam is an advocate. Affects launch timeline. |
| Q3 timeline: viable or not | Yes | Depends on Maya surfacing her feasibility concern. Decider: PM + Maya jointly, with awareness of promo code scope. |

**Pass:** All three appear in a "Decisions on the Table" section (or equivalent) as named decision questions with options and decider. Not just mentioned once inside an agenda topic description.
**Fail:** Decisions embedded in discussion items without being surfaced as decisions. Fewer than 3 decisions listed. "General discussion of the timeline" instead of "Decision: Is Q3 viable given Maya's feasibility concerns?"

---

## Overloaded Agenda Flagged

5 items in 45 minutes with 3 decisions is too much. The brief must name this.

**Pass:** Brief explicitly states the agenda is overloaded. Proposes a time allocation for each item that sums to 45 minutes, with realistic weighting. An approximate pass-criterion allocation:
- Design review + design direction decision: 15 min
- Promo code scope decision: 10 min
- Q3 timeline decision: 10 min
- Alex's data (if not pre-read, though brief should recommend pre-read): 5 min
- Buffer: 5 min
- General team update: 0 min (async'd)

The exact split may vary, but time allocations must total 45 minutes and must exclude or minimize the FYI item.

**Fail:** All 5 items presented with no comment on feasibility. Time allocation sums to more than 45 minutes. Agenda treated as if it's fine as-is.

---

## FYI Item Recommended as Async

The "general team update" is company news — not a decision, not a discussion, not requiring synchronous time.

**Pass:** "General team update" explicitly called out as an async item. Brief recommends sending it as a Slack message or email instead of consuming meeting time. Item removed from the proposed 45-minute agenda.
**Fail:** "General team update" included as a meeting agenda item alongside the decisions. No comment on whether it belongs in the meeting.

---

## Alex's Data Flagged as Pre-Read

Alex has abandonment data showing the address entry step — a component the redesign changes — has the highest mobile dropout rate. This directly informs the design decision. Revealing it for the first time during the meeting is inefficient and risks derailing the discussion.

**Pass:** Alex's mobile abandonment analysis is listed as a pre-read to distribute before the meeting. Brief notes that attendees — especially Jordan and Maya — should review it before arriving, so the design discussion can be informed by the data rather than surprised by it. May include a note that "sharing data live that could have been a pre-read wastes the room's time on context-setting."
**Fail:** Alex's data not mentioned as a pre-read. Data presumably shared live during the meeting. No pre-read section, or pre-read section doesn't include Alex's analysis.

---

## Overall Assessment

**Would attendees arrive at this meeting ready to decide in 45 minutes?**

- Does Maya know she has space to surface her feasibility concern — and that it won't be treated as a surprise?
- Does Jordan know the expected outcome is a direction (not just "feedback")?
- Does Sam know the promo code will be decided, not debated indefinitely?
- Has Alex been asked to share her data in advance?
- Has the PM removed the general team update from the meeting agenda?

**Pass threshold:** Surfaces all 3 decisions explicitly, provides attendee-specific stakes (not role descriptions), flags the overloaded agenda with time allocation, removes or async-ids the FYI item, and identifies Alex's analysis as a pre-read.

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| Meeting objective as outcome (not activity) | 10% | Objective names all 3 decisions as the required outputs of the meeting |
| All 3 decisions surfaced as explicit decision points | 25% | Approve/revise/reject design, promo code in/out, Q3 viable or not — all present as named decisions with options and deciders |
| Attendee stakes specific and accurate | 20% | Maya's unpublished concern named; Jordan's need for a direction named; Sam's advocacy named; Alex's data role named |
| Overloaded agenda flagged with time allocation | 15% | Agenda named as overloaded; time split proposed that sums to 45 minutes |
| FYI item recommended as async | 15% | General team update removed from meeting and recommended as Slack/email |
| Alex's data called out as pre-read | 15% | Alex's mobile abandonment analysis listed as pre-read to distribute before the meeting |
