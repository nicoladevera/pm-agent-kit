# Evaluation Rubric — doc-review (PRD: B2B SaaS Scheduling Feature)

**Target input:** `evals/doc-review/sample-prd-02.md`
**Skill under test:** `skills/doc-review/SKILL.md`
**Purpose:** Determine whether `doc-review` correctly identifies the 4 planted quality issues in this B2B SaaS PRD, avoids false positives on the intentional strengths, and produces actionable, criterion-referenced feedback.

**Coverage:** Single mode — doc-review on a PRD document type.

---

## Document Type Detection

The document is a PRD. Signals: Problem Statement section, Users section, Success Metrics, Scope, Functional Requirements, Dependencies, Open Questions — all hallmarks of a product requirements document.

**Pass:** Identified as PRD type. PRD-specific quality criteria applied (all 9 from `references/quality-criteria-prd.md` evaluated). **Fail:** Treated as a general document, a project brief, or any other type that would cause non-PRD criteria to be applied.

---

## Planted Issues (Must Catch)

The document contains 4 deliberate quality failures. The review must detect all of them.

| # | Issue | Criterion ID | What good detection looks like | What failure looks like |
|---|-------|-------------|-------------------------------|------------------------|
| 1 | **Vague success metric with no baseline, target, or timeframe** | PRD-2 (Success Metrics) | Flags specifically: "improve booking completion rate" has no current baseline number, no target, and no timeframe. Names what's missing: "current completion rate is X%, target is Y% by Z date, measured via [data source]." Severity: High. Explains consequence: without a measurable target, there is no way to evaluate whether the feature succeeded. | Review says "metrics could be improved" without naming what's specifically missing. Or accepts "reduce time to first available slot" as adequately defined without noting the absence of baseline and target. |
| 2 | **Scope boundary not stated — no out-of-scope section** | PRD-3 (Scope) | Flags the complete absence of an Out of Scope section. Names specific ambiguities created by the absence: Is Zoom scheduling integration in scope? Is Apple Calendar / iCloud integration supported? Is SMS confirmation in scope? Is the distribution logic available via API for headless integrations? Severity: High. Notes that the PRD mentions timezone detection and Google/Outlook calendar sync — which implies non-listed integrations might be in-scope expectations from readers. | Review mentions the scope section looks incomplete without naming specific technologies or integrations the PRD leaves ambiguous. |
| 3 | **Acceptance criteria written as prose, not Given/When/Then** | PRD-5 (Acceptance Criteria) | Flags that the "Behavior" section describes what the system does in paragraphs, not in testable AC format. Cites specific example: "When a user submits the booking form, the system will find the next available slot..." — asks: What is the Given? What are the boundary conditions? What does the system do if no slots are available in the requested window? What if two bookers submit simultaneously and the last slot is claimed? Severity: High. Recommends converting to Given/When/Then with explicit boundary conditions and error states. | Review notes "AC could be more structured" without naming specific scenarios missing or providing an example of what a testable version would look like. |
| 4 | **No data/analytics plan — events, dashboards, or tracking not mentioned** | PRD-6 (Data Requirements) | Flags the complete absence of a Data Requirements section. Notes that the PRD mentions an "admin dashboard showing distribution stats" but never defines what events produce those stats. Names what should be present: `booking_request_initiated`, `booking_slot_assigned` (with assigned_member_id, cycle_position), `booking_confirmed`, `booking_completion_abandoned`, `pool_member_skipped` (with skip_reason). Connects to success metrics: without instrumentation, "booking completion rate" cannot be measured. Severity: High. | Review omits the missing data plan entirely. Or mentions it briefly without connecting to the stated success metrics or naming specific events. |

---

## False Positives Check

The 2 intentional strengths must NOT be flagged as issues.

| Strength | Why it's strong | False positive to avoid |
|----------|----------------|------------------------|
| Clear problem framing | "Teams using shared calendars have no way to distribute inbound requests fairly — one person gets overbooked while others have open slots." Specific, operational, names the affected segment and the failure mode. | Review should not flag the problem statement as vague or insufficiently validated. It should not say "more user research needed" — the problem is clearly stated. |
| Well-defined user segments | "Team admins" and "external bookers" are explicitly differentiated with distinct workflows and success criteria. The Users section names what each group cares about. | Review should not flag "audience not defined" or "user segment unclear." The Users section is one of the PRD's stronger elements. |

**Pass:** Both strengths acknowledged explicitly in the "What's Strong" section. **Fail:** Either strength flagged as a gap, or neither mentioned as a positive — treating the review as all-negative without acknowledging what works.

---

## Feedback Quality

Each issue should be more than a label — it should explain why the gap matters and what a stronger version looks like.

**Pass:** Each of the 4 flagged issues includes:
1. What specifically is wrong (not "metrics need work" but "booking completion rate has no baseline, target, or timeframe")
2. The consequence of leaving it as-is (e.g., "without a measurable target, there is no way to evaluate the feature post-launch")
3. What a fix looks like (e.g., "Rewrite as: Booking completion rate improves from X% baseline to Y% within 90 days of launch, measured via booking_confirmed events in analytics")

**Fail:** Issues listed as brief bullet points without explanation of consequence or concrete fix examples.

---

## Prioritization

Issues should be ordered by impact, not by document order.

- The missing data plan and vague success metrics are structural failures that affect post-launch evaluation — they should appear before the AC format issue.
- The missing out-of-scope section creates scope ambiguity that affects engineering alignment — it should rank higher than individual AC formatting.

**Pass:** Structural issues (data plan, success metrics, scope boundary) appear before formatting-level issues (AC prose vs. Given/When/Then). **Fail:** Issues listed in the order they appear in the document (problem → metrics → scope → behavior → no data plan would be the wrong order).

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| Document type correctly identified as PRD | 10% | PRD-specific criteria applied; type stated at top of output |
| Vague success metric caught (no baseline, target, timeframe) | 10% | Specific language flagged; what's missing named; consequence explained |
| Missing out-of-scope section caught with named ambiguities | 10% | Specific technologies named (Zoom, Apple Calendar, or similar); severity High |
| Prose AC flagged with Given/When/Then conversion example | 10% | Specific behavior quoted; boundary condition gap named; example fix provided |
| Missing data plan caught with named events | 10% | At least 3 specific event names suggested; connection to success metrics made |
| No false positives on intentional strengths | 15% | Problem framing and user segments acknowledged as strong — not flagged as gaps |
| Feedback quality (problem + consequence + fix for each issue) | 25% | All 4 issues include what's wrong, why it matters, and what a stronger version looks like |
| Output format compliance | 10% | What's Strong / What Needs Work / Smell Test / Open Questions / Agent Block all present |
