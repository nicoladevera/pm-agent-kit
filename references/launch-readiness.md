# Launch Readiness Standards

What makes a launch checklist complete and a launch ready to ship. Use this to generate launch checklists, evaluate launch readiness, or assess whether a feature is prepared for its intended audience. The launch analog to `sprint-planning.md` — that file covers sprint-level execution; this file covers the ship-level coordination that follows.

Launching is caring. A thorough checklist isn't bureaucracy — it's the difference between a feature that lands well and one that creates fire drills. The PM who shows up with every dimension covered earns the team's trust that nothing will fall through the cracks.

---

## Launch Types

### Four Types, Increasing Scope

Not every launch needs a full GTM playbook. The launch type determines checklist depth — which dimensions apply and how thoroughly.

| Type | Audience | Scale | Min. Duration | Internal Scope | What's Required |
|------|----------|-------|---------------|----------------|-----------------|
| **Internal** | Team and internal users only | 5–20 people | 1–2 weeks | Dogfooding, internal testing, validation | Basic documentation, internal comms, monitoring. No external communication, no support enablement. |
| **Alpha** | Hand-selected external users | 10–50 users, single invite-only cohort | 2–4 weeks | Early signal, direct feedback | Everything in Internal + explicit opt-in process, feedback channel, known limitations documented, rollback plan. |
| **Beta** | Broader external users, may be self-enrolled | 100–1,000 users or 1–5% rollout | 4–8 weeks | Validation at scale, usability at volume | Everything in Alpha + broader comms, support awareness, feature flag or percentage rollout, success criteria. |
| **GA** | All users | 100% | N/A — ongoing | Full production ship | Everything in Beta + complete documentation, full support enablement, external comms (changelog, blog, email as appropriate), monitoring hardened, rollback tested. |

**Red flag:** A GA launch treated with alpha-level preparation. A beta launch with no rollback plan. Any launch type with no monitoring. Scale targets compressed below minimums due to roadmap pressure.

---

### Feature Scope by Launch Type

The table above covers internal readiness requirements. This covers what the *feature itself* needs to include from a user capability standpoint before each launch type is appropriate. A launch checklist can be complete while the feature is still unfit for its intended audience — these are different questions.

| Type | Capability Completeness | Acceptable Gaps | Not Acceptable |
|------|------------------------|-----------------|----------------|
| **Internal** | Core mechanic functional end-to-end | Missing edge cases, rough UX, no polish | Core loop broken or blocked |
| **Alpha** | Primary use case works reliably | Known rough edges, missing secondary flows, accessibility compliance not required | Unstable core, data integrity risks, missing feedback mechanism |
| **Beta** | Full primary use case + most secondary flows | Minor UX gaps, edge case handling incomplete, non-critical missing features | Accessibility non-compliant (if user-facing), P0/P1 bugs open, missing use cases that were marketed to beta users |
| **GA** | All documented use cases complete | Minor enhancements deferred to follow-on | Any documented capability missing, known P0/P1 bugs, accessibility violations |

**Red flag:** Launching to GA with scope gaps rationalized as "v1 limitations." Feature capabilities not explicitly scoped before launch, leaving the team to discover gaps from support tickets.

---

### Exit Criteria (Stage Transitions)

These are gates, not suggestions. A launch should not graduate to the next stage until exit criteria are met. Define the quantitative thresholds (marked [X] below) before each stage begins — not after.

**Internal → Alpha:**
- Core loop validated by at least 3 internal users across different roles
- No P0 bugs open
- Feedback mechanism in place for alpha participants
- Rollback mechanism tested

**Alpha → Beta:**
- Minimum of [X] user interviews or feedback sessions completed (team sets X before Alpha starts)
- Top issues from Alpha triaged and dispositioned: fixed, deferred with rationale, or won't fix
- No P0 or P1 bugs open
- Primary use case completion rate at or above [X]% (define threshold before Alpha starts)
- Support briefed on known limitations

**Beta → GA:**
- Success metrics at or above defined Beta targets — not directionally okay, at the threshold
- Support fully enabled: FAQ complete, troubleshooting guide tested, escalation path live
- All P0/P1 bugs resolved
- External comms drafted and approved
- Rollback plan tested, not just written
- Monitoring and alerting live, routed to the right team, and verified

**Red flag:** Declaring Beta done because the calendar says so. Graduating to GA without meeting quantitative success criteria. Skipping stage transitions entirely ("we'll go straight from Alpha to GA"). Thresholds defined after the stage is already underway.

---

### Participant Selection

Who you invite into each stage directly determines the quality of signal you get. "Hand-selected" and "self-enrolled" describe mechanisms — not criteria.

**Alpha participants should be:**
- Representative of the primary target use case — not just available or willing
- Tolerant of rough edges and incomplete workflows
- Willing to give structured, candid feedback (not just validation)
- Accessible for follow-up questions during the Alpha window
- Not internal champions or advocates who will rationalize problems away

**Beta participants should be:**
- Enrolled via segment targeting, not just open sign-up — define which users belong in Beta and which should wait for GA
- Excluded if a failure during Beta would cause disproportionate harm (high-value accounts, users in regulated contexts, users with no fallback)
- Diverse enough across use cases and environments to surface edge cases before GA

**Red flag:** Alpha cohort composed entirely of friendly users who won't surface friction. Beta open to all users with no enrollment criteria — that's GA, not Beta.

---

### Type Determines Depth, Not Whether You Plan

Even an internal launch needs a checklist. The question isn't "do we need a checklist?" — it's "how deep does each section need to be?" An internal launch might have three items under Documentation and none under External Communication. That's fine. Skipping the exercise entirely is not.

---

## Readiness Dimensions

Every launch touches multiple dimensions. Not every dimension applies to every launch type — but every dimension should be considered and explicitly marked N/A when it doesn't apply.

### Documentation

What needs to be written or updated for this launch.

- **User-facing docs:** Help center articles, feature guides, API documentation, changelog entries
- **Internal docs:** Technical runbooks, architecture diagrams, troubleshooting guides
- **Release notes:** What changed, who it affects, known limitations

**Calibration by type:**
- Internal: Technical notes for the team. No user-facing docs.
- Alpha: Known limitations doc shared with alpha users. Internal technical docs.
- Beta: Help center draft or FAQ. Internal technical docs updated.
- GA: Full user-facing documentation. Internal docs finalized. Release notes published.

**Red flag:** GA launch with no user-facing documentation. Any launch with no technical runbook for the owning team.

---

### Internal Communication

Who inside the company needs to know, and when.

- **Team communication:** Engineering, design, QA — everyone who worked on it
- **Adjacent teams:** Teams whose work is affected or who interface with the feature
- **Leadership:** VP, director, or whoever needs to know before it ships
- **Company-wide:** All-hands, Slack announcement, internal newsletter (if applicable)

**Calibration by type:**
- Internal: Team Slack channel. Maybe a note to the engineering lead.
- Alpha: Team + leadership heads-up. Adjacent teams if there are dependencies.
- Beta: Team + leadership + adjacent teams + any team that might get questions.
- GA: All relevant stakeholders. Possibly company-wide if the feature is significant.

**Red flag:** Adjacent teams surprised by a launch. Leadership learning about a GA launch from a customer.

---

### External Communication

How users and the market learn about the launch.

- **Changelog:** Product changelog entry
- **In-app:** Tooltips, banners, onboarding flows, feature announcements
- **Email:** Targeted or broad email to affected users
- **Blog / social:** Blog post, social media, press (for significant launches)
- **Sales / marketing:** Sales enablement materials, marketing campaigns

**Calibration by type:**
- Internal: None.
- Alpha: Direct communication to alpha participants only.
- Beta: Changelog entry. Possibly in-app for beta users. No broad external comms.
- GA: Full external communication appropriate to the feature's significance. Not every GA needs a blog post — but every GA needs users to know it exists.

**Red flag:** A significant GA launch with no external communication plan. External comms that go out before support is enabled.

---

### Support Enablement

How support and customer-facing teams are prepared.

- **Training:** Support team briefed on what the feature does, how it works, common issues
- **FAQ / troubleshooting guide:** Document covering expected questions and known issues
- **Escalation path:** Who support escalates to when they can't resolve an issue
- **Lead time:** Support needs to be trained before launch, not after the first ticket

**Calibration by type:**
- Internal: N/A (no external users).
- Alpha: Light briefing — alpha users route feedback directly to the team.
- Beta: Support aware of the feature. Basic FAQ available. Escalation path defined.
- GA: Full support enablement. FAQ complete. Troubleshooting guide tested. Escalation path live.

**Red flag:** GA launch where support learns about the feature from a customer ticket. No escalation path defined. FAQ written after launch.

---

### Monitoring and Alerting

What you're watching to know whether the launch is healthy.

- **Feature-specific metrics:** Adoption rate, usage patterns, error rates for the new feature
- **System health:** Latency, error rates, resource utilization for affected services
- **Alerts:** Automated alerts for anomalous behavior (error spike, latency increase, drop in success rate)
- **Dashboards:** Where to look on day one to assess launch health

**Calibration by type:**
- Internal: Basic error monitoring. Feature usage tracking optional.
- Alpha: Error monitoring + basic usage tracking. Manual dashboard check is fine.
- Beta: Automated alerts for errors and performance. Usage dashboard live. Feature adoption tracked.
- GA: Full monitoring suite. Alerts tested and routed to the right team. Dashboard accessible to stakeholders. SLOs defined for the feature.

**Red flag:** Any launch with no error monitoring. GA launch with no alerts. "We'll set up monitoring after launch."

---

### Data and Analytics

How you'll measure whether the feature is working.

- **Instrumentation:** Events tracked, properties captured, taxonomy followed
- **Success metrics:** What you're measuring and what "good" looks like (with targets)
- **Baseline:** Current state of metrics before launch (so you can measure the delta)
- **Dashboard:** Where success metrics are visible post-launch

**Calibration by type:**
- Internal: Minimal — enough to validate the feature works as intended.
- Alpha: Core events instrumented. Qualitative feedback is the primary signal.
- Beta: Full instrumentation. Success metrics defined. Baseline captured.
- GA: Everything in Beta + dashboard accessible to stakeholders. Targets set for 1-day, 1-week, 1-month reviews.

**Red flag:** Any launch with no instrumentation. Success metrics defined after launch. "We'll track this later."

---

### Rollback Plan

How you undo the launch if something goes wrong.

- **Mechanism:** Feature flag, deployment rollback, database migration reversal, or manual process
- **Trigger criteria:** Quantitative thresholds (error rate > X%, latency > Y ms, conversion drop > Z%) or qualitative signals (critical user-reported issues, data integrity concerns)
- **Steps:** Exact steps to execute the rollback, in order
- **Authorization:** Who can decide to roll back (on-call engineer? PM? Engineering lead?)
- **Communication:** Who gets notified on rollback (team, stakeholders, affected users)
- **Data implications:** What happens to data created during the launch window if rolled back

**Calibration by type:**
- Internal: Feature flag off. Minimal process.
- Alpha: Feature flag off + communication to alpha users.
- Beta: Feature flag or percentage rollback + communication plan + data handling.
- GA: Full rollback plan with quantitative triggers, tested mechanism, authorization chain, and communication plan for users and stakeholders.

**Red flag:** Any launch beyond internal with no rollback plan. Rollback triggers that are qualitative only ("if things seem bad"). No one designated to authorize rollback. Rollback mechanism untested.

---

### Dependencies

What must be in place before launch.

- **Technical:** Services deployed, migrations run, feature flags configured, infrastructure scaled
- **Cross-team:** Other teams' work that must be complete (API changes, design assets, legal review)
- **External:** Third-party integrations, vendor approvals, compliance certifications
- **Sequencing:** What must happen in what order (e.g., backend deployed before frontend, docs published before email sent)

**Red flag:** Dependencies discovered on launch day. Cross-team work assumed complete but not confirmed. External dependencies with no status check.

---

### Legal and Compliance

Regulatory or policy requirements (when applicable).

- **Privacy:** Data collection changes, consent requirements, privacy policy updates
- **Terms of service:** Changes that affect ToS
- **Regulatory:** Industry-specific requirements (financial, healthcare, etc.)
- **Accessibility:** WCAG compliance for user-facing changes

Not every launch has legal/compliance implications. When it doesn't, mark N/A explicitly rather than leaving it ambiguous.

---

## Post-Launch

### Success Criteria

Every launch needs a definition of success — not just "users adopt it" but quantitative targets with timeframes.

**Structure success criteria as:**
- **Metric:** What you're measuring
- **Target:** What "good" looks like (a number, not a direction)
- **Timeframe:** When you'll evaluate (1 day, 1 week, 1 month)
- **Data source:** Where the number comes from

**Red flag:** Success criteria with no targets ("we'll track adoption"). Targets with no timeframes. Metrics that can't be measured with current instrumentation.

---

### Post-Launch Review

A scheduled review ensures the team evaluates outcomes rather than moving on to the next thing.

- **When:** Typically 1-2 weeks post-GA for a first read, 30 days for a fuller picture
- **What to review:** Success metrics vs. targets, user feedback, support ticket volume, system health
- **Who attends:** PM, engineering lead, design lead, data analyst
- **Output:** Brief summary of outcomes, learnings, and any follow-up work needed

---

## Using These Standards

**For launch checklist generation (`launch-checklist` skill):** Generate checklists covering all applicable dimensions for the identified launch type. Every item has an owner. Rollback is specific. Success criteria are measurable. Nothing is deferred to "after launch" that should be in place before launch.

**For launch readiness assessment:** Evaluate a launch against these dimensions. Flag dimensions that are missing or underprepared for the launch type. A checklist with gaps is more useful than no checklist — but the gaps should be named.

**For stage transition decisions:** Use exit criteria to evaluate whether a launch has produced sufficient signal to graduate to the next stage. Exit criteria are gates, not aspirations. If thresholds haven't been defined yet, that's the first gap to close — not the last.

**For feature scope evaluation:** Use the Feature Scope by Launch Type table to assess whether the product itself is appropriate for its intended audience at a given stage, independent of whether internal readiness is complete.
