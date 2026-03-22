> **This is an example file.** Replace all content below with your company's actual context. The goal is to show what "substantive" means — enough detail that the agent can reason about ownership, capacity, and stakeholder dynamics without asking follow-up questions.

---

# Team Context

## Team Structure

Spendulum's product org is split into two squads, both reporting to the VP of Product (Jordan Park).

**Growth Squad** — Owns acquisition, activation, retention, and monetization.
- PM: Alex Ruiz (you)
- Engineering: 4 engineers (2 iOS, 1 Android, 1 backend)
- Design: 1 designer (shared with Platform at 50%)
- Data: 1 analyst (Priya Nair, shared with Platform)

**Platform Squad** — Owns core tracking infrastructure, bank sync, and data pipeline reliability.
- PM: Sam Ortega
- Engineering: 3 engineers (1 iOS, 1 Android, 1 backend/infra)
- Design: 1 designer (shared with Growth at 50%)
- Data: shared analyst (Priya Nair)

**Cross-functional partners (not embedded):**
- Legal/Compliance: Maya Chen (consult before any new data collection or advice-adjacent copy)
- Security: Darius Kim (loop in for anything touching credentials, payments, or PCI scope)
- Marketing: Jasmine Torres (owns app store copy and external messaging; coordinates on launch timing)

---

## Velocity and Capacity

**Growth squad velocity:** ~18-22 story points per sprint (2-week sprints). Typical overhead: 20-25% (standups, code review, bug triage, on-call rotation).

**On-call rotation:** One engineer is on-call per week, handling production issues and sync failure escalations. On-call engineers are available for sprint work but at reduced capacity (~50%).

**Current constraints:**
- One iOS engineer (Marcus) is onboarding to the bank sync codebase. Expect 30% ramp-up cost on sync-related work through end of Q1.
- Android coverage is thin — single-engineer. Android work has higher blast radius; size stories conservatively and avoid committing to parallel Android tracks.

---

## Ownership Map

| Area | iOS | Android | Backend | Design |
|------|-----|---------|---------|--------|
| Onboarding & Activation | Priya L. | Jordan T. | Sam W. | Lena K. |
| Core Tracking | Marcus | Jordan T. | Sam W. | Lena K. |
| Bank Sync | Marcus (ramping) | Jordan T. | Sam W. (primary) | — |
| Budgets & Goals | Priya L. | Jordan T. | Sam W. | Lena K. |
| Notifications | Priya L. | Jordan T. | Sam W. | — |
| Monetization / Paywall | Priya L. | Jordan T. | Sam W. | Lena K. |

---

## Decision-Making

**Roadmap and priority calls:** Alex (PM) owns, with sign-off from Jordan Park (VP) for anything affecting H1 OKRs or requiring cross-squad resources.

**Technical architecture:** Engineering leads make the call, with PM input on scope and timing. Escalate to CTO (Nadia Reyes) only for decisions that affect multiple squads or introduce new external dependencies.

**Copy and legal review:** Any user-facing copy that touches financial guidance, advice language, or new data collection requires legal sign-off (Maya Chen). Turnaround is typically 3-5 business days; plan accordingly.

**Design system changes:** Design lead (Lena K.) owns. Changes affecting both squads require a sync between Lena and Sam Ortega's squad designer before implementation.

---

## Stakeholder Map

| Stakeholder | Role | Cares about | How to communicate |
|-------------|------|-------------|-------------------|
| Jordan Park | VP of Product | D7 retention, free-to-Plus conversion, OKR progress | Weekly in 1:1; written summary for anything that affects OKRs |
| Nadia Reyes | CTO | Technical risk, infra reliability, engineering velocity | Loop in via Jordan; direct ping for P0 production issues |
| Maya Chen | Legal | Regulatory exposure, content compliance | Slack for quick questions; doc review for new features |
| Jasmine Torres | Marketing | Launch timing, ASO, external messaging | Weekly sync before major releases; 2-week heads-up for store copy changes |
| Priya Nair | Data Analyst | Metric definitions, data integrity, analysis turnaround | Slack for ad hoc; 3-day heads-up for structured analysis requests |

---

## Known Team Constraints and Patterns

- **Android is the bottleneck.** Single engineer means Android work serializes. Don't plan parallel Android tracks in the same sprint unless stories are truly independent.
- **Design is shared.** Lena splits her time between squads. Growth work is prioritized for her time, but high-complexity Platform sprints can pull her. Confirm availability before committing design-dependent stories.
- **Data requests have lead time.** Priya handles both squads. Structured analysis requests need 3 business days minimum. Don't put a data deliverable in a sprint without confirming it's in her queue.
- **Legal review is slow.** 3-5 days is the floor. If a feature has any advice-adjacent copy or new data collection, flag it to Maya at design kickoff, not right before launch.
- **Retro action items have a poor completion rate.** The last three retros surfaced the same issue: action items get assigned but not tracked. Pending a process fix, PM is tracking these in `knowledge/retros/` and following up in weekly syncs.
