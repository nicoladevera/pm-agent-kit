# PRD: Installment Schedule Visibility

**Author:** PM Lead, Lending
**Status:** Approved
**Last Updated:** 2026-03-18

---

## Problem Statement

Users in Mexico with active installment plans are confused about their repayment schedules. Since launching installment plans (replacing single-repayment loans), support tickets asking "when is my next payment" have increased 40%. First-payment miss rates for installment users are 12% higher than the historical first-payment miss rate for single-repayment users. Approximately 150,000 active installment plan users in Mexico are affected.

The current loan detail screen shows only the total amount owed and the next payment date. For installment plans with 3-12 payments over multiple months, users need to see the full schedule — all payments, amounts, dates, and statuses — to plan their finances.

---

## Success Metrics

| Metric | Baseline | Target | Timeframe | Data Source |
|--------|----------|--------|-----------|-------------|
| "When is my next payment" support tickets | 2,400/month | 1,200/month (50% reduction) | 3 months post-launch | Zendesk ticket classifier |
| First-payment miss rate (installment users) | 18% | 10% (match single-repayment historical rate) | 3 months post-launch | Payment events in analytics warehouse |
| Installment schedule screen view rate | N/A (new) | 60% of installment users view within first week | 1 month post-launch | Screen view events |

---

## Proposed Solution

Add an installment schedule view to the existing loan detail screen in the Mexico mobile app. The schedule displays all payments (past and upcoming) with amounts, due dates, and payment status. Users with their first installment plan see a one-time onboarding tooltip explaining the schedule.

### User Flow

1. User opens the app and navigates to their loan
2. Loan detail screen now shows a "View Payment Schedule" section below the existing loan summary
3. User sees a timeline/table of all installment payments with status indicators
4. For first-time installment users, a tooltip explains: "Your loan is now paid in installments. Here's your full payment schedule."
5. User can tap any payment row to see details (amount, due date, payment method if paid)

---

## Scope

### In Scope
- Installment schedule display on loan detail screen (integrated, not a separate screen)
- Payment status indicators: Paid, Upcoming, Overdue, Due Today
- One-time onboarding tooltip for first-time installment users
- Spanish language support (Mexico market)
- Pull data from existing `GET /api/v2/loans/{loan_id}/installments` endpoint

### Out of Scope
- Payment infrastructure changes
- Push notification reminders (separate initiative)
- Payment history export or download
- Other markets beyond Mexico
- Changes to the payment flow itself
- Auto-pay enrollment or scheduling

---

## Edge Cases

| Scenario | Expected Behavior |
|----------|-------------------|
| User has overdue payment(s) | Overdue payments displayed first with red "Overdue" status badge. Overdue amount shown prominently. |
| User has fully paid off installment plan | Show completed schedule with all payments marked "Paid". Display "Plan Complete" banner. |
| User has both a single-repayment loan and an installment plan | Each loan has its own detail screen. Installment schedule only appears on installment plan loans. |
| Payment due today | "Due Today" status with amount. No distinction between morning and evening. |
| User's device timezone differs from payment timezone | All dates displayed in the user's local timezone. Payment processing happens in Mexico City timezone (CST/CDT). |
| API returns error when loading schedule | Display error state: "Unable to load your payment schedule. Pull to refresh or try again later." Log error event. |
| User has 12 installments (maximum) | All 12 display. No pagination needed — vertical scroll is sufficient for up to 12 items. |
| User dismisses onboarding tooltip | Tooltip does not reappear. Dismissal state persisted locally on device. |

---

## Acceptance Criteria

- **Given** a user with an active installment plan, **When** they navigate to the loan detail screen, **Then** a "Payment Schedule" section displays below the loan summary showing all installment payments
- **Given** the Payment Schedule section is displayed, **Then** each payment row shows: payment number (e.g., "Payment 3 of 6"), amount in MXN, due date, and status (Paid / Upcoming / Overdue / Due Today)
- **Given** a payment has status "Paid," **Then** display a green checkmark icon and the date it was paid
- **Given** a payment has status "Overdue," **Then** display the row with a red background and "Overdue" badge, and show the overdue payment(s) at the top of the schedule
- **Given** a payment has status "Due Today," **Then** display the row highlighted with an orange "Due Today" badge
- **Given** a user is viewing an installment plan for the first time (no prior `schedule_viewed` event for this plan), **When** the Payment Schedule section loads, **Then** display a tooltip: "Your loan is now paid in installments. Here's your full payment schedule." with a dismiss button
- **Given** the user taps the dismiss button on the onboarding tooltip, **Then** the tooltip disappears and does not reappear on subsequent visits (persist dismissal locally)
- **Given** the user taps a payment row, **Then** expand the row to show: payment amount, due date, payment method (if paid), and transaction ID (if paid)
- **Given** the API call to `GET /api/v2/loans/{loan_id}/installments` fails, **Then** display an error state with message "Unable to load your payment schedule. Pull to refresh or try again later." and log an `installment_schedule_error` event with `user_id`, `loan_id`, `error_code`
- **Given** all payments in the installment plan are marked "Paid," **Then** display a "Plan Complete" banner above the schedule
- **Given** the user's device language is Spanish (Mexico), **Then** all schedule UI text, status badges, tooltip content, and error messages display in Spanish

---

## Data Requirements

### Events

| Event Name | Trigger | Payload |
|------------|---------|---------|
| `installment_schedule_viewed` | User loads the Payment Schedule section | `user_id`, `loan_id`, `plan_id`, `num_installments`, `num_overdue`, `is_first_view: boolean` |
| `installment_schedule_row_tapped` | User taps a payment row to expand details | `user_id`, `loan_id`, `payment_number`, `payment_status` |
| `installment_onboarding_tooltip_shown` | Onboarding tooltip displayed | `user_id`, `loan_id`, `plan_id` |
| `installment_onboarding_tooltip_dismissed` | User dismisses onboarding tooltip | `user_id`, `loan_id`, `plan_id`, `time_visible_ms` |
| `installment_schedule_error` | API call to load schedule fails | `user_id`, `loan_id`, `error_code`, `retry_count` |

### Dashboard

- Schedule adoption: daily/weekly unique users viewing the schedule, segmented by first-time vs. returning
- Onboarding tooltip engagement: shown rate, dismiss rate, time visible
- Correlation: schedule view rate vs. on-time payment rate (to validate hypothesis)
- Error rate monitoring: schedule load failures by error code

---

## Dependencies

| Dependency | Owner | Status | Risk |
|------------|-------|--------|------|
| `GET /api/v2/loans/{loan_id}/installments` endpoint | Backend Lending Team — Edgar Saldaña | Available | Low — endpoint exists and is stable |
| Spanish translations for all UI strings | Localization Team — Victoria L. | Not started | Medium — 2-week turnaround typical |
| UX design for schedule component and tooltip | Design — Diana Pérez | In progress | Low — draft designs available |
| Mobile team capacity for Mexico app release | Mobile Team — James Park | Constrained | High — team is stretched; needs slot in sprint |

---

## Open Questions

1. Should we show payment history (past payments) inline with upcoming payments, or only upcoming? Current design includes both — PM to confirm.
2. Should the onboarding tooltip appear for users who already have payment history on their installment plan, or only for net-new installment users?
3. Is there a minimum number of installments where the schedule adds value? (e.g., a 2-payment plan might not need a full schedule view)
