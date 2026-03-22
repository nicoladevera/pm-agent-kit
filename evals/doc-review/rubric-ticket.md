# Evaluation Rubric — doc-review (Ticket)

**Target input:** `evals/doc-review/sample-ticket-01.md`
**Skill under test:** `skills/doc-review/SKILL.md`
**Purpose:** Determine whether `doc-review` correctly identifies the document as a ticket, applies ticket quality criteria, catches planted weaknesses, and avoids false positives.

---

## Planted Issues

The sample ticket contains four deliberate weaknesses. The review should detect all of them.

| # | Issue | Must Catch? | What a good detection looks like |
|---|-------|-------------|----------------------------------|
| 1 | **Vague acceptance criteria** — AC #3 ("looks visually consistent"), AC #5 ("loads quickly enough that users don't experience a noticeable delay"), AC #7 ("appropriate message") all use subjective language that can't be tested against. | Yes | Cites specific AC by number and names the subjective phrase. Should explain what a testable version looks like — e.g., AC #5 needs a specific latency threshold (under 500ms), not "quickly enough." |
| 2 | **No data events specified** — The definition of done and acceptance criteria say nothing about tracking. If this widget ships, there's no plan for measuring whether users engage with it or tap through to the Loans tab. | Yes | Identifies the complete absence of instrumentation. Should note that without tracking, the PM can't evaluate whether the widget delivers value or how to improve it. |
| 3 | **Scope spans two stories** — The ticket describes a single-loan widget AND a multi-loan summary view with expand behavior. These are two distinct deliverables with different complexity. The multi-loan case adds significant UI and data complexity that should be a separate ticket. | Yes | Names the split explicitly — single-loan display is one story; multi-loan aggregation and expand behavior is another. Should recommend splitting, not just flagging. |
| 4 | **Missing error states in AC** — AC #7 handles "loan data unavailable" but nothing else. Missing: what happens if the API times out, if the network request fails entirely, if the cache is stale, or if the user has loans in multiple states (some active, some closed). | Yes | Names at least two specific missing error states. "API timeout" and "partial data" are both plausible gaps given the caching architecture described in the background. |

---

## Intentional Strengths

The sample ticket also contains sections that are deliberately well-done. The review should recognize these, not flag them as problems.

| Section | Why it's strong |
|---------|----------------|
| **Story framing** | Written from the user's perspective with a clear "so that" — names the behavior and the benefit. Not an implementation task dressed as a story. |
| **Background** | Provides evidence (support ticket volume, navigation behavior), explains the feature, and notes the multi-loan case. More context than most tickets include. |
| **Tap-to-navigate AC** | AC #4 ("tapping the widget navigates the user to the Loans tab") is specific and testable as written. |

**False positive check:** If the review criticizes the story framing, the background section, or AC #4 as weak, that's a false positive.

---

## Type Detection Check

The review must correctly identify this as a **ticket**, not a PRD or project brief. Signals the skill should detect:
- "Story" header with user-facing framing
- "Acceptance Criteria" as the primary evaluation structure
- "Definition of Done" section
- No success metrics or problem statement at product level

**Fail:** If the skill identifies this as a PRD and applies PRD criteria (e.g., flags missing success metrics), that's a type detection error.

---

## Quality Checks

### Actionability
For each issue flagged, does the review include:
- What's wrong (specific, not vague)
- Why it matters (the risk or consequence)
- What a fix looks like (concrete suggestion)

**Pass:** Every major issue includes all three. **Fail:** Issues flagged without guidance on how to fix them.

### Prioritization
Scope spanning two stories should appear before minor AC wording issues — it's a more fundamental problem.

**Pass:** Structural issues (split, missing data tracking) come before wording-level issues. **Fail:** Issues listed in document order.

### Calibration
The review should apply ticket criteria, not PRD criteria. It should not penalize the ticket for lacking success metrics or a data section at the PRD level.

**Pass:** Feedback is grounded in ticket quality criteria. **Fail:** Review treats the ticket like an incomplete PRD.

---

## Overall Assessment

**Pass threshold:** Correctly identifies document type, catches all 4 planted issues, produces zero false positives on intentional strengths, and every piece of feedback is actionable.
