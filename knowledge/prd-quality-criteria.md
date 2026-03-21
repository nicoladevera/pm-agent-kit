# PRD Quality Criteria

What makes a good PRD. Use this to evaluate PRDs or to generate them — every criterion here is something a PRD should satisfy, and something a review should check.

---

## The Criteria

### 1. Problem Definition Is Clear and Bounded

The problem statement is specific, names who is affected, and does not smuggle a solution into the framing. "Users need a reminder system" is a solution disguised as a problem. "38% of users with active installment plans miss their first payment because they don't know when it's due" is a problem.

**Evaluate:** Can you restate the problem without referencing the proposed solution? If not, the problem isn't defined — the solution is.

### 2. Success Metrics Are Defined and Measurable

Metrics have targets, timeframes, and a named data source. Each metric should pass this test: two people reading it should agree, six months from now, on whether it was achieved.

**Evaluate:** Does each metric have a baseline, a target, and a timeframe? Is the data source identified? Could you build a dashboard from what's written here?

### 3. Scope Is Explicitly Bounded

What's in and what's out. The out-of-scope section is not optional — it's where discipline lives. If scope boundaries are missing, scope creep is already happening in the spec itself.

**Evaluate:** Is there a clear "out of scope" section? Does the in-scope section stay within its own boundaries, or does it bleed into "future phases" and "stretch goals"?

### 4. Edge Cases Are Addressed

The document anticipates what happens when things go wrong or when users are in unexpected states. Payment failures, empty states, concurrent actions, partial completions, timezone differences, multi-product interactions.

**Evaluate:** Does the document address at least the most likely failure modes? Are edge cases relevant to the specific domain covered (not just generic error handling)?

### 5. Acceptance Criteria Are Specific and Testable

Each AC describes one verifiable behavior. An engineer can implement and test against it without follow-up questions.

**Evaluate:** Apply the standards in `knowledge/acceptance-criteria.md`. Check for subjective language, compound criteria, and business outcomes disguised as AC.

### 6. Data Requirements Are Scoped

What events need tracking. What schemas change. What dashboards need building. What existing instrumentation is affected. Data requirements are product requirements — they belong in the PRD, not in a follow-up ticket created after the build starts.

**Evaluate:** Is there a data section? Does it name specific events, fields, and data flows? Is there a plan for how success metrics will actually be measured?

### 7. Dependencies Are Identified

Cross-team, cross-system, and external vendor dependencies are called out with owners. Each dependency should have: what the dependency is, who owns it, what the timeline risk is, and what happens if it's delayed.

**Evaluate:** Are dependencies listed? Does each have a named owner? Are timeline risks acknowledged?

### 8. Open Questions Are Surfaced

Things the PM hasn't resolved yet are stated explicitly, not buried or omitted. An honest "open questions" section is a sign of maturity, not weakness. Pretending everything is decided when it isn't creates false confidence.

**Evaluate:** Is there an open questions section? Are the questions genuine (things that actually need resolution) or cosmetic (things that are already decided but phrased as questions)?

---

## Using These Criteria

**For review (`doc-review`):** Evaluate the document against each criterion. For each, determine: strong, needs work, or missing. Prioritize feedback by impact — a weak problem statement is more fundamental than a missing edge case.

**For generation (future `prd-draft`):** Generate toward these criteria. A first draft should satisfy all eight, even if some sections are thinner than others. It's better to have a placeholder open questions section than to silently omit it.

**Rating scale:**
- **Strong** — The criterion is clearly satisfied. The section is specific, complete, and doesn't require follow-up.
- **Needs work** — The criterion is partially addressed but has gaps. The section exists but lacks specificity, measurability, or completeness.
- **Missing** — The criterion is not addressed at all. No section exists, or the existing content doesn't meet the minimum bar.
