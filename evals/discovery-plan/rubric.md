# Evaluation Rubric — discovery-plan

**Target input:** `evals/discovery-plan/sample-input-01.md`
**Skill under test:** `.claude/skills/discovery-plan/SKILL.md`
**Purpose:** Determine whether `discovery-plan` correctly extracts assumptions from a problem area with multiple competing hypotheses, risk-ranks by consequence rather than comfort, selects appropriate methods matched to assumption types, defines pre-registered evidence criteria, and sequences research to test the problem before the solution.
**Coverage:** Single mode — full skill coverage.

---

## Problem Space Framing

The input has a clear trap: the VP has been pushing an "enterprise onboarding redesign" for two quarters. The product team already has a hypothesis (onboarding flow doesn't work for teams). The PM is rightly skeptical — the funnel data shows *where* enterprise users drop, not *why*.

**The skill must frame this as a problem validation exercise, not a solution validation exercise.** The decision is "should we invest in an enterprise onboarding redesign?" — not "how should we redesign enterprise onboarding?"

**Good framing:** "Enterprise users convert at roughly half the rate of SMB users (34% vs 62% to first meaningful action), representing a significant revenue gap. The team hypothesizes onboarding UX is the cause, but five competing explanations exist. This discovery plan tests which explanation is correct before committing to a redesign."

**Bad framing:** "We need to understand how to improve the enterprise onboarding flow." (This assumes onboarding is the problem — which is exactly what needs to be tested.)

**Pass:** Problem framed as "why are enterprise users dropping off?" not "how do we fix onboarding?" Decision named (whether to greenlight the redesign). The VP's existing hypothesis treated as an assumption to test, not a premise to build on. **Fail:** Framing accepts the onboarding redesign as the starting point. Discovery plan is designed to validate a predetermined solution.

---

## Assumption Extraction Quality

The input provides five explicit competing hypotheses. The skill must capture all of them as testable assumptions and surface additional hidden ones.

### Expected assumptions (at minimum):

**Explicitly in the input:**
1. The onboarding flow doesn't work for teams (no bulk invite, no admin setup, no role-based permissions)
2. Enterprise buyers are evaluating competitors and churning to them, not because of onboarding
3. "Enterprise" is too broad a segment — 10-person startups and 500-person companies have different needs
4. IT/procurement friction (SSO, security reviews, vendor approval) is the real blocker
5. Champion adoption failure — the person who signed up can't get their team to use it

**Hidden assumptions the skill should surface:**
6. Enterprise users actually *want* a team-oriented product — they might be signing up for individual use despite having team licenses
7. The 34% conversion rate is an onboarding problem, not a product-market fit problem — enterprise users may complete onboarding fine and *then* churn because the product doesn't solve their specific pain points
8. The behavioral data in Amplitude is reliable enough to diagnose the problem — nobody's done the enterprise-specific deep dive yet

**Pass:** All 5 explicit hypotheses captured as testable assumptions. At least 2 hidden assumptions surfaced (especially #7 — the PMF vs. onboarding distinction, which is the most consequential hidden assumption). Assumptions stated as testable claims, not vague areas. **Fail:** Fewer than 5 assumptions mapped. No hidden assumptions surfaced. Assumptions stated as topics rather than testable claims.

---

## Risk Ranking Judgment

The key test: the skill must prioritize by consequence, not by ease of testing.

### Expected priority ranking logic:

**Highest priority (test first):**
- **Segment validity** (assumption #3) — if "enterprise" isn't a coherent segment, every other assumption is framed wrong. This gates everything downstream.
- **Problem vs. PMF** (assumption #7, hidden) — if the issue is product-market fit rather than onboarding, a redesign is wasted investment regardless of how well-executed it is.

**High priority:**
- **Onboarding UX vs. other causes** (#1 vs #2, #4, #5) — distinguishing between the competing explanations for drop-off.

**Lower priority:**
- **Specific onboarding improvements** — testing which onboarding features to build is premature until the problem is validated.

### Critical tests:

**The segment validity assumption should be ranked high.** The input explicitly mentions that "10-person startups and 500-person companies probably have very different needs." If the skill doesn't flag segment definition as a gating assumption, it's building a plan on potentially invalid foundations.

**The PMF vs. onboarding distinction is the hardest and most consequential.** If the skill buries this or doesn't surface it, the plan may lead to an expensive redesign that doesn't address the real issue.

**Pass:** Gating assumptions (segment validity, problem vs. PMF) ranked highest. Ranking rationale references consequence and dependency, not ease of testing. Solution-oriented assumptions explicitly deprioritized until problem is validated. **Fail:** Assumptions ranked by ease of testing (data mining first because it's cheap). Onboarding UX assumed as the problem. No gating logic.

---

## Method Selection Appropriateness

The input provides real constraints: Amplitude data exists but hasn't been analyzed for enterprise specifically, CSM team has qualitative signal, no prior formal research, 8-week timeline.

### Expected method selections:

1. **Data mining (Amplitude)** — for segment analysis and funnel deep-dive. The input says "nobody's done a deep dive on the enterprise onboarding funnel specifically." This is low-cost, fast, and should happen first to ground the qualitative research.
2. **User interviews (enterprise customers and churned enterprise accounts)** — for understanding *why* users drop off, which of the competing hypotheses holds, and what the champion adoption experience looks like.
3. **CSM debrief / structured internal interviews** — the CSM team has qualitative signal that hasn't been systematized. This is a low-cost way to bootstrap understanding before external research.
4. **Survey** (optional, if time allows) — to quantify findings from interviews across the enterprise base.

### Critical tests:

**Data mining must be recommended as the first step.** The input explicitly says Amplitude data exists and hasn't been analyzed. Not starting with data mining would be a miss — it's the cheapest way to validate whether the segment definition is valid and where exactly the funnel breaks.

**Churned enterprise users must be included as interview targets.** The input mentions 41% 14-day retention for enterprise — meaning 59% are gone. Studying only current users produces survivorship bias. The skill should explicitly recommend recruiting churned enterprise accounts.

**Prototype testing or A/B testing should NOT be recommended at this stage.** The problem hasn't been validated yet. If the skill recommends testing onboarding flow variants before understanding why users drop off, it's jumped to solutions.

**Pass:** Data mining first. Interviews second with churned users explicitly included. CSM debrief as quick-win. No solution testing before problem validation. Method rationale explains why each method fits the assumption type. **Fail:** Interviews only. No data mining despite Amplitude being available. Only current users studied. Prototype testing recommended before problem validation.

---

## Evidence Criteria Specificity

Each research activity must have pre-defined success/failure criteria — not vague goals.

**Good criteria:** "Segment analysis: if enterprise accounts show 3+ distinct behavioral clusters with meaningfully different drop-off patterns, the 'enterprise' segment needs to be decomposed before further research."

**Bad criteria:** "We'll look at the data and see what patterns emerge."

**Pass:** Every research activity has specific success, failure, and ambiguous-result criteria defined before execution. Criteria are testable — someone could evaluate results against them and agree on the outcome. At least one decision point in the sequence ("if X is invalidated, stop and reassess"). **Fail:** Criteria are vague ("understand enterprise behavior"). No failure criteria. No decision points.

---

## Sequencing Logic

The plan must reflect dependency logic: test gating assumptions first, test the problem before the solution.

### Expected sequence:

1. **Data mining / funnel analysis** (1-2 weeks) — segment analysis + enterprise-specific funnel deep-dive. This grounds everything that follows.
2. **CSM debrief** (can parallel with #1, 1 week) — systematize existing qualitative signal.
3. **Enterprise user interviews** (2-3 weeks) — both active and churned users, segmented by company size if the data mining reveals meaningful clusters.
4. **Synthesis + decision point** — do we have enough to decide? If problem is validated as onboarding, proceed to solution research. If not, redirect.
5. **Optional: solution-oriented research** (only if problem is validated) — concept tests or prototype tests for specific onboarding improvements.

### Critical tests:

**The 8-week timeline constraint must be respected.** The input says the VP wants a decision by end of Q2 (8 weeks). The plan should fit within that window, with buffer for analysis and synthesis.

**There must be at least one explicit decision point.** "If the data mining shows enterprise users actually complete onboarding at similar rates to SMB but churn afterward, the onboarding redesign hypothesis is invalidated — redirect to retention/PMF research."

**Pass:** Gating research first. Decision points named. Timeline fits within 8 weeks. Problem validation before solution testing. **Fail:** All research runs in parallel with no sequencing logic. No decision points. Timeline exceeds 8 weeks without acknowledging the constraint. Solution testing included from the start.

---

## Scope Realism

**Pass:** Participant counts are justified (e.g., 8-12 enterprise users per behavioral cluster, 5-8 churned accounts). Timeline accounts for recruiting lag. Resource needs are honest — specifically noting that recruiting churned enterprise users will be harder than recruiting active users. Total plan fits the 8-week constraint. **Fail:** Participant counts are arbitrary or unjustified. Timeline ignores recruiting. Resource needs not addressed. Plan requires capabilities the team hasn't confirmed.

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| Assumption extraction quality | 15% | All 5 explicit hypotheses captured; 2+ hidden assumptions surfaced; testable claims not vague topics |
| Risk ranking judgment | 20% | Gating assumptions ranked highest; consequence-based not ease-based; solution assumptions deprioritized |
| Method selection appropriateness | 20% | Data mining first; interviews include churned users; no premature solution testing; methods matched to assumption types |
| Evidence criteria specificity | 15% | Pre-defined success/failure criteria for each activity; testable and specific; decision points included |
| Sequencing logic | 10% | Gating research first; decision points named; problem before solution; 8-week constraint respected |
| Scope realism | 10% | Participant counts justified; timeline honest; recruiting challenges acknowledged |
| Output format compliance | 10% | Matches format; context note present; smell test completed; Agent Block populated |
