# Evaluation Rubric — decision-log (B2B SaaS: Native App vs. Mobile Web)

**Target input:** `evals/decision-log/sample-input-02.md`
**Skill under test:** `skills/decision-log/SKILL.md`
**Purpose:** Determine whether `decision-log` correctly triggers Structure mode, frames genuine alternatives (including hybrid/PWA), assesses reversibility honestly (native app is a one-way door in terms of maintenance burden), interprets mobile session data for what it implies about the right solution, frames the escalation fork clearly, and closes each option with a verdict rather than just a trade-off summary.

**Coverage:** Single mode — Structure mode tested (pending decision).

---

## Mode Detection

PM says "we haven't decided" and asks to "structure this decision" for a leadership meeting in 2 weeks. This is unambiguously Structure mode.

**Pass:** Produces a structured decision brief ready for the leadership meeting — options, trade-offs, reversibility, recommendation, escalation fork, named deciders. Not a record of a decision already made.
**Fail:** Produces a Capture-style log as if "build native" has been decided. Treats the VP Product's advocacy as a decision signal rather than a stakeholder position.

---

## Problem Framing (Problem-First)

The decision should be framed as a problem question, not a solution question. "Should we build native or stay mobile web?" is solution-framed. The right framing opens space for options beyond the binary.

**Pass:** Decision framed as something like "How do we best serve our 40% of mobile users while managing engineering investment at a pre-Series B stage?" or "What mobile experience strategy best supports our enterprise sales goals without overcommitting engineering resources?" The framing is problem-first and opens the door to options beyond the native vs. mobile-web binary.
**Fail:** Framing is "Should we build a native iOS app or stay mobile-web-only?" — this is a solution-framed binary that closes off intermediate options before the analysis begins.

---

## Genuine Alternatives (Not Strawmen)

The two obvious options are native iOS app and mobile-web-only. A strong Structure output adds at least one more — specifically the Progressive Web App (PWA) option, which the PM explicitly suspects may exist ("I feel like there might be a middle ground") but cannot articulate.

| Alternative | What a genuine assessment looks like |
|-------------|--------------------------------------|
| Native iOS app (iOS-first, Android later) | High cost (4-5 months, 2 engineers, 1 engineer ongoing), long timeline, delays Q3 roadmap. Benefit: App Store presence, push notifications, enterprise procurement checklist signal. One-way door: creates permanent support obligation. |
| Progressive Web App (PWA) | Web-based app-like experience installable from browser, no App Store required. Moderate build effort (likely 6-8 weeks, not 4-5 months). Addresses "app-like experience" need. No push notifications in all browsers. No App Store checkbox. Often underconsidered by teams not familiar with the capability. |
| Mobile web optimization only | Improve the existing mobile web UX — faster load, better navigation, touch-optimized. Low cost, ships fast. No App Store presence. Does not satisfy the enterprise procurement checklist. Addresses the "checking in" use case well if the UX is fast. |
| Do nothing | Maintain status quo. Lowest cost. Growing mobile user base underserved. Enterprise sales gap persists. |

**Pass:** At least 3 genuine alternatives including PWA or equivalent hybrid option. "Do nothing" present with honest assessment of cost of inaction (enterprise deals at risk per Kieran's data). PWA is not a strawman — it gets a genuine treatment with real trade-offs.
**Fail:** Only "build native app" vs. "don't build native app." PWA not mentioned or dismissed without analysis. "Do nothing" absent or characterized as clearly unacceptable without evidence.

---

## Reversibility Honest

Building a native iOS app is a one-way door in a specific and important sense: once you ship it and users adopt it, you cannot simply stop supporting it without user impact, enterprise credibility damage, and potential deal loss.

**Pass:** Names the one-way-door nature explicitly: "Shipping an iOS app creates a permanent maintenance obligation. Unlike a feature flag or a web update, you cannot remove a native app from users' devices or stop supporting it without visible degradation — review score drops, user complaints, enterprise relationship risk. The 1-engineer-ongoing estimate is not a sunk cost; it is a commitment floor that cannot be walked back without consequences." Contrasts this with PWA and mobile web optimization, which are closer to two-way doors.
**Fail:** Treats all options as equally reversible — "we can always change direction later" — without naming that native app support obligations are structurally different from web product decisions.

---

## Mobile Session Data Interpreted

The PM provided that mobile sessions are 3x shorter than desktop (7 min vs. 22 min). This is the most important data point in the input. The skill must interpret it for what it implies about the right solution.

**Pass:** Interprets the session data explicitly: "Mobile users are in checking mode, not creation mode. A 7-minute average session strongly suggests users are reviewing status, checking task completion, and getting quick context — not creating projects, building timelines, or doing deep work. This matters for the solution: a native app optimized for full productivity may be solving the wrong problem. The actual mobile use case — fast status checks — is arguably better served by a fast, lightweight experience (PWA or optimized mobile web) than by a full native app with all its development and maintenance overhead. Before committing to a native app, test whether the enterprise sales signal is really about native app capability or about mobile UX quality."

**Fail:** Session data mentioned in the context section but not interpreted for what it implies about which solution fits the actual use case. Treating native app as the default answer without connecting it to the observed user behavior.

---

## Escalation Fork Framed

The decision is at an impasse (CFO vs. VP Product vs. Sales signal). The Structure output must frame a clear escalation fork with named paths and a named decider.

**Pass:** Names the fork explicitly with at least two paths and a named decision owner:

- Path A: Prioritize enterprise sales signal → build native iOS. Accepts 4-5 month delay to Q3 roadmap, 1-engineer ongoing commitment, and pre-Series B engineering budget risk. Decider: CEO/CFO must explicitly sign off on the budget commitment.
- Path B: Invest in PWA as the middle path → addresses mobile UX need without App Store, tests whether the enterprise signal is about capability or experience. Lower cost, faster to ship, reversible. Decider: VP Product + PM, no C-suite resource approval needed.
- Path C: Delay the decision → wait until post-Series B when engineering budget is less constrained. Accept the risk of losing enterprise deals in the interim. Decider: CEO.

**Fail:** Presents trade-offs without framing a fork. "It depends on your priorities" without naming who decides and what they're committing to.

---

## Option Verdicts

Each alternative must close with a verdict — not just a trade-off summary. Neutral options tables are easier to produce but less useful for decision-making.

**Pass:** Each option ends with a verdict:
- Native iOS app: "Not recommended at pre-Series B without first testing whether the enterprise gap can be addressed by PWA."
- PWA: "Recommended as the first step — lower cost, ships in weeks not months, and will tell us whether the enterprise sales signal is about capability or experience quality."
- Mobile web optimization: "Viable if the enterprise procurement checkbox is not a real deal-killer — but Kieran's data suggests it is."
- Do nothing: "Not recommended — the enterprise signal is credible (two lost deals) and mobile usage is growing."

**Fail:** Options presented as neutral pros/cons without a directional recommendation. The PM finishes reading and still doesn't know what to bring to leadership as the recommendation.

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| Structure mode detected (not Capture) | 10% | Produces a structured brief for a pending decision, not a record of a decided outcome |
| Genuine alternatives (≥3, including hybrid/PWA) | 20% | At least 3 options including PWA or equivalent. "Do nothing" present with honest assessment. No strawmen. |
| Reversibility assessed honestly for native app | 15% | Names the permanent support obligation as a one-way door distinct from web-based options |
| Mobile session data interpreted for solution implications | 15% | 7-min sessions = checking mode, not creation mode. Implies fast/lightweight beats full native for the actual use case. |
| Escalation fork with named paths and decision owner | 20% | At least 2 clear paths named. Decision owner named for each path. PM leaves knowing who needs to make what call. |
| Each option closes with a verdict | 20% | Every option has "Recommended" / "Viable" / "Not recommended" with one-sentence rationale. Not just a trade-off list. |
