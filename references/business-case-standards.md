# Business Case Standards

What makes a business case convincing and complete. Use this to construct the argument for or against an initiative — problem, impact sizing, proposed solution, cost, risks, alternatives considered, recommendation. The strategic counterpart to `decision-frameworks.md` — that file structures individual decisions; this file structures the investment argument that precedes them.

A business case is not a PRD. A PRD defines what to build and how. A business case argues whether to invest at all — and if so, why this approach over the alternatives. The business case earns the PRD. If the business case is weak, the PRD shouldn't exist yet.

---

## Business Case Anatomy

Every business case has the same components regardless of initiative size. A small feature investment and a major platform bet use the same structure — the depth scales, the structure doesn't.

| Component | What it is | Why it matters |
|-----------|-----------|---------------|
| **Problem / Opportunity** | What gap, pain point, or market opportunity exists. Framed independently from the solution. | Without a clear problem, the business case is a solution looking for justification. |
| **Impact Sizing** | How large the opportunity is — users affected, revenue potential, cost savings, strategic value. | The foundation of the investment argument. If the impact isn't sized, the case can't be evaluated against alternatives. |
| **Proposed Solution** | What the initiative involves and how it addresses the problem. | Enough to evaluate feasibility and cost, not a full specification. |
| **Cost Model** | What the investment requires — engineering time, opportunity cost, infrastructure, ongoing maintenance. | Total cost of ownership, not just build cost. The denominator of the ROI calculation. |
| **Risk Assessment** | What could go wrong and how likely it is. | Honest risk assessment builds credibility. Missing risks destroy it — especially when they materialize. |
| **Alternatives Considered** | At least two genuine alternatives plus "do nothing," with honest trade-offs for each. | A business case with one option isn't a case — it's a fait accompli. Alternatives prove the recommendation was chosen, not assumed. |
| **Recommendation** | The PM's point of view, stated directly. | Come with a position. Don't present options and wait for someone else to think. |

---

## Impact Sizing

Impact sizing is the analytical core of every business case. It answers: "How big is this opportunity, and how confident are we in that estimate?"

### Three Approaches

Choose the approach that best fits the available data and initiative type. State the approach explicitly — the reader should know how the numbers were derived.

#### Top-Down

Start with the total addressable population or market and narrow to what's realistically capturable.

**When to use:** New market entry, new product line, initiatives where bottom-up data doesn't exist because there's no current user behavior to extrapolate from.

**Structure:**
- Total addressable market/users (TAM)
- Serviceable addressable market/users (SAM) — what portion we could realistically reach
- Serviceable obtainable market/users (SOM) — what portion we'd realistically capture given competition, timing, and execution
- Revenue or value per captured unit

**Red flag:** Presenting TAM as if it's achievable. "The market is $2B" means nothing without the narrowing steps. A business case that jumps from total market to expected revenue is not sizing — it's wishful thinking.

#### Bottom-Up

Start with current usage data, user behavior, or operational metrics and extrapolate the impact of the proposed change.

**When to use:** Feature improvements, conversion optimization, cost reduction, initiatives where current data exists to project from.

**Structure:**
- Current baseline (what's happening now — volume, rate, cost)
- Expected change (what the initiative would improve and by how much)
- Projected impact (baseline × expected change × time period)
- Confidence basis (why you believe the expected change is realistic)

**Red flag:** Extrapolating without stating the assumption. "If we improve conversion by 5%..." needs "based on [comparable initiative / A/B test data / industry benchmark]." The "if" is doing all the work and must be grounded.

#### Analog-Based

Use the results of comparable initiatives — internal or external — as a basis for projection.

**When to use:** Limited data on the specific initiative, but comparable initiatives have been executed before (internally or at other companies).

**Structure:**
- The analog: what initiative, where, what result
- Adjustability: how similar the conditions are (market, product maturity, team, timing)
- Projected range: what the analog suggests, adjusted for known differences

**Red flag:** Cherry-picking analogs that support the desired outcome. If you use an analog, name what's different about your situation, not just what's similar.

### Sizing Standards

- **Present a range, not a single number.** Conservative / Expected / Optimistic. A single revenue projection is more suspicious than a range with stated assumptions.
- **State all assumptions explicitly.** Every number depends on something. Name it. "Assumes 60% feature adoption based on comparable feature X in Q2" is credible. "Revenue impact: $500K" without assumptions is not.
- **Name the approach and why.** Don't make the reader guess how the numbers were derived.
- **Include both quantitative and strategic value.** Some initiatives matter for reasons beyond direct revenue — competitive positioning, platform capability, user trust, retention. If strategic value is part of the case, state it explicitly rather than inflating the quantitative estimates.
- **Flag what you can't size.** "We believe this will improve retention but don't have data to size the impact" is more honest than omitting retention entirely or fabricating a number.

---

## Cost Model Standards

### What Goes Into Cost

A business case that only accounts for engineering build time is lying about the investment. Total cost of ownership includes:

| Cost Category | What it includes | Common blind spots |
|---------------|-----------------|-------------------|
| **Engineering** | Design, development, QA, code review. Convert to cost using team rates or headcount-weeks if team rate information is available. | Underestimating integration complexity. Forgetting QA time. |
| **Opportunity cost** | What doesn't get built while this is being built. Name the specific initiatives that get deprioritized or delayed. | The most important cost and the most frequently omitted. |
| **Infrastructure** | Servers, third-party services, data storage, API costs. Both one-time setup and ongoing run costs. | Scaling costs — what happens when usage grows 10x. |
| **Ongoing maintenance** | Bug fixes, performance monitoring, dependency updates, support escalations. | Everything has a maintenance tail. A feature that "ships and is done" is a fantasy. |
| **Other** | Legal review, compliance certification, vendor contracts, training, documentation. | The non-engineering costs that show up after the build is approved. |

### Cost Model Standards

- **Multi-quarter view.** Show the cost over at least 3-4 quarters, not just the initial build. Quarter 1 is build. Quarters 2-4 are maintenance + infrastructure + opportunity cost of what you're still not building.
- **Distinguish one-time from ongoing.** A $200K build with $10K/quarter maintenance is a very different investment profile than a $200K build with $80K/quarter operational cost.
- **Present as a range when uncertain.** Engineering estimates are notoriously optimistic. A range (optimistic / expected / padded) is more honest than a single number.
- **Flag hidden costs.** Support load for a user-facing feature. Documentation for a platform feature. Monitoring for a reliability initiative. These show up whether you plan for them or not.

---

## Risk Assessment Framework

### Risk Categories

Every initiative carries risks across multiple dimensions. Assess each relevant category:

| Category | What it covers | Example |
|----------|---------------|---------|
| **Execution risk** | Can we actually build this? On time? To spec? | Team lacks domain expertise. Key engineer is on parental leave. Integration with legacy system is uncertain. |
| **Market risk** | Will the market want this? Will timing work? | Competitor may ship first. Market conditions may shift. Customer need may be overestimated. |
| **Technical risk** | Will the technology work as expected? Will it scale? | Untested architecture. Performance at scale is unknown. Third-party dependency is unstable. |
| **Adoption risk** | Will users actually use it? Will behavior change? | Feature requires behavior change. Migration path is complex. Value proposition is unclear. |
| **Organizational risk** | Will the org support this through completion? | Priority may shift. Sponsorship may change. Cross-team dependency may not be honored. |

### For Each Risk

- **Likelihood:** High / Medium / Low — based on evidence, not hope
- **Impact:** High / Medium / Low — what happens if this risk materializes
- **Mitigation:** What can be done to reduce likelihood or impact. If no mitigation exists, say so.
- **Monitoring:** How you'll know the risk is materializing (leading indicators, not lagging)

### Reversibility Assessment

Connect to the reversibility framework from `decision-frameworks.md`:

- **Two-way door:** The initiative can be rolled back or pivoted without significant cost. This lowers the decision threshold — try it, learn, adjust. Feature flags, phased rollouts, and modular architecture create two-way doors.
- **One-way door:** The initiative involves commitments that are expensive or impossible to reverse — public announcements, platform migrations, contractual obligations, data model changes. One-way doors require more thorough risk assessment and higher confidence.

State the reversibility assessment explicitly. It changes how the business case should be evaluated.

---

## Alternatives Quality

### Minimum Bar

At least **two genuine alternatives** plus **"do nothing."** Each alternative must be something the organization could actually choose — not a strawman designed to make the preferred option look inevitable.

### For Each Alternative

- **What it involves** — enough to understand the approach, not a full spec
- **Pros** — what you gain
- **Cons** — what it costs or risks (every option has cons; if an option has no cons, the analysis is incomplete)
- **Trade-offs** — what you give up by choosing this over the others
- **Why it's less preferred** (or not) — the honest assessment of why the recommendation is better
- **Verdict** — a single sentence that closes the option. Characterize its role in the decision: whether it's right for a specific scenario, wrong for the current context, or worth revisiting at a future stage. Example: "Right as a stopgap if budget approval is delayed past Q2, but not the target architecture." A verdict replaces open-ended trade-off deliberation with resolution.

### "Do Nothing" Is Always an Option

Explicitly evaluate what happens if the initiative is not pursued. Sometimes "do nothing" is genuinely the right call — the opportunity cost of building may exceed the opportunity cost of not building. Articulate:
- What stays the same
- What gets worse (if the problem is growing)
- What risk is accepted
- What resources remain available for other priorities

### Red Flags

- **Strawman alternatives:** Options that are clearly inferior in every dimension, designed to make the recommendation look good. A real alternative should have at least one dimension where it's genuinely better.
- **Missing "do nothing":** The implicit message is "we must do something." Sometimes the right answer is to wait, gather more data, or invest elsewhere.
- **Only cost-differentiated:** All alternatives are versions of the same approach at different price points. Real alternatives involve different approaches, not just different budgets.
- **Recommendation presented as inevitable:** If the analysis reads as "here's why we should obviously do X, and here are some bad options we considered," the alternatives section failed.

---

## Visualization

For proposals involving system components, data flows, or decision routing, include a diagram. ASCII is the default format.

**Why ASCII:** ASCII diagrams survive copy-paste, PDF export, Confluence rendering, and Slack — they require no external tool (no Miro, no Figma, no LucidChart). A diagram that requires a link is a diagram that half the readers won't see.

**When to include a diagram:**
- The proposal involves an architecture with 3 or more components
- There is a data or process flow with sequential stages
- There is a decision routing structure (if X then Y, else Z)

**When to omit:**
- The proposal is pure business or market analysis with no system components (impact sizing, pricing changes, GTM strategy)

**Diagram standards:**
- Label every component clearly
- Show directionality with arrows (`-->`, `<--`, `<-->`)
- Keep it compact enough to read without zooming — if it needs a legend, it's too complex
- Position it in the Proposed Solution section or immediately after the component it explains

---

## Audience Calibration for Business Cases

Different audiences need different depth and emphasis from the same business case.

| Audience | What they need | What to emphasize | What to minimize |
|----------|---------------|-------------------|-----------------|
| **VP / Director** | Enough to decide whether to fund. | Problem, impact range (not details), cost summary, recommendation, timeline, biggest risks. | Detailed calculations, methodology deep-dives, technical implementation details. |
| **Board / C-suite** | Strategic alignment and financial material. | Market context, strategic rationale, financial model summary, competitive implications, ask (what you need from them). | Feature-level detail, engineering estimates, operational specifics. |
| **Team** | Enough to understand why this is being prioritized. | Problem context, what changes for them, timeline, how success is measured, what's not changing. | Financial projections, board-level strategic framing, organizational politics. |
| **Cross-functional** | How this affects their domain. | Dependencies, timeline, what they need to do, what changes in their area. | Financial details, strategic rationale beyond their scope. |

The business case output should be complete enough to serve any audience. The PM adapts the presentation of the material — the `presentation-deck` skill handles that translation.

---

## Red Flags

Business case smells that indicate more thinking is needed:

- **Impact sizing with no stated assumptions.** Every number is built on assumptions. If they're not stated, they can't be examined.
- **Single-number projections.** "$500K revenue impact" without a range signals either false precision or an unwillingness to acknowledge uncertainty.
- **Cost model that only includes build cost.** Opportunity cost, maintenance, infrastructure, and support are real costs that the business case must account for.
- **"Do nothing" not considered.** The implicit assumption that action is required may be wrong.
- **Problem statement that's actually a solution in disguise.** "We need to build a self-service portal" is a solution. "40% of support tickets are account changes that users can't make themselves" is a problem.
- **Risk assessment with no mitigation plans.** Listing risks without addressing them is acknowledging danger without preparing for it.
- **Recommendation presented as inevitable rather than chosen.** The recommendation should feel selected from genuine options, not preordained.
- **Strawman alternatives.** Options designed to fail so the preferred option looks good by comparison.
- **No acknowledgment of what's given up.** Every investment has an opportunity cost. If the business case doesn't name what else could be done with those resources, it's incomplete.

---

## Confidence Tiering for Complex Proposals

When a business case synthesizes multiple heterogeneous inputs — strategy documents, field research, stakeholder conversations, meeting notes, and technical assessments — different claims carry meaningfully different evidentiary bases. A single conviction score obscures this. Confidence tiering makes the evidentiary quality of each key claim explicit.

**When to use tiered confidence instead of a simple conviction score:**
- The proposal draws on 3 or more source types with meaningfully different reliability (a strategy doc, a customer interview, an engineering estimate, and a competitive analysis carry different weight)
- Different parts of the proposal have meaningfully different evidentiary quality — some claims are load-bearing facts, others are calibrated guesses
- The proposal includes architecture or technical decisions where specific unknowns are blockers

**When to use simple conviction (1-10):** The uncertainty is more uniform — all the key claims rest on comparable evidence, and a single score accurately reflects the aggregate confidence.

### Tiers

**High confidence** — Claims empirically backed by the organization's own data, confirmed across multiple independent sources, or grounded in a direct causal relationship. State what makes the claim load-bearing.

**Medium confidence** — Claims that are directionally correct but unvalidated in specifics. State what makes the direction credible and what needs to be confirmed.

**Lower confidence** — Genuine unknowns that could invalidate specific parts of the plan if the assumption is wrong. State what must be confirmed before the relevant section can be relied on.

### "What Would Change the Recommendation" Table

Follow the confidence tiers with a table mapping specific conditions to specific course corrections. This is more operationally useful than a list of things that might lower confidence — it tells the reader exactly what to watch for and what the response would be.

| Condition | Impact on recommendation |
|-----------|--------------------------|
| [Specific condition that would change the picture] | [Specific course correction — not just "revisit" but what specifically changes] |

One row per genuine pivot condition. If a condition would merely lower confidence without changing the recommendation, it belongs in the blindspot check, not this table.
