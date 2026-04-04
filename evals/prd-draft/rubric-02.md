# Evaluation Rubric — prd-draft (B2B SaaS)

**Target input:** `evals/prd-draft/sample-input-02.md`
**Skill under test:** `.claude/skills/prd-draft/SKILL.md`
**Purpose:** Determine whether `prd-draft` produces a complete, structured PRD that satisfies all 9 quality criteria, handles the rough input's planted gaps (missing metrics baseline, no data plan, implicit scope decisions), and preserves the input's genuine strengths without manufacturing problems.

**Coverage:** Single mode — full skill coverage.

---

## Quality Criteria Satisfaction

The output must satisfy all 9 criteria from `references/quality-criteria-prd.md`. Rate each:

| # | Criterion | What to check in the output |
|---|-----------|----------------------------|
| 1 | **Problem definition** | Did it translate the rough input into a clear, bounded problem statement? Does it name the user segment (enterprise support teams, 10-50 agents)? Does it surface the three core failure modes (collision, visibility, no audit trail)? Does it reference the 8-interview research signal? Does it avoid smuggling the solution into the problem? |
| 2 | **Success metrics** | Did it generate metrics with a flagged placeholder baseline for response time? Does it name the metric (avg. first response time, ticket resolution time, collision rate) and state the data source (support platform analytics / Zendesk)? Does it explicitly note that the current baseline is TBD — PM to confirm — rather than inventing a number? |
| 3 | **Scope** | Is there a clear in-scope / out-of-scope split? Did it respect stated constraints (mobile web yes, native mobile no, multi-tenant boundaries, tight scope)? Did it surface ticket reassignment and internal notes as either explicit scope decisions or open questions — not treat them as silently settled? |
| 4 | **Edge cases** | Did it generate edge cases relevant to this feature? (Two agents trying to claim the same ticket simultaneously; agent claims ticket then goes offline; ticket reassigned to agent who is at capacity; customer sends follow-up while ticket is claimed; internal note visible to wrong tenant.) |
| 5 | **Acceptance criteria** | Are AC in Given/When/Then format? Do they cover claim, unclaim, reassign, internal note, and close ticket scenarios? Are boundary conditions present (e.g., what if two agents click "claim" at the same time)? Are error states specified? |
| 6 | **Data requirements** | Did it generate a data requirements section with specific events even though the input never mentioned tracking? Are events named with payloads? Examples: `inbox_ticket_claimed`, `inbox_ticket_reassigned`, `inbox_internal_note_added`, `inbox_ticket_closed`, `inbox_collision_prevented`. Is there a measurement plan for success metrics? |
| 7 | **Dependencies** | Did it identify dependencies? (Customer messaging API, multi-tenant access control, mobile web compatibility, design resources for queue UI.) |
| 8 | **Open questions** | Did it preserve the PM's stated uncertainties (baseline response time, enterprise gate vs. all-customer rollout)? Did it surface the scope decisions on reassignment and internal notes as genuine open questions if not explicitly decided? |
| 9 | **Domain terms defined** | Are terms like "claimed," "unclaimed," "collision," "internal note" defined in a Definitions section so an engineer implements consistent semantics? |

**Pass:** All 9 criteria satisfied with real content (not placeholders). **Fail:** Any criterion missing entirely or filled with generic placeholder text.

---

## Input Fidelity

Did the output preserve the PM's intent while imposing structure?

- **Preserved:** The "Gmail inbox collision" framing, the 8-interview research signal, the multi-tenant constraint, the customer messaging API foundation, the tight scope constraint.
- **Didn't fabricate:** The output shouldn't invent features or constraints the PM didn't mention. The PM mentioned reassignment and internal notes as possibilities — if included in scope, they should be flagged as scope assumptions, not treated as unambiguous requirements.
- **Amplified strengths:** The 8-interview research backing should appear in the Problem section as evidence, not be relegated to a footnote or omitted.

**Pass:** The PM would recognize their thinking in the output. The specific pain ("customers get 3 different answers in one day") is preserved. **Fail:** The output is generic enough to have been written without reading the input — e.g., "Support agents struggle with communication" instead of the inbox collision framing.

---

## 4 Planted Gaps Addressed

| Gap | What good handling looks like | What failure looks like |
|-----|------------------------------|------------------------|
| **No metrics baseline** | PRD Success Metrics section names avg. first response time and collision rate as the primary metrics. Baseline field reads "TBD — PM to confirm current value from Zendesk" (or equivalent). Does NOT invent a number like "currently 4 hours." Data source named as support platform analytics. | PRD either invents a baseline number, leaves the baseline field empty, or omits the metric entirely. |
| **No data/analytics plan** | PRD includes a Data Requirements section with at minimum: `inbox_ticket_claimed`, `inbox_ticket_reassigned`, `inbox_internal_note_added`, `inbox_collision_prevented` (or equivalent naming). Payloads specified. Does not leave this out because the PM didn't mention it. | PRD omits a Data Requirements section. Or includes a section that says "TBD" without naming specific events. |
| **Implicit scope decisions not surfaced** | PRD either (a) lists ticket reassignment and internal notes as explicit in-scope items with a note that these were inferred assumptions, flagged for PM confirmation, OR (b) surfaces them in Open Questions as "Scope decision needed: are ticket reassignment and internal notes in v1?" Either treatment is acceptable — silently treating them as settled is not. | PRD lists reassignment and internal notes in scope without any flag that these were unstated scope choices, treating the PM's "we could" as a confirmed decision. |
| **AC written as prose** | PRD converts the "how it should work" paragraph into Given/When/Then AC with explicit boundary conditions and error states — e.g., "Given an unclaimed ticket in the inbox, When agent A clicks Claim, Then the ticket status changes to In Progress and is attributed to agent A in the assignment log, and the ticket is no longer visible in other agents' unclaimed queues." | PRD reproduces the PM's prose description ("agents can claim tickets") as AC without Given/When/Then structure or boundary conditions. |

---

## No False Positives on Strengths

The problem statement and user research context are strong and should not be flagged as gaps or weakened in the PRD output.

| Strength | What good handling looks like | False positive |
|----------|------------------------------|----------------|
| Clear problem statement: "Gmail inbox collision, visibility issues, no audit trail" | PRD uses this framing in the Problem Statement section — specific, operational, grounded. | PRD replaces it with generic "support agents have communication challenges." |
| 8-interview research backing | PRD cites the 8 enterprise support leads in the Problem section as evidence of validated pain. | PRD adds a "Problem Validation" section implying the research still needs to be done, or omits the research signal entirely. |
| Reasonable scope signal | PRD respects the PM's constraints (mobile web yes, native no, multi-tenant boundaries) without second-guessing them. | PRD flags the mobile web constraint as an open question when the PM was clear about it. |

**Pass:** All three strengths preserved and amplified. **Fail:** Any strength flagged as a gap or rewritten away from the PM's original framing.

---

## Assumption Handling

- Are assumptions listed explicitly in an Assumptions section?
- Is each assumption specific? ("Assumed ticket reassignment is in scope for v1 based on PM's description — flagged for confirmation" not "Made assumptions about scope.")
- Can the PM scan the assumptions and quickly confirm or correct each one?

**Pass:** At least 3 explicit assumptions listed and traceable to specific inferences. Baseline metrics TBD is surfaced as an action item, not buried. **Fail:** Assumptions omitted, or stated too generally to be correctable.

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| Input fidelity (problem statement, research preserved) | 15% | "Gmail inbox collision" framing and 8-interview backing appear in Problem Statement |
| Success metrics with placeholder baseline | 15% | Avg. first response time named as metric; baseline field reads "TBD — PM to confirm"; no invented number |
| Data requirements section with specific events | 20% | At least 4 named events with payloads; section present and substantive, not placeholder |
| Implicit scope decisions surfaced (reassignment, internal notes) | 15% | Both decisions flagged as assumptions or open questions — not silently settled |
| AC in Given/When/Then format with boundary conditions and error states | 20% | Claim, reassign, internal note, and close flows all have structured AC; simultaneous claim edge case covered |
| Assumptions explicit and flagged for PM confirmation | 10% | At least 3 specific, correctable assumptions listed |
| Output format compliance | 5% | All required PRD sections present; Agent Block populated; context note included |
