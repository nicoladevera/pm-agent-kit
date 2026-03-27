# Pushback and Negotiation

How a strong PM protects scope, navigates disagreement, and escalates when needed. Use this when reviewing documents with scope boundaries, drafting sprint plans under capacity pressure, structuring escalation decisions, or any situation where saying no, reframing, or holding a line is the right move. The goal is never to win an argument — it's to make the right trade-off visible and get explicit agreement on it.

---

## 1. Saying No / Not Now

Hard refusals burn bridges and close doors. Conditional holds preserve the relationship and keep the path open. The strongest "no" is one that names what would need to be true for the answer to change.

**Frame around conditions, not authority:**
- "We can't do this in Q2 because [capacity math / dependency X isn't ready / the problem isn't well-enough defined yet]"
- "This becomes viable when [condition] — here's what that looks like"
- "The current answer is not now, because [specific reason]. When [X changes], let's revisit"

**Timeline math is your friend.** When someone pushes for inclusion, show the arithmetic: available capacity, committed work, what gets displaced. Numbers are harder to argue with than opinions. "Adding this means dropping Y or slipping the deadline by Z days" is more useful than "we don't have bandwidth."

**Early-stage incompleteness is a valid reason to defer.** A request that hasn't been through problem definition isn't ready for a sprint — that's not a judgment on the idea, it's a statement about readiness. Name it that way: "This needs problem definition before we can size and schedule it."

**Always leave a door open.** Every "not now" should include a "when" or a "what would need to change." This isn't softness — it's honesty about conditions.

**Evaluate:** Is the "no" framed around conditions, not authority? Is there a path back? Would the person hearing this understand what needs to change for the answer to become yes?

---

## 2. Scope Protection

Scope doesn't erode in dramatic moments. It erodes in small, reasonable-sounding additions that nobody wrote down. The defense is simple: write scope down, get confirmation, and attach delivery-risk language to any flexibility.

**Write scope as confirmable contracts:**
- "We are NOT doing X — please confirm"
- "The following items are explicitly out of scope for this sprint/release: [list]"
- "Scope is confirmed as of [date]. Additions from this point require a trade-off conversation"

**Soft suggestions erode.** "We're probably not going to get to X" is an invitation to push. "X is out of scope — confirmed on [date] by [person]" is a boundary. The difference is specificity and attribution.

**Attach delivery-risk language to open-ended commitments:**
- "Our current estimates are based on confirmed scope as of [date]. New requirements from this point could result in delivery risks"
- "If scope changes after sprint commitment, we'll need to re-evaluate the sprint goal and communicate the impact"

**When scope pressure comes from above:** Don't just absorb it. Name the trade-off: "We can add X if we drop Y or extend the timeline by Z. Which do you prefer?" Force the choice into the open rather than silently overcommitting.

**Evaluate:** Are scope boundaries written as confirmable contracts or soft suggestions? Is there a named date and person attached to scope confirmation? Would this boundary survive pressure from a senior stakeholder, or would it fold?

---

## 3. Problem Reframing

When a conversation is stuck — people talking past each other, debating solutions without agreeing on the problem, or circling without progress — the PM's job is to name the confusion and decompose it.

**Name confusion explicitly:**
- "I think we're debating two different things — let me try to separate them"
- "I'm not aligned on [specific point] — here's where my understanding diverges"
- "Before we pick a solution, can we confirm we agree on the problem?"

**Use "I'm not aligned" not "this is wrong."** The first invites conversation. The second invites defense. Both might be true, but the first one gets you to resolution faster.

**Decompose into discrete, answerable questions.** A tangled discussion usually contains 2-3 separate questions masquerading as one. Pull them apart:
- "I think there are three questions here: (1) Do we agree this is a problem worth solving? (2) If yes, is this the right quarter for it? (3) If yes, which approach do we take?"

**Reframe solution-first conversations as problem-first.** When someone proposes a solution, ask what problem it solves. Not as a challenge — as genuine clarification. "Help me understand — what's the user problem this addresses?" often reveals that the problem hasn't been articulated yet.

**Evaluate:** When confusion exists, is it named and decomposed? Are tangled debates separated into discrete questions? Does the reframing move the conversation forward or just restate the disagreement?

---

## 4. Navigating Disagreement

Disagreement is normal. Productive disagreement requires structure: pair your pushback with something specific and quotable, ground it in reasoning, and calibrate your directness to the setting.

**Pair pushback with a specific anchor:**
- A data point: "Usage data shows 80% of users never touch this feature — I'd want to see evidence of demand before investing here"
- A principle: "Our team norm is to ship instrumentation with every feature. Skipping it here sets a precedent"
- An analogy: "This feels similar to what happened with [X] — we added scope mid-sprint and carried over three stories"

**Reasoning structure matters.** "I disagree" is a position. "I disagree because [evidence/principle/pattern] suggests [consequence]" is an argument. The second one can be engaged with; the first one can only be overruled.

**Calibrate directness to the setting:**
- **Private (1:1, DM):** Be direct. "I think this is the wrong call because [reason]." Directness in private is a gift — it gives the other person space to reconsider without audience pressure.
- **Public (meeting, group Slack):** Be diplomatically direct. "I see it differently — [reasoning]. Can we look at [evidence] before committing?" Preserve the other person's standing while still stating your position clearly.

**Don't soften to the point of invisibility.** "I wonder if maybe we might want to consider possibly looking at alternatives" is not pushback — it's background noise. Say what you mean. Be kind about it, but say it.

**Evaluate:** Is disagreement grounded in evidence, or just a position stated louder? Is there a quotable anchor (data, principle, pattern) that others can engage with? Is the directness calibrated to the setting?

---

## 5. Escalation

Escalate when the issue is systemic, crosses organizational levels, or can't be resolved at the current level of authority. Don't escalate complaints — escalate decision forks.

**Frame as a fork, not a grievance:**
- "We're at a point where two paths diverge, and the choice has implications beyond our team. Here are the paths, the consequences of each, and who I think needs to make this call"
- Not: "Engineering won't prioritize our work and it's blocking the roadmap"

**Name the decision owner.** Escalation without a named decider is just venting upward. Be specific: "This decision sits with [person/role] because [reason — authority level, cross-team impact, resource commitment]."

**Name the paths and consequences:**
- Path A: [What it involves]. Consequence: [What happens — timeline, cost, risk, opportunity]
- Path B: [What it involves]. Consequence: [What happens]
- What happens if no decision is made: [The cost of inaction]

**Escalate the decision, not the emotion.** Strip out frustration, attribution of blame, and narrative about who did what wrong. The decider needs a clean decision frame, not a story about organizational dysfunction.

**When to escalate:**
- The issue affects teams beyond your own and can't be resolved bilaterally
- You've tried to align at your level and reached an impasse
- The decision commits resources or changes commitments beyond your authority
- A pattern is recurring and the root cause is structural, not interpersonal

**Evaluate:** Is escalation framed as a decision fork with named paths and consequences? Is there a specific decision owner identified? Is the escalation clean of blame and focused on the choice that needs to be made?

---

## 6. Using This Reference

**Skills that reference this file:**

- **`doc-review`** — When reviewing documents with scope definitions or trade-off sections (PRDs, project briefs, tech specs), checks whether scope boundaries are written as confirmable contracts. Uses Section 2 (Scope Protection).
- **`sprint-plan`** — When capacity doesn't fit requested scope, frames trade-offs explicitly. Uses Section 2 (Scope Protection) and Section 1 (Saying No / Not Now).
- **`decision-log`** — When structuring escalation decisions that need executive ownership. Uses Section 5 (Escalation).

**General applicability:** Any skill that produces or evaluates artifacts involving trade-offs, scope boundaries, or stakeholder disagreement can draw on this reference. The patterns here are not skill-specific — they encode how a strong PM holds a line, navigates tension, and makes trade-offs visible.
