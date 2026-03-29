# Prioritization Judgment

What makes a roadmap prioritization rigorous and defensible. Use this to compare candidate initiatives, sequence work, manage opportunity cost, and explain why A beats B. The portfolio counterpart to `business-case-standards.md` — that file argues for or against a single initiative; this file governs the comparative judgment across multiple initiatives competing for the same resources.

Prioritization is not scoring. A RICE spreadsheet doesn't prioritize — it creates an illusion of objectivity over fabricated inputs. Prioritization is judgment: given these candidates, these goals, and these constraints, this is the best sequence and here's why. The reasoning must be transparent enough that a reasonable person who disagrees can point to exactly where they disagree.

---

## Opportunity Cost as the Core Question

The question is never "is this valuable?" — everything on a roadmap has some value, or it wouldn't be there. The question is: **"Is this more valuable than everything else we could do instead, given our constraints?"**

Every slot on the roadmap has a cost: not the cost of building the thing in that slot, but the cost of *not building everything else*. A feature that's worth $500K in annual value is a bad investment if it displaces a feature worth $2M. The absolute value of an initiative is irrelevant without the relative comparison.

**In practice:**
- Every prioritization rationale must name what's *not* being done and why
- "This is important" is not a prioritization argument — "this is more important than these specific alternatives because..." is
- When a stakeholder asks "why aren't we building X?" the answer must reference what *is* being built instead and why it won

**Red flag:** A prioritization rationale where everything is P0. A roadmap that lists what's being built but never names what was cut. Arguments for an initiative that never compare it to the alternatives.

---

## Candidate Comparison Anatomy

For each candidate initiative in the comparison, establish a consistent profile so the comparison is apples-to-apples. Every initiative should be assessed on the same dimensions, even if the depth of available evidence varies.

| Dimension | What to capture | Why it matters |
|-----------|----------------|---------------|
| **Problem** | What problem does this solve? For whom? How severe? | The foundation. An initiative without a clear problem is a solution in search of justification. |
| **Evidence quality** | What data or research supports this? How strong is the evidence? | A well-evidenced initiative and a gut-feel initiative aren't comparable at face value. Name the evidence gap. |
| **Expected impact** | What happens if this succeeds? Revenue, users, retention, strategic positioning? | The numerator of the comparison. Present as ranges where possible. |
| **Estimated cost** | What does this require? Engineering, opportunity cost, ongoing maintenance? | The denominator. Including opportunity cost — what you can't build while building this. |
| **Dependencies** | What does this depend on? What does it unlock? | Dependency chains affect sequencing regardless of individual value. |
| **Reversibility** | Is this a one-way or two-way door? | Per `decision-frameworks.md` — one-way doors need higher confidence; two-way doors can be tried and adjusted. |
| **Time sensitivity** | Is there a closing window? A competitive threat? A regulatory deadline? | Time-sensitive items may need to be prioritized even if their absolute value is lower. |
| **Cost of waiting** | What happens if we do this next quarter instead of this quarter? | Some things are urgent (the window closes). Others are important but patient (the opportunity doesn't degrade). This distinction drives sequencing. |

### Evidence Quality Assessment

Not all supporting evidence is created equal. When comparing initiatives, explicitly grade the evidence behind each one:

| Evidence level | What it means | How to weight it |
|----------------|--------------|-----------------|
| **Validated** | Direct evidence from research, experiments, or production data | High confidence in the claims. Treat the impact estimate seriously. |
| **Inferred** | Extrapolated from adjacent data, comparable initiatives, or partial research | Moderate confidence. Discount the impact estimate and flag what would need to be validated. |
| **Assumed** | Team belief, stakeholder conviction, or "everyone knows" | Low confidence. The initiative may be right, but the evidence doesn't support the claims yet. Flag for discovery. |
| **None** | No evidence cited. The initiative exists because someone asked for it. | Cannot be compared on impact. Prioritize evidence-gathering before committing resources. |

**Red flag:** Treating all initiatives as equally well-evidenced when they're not. A business case backed by production data should outweigh an initiative backed by a stakeholder's conviction — unless the stakeholder's conviction is explicitly acknowledged as the basis and the team accepts that risk.

---

## Sequencing Heuristics

After comparison, sequencing determines what gets built first. Comparison answers "what's most valuable?" — sequencing answers "what order maximizes total value over time?"

### Dependencies

Map the dependency graph before sequencing:
- **Enabling dependencies:** A must be built before B is possible (platform capability before feature, API before integration)
- **Information dependencies:** Learning from A reduces uncertainty in B (discovery before investment, MVP before scale)
- **Resource dependencies:** The same team or infrastructure is required for both (can't parallelize)

Enabling and information dependencies often override raw priority. An initiative ranked #3 in value but required by #1 and #2 should be built first.

### Learning Value

Initiatives that reduce uncertainty for later decisions should be front-loaded, even if their standalone value is modest. A $50K discovery experiment that determines whether a $2M investment is sound has higher sequencing priority than its absolute value suggests.

Connect to `discovery-methods.md`: discovery plan outputs directly inform prioritization confidence. When evidence quality differs across candidates, sequencing research to fill evidence gaps before committing is often the highest-value move.

### Reversibility

Two-way doors before one-way doors, all else being equal. Try, learn, and adjust on reversible initiatives early — this builds organizational confidence and creates data for the less reversible decisions downstream.

### Time Sensitivity

Closing windows override other sequencing heuristics:
- Competitive: a competitor is about to ship something that changes the landscape
- Market: a seasonal or cyclical opportunity that won't recur
- Regulatory: a compliance deadline that imposes a hard constraint
- Internal: a planning cycle, reorg, or leadership change that shifts priorities

If the window is real and the cost of missing it is high, time sensitivity trumps learning value and reversibility. But verify the window is real — artificial urgency is the most common form of priority manipulation.

### Context-Switching Cost

Building three initiatives with one team sequentially is cheaper than building three initiatives with one team concurrently. Context-switching destroys velocity and quality. When sequencing:
- Prefer completing one initiative before starting the next
- Group related initiatives to minimize context switches
- Name the cost of interruptions and split attention explicitly

---

## Framework Traps

Scoring frameworks (RICE, WSJF, ICE, value/effort matrices) are useful for forcing structured comparison but dangerous when the score becomes the answer.

### When Frameworks Help

- **Forcing structured thinking.** Making teams state their assumptions about reach, impact, confidence, and effort is valuable even if the numbers are rough.
- **Creating a common vocabulary.** Frameworks give the team a shared language for discussing trade-offs.
- **Surface disagreements.** When two people score the same initiative differently, the interesting question is why — the disagreement is the value, not the score.

### When Frameworks Mislead

- **Fabricated precision.** A RICE score of 847 vs. 823 doesn't mean anything when the input numbers are guesses. False precision in, false precision out.
- **Hidden weighting assumptions.** Every framework embeds assumptions about what matters. RICE weights reach heavily — but reach isn't always the right priority. WSJF prioritizes cost of delay — but not every initiative has a meaningful delay cost.
- **Score-as-answer.** When the team says "we should build X because it has the highest RICE score," the framework has replaced judgment rather than informing it. The score is an input, not a conclusion.
- **Gaming.** People learn to score their preferred initiatives higher. Inflated reach estimates, deflated effort estimates, generous confidence ratings — all to get a higher number.

**Guidance:** Use frameworks as a structured discussion tool. Don't use them as an algorithm. If the framework's output disagrees with your judgment, investigate the disagreement rather than deferring to the number or ignoring the framework. The answer is in the gap between the score and the intuition.

---

## Explaining "Why A Beats B"

The prioritization rationale must be legible to stakeholders who care deeply about the initiative that *didn't* make the cut. This is the hardest communication problem in prioritization.

### Framing Patterns

**"Not now, not never":** The initiative has merit but not this quarter. Name when it would be reconsidered and what would need to change. This is honest and prevents the stakeholder from feeling dismissed.

**"Conditional yes":** The initiative is worth doing *if* a condition is met (evidence is gathered, a dependency is resolved, capacity frees up). Name the condition and the timeline for re-evaluation.

**"Different bet":** The initiative solves a real problem, but a different initiative solves a bigger problem with the same resources. Show the comparison directly — not as "yours is bad" but as "this one creates more value given what we know today."

**"Evidence gap":** The initiative might be the right call, but the evidence isn't there yet. Investing in discovery before committing resources is the responsible move. Connect to `discovery-plan` outputs.

### Stakeholder Disagreement

When stakeholders disagree on priorities:
- Name the disagreement explicitly rather than papering over it
- Identify what they're optimizing for — different priorities often reflect different objective functions, not different analyses
- Present the trade-off clearly: "If we optimize for [stakeholder A's priority], the sequence is X. If we optimize for [stakeholder B's priority], the sequence is Y. Here's what each costs."
- Escalate to the decision-maker with the trade-off framed, not with a recommendation that pretends the disagreement doesn't exist

---

## Constraint-Based Prioritization

Prioritization in theory: pick the highest-value items. Prioritization in practice: navigate fixed constraints.

### Common Constraints

| Constraint | How it affects prioritization |
|-----------|------------------------------|
| **Fixed capacity** | Can't do everything. The total set of initiatives must fit within the team's realistic capacity (after overhead, support, and maintenance). Overstuffing the roadmap guarantees nothing ships well. |
| **Competing roadmap owners** | Multiple PMs or teams lobbying for resources. Prioritization must account for whose perspective the roadmap serves and whose input was considered. |
| **Platform vs. product tension** | Infrastructure and platform work enables future features but doesn't deliver user value now. Tech debt compounds if ignored but is invisible to stakeholders. Allocate explicitly — don't let it compete with product features on the same scorecard. |
| **Tech debt allocation** | Reserve capacity for tech debt and maintenance explicitly. Making tech debt compete with features in a prioritization exercise guarantees tech debt always loses — until the system breaks. Treat it as a constraint, not a candidate. |
| **Stakeholder commitments** | Promises already made — to customers, partners, or leadership. These constrain the solution space regardless of what the analysis says is optimal. Name them explicitly and assess whether they're still valid. |

### Capacity Honesty

The plan must account for realistic capacity, not idealized capacity:
- Engineering teams are not 100% available for roadmap work — maintenance, support, on-call, and overhead consume 20-30% of capacity
- Multi-quarter initiatives have carrying costs: coordination, context maintenance, and cross-team dependencies
- The roadmap should state the capacity assumption explicitly so stakeholders understand what "full" means

---

## Red Flags

Prioritization anti-patterns that indicate more thinking is needed:

- **Prioritizing by loudest voice.** The initiative that gets the most airtime isn't necessarily the most important. If the prioritization rationale reads like "these are the things people keep asking for," it's captured demand, not assessed value.
- **HiPPO-driven roadmap.** The Highest Paid Person's Opinion determines the sequence. If a senior stakeholder's pet project is ranked #1 without evidence, name it — "this is prioritized because [person] directed it" is more honest than fabricating a rationale.
- **Everything is P0.** If everything is highest priority, nothing is. A prioritization that doesn't name what's NOT being done hasn't prioritized.
- **Score-driven prioritization without judgment.** The RICE spreadsheet determines the roadmap with no human override. Frameworks inform judgment — they don't replace it.
- **Missing "what we're NOT doing" section.** The most important part of a prioritization rationale is what was cut and why. Without it, the document doesn't demonstrate that trade-offs were considered.
- **No evidence quality assessment.** Treating a gut-feel initiative the same as one backed by production data and user research. Evidence quality should visibly influence the priority.
- **Sequencing by preference, not dependency.** Building the exciting initiative first when a less exciting enabling initiative is a prerequisite. Dependencies constrain sequence regardless of preference.
- **Ignoring opportunity cost.** Evaluating each initiative in isolation rather than against the alternatives. "This is valuable" is not a prioritization argument.
- **Artificial urgency.** Every initiative is urgent, every window is closing, every competitor is about to ship. Verify time sensitivity claims before letting them override other sequencing logic.

---

## Using These Standards

**For roadmap prioritization (`roadmap-prioritization` skill):** Catalog candidates with consistent profiles. Assess evidence quality per candidate. Compare on the same dimensions. Apply sequencing heuristics. Name what's not being done and why. Use frameworks as discussion tools, not algorithms. Stress-test the sequence.

**For business case evaluation:** When a business case from `business-case` is used as input to prioritization, its evidence quality and confidence level should carry forward. A high-conviction business case earns its initiative a higher priority than one with acknowledged gaps — but both should be in the comparison.

**For connecting discovery to prioritization:** When `discovery-plan` outputs are available, they directly inform the evidence quality assessment. An initiative with completed discovery has stronger evidence than one running on assumption alone. When evidence quality differs across candidates, "invest in discovery first" is a valid prioritization outcome for the weaker candidates.

**For communicating priorities:** The prioritization rationale is the basis for downstream communications — `presentation-deck` for roadmap reviews, `status-update` for progress against the plan, `meeting-brief` for planning meetings. The rationale must be clear and complete enough to support these downstream uses without re-deriving the logic.
