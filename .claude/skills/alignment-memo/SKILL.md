---
name: alignment-memo
description: Drafts internal alignment artifacts — frameworks, standards, operating memos, and lightweight program proposals. Use when asked to "draft a framework", "write a memo on how we should think about X", "create a standard for Y", "propose a hackathon", or "write an operating memo".
metadata:
  type: Generator
  tier: 4
  approval: draft-confirm
  context-required: []
  context-optional:
    - company/facts/product.md
    - company/facts/team.md
    - company/norms/communication.md
  degradation: proceed-with-caveat
---

# alignment-memo

Draft internal alignment artifacts that define how a team should think or operate — frameworks, standards, operating memos, and program proposals. These documents sit upstream of feature work: they codify principles, establish norms, or propose programs that shape how the team builds, not what it builds. The artifact earns adoption through clarity and specificity, not authority.

This skill covers the class of PM work that isn't a PRD, business case, or presentation — but still requires structured thinking, audience calibration, and a clear ask. An AI adoption framework, a data requirements standard, a hackathon proposal, a team operating guide. The common thread is internal alignment: the document exists to get people on the same page about how to work.

---

## What It Accepts

Any form of input that needs to become a structured internal alignment document:
- Rough notes, bullet points, or a verbal download about a practice, standard, or program
- A problem statement about an organizational gap (inconsistent practices, missing standards, cultural initiative)
- A request to codify something the team already does informally
- An existing document or Slack thread that needs to be turned into a formal memo
- A combination of the above

The input provides the substance. The skill provides the structure and audience calibration.

---

## Intake

An alignment memo built on a vague ask or addressed to the wrong audience wastes the PM's credibility. These documents only work if the reader knows why they're reading, what's being proposed, and what's expected of them. Confirm the shape before drafting.

### Signals to Check

- **Artifact subtype:** What kind of document is this? A framework (how we think about X), a standard (what good looks like for Y), a proposal (let's do Z), or an operating guide (how we do W)?
- **Audience:** Who reads this and what do they do with it? Leadership (approve or endorse), the team (adopt), cross-functional partners (align), or some combination?
- **Ask type:** What is the memo trying to achieve? Alignment (shared understanding), adoption (behavior change), approval (a decision), or awareness (informing)?

### Adaptive Response

**Rich input** (subtype, audience, and ask are clear or inferable from context): Restate understanding in 1-2 sentences and proceed. Example: "This is a framework for AI adoption aimed at the product and engineering org, seeking alignment on how teams should evaluate and adopt AI tools. Proceeding."

**Moderate input** (some signals present, some gaps): Ask up to 3 targeted questions. Examples:
- "Who is the primary audience for this — leadership for approval, the team for adoption, or cross-functional partners for alignment?"
- "Is this establishing a new standard (prescriptive, here's what you must do), proposing a framework (directional, here's how to think about it), or proposing a program (let's run this)?"
- "What's the ask — do you need people to approve this, adopt it, or just be aware of it?"

**Thin input** (a topic or vague request like "write something about data requirements"): Present a structured interpretation:

> **Here's how I'd frame this — tell me what needs adjusting:**
>
> - **Artifact subtype:** [Framework / Standard / Proposal / Operating guide — inferred from the input]
> - **Audience:** [Who reads this and what they do with it]
> - **Ask type:** [Alignment / Adoption / Approval / Awareness]
> - **Core problem:** [What gap this memo addresses — translated problem-first]
>
> Anything off? I'll adjust before drafting.

---

## Instructions

### 1. Read the input fully

Absorb all context before structuring. Understand what the PM wants to establish, what gap it addresses, who needs to read it, and what existing practices or context should be built on rather than ignored. Note what's provided and what's missing.

### 2. Load reference files

Read these files:
- `references/quality-criteria-general-document.md` — Six universal quality dimensions (purpose clarity, audience fit, logical structure, completeness, actionability, evidence and grounding)
- `references/communication-quality.md` — Quality criteria for PM communications: lead with the answer, risk surfaced, audience calibration, structured naturally
- `references/audience-registers.md` — Per-audience communication registers: tone, depth, and framing by stakeholder type
- `references/pm-philosophy.md` — Operating heuristics, especially Problem-First, Data Requirements Are Product Requirements, and Clarity Is the Deliverable
- `references/agent-readable-output.md` — Agent Block format and shared enum vocabulary

### 3. Load company context (if available)

If `company/facts/product.md` exists and is substantive, read it for product landscape and team focus areas. This grounds the memo in the actual organizational context rather than generic advice.

If `company/facts/team.md` exists and is substantive, read it for team structure, roles, and working patterns. This informs who owns what in the Application section and ensures the memo addresses real organizational dynamics.

If `company/norms/communication.md` exists and is substantive, read it for how the company communicates internally — tone, formats, channels. This helps calibrate the memo to fit the org's existing communication patterns.

If any of these files exist but are still stub templates, treat them as unavailable and say so in the context note.

### 4. Establish the problem or gap

Start with why this memo needs to exist, not what it proposes. Per the Problem-First operating heuristic from `CLAUDE.md`:

- If the PM's input leads with a solution ("we should start using AI tools"), translate back to the underlying problem or gap (inconsistent practices, no shared mental model, organizational risk from uncoordinated adoption).
- Name the current state honestly: what's happening today, what's not working, what changed to make this memo necessary now.
- If existing practices are mentioned (some teams already doing something informally), acknowledge them as a foundation to build on rather than proposing a clean-slate replacement.

### 5. Calibrate structure to artifact subtype

The structural spine is consistent across subtypes, but section weight and emphasis shift:

| Subtype | Principles | Core Content | Application | Ask |
|---------|-----------|-------------|-------------|-----|
| **Framework** | Heavy — the mental model rests on these | The model, tiers, decision criteria | How to apply the framework to specific decisions | Alignment or endorsement |
| **Standard** | Moderate — ground the "why" behind requirements | Stage-by-stage or dimension-by-dimension requirements | Integration into existing workflows, enforcement points | Adoption — specific behavior changes |
| **Proposal** | Light — guiding values for the program | Plan, logistics, mechanics, timeline | Participation model, success criteria | Approval — decision requested |
| **Operating guide** | Light to moderate — the beliefs behind the practice | Step-by-step or situation-by-situation guidance | Where this fits in existing ceremonies and workflows | Awareness and adoption |

Adjust section depth accordingly. A framework with thin Principles has no foundation. A standard with no Application section is an aspiration, not a standard. A proposal with no clear Ask wastes the reader's time.

### 6. Draft the memo

Write each section following the output format below.

**Executive Summary:** State the point in 2-4 sentences. A reader who stops here should know what the memo proposes, why, and what's being asked. Per `references/communication-quality.md` criterion 1 — lead with the answer.

**Context:** Why this, why now. Establish the gap, the current state, what changed. If the PM provided specific examples of the problem (failed launches, inconsistent practices, organizational friction), use them — concrete evidence is more compelling than abstract claims. Per `references/pm-philosophy.md` — Encyclopedic Context Earns Trust.

**Principles:** The beliefs that underpin the framework, standard, or proposal. Required for frameworks and standards. Recommended for proposals. Omit only for operating guides where the principles are self-evident from the content.

Each principle should be:
- Stated as a clear belief, not a platitude ("Data requirements belong in the PRD, not in a post-launch ticket" — not "Data is important")
- Grounded with a brief rationale tied to the org's reality or the problem established in Context
- Specific enough that someone could disagree with it — if a principle is so generic that no reasonable person would contest it, it's not doing work

**Core Content:** The substance of the memo. Section title adapts to the subtype:
- Framework: "Framework" or "[Topic] Framework" — the model, tiers, evaluation criteria, decision logic
- Standard: "Standard" or "[Topic] Requirements" — the expectations by stage, dimension, or role
- Proposal: "Proposal" or "[Program Name]" — the plan, format, logistics, timeline
- Operating guide: "Guide" or "Process" — the step-by-step or situation-by-situation guidance

This section must have enough depth that a reader can act on it without a follow-up conversation. A framework with only high-level categories fails. A standard with no specifics per stage fails. A proposal with no logistics fails.

**Application:** How this becomes real. Name specific integration points — which workflows, ceremonies, templates, or review gates are affected. Name who owns what. If the memo builds on existing informal practices, say so: "Some PMs already do X — this memo formalizes it and extends it to Y." If adoption is phased, describe the phases and criteria for progression.

**Ask:** What needs to happen next. Calibrate to the ask type:
- Approval: Name the decision, the decider, and the timeline
- Adoption: Name the specific behavior changes expected and when they take effect
- Alignment: Name what shared understanding the reader should walk away with
- Awareness: Name the key takeaways explicitly rather than hoping the reader synthesizes them

### 7. Self-review against quality dimensions

Before finalizing, check the draft against the six dimensions from `references/quality-criteria-general-document.md`:

1. **Purpose clarity:** Can you state in one sentence what this document is for?
2. **Audience fit:** Is the content, detail level, and tone right for the declared audience?
3. **Logical structure:** Does each section follow naturally from the previous one?
4. **Completeness relative to intent:** Does the memo cover what it needs to, given its purpose?
5. **Actionability:** Does the reader know what to do after reading?
6. **Evidence and grounding:** Are claims supported? Are assumptions labeled?

If any dimension is weak, revise before finalizing.

### 8. Populate the Agent Block

After completing the self-review, fill in the Agent Block:
- `artifact_subtype`: Framework / Standard / Proposal / Operating Guide
- `audience`: the primary audience for the memo
- `ask_type`: Alignment / Adoption / Approval / Awareness
- `principle_count`: number of principles stated (0 if section omitted)
- `word_count`: approximate word count of the full memo

---

## Output Format

````markdown
## [Title]

**Status:** Draft
**Date:** [Current date]
**Audience:** [Primary audience]
**Ask:** [One sentence — what this memo is asking of the reader]

<!-- AGENT BLOCK -->
```yaml
agent_block:
  skill: alignment-memo
  artifact_subtype: "[Framework / Standard / Proposal / Operating Guide]"
  audience: "[Primary audience description]"
  ask_type: "[Alignment / Adoption / Approval / Awareness]"
  principle_count: [integer]
  word_count: [integer]
```
<!-- /AGENT BLOCK -->

---

### Executive Summary

[The point, up front. What this document proposes or establishes and why it matters. 2-4 sentences. A reader who stops here should know the memo's purpose, the gap it addresses, and what's being asked.]

---

### Context

[Why this, why now. Current state — what's happening today. What changed or what gap exists. Concrete examples where available. What motivated this memo.]

---

### Principles

[The beliefs that underpin the framework, standard, or proposal. Each principle stated as a clear belief with a brief grounding rationale. Omit this section only for operating guides where principles are self-evident.]

1. **[Principle name]** — [Belief statement. Why this matters, grounded in the org's reality.]
2. **[Principle name]** — [Belief statement. Rationale.]
3. **[Principle name]** — [Belief statement. Rationale.]

---

### [Core Content — title adapts to subtype]

[The substance. Depth and structure adapt to the subtype:
- Framework: model, tiers, evaluation criteria, decision logic
- Standard: requirements by stage, dimension, or role
- Proposal: plan, format, logistics, timeline, mechanics
- Operating guide: step-by-step or situation-by-situation guidance]

---

### Application

[How this becomes real. Which workflows, ceremonies, templates, or review gates change. Who owns what. Integration with existing practices. Phased rollout if applicable.]

---

### Ask

[What happens next. Calibrated to ask type:
- Approval: decision requested, decider named, timeline
- Adoption: specific behavior changes, effective date
- Alignment: shared understanding expected
- Awareness: key takeaways stated explicitly]

> **Context note:** [State which substantive company files were loaded, which were absent, and which were stub templates. Note how missing context may have affected the quality of the memo — e.g., organizational structure assumptions, communication norms inferred rather than loaded.]
````

---

## Quality Bar

- **Does the Executive Summary stand alone?** A reader who only reads the summary knows what the memo proposes, why, and what's expected of them. No follow-up needed to understand the point.
- **Is the Context problem-first?** The gap or need is established before the solution is described. The reader understands why this memo exists before being told what it says.
- **Are the Principles grounded, not generic?** Each principle states a belief that someone could reasonably disagree with, and grounds it in the org's reality. "Be thoughtful" is not a principle. "Start with tasks where the cost of a wrong output is low and feedback loops are fast" is.
- **Does the Core Content have enough depth to act on?** A framework provides decision criteria, not just categories. A standard specifies expectations per stage, not just "include data." A proposal includes logistics, not just the idea. The reader can use this section without a follow-up conversation.
- **Is the Application section realistic?** It names specific integration points, specific owners, and specific changes to existing workflows. It builds on what already works rather than proposing a clean-slate replacement of existing practices.
- **Is the Ask specific?** Named owners, dates, decisions, or behavior changes — not "please review and let me know your thoughts." The reader knows exactly what's being asked of them.
- **Does it pass the six dimensions in `quality-criteria-general-document.md`?** Purpose clarity, audience fit, logical structure, completeness relative to intent, actionability, evidence and grounding.
- **Would this memo earn adoption on its own merits?** The document is compelling enough that people would follow it because it's clearly right, not because someone told them to. Influence through execution, not authority.

---

## Save

After producing the artifact, write it to `knowledge/memos/` using the naming convention: `YYYY-MM-DD-descriptive-slug.md`, where the date is the creation date and the slug describes the topic. Report the saved file path in the conversation.
