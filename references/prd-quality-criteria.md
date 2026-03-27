# PRD Quality Criteria

What makes a good PRD. Use this to evaluate PRDs or to generate them — every criterion here is something a PRD should satisfy, and something a review should check.

---

## The Criteria

### 1. Problem Definition Is Clear and Bounded

The problem statement is specific, names who is affected, and does not smuggle a solution into the framing. "Users need a reminder system" is a solution disguised as a problem. "38% of users with active installment plans miss their first payment because they don't know when it's due" is a problem.

**Evaluate:** Can you restate the problem without referencing the proposed solution? If not, the problem isn't defined — the solution is.

### 2. Success Metrics Are Defined and Measurable

Metrics are organized in three tiers:

- **Success Metrics** — the primary outcomes this product is expected to move. Each has a priority (P0/P1/P2), baseline, target, and timeframe.
- **KPI Definitions** — for each success metric, how it is actually calculated: numerator, denominator, required segmentation. Without this, the metric exists on paper but can't be instrumented.
- **Product Health Metrics** — signals that the product is functioning as expected (error rates, latency, failure counts). Distinct from business outcomes; these tell you if the product is working, not whether it's working well.

**Evaluate:** Does each Success Metric have a baseline, target, and timeframe? Does each KPI Definition specify how the metric is calculated and what data is needed? Are Product Health Metrics present for the riskiest parts of the feature?

### 3. Scope Is Explicitly Bounded

What's in and what's out. The out-of-scope section is not optional — it's where discipline lives. If scope boundaries are missing, scope creep is already happening in the spec itself.

**Evaluate:** Is there a clear "out of scope" section? Does the in-scope section stay within its own boundaries, or does it bleed into "future phases" and "stretch goals"?

### 4. Product Experience Is Fully Specified

The document specifies what happens in every meaningful state — not just failure modes, but the complete behavioral model: happy path, sad path, error handling, and edge cases. Both paths are documented explicitly so that engineers and agents know the primary flow and the failure recovery paths without inferring either.

**Happy path:** The core flow works as designed. Each state, action, and transition is described.
**Sad path:** Failure modes, error states, partial completions, and system failures are documented with expected behavior for each.

**Evaluate:** Is the happy path described in enough detail to build from? Are failure modes and error states covered — not just "system handles errors gracefully" but specific behaviors per failure scenario? Are both paths labeled and separated so readers can navigate them?

### 5. Acceptance Criteria Are Specific and Testable

Each AC describes one verifiable behavior. An engineer can implement and test against it without follow-up questions.

**Evaluate:** Apply the standards in `references/acceptance-criteria.md`. Check for subjective language, compound criteria, and business outcomes disguised as AC.

### 6. Data Requirements Are Scoped

What events need tracking. What schemas change. What dashboards need building. What existing instrumentation is affected. Data requirements are product requirements — they belong in the PRD, not in a follow-up ticket created after the build starts.

**Evaluate:** Is there a data section? Does it name specific events, fields, and data flows? Is there a plan for how success metrics will actually be measured?

### 7. Dependencies Are Identified

Cross-team, cross-system, and external vendor dependencies are called out with owners. Each dependency should have: what the dependency is, who owns it, what the timeline risk is, and what happens if it's delayed.

**Evaluate:** Are dependencies listed? Does each have a named owner? Are timeline risks acknowledged?

### 8. Open Questions Are Surfaced

Things the PM hasn't resolved yet are stated explicitly, not buried or omitted. An honest "open questions" section is a sign of maturity, not weakness. Pretending everything is decided when it isn't creates false confidence.

**Evaluate:** Is there an open questions section? Are the questions genuine (things that actually need resolution) or cosmetic (things that are already decided but phrased as questions)?

### 9. Domain Terms Are Defined

Any term with a product-specific or technically precise meaning is defined before first use. This applies especially to financial products, platform products, and any domain where common words carry specific technical meaning (e.g., "balance," "payment," "status").

A missing or inconsistent definition is a silent source of implementation errors — agents and engineers will interpret undefined terms according to general knowledge, which may not match the product intent.

**Evaluate:** Are domain-specific terms defined in a Definitions section? Are terms used consistently throughout the document? Would a new engineer or an agent reading this document reach the same understanding of key terms as someone who wrote it?

---

## Using These Criteria

**For review (`doc-review`):** Evaluate the document against each criterion. For each, determine: strong, needs work, or missing. Prioritize feedback by impact — a weak problem statement is more fundamental than a missing edge case.

**For generation (`prd-draft`):** Generate toward these criteria. A first draft should satisfy all nine, even if some sections are thinner than others. It's better to have a placeholder open questions section than to silently omit it.

**Rating scale:**
- **Strong** — The criterion is clearly satisfied. The section is specific, complete, and doesn't require follow-up.
- **Needs work** — The criterion is partially addressed but has gaps. The section exists but lacks specificity, measurability, or completeness.
- **Missing** — The criterion is not addressed at all. No section exists, or the existing content doesn't meet the minimum bar.
