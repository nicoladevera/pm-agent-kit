# Evaluation Rubric — one-pager (From Scratch: Hackathon Proposal)

**Target input:** `evals/one-pager/sample-input-01.md`
**Skill under test:** `.claude/skills/one-pager/SKILL.md`
**Purpose:** Determine whether `one-pager` correctly handles a from-scratch scenario with thin input, translates a solution-first pitch into a problem-first argument, enforces the one-page constraint, calibrates for a delivery-focused VP audience, and includes the right conditional sections for a budget/approval ask.
**Coverage:** From-scratch workflow. Tests thin-input intake, problem-first translation, VP audience calibration, one-page constraint enforcement, and conditional section logic for a Fund ask.

---

## Intake Behavior

The input provides the audience (VP of Engineering) and the ask (approve + allocate budget), but the substance is thin — bullet points, half-formed goals, no data. The skill should recognize this as moderate-to-thin input and either proceed with a brief confirmation or present a structured interpretation.

The PM leads with "we should run a hackathon" — a solution, not a problem. The skill should identify the underlying problem before drafting.

**Pass:** Skill either (a) restates the argument problem-first and confirms before drafting, or (b) asks 1-2 targeted questions about the strongest gap (likely: what specific outcomes does the VP care about?). Does not proceed directly to drafting without any confirmation. **Fail:** Drafts immediately from the solution-first framing without translating to the underlying problem.

---

## Problem-First Translation

The PM's input is entirely solution-first: "we should run a hackathon" with reasons bolted on. The skill must translate this into a problem statement that stands independently from the hackathon proposal.

**Good Problem / Opportunity section:** "Engineering morale and creative engagement have declined since the Q1 reorg. The team is locked into sprint cycles with no structured outlet for experimentation — two engineers are building product-relevant prototypes on personal time because there's no sanctioned path to explore them. Meanwhile, leadership messaging about innovation hasn't been backed by any concrete program."

**Bad Problem / Opportunity section:** "We should run a hackathon to boost morale and encourage innovation." (This is the solution restated as a problem.)

**Pass:** Problem framed as an organizational gap (morale, innovation stagnation, no experimentation outlet) — not as "we need a hackathon." The hackathon appears in the Proposed Approach section, not the Problem section. **Fail:** Problem section is just "we should do a hackathon" reworded, or the problem is generic ("morale is important").

---

## Ask Placement

The one-pager's defining structural choice: the ask goes first, before the problem, before the approach.

**Pass:** The ask is stated in the first two sentences of the document body (after the header metadata). The reader knows they're being asked to approve a 2-day hackathon and allocate $3-5K before reading any background. **Fail:** The ask is buried after the problem statement or approach description. The reader has to read 200+ words before knowing what they're being asked to do.

---

## VP Audience Calibration

The PM explicitly flags that the VP is "very delivery-focused" and "won't love the idea of losing two days of sprint velocity." The skill must calibrate for the Leadership / Stakeholders register from `references/audience-registers.md`.

**Critical tests:**

**The sprint velocity concern must be addressed proactively.** Per the audience register: "Anticipate their questions — lead with what's NOT the problem before naming what is." The one-pager should preemptively address the delivery impact: Thursday-Friday timing minimizes sprint disruption, the velocity "cost" is bounded to 2 days, and past hackathons at comparable companies have produced shippable features.

**Every risk must be paired with a mitigation.** The VP register requires this. "We've never done this before" is not acceptable as a standalone risk. It needs: "We've never done this before — we'll run a lightweight post-event retro and commit to iterating the format if it doesn't produce value."

**Framing should be strategic, not tactical.** The VP doesn't need to know about swag and food logistics. She needs to know the investment, the expected return, and how it connects to the team health and innovation signals she's already hearing about.

**Pass:** Sprint velocity addressed proactively. Every risk paired with mitigation. Strategic framing (not operational details). Register matches Leadership/Stakeholders. **Fail:** Sprint velocity concern not addressed. Risks listed without mitigations. Operational details (food, swag) included. Register too casual or too tactical.

---

## Conditional Section Inclusion

The ask is "approve and allocate budget" — this maps to the Fund ask type. Per the skill's instructions:

| Expected Section | Should Appear? | Reason |
|-----------------|---------------|--------|
| Cost / Resource Ask | Yes | This is a budget request — the VP needs to know the number |
| Success Criteria | Yes | The VP is approving something — she needs to know how to evaluate whether it worked |
| Impact / Sizing | No | Not a prioritization ask |
| Alternatives Considered | No | Not choosing between options |

**Pass:** Cost / Resource Ask section present with the $3-5K estimate. Success Criteria section present with 2-3 measurable outcomes (not "it went well"). Impact / Sizing and Alternatives Considered sections absent. **Fail:** Missing Cost / Resource Ask for a budget request. Missing Success Criteria for an approval ask. Unnecessary sections included.

---

## Why Now Quality

The PM provides a genuine timing signal: morale is low since the reorg, and there's a big launch in 6 weeks. The skill should turn the launch into a timing argument rather than a blocker.

**Good Why Now:** "The post-launch window — 6-8 weeks from now — is the natural inflection point. The team will have shipped a major milestone, energy will be high, and the sprint pressure will temporarily ease. Running the hackathon then capitalizes on momentum rather than competing with it."

**Bad Why Now:** "Now is a good time because morale is low." (Vague.) Or: "We should wait until after the launch." (The PM didn't ask whether to do it — they asked for a pitch.)

**Pass:** Why Now section presents a specific, real timing argument grounded in the team's actual situation. Not manufactured urgency, but genuine timing logic. **Fail:** Generic ("innovation is always timely") or dismissive of the launch timing constraint.

---

## One-Page Constraint

The most important structural test. The output must be genuinely one page.

**Pass:** Content (excluding Agent Block and context note) is 400-600 words. Every sentence is load-bearing — removing any single sentence would weaken the case. No setup paragraphs, no throat-clearing, no "as you may know" framing. No operational details that don't serve the ask (food menus, swag options, room booking logistics). **Fail:** Over 600 words. Generic filler sentences present. Operational details that the VP doesn't need.

---

## Agent Block and Output Format

**Pass:** Agent Block present with all required fields populated correctly:
- `ask_type`: Fund (or Approve — both are defensible for this input)
- `audience`: VP of Engineering (or equivalent)
- `source_artifact`: original
- `confidence`: an integer that reflects the thin input (likely 5-7 range)
- `time_sensitivity`: Near-term or Strategic

Smell test section present with findings for smells 1, 4, 5. Context note present. Output follows the template structure from the skill definition.

**Fail:** Agent Block missing or fields incorrectly populated. Smell test absent. Format deviates from the skill's output template.

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| Problem-first translation | 15% | Problem stated independently from hackathon solution; organizational gap established |
| Ask placement | 15% | Ask in the first two sentences of the document body |
| VP audience calibration | 20% | Sprint velocity addressed proactively; risks paired with mitigations; strategic framing |
| Conditional section logic | 10% | Cost/Resource and Success Criteria present; Impact/Sizing and Alternatives absent |
| Why Now quality | 15% | Specific timing argument grounded in team's situation; not generic or manufactured |
| One-page constraint | 15% | 400-600 words; every sentence load-bearing; no operational filler |
| Output format compliance | 10% | Agent Block populated; smell test present; context note included; template followed |
