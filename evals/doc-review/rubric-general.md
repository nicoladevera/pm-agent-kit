# Evaluation Rubric — doc-review (General Document)

**Target input:** `evals/doc-review/sample-general-01.md`
**Skill under test:** `skills/doc-review/SKILL.md`
**Purpose:** Determine whether `doc-review` correctly classifies the document as a General Document, names the subtype, applies general quality criteria (not PRD criteria), catches planted weaknesses, and avoids false positives on intentional strengths.

---

## Type Detection Check

The review must correctly identify this as a **General Document (GTM Plan)**, not a PRD, project brief, or tech spec.

Signals the skill should detect:
- No problem statement / success metrics structure (not a PRD)
- No acceptance criteria or Given/When/Then (not a ticket)
- Not a brief or early-stage exploration — this is a structured execution plan (not a project brief)
- Not describing system architecture or implementation approach (not a tech spec)
- Has channel strategy, pricing, timeline, and launch phases — this is a go-to-market plan

**Fail:** If the skill identifies this as a PRD because it has a product description and pricing. The document describes *how to bring a product to market*, not *what to build*. If it's classified as a project brief, that's also wrong — this is too structured and execution-oriented for a brief.

---

## Planted Issues

The sample GTM plan contains four deliberate weaknesses. The review should detect all of them.

| # | Issue | Must Catch? | What a good detection looks like |
|---|-------|-------------|----------------------------------|
| 1 | **No stated audience or purpose** — The document never says who it's for or what the reader should do with it. Is this for the exec team to approve the launch? For marketing to execute? For sales to prepare? The reader has to guess. There's no "Purpose" section, no framing of what decision this document supports, and no indication of what happens after someone reads it. | Yes | Names the absence of audience and purpose explicitly. Should note that without knowing who the document is for, it's impossible to judge whether the level of detail is right. Should point out that a GTM plan supporting an approval decision looks different from one enabling execution. |
| 2 | **Key claims without evidence** — The document asserts that "our ICP is ready for a premium tier" implicitly (via the three Growth accounts who asked) and states competitor pricing ("$650–$1,100/mo based on public pricing pages") without linking to sources. The claim that "top 15% by usage are generating 40% of support tickets" has no citation. These are consequential claims that drive the pricing and positioning strategy — they need sourcing. | Yes | Identifies at least two unsupported claims and explains why they matter. Should distinguish between claims that are plausible but unsourced (the support ticket stat likely comes from internal data but isn't cited) and claims that are harder to verify (competitor pricing). Should recommend adding source links or data references. |
| 3 | **No channel prioritization or sequencing** — The Channel Strategy section lists five channels but doesn't prioritize them. Which channels are highest-leverage for launch? Where should the team concentrate resources if not everything can be fully activated by GA? The channels are listed as equals, but they're not — direct sales outreach to existing Growth accounts is likely the highest-conversion channel, while content marketing is a slow burn. A GTM plan without prioritization leaves the team spreading effort evenly when they should be concentrating it. | Yes | Names the absence of prioritization or sequencing across channels. Should point to the five-channel list and note that resource allocation is implicit at best. Should recommend ranking channels by expected impact or at minimum identifying the primary and secondary channels for launch. |
| 4 | **No next steps, owners, or post-read action** — The document ends with a Risks section but never states what happens next. Who owns each channel? Who's responsible for the beta? Who makes the call if beta feedback requires a delay? The Timeline section lists phases but not owners. A GTM plan that doesn't drive action is a strategy doc that forgot to be useful. | Yes | Identifies the absence of owners across timeline phases and channels. Should note that the Risks section names mitigations ("hire two additional support engineers") without naming who owns the hiring. Should recommend adding an owners/RACI section or at minimum naming a DRI for the launch. |

---

## Intentional Strengths

The sample GTM plan also contains sections that are deliberately well-done. The review should recognize these, not flag them as problems.

| Section | Why it's strong |
|---------|----------------|
| **Market Context** | Specific and well-grounded. Names competitors by name, cites concrete signals (deal review observations, support ticket patterns, direct customer requests), and frames the market gap clearly. The reader understands why Apex Pro exists and why now. This section does the "why" work that the rest of the document builds on. |
| **Pricing** | Shows the work. Three options evaluated with trade-offs named. The recommended option has clear rationale — competitive anchoring, upsell path, willingness-to-pay segmentation. The tier breakdown (base vs. plus) maps to specific team sizes with a logic the reader can follow. |

**False positive check:** If the review criticizes the Market Context section as lacking evidence or the Pricing section as insufficiently justified, that's a false positive. Both sections are among the strongest in the document.

---

## Criteria Application Check

The review must use the six general quality dimensions from `references/quality-criteria-general-document.md`, not PRD criteria.

**Pass:** The review evaluates against Purpose Clarity, Audience Fit, Logical Structure, Completeness Relative to Intent, Actionability, and Evidence and Grounding. The assessment is grounded in what a GTM plan needs to accomplish, not what a PRD needs to contain.

**Fail:** The review flags missing success metrics, acceptance criteria, or a problem statement as gaps. These are PRD criteria, not general document criteria. A GTM plan doesn't need acceptance criteria — it needs channel prioritization and launch sequencing.

---

## Context Note Check

The review's context note must:
1. State that the document was classified as General Document (GTM Plan)
2. Note that general quality dimensions were used rather than type-specific criteria
3. State which company context files were loaded, absent, or stub-level

**Bonus (not required for pass):** The context note suggests re-running as a specialized type if the document might actually be one — and correctly notes that this document is not a candidate for any of the four specialized types.

---

## Quality Checks

### Specificity
Does the review engage with the specific content of this GTM plan, or does it produce generic feedback that could apply to any document?

**Pass:** Feedback references specific sections — the Channel Strategy list, the Pricing table, the Timeline phases — and names what's working or missing in each. **Fail:** Feedback is abstract ("the document could benefit from more detail") without pointing to where.

### Calibration
Does the review evaluate this as a GTM plan, not as a generic "document"?

**Pass:** The review understands that a GTM plan's job is to align a team on how to bring a product to market, and evaluates completeness, structure, and actionability through that lens. **Fail:** The review applies a generic checklist without accounting for what a GTM plan specifically needs.

### Prioritization
Are the issues ranked by importance?

**Pass:** The most fundamental issues (missing purpose/audience, missing owners) are listed before secondary ones (missing channel prioritization, unsourced claims). **Fail:** Issues are listed in the order they appear in the document rather than by impact.

---

## Overall Assessment

**Pass threshold:** Correctly classifies as General Document (GTM Plan), catches all 4 planted issues with specific references to the document, produces zero false positives on intentional strengths (Market Context and Pricing), applies general quality dimensions rather than PRD criteria, and includes an appropriate context note about general criteria usage.
