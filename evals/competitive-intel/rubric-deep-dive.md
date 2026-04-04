# Evaluation Rubric — competitive-intel (Deep Dive Mode)

**Target input:** `evals/competitive-intel/sample-input-02.md`
**Skill under test:** `.claude/skills/competitive-intel/SKILL.md`
**Purpose:** Determine whether `competitive-intel` Deep Dive mode goes beyond feature enumeration to philosophy and trade-off analysis, connects competitive insights to a specific product decision, and properly distinguishes observed facts from inferences.

## Coverage

**This rubric tests:** Deep Dive mode — named competitor (Linear), specific area (sprint planning philosophy and backlog prioritization).
**Not covered here:** Monitor mode (`rubric.md`), Research mode (deferred).

---

## Mode Detection

The input names Linear explicitly, names a specific area (sprint planning and backlog prioritization workflows), and states a decision context (whether to invest in sprint tooling before Series B). This should trigger **Deep Dive mode**.

**Pass:** Deep Dive mode selected; output is a deep dive on Linear's sprint planning philosophy, not a landscape snapshot with multiple competitors. **Fail:** Monitor mode selected (no specific analysis of Linear's philosophy and trade-offs), Research mode triggered, or mode not stated.

---

## Philosophy vs. Feature Comparison

This is the most important test. A feature-level analysis lists what Linear has. A philosophical analysis explains *why* Linear built what they built and what that implies. The analysis must go to that second level.

### Key philosophical points the analysis should capture:

| Philosophy | What it explains | What good analysis looks like |
|------------|-----------------|-------------------------------|
| **"No estimates" / cycles over sprints** | Linear explicitly rejects story point estimation as a useful practice. Cycles are scope-based, not velocity-based. There is no "sprint goal burndown" because Linear doesn't believe that model produces better outcomes. | Analysis names this as a design philosophy, not a missing feature. Explains the implicit claim: that discipline and iteration matter more than estimation precision. Notes what you give up: velocity forecasting, historical data for capacity planning, and integration with classic Scrum-style processes. |
| **Keyboard-first, speed-obsessed UX** | Linear's primary user is an engineer, not a PM. The tool is built for people who find context-switching expensive and who want zero friction between thought and action. This drives keyboard shortcuts, fast issue creation, and a deliberately minimal UI. | Analysis connects UX philosophy to product strategy: Linear is not trying to serve PMs who manage boards; they're trying to serve engineering teams who want to stay in flow. This means their sprint tooling will never be feature-complete in the "enterprise PM" sense — that's intentional. |
| **Opinionated scope (deliberate feature absence)** | Linear doesn't have Gantt charts, resource planning views, or cross-project portfolio management. This isn't an oversight — it's a stance. They have said publicly that adding those features would compromise the core experience. They'd rather lose customers who need those features than dilute for customers who don't. | Analysis names this as differentiation through deliberate constraint. Explains the trade-off: Linear serves teams who accept Linear's model; teams who don't are out of scope. For a product company trying to serve a broader B2B market, this matters — it tells you what Linear is *not* competing on. |

**Pass:** Analysis names at least 2 of the 3 philosophies above, connects each to a specific product trade-off, and relates the trade-off to the PM's decision context (build sprint tooling: what kind, for whom). **Fail:** Analysis lists Linear's features (cycles, keyboard shortcuts, no estimates, roadmap views) without explaining the reasoning behind them or the trade-offs they imply.

---

## Competitive Implication Connected to Decision

The PM's decision is whether to invest in sprint tooling before a Series B demo. The analysis should give her something to act on — not just a description of what Linear does.

### Implications the analysis should draw:

**Implication 1: Sprint tooling only works if the team adopts the discipline behind it.**

Linear's philosophy implies that the tooling is downstream of the process. Teams that don't have sprint discipline won't get value from better sprint tooling — regardless of whether it looks like Linear's cycles or classic Scrum. Building sprint features without understanding whether your customers have the discipline to use them is the wrong sequence.

**Implication 2: Entering this space means choosing a philosophy, not building a neutral tool.**

Linear made a deliberate choice (opinionated, engineer-centric, no estimates). Jira made a different choice (flexible, PM-centric, estimation-forward). There is no neutral middle ground that captures both. The PM's company needs a thesis: are their customers trying to adopt better engineering discipline (Linear territory) or are they trying to manage cross-functional PM workflows (Jira territory)? Building sprint tooling without choosing means building a mediocre version of both.

**Implication 3: Differentiation against Linear requires a clear counter-thesis, not feature parity.**

If the company builds sprint tooling that looks like Linear's cycles, they're building a worse version of Linear with fewer integrations and a smaller community. The only way to compete is to be genuinely different — e.g., building for teams that want sprint structure with flexibility (no/low estimates + optional velocity tracking), or targeting a segment Linear has deliberately excluded (e.g., multi-team portfolio management for mid-market companies above Linear's sweet spot).

**Pass:** Analysis provides at least one concrete product direction implication — something the PM can use to frame or reframe the build/don't-build decision. The implication is specific to the PM's context (200 B2B customers, Series B, kanban baseline), not generic advice about competing with Linear. **Fail:** Analysis summarizes Linear's features and concludes with "Linear is strong in this space, worth watching" without naming a direction.

---

## Source Reliability and Inference Hedging

Linear is a public product with a documented philosophy. Their founder (Karri Saarinen) has written and spoken publicly about their engineering-first approach and their stance on estimates. The analysis should distinguish what's documented from what's inferred.

### What should be hedged vs. stated as fact:

| Claim type | How it should be presented |
|------------|---------------------------|
| "Linear doesn't default to story points in Cycles" | Stated as observed fact — this is verifiable by using the product or reading their documentation |
| "Linear's founders don't believe estimation is useful" | Stated as documented position — sourced to their public writing (blog, changelog, founder interviews) |
| "Linear's keyboard-first UX is a core design principle" | Stated as documented philosophy — they've said this explicitly |
| "Linear's team believes velocity metrics are misleading" | Stated as an inference from their documented position — the "no estimates" stance implies this, but they may not have said exactly this |
| "Linear is intentionally constraining scope to stay in their sweet spot" | Inference from observable product behavior — should be flagged as interpretation, with the evidence noted (no Gantt charts, no resource planning, despite customer requests) |

**Pass:** The analysis explicitly distinguishes observed facts from inferences. At minimum: states what's documented (blog posts, public writing, product teardown) vs. what the analysis is inferring from that evidence. A parenthetical like "(this is inference from their stated position)" is acceptable. **Fail:** All statements presented as equally factual, with no acknowledgment of what's observed vs. inferred vs. speculated.

---

## Depth of Analysis on One Sub-Area

A deep dive that covers everything at the same level of detail covers nothing well. The analysis should pick the most decision-relevant sub-area and go deeper than the others. Given the PM's question, that sub-area is **cycle-based planning vs. sprint-based planning**.

### What deep analysis of this sub-area looks like:

**Level 1 — What:** Linear uses Cycles instead of Sprints. Cycles are time-boxed, have a scope (which issues are in), and track completion. They don't track story points or velocity by default.

**Level 2 — Why:** Linear's choice reflects a belief that story points add overhead without adding forecasting accuracy. Cycles are designed to answer "did we complete what we said we'd complete?" rather than "how many points did we burn down?" The distinction matters: one measures team discipline; the other attempts to measure team throughput. Linear has bet that discipline is the more useful signal.

**Level 3 — Trade-off and implication:** The cost of this approach is that you can't do velocity-based capacity planning. You can't look at historical sprint data and say "we average 38 points, so next sprint we should commit to 35-40 points." You can look at historical cycle completion rates (did we finish 70% of scope, 90%, 100%?) — but this tells you about discipline, not throughput. For a PM's company entering this space: if their customers are currently running Scrum with story points, they can't just import those customers into a cycle model without process change. That's a significant adoption barrier that a feature doesn't solve.

**Pass:** The analysis goes to at least 3 levels of depth on cycle-based planning — what it is, why Linear chose it, and what trade-off it creates for our PM's decision. The trade-off is specific to the PM's context. **Fail:** All areas (cycles, keyboard UX, no estimates, issue hierarchy) covered at the same level of surface-level description.

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| Mode detection correctly | 10% | Deep Dive mode selected; output is a named competitor deep dive, not a landscape snapshot |
| Philosophy vs. feature comparison | 25% | At least 2 of 3 philosophies named with their trade-offs; analysis explains the reasoning behind Linear's choices, not just the choices themselves |
| Competitive implication connected to decision | 20% | At least one concrete product direction implication stated, specific to the PM's context (200 B2B customers, Series B, build/don't-build decision) |
| Source reliability and inference hedging | 15% | Observed facts and inferences explicitly distinguished; documented positions vs. analysis-layer inferences noted |
| One sub-area analyzed deeply (cycle-based planning) | 20% | Cycle model analyzed at 3+ levels: what it is, why Linear chose it, what trade-off it creates |
| Output format compliance | 10% | Deep Dive format used; Agent Block present with correct fields (competitor, area, product_implication, positioning_implication, urgency, risk_level); Smell Test section present |
