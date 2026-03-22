# Ticket: Add Loan Summary Widget to Home Dashboard

**Type:** Feature
**Priority:** P1
**Epic:** Dashboard Personalization
**Assignee:** TBD
**Sprint:** Sprint 24

---

## Story

As a borrower, I want to see my loan information on the home screen so I can quickly check my balance and upcoming payments without navigating to the Loans tab.

---

## Background

Multiple users have requested a quick-view loan summary on the home dashboard. Support tickets indicate that users frequently navigate to the Loans tab just to check their next payment date. This widget would surface the most critical loan info at a glance.

The widget will display: current balance, next payment amount, next payment date, and payment status.

For borrowers with multiple active loans, the widget will show a summary view with the ability to expand.

---

## Acceptance Criteria

1. The loan summary widget appears on the home dashboard for all users with at least one active loan.
2. The widget displays the correct loan balance, next payment date, and payment status.
3. The widget should look visually consistent with other dashboard cards.
4. Tapping the widget navigates the user to the Loans tab.
5. The widget loads quickly enough that users don't experience a noticeable delay.
6. For users with multiple loans, a summary count is shown with a "See all loans" link.
7. The widget handles the case where a user's loan data is unavailable and shows an appropriate message.

---

## Design

Link to Figma: [pending — designs not yet finalized]

---

## Dependencies

- Loans API team to confirm the endpoint for fetching summary data
- Design team for final widget specs

---

## Definition of Done

- Widget appears on home dashboard for eligible users
- All AC pass QA review
- No regressions on existing dashboard components
