# Evaluation Rubric — roadmap-prioritization (Platform vs. Growth)

**Target input:** `evals/roadmap-prioritization/sample-input-02.md`
**Skill under test:** `.claude/skills/roadmap-prioritization/SKILL.md`
**Purpose:** Determine whether `roadmap-prioritization` handles a two-candidate, high-stakes, politically charged prioritization with genuine trade-offs, a technical dependency between the options, and conflicting stakeholder preferences — producing a defensible recommendation rather than a compromise that satisfies nobody.
**Coverage:** Single mode — full skill coverage. Tests the skill's ability to handle thin candidate lists with deep trade-offs rather than broad candidate lists with surface comparison.

---

## Problem Framing

The input presents this as a binary choice: multi-tenant migration (CTO) vs. enterprise analytics (Head of Sales). The skill should explore whether the choice is truly binary.

### Critical tests:

**The skill must explore a third option.** The input presents two options, but the skill should consider at least one alternative framing: a hybrid approach (partial migration + stripped-down analytics), a sequenced approach (analytics workaround now, migration next quarter with the 4 new hires), or a phased migration that preserves some feature velocity. The most interesting question is whether the technical dependency (analytics needs cross-tenant data, which requires multi-tenant) makes Option B a dead end or a viable interim step.

**The "good enough" workaround debate must be directly addressed.** The CTO says the anonymized sample data approach is a dead end. Sales says it's good enough. The skill must assess this technical judgment, not just note the disagreement.

**Pass:** Third option explored. The CTO's "dead end" claim evaluated against evidence. The framing moves beyond binary to structured comparison of 3+ approaches (including hybrid/sequenced). **Fail:** Accepts the binary framing without question. Doesn't evaluate the workaround viability. Only two options compared.

---

## Evidence Quality Assessment

Both options have evidence, but of very different types and strengths.

### Option A (Multi-Tenant):
- **Validated:** Infrastructure costs ($48K/month), deployment time (3 days), on-call burden (40%), incremental cost per customer ($270/month). This is operational data, directly measurable.
- **Inferred:** "It only gets harder" — the CTO's projection about 300 and 500 customers is plausible but unvalidated. The growth rate is 40% YoY, so reaching 300 customers is ~18 months away, not imminent.
- **Assumed:** That the migration takes 2 quarters. Large migrations are notoriously underestimated.

### Option B (Analytics):
- **Inferred:** 6 qualified prospects totaling $1.2M ACV from Sales pipeline. Pipeline data is not closed revenue — "I can close at least 4 of the 6" is a sales forecast, not a fact.
- **Validated:** 3 named lost deals citing analytics gaps (from CRM). Competitor launched benchmarking last quarter.
- **Assumed:** That shipping by end of Q3 is sufficient to close the deals. The sales cycle may not wait even that long.

### Critical tests:

**The skill must distinguish operational data (Option A) from sales forecasts (Option B).** Infrastructure costs are measurable. Pipeline predictions are not. Treating "$1.2M in pipeline" the same as "$48K/month in infrastructure costs" is a category error.

**The CTO's migration estimate should be flagged as a risk.** Two quarters for a multi-tenant migration with 180 customers is optimistic. The skill should note that large migrations frequently exceed estimates.

**The sales forecast confidence should be probed.** "I can close at least 4 of the 6" — what's the basis? Win rate? Stage of pipeline? Verbal commitments? The skill should note this is a forecast, not a guarantee.

**Pass:** Evidence types distinguished (operational data vs. sales forecast). Migration estimate flagged as risky. Sales forecast treated as a forecast, not a fact. Both options' evidence honestly assessed. **Fail:** Both options' evidence treated as equally reliable. Migration timeline accepted without risk assessment. Sales forecast taken at face value.

---

## Handling the Technical Dependency

The most interesting complexity in this input: the analytics suite needs cross-tenant data for benchmarking, which is what the multi-tenant migration delivers. But Sales says a workaround exists (anonymized sample data). The CTO says the workaround is a dead end.

### Expected analysis:

The skill should evaluate the workaround on its merits:
- **What does "good enough" actually mean?** Can anonymized sample data deliver benchmarking that enterprise buyers would find compelling? Or is it materially different from real cross-tenant analytics?
- **What's the rebuild cost?** If the workaround ships and the migration happens later, what's the cost of rebuilding the analytics on the new architecture? Is it 2 weeks of refactoring or 2 months of rearchitecture?
- **Is the CTO's "dead end" claim about technical reality or architectural principle?** There's a difference between "this literally can't scale" and "this isn't how I'd build it."

### Critical tests:

**The skill must take a position on the workaround viability.** Not "the CTO and Sales disagree" — the skill should assess the technical claim and state whether the workaround is viable as an interim step or genuinely a dead end.

**The dependency should influence sequencing.** If the workaround is viable, "analytics first with workaround, then migrate" is a defensible sequence. If the workaround is a dead end, "migrate first, then analytics" is the only responsible path (at the cost of the pipeline).

**Pass:** Workaround viability directly assessed. Position taken on whether it's viable-interim or dead-end. Dependency explicitly influences the recommended sequence. **Fail:** Workaround debate noted but not resolved. Skill defers to "the team should decide." Dependency mentioned but doesn't affect the recommendation.

---

## Recommendation Defensibility

The PM explicitly says: "I need a clear-headed recommendation that I can defend in a room where the CTO and Head of Sales are both going to push back." The recommendation must be defensible under pressure.

### Critical tests:

**The recommendation must name what the opposing side loses.** If the recommendation favors migration, it must name the pipeline risk ($1.2M in potential deals). If it favors analytics, it must name the growing infrastructure cost and the CTO's warning about increasing migration difficulty.

**The recommendation should address the board's concern.** "Path to $50M ARR" at 40% YoY growth — that's about $29M next year. The gap between $29M (organic) and $50M requires acceleration. The skill should assess which option better serves the board's growth expectation.

**The recommendation should have a clear "what we're not doing and what it costs" section.** The losing option's stakeholder will push back. The rationale must preemptively address their strongest argument.

**Pass:** Recommendation stated directly. Both sides' losses named. Board growth target addressed. "What we're not doing" anticipates the pushback. Confidence level calibrated to the genuine uncertainty. **Fail:** Recommendation hedged ("it depends on..."). One side's losses not named. Board priority ignored. No anticipation of pushback.

---

## Stress Test Specificity

The stress test must surface failure modes specific to the recommended path.

### Expected premortem failure modes (if migration recommended):

- The 6 enterprise prospects close with a competitor during the migration period, and enterprise pipeline takes 12+ months to rebuild
- The migration takes 3 quarters instead of 2 (underestimate), meaning feature velocity is reduced for 9 months, not 6
- The 4 new hires join but are consumed by migration ramp-up, so the expected post-migration acceleration doesn't materialize

### Expected premortem failure modes (if analytics recommended):

- The workaround ships but enterprise buyers see through the anonymized sample data — it's not benchmarking, it's a demo
- Infrastructure costs continue growing and at 250 customers the system stability degrades, causing retention problems that dwarf the enterprise revenue gained
- The CTO loses faith and leaves — organizational risk from ignoring the technical recommendation

### Expected blindspots:

- **The 40% growth rate assumption:** The board wants $50M in 18 months. Is the real question "which option gets us to $50M faster?" not "which option is the better product investment?" If so, the analysis frame is wrong.
- **The people risk:** The CTO and Head of Sales "aren't even in the same meeting anymore." The organizational damage from this conflict may be more important than the technical trade-off. The recommendation should acknowledge this.

**Pass:** Premortem has 3+ failure modes specific to the recommended path. Blindspot catches the growth frame question or the organizational risk. Conviction is 5-7 (this is a genuine judgment call under uncertainty). **Fail:** Stress test is generic. Blindspot misses the organizational dynamic. Conviction is 8+ (inappropriate confidence for a genuinely close call).

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| Problem framing | 10% | Third option explored; binary framing questioned; workaround viability addressed |
| Evidence quality assessment | 15% | Operational data vs. sales forecasts distinguished; migration timeline flagged; sales forecast probed |
| Technical dependency handling | 20% | Workaround viability assessed; position taken; dependency influences sequencing |
| Recommendation defensibility | 20% | Direct recommendation; both sides' losses named; board growth target addressed; pushback anticipated |
| Stress test specificity | 15% | Path-specific failure modes; organizational risk or growth frame blindspot; conviction 5-7 |
| "What we're not doing" quality | 10% | Losing option's strongest argument preemptively addressed; reconsideration conditions named |
| Output format compliance | 10% | Matches format; context note present; smell test completed; Agent Block populated |
