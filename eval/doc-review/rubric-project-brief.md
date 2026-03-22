# Evaluation Rubric — doc-review (Project Brief)

**Target input:** `eval/doc-review/sample-project-brief-01.md`
**Skill under test:** `skills/doc-review/SKILL.md`
**Purpose:** Determine whether `doc-review` correctly identifies the document as a project brief, calibrates its evaluation to the brief's maturity level, catches planted weaknesses, and avoids false positives.

---

## Maturity Calibration

This brief is early-stage — loosely structured, still exploring directions, no owner named. The review should assess it at that level. It should not penalize the brief for lacking PRD-level structure, success metrics, or defined acceptance criteria. The question is: does the brief have the signal it needs to progress?

**Critical check:** The review must name the maturity level (early exploration / working brief / structured brief) before evaluating. If it skips this step and applies full PRD criteria, that's a calibration failure.

---

## Planted Issues

The sample brief contains four deliberate weaknesses. The review should detect all of them.

| # | Issue | Must Catch? | What a good detection looks like |
|---|-------|-------------|----------------------------------|
| 1 | **No scope signal** — The brief describes three separate directions (re-engagement email series, application abandonment push, loyalty program) but never indicates which one is the focus, whether all three are in scope, or what this initiative is actually trying to deliver. A reader can't estimate effort or sequence work from this. | Yes | Names the absence of scope signal specifically. Should point to the "What We're Thinking" section listing three directions without prioritization or scope boundary. Should recommend naming which direction is the starting point, or explicitly framing this as a discovery initiative. |
| 2 | **Key decisions buried, not surfaced** — The most consequential decision in this brief ("is this a marketing problem or a product problem?") is mentioned in passing at the end of a paragraph, not called out as an open question. Other key decisions — which direction to pursue first, who owns this — are similarly buried. | Yes | Names the "marketing vs. product problem" framing and flags that it's the most important unresolved question in the brief, not an aside. Should also flag the ownership question as a decision that needs to be made before work can start. |
| 3 | **No audience or purpose stated** — The brief doesn't say who it's for or what the reader is expected to do with it. Given that it names "Q2 planning lock" as a deadline, it's presumably meant to drive some kind of decision — but the brief doesn't say what decision or who needs to make it. | Yes | Identifies that the brief's purpose and audience are implicit. Should note that without knowing the intended action, it's hard to tell whether the brief has the right information at the right level of detail. |
| 4 | **Open questions list is incomplete** — The brief's open questions section names three things (retention analysis pending, unclear ownership, uncertain direction). But the bigger unresolved question — "is this a marketing or product problem" — is not in the open questions section. It's buried in the preceding paragraph, which means it's less likely to be acted on. | Yes | Notes that the most important open question isn't in the open questions section. Should recommend surfacing it explicitly. |

---

## Intentional Strengths

The sample brief also contains sections that are deliberately well-done. The review should recognize these, not flag them as problems.

| Section | Why it's strong |
|---------|----------------|
| **Problem framing** | The "Why We're Losing Borrowers" logic is clear — first loan repaid, no return, hypothesis about top-of-mind vs. competitor. The root cause hypothesis ("we're not building a relationship between transactions") is articulate for an early-stage brief. |
| **Why Now** | Specific: names the leadership priority, cites a concrete data point (12% year-over-year drop in second-loan conversion), and names the deadline (Q2 planning lock). This is useful context for a reader deciding how urgently to engage. |

**False positive check:** If the review criticizes the problem framing or the "Why Now" section as weak, that's a false positive.

---

## Type Detection Check

The review must correctly identify this as a **project brief**, not a PRD or ticket. Signals the skill should detect:
- Exploratory, loosely structured writing
- No success metrics, acceptance criteria, or formal sections
- "Early exploration" status marker
- Multiple directions under consideration, no single solution defined

**Fail:** If the skill identifies this as a PRD and flags missing success metrics as a gap that needs fixing before the brief is acceptable, that's a type detection error. At this maturity level, that's expected.

---

## Quality Checks

### Calibration
Does the review match the brief's maturity level? It should not hold a loose early-stage brief to structured-brief standards.

**Pass:** Feedback is framed around "what's needed to progress" rather than "what's missing for a complete document." **Fail:** Review penalizes the brief for lacking PRD-level sections.

### Actionability
For each issue flagged, is the feedback actionable given the brief's stage?

**Pass:** Suggestions tell the PM what to add, clarify, or decide — not how to turn this into a PRD. **Fail:** Suggestions require a level of detail the brief isn't ready for.

---

## Overall Assessment

**Pass threshold:** Correctly identifies document type and maturity level, catches all 4 planted issues, produces zero false positives on intentional strengths, and feedback is calibrated to early-stage exploration — not PRD-level rigor.
