# Story Structure Standards

What makes a good story or task — the container around the acceptance criteria. `acceptance-criteria.md` covers the AC inside stories; this file covers how to scope, structure, and organize the stories themselves.

**Primary implementers:** AI coding agents with human engineer oversight. Each story must contain enough context for an agent to start work without reading the full source document or asking follow-up questions.

---

## Story Title

- **Imperative form.** Start with a verb: "Display payment schedule on loan detail screen" not "Payment schedule display."
- **User-facing when possible.** Describe what the user experiences, not the technical implementation: "Send payment reminder 24 hours before due date" not "Implement reminder scheduling cron job."
- **Specific enough to distinguish.** A team looking at a board of 15 stories should be able to tell each one apart from the title alone. "Update payment flow" is too vague. "Cap overpayment at remaining balance with confirmation" is identifiable.

---

## Story Scoping

A story should be **one deployable unit of work** — something that can be built, tested, and shipped independently.

**Right-sized stories:**
- Can be completed within one sprint (or ideally a few days)
- Have a clear "done" state — you can tell whether it's finished without asking
- Touch one logical area of the system (one service, one screen, one flow)
- Can be demonstrated or verified independently

**Too large:**
- Spans multiple services with no natural break point
- Requires both frontend and backend work that can't be shipped separately
- Has more than 8-10 acceptance criteria (probably multiple stories merged)
- Takes more than one sprint — at that point it's an epic, not a story

**Too small:**
- Is a single acceptance criterion with no surrounding context
- Can't be meaningfully demonstrated ("add a database column" — for what?)
- Is a subtask of a story, not a story itself

---

## When to Split

Split a story when:

- **It touches multiple services or layers.** A backend API change and a frontend UI change that consumes it are two stories, linked by a dependency. An agent working on the frontend doesn't need to understand the backend implementation — it needs the API contract.
- **AC span different user flows.** If one story covers "create a plan" and "cancel a plan," those are different flows with different edge cases. Split them.
- **It includes both feature work and data/analytics work.** Instrumentation, event tracking, and dashboard creation should be their own stories (see Data Stories below).
- **It has a natural phased rollout.** If the feature ships to one market first, the market-specific configuration is a separate story from the core feature.
- **The AC list exceeds 8-10 items.** This usually means multiple stories are bundled. Look for natural groupings.

When you split, always flag the dependency between the resulting stories.

---

## Story Description

The description is **not a repeat of the AC.** It's the context an implementer needs — what this story does, why it exists, and where it fits.

**Include:**
- What the story accomplishes in 2-3 sentences
- Why it matters — the user problem or business need it addresses
- Where it fits — which part of the product, which user flow, what comes before and after
- Any technical context the implementer needs (which service, which API, which screen)

**Don't include:**
- The full problem statement (that's in the PRD)
- A restatement of the acceptance criteria
- Implementation instructions (that's the engineer's or agent's job)

**For agent implementers specifically:** Include enough context that the agent can make reasonable decisions about implementation approach without needing to read the full PRD. If the story depends on an API, name the endpoint. If it modifies a specific screen, name the screen. Agents work best with explicit pointers, not implied context.

---

## Dependencies

Flag dependencies explicitly. For each dependency:

- **What** depends on **what** — name both stories or both teams
- **Owner** — who is responsible for the blocking work
- **Type** — is this a hard block (can't start without it) or a soft dependency (can start but can't ship without it)?
- **API contracts** — if one story produces an API that another consumes, define the contract in the blocking story's AC so the dependent story can code against it

Don't bury dependencies in AC or descriptions. Surface them as a dedicated field so they're visible on a board.

---

## Data Stories

Analytics events, dashboards, instrumentation, and schema changes should be **their own stories**, not buried inside feature stories. This reflects the "Data Requirements Are Product Requirements" principle.

**Why separate data stories:**
- Different skills needed (analytics engineering vs. feature engineering)
- Different review requirements (data team needs to verify schemas, naming, and pipeline compatibility)
- Can often be built in parallel with the feature story
- If data work is buried in a feature story, it gets deprioritized or forgotten

**What a data story includes:**
- Event names and payloads (exact field names and types)
- Schema changes (new tables, new columns, migrations)
- Dashboard requirements (what questions the dashboard answers, what metrics it displays)
- Pipeline destination (where events route — analytics warehouse, real-time system, etc.)

**Dependency:** Feature stories and data stories should reference each other. The feature story fires the event; the data story ensures it arrives, is stored, and is queryable.

---

## Story Output Template

When generating stories, use this structure for each:

```markdown
#### [Story Title]

**Description:** [2-3 sentences — what, why, and where it fits]

**Acceptance Criteria:**
- **Given** [precondition], **When** [action], **Then** [expected result]
- **Given** [precondition], **When** [action], **Then** [expected result]

**Dependencies:** [Other stories, teams, or systems — or "None"]

**Notes:** [Splitting recommendations, risks, assumptions, or implementation hints]
```

---

## Anti-Patterns

- **The "mega-story"** — A story that's really an epic. If the title includes "and" connecting two distinct features, it should probably be split.
- **The "technical task" story** — A story framed as "refactor X" or "set up Y" without connecting it to user value. Even infrastructure work should explain what it enables.
- **The "AC-only" story** — A list of acceptance criteria with no description. The implementer (human or agent) has no context for why these behaviors matter or how they connect.
- **The "buried data" story** — A feature story that includes "and track the event" as a final AC. This gets skipped or implemented hastily. Make it its own story.
- **The "implied dependency" story** — A story that assumes another story is done but doesn't say so. Agents and humans alike will start work on it and get stuck.
