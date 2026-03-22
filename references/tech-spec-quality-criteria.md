# Tech Spec Quality Criteria

What makes a good technical spec or engineering design document (EDD). Use this to evaluate tech specs — every criterion here is something a spec should satisfy, and something a review should check.

A tech spec is evaluated from a PM perspective: does it surface the decisions that matter, make tradeoffs legible, and give the PM enough signal to understand risk and sequence? Deep implementation correctness is the engineer's domain — the PM's job is to catch the gaps that create downstream product risk.

---

## The Criteria

### 1. Problem Is Stated Before Solution

The spec explains what and why before how. A spec that opens with an architecture diagram or a list of API endpoints before establishing the problem has buried its assumptions. The reader can't evaluate whether the solution is appropriate if the problem isn't stated.

**Evaluate:** Is there a problem statement or context section before the proposed solution? Does it explain what the feature needs to do and why this approach is being taken? Can you understand what's being built without reading the implementation details?

### 2. Alternatives Were Considered

At least two approaches are described, with tradeoffs stated. "We chose X" is less useful than "We considered X and Y. We chose X because of Z, accepting the tradeoff of W." Specs that present a single path as the obvious answer have likely not examined the decision — or have and are hiding the consideration.

**Evaluate:** Are at least two approaches named? Are the tradeoffs between them articulated? Is the selected approach's tradeoffs acknowledged, not just its benefits?

### 3. Failure Modes Are Addressed

What happens when each significant component fails. The happy path is not enough. For each major integration point, dependency, or external call: what is the expected behavior when it fails? Degraded states, retry behavior, user-visible impact, and fallback handling should be addressed.

**Evaluate:** What are the 2-3 highest-risk integration points in this spec? Are failure modes described for each? Does the spec describe what the user experiences on failure, not just what the system does?

### 4. Data Contracts Are Specified

API schemas, database models, event names and types, and data flows are defined with enough specificity that another engineer could implement against them without follow-up conversations. Vague references to "the API" or "the database" are not specs — they're placeholders.

**Evaluate:** Are API request/response schemas defined? Are database model changes described (fields, types, indexes)? Are data events named and their properties listed? Would a frontend engineer be able to integrate with this from the spec alone?

### 5. Observability Is Planned

Logging, metrics, and alerting tied to the feature are called out. A feature that ships without a monitoring plan will be investigated blind when something goes wrong. Observability is a product requirement, not an afterthought.

**Evaluate:** What will be logged? What metrics will be tracked? Are there SLOs or alerting thresholds defined? Is there a plan for knowing if the feature is working after it ships?

### 6. Scope Is Bounded

What this spec does and does not cover is explicit. A spec with unbounded scope creates unbounded implementation — engineers will make their own scope decisions when they encounter the edges. Out-of-scope items should be named, not silently absent.

**Evaluate:** Is there an explicit scope section? Are out-of-scope items named? Does the spec stay within its own scope, or does it reference "future work" without defining where this spec ends?

### 7. Dependencies Are Explicit

Upstream services, downstream consumers, external APIs, and migration requirements are named with their owners. A dependency that isn't named can't be sequenced, tracked, or escalated when it blocks.

**Evaluate:** Are all service dependencies listed? Does each have an owner or a link to the relevant team? Are migration requirements (data migrations, API version changes, deprecations) called out?

### 8. Open Questions Are Surfaced

Unresolved technical decisions are flagged, not buried. An honest open questions section — "We haven't decided how to handle X" — is safer than a spec that silently makes a consequential assumption. Open questions at spec time are cheap. The same questions surfaced mid-implementation are expensive.

**Evaluate:** Are there genuine open questions named? Are they things that actually need resolution before or during implementation, not cosmetic? Is there a path to resolving each one?

---

## Using These Criteria

**For review (`doc-review`):** Evaluate from a PM perspective — surface decisions that create product risk, tradeoffs the PM should weigh in on, and gaps that will cause problems downstream. Don't evaluate implementation correctness — that's the engineering team's job.

**Rating scale:**
- **Strong** — The criterion is clearly satisfied. The section is specific, complete, and would not require follow-up.
- **Needs work** — The criterion is partially addressed but has gaps the PM or engineering team should resolve before implementation starts.
- **Missing** — The criterion is not addressed. This is a gap that creates downstream risk.
