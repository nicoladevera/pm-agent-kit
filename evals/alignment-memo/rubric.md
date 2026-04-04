# Evaluation Rubric — alignment-memo (Framework: AI Adoption)

**Target input:** `evals/alignment-memo/sample-input-01.md`
**Skill under test:** `.claude/skills/alignment-memo/SKILL.md`
**Purpose:** Determine whether `alignment-memo` correctly translates a solution-first, platitude-heavy input into a problem-first framework with grounded principles, actionable depth, and a realistic adoption path — while handling missing audience and uneven organizational context.
**Coverage:** Single subtype — Framework.

---

## Problem-First Translation

The PM leads with "We should start using AI tools across the team" — a solution, not a problem. The underlying problem is scattered across the input: inconsistent adoption (some teams using tools, others not), no shared evaluation criteria, unresolved legal and IP concerns, and leadership signaling interest without follow-through.

**Good Context section:** "AI tool adoption is happening unevenly across product and engineering — the payments backend team uses Copilot, some PMs use ChatGPT informally, and a design exploration was shut down over IP concerns. There is no shared framework for evaluating which tools are appropriate, what data can be exposed, or how to scale from individual experimentation to team-level practice. Two months after the CTO's all-hands endorsement, no organizational guidance has followed."

**Bad Context section:** "AI is transforming how teams work. We should adopt AI tools to stay competitive and improve productivity." (Generic, not grounded in the org's actual situation.)

**Pass:** Context establishes the organizational gap before describing the proposed framework. References specific signals from the input (uneven adoption, design team shutdown, CTO's unfollowed statement). **Fail:** Opens with "AI is here" or "we should adopt AI tools" rather than the problem.

---

## Principle Quality

The PM provides two proto-principles: "we should be thoughtful about it" and "AI should help, not replace." These are platitudes — vague enough that no reasonable person would disagree with them. The skill must translate these into specific, grounded principles.

**Good principles (examples — the skill should produce its own, not these exactly):**

- "Start with judgment-heavy, repetitive tasks where the cost of a wrong output is low and feedback loops are fast." Grounds: the payments team's success with boilerplate generation is evidence this pattern works; the design team's IP concern shows that high-judgment creative tasks require more caution.
- "Data sensitivity determines the evaluation path, not the tool category." Grounds: the org handles financial data; the legal gap is the most critical unresolved concern; tool evaluation must start with what data flows through the tool.
- "Adoption follows demonstrated value, not mandates." Grounds: the CTO's all-hands statement changed nothing because it was enthusiasm without structure; the payments team adopted Copilot because it visibly saved time, not because they were told to.

**Bad principles:** "Be thoughtful about AI adoption." "AI should augment, not replace." "Start small and iterate." "Use AI responsibly." These could apply to any org and don't help anyone make a specific decision.

**Pass:** Each principle states a specific belief with a rationale tied to the org's reality (uneven adoption, data sensitivity, design team pushback). A reader could use the principles to make a decision about a specific tool or use case. **Fail:** Principles are platitudes that restate the PM's input without adding specificity. "Be thoughtful" survives into the output.

---

## Framework Depth

The Core Content section must provide an actual operating model — not just a list of tools to evaluate.

**What a good framework includes:**

- **Evaluation criteria or tiers:** A way to categorize tools or use cases by risk level. For example: Tier 1 (low data sensitivity, individual productivity — code completion, document drafting), Tier 2 (moderate sensitivity, team workflow integration — design tools, testing frameworks), Tier 3 (high sensitivity, customer-facing or data-processing — anything touching financial data or customer PII). Each tier has different evaluation requirements.
- **Decision logic:** For a given tool/use case, how does a team decide whether and how to adopt? What questions must be answered (data flow, IP implications, quality bar, legal review)?
- **Guardrails:** What is explicitly off-limits until specific conditions are met (e.g., no tools processing customer financial data until legal signs off)?

**What a bad framework looks like:** A list of tool categories with generic guidance ("Evaluate code generation tools for quality"). A scoring rubric template with no actual criteria. High-level categories without decision logic.

**Pass:** A reader could use the framework to make a specific decision about a specific tool — e.g., "Should the QA team use AI for test generation?" and know which tier it falls into, what evaluation is required, and what approval path to follow. **Fail:** The framework is too abstract to apply to a concrete case without a follow-up conversation.

---

## Application Realism

The PM provides no adoption path. The skill must construct one that accounts for the org's reality: existing informal adoption (payments team, individual PMs), resistance in some areas (design VP), unresolved legal questions, and no allocated budget.

**Good Application section:**

- Acknowledges what's already working (payments team's Copilot adoption, PM document drafting) and builds on it rather than proposing a clean-slate process
- Proposes a phased approach that accounts for real constraints: Phase 1 might be formalizing what's already happening (Tier 1 tools) while legal reviews data handling for higher-tier tools
- Names who owns each phase — who runs the legal review, who owns the tool evaluation for each tier, who tracks adoption and reports back
- Defines what success looks like at each phase before expanding scope

**Bad Application section:** "Roll out the framework across the org" or "Share this document with all teams" with no mechanics for how adoption actually happens.

**Pass:** Names concrete adoption steps, acknowledges existing practices as a foundation, accounts for stated constraints (legal gap, no budget, design team resistance), and names owners or ownership roles. **Fail:** Generic "implement this framework" without mechanics.

---

## Audience Calibration

The PM does not specify an audience. The input says "I want something we can circulate that helps everyone understand how to think about this" — which is too vague to calibrate to.

**Pass:** The skill either asks the PM to clarify the audience (acceptable) or makes a reasonable assumption and states it explicitly (e.g., "This is addressed to the product and engineering org — PMs, engineers, and design leads — for alignment on shared AI adoption practices. Leadership review may be needed for budget and legal decisions."). The tone and depth match the declared audience. **Fail:** No audience named or inferred. The document reads as generically written with no clear reader.

---

## Output Format Compliance

**Pass:** All six sections present (Executive Summary, Context, Principles, Core Content, Application, Ask). Agent Block populated with correct field types. Context note present and honest about company context availability. Executive Summary is self-contained — a reader who stops after the summary knows what the framework proposes, why, and what's being asked.

**Fail:** Missing sections. Agent Block omitted or incomplete. No context note. Executive Summary requires reading the full document to understand the point.

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| Problem-first translation | 15% | Context establishes organizational gap before describing the framework; references specific input signals (uneven adoption, design shutdown, CTO statement) |
| Principle quality | 20% | Each principle is specific, grounded in the org's reality, and usable for decision-making; no platitudes survive from the input |
| Framework depth | 20% | Provides an operating model with tiers or evaluation criteria, decision logic, and guardrails; a reader can apply it to a specific tool/use case |
| Application realism | 15% | Names concrete adoption steps; builds on existing practices; accounts for stated constraints; names owners |
| Audience calibration | 15% | Audience named or inferred and stated; tone and depth match the audience |
| Output format compliance | 15% | All sections present; Agent Block populated; context note included; Executive Summary self-contained |
