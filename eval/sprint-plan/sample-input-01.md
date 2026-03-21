# Sprint Planning Input: Sprint 15

**Request from PM:** "Plan the next sprint. Sprint 14 wraps tomorrow. Here's the backlog and capacity."

---

## Priorities

From Carlos (VP Engineering) in the Q2 planning meeting:
1. Ship installment schedule visibility for Mexico (any remaining work from Sprint 14)
2. Start payment reminder system — the notification service decision landed on "build" last Thursday
3. Continue loan restructuring API groundwork if capacity allows

---

## Team Capacity — Sprint 15 (March 24 - April 4, 10 business days)

| Member | Role | Availability | Notes |
|--------|------|-------------|-------|
| Dev Patel | Backend Engineer | 8 of 10 days | PTO March 27-28 (Thu-Fri) |
| James Wu | SRE / Backend | 6 of 10 days | On-call rotation first week (March 24-28), reduces to ~50% availability |
| Ana Torres | Design | 3 of 10 days | Splitting time with the growth team — only available Mon/Wed/Fri |
| Sarah Chen | Eng Lead | 10 of 10 days | Full availability but splits time between coding and lead duties (~60% IC capacity) |
| Raj Sharma | New Backend Engineer | 10 of 10 days | Just joined the team Monday. First sprint. Needs onboarding and pairing. |

---

## Carryover from Sprint 14

| Ticket | Title | Status | Points | Notes |
|--------|-------|--------|--------|-------|
| PMT-206 | Spanish localization for schedule screens | Blocked | 3 | Localization team still hasn't responded. Sarah escalated to their manager. |
| PMT-204 | Onboarding tooltip for first-time schedule view | In Progress | 2 | Design handoff done. ~50% implemented. |
| PMT-207 | Analytics events for schedule interactions | In Progress | 2 | Waiting on data team schema confirmation. |

---

## Backlog (Unprioritized)

| Ticket | Title | Points | AC? | Notes |
|--------|-------|--------|-----|-------|
| PMT-301 | Design notification service database schema | 5 | Yes — 6 AC | Foundation for the notification build. Must be done before any other notification work. |
| PMT-302 | Build notification scheduling engine | 8 | Yes — 12 AC | Core scheduling logic. Handles timing rules, retry, multi-channel routing. |
| PMT-303 | Build push notification delivery via FCM | 5 | Yes — 7 AC | Push channel implementation. Depends on PMT-301. |
| PMT-304 | Build in-app notification rendering | 3 | Yes — 5 AC | In-app channel. Depends on PMT-301. |
| PMT-305 | Notification template engine | 5 | No AC | Templates for different notification types. Depends on PMT-301. |
| PMT-306 | Payment reminder business logic | 3 | Partial — 3 AC, missing error handling | Maps installment due dates to reminder triggers. Depends on PMT-302. |
| PMT-307 | Admin dashboard for notification monitoring | 2 | No AC | Ops visibility into notification delivery rates and failures. |
| PMT-308 | Load testing for notification throughput | 3 | No AC | Verify system handles 150K+ users at peak. |
| PMT-401 | Loan restructuring API — endpoint scaffolding | 5 | Yes — 8 AC | First story for loan restructuring feature. Independent of notification work. |
| PMT-402 | Loan restructuring — eligibility rules engine | 5 | Yes — 9 AC | Business logic for which loans qualify for restructuring. Depends on PMT-401. |
| PMT-501 | Fix: Schedule screen crashes on plans with 0 remaining payments | 1 | Yes — 2 AC | Bug found in Sprint 14 QA. Quick fix. |
| PMT-502 | Tech debt: Refactor payment status enum across services | 3 | No | Has been in the backlog for 4 sprints. Keeps getting deprioritized. |

---

## Additional Context

- The notification service "build" decision means Dev is assigned to notification work full-time per the resource plan Sarah presented.
- Raj (new engineer) has Go experience but has never worked in this codebase. Sarah plans to pair with him for the first week.
- The localization team's Kenya launch is March 31. Sarah expects they'll be available after that, meaning Spanish strings could arrive in Sprint 15's second week.
- Data team confirmed they can review the analytics event schema by Monday (March 24).
