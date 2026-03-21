---
skill: retro-synthesis
type: Analyzer
tier: 2
approval: draft-confirm
context-required: []
context-optional:
  - company/norms/process.md
  - company/facts/team.md
degradation: proceed-with-caveat
---

# retro-synthesis

Synthesize retrospective notes into patterns — what keeps recurring, what got fixed, what's getting worse. Track action items across retros and flag which ones were never addressed. The value is synthesis, not summary. "Team discussed carryover" is summary. "This is the third sprint in a row that carryover was raised. The action item from Sprint 12 (reduce WIP limits) was never implemented" is synthesis.

---

## What It Accepts

Any form of retrospective input:
- Retro notes from a single retrospective
- Retro notes from multiple retrospectives (for longitudinal analysis)
- A previous retro synthesis (for tracking patterns over time)
- Action items from previous retros (for follow-through tracking)
- Miro board exports, structured retro docs, or raw unstructured notes
- A combination of the above

The skill is more useful with multiple retros — one retro gives you themes; three retros give you patterns.

---

## Instructions

### 1. Read all input before analyzing

If multiple retros are provided, read every one before identifying patterns. Cross-retro patterns are invisible if you analyze each retro in isolation. Note which sprint or date each retro covers.

### 2. Load knowledge files

Read these files:
- `knowledge/pm-philosophy.md` — Reference the "Proactive Gap-Closing" heuristic: don't wait for the team to notice patterns; surface them
- `knowledge/pm-smell-test.md` — Check for smell 6 (activity reported as progress): the team did a retro but nothing changed
- `knowledge/communication-quality.md` — The synthesis itself is a communication artifact; it should meet communication quality standards

### 3. Load company context (if available)

If `company/norms/process.md` exists and is substantive, read it for retro cadence, sprint rhythm, and team process context. This helps assess whether issues are process-related or situational.

If `company/facts/team.md` exists and is substantive, read it for team structure context — who owns what, team dynamics references.

If either file exists but is still a stub template, treat it as unavailable and say so in the output.

If neither substantive file is available, proceed — note the absence in the output.

### 4. Categorize items

Group retro items into themes. Common categories (adapt based on what the data shows):
- **Process** — sprint mechanics, planning, estimation, ceremonies
- **Communication** — information flow, alignment, cross-team coordination
- **Tooling** — developer experience, infrastructure, CI/CD, environments
- **Scope** — scope creep, unclear requirements, changing priorities
- **Quality** — bugs, tech debt, testing gaps, production issues
- **Team dynamics** — collaboration, morale, workload distribution
- **External dependencies** — other teams, vendors, third-party systems

Don't force categories. If the data suggests a theme that doesn't fit the list above, use it. If a category has no items, omit it.

### 5. Identify patterns across retros

For each theme that appears in the input:
- **Frequency** — How many retros raised this theme?
- **Trend** — Getting better, getting worse, or flat?
- **Evidence** — What specifically was said in each retro? Quote or paraphrase.
- **Root cause** — If the same issue recurs, why? Is there a structural cause?

Distinguish between:
- **Recurring patterns** — appeared in 2+ retros, indicating a structural issue
- **One-time items** — appeared once; may have been resolved, or may have been forgotten
- **Improvements** — something that was a problem and got better (credit what worked)

### 6. Track action items

For each action item from current and previous retros:
- What was committed
- Who owned it
- Which sprint it was committed in
- Current status: Done / In Progress / Not Started / Abandoned

Flag action items that were committed but never addressed — especially recurring ones. This is the most important function of the synthesis. If the team keeps committing to the same action item without follow-through, that pattern needs to be named plainly: "This action item has been committed in 3 sprints and never started. Either commit resources or acknowledge this won't happen."

### 7. Assess severity

Not all retro items are equal. A recurring communication breakdown that affects delivery is more serious than a one-time tooling glitch. Prioritize by:
- **Impact** — How much does this affect delivery, quality, or team health?
- **Recurrence** — Is this a pattern or an incident?
- **Trend** — Is it getting worse?

### 8. Synthesize, don't summarize

The output should surface insights the team might not see from individual retros:
- Patterns across time ("carryover has been raised in every retro for 4 sprints")
- Connections between themes ("the scope creep complaints and the estimation complaints may be the same problem")
- Action item accountability ("we committed to X three times and never did it")
- What actually worked ("code review speed improved after we adopted the pairing model in Sprint 11")

Avoid simply restating what each retro discussed. If the output reads like "Sprint 10 discussed X, Sprint 11 discussed Y," it's a summary, not a synthesis.

### 9. Run the smell test

Check for:
- **Smell 6 (Activity as Progress)** — Is the retro producing action items that never get addressed? Is the team going through the motions of reflection without the follow-through?
- **Proactive Gap-Closing** — Are you surfacing patterns the team hasn't named yet? Connections they might not see?

### 10. Recommend focus

Based on the synthesis, recommend 1-2 areas for the team to focus on. Prioritize by: most impactful, most recurring, or most worsening. These should be specific enough to act on — not "improve communication" but "establish a shared channel for cross-team dependency updates, since dependency miscommunication was raised in 3 of the last 4 retros."

---

## Output Format

```markdown
## Retro Synthesis: [Sprint(s) Covered]

### Summary

[2-3 sentences. Most important pattern. Biggest unresolved issue. One thing that's working well.]

---

### Recurring Patterns

| Pattern | Sprints Seen | Trend | Severity |
|---------|-------------|-------|----------|
| [Theme] | [Sprint X, Y, Z] | [Getting better / Getting worse / Flat] | [High / Medium / Low] |
| [Theme] | ... | ... | ... |

---

### What's Improving

- **[Pattern]** — Evidence: [What changed. What intervention worked. Which sprint it turned around.]

---

### What's Getting Worse

- **[Pattern]** — Evidence: [What's happening. How severe. Impact on delivery or team health.]

---

### One-Time Items

- [Items that appeared in a single retro. Note whether resolved or status unknown.]

---

### Action Item Tracker

| Action Item | Sprint Committed | Owner | Status |
|-------------|-----------------|-------|--------|
| [Item] | [Sprint X] | [Who] | [Done / In Progress / Not Started / Abandoned] |

---

### Unaddressed Action Items

- **[Action item]** — Committed in [Sprint X]. Status: [Not started / Abandoned]. This is the [Nth] sprint it's been open. Impact: [What continues to suffer because this wasn't done.]

---

### Recommended Focus

1. **[Top priority]** — Why: [Most impactful / most recurring / most worsening]. Suggested action: [Specific, actionable recommendation.]
2. **[Second priority]** — Why: [...]. Suggested action: [...]

> **Context note:** [State which substantive company files were loaded, which files were absent, and which files existed but were stub templates and therefore skipped. Also note the number of retros analyzed and whether a previous synthesis was available for longitudinal tracking.]
```

---

## Quality Bar

- **Does the synthesis surface patterns the team might not see?** Cross-retro connections, root causes behind recurring themes, action item accountability. Not just a restatement of what was discussed.
- **Are action items tracked with follow-through accountability?** Every committed action item has a status. Unaddressed items are called out with sprint count and impact.
- **Is the "getting worse" section honest?** Not softened, not buried. If something is deteriorating, the synthesis says so plainly and names the impact.
- **Does the recommended focus prioritize by impact?** Not by recency. The most important pattern gets top billing even if it's not the newest one.
- **Would a team lead find this useful for improving team health?** The synthesis gives them ammunition: data-backed patterns, specific recommendations, and accountability for past commitments.
