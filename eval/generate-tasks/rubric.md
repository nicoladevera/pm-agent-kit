# Evaluation Rubric — generate-tasks

**Target input:** `eval/generate-tasks/sample-input-01.md`
**Skill under test:** `skills/generate-tasks/SKILL.md`
**Purpose:** Determine whether generate-tasks decomposes a PRD into well-scoped stories with agent-implementable AC.

---

## Story Decomposition

The sample PRD describes an installment schedule visibility feature with several distinct components. The decomposition should identify natural story boundaries.

### Expected Stories (approximate)

The exact decomposition may vary, but it should roughly cover these areas:

| Area | What it covers | Should be separate? |
|------|---------------|-------------------|
| **Core schedule display** | The Payment Schedule section on loan detail screen — table/timeline of payments with status indicators | Yes — this is the foundation story |
| **Payment row detail expansion** | Tap a row to see payment details (amount, due date, method, transaction ID) | Could be separate or part of core — either is valid if well-scoped |
| **Overdue payment handling** | Red status, overdue badge, reordering overdue to top | Could be separate or part of core — depends on complexity |
| **Onboarding tooltip** | First-time tooltip display, dismiss, and persistence | Yes — distinct feature with its own AC and data events |
| **Error handling** | API failure state, error display, retry | Could be separate or part of core |
| **Localization** | Spanish translations for all UI text | Yes — different skill needed, different team owns it |
| **Data/analytics** | All 5 events, dashboard requirements | Yes — must be a separate data story per story-structure.md |
| **Plan Complete state** | Banner when all payments are "Paid" | Could be its own story or grouped with core |

**Pass:** Stories cover all functionality in the PRD with no gaps. Each story is a deployable unit. **Fail:** Major functionality is missing, or stories are so large they're just the PRD broken into sections.

### Decomposition Quality

- **No mega-stories** — If any story has more than 8-10 AC, it should be flagged for splitting
- **No micro-stories** — A story that's just a single AC with no context is too small
- **Natural boundaries** — Stories should split along logical lines (different UI components, different user flows, different teams), not arbitrary ones
- **Frontend/backend separation** — Since the backend API already exists, stories should be frontend-focused. If any backend work is identified, it should be a separate story

---

## Acceptance Criteria Quality

Apply `references/acceptance-criteria.md` standards to every AC in every story.

| Check | What to verify |
|-------|---------------|
| **Given/When/Then format** | Every AC uses the structured format |
| **Specificity** | No subjective language ("appropriate," "relevant," "seamless"). Exact behaviors named. |
| **Boundary conditions** | Maximum installments (12), overdue states, empty/complete states, error states |
| **Error handling** | Error scenarios have their own AC with specific messages and system behavior |
| **Data contracts** | Event names and payloads match what the PRD specifies. Any new events invented by the decomposition should be flagged as assumptions. |
| **Testable** | Each AC could be translated into an automated test by an agent |
| **Agent-implementable** | An agent reading any AC could start implementation without asking the PM questions |

**Pass:** All AC meet acceptance-criteria.md standards. **Fail:** AC contain vague language, compound behaviors, or missing boundary conditions.

---

## Data Stories

Per `references/story-structure.md`, analytics and instrumentation should be their own stories.

- **Separated?** Are data stories distinct from feature stories?
- **Complete?** Do data stories cover all 5 events from the PRD?
- **Specific?** Do data stories name exact event payloads with field names and types?
- **Dashboard included?** Is dashboard/monitoring work captured as a story?
- **Cross-referenced?** Do feature stories and data stories reference each other?

**Pass:** Data work is separated into its own story (or stories), with complete event specifications. **Fail:** Data tracking is buried as final AC in feature stories, or events are missing.

---

## Dependencies

- Are cross-story dependencies flagged explicitly?
- Are external dependencies (localization team, design, mobile team capacity) captured?
- Is the dependency type clear (hard block vs. soft dependency)?
- Are API contracts referenced (the existing `/api/v2/loans/{loan_id}/installments` endpoint)?

**Pass:** Dependencies are visible and actionable. **Fail:** Dependencies are implied but not stated, or external dependencies from the PRD are lost in the decomposition.

---

## Implementation Sequence

- Is there a suggested build order?
- Do foundation stories come first?
- Are parallel tracks identified?
- Does the sequence respect dependencies?

**Pass:** A team could follow the sequence and not get blocked. **Fail:** No sequence provided, or the sequence ignores dependencies.

---

## Flagged Items

- Did the skill identify any areas needing PM input before engineering starts?
- The PRD has 3 open questions — did the skill surface them as items to resolve, or did it make assumptions?
- If assumptions were made, are they flagged?

**Pass:** Open questions from the PRD are either preserved or resolved with flagged assumptions. **Fail:** Open questions disappear silently.

---

## Overall Assessment

**Could a coding agent pick up any story and start work?** Test by reading each story in isolation — does it have enough context, specific-enough AC, and clear-enough scope that an agent wouldn't need to read the full PRD?

**Is the decomposition complete?** Does the total set of stories cover everything in the PRD? If you implemented all the stories, would you have the full feature?

**Is the sizing right?** Stories should be completable in a few days, not multi-sprint efforts. Stories should be substantial enough to be meaningful, not just individual AC wrapped in a story format.

**Pass threshold:** All functionality covered. All AC meet acceptance-criteria.md standards. Data stories separated. Dependencies visible. Implementation sequence logical. No silent assumptions.
