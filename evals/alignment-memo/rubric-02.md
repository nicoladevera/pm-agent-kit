# Evaluation Rubric — alignment-memo (Standard: Data Requirements)

**Target input:** `evals/alignment-memo/sample-input-02.md`
**Skill under test:** `skills/alignment-memo/SKILL.md`
**Purpose:** Determine whether `alignment-memo` preserves concrete failure examples as motivation, produces grounded principles (not generic "data is important"), maps requirements to specific SDLC stages with role-specific expectations, and proposes realistic adoption mechanisms that build on existing partial practices.
**Coverage:** Single subtype — Standard.

---

## Concrete Examples Preserved

The PM provides four specific launch failures where missing data requirements caused real damage: subscription tiers (no measurement for 3 weeks), mobile checkout (inconsistent event schemas), referral program (ad hoc tracking, wrong events), and fraud detection (missing data warehouse fields). These are the motivation for the standard.

**Good Context section:** Uses at least 2-3 of these examples directly to establish why the standard is needed. The examples are specific enough that a reader who wasn't there can understand the cost of missing data requirements. The Context section makes the reader feel the pain before presenting the solution.

**Bad Context section:** "Data requirements are often an afterthought in our SDLC, leading to measurement gaps and post-launch rework." (Generic framing that wastes the four concrete examples the PM provided.)

**Pass:** At least 2 concrete examples from the input appear in Context with enough specificity that a reader understands the cost (3 weeks blind, 2 sprints of reconciliation, 3-week project slip). **Fail:** Generic "data is important" or "we've had issues" framing that doesn't use the provided evidence.

---

## Principle Quality

The PM's request echoes a core operating heuristic — "Data Requirements Are Product Requirements" — without naming it explicitly. The skill should draw on this philosophy naturally. The principles should articulate why data requirements matter with specificity grounded in the org's experience.

**Good principles (examples — the skill should produce its own):**

- "Data requirements are product requirements — they belong in the PRD, not in a post-launch ticket." Grounds: the referral program had clear success metrics in the PRD but nobody speced the events to measure them, so the metrics were unverifiable at launch.
- "Data schema decisions are architecture decisions — changing them after launch is rework, not iteration." Grounds: the mobile checkout redesign shipped with inconsistent schemas, and the 2-sprint reconciliation effort was a direct consequence of treating schemas as an afterthought.
- "The data team is a design partner, not a post-launch service desk." Grounds: Marcus's observation that PRD involvement would save 30% of his time — data expertise applied upstream prevents downstream fires.

**Bad principles:** "Data is important for decision-making." "We should think about analytics earlier." "Measurement matters." These add nothing the reader doesn't already know.

**Pass:** Principles are specific, grounded in the org's actual failure patterns, and state beliefs that reshape how people think about data in the SDLC. **Fail:** Generic statements about data's importance.

---

## SDLC Integration Depth

The Core Content section must map data requirements to specific SDLC stages with concrete expectations. This is the highest-weighted dimension because the PM explicitly asked for integration "into every stage of how we build software."

**What a good standard covers (at minimum):**

| Stage | Expected Data Artifacts | Who Owns |
|-------|------------------------|----------|
| **Discovery / Problem Definition** | Data availability check — do we have the data we need? Are there warehouse gaps? | PM + Data Analyst |
| **Spec / PRD** | Success metrics with event schemas, data source identification, dashboard requirements, data dependencies called out | PM (authors), Data Analyst (reviews) |
| **Design Review** | Confirm instrumentation points in UX flows — what user actions trigger which events | PM + Design + Data |
| **Build** | Event implementation matching spec'd schemas, data pipeline setup if needed | Engineering + Data Engineering |
| **QA** | Analytics QA — verify events fire correctly, schemas match spec, data lands in the right place | QA + Data Analyst |
| **Launch** | Dashboard live, monitoring in place, data reconciliation check (do the numbers make sense?) | PM + Data |
| **Post-Launch** | Measurement review against success metrics, data quality audit | PM + Data Analyst |

**What a bad standard looks like:** "Include data requirements in your PRD" without specifying what that means at each stage, who does what, or how to verify compliance.

**Pass:** Requirements mapped to at least 4 distinct SDLC stages. Each stage names the expected artifacts and the responsible role. A PM or engineer reading this knows exactly what data work is expected of them at each stage. **Fail:** General guidance about "including data in the process" without stage-by-stage specificity.

---

## Multi-Audience Actionability

The PM specifies four audiences: PMs, engineers, data analysts, and QA. The standard must be actionable for each role, not just PMs.

**What good multi-audience handling looks like:**

- **PMs:** Own data requirements in the PRD — success metrics, event schemas, dashboard specs. Invite data analyst to PRD review.
- **Engineers:** Implement events matching the spec'd schemas. Flag data dependencies during technical design. Don't add ad hoc tracking without coordinating with the data team.
- **Data Analysts:** Review PRDs for data completeness. Validate schemas. Build dashboards before launch, not after. Participate in launch readiness check.
- **QA:** Add analytics verification to the test plan. Verify events fire with correct schemas. Treat analytics bugs with the same severity as functional bugs.

**Pass:** Role-specific expectations are named for at least 3 of the 4 audiences. A person in each role could read the standard and know what's expected of them specifically — not just "the team should do data better." **Fail:** Everything framed as "the team should" or responsibilities only defined for PMs.

---

## Application and Adoption Realism

The PM provides a critical signal: "Some PMs already include event schemas in their PRDs — Aisha on the payments team is great about it. But it's inconsistent." The skill should build on existing good practice rather than proposing a new process that ignores what's already working.

The PM also signals real constraints: no data section in the PRD template, no analytics QA step, no formal checkpoint. And an explicit request: "prescriptive enough that people actually follow it, but not so bureaucratic that it slows us down."

**Good Application section:**

- Acknowledges Aisha's existing practice as the model to scale: "The payments team already includes event schemas in PRDs — this standard formalizes that practice and extends it to every product team."
- Names specific enforcement mechanisms that integrate into existing workflows: add a data requirements section to the PRD template, add a data analyst to the PRD review checklist, add an analytics QA step to the test plan, add a data readiness gate to the launch checklist.
- Proposes a credible rollout: start with new PRDs immediately (template change), phase in analytics QA over the next sprint cycle, train QA on analytics verification by a specific timeframe.
- Balances prescription with pragmatism per the PM's request — the standard is clear about what's required without creating a new approval committee.

**Bad Application section:** "Everyone should follow this standard" or "Share with all teams and discuss in the next all-hands." No specific integration points, no acknowledgment of existing practices, no phasing.

**Pass:** Names at least 3 specific integration points (PRD template, review checklist, QA test plan, launch gate). Acknowledges existing good practice. Proposes adoption that's phased and realistic. **Fail:** Generic adoption guidance with no mechanics.

---

## Output Format Compliance

**Pass:** All six sections present (Executive Summary, Context, Principles, Core Content, Application, Ask). Agent Block populated with `artifact_subtype: Standard` and correct field types. Context note present and honest about company context availability. Executive Summary is self-contained. Ask section names specific next steps with owners or ownership roles (e.g., "Add data requirements section to the PRD template by [date]," "Schedule analytics QA training for QA team").

**Fail:** Missing sections. Agent Block omitted or incomplete. No context note. Ask is vague ("let me know your thoughts").

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| Concrete examples preserved in Context | 15% | At least 2 specific launch failures from input used with enough detail to convey cost |
| Principle quality | 15% | Principles grounded in org's failure patterns; specific enough to reshape thinking; no generic "data is important" |
| SDLC integration depth | 25% | Requirements mapped to 4+ stages; each stage names artifacts and responsible roles; a reader can act on it |
| Multi-audience actionability | 15% | Role-specific expectations for at least 3 of 4 named audiences; not just PM-centric |
| Application and adoption realism | 15% | 3+ specific integration points; acknowledges existing practice; phased and realistic |
| Output format compliance | 15% | All sections present; Agent Block correct; context note present; Ask names specific next steps |
