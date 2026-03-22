# Evaluation Rubric — launch-checklist

**Target input:** `evals/launch-checklist/sample-input-01.md`
**Skill under test:** `skills/launch-checklist/SKILL.md`
**Purpose:** Determine whether `launch-checklist` produces a complete, calibrated checklist that catches gaps the PM hasn't addressed, assigns owners, and includes a specific rollback plan.

---

## Launch Type Detection

The input explicitly states "this is a beta launch" with a 20% rollout to new installment plan users. The skill must:
- Correctly identify the launch type as **Beta**
- Calibrate checklist depth to Beta (not GA-heavy, not Internal-light)

**Fail:** Launch type misidentified. Checklist depth mismatched (e.g., requiring a full blog post and press plan for a beta, or omitting support enablement).

---

## Planted Gaps

The sample input deliberately omits several things a complete beta launch needs. The checklist should surface these.

| # | Gap | Must Catch? | What good detection looks like |
|---|-----|-------------|-------------------------------|
| 1 | **No rollback plan in the input** — The PM describes worries about ACH failures and fallback logic but never specifies rollback triggers, mechanism, or authorization. | Yes | Generates a rollback section with specific trigger criteria (e.g., ACH failure rate > X%, fallback-to-card rate > Y%). Flags that the PM needs to define thresholds. Feature flag mechanism should be assumed or asked about. |
| 2 | **No monitoring or alerting specified** — The PM says "we don't have a dashboard for ACH-specific metrics yet." No alerts, no error rate monitoring, no latency tracking for the new payment rail. | Yes | Includes monitoring items: ACH success/failure rate dashboard, Plaid bank-linking error rate, fallback-to-card trigger rate, alerting for anomalous failure spikes. Flags the missing dashboard as a pre-launch dependency, not a post-launch nice-to-have. |
| 3 | **No success metrics or targets** — The PM says they want to "expand based on results" but never defines what results. No adoption targets, no failure rate thresholds, no comparison framework for ACH vs. card. | Yes | Generates success criteria with specific metrics: ACH adoption rate among eligible users, ACH payment success rate, fallback-to-card frequency, user-reported payment confusion rate. Flags that targets need PM input. |
| 4 | **No support enablement plan** — The PM notes "support team will get questions" but provides no plan for training, FAQ, or escalation path. | Yes | Includes support enablement items: FAQ document covering ACH timing, failure scenarios, and bank linking issues. Escalation path for ACH-specific issues. Training session or brief before launch. |
| 5 | **No external communication plan** — For a beta with 20% of new users, there's no plan for how users learn about ACH as an option — in-app, email, changelog. | Should catch | Notes that beta users encountering ACH need to understand what it is and how it works. Recommends in-app education or contextual help. Changelog entry for the beta. |

---

## Intentional Strengths in the Input

The sample input provides several strong elements. The checklist should build on these, not flag them as gaps.

| Element | Why it's strong |
|---------|----------------|
| **Team is named with roles** | Allows the checklist to assign owners to specific people, not just roles. |
| **Timeline is specific** | Engineering complete date + target launch date allows relative due dates (L-5, L-3, etc.). |
| **PM's worries are articulated** | The ACH failure timing, Plaid flakiness, and settlement communication concerns should inform specific checklist items — not be repeated back as "risks." |
| **Legal already reviewed** | The checklist should note this under Legal/Compliance as complete, not re-flag it. |

**False positive check:** If the checklist flags "legal review needed" when the input explicitly states legal has already approved, that's a false positive.

---

## Quality Checks

### Owner Assignment
Every checklist item should have a named owner (person or role). The input provides enough team information to assign most items:
- Engineering items → Marcus, Priya, David, or Sarah by specialty
- Documentation → Nicola (PM) or could involve Leo (design) for user-facing materials
- Support enablement → Nicola (PM)
- Monitoring → Engineering (Marcus or Priya)

**Pass:** Most items have specific names from the input. Remaining items have role-based owners with a note to confirm. **Fail:** All owners are "TBD" despite the input providing a full team roster.

### Checklist Depth Calibration
Beta launches should include:
- Documentation (help center draft or FAQ, internal technical docs)
- Internal communication (team + leadership + adjacent teams)
- External communication (contextual/in-app for beta users, changelog)
- Support enablement (FAQ, escalation path, basic training)
- Monitoring (automated alerts, usage dashboard)
- Data and analytics (full instrumentation, success metrics, baseline)
- Rollback plan (feature flag, quantitative triggers, communication)
- Dependencies (confirm Plaid and Stripe integrations, staging validation)

Should NOT include (over-scoping for beta):
- Full blog post or press release
- Company-wide announcement
- Sales enablement materials
- Formal post-launch board review

**Pass:** All beta-appropriate dimensions covered. No GA-level items inflating the checklist. **Fail:** Missing monitoring or rollback (critical for beta), or including press release for a 20% rollout.

### PM Worries Converted to Checklist Items
The PM's stated worries should become specific, actionable checklist items — not just acknowledged:
- "ACH failures harder to communicate" → Checklist item for user-facing error messaging and timing explanation
- "Fallback-to-card must be bulletproof" → QA checklist item for fallback testing + monitoring item for fallback trigger rate
- "Plaid can be flaky" → Monitoring item for Plaid error rates + support FAQ entry for bank linking issues
- "Settlement timing communication" → Documentation item for user-facing explanation of 3-day ACH timeline

**Pass:** Each worry maps to at least one specific checklist item. **Fail:** Worries are echoed in a "risks" section but not converted to preventive checklist items.

### Rollback Specificity
- Trigger criteria must be quantitative (numbers, not vibes)
- Rollback mechanism should reference feature flag or percentage rollout (the input implies this)
- Authorization chain should name who decides
- Communication plan for affected users if rolled back mid-beta

**Pass:** All four elements present with specifics. **Fail:** "Roll back if things go wrong" or triggers without thresholds.

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| Launch type correctly identified | 10% | Beta identified and depth calibrated |
| All 5 planted gaps caught | 30% | Each gap surfaced with actionable items (4/5 minimum) |
| No false positives on strengths | 10% | Legal not re-flagged; team names used, not ignored |
| Owner assignment quality | 15% | Specific names where input allows; roles elsewhere |
| Rollback plan specificity | 15% | Quantitative triggers, mechanism, authorization, comms |
| PM worries → checklist items | 10% | Each worry converted to preventive action |
| Output format compliance | 10% | Matches declared format; context note present |
