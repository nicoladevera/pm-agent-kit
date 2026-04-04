# Evaluation Rubric — roadmap-prioritization

**Target input:** `evals/roadmap-prioritization/sample-input-01.md`
**Skill under test:** `.claude/skills/roadmap-prioritization/SKILL.md`
**Purpose:** Determine whether `roadmap-prioritization` correctly profiles candidates with uneven evidence quality, weights evidence quality visibly in the comparison, handles a soft commitment constraint, identifies the dependency between SSO auth refactoring and other work, produces a substantive "what we're not doing" section, and delivers a stress test that surfaces non-obvious risks.
**Coverage:** Single mode — full skill coverage.

---

## Candidate Profiling Completeness

The input deliberately provides uneven evidence across 5 candidates. The skill must normalize the comparison while making the unevenness visible.

### Evidence quality expected per candidate:

1. **Smart Notification Engine** — Validated (cross-channel feedback synthesis, exit survey, CSM signal). Strong evidence.
2. **Reporting Performance Overhaul** — Validated (feedback synthesis #1 theme, support tickets, named lost deals, competitive intel). Strongest evidence of any candidate.
3. **Self-Serve Enterprise SSO** — Inferred (VP conviction, 4 anecdotal deal losses from Sales, no formal win/loss analysis). Moderate but not validated.
4. **API v2 and Developer Platform** — Assumed (CEO enthusiasm, 3 feature requests, no research, no business case). Weakest evidence.
5. **Automated Churn Prediction** — Inferred (3 years of data, feasibility study showing AUC > 0.8, but no business case for the retention impact). Technical feasibility validated, business impact assumed.

**Pass:** All 5 candidates profiled on the same dimensions. Evidence quality explicitly graded per candidate. The gap between Reporting (validated, #1 theme, competitive intel) and API v2 (CEO enthusiasm, no evidence) is named and weighted in the comparison. **Fail:** All candidates treated as equally well-evidenced. Evidence quality not named. Profiles inconsistent across candidates.

---

## Evidence Quality Assessment

The key test: the skill must visibly weight evidence quality in the ranking, not just note it.

### Critical tests:

**Reporting Overhaul should be ranked as the strongest candidate on evidence.** It has the most evidence: #1 feedback theme, support ticket data, named lost deals, and competitive intel. If it doesn't rank highly, the rationale needs to explain why strong evidence was overridden.

**API v2 should be flagged as having insufficient evidence for prioritization.** Three feature requests and CEO enthusiasm do not constitute a business case. The skill should recommend gathering evidence (business case or discovery) before committing 12-16 weeks of engineering.

**SSO's evidence gap should be named specifically.** The VP says it's critical, Sales has 4 anecdotal losses, but there's no formal win/loss analysis and no research with enterprise buyers. The soft commitment ("SSO by end of summer") adds pressure, but the evidence doesn't match the conviction level.

**Pass:** Evidence quality visibly influences the ranking. High-evidence candidates treated differently from low-evidence ones. API v2 flagged for evidence gathering before commitment. SSO evidence gap named despite VP pressure. **Fail:** All candidates ranked purely on stated impact. Evidence quality noted but not weighted. API v2 included in the roadmap without questioning the evidence basis.

---

## Comparison Rigor

The comparison must be structured and honest about trade-offs.

### Expected comparison dynamics:

**Reporting vs. Notifications:** Both address retention (the H2 OKR is NRR 95% → 105%). Reporting has stronger evidence and higher urgency (competitive deals being lost now). Notifications have strong evidence but are a lower-urgency retention driver.

**SSO vs. everything else:** SSO serves the "enterprise groundwork" theme (VP's strategic interest) but has weaker evidence. The soft commitment to 2 enterprise prospects creates a constraint — the skill must acknowledge this commitment without letting it override evidence-based prioritization. The auth refactoring dependency (3-4 weeks before SSO can start) is a sequencing factor.

**Churn Prediction vs. other retention plays:** Directly serves the NRR OKR. Technical feasibility is validated but business impact is assumed. Shares the data scientist (60% availability) with analytics, creating a resource constraint.

**API v2:** Should be assessed honestly — CEO enthusiasm is not evidence. The skill should recommend either building a business case or deferring.

**Pass:** Structured comparison across consistent dimensions. Trade-offs between Reporting and Notifications articulated. SSO constraint (soft commitment) named without overriding evidence assessment. Resource contention (shared data scientist) addressed. API v2 evidence gap honestly handled. **Fail:** Candidates evaluated in isolation. Trade-offs not articulated. Soft commitment treated as a hard constraint that automatically prioritizes SSO.

---

## Sequencing Logic

The sequence should reflect the H2 OKR (NRR 95% → 105%), dependencies, evidence quality, and constraints.

### Expected sequencing considerations:

1. **Reporting Overhaul should be prioritized.** Strongest evidence, directly addresses retention, competitive urgency (deals being lost now), and #1 user complaint. The database architecture changes also partially address tech debt.

2. **The SSO commitment creates a sequencing constraint.** Two enterprise prospects were promised SSO "by end of summer." The skill must address this — honor the commitment (smaller team, parallel work), renegotiate the timeline, or accept the risk of losing those deals. The auth refactoring dependency (3-4 additional weeks) affects the timeline.

3. **Churn Prediction and Notifications are both retention plays.** The skill should assess which has a faster path to NRR impact. Churn prediction has a resource constraint (shared data scientist).

4. **API v2 should not be in the Q3 sequence.** Insufficient evidence. The recommendation should be to build a business case or run discovery — not to commit 12-16 weeks of engineering on CEO enthusiasm.

### Critical tests:

**The skill must address the soft SSO commitment explicitly.** Ignoring it is not an option — real-world prioritization includes honoring or renegotiating commitments. The skill should name the trade-off: honoring the commitment vs. the evidence gap.

**Capacity math must work.** 6-7 engineers available, 13-week quarter. The recommended initiatives must fit within capacity. If the skill recommends more work than the team can deliver, it hasn't prioritized.

**Pass:** Reporting prioritized based on evidence + OKR alignment + competitive urgency. SSO commitment addressed explicitly (honored with constraints, renegotiated, or risk accepted). API v2 deferred with evidence-gathering recommendation. Capacity math is realistic. **Fail:** Sequence doesn't account for capacity. SSO commitment ignored. API v2 included without questioning evidence. Reporting deprioritized despite strongest evidence.

---

## "What We're Not Doing" Quality

At least 1-2 candidates must be deferred, and the "not doing" section must be substantive.

### Expected deferrals:

**API v2** — deferred due to insufficient evidence. Reconsideration condition: complete a business case that sizes the integration opportunity and validates demand beyond 3 feature requests.

**At least one other candidate** will likely be deferred or reduced in scope based on capacity. The rationale must name what was cut and why.

### Critical tests:

**Each deferred initiative must have a reconsideration path.** "Not now, not never" framing with a specific condition for re-evaluation. Not a dismissal.

**The CEO's enthusiasm for API v2 must be handled diplomatically but honestly.** The skill should not fabricate a rationale for including API v2 to avoid the awkward conversation. "The evidence doesn't support a 12-16 week investment this quarter — here's what we'd need to see" is the right framing.

**Pass:** Deferred initiatives have specific reasons, reconsideration conditions, and framing. API v2 honestly assessed. CEO enthusiasm acknowledged without inflating the evidence. **Fail:** No deferrals (everything fits, somehow). Deferrals are perfunctory ("didn't make the cut"). API v2 deferred without a constructive path forward.

---

## Stress Test Novelty

The stress test must surface insights specific to this prioritization, not generic risks.

### Expected premortem failure modes:

- We prioritized Reporting but the real retention driver was notification fatigue — the #1 and #2 feedback themes had different causal weights on churn
- The SSO commitment blows up — we lose both enterprise prospects AND the work consumed capacity that could have gone to higher-impact retention work
- Churn Prediction's ML model works technically but CSMs don't adopt the workflow — the tool exists but the retention impact doesn't materialize
- The CEO escalates API v2 mid-quarter, disrupting the plan

### Expected blindspots:

- **OKR assumption:** The plan optimizes for NRR, but what if the board's "path to $50M" requires new logo acquisition, not retention? NRR and acquisition are different levers.
- **Reporting-as-retention assumption:** Reporting speed is the #1 complaint, but is it actually a churn driver? Users complain about slow reports but might not churn over it. The link between #1 complaint and #1 churn driver is assumed, not proven.

**Pass:** Premortem has 3+ failure modes specific to this sequence. Blindspot surfaces a non-obvious assumption (complaint ≠ churn driver, or OKR vs. board priorities). Conviction calibrated to evidence quality. **Fail:** Stress test repeats the evidence quality concerns already discussed. Blindspot is generic ("our estimates might be wrong"). Conviction is 9-10 with no conditions.

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| Candidate profiling completeness | 10% | All 5 candidates profiled on same dimensions; evidence quality graded per candidate |
| Evidence quality assessment | 15% | Evidence visibly weighted in ranking; API v2 flagged; SSO gap named |
| Comparison rigor | 20% | Structured comparison; trade-offs articulated; SSO commitment addressed; resource contention handled |
| Sequencing logic | 15% | OKR-aligned; dependencies respected; SSO commitment addressed; capacity math works |
| "What we're not doing" quality | 15% | Substantive deferrals with reconsideration paths; API v2 honestly handled; CEO enthusiasm managed |
| Stress test novelty | 15% | Specific premortem failures; non-obvious blindspot (complaint ≠ churn, or OKR vs. board); conviction calibrated |
| Output format compliance | 10% | Matches format; context note present; smell test completed; Agent Block populated |
