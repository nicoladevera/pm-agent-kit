# Evaluation Rubric — decision-log

**Target input:** `eval/decision-log/sample-input-01.md`
**Skill under test:** `skills/decision-log/SKILL.md`
**Purpose:** Determine whether `decision-log` extracts structure from messy conversational input, considers all options genuinely, and produces a decision document ready for resolution.

---

## Mode Detection

The input includes a PM note saying "I don't think we actually made a final decision yet" and "help me structure this for Thursday's meeting." The skill should detect **structure mode** (pending decision, not capture).

**Pass:** Produces a pending decision document / escalation brief framed for Thursday's meeting. **Fail:** Treats this as a decided outcome and logs "build" as the decision.

---

## Planted Issues

The sample input contains four deliberate gaps the skill should catch:

| # | Issue | Must Catch? | What a good detection looks like |
|---|-------|-------------|----------------------------------|
| 1 | **"Do nothing" not considered** — The thread jumps straight to build vs. buy. Nobody asked whether the existing system could handle this with a simpler workaround (e.g., manual reminders, cron job with existing tools, delaying the feature). | Yes | Names "do nothing" or "delay/simplify" as a missing option. Adds it to the options table, even if just to explicitly dismiss it. |
| 2 | **Hybrid option not explored** — Buy for v1 to hit the Q2 timeline, build the custom service in Q3 when capacity frees up. This is arguably the strongest option and nobody mentioned it. | Should flag | Either adds this as an explicit option or notes in the output that a phased approach wasn't discussed. |
| 3 | **Capacity cost unresolved** — Dev explicitly raised the concern about team capacity and carryover. Sarah was asked to provide estimates but hasn't yet. The decision can't be made without this information. | Yes | Lists capacity/resource plan as a required input before the decision can be made. Flags it in Open Items. |
| 4 | **Reversibility not assessed** — Nobody discussed whether this is a one-way or two-way door. Building a shared notification service is arguably a one-way door (hard to rip out and replace with a vendor later). Buying is more of a two-way door (can replace vendor or build later). | Yes | Assesses reversibility for each option in the options table. |

---

## Intentional Strengths in the Input

The thread contains useful information the skill should preserve, not lose:

| Element | What's strong about it |
|---------|----------------------|
| **Multi-product justification** | Sarah's point that lending support, payment reminders, and marketing all need notifications — this is a key factor favoring build |
| **Volume economics** | 150K active users, per-message pricing concern — concrete data point |
| **Timeline constraint** | Mexico launch in Q2, ~10 weeks — the skill should anchor the decision to this deadline |
| **SRE perspective** | James's ops argument about owning critical path — a distinct concern from cost or timeline |

**Preservation check:** If any of these concrete data points are lost in the structuring, the output is less useful than the original Slack thread.

---

## Quality Checks

### Decision Question Framing
Is the decision framed problem-first? "How do we deliver notification capabilities for the Mexico launch and beyond?" is better than "Should we build or buy a notification system?" The problem framing opens space for options beyond build vs. buy.

**Pass:** Problem-first framing. **Fail:** Binary build-vs-buy framing without broader context.

### Options Table Quality
Does each option have genuine pros and cons? Are trade-offs honest? Is reversibility assessed?

**Pass:** 3+ options (including at least one the thread didn't consider), honest trade-offs, reversibility noted. **Fail:** Only build and buy with pros/cons restating what was already in the thread.

### Recommendation
Does the skill state a recommendation if the input provides enough signal? The thread leans build, with the PM noting the same. The skill should either recommend with reasoning or explain what information is needed before recommending (capacity plan from Sarah).

**Pass:** Either a conditional recommendation ("recommend build IF capacity plan confirms feasibility") or a clear statement of what's needed before recommending. **Fail:** No recommendation at all, or a recommendation without acknowledging the unresolved capacity question.

### Smell Detection
Does the skill catch smell 14 (options not considered)? The thread presents this as a binary choice when at least one additional option exists.

**Pass:** Flags the limited option set. **Fail:** Accepts build vs. buy as the complete option space.

---

## Overall Assessment

**Would a PM walk into Thursday's meeting prepared with this document?**

- Does the document frame the decision clearly enough that the meeting can focus on deciding, not on understanding?
- Are the options complete enough that the team isn't blindsided by "what about...?"
- Is the unresolved information (capacity plan) called out clearly so people arrive with it?
- Could the decider make the call based on what's written, plus the missing data?

**Pass threshold:** Correctly identifies structure mode, frames the decision problem-first, includes at least 3 genuine options, flags the capacity gap, assesses reversibility, and either recommends conditionally or explains what's needed to recommend.
