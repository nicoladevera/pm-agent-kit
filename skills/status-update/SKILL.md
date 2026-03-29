---
skill: status-update
type: Generator
tier: 2
approval: draft-confirm
context-required: []
context-optional:
  - company/norms/communication.md
  - company/norms/team-process.md
  - company/facts/team.md
  - company/facts/product.md
degradation: proceed-with-caveat
---

# status-update

Assess delivery state across workstreams and/or produce status communications calibrated to a specific audience. Status updates tell the reader where things stand — not what was done. Activity is evidence; assessment is the point.

---

## What It Accepts

Any form of delivery data:
- Sprint board state (pasted or described)
- Notes on what happened this week/sprint
- A list of workstreams with current status
- A previous status update to diff against
- Raw delivery data (tickets completed, blockers, bugs opened/closed)
- A combination of the above

The input does not need to be organized. This skill synthesizes.

---

## Modes

This skill operates in two modes. The PM selects the mode through how they invoke it.

### Analyze

Assess the delivery state. Surface risks, blockers, dependencies, and velocity concerns. Produce an internal assessment the PM uses to decide what to communicate and where to intervene.

**Triggered by:** "assess delivery," "what's at risk," "analyze this sprint," "how are we tracking," or any request that asks for an assessment without a communication artifact.

### Draft

Analyze first (same process as Analyze mode), then produce a status communication calibrated to the specified audience. The analysis happens internally; the output is the comm.

**Triggered by:** "write the VP update," "draft a status update for the team," "send the weekly update," or any request that asks for a communication artifact. Requires an audience — if none specified, ask: "Who is this status update for?"

**Default:** If the mode is ambiguous, ask: "Do you want an assessment of where things stand, or a status update drafted for a specific audience?"

---

## Intake

Applies to **Draft mode only.** Analyze mode produces an internal assessment — intake adds no value there.

A status update without a clear top-line message becomes a list of things that happened. Confirm what the PM most wants the reader to take away.

### Signals to Check

- **Audience:** Named? (Already required for Draft mode — if missing, the existing ask handles this.)
- **Key takeaway:** Does the input signal what the single most important message is — the thing the reader should remember after scanning?
- **Mode clarity:** Is it clear the PM wants a drafted communication, not just an assessment?

### Adaptive Response

**Rich input** (audience named, delivery data provided, key message clear): Confirm and proceed. Example: "Status update for [audience]. Leading with [key takeaway]. Drafting now."

**Moderate input** (audience and data present, but no clear top-line message): Ask one targeted question:
- "What's the single most important thing you want [audience] to take away — is it [risk X], [progress on Y], or something else?"

**Thin input** (delivery data dumped with "write an update"): The existing audience ask fires first. Once audience is established, if the key message is unclear:

> **Based on the delivery data, here's the top-line message I'd lead with — tell me if this is right:**
>
> - **Lead:** "[Inferred assessment — e.g., 'Sprint is on track overall, but the payments integration is at risk of slipping by 3 days']"
> - **Emphasis for [audience]:** [What this audience most needs to hear — risk, progress, an ask]
>
> Should I lead with that, or is there something more important to surface?

---

## Instructions

### Shared Steps (Both Modes)

#### 1. Read the input fully

Absorb all delivery data before assessing. Understand what was planned, what happened, what changed, and what's coming. If a previous status update is included, note what was flagged then so you can track whether it's resolved.

#### 2. Load reference files

Read these files:
- `references/communication-quality.md` — Quality criteria for the output (both modes produce communication)
- `references/sprint-planning.md` — Sprint health indicators and what they signal
- `references/pm-smell-test.md` — Check for smells 4 (audience mismatch), 6 (activity reported as progress), and 12 (risk buried or absent)
- `references/audience-registers.md` — Per-audience communication register for calibrating tone, depth, and framing
- `references/pushback-and-negotiation.md` — For risk framing and scope trade-off communication
- `references/agent-readable-output.md` — Agent Block format and shared enum vocabulary

#### 3. Load company context (if available)

If `company/norms/communication.md` exists and is substantive, read it for status update conventions — who receives updates, how often, what format, what's expected.

If `company/norms/team-process.md` exists and is substantive, read it for sprint cadence and process context.

If `company/facts/team.md` exists and is substantive, read it for team structure, stakeholders, and who cares about what.

If `company/facts/product.md` exists and is substantive, read it for product landscape context.

If any of these files exist but are still stub templates, treat them as unavailable and say so in the output.

If no substantive company context is available, proceed — note the absence in the output.

#### 4. Assess delivery state

For each workstream or body of work in the input:

- **Status:** On Track / At Risk / Blocked / Complete
- **Evidence:** What data supports this assessment (stories completed, velocity trend, days remaining vs. work remaining)
- **Risks:** For at-risk items — what's the risk, how severe, what's the timeline impact, what would mitigate it
- **Blockers:** Anything blocked — what's blocking it, who owns the blocker, how long it's been blocked
- **Dependencies:** External dependencies — status, owner, whether they're tracking to timeline

**Look for what the data implies but doesn't state:**
- If 3 of 8 stories are still "in progress" on day 8 of a 10-day sprint, that's a velocity risk even if nobody said so
- If a dependency was "on track" last week and is now missing from the update, that's a signal
- If completed work doesn't connect to the sprint goal, that's activity without progress

#### 5. Compare to commitments

What was planned vs. what's actually happening? If sprint goals were stated, assess progress toward the goals — not just task completion. If a previous status update exists, note what changed: risks that materialized, blockers that resolved, new issues that emerged.

#### 6. Run the smell test

Check for:
- **Smell 6 (Activity as Progress)** — Are you (or the input) reporting what was done without assessing whether it moved the needle?
- **Smell 12 (Risk Buried or Absent)** — Are risks prominent in your output, or did they drift to the bottom?
- **Smell 4 (Audience Mismatch)** — In draft mode: is the detail level right for the stated audience?

### Analyze Mode: Produce the Assessment

Output the assessment using the Analyze Mode format below. Include recommended actions — what should the PM do next based on this assessment?

Populate the Agent Block from the completed assessment:
- `overall_status`: matches the Overall Status enum
- `active_blocker_count`: count of Blocked items in the Workstream Status table
- `at_risk_workstream_count`: count of At Risk items in the Workstream Status table
- `max_timeline_impact_days`: the largest timeline impact stated across all Risks entries (use 0 if none)
- `escalation_needed`: Yes if any Blocker entry has "Escalation needed: Yes"

### Additional Steps for Draft Mode

#### 7. Determine and calibrate for audience

Identify the audience from the invocation. Calibrate:

| Audience | Lead with | Detail level | Include |
|----------|----------|-------------|---------|
| **VP / Leadership** | Overall assessment + top risks | Summary — strategic, not operational | What you need from them |
| **Team** | Sprint progress + blockers | Detailed — operational, actionable | What's next, what's changed |
| **Cross-functional** | What they need to know + what they need to do | Interface-level — their dependencies and asks | Timeline impacts on shared work |
| **Stakeholders** | Progress toward commitments + risks to timeline | Mid-level — informed, not overwhelmed | When the next update comes |

#### 7b. Detect and adapt for pressure context

If the PM's input or invocation signals urgency, crunch, incident, or high-stakes context (launch week, production issue, tight deadline, org-wide reprioritization):

- **Shift from consultative to broadcast.** The update informs and directs; it doesn't invite open-ended discussion.
- **Anchor urgency to business consequences.** Not "this is a P0 bug" but "353 failures today, approaching payday weekend — support tickets will accumulate."
- **Include an explicit "Not Doing" list.** Name what's deprioritized and why, so the team and stakeholders don't have to guess.
- **Gratitude goes public and specific.** Under pressure, name individual contributions by person and what they did — not just "great work team."
- **Don't minimize scope.** Quantify the impact immediately. State what you know and what you don't.

#### 8. Draft the communication

- **Lead with the assessment, not activity.** The first sentence should tell the reader whether to be worried or not.
- **Risks and blockers before wins.** The reader needs to know what's at risk before they hear what went well.
- **"Needs from you" section** — if the audience can take action, make the ask explicit. If there's nothing they need to do, omit this section.
- **Link to everything referenced.** Jira tickets, dashboards, docs — never make the reader search.
- **Warm but efficient.** The reader should feel informed and respected, not processed.

---

## Output Format

### Analyze Mode

````markdown
## Delivery Assessment: [Sprint/Period]

### Overall Status: [On Track / At Risk / Blocked]

[1-2 sentence summary. Why this assessment.]

<!-- AGENT BLOCK -->
```yaml
agent_block:
  skill: status-update
  overall_status: [On Track / At Risk / Blocked]
  active_blocker_count: [integer]
  at_risk_workstream_count: [integer]
  max_timeline_impact_days: [integer — 0 if no impact]
  escalation_needed: [Yes / No]
```
<!-- /AGENT BLOCK -->

---

### Workstream Status

| Workstream | Status | Key Issue | Owner |
|------------|--------|-----------|-------|
| [Workstream 1] | [On Track / At Risk / Blocked / Complete] | [Primary issue or "Tracking well"] | [Who] |
| [Workstream 2] | ... | ... | ... |

---

### Risks

1. **[Risk]** — Severity: [High / Medium / Low]. Timeline impact: [X days/sprint]. Mitigation: [What would help].
2. **[Risk]** — ...

---

### Blockers

1. **[Blocker]** — Owner: [Who]. Duration: [How long blocked]. Escalation needed: [Yes / No].

---

### Dependencies

| Dependency | Owner | Due | Status |
|------------|-------|-----|--------|
| [What] | [Who] | [When] | [On track / At risk / Overdue] |

---

### Changes Since Last Update

- [What shifted since the last assessment — or "First assessment, no prior baseline"]

---

### Recommended Actions

- [What the PM should do next based on this assessment]
- [Conversations to have, escalations to make, scope decisions to consider]

> **Context note:** [State which substantive company files were loaded, which files were absent, and which files existed but were stub templates and therefore skipped. Note what the assessment might miss without that context.]
```

### Draft Mode

```markdown
## Status Update: [Sprint/Period] — [Audience]

### Summary

[Overall delivery state in 2-3 sentences. Lead with the assessment — on track, at risk, or blocked. Why.]

---

### What Needs Attention

- **[Risk or blocker]** — [Impact. What's being done. What help is needed.]
- **[Risk or blocker]** — [...]

---

### What's On Track

- [Workstream/item — brief status and what's expected next]
- [...]

---

### Key Wins

- [Completed items that matter to this audience — not just anything that got done]

---

### Needs From You

- [Specific asks to this audience. If none, omit this section entirely.]

---

### Next Week

- [What to expect in the next update cycle]

> **Context note:** [State which substantive company files were loaded, which files were absent, and which files existed but were stub templates and therefore skipped. Note that audience calibration was based on the stated or inferred audience.]
````

---

## Quality Bar

- **Does the assessment catch what a senior PM would catch?** Risks inferred from data, not just risks explicitly stated. Velocity concerns surfaced. Dependencies tracked.
- **Does the draft lead with assessment, not activity?** The reader knows whether to be worried within the first two sentences.
- **Is audience calibration correct?** A VP update is strategic, not operational. A team update is detailed, not summarized. The content matches what the reader needs.
- **Are risks stated with severity?** Not just "X is at risk" but how severe, what the timeline impact is, and what would mitigate it.
- **Would the PM trust this enough to send it?** After reviewing and editing, the PM should feel confident putting their name on it. The assessment should be one she'd use to prepare for a stakeholder conversation.

---

## Save

*Draft mode only.* After producing the artifact, write it to `knowledge/status-updates/` using the naming convention: `YYYY-MM-DD-period-status.md`, where `YYYY-MM-DD` is today's date and `period` is a lowercase hyphenated slug derived from the sprint or time period named in the update. Report the saved file path in the conversation. Analyze mode output is ephemeral — do not save it.
