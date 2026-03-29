# Evaluation Rubric — retro-synthesis

**Target input:** `evals/retro-synthesis/sample-input-01.md`
**Skill under test:** `skills/retro-synthesis/SKILL.md`
**Purpose:** Determine whether `retro-synthesis` identifies cross-retro patterns, tracks action item follow-through, credits improvements, and produces synthesis rather than summary.
**Coverage:** Single mode — full skill coverage.

---

## Patterns the Skill Must Identify

The input contains three retros with deliberate patterns:

| # | Pattern | Sprints | Trend | Must Catch? |
|---|---------|---------|-------|-------------|
| 1 | **Carryover is recurring** — Raised in all 3 retros (Sprint 10, 11, 12). Different proximate causes each time (underestimation, scope expansion, design delay), but the pattern is persistent. Action items committed in every retro ("reduce carryover") with different tactics each time, but carryover keeps happening. | 10, 11, 12 | Flat/Getting worse | Yes — this is the central pattern |
| 2 | **Code review speed improved** — A problem in Sprint 10 (Sarah bottleneck), action taken (add Dev as reviewer), measurably improved by Sprint 11 (~2 days → ~1 day), sustained in Sprint 12. | 10 → 11 → 12 | Getting better | Yes — this is the improvement story |
| 3 | **Testing gaps persist** — Bugs found late in Sprint 11. Action item committed ("unit tests before review"). Only 60% compliance by Sprint 12. Bug still found late in Sprint 12. The action item isn't working. | 11, 12 | Getting worse | Yes |
| 4 | **Cross-team communication fixed** — Risk team surprise in Sprint 10. Slack channel set up in Sprint 11. Working well by Sprint 12. No more surprises. | 10 → 11 → 12 | Getting better (resolved) | Yes — credit the fix |
| 5 | **Planning efficiency improved** — 2.5-hour planning in Sprint 11. Separate refinement session introduced. 75-minute planning in Sprint 12. | 11 → 12 | Getting better | Should catch |

---

## Action Item Tracking

The skill must track action items across retros with status:

| Action Item | Sprint | Owner | Expected Status |
|-------------|--------|-------|----------------|
| Break large stories into smaller pieces | 10 | Maria | Partially adopted — but carryover persists, suggesting the intervention isn't sufficient |
| Shared Slack channel with risk team | 10 | Sarah | Done — working well |
| Add Dev as secondary reviewer | 10 | Sarah | Done — working well |
| Story point buffer (plan to 85%) | 11 | Maria | Implemented — unclear impact (still had carryover) |
| Unit tests before review | 11 | Dev | Partially adopted (~60%) — not consistently followed |
| Separate refinement session | 11 | Maria | Done — working well |
| Design finalized before sprint start | 12 | Maria + Ana | Not yet assessed |
| PR template checklist for tests | 12 | Sarah | Not yet assessed |
| Planning poker for estimation | 12 | Maria | Not yet assessed |

**Must catch:** The "reduce carryover" action item has been committed in some form in all 3 retros. Different tactics each time (break stories → capacity buffer → design sign-off). The synthesis should name this pattern: the team keeps committing to fix carryover but the root cause may be deeper than any individual tactic.

**Must catch:** The "unit tests before review" commitment has 60% compliance — the action item isn't working as intended. The synthesis should flag this as needing a different approach, not just continued commitment.

---

## Synthesis vs. Summary Test

The most critical quality test. The output should surface insights not visible from any single retro:

| Check | Synthesis (Pass) | Summary (Fail) |
|-------|-----------------|----------------|
| **Carryover** | "Carryover has been raised in every retro for 3 sprints. The team has tried 3 different interventions (story splitting, capacity buffer, design sign-off). None have resolved it. The root cause may be deeper — estimation accuracy, scope management, or planning assumptions." | "Sprint 10 discussed carryover. Sprint 11 discussed carryover. Sprint 12 discussed carryover." |
| **Testing** | "The testing commitment from Sprint 11 has 60% compliance. A process commitment that's only 60% followed isn't a solved problem — either the process needs enforcement (PR template checklist) or the team needs to decide this isn't actually a priority." | "Sprint 11 committed to unit tests. Sprint 12 notes 60% compliance." |
| **Improvements** | "Code review speed improved from ~2 days to ~1 day after adding Dev as reviewer. This is a success story — a clear problem, a specific intervention, and measurable improvement sustained over 2 sprints." | "Code review improved." |
| **Connections** | "The carryover and estimation problems may be related — scope expansion and integration complexity both suggest the team is consistently underestimating. The separate refinement session is a step in the right direction, but refinement quality (not just timing) may need attention." | No cross-theme connections |

---

## Proactive Gap-Closing

The highest bar for synthesis: surfacing insights the team hasn't named, not just connecting things they have named.

The key test: **could someone read all 3 retro inputs and independently reach every point in the synthesis?** If yes, the synthesis is thorough but not proactive. Proactive synthesis finds the thing no individual retro explicitly says.

### What proactive gap-closing looks like in this sample

The three retros never state: "the problem might be our estimation model, not our tactics." They describe symptoms (carryover, scope expansion, missed estimates) but don't diagnose the root cause. A proactive synthesis would:
- Observe that the team has tried 3 different tactical interventions for carryover (story splitting, capacity buffer, design sign-off), none of which have resolved it
- Name that when interventions don't work, the root cause may be upstream of the tactics — in this case, estimation accuracy during planning, not execution discipline
- Recommend tracking actual vs. estimated points per story for 2 sprints to surface where the gap lives

This insight is deducible from the data but never explicitly named in any retro.

**Pass:** The synthesis includes at least one insight that isn't stated in any retro input — something deducible from the pattern across retros but requiring interpretive synthesis. The PM reads it and learns something they didn't already know from reading the retros themselves.

**Fail:** Every point in the synthesis can be traced to a verbatim statement in one of the three retro inputs. The synthesis is comprehensive but not analytical — it's an organized copy, not an interpretation.

---

## Recommended Focus Quality

The synthesis should recommend 1-2 focus areas:

**Expected top priority:** Carryover / estimation — most recurring, unresolved despite multiple interventions, affects delivery predictability.

**Expected second priority:** Testing compliance — action item not working, risk of shipping bugs, needs a different approach.

**Pass:** Recommendations are specific and actionable ("investigate why estimation is consistently off — track actual vs. estimated for the next 2 sprints" not "improve estimation"). **Fail:** Generic recommendations ("focus on quality" or "improve processes").

---

## Quality Checks

### Honesty
Does the synthesis honestly name that carryover keeps happening despite action items? Does it name that the testing commitment isn't being followed? These are uncomfortable truths that a good synthesis doesn't soften.

**Pass:** Direct and specific about unresolved patterns. **Fail:** Softened language that obscures the persistence of the problem.

### Credit Where Due
Does the synthesis acknowledge the improvements? Code review speed, cross-team communication, and planning efficiency all improved through specific interventions. A synthesis that only names problems is demoralizing and inaccurate.

**Pass:** Improvements acknowledged with evidence (what changed, what intervention worked). **Fail:** Only problems surfaced, or improvements mentioned without evidence.

### Action Item Accountability
Are action items tracked with sprint of commitment, owner, and status? Are unaddressed items called out with sprint count?

**Pass:** Every action item has a status. The "reduce carryover" pattern is named as a 3-sprint recurring commitment. **Fail:** Action items listed without tracking or no follow-through assessment.

---

## Overall Assessment

**Would a team lead use this synthesis to run a better retro and improve team health?**

- Does it surface patterns the team might not see from individual retros?
- Does it hold the team accountable for past commitments?
- Does it credit what's working, not just call out problems?
- Does it recommend specific, actionable focus areas?
- Would the PM walk into the next retro with data-backed observations instead of feelings?

**Pass threshold:** Identifies all 5 patterns (carryover recurring, code review improved, testing gaps persist, cross-team comm fixed, planning improved), tracks action items with status across retros, produces synthesis (not summary), and recommends specific focus areas.

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| Pattern identification | 25% | All 5 patterns identified (carryover recurring, code review improved, testing gaps persist, cross-team comm fixed, planning improved) |
| Action item tracking | 20% | Every action item has sprint of commitment, owner, and status; 3-sprint carryover pattern named |
| Synthesis vs. summary test | 20% | Cross-retro insights produced; connections made between themes; not just organized summary |
| Proactive gap-closing | 10% | At least one insight not stated in any retro input — deducible from pattern across retros but requiring interpretive synthesis |
| Recommended focus quality | 10% | Top 1-2 priorities are specific and actionable; not generic ("improve processes") |
| Honesty | 10% | Persistent problems named directly; action items not working called out without softening |
| Output format compliance | 5% | Matches declared format; context note present |
