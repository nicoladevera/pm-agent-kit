# Ticket Quality Criteria

What makes a good user story or ticket. Use this to evaluate tickets — every criterion here is something a ticket should satisfy, and something a review should check.

Companion files: `references/acceptance-criteria.md` (AC standards in detail), `references/story-structure.md` (story scoping and structure).

---

## The Criteria

### 1. Scope Is Atomic

The ticket represents one deployable unit of work — something that can be built, tested, and shipped independently by one engineer within a sprint. See `references/story-structure.md` for right-sizing guidance and when-to-split rules.

**Evaluate:** Can one engineer own this end-to-end? If not, what's the split point?

### 2. Story Is Written From the User's Perspective

The ticket describes what the user can do and why it matters — not what the engineer should build. "Add server-side pagination to the admin user table" is a task. "As a workspace admin, I can load the user list in under 2 seconds so I can find and manage team members without waiting" is a story. A story framed around implementation is harder to scope, harder to evaluate, and more likely to miss the user need.

**Evaluate:** Is the user named? Is the user action described? Is the "why" tied to a user outcome, not a technical goal?

### 3. Acceptance Criteria Are Specific and Testable

Each AC describes exactly one verifiable behavior. See `references/acceptance-criteria.md` for the full standard — what good AC look like, Given/When/Then patterns, data contracts, boundary conditions, and error states.

**Evaluate:** Apply `references/acceptance-criteria.md` directly. The short checklist: no subjective language, no compound criteria, no business outcomes disguised as AC.

### 4. Definition of Done Is Explicit

"Done" means the same thing to the PM, the engineer, and QA. This includes: data events fired, error states handled, edge cases covered, design matched, and any documentation updated. If definition of done is implicit, it will be interpreted differently by everyone.

**Evaluate:** Is it clear what "shipped" means beyond the happy path? Are data events specified? Are error states included in the AC or explicitly excluded?

### 5. Implementation Ambiguity Is Surfaced

The ticket leaves nothing for the engineer to guess. Any decision that the PM has already made should be stated. Any decision intentionally left to the engineer should be acknowledged as such. Silent ambiguity — where the engineer has to decide something the PM didn't realize they left undecided — is the most expensive kind.

**Evaluate:** Read the ticket as if you were implementing it. What would you have to guess? Each guess is a gap.

### 6. Dependencies Are Named

Anything this ticket relies on — another team's API, a design file, a configuration service, a preceding ticket — is explicitly called out. See `references/story-structure.md` for dependency field conventions (what, owner, hard vs. soft block, API contract location).

**Evaluate:** Are dependencies surfaced as a dedicated field, not buried in the description or AC?

### 7. Edge Cases Are Addressed

The ticket accounts for at least the most likely failure modes: empty states, error states, invalid inputs, concurrent actions, and edge conditions specific to this feature's domain. Edge cases that aren't documented become engineer judgment calls — sometimes correctly, sometimes not.

**Evaluate:** What happens when the user is in an unexpected state? What happens when the system fails? Are these handled in the AC or explicitly deferred?

---

## Using These Criteria

**For review (`doc-review`):** Evaluate the ticket against each criterion. For each, determine: strong, needs work, or missing. Prioritize feedback by impact — vague AC is more fundamental than a missing dependency link.

**Rating scale:**
- **Strong** — The criterion is clearly satisfied. The story is specific, complete, and ready to implement.
- **Needs work** — The criterion is partially addressed but has gaps. The story needs clarification before an engineer should start.
- **Missing** — The criterion is not addressed at all. The story is not ready for implementation.
