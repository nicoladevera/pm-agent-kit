# Decision Frameworks

What makes a decision well-captured and well-structured. Use this to log decisions that have been made or to frame decisions that need to be made. A decision log that someone can't understand six months later failed at its only job.

---

## Decision Anatomy

Every decision — made or pending — has the same components. The difference between a logged decision and an escalation brief is whether the "Decision" field is filled in.

| Component | What it is | Why it matters |
|-----------|-----------|---------------|
| **The question** | What are we deciding? Framed as a specific, answerable question. | Without a clear question, people debate different things in the same room. |
| **The context** | Why this decision matters now. What prompted it. What's at stake. | Decisions without context can't be evaluated — or re-evaluated later. |
| **The options** | At least 2 genuine alternatives with honest trade-offs. | A decision with one option isn't a decision — it's a fait accompli. |
| **The criteria** | What matters most in choosing. What are we optimizing for? | Makes the reasoning transparent and auditable. |
| **The recommendation** | The PM's point of view, stated directly. | Come with a position. Don't present options and wait for someone else to think. |
| **The decision** | What was decided. By whom. When. | The whole point. If this isn't clear, the log failed. |
| **The rationale** | Why this option over the others. | Six months from now, "we chose option A" means nothing without "because X mattered more than Y." |
| **What was rejected** | Options considered but not chosen, and why. | Prevents relitigating. Shows the decision was made thoughtfully, not reflexively. |

---

## Problem Before Options

Frame the decision question before listing solutions. "Should we build or buy a notification system?" is a solution-framed question. "How do we reduce first-payment miss rates from 12% to under 5%?" is a problem-framed question. The second one might lead to building a notification system — or it might lead to something better.

**In practice:**
- Decision logs start with what's being decided and why it matters — not with the recommended option
- Escalation briefs open with the situation and stakes before presenting choices
- The context section earns the reader's attention before asking them to evaluate options

**Red flag:** A decision log that leads with "We decided to..." and only explains context after. An escalation brief that opens with the recommendation and backfills the reasoning.

---

## Options Quality

### Genuine Alternatives

At minimum 2 real options. Each option should be something the team could actually choose — not a strawman designed to make the preferred option look good. "Do nothing" is always a valid option and should be explicitly considered; sometimes it's the right one.

**For each option, state:**
- What it involves (enough to understand, not a full spec)
- Pros — what you gain
- Cons — what it costs or risks
- Trade-offs — what you give up by choosing this over the others

**Red flag:** Options where one is clearly superior in every dimension (the others are strawmen). Options missing cons. "Do nothing" not considered when it's viable. Options that are variations of the same approach rather than genuinely different paths.

---

## Reversibility Assessment

Not all decisions deserve the same process. The right amount of rigor depends on how hard the decision is to undo.

| Type | What it means | How much rigor |
|------|--------------|----------------|
| **One-way door** | Hard or impossible to reverse. Architectural choices, public commitments, team restructuring, deprecating a product. | Full decision framework. Multiple stakeholders. Written record with rationale. |
| **Two-way door** | Easy to reverse or iterate on. Feature flags, UI copy, pricing experiments, process tweaks. | Lighter process. Decide, ship, evaluate. Don't over-deliberate. |

**Name which type this is.** If the decision is a two-way door, say so — it gives the decider permission to move fast. If it's a one-way door, say so — it signals that the extra deliberation is warranted, not overhead.

**Red flag:** One-way doors treated casually ("let's just try it and see"). Two-way doors treated like one-way doors (three meetings and an RFC for a button color).

---

## Encyclopedic Context

Know the full picture before framing a decision. The difference between a useful decision log and a bureaucratic one is whether the person writing it understood the system — adjacent work, history, stakeholder stakes, technical constraints, delivery implications.

**In practice:**
- Understand prior art — has this been decided before? What changed?
- Know the stakeholder landscape — who cares about this and what do they care about?
- Understand downstream effects — what does this decision unlock or block?
- Know the constraints — timeline, budget, team capacity, technical debt

**Red flag:** A decision log that treats the decision in isolation. An escalation brief that doesn't mention who else is affected. Options evaluated without understanding the system they exist in.

---

## Recommendation with Reasoning

Come with a point of view. State it directly. The PM's job is not to present options neutrally — it's to assess the situation, form a judgment, and state it clearly while being transparent about the reasoning.

**A good recommendation:**
- States the preferred option plainly: "I recommend Option B"
- Names the reasoning: "because the timeline risk of Option A outweighs the cost savings"
- Acknowledges what's given up: "this means we accept higher infrastructure cost in exchange for shipping on schedule"
- States confidence level when appropriate: "I'm highly confident" vs. "this is a judgment call — here's what would change my mind"

**Red flag:** "Here are the options — what do you think?" with no recommendation. Recommendations hedged to the point of meaninglessness. The PM's point of view only discoverable by reading between the lines.

---

## Escalation Signals

Not every decision needs to be escalated. Escalate when:

- **Cross-team impact** — the decision affects teams beyond your own and they haven't been consulted
- **Irreversibility** — it's a one-way door with significant consequences
- **Unresolvable disagreement** — you've tried to align and can't; the decider needs to decide
- **Budget or resource threshold** — the decision commits resources beyond your authority
- **Risk to timeline or commitments** — the decision changes what's been promised to stakeholders

An escalation brief is a decision log for a decision that hasn't been made yet. It frames the decision for the decider — context, options, recommendation — so they can decide, not investigate. Don't dump the problem; present it structured.

**Red flag:** Escalation briefs that present the problem without a recommendation ("what should we do?"). Escalations that should have been handled locally. Decisions escalated to avoid accountability.

---

## Decision Debt

Decisions deferred without a timeline accumulate. They're the decision equivalent of tech debt — they don't go away, they just get more expensive.

**Track deferred decisions:**
- What decision was deferred
- Why (missing information, wrong timing, dependent on something else)
- When it should be revisited
- What happens if it's never made (the cost of inaction)

**Red flag:** A decision log full of "pending" items with no revisit date. Decisions deferred repeatedly without new information. The team working around an unmade decision instead of making it.

---

## Using These Frameworks

**For decision capture (`decision-log` capture mode):** Extract the decision anatomy from messy input — meeting notes, Slack threads, verbal downloads. The PM may not have structured the decision; the skill imposes structure while preserving the substance.

**For decision framing (`decision-log` structure mode):** When a decision needs to be made, structure it using these frameworks. Frame the question, lay out options, assess reversibility, make a recommendation. The output is an escalation brief or a decision document ready for the decider.

**For meeting prep (`meeting-brief` skill):** Identify decisions on the table for upcoming meetings. Each decision should have at minimum: the question, the known options, and who decides.

**For smell testing:** Check for Decision and Strategy Smells 14 (options not considered) and 15 (recency bias) from `pm-smell-test.md`.
