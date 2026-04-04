# Evaluation Rubric — doc-review (Tech Spec)

**Target input:** `evals/doc-review/sample-tech-spec-01.md`
**Skill under test:** `.claude/skills/doc-review/SKILL.md`
**Purpose:** Determine whether `doc-review` correctly identifies the document as a tech spec, applies tech spec quality criteria from a PM perspective, catches planted weaknesses, and avoids false positives.

---

## PM Perspective Note

A doc-review on a tech spec is not an engineering code review. The skill evaluates the spec for decisions that create product risk, tradeoffs the PM should weigh in on, and gaps that will cause downstream problems. It does not evaluate implementation correctness — that's the engineering team's job.

---

## Planted Issues

The sample spec contains four deliberate weaknesses. The review should detect all of them.

| # | Issue | Must Catch? | What a good detection looks like |
|---|-------|-------------|----------------------------------|
| 1 | **No alternatives considered** — The spec presents a single approach (new endpoint + Redis caching) without acknowledging any alternatives. Options that were likely considered include: extending an existing loans endpoint, having the frontend calculate summary data from existing loan responses, or using a different caching strategy. The absence of alternatives makes the tradeoffs invisible. | Yes | Names the missing alternatives consideration and explains the PM risk: if the team hits a problem with this approach mid-sprint, there's no documented fallback. Should recommend documenting at least one alternative, even briefly. |
| 2 | **Failure modes not addressed for the primary dependency** — The spec relies on cache invalidation from the payment service to keep data fresh. If the payment service fails to publish the invalidation event, the widget will show stale loan data — potentially showing a balance that was already paid. This is a product risk (user confusion, trust issues) that the spec doesn't address. | Yes | Names the cache invalidation failure mode specifically. Should explain the user-facing impact (stale balance display) and note that a fallback (TTL-only expiry, or a staleness indicator) should be defined. Generic "failure modes not covered" is insufficient. |
| 3 | **No observability plan** — The spec defines the endpoint and the caching strategy but says nothing about logging, metrics, or alerting. There's no way to know after launch whether the endpoint is performing correctly, whether cache hit rates are healthy, or whether errors are occurring. | Yes | Identifies the complete absence of observability. Should name what's needed: at minimum, error rate and latency metrics on the endpoint, and cache hit/miss tracking. Should connect this to the PM's ability to validate that the widget is working after launch. |
| 4 | **Implicit dependency not named** — The spec says "Payment service to publish payment events for cache invalidation" but doesn't name a team owner, doesn't link to the payment service's event contract, and doesn't acknowledge the risk if the payment service doesn't currently publish this event. This is a cross-team dependency being treated as a given. | Yes | Names the payment service dependency as a gap in specificity. Should flag: is there a confirmed contract for this event? Who is the owner? What happens during the sprint if this event doesn't exist or doesn't behave as expected? |

---

## Intentional Strengths

The sample spec also contains sections that are deliberately well-done. The review should recognize these, not flag them as problems.

| Section | Why it's strong |
|---------|----------------|
| **Response schema** | Specific, typed JSON schema with field names and types. A frontend engineer could implement against this without a follow-up conversation. |
| **Open questions** | The two open questions are genuine unresolved decisions (loan-level detail, latency target) that require PM input, not cosmetic placeholders. These are appropriately surfaced. |

**False positive check:** If the review criticizes the response schema or the open questions section as weak, that's a false positive.

---

## Type Detection Check

The review must correctly identify this as a **tech spec**, not a ticket or PRD. Signals the skill should detect:
- System architecture description (endpoints, caching, Redis)
- JSON schema definition
- Database dependencies described
- Engineering-authored with implementation-level detail

**Fail:** If the skill identifies this as a ticket and applies ticket quality criteria (e.g., flags missing AC), that's a type detection error.

---

## Quality Checks

### PM Perspective
Does the review evaluate from a PM perspective — product risk, tradeoffs, downstream gaps — rather than as an engineering code review?

**Pass:** Feedback focuses on what the PM needs to understand and weigh in on. **Fail:** Review evaluates implementation correctness or makes engineering recommendations beyond PM scope.

### Actionability
For each issue flagged, does the review include what's wrong, why it matters from a product perspective, and what needs to happen?

**Pass:** Each issue connects to a product risk (stale data display, inability to validate launch health, sprint blocker risk). **Fail:** Issues flagged in engineering terms without PM relevance.

### Specificity
Does the review reference specific sections, field names, or architectural choices? Or offer generic tech spec advice?

**Pass:** Feedback points to the cache invalidation strategy, the payment service dependency, the specific missing log/metric types. **Fail:** Generic feedback applicable to any API spec.

---

## Overall Assessment

**Pass threshold:** Correctly identifies document type, catches all 4 planted issues, produces zero false positives on intentional strengths, evaluates from a PM perspective (not an engineering review), and every piece of feedback is actionable.
