# Evaluation Rubric — sprint-plan (Analyze Mode)

**Target input:** `evals/sprint-plan/sample-input-02.md`
**Skill under test:** `skills/sprint-plan/SKILL.md`
**Purpose:** Determine whether `sprint-plan` Analyze mode correctly identifies all backlog health issues, outputs a backlog health report (not a sprint plan), and provides actionable remediation steps for each issue found.

## Coverage

**This rubric tests:** Analyze mode — backlog health assessment, no sprint plan produced.
**Not covered here:** Draft mode (full sprint plan with goals, capacity math, story selection) — see `rubric.md`.

---

## Mode Detection

The PM asks to "check if our backlog is ready" the night before sprint planning. She is explicitly NOT asking for a sprint plan — she says "I'm not asking for a sprint plan yet." This should trigger **Analyze mode**.

**Pass:** Produces a backlog health report with a summary, a list of ready stories, a list of issues with remediation steps, and an Agent Block. Does NOT produce a sprint plan with sprint goals, story selection, or capacity math. **Fail:** Produces a full sprint plan with sprint goals and committed stories, or silently upgrades to Draft mode.

---

## Backlog Issues Caught

Five issues are planted in the backlog. The rubric tests whether the skill catches all five.

| Issue | Must Catch? | What good detection looks like |
|-------|-------------|-------------------------------|
| **PR-108 too large (13 AC)** | Yes | Flagged as a split candidate. Analysis names the specific problem (13 AC, spanning multiple distinct concerns — rendering, navigation, performance, edge cases). Suggests a concrete split along natural seams — e.g., "PR-108a: Core diff rendering and syntax highlighting" / "PR-108b: Navigation, keyboard shortcuts, and hunk traversal" / "PR-108c: Edge cases (binary files, large diffs, mobile)" — or equivalent split logic. Does not simply say "this story is too big." |
| **PR-112 no AC** | Yes | Flagged as not sprint-ready. States specifically what's missing: written acceptance criteria in a verifiable format (Given/When/Then or equivalent). Names the action required and the owner: "PM (Reza) needs to write AC before this can be planned." The fact that the idea is clear in the PM's head does not satisfy the AC requirement. |
| **PR-115 no AC ("Dev knows what to do")** | Yes | Flagged as not sprint-ready. The note "Dev knows what to do" and "he's got it in his head" should not satisfy the AC requirement. Analysis should name the risk explicitly: unwritten AC means no shared definition of done, no QA test basis, and no way to verify the story is complete. Owner action: Marcus should write up his implementation plan as AC before planning. |
| **PR-119 no data story** | Yes | Flags that the dashboard home page story (PR-119) has no corresponding analytics or instrumentation story. The dashboard shows "open PRs, review queue, recent activity" — these are surfaces that need tracking events (page view, widget interactions, filter usage, etc.). Names what's missing: a data story for at minimum page-view events and key interaction events on the dashboard. Does not accept that "7 AC on layout" substitutes for a data plan. |
| **PR-104 stale (3 sprints)** | Yes | Names the staleness explicitly: "3 sprints in the backlog (since Sprint 19)." Provides a disposition recommendation — not just "this is stale" but one of: reprioritize (add to this sprint if capacity allows), remove (if not actually important), or rewrite scope (if poorly defined and that's why it keeps getting bumped). Does not let "the team will get to it eventually" stand without a concrete decision prompt. |

### Partial credit criteria

Each planted issue caught = 8% of total score. Partial catch (identifies the problem but gives no specific remediation) = 4%.

**Pass for any single issue:** Issue named, root problem identified, specific remediation stated with an owner. **Fail:** Issue not mentioned, or mentioned only in passing without a remediation step.

---

## Actionable Recommendations

Every flagged issue should include a specific next action with a named owner — not just a description of the problem.

| Quality level | Example |
|---------------|---------|
| **Pass** | "Reza needs to write AC for PR-112 tonight using Given/When/Then format before planning tomorrow." |
| **Fail** | "PR-112 needs acceptance criteria before it can be planned." |
| **Pass** | "Marcus should document his implementation plan for PR-115 as AC (6-8 conditions covering assignment logic, load calculation, tie-breaking, and edge cases) before the planning meeting." |
| **Fail** | "PR-115 needs AC." |

**Pass:** Every flagged issue has a named owner and a concrete action with timing context (e.g., "before planning tomorrow"). **Fail:** Issues listed without owners or without specific actions.

---

## No False Positives on Ready Stories

The four sprint-ready stories (PR-109, PR-110, PR-111, PR-116) are intentionally clean. They have clear AC, clear scope, and no hidden issues. The skill should not invent problems with these stories.

| Story | What "ready" looks like |
|-------|------------------------|
| PR-109 Add GitHub OAuth login | 5 AC, prerequisite story, clear scope — should appear in Ready section |
| PR-110 Webhook retry logic | 4 AC, technical and self-contained — should appear in Ready section |
| PR-111 PR comment threading UI | 6 AC, design handoff done — should appear in Ready section |
| PR-116 Email notification for review complete | 4 AC, narrow scope — should appear in Ready section |

**Pass:** All four stories appear in the "Ready for Sprint" section without issues. Capacity context (Sasha at 80%, Daniel at 80% week 1) may be noted as planning context but should not trigger false issues against these stories. **Fail:** Any of the four ready stories flagged for invented or trivial issues (e.g., "PR-110 could have more AC" when 4 AC fully cover a retry logic story).

---

## Output Format

The Analyze mode output should produce a structured Backlog Health Report — not a sprint plan.

### Required sections:

| Section | Required? | What it should contain |
|---------|-----------|------------------------|
| Agent Block | Yes | `backlog_health`, `ready_story_count`, `needs_refinement_count`, `missing_data_story_count` — all populated with values matching the analysis |
| Summary | Yes | Overall health status (Healthy / Needs Attention / Critical), ready count, needs-work count, top issues in 2-3 sentences |
| Ready for Sprint | Yes | Table of stories that passed readiness assessment. Should include PR-109, PR-110, PR-111, PR-116 and exclude the 5 flagged stories |
| Needs Refinement | Yes | Numbered list — each entry names the issue and states the fix with an owner |
| Split Candidates | Yes | PR-108 should appear here with a suggested split |
| Stale Items | Yes | PR-104 should appear here with a disposition recommendation |
| Missing Data Stories | Yes | PR-119 should appear here |
| Context note | Yes | States which company context files were loaded or absent |

**Pass:** All sections present. Agent Block `backlog_health` field matches the severity of issues found (with 5 flagged issues out of 9, "Needs Attention" or "Critical" — not "Healthy"). `needs_refinement_count` = 5, `ready_story_count` = 4, `missing_data_story_count` = 1. **Fail:** Output looks like a sprint plan with goals and selected stories; no Agent Block present; or Agent Block uses Draft mode fields instead of Analyze mode fields.

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| Mode detection (Analyze not Draft) | 15% | Produces backlog health report; does not produce a sprint plan with goals and committed stories |
| All 5 planted issues caught | 40% | 8% each: PR-108 too large with split suggestion; PR-112 no AC; PR-115 no AC despite "Dev knows"; PR-119 missing data story; PR-104 stale with disposition |
| Recommendations are actionable with named owners | 20% | Each flagged issue has a specific next action and a named owner; not just "this needs work" |
| No false positives on ready stories | 15% | PR-109, PR-110, PR-111, PR-116 all in Ready section without invented issues |
| Output format and Agent Block | 10% | All required sections present; Agent Block present with correct Analyze mode fields populated |
