# PM Smell Test

Red flags that indicate a PM artifact isn't ready — applicable across document types, not just PRDs. Use this when reviewing any product artifact: PRDs, tickets, status updates, sprint plans, decision logs, meeting briefs, competitive analyses, business cases, or launch checklists.

Each smell signals that more thinking is needed before the artifact should move forward. Some smells are universal (they apply to everything). Others are artifact-specific.

---

## Universal Smells

These apply to any PM artifact regardless of type.

### 1. Missing the "Why"

The artifact describes *what* but not *why*. A PRD without a problem statement. A sprint goal without a reason. A status update that reports activity but not progress toward an objective. A decision log that records the decision but not the reasoning. Every PM artifact exists to serve a purpose — if the purpose isn't stated, the artifact can't be evaluated.

**What to look for:** The document jumps straight into content without establishing context or motivation. You can't answer "why does this matter?" from reading it.

### 2. No Way to Measure Success

The artifact has no measurement plan. A PRD with vague metrics. A sprint plan with no definition of "done." A launch checklist with no success criteria for the launch itself. A competitive analysis with no framework for what signals matter. If you can't tell whether the thing worked, you haven't finished defining it.

**What to look for:** Metrics without targets, targets without timeframes, timeframes without baselines. Claims that can't be verified. "We'll track this later."

### 3. Missing Owners

Decisions, dependencies, action items, or open questions with no named person responsible. This shows up everywhere: PRDs with unowned dependencies, sprint plans with unassigned risks, retro action items that belong to nobody, decision logs with "the team decided."

**What to look for:** Any action or dependency without a specific person's name. "TBD" as a permanent state. "The team" as an owner.

### 4. Audience Mismatch

The artifact isn't calibrated for who's reading it. A VP status update with engineering-level detail. A sprint plan written for stakeholders instead of the team. A meeting brief that assumes context the attendees don't have. Every artifact has a reader — if the content doesn't match what that reader needs, it fails regardless of quality.

**What to look for:** Level of detail that's wrong for the audience. Jargon the reader won't know. Missing context the reader needs. Detail the reader doesn't need.

### 5. False Precision

The artifact presents uncertain information with confident specificity. Timeline estimates treated as commitments. Preliminary data presented as conclusive. Competitive intelligence stated as fact when it's inference. Confidence should match the quality of the underlying information.

**What to look for:** Dates without caveats on known risks. Data insights without sample sizes or confidence intervals. Competitive claims without source attribution. Impact estimates presented as forecasts.

### 6. Activity Reported as Progress

The artifact describes what was done rather than what it achieved. A status update that lists completed tasks but doesn't assess whether the project is on track. A retro that catalogs discussion topics but doesn't synthesize patterns. A sprint review that shows demos but doesn't evaluate against the sprint goal.

**What to look for:** Lists of completed items with no assessment of whether they moved the needle. "We did X, Y, Z" with no "and this means..."

---

## Specification Smells

These apply to PRDs, tickets, technical specs, and other artifacts that define what to build.

### 7. Solution Without a Problem

The document starts with what to build instead of why to build it. A feature description without a problem statement is a solution in search of justification.

**What to look for:** The document leads with functionality. The problem statement is absent or is a single vague sentence. The "why" section restates the "what."

### 8. Unbounded Scope

No explicit scope boundaries, or the scope keeps growing within the document. "And eventually we could also..." and "future phases will include..." blur what's being built now versus what's aspirational.

**What to look for:** In-scope sections that include future phases. Features mentioned in passing that appear in AC but not in scope. The word "eventually" in a v1 spec.

### 9. Happy Path Only

The document describes what happens when everything goes right but not what happens when things fail. No error states. No unexpected user behavior. No system failures. No edge cases around timing, concurrency, or partial completion.

**What to look for:** No mention of error states, fallbacks, or failure modes. No discussion of users in unexpected states.

### 10. Untestable Acceptance Criteria

AC that can't be verified without reading the PM's mind. Subjective language, undefined terms, compound requirements.

**What to look for:** AC containing "appropriate," "relevant," "user-friendly," "fast," or "seamless" without definitions. See `knowledge/acceptance-criteria.md` for the full standard.

### 11. No Data Plan

The artifact describes a feature but never specifies how you'll know if it worked. No events, no tracking, no dashboards, no schemas. The feature will launch without instrumentation.

**What to look for:** Success metrics with no measurement plan. No mention of analytics events or data engineering. See the "Data Requirements Are Product Requirements" heuristic.

---

## Communication Smells

These apply to status updates, stakeholder communications, meeting briefs, and other artifacts meant to inform or align.

### 12. Risk Buried or Absent

The update presents an optimistic picture without surfacing what's actually at risk. Risks are mentioned in passing, minimized, or absent entirely. The reader walks away feeling good when they should feel concerned.

**What to look for:** Status reports that are all green. Updates where risks appear only at the bottom. Language that softens the severity ("slight delay" for a two-week slip).

### 13. Missing Context for the Audience

The artifact assumes the reader has context they don't have. A stakeholder update that references tickets by ID. A decision log that assumes knowledge of the previous meeting. A meeting brief that doesn't explain why this meeting is happening.

**What to look for:** References to things the reader can't access or doesn't know about. Unexplained acronyms. Decisions presented without the context that makes them make sense.

---

## Decision and Strategy Smells

These apply to decision logs, business cases, competitive analyses, and strategic artifacts.

### 14. Options Not Considered

A decision is presented as the only option rather than the best option among alternatives. A business case that doesn't name what else could be done with the same resources. A decision log that records the choice but not what was rejected and why.

**What to look for:** No "alternatives considered" section. No trade-off analysis. The recommendation presented as inevitable rather than chosen.

### 15. Recency Bias in Analysis

Competitive analysis or customer feedback that overweights recent events. A competitor launches a feature and the response is panic; customer feedback from the last week dominates a quarterly synthesis. Signal should be weighted by pattern, not by recency.

**What to look for:** Analysis dominated by the most recent data points. No longitudinal view. Conclusions that would change entirely if last week's data were removed.

---

## How to Use This

When reviewing any PM artifact:

1. Identify the artifact type and check both universal smells and type-specific smells.
2. For each smell found, name it specifically — don't just say "this needs work."
3. Point to the exact section where the smell appears.
4. Explain the risk — what goes wrong if this isn't fixed?
5. Suggest what a fix looks like — make the feedback actionable.

Prioritize by impact. A missing "why" is more fundamental than a missing edge case. A risk buried in a status update matters more than imperfect formatting. Flag the structural issues first.
