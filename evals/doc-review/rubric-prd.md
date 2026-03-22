# Evaluation Rubric — doc-review (PRD)

**Target input:** `evals/doc-review/sample-prd-01.md`
**Skill under test:** `skills/doc-review/SKILL.md`
**Purpose:** Determine whether `doc-review` catches what a strong PM would catch, avoids false positives, and produces actionable feedback.

---

## Planted Issues

The sample PRD contains five deliberate weaknesses. The review should detect all of them.

| # | Issue | Must Catch? | What a good detection looks like |
|---|-------|-------------|----------------------------------|
| 1 | **Vague success metrics** — "Reduce late payments" with no baseline, no target percentage, no timeframe. All four metrics are unmeasurable as written. | Yes | Names specific metrics and explains what's missing (baseline, target, timeframe, data source). Doesn't just say "metrics need work" — says *how*. |
| 2 | **Missing edge cases** — No coverage of: user has multiple active plans and receives overlapping reminders; reminder fires but payment was already made; user's device has notifications disabled; payment fails after reminder was sent. | Yes | Names at least two specific missing edge cases relevant to this feature. Generic "consider edge cases" is insufficient. |
| 3 | **Unbounded scope** — In-scope section includes "Future phases will include SMS reminders, email reminders, and AI-powered optimal send-time prediction." The Key Features section also mentions "Eventually, AI-powered smart scheduling." Future work is listed inside the v1 scope boundary. | Yes | Identifies that future-phase items are listed within the in-scope section, blurring the v1 boundary. Should recommend moving them to a separate "Future Considerations" section or removing them. |
| 4 | **Untestable AC** — AC #1 ("before their due date" — how far before?), AC #4 ("at the appropriate time" — undefined), AC #5 ("at a later time" — when exactly?), AC #9 ("appropriate reminders" — what makes them appropriate?). | Yes | Cites at least two specific AC by number and explains what's untestable about them. Should reference the subjective language ("appropriate," "later time"). |
| 5 | **No data plan** — The PRD defines success metrics but has zero instrumentation plan. No events, no tracking, no dashboard, no schema. There's no way to measure whether reminders actually reduce late payments. | Yes | Identifies the complete absence of data requirements. Should connect this to the success metrics — if you can't measure it, you can't evaluate the feature. |

---

## Intentional Strengths

The sample PRD also contains sections that are deliberately well-done. The review should recognize these, not flag them as problems.

| Section | Why it's strong |
|---------|----------------|
| **Problem statement** | Clear, names the affected user segment, cites evidence sources (support tickets, NPS), explains the impact (fees, support volume). |
| **Dependencies** | Named owners, specific people, status tracked. This is above-average for a draft PRD. |
| **Technical approach** | Reasonable architecture. Names specific systems (Kafka, FCM, PostgreSQL). Shows the PM understands how the system works. |

**False positive check:** If the review criticizes the problem statement, the dependencies section, or the technical approach as weak, that's a false positive and should be flagged as a calibration issue.

---

## Quality Checks

Beyond issue detection, evaluate the review output on these dimensions:

### Actionability
For each issue flagged, does the review include:
- What's wrong (specific, not vague)
- Why it matters (the risk or consequence)
- What a fix looks like (concrete suggestion, not "improve this section")

**Pass:** Every major issue includes all three. **Fail:** Issues are flagged without guidance on how to fix them.

### Prioritization
Are issues ordered by importance? The most fundamental issues (vague success metrics, no data plan) should appear before more specific ones (individual untestable AC).

**Pass:** Structural issues come first. **Fail:** Issues are listed in document order or alphabetically rather than by impact.

### Tone
Is the feedback direct and specific? Does it acknowledge strengths genuinely (not performatively)? Does it avoid corporate hedging ("could perhaps benefit from...")?

**Pass:** Reads like feedback from a strong PM peer. **Fail:** Reads like a generic document review checklist or uses soft language that obscures the actual assessment.

### Specificity
Does the review reference exact sections, quote specific language, and name concrete concerns? Or does it offer generic PRD advice that could apply to any document?

**Pass:** Every piece of feedback points to something specific in this PRD. **Fail:** Feedback is interchangeable with advice you'd give on any PRD.

---

## Overall Assessment

Answer this question: **Would a PM find this review useful without further conversation?**

- Could the PM take this review and improve the PRD based solely on what's written?
- Would the PM learn something they didn't already know about the document's weaknesses?
- Would the PM trust this reviewer's judgment on future documents?

**Pass threshold:** Catches all 5 planted issues, produces zero false positives on intentional strengths, and every piece of feedback is actionable.
