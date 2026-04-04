# Evaluation Rubric — retro-synthesis (Platform Engineering: Kubernetes Migration)

**Target input:** `evals/retro-synthesis/sample-input-02.md`
**Skill under test:** `.claude/skills/retro-synthesis/SKILL.md`
**Purpose:** Determine whether `retro-synthesis` credits the two interventions that worked (documentation runbook, alert tuning), surfaces the stalled on-call review as an accountability failure (3 sprints, same owner, never completed), identifies that incident response time has not improved despite fewer incidents, and correctly distinguishes a 1-sprint emergence from a recurring pattern.

**Coverage:** Single mode — full skill coverage.

---

## Patterns the Skill Must Identify

| Pattern | Sprints | Trend | Must Catch? |
|---------|---------|-------|-------------|
| Documentation runbook intervention worked | Atlas-1 → Atlas-2 | Improving (resolved) | Yes — credit the improvement with evidence |
| Alert tuning intervention worked | Atlas-2 → Atlas-3 | Improving (resolved) | Yes — credit the improvement with evidence |
| Incident response time not improving | Atlas-1, 2, 3 | Flat (stuck) | Yes — the key analytical finding: volume is solved, response process is not |
| On-call load review never completed (3-sprint carryover) | Atlas-1, 2, 3 | Flat / Worsening | Yes — accountability failure on the same owner for three consecutive sprints |
| Product team interruptions (single sprint) | Atlas-3 only | Emerging | Should note as emerging signal, not a pattern — only 1 sprint of data |

---

## Action Item Tracking

The skill must track all action items with sprint of commitment, owner, and status.

| Action Item | Sprint Committed | Owner | Expected Status in Synthesis |
|-------------|-----------------|-------|-------------------------------|
| K8s DNS troubleshooting runbook | Atlas-1 | Priya | Done — verified effective in Atlas-2 (30-min resolution vs. 3 days) |
| On-call load review | Atlas-1 (carryover Atlas-2, Atlas-3) | Marcus | Never completed — 3 consecutive sprints outstanding |
| Alert tuning session | Atlas-2 | Priya | Done — false positive rate dropped from ~40% to ~12% |
| Intake process for product team requests | Atlas-3 | Jamie | Not yet assessed — committed once, one sprint old |

**Pass:** On-call review called out explicitly as 3-sprint carryover on the same owner (Marcus). The synthesis uses direct language: "This action item has been committed in every sprint of this project and never completed." Synthesis names the impact: on-call burden on Jamie and Priya has not been addressed.
**Fail:** Carryover noted as "still in progress" or "pending." Marcus not named. The 3-sprint pattern not distinguished from a normal open item.

---

## Response Time vs. Volume Distinction

This is the most critical analytical test in this rubric. The alert tuning intervention reduced incident volume (3 incidents → 1 incident) but average response time has not improved (47 min in Atlas-2 → 45 min in Atlas-3). The team may confuse "fewer incidents" with "on-call is fixed." They are different problems requiring different interventions.

**Pass:** Synthesis explicitly names the distinction: "Alert tuning solved the volume problem — incidents dropped from 3 to 1. But response time has not improved: 47 minutes in Atlas-2, 45 minutes in Atlas-3. The SLA is 30 minutes. These are separate problems. Volume was a noise problem (too many false positives); response time is a process problem (how the team responds once a real alert fires). The alert tuning intervention was correct but it doesn't fix response time. The team may believe on-call is improving overall — it is, in one dimension. It is not improving in the dimension that is actually measured by the SLA."

**Fail:** "On-call is improving" treated as fully true because alert volume dropped. Response time data present but not interpreted for the implication. The 45-minute average treated as a minor remaining issue rather than the actual open problem.

---

## Credit for What Worked

Both the DNS runbook and the alert tuning intervention worked. The synthesis must credit these specifically — not with generic praise but with evidence.

**Pass:**
- Names the DNS runbook intervention (Atlas-1, Owner: Priya) and the measurable improvement: Atlas-2 resolved a DNS issue in 30 minutes vs. 3 days in Atlas-1. Connects the action item to the outcome.
- Names the alert tuning intervention (Atlas-2, Owner: Priya) and the measurable improvement: false positive rate dropped from ~40% to ~12%. Incident volume dropped from 3 to 1.
- Frames these as a pattern: "Priya's two interventions — documentation and alert tuning — both produced measurable improvements. This is what working action items look like."

**Fail:** "Team made progress on documentation" without naming the intervention or the outcome. Improvements mentioned in passing without connecting them to the action item that caused them.

---

## Product Team Interruptions: Emerging Signal, Not a Pattern

The product team interruptions appeared in Atlas-3 only. One sprint of data is not enough to call it a pattern. The synthesis must scope this correctly.

**Pass:** "Product team interruptions surfaced in Atlas-3 — three unplanned requests mid-sprint that contributed to two K8s stories slipping. This is one sprint of data, not a pattern. It should be monitored: if it appears in Atlas-4, treat it as a pattern. An intake formalization action item (Owner: Jamie) was committed in Atlas-3."
**Fail:** Treated as a recurring pattern requiring immediate structural fix. Or framed with the same urgency as the on-call issue. Or labeled as "recurring external dependency problem" when it has only appeared once.

---

## Proactive Gap-Closing

The synthesis should name at least one insight not explicitly stated in any retro. The retros describe symptoms but don't diagnose the response time problem.

**Pass:** Names the underlying issue: "The team has two different on-call problems that are being tracked as one. The first — alert volume and fatigue — has been largely resolved by the alert tuning. The second — response process speed — has never been directly addressed. There's no action item specifically targeting response time reduction: no runbook for incident command, no on-call escalation path, no first-response SLA protocol. The 3-sprint-old on-call review that Marcus hasn't completed may be the right vehicle to address this, but only if it expands scope from 'load balancing the rotation' to 'improving our response process.'"
**Fail:** Every finding in the synthesis is traceable directly to a verbatim statement in the retros. The synthesis is thorough but not analytical.

---

## Recommended Focus Quality

**Expected top priority:** Incident response time / response process — the SLA is not being met, the volume problem is solved, and no action item has directly targeted response process improvement.

**Expected second priority:** On-call load review completion — Marcus's carryover action item is now 3 sprints old and may be the vehicle to address both rotation fairness and response process.

**Pass:** Recommendations are specific and actionable:
- "Dedicate an Atlas-4 working session specifically to incident response process — time from page to first action. Map the current response steps, find where time is lost, set a target. This is distinct from the rotation load question."
- "Marcus completes the on-call review in Atlas-4 or ownership is reassigned. The review should include rotation fairness AND response process improvement."

**Fail:** Generic recommendations like "improve incident response" or "address on-call burnout." Recommendations not distinguishing the two separate on-call problems.

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| Documentation and alert tuning interventions credited with evidence | 15% | Both interventions named, sprint committed, owner named, measurable improvement cited (30-min resolution; 40% → 12% false positive rate) |
| On-call review identified as 3-sprint carryover with accountability call-out | 20% | Marcus named explicitly; "3 consecutive sprints" language present; impact on team named |
| Response time vs. volume distinction named as separate problems | 25% | Synthesis explicitly states these are different problems requiring different interventions; SLA gap not attributed to volume |
| Action item tracking with status for all items | 20% | All 4 action items tracked with sprint, owner, and status; "not yet assessed" for Atlas-3 new item |
| Product team interruptions correctly scoped as emerging signal | 10% | 1-sprint caveat present; not treated as recurring pattern; "monitor in Atlas-4" framing |
| Recommended focus specific and actionable | 10% | Top 1-2 recommendations name specific actions (response process mapping, on-call review scope expansion or ownership change) |
