# Evaluation Rubric — status-update (Analyze Mode)

**Target input:** `evals/status-update/sample-input-02.md`
**Skill under test:** `skills/status-update/SKILL.md`
**Purpose:** Determine whether `status-update` Analyze mode correctly infers risks from data (including unstated ones), surfaces the explicit blocker and both implicit risks, and produces an internal assessment — not an audience-addressed communication.

## Coverage

**This rubric tests:** Analyze mode — internal delivery state assessment, no audience specified, no communication output.
**Not covered here:** Draft mode (audience-addressed status communication) — see `rubric.md`.

---

## Mode Detection

No audience is named in the input. The PM explicitly says "not writing anything up for stakeholders" and asks for an "honest read on where we are." This should trigger **Analyze mode**.

**Pass:** Produces an internal assessment of delivery state — workstream status table, risk log, blockers, dependency flags. Output is structured for the PM's own use. **Fail:** Produces an audience-addressed communication (a VP email, a team update with a subject line and greeting, or a stakeholder summary). If the output opens with "Hi [name]" or has a "To:" field, that is a clear fail.

---

## Risks the Skill Must Infer

Five risks are present in the input. Two are stated explicitly; two require inference from data; one should be flagged as a downstream impact. The core test is whether the skill surfaces what the data implies, not just what was stated.

| Risk | Must Catch? | What good detection looks like |
|------|-------------|-------------------------------|
| **Sprint goal at risk from low completion rate** | Yes | The math must be done. Day 6 of 10, 4 of 14 stories done (29% complete). 9 stories not started. To hit both sprint goals, those 9 stories need to complete in 4 remaining days — roughly 2.25 stories/day, against the current pace of ~0.67 stories/day (4 stories over 6 days). The assessment should surface this velocity gap explicitly with numbers, not just say "things are behind." |
| **Explicit blocker: legal review delayed** | Yes | Named and assessed for impact, not just listed. The legal delay on the consent form is blocking Marcus from finalizing SEL-204 and doing integration testing for SEL-205 (Checkr submission). This is on the critical path for Sprint Goal 1 ("functional seller onboarding flow through background check submission"). Legal said "by end of next week" — which is after the sprint ends. The assessment should name this as a potential sprint goal miss, not just a ticket status issue. |
| **Implicit risk: Priya's sick leave (capacity reduction)** | Yes | Priya has been out sick since day 4 (3 days). Her 2 stories (SEL-206, SEL-207) are not started. Neither has been reassigned. The assessment should surface this as a capacity risk even though the input doesn't frame it as one — the PM reported it as factual context, not as a flagged risk. Detection: "Priya has been out 3 days with 2 unstarted stories (SEL-206, SEL-207) — 10 story points without an assigned resource for the remaining 4 days. These stories are on the critical path for Sprint Goal 2 (marketplace profile visibility) and have not been reassigned." |
| **Implicit risk: Checkr API spec unconfirmed** | Yes | The PM mentioned this casually ("Marcus thinks we're fine but wants to confirm"). The skill should surface it as a dependency risk, not treat it as a non-issue because Marcus is optimistic. Detection: "API spec confirmation from Checkr is pending. Marcus is proceeding on the assumption that the initial docs are current. If the spec differs from assumptions, test rework on SEL-212 is likely, and the Checkr integration work (SEL-205, SEL-212) may need revision." Should be flagged as an unconfirmed external dependency with unknown resolution timeline. |
| **Downstream sprint impact** | Should flag | SEL-206 and SEL-207 are blockers for SEL-208, which is the foundation for Sprint 9's marketplace visibility work. If these stories slip (which the current data suggests is likely), Sprint 9's first week is blocked. The assessment should surface this as a downstream risk — not just "these stories aren't done" but "slippage here cascades into Sprint 9." |

---

## Assessment Leads with Risk, Not Activity

The overall status should be stated upfront and should be derived from the data, not softened.

Given the inputs — day 6 of 10, 29% complete, an explicit blocker with a post-sprint resolution timeline, a capacity reduction with no mitigation, and an unconfirmed external dependency — the correct overall status is **At Risk**.

**Pass:** First paragraph states overall status ("At Risk") and explains the primary reason in 1-2 sentences. The reader knows the sprint is in trouble before they see the details. Example: "The seller onboarding sprint is At Risk. At day 6, 29% of stories are complete — the current pace requires a ~3x acceleration to hit both sprint goals, and the legal review delay puts Sprint Goal 1 (background check submission) at risk of slipping past sprint end." **Fail:** Output leads with "The team has completed 4 stories this sprint, including..." — completed work listed before the risk assessment. Or overall status assessed as "On Track" or "Minor Concerns" given the available data.

---

## Output Is an Assessment, Not a Communication

The Analyze mode output should be structured for the PM's internal use only — a reference document they use to prepare for the team sync and decide what to escalate. It should not read like a message to send to someone.

| Output structure | Pass | Fail |
|-----------------|------|------|
| Overall status header | "Overall Status: At Risk" | "Subject: Sprint 8 Update" |
| Workstream status table | Table with Status, Key Issue, Owner columns | Paragraph addressed to stakeholders |
| Risks section | Numbered list with severity and timeline impact | "I wanted to flag that..." |
| Blockers section | Blocker named, duration noted, escalation flag | Buried in a paragraph |
| Dependencies section | Table with owner, due date, status | Mentioned as an aside |
| Recommended actions | Bulleted list of what the PM should do | "Let me know if you have questions" |

**Pass:** Output uses assessment structure (workstream table, risks, blockers, dependencies, actions). No audience framing. **Fail:** Output is formatted as an email, a Slack message, or a communication artifact addressed to any person.

---

## Agent Block Correct

Analyze mode Agent Block should include the five fields from the `status-update` skill's Analyze mode output spec: `overall_status`, `active_blocker_count`, `at_risk_workstream_count`, `max_timeline_impact_days`, `escalation_needed`.

Given the input data, expected values:
- `overall_status`: At Risk
- `active_blocker_count`: at minimum 1 (legal review delay is an explicit blocker; Priya's absence could be counted as a second)
- `at_risk_workstream_count`: at minimum 2 (Sprint Goal 1 blocked by legal; Sprint Goal 2 at risk from Priya absence)
- `max_timeline_impact_days`: at least 4 (legal said "end of next week" — that's after sprint end, meaning the background check flow may not complete this sprint)
- `escalation_needed`: Yes (legal review delay needs escalation to unblock Marcus)

**Pass:** Agent Block present with all five fields using the correct field names from the Analyze mode spec. Values are internally consistent with the risks identified in the assessment. **Fail:** No Agent Block; Agent Block uses Draft mode fields (`audience`, `delivery_status`, etc.) instead of Analyze mode fields; or fields present but values are clearly inconsistent with the risks (e.g., `escalation_needed: No` when a blocker requiring escalation is named).

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| Mode detection (Analyze not Draft) | 10% | Internal assessment produced; no audience-addressed communication; no subject line or greeting |
| Sprint goal risk surfaced with math | 15% | Velocity gap calculated explicitly (4 done in 6 days; 9 remaining in 4 days; ~2.25/day needed vs. ~0.67/day current); overall status assessed as At Risk |
| Explicit blocker named and impact assessed | 15% | Legal review delay identified as blocker; connected to Sprint Goal 1 (background check submission); "end of next week" resolution timeline flagged as post-sprint |
| Implicit risk 1 (Priya sick leave) inferred | 20% | Priya's absence surfaced as a capacity risk even though not flagged as such in input; unstarted stories (SEL-206, SEL-207) identified; Sprint Goal 2 impact named |
| Implicit risk 2 (Checkr API spec unconfirmed) inferred | 20% | Checkr API spec gap flagged as a dependency risk; Marcus proceeding on assumptions identified as a risk; potential rework impact named |
| Assessment format (not communication format) | 10% | Workstream status table, risks, blockers, dependencies, and recommended actions all present in PM-reference format; no communication framing |
| Agent Block with correct fields | 10% | All five Analyze mode fields present with correct names; values consistent with risks identified in the assessment |
