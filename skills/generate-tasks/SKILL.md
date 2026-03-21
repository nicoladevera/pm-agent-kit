---
skill: generate-tasks
type: Generator
tier: 1
approval: draft-confirm
context-required: []
context-optional:
  - company/facts/product.md
  - company/norms/process.md
degradation: proceed-with-caveat
---

# generate-tasks

Generate stories and tasks with acceptance criteria from any source artifact. The skill decomposes a product artifact into discrete, shippable units of work — each one specific enough that a coding agent with human oversight can pick it up and implement it without follow-up questions.

---

## What It Accepts

Any source artifact:
- A PRD (structured or rough)
- An engineering design document (EDD)
- Meeting notes
- A Slack thread
- Rough notes or bullet points
- A verbal description captured as text

The input does not need to be polished. The skill extracts the work to be done and structures it.

---

## Instructions

### 1. Read the source artifact fully

Understand the full scope before decomposing. Note: the problem being solved, the proposed solution, scope boundaries, edge cases, dependencies, and any data requirements. If these aren't explicit in the source, infer what you can and flag gaps.

### 2. Load knowledge files

Read these files — they define the standards for stories and AC:
- `knowledge/acceptance-criteria.md` — Every AC must meet these standards
- `knowledge/story-structure.md` — Story scoping, splitting, and structure standards

### 3. Load company context (if available)

If `company/facts/product.md` exists, read it for product context that affects how stories should be scoped (e.g., which services exist, what teams own what).

If `company/norms/process.md` exists, read it for how stories are typically structured at this company (sprint cadence, ticket conventions, definition of done).

If neither exists, proceed — note the absence in the output.

### 4. Decompose into stories

Break the source artifact into discrete, shippable units of work. Apply the scoping standards from `knowledge/story-structure.md`:

- Each story should be **one deployable unit** — buildable, testable, and shippable independently
- If a piece of work touches multiple services or layers (frontend + backend), split it into separate stories linked by dependencies
- If AC span different user flows, split into separate stories
- Keep stories right-sized: more than 8-10 AC usually means multiple stories are bundled

### 5. Write each story

For each story, produce:

**Title:** Imperative, user-facing when possible, specific enough to distinguish from other stories on a board.

**Description:** 2-3 sentences covering what this story does, why it exists, and where it fits in the product. Not a repeat of the AC — it's the context an implementer needs. For agent implementers, include explicit pointers: which service, which screen, which API.

**Acceptance Criteria:** Given/When/Then format meeting all standards in `knowledge/acceptance-criteria.md`:
- Specific enough for an agent to implement without questions
- Input/output explicit
- Boundary conditions declared
- Error states as separate AC
- Data tracking included where relevant

**Dependencies:** Other stories, teams, or external systems this story depends on. Flag whether it's a hard block or soft dependency.

**Notes:** Any splitting recommendations, risks, assumptions, or implementation hints.

### 6. Separate data stories

Analytics events, dashboards, instrumentation, and schema changes get their own stories. Don't bury "and track the event" as a final AC in a feature story.

For each data story:
- Name exact events and payloads (field names and types)
- Specify pipeline destination
- Reference the feature story it relates to
- Include dashboard or monitoring requirements if applicable

### 7. Flag cross-story dependencies

After all stories are written, review the full set and explicitly flag dependencies:
- Which stories must be completed before others can start
- Which stories can be worked in parallel
- Which stories share an API contract or data schema that needs to be defined first

### 8. Suggest implementation sequence

Order stories by suggested build sequence:
- Foundation stories first (shared API contracts, core data models)
- Feature stories next (can often be parallelized once foundations are in)
- Data stories alongside or after their feature counterparts
- Note which stories can be worked in parallel

### 9. Flag items needing PM input

If any stories have ambiguity that the PM should resolve before engineering picks them up, list them explicitly. Common reasons:
- Scope questions the source artifact didn't answer
- Edge cases where the right behavior isn't clear
- Dependencies with unknown owners or timelines
- Data requirements where the event schema needs PM/analytics alignment

---

## Output Format

```markdown
## Generated Tasks: [Source Document Title]

### Summary

[Total story count. Brief description of how the source was decomposed — what logical groupings emerged. Any major assumptions made during decomposition.]

---

### Stories

#### Story 1: [Title]

**Description:** [2-3 sentences — what, why, and where it fits]

**Acceptance Criteria:**
- **Given** [precondition], **When** [action], **Then** [expected result]
- **Given** [precondition], **When** [action], **Then** [expected result]

**Dependencies:** [Other stories, teams, or systems — or "None"]

**Notes:** [Splitting recommendations, risks, or assumptions]

---

#### Story 2: [Title]
[Same structure]

---

[Continue for each story]

---

### Data Stories

#### Data Story: [Title]

**Description:** [What's being instrumented and why]

**Events:**
| Event Name | Trigger | Payload |
|------------|---------|---------|
| [event_name] | [When it fires] | [field: type, ...] |

**Related Feature Story:** [Which story this supports]

**Notes:** [Pipeline destination, dashboard requirements, schema considerations]

---

### Implementation Sequence

[Ordered list with parallel tracks noted]

1. **First:** [Foundation stories — API contracts, core models]
2. **Then (parallel):** [Feature stories that can be built simultaneously]
3. **Alongside:** [Data stories paired with their feature counterparts]
4. **Last:** [Stories that depend on everything above]

### Flagged Items

- [Stories or decisions that need PM input before engineering starts]

> **Context note:** [Whether company context was loaded. What the decomposition might miss without it.]
```

---

## Quality Bar

The output should meet these tests:

- **Could an agent pick up any story and start work?** Each story has enough context, specific-enough AC, and clear-enough scope that implementation can begin without reading the full source document.
- **Do all AC meet acceptance-criteria.md standards?** Given/When/Then. Specific. Testable. Boundary conditions declared. Error states specified. No subjective language.
- **Are data stories separated?** Instrumentation, events, and dashboards are their own stories, not afterthoughts buried in feature stories.
- **Are dependencies visible?** Cross-story and cross-team dependencies are flagged, not implied.
- **Is the sizing right?** Stories are deployable units — not too large (multi-sprint epics) and not too small (single AC without context).
- **Does the implementation sequence make sense?** Foundation work comes first. Parallel tracks are identified. Nothing is scheduled before its dependencies.
