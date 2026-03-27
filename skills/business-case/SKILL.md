---
skill: business-case
type: Generator
tier: 4
approval: draft-confirm
context-required: []
context-optional:
  - company/facts/product.md
  - company/facts/team.md
  - company/norms/decisions.md
degradation: proceed-with-caveat
---

# business-case

Build the argument for or against an initiative: problem, impact sizing, proposed solution, cost, risks, alternatives considered, recommendation. The business case earns the PRD — it argues whether to invest at all, not what to build. Opportunity sizing is the analytical core; a structured stress test — premortem, blindspot check, and conviction assessment — pressure-tests the argument before it leaves the room.

---

## What It Accepts

Any form of initiative context:
- A problem statement or opportunity description (structured or rough)
- Rough notes, bullet points, or a verbal download about a proposed initiative
- A Slack thread debating whether to invest in something
- An existing PRD that needs a business justification (pasted or referenced from `knowledge/prds/`)
- Market data, user research findings, or competitive signals
- A data analysis from `knowledge/data-analyses/`
- A combination of the above

The input does not need to be complete. This skill identifies what's present, sizes what it can, and flags what's missing as open items.

---

## Intake

A business case built on the wrong problem or sized with the wrong approach wastes the PM's time and produces a plausible-but-wrong argument. Confirm the foundation before building.

### Signals to Check

- **Problem or opportunity:** Is a clear problem/opportunity stated, or does the input lead with "we should build X"?
- **Available data for sizing:** Are there numbers, metrics, user counts, revenue figures — or is the input qualitative only?
- **Sizing approach signal:** Does the input suggest top-down (new market), bottom-up (existing flow improvement), or analog-based (comparable past initiative)?
- **Alternatives awareness:** Does the PM mention alternatives or competing approaches, or is only one path described?
- **Recommendation stance:** Is the PM looking for a genuine evaluate-and-recommend, or building the argument for an already-decided initiative?

### Adaptive Response

**Rich input** (problem clear, data provided, alternatives mentioned): Restate the problem and confirm the sizing approach. Example: "The opportunity is [X], I have [data signals] to work with, and I'll evaluate [alternative A] and [alternative B] alongside the primary proposal. Sizing bottom-up from the existing funnel data. Proceeding."

**Moderate input** (problem present but data sparse, or data present but problem vague): Ask up to 3 targeted questions. Examples:
- "What data do you have for sizing — existing funnel metrics, revenue numbers, user counts? Or should I construct estimates from assumptions?"
- "Are there specific alternatives you want evaluated, or should I generate the most plausible ones?"
- "Is this a genuine 'should we do this?' or a 'build the argument for this'? Either is fine — it changes the framing."

**Thin input** (a solution pitch, a vague area, or "build a business case for X"): Present a structured interpretation:

> **Here's how I'd frame this — tell me what needs adjusting:**
>
> - **Problem/opportunity:** [Translated from the input — problem-first, even if the input was solution-first]
> - **Sizing approach:** [Which approach and why, given what data seems available]
> - **Alternatives I'd evaluate:** [2-3 plausible alternatives based on the problem space]
> - **Recommendation stance:** [Genuine evaluation / Building the argument — my read based on the input]
>
> Anything off? I'll adjust before drafting.

---

## Instructions

### 1. Read the input fully

Absorb all initiative context before structuring. Understand what the PM is proposing, what problem or opportunity motivates it, what data exists, and what constraints are stated. Note what's provided and what's missing — the gaps inform the open items section.

### 2. Load reference files

Read these files:
- `references/business-case-standards.md` — Impact sizing frameworks, cost model standards, risk assessment, alternatives quality, audience calibration
- `references/decision-frameworks.md` — Options quality, reversibility assessment, recommendation standards
- `references/pm-smell-test.md` — Check for smells 1 (missing why), 5 (false precision), and 14 (options not considered)
- `references/agent-readable-output.md` — Agent Block format and shared enum vocabulary

### 3. Load company context (if available)

If `company/facts/product.md` exists and is substantive, read it for product landscape, user segments, and key metrics. This grounds impact sizing in the actual product context.

If `company/facts/team.md` exists and is substantive, read it for team structure, capacity, and stakeholder landscape. This informs the cost model and organizational risk assessment.

If `company/norms/decisions.md` exists and is substantive, read it for how the company evaluates and approves initiatives — decision criteria, approval process, and who needs to sign off.

If any of these files exist but are still stub templates, treat them as unavailable and say so in the context note.

### 4. Establish the problem or opportunity

Start with the problem, not the solution. Per the Problem-First operating heuristic from `CLAUDE.md`:

- If the PM's input leads with a solution ("we should build X"), translate back to the underlying problem or opportunity. The problem statement must stand on its own without referencing the proposed solution.
- Quantify the gap where possible: how many users are affected, what's the current cost, what's the competitive risk, what's the size of the opportunity.
- If the input doesn't contain a clear problem statement, extract one from the context and flag it for PM confirmation.

The problem statement is the foundation. If it's weak, everything downstream — impact sizing, alternatives, recommendation — is built on sand.

### 5. Size the impact

Select the appropriate sizing approach from `references/business-case-standards.md`:

- **Top-down** — for new market entry or initiatives without current usage data to extrapolate from
- **Bottom-up** — for improvements to existing flows where current data provides a projection basis
- **Analog-based** — for initiatives similar to past work where comparable results exist

For the selected approach:
- State the approach explicitly and why it was chosen
- Present a range: Conservative / Expected / Optimistic
- State all assumptions. Every number depends on something — name it.
- Include both quantitative impact (users, revenue, cost savings) and strategic value (competitive positioning, platform capability, user trust) where relevant
- If the input doesn't provide enough data to size impact precisely, state what's known, what's assumed, and what data would be needed for higher confidence

Do not present a single number as the impact estimate. A range with stated assumptions is honest. A single number is false precision.

### 6. Define the proposed solution

Describe what the initiative involves and how it addresses the problem. Keep this focused — the business case argues whether to invest, not the full specification. Include:
- What capabilities the initiative delivers
- How it addresses the problem established in step 4
- Key dependencies or prerequisites
- If an existing PRD or artifact in `knowledge/` provides more detail, reference it

### 7. Model the cost

Per `references/business-case-standards.md` cost model standards:

- **Engineering:** Design, development, QA, code review. Convert to cost if team rate information is available from company context.
- **Opportunity cost:** What doesn't get built while this is being built. Name the specific initiatives that get deprioritized or delayed.
- **Infrastructure:** One-time setup and ongoing run costs (servers, third-party services, data storage, API costs).
- **Ongoing maintenance:** Bug fixes, monitoring, dependency updates, support escalations.
- **Other:** Legal review, compliance, vendor contracts, training, documentation.

Present costs over at least 3-4 quarters (not just the initial build). Distinguish one-time from ongoing. If the input doesn't provide cost data, construct a reasonable estimate and flag all assumptions as open items the PM should validate.

### 8. Assess risks

Per the risk assessment framework in `references/business-case-standards.md`:

For each relevant risk category (execution, market, technical, adoption, organizational):
- State the risk specifically
- Assess likelihood (High / Medium / Low) and impact (High / Medium / Low)
- Define mitigation — what can be done to reduce likelihood or impact
- Note monitoring — how you'll know the risk is materializing

Connect to the reversibility assessment from `references/decision-frameworks.md`: Is this a one-way door (expensive to reverse) or a two-way door (can be rolled back cheaply)? State this explicitly — it changes how the business case should be evaluated.

### 9. Present alternatives

Per options quality standards from `references/decision-frameworks.md` and `references/business-case-standards.md`:

- Minimum **2 genuine alternatives** plus **"do nothing"**
- Each alternative: what it involves, pros, cons, trade-offs, and why it's less preferred (or not)
- No strawmen — each alternative should have at least one dimension where it's genuinely better than the recommendation
- "Do nothing" must be honestly evaluated: what stays the same, what gets worse, what risk is accepted, what resources remain available

If the PM's input mentions alternatives, include them. If not, generate plausible alternatives from the problem context — a strong business case always shows the recommendation was chosen, not assumed.

### 10. Make a recommendation

State the preferred option directly. Per recommendation standards from `references/decision-frameworks.md`:

- Name the recommended option and why
- Acknowledge what's given up (opportunity cost, risks accepted, trade-offs)
- State the confidence level and what it's based on
- Name what would change the recommendation (new data, changed constraints, market shift)

Come with a position. Don't present options and wait for someone else to think.

### 11. Stress-test the argument

Before finalizing, pressure-test the business case from three angles:

#### Premortem
*"It's 6 months from now and this initiative failed. What went wrong?"*

Generate 3-5 specific, plausible failure modes. For each:
- State the failure scenario concretely
- Check whether the risk assessment in step 8 already covers it
- If it's new, note it as a gap the PM should consider

The premortem should surface risks the structured risk assessment missed — especially organizational and adoption risks that don't fit neatly into risk categories.

#### Blindspot Check
*"What am I not seeing? What assumptions am I making that I haven't examined?"*

Identify at least 2 unexamined assumptions across these dimensions:
- Market assumptions (demand exists, timing is right, users will behave as expected)
- Technical assumptions (it can be built as described, it will perform at scale)
- Organizational assumptions (priority will hold, cross-team dependencies will be honored)
- Data assumptions (the numbers the impact sizing is built on are accurate and current)

Name the assumption and what would happen if it's wrong.

#### Conviction Test
*"On a scale of 1-10, how confident am I in this recommendation? What would change my mind?"*

- State a conviction level (1-10) with a brief rationale
- Name 2-3 specific conditions that would lower confidence significantly
- Distinguish between what's known, what's assumed, and what's hoped

The stress test should surface something new beyond what's already in the risk assessment. If it merely repeats the risk table in different words, it hasn't added value.

### 12. Run the smell test

Check for:
- **Smell 1 (Missing Why):** Does the business case establish why this initiative matters? Is the problem clear without reference to the solution? Would someone outside the team understand the motivation?
- **Smell 5 (False Precision):** Are impact estimates presented as ranges with assumptions? Or are single numbers stated with false confidence? Are timelines presented as estimates or commitments?
- **Smell 14 (Options Not Considered):** Are alternatives genuine? Is "do nothing" honestly evaluated? Is the recommendation chosen or assumed?

### 13. Populate the Agent Block

After completing the smell test, fill in the Agent Block:
- `recommendation`: the one-sentence recommendation from the header (repeat it here)
- `confidence`: the integer from the Conviction section of the Stress Test
- `primary_risk`: the risk category with the highest combined likelihood × impact from the Risk Assessment table
- `reversibility`: from the Reversibility field in Risk Assessment
- `key_assumption`: the single assumption from the Blindspot Check that, if wrong, would most change the recommendation
- `do_nothing_viable`: Yes if the Do Nothing alternative analysis shows it is a genuinely reasonable path; No if Do Nothing analysis identifies significant deterioration

### 14. Flag open items

List everything the PM needs to resolve before the business case is ready to present:
- Missing data that would improve impact sizing confidence
- Cost assumptions that need validation
- Risks that need mitigation plans
- Stakeholder alignment needed
- Decisions that the business case depends on but hasn't resolved

Open items are a feature of the business case, not a failure of it.

---

## Output Format

```markdown
## Business Case: [Initiative Name]

**Status:** Draft
**Date:** [Current date]
**Recommendation:** [One-sentence recommendation — stated up front so the reader knows where this is going]

<!-- AGENT BLOCK -->
```yaml
agent_block:
  skill: business-case
  recommendation: "[One sentence — what is recommended]"
  confidence: [1-10]
  primary_risk: [Execution / Market / Technical / Adoption / Organizational]
  reversibility: [One-way door / Two-way door]
  key_assumption: "[One sentence — the single assumption the recommendation is most sensitive to]"
  do_nothing_viable: [Yes / No]
```
<!-- /AGENT BLOCK -->

---

### Problem / Opportunity

[The problem or opportunity, stated independently from the solution. Who's affected. How large the gap is. Why it matters now. Quantified where possible.]

---

### Impact Sizing

**Approach:** [Top-down / Bottom-up / Analog-based] — [Why this approach was chosen]

| Dimension | Conservative | Expected | Optimistic | Assumptions |
|-----------|-------------|----------|------------|-------------|
| [Users affected] | [Low] | [Mid] | [High] | [What's assumed] |
| [Revenue / cost impact] | [Low] | [Mid] | [High] | [What's assumed] |
| [Strategic value] | [Qualitative assessment] | | | [Basis] |

[Narrative explanation of the sizing: what data was used, what was extrapolated, what the key assumptions are, and where confidence is highest/lowest.]

---

### Proposed Solution

[What the initiative involves. How it addresses the problem. Key capabilities. Dependencies. Reference to existing PRD or knowledge artifact if available.]

---

### Cost Model

| Cost Category | One-Time | Ongoing (Quarterly) | Notes |
|---------------|----------|---------------------|-------|
| Engineering | [Estimate] | [Maintenance] | [Assumptions] |
| Infrastructure | [Setup] | [Run cost] | |
| Opportunity cost | [What doesn't get built] | — | [Named initiatives] |
| Other | [Legal, compliance, etc.] | [Support, docs, etc.] | |

**Total estimated investment:** [Range — not a single number]
**Payback period:** [Estimated time to recoup investment, if applicable]

---

### Risk Assessment

| Risk | Category | Likelihood | Impact | Mitigation |
|------|----------|-----------|--------|------------|
| [Risk 1] | [Execution / Market / Technical / Adoption / Organizational] | [H / M / L] | [H / M / L] | [Mitigation plan] |
| [Risk 2] | ... | ... | ... | ... |

**Reversibility:** [One-way door / Two-way door] — [Why, and what that means for the decision threshold]

---

### Alternatives Considered

#### Option A: [Recommended Option]
[What it involves. Pros. Cons. Why it's preferred.]

#### Option B: [Genuine Alternative]
[What it involves. Pros. Cons. Trade-offs. Why it's less preferred — or in what scenario it would be better.]

#### Option C: [Another Alternative or Variant]
[What it involves. Pros. Cons. Trade-offs.]

#### Option D: Do Nothing
[What stays the same. What gets worse. What risk is accepted. What resources remain available for other priorities.]

---

### Recommendation

[State the preferred option directly. Name the reasoning. Acknowledge what's given up. State confidence level. Name what would change the recommendation.]

---

### Stress Test

#### Premortem
*"It's 6 months from now and this initiative failed. What went wrong?"*

1. [Failure mode 1] — [Whether risk assessment covers it. If not, what's the gap.]
2. [Failure mode 2] — ...
3. [Failure mode 3] — ...

#### Blindspot Check
*"What am I not seeing?"*

- **[Assumption category]:** [Unexamined assumption. What happens if it's wrong.]
- **[Assumption category]:** [Unexamined assumption. What happens if it's wrong.]

#### Conviction
**Confidence level:** [1-10] — [Brief rationale]
**What would lower confidence:**
- [Condition 1]
- [Condition 2]

---

### Open Items

- [Data needed to improve impact sizing confidence]
- [Cost assumptions requiring validation]
- [Stakeholder alignment needed]
- [Decisions this business case depends on but hasn't resolved]

---

### Smell Test

- **Smell 1 (Missing Why):** [Finding — or "Clear — problem established independently from solution"]
- **Smell 5 (False Precision):** [Finding — or "Clear — estimates presented as ranges with stated assumptions"]
- **Smell 14 (Options Not Considered):** [Finding — or "Clear — genuine alternatives evaluated, including do-nothing"]

> **Context note:** [State which substantive company files were loaded, which were absent, and which were stub templates. Note how missing context may have affected the quality of impact sizing, cost estimates, or risk assessment.]
```

---

## Quality Bar

- **Does the problem statement stand on its own without the solution?** The opportunity is clear, quantified, and compelling independently of the proposed initiative. Someone could read the problem section and agree it matters before seeing what's proposed.
- **Is impact sizing honest about uncertainty?** Ranges presented, assumptions stated, approach named. No single-number projections without caveats. The reader can evaluate the quality of the estimate, not just the number.
- **Are alternatives genuine?** At least one alternative that a reasonable person could prefer. "Do nothing" honestly evaluated — not dismissed in one sentence. No strawmen designed to make the recommendation look inevitable.
- **Does the cost model include opportunity cost?** Not just build cost but what doesn't get built and ongoing maintenance. Multi-quarter view. Hidden costs flagged.
- **Does the stress test surface something new?** The premortem, blindspot check, and conviction test add value beyond what's already in the risk assessment. If they just repeat the risk table in different words, they failed.
- **Would a VP read this and have enough to decide?** The business case is self-contained. The reader doesn't need a follow-up meeting to understand the argument, the evidence, the alternatives, and the recommendation.
- **Is the recommendation stated directly?** The PM has a point of view. The reasoning is transparent. Trade-offs are acknowledged. The reader knows what's being recommended and why.
