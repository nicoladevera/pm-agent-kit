# Evaluation Rubric — prd-draft

**Target input:** `evals/prd-draft/sample-input-01.md`
**Skill under test:** `.claude/skills/prd-draft/SKILL.md`
**Purpose:** Determine whether prd-draft produces a structured, substantive PRD from rough input — and whether the references layer works bidirectionally with doc-review.
**Coverage:** Single mode — full skill coverage.

---

## Quality Criteria Satisfaction

The output must satisfy all 8 criteria from `references/quality-criteria-prd.md`. Rate each:

| # | Criterion | What to check in the output |
|---|-----------|----------------------------|
| 1 | **Problem definition** | Did it translate the rough input into a clear, bounded problem statement? Does it name the user segment (150K installment users in Mexico)? Does it quantify impact (40% support ticket spike, missed first payments)? Does it avoid smuggling the solution into the problem? |
| 2 | **Success metrics** | Did it generate metrics even though the input said "I haven't thought about metrics yet"? Do metrics have baselines, targets, timeframes, and data sources? Are they specific enough to be measurable? |
| 3 | **Scope** | Is there a clear in-scope / out-of-scope split? Did it respect the stated constraints (no payment infrastructure changes, frontend/UX only, Mexico first)? Did it resolve the open question about separate screen vs. integrated view, or flag it appropriately? |
| 4 | **Edge cases** | Did it generate edge cases relevant to this specific feature? (Users with overdue payments, users with fully paid schedules, users switching between single-repayment and installment products, timezone edge cases for payment dates) |
| 5 | **Acceptance criteria** | Are AC in Given/When/Then format? Are they specific enough for an agent to implement? Do they include boundary conditions and error states? |
| 6 | **Data requirements** | Did it generate data requirements even though the input didn't mention them? Are events named with payloads? Is there a measurement plan for the success metrics? |
| 7 | **Dependencies** | Did it identify dependencies? (The existing API endpoint, the mobile team's capacity, localization for Spanish, potential design resources) |
| 8 | **Open questions** | Are open questions genuine? Does it preserve the PM's stated uncertainties (payment history vs. upcoming only, separate screen vs. integrated)? Did it surface new questions the PM didn't think of? |

**Pass:** All 8 criteria satisfied with real content (not placeholders). **Fail:** Any criterion missing entirely or filled with generic placeholder text.

---

## Input Fidelity

Did the output preserve the PM's intent while imposing structure?

- **Preserved:** The core problem (user confusion about installment schedules), the user segment (Mexico installment users), the constraints (no payment infra changes, Spanish, tight scope), the existing API reference
- **Didn't fabricate:** The output shouldn't invent features or constraints the PM didn't mention. Everything beyond the input should be in the Assumptions section.
- **Resolved vs. flagged:** For the PM's open questions (metrics, payment history vs. upcoming, separate screen), did the skill either make a reasonable recommendation with a flagged assumption, or preserve it as an open question? Either is valid — ignoring it silently is not.

**Pass:** The PM would recognize their thinking in the output. **Fail:** The output is generic enough to have been written without reading the input.

---

## Assumption Handling

- Are assumptions listed explicitly in an Assumptions section?
- Is each assumption specific? ("Assumed integrated view on existing loan detail screen based on constraint to keep scope tight" — not "Made assumptions about UI")
- Can the PM scan the assumptions and quickly confirm or correct each one?

**Pass:** All inferred content is traceable to a flagged assumption. **Fail:** The output presents inferences as facts.

---

## Bidirectionality Test

This is the key Phase 2 test. After generating the PRD:

1. Run `doc-review` on the prd-draft output
2. The review should be **meaningful** — not trivial ("everything is great") and not devastating ("everything is missing")
3. The review should identify areas where the draft is thin (likely: metrics based on inferred baselines, edge cases the input didn't mention) while recognizing areas that are strong (likely: problem statement, constraints, scope boundaries)
4. The quality criteria prd-draft generated toward are the same criteria doc-review evaluates against — they should speak the same language

**Pass:** doc-review produces 2-3 actionable suggestions that would genuinely improve the draft. **Fail:** doc-review either can't find anything to improve (output too perfect — unlikely) or finds everything broken (output too thin — format problem).

---

## Overall Assessment

**Would this draft save the PM time?** The PM gave a 5-minute verbal dump. Did the output turn it into something she can edit and sharpen — or did it produce something she'd throw away and start over?

**Is it a real draft, not a template?** Does the content reference the specific problem (installment schedule visibility in Mexico), the specific numbers (150K users, 40% support spike), and the specific constraints (existing API, Spanish, tight mobile team)?

**Pass threshold:** All 8 quality criteria satisfied with real content. Assumptions flagged. Open questions preserved or resolved with flagged assumptions. The bidirectionality test produces a meaningful doc-review.
