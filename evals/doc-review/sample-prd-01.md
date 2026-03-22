# PRD: Automated Payment Reminders

**Author:** PM Lead, Lending
**Status:** Draft
**Last Updated:** 2026-03-15

---

## Problem Statement

Many users with active installment plans miss their scheduled payments. Late payments result in fees for the user and increased support volume for the team. Users have told us through support tickets and NPS surveys that they forget when payments are due, especially when they have multiple financial commitments.

We need a way to proactively remind users about upcoming payments so they can plan accordingly and avoid unnecessary fees.

---

## Proposed Solution

Build an automated payment reminder system that sends push notifications and in-app messages to users with active installment plans before their payment due dates.

### Key Features

- Push notifications sent before upcoming payment due dates
- In-app reminder banner on the home screen when a payment is upcoming
- Configurable reminder timing per market (different markets may have different optimal windows)
- Support for multiple active plans per user
- Snooze functionality so users can dismiss reminders temporarily
- Eventually, AI-powered smart scheduling that predicts the optimal time to send reminders based on user behavior patterns

### User Flow

1. User has an active installment plan with a scheduled payment
2. System identifies that a payment due date is approaching
3. System sends a push notification to the user with the payment amount and due date
4. User taps the notification and is taken to the payment screen
5. User completes the payment
6. If the user doesn't act on the notification, a follow-up reminder is sent closer to the due date
7. An in-app banner appears on the home screen showing the upcoming payment details

---

## Success Metrics

- Reduce late payments
- Increase user satisfaction with the payment experience
- Reduce payment-related support tickets
- Improve on-time payment rate for installment plan users

---

## Scope

### In Scope

- Push notification reminders for installment plan payments
- In-app reminder banner on home screen
- Configurable reminder windows per market
- Snooze/dismiss functionality
- Multi-language support for notification copy
- Quiet hours (no notifications between 10pm-7am local time)
- Future phases will include SMS reminders, email reminders, and AI-powered optimal send-time prediction

### Out of Scope

- Reminders for non-installment products (line of credit, single-repayment loans)
- Automatic payment scheduling or auto-pay enrollment
- Changes to the payment flow itself

---

## Technical Approach

The reminder system will be built as a new microservice that subscribes to the loan events Kafka topic. When an installment plan is created or a payment schedule is generated, the reminder service will schedule notifications based on the configured timing rules for that market.

We'll use the existing notification infrastructure (Firebase Cloud Messaging for push, in-app messaging SDK for banners) so there's no need to build new delivery channels.

### Architecture

- New `reminder-service` microservice
- Consumes events from `loan-events` Kafka topic
- Stores reminder schedules in PostgreSQL
- Publishes to existing notification service via internal API
- Market-specific configuration stored in config service

---

## Dependencies

| Dependency | Owner | Status |
|------------|-------|--------|
| Notification service capacity for increased volume | @Platform Team — Maria Chen | Not yet assessed |
| Firebase Cloud Messaging quota review | @Mobile Team — James Park | In progress |
| Market-specific regulatory review for reminder messaging | @Legal — Zaida Guzman | Not started |
| Config service support for per-market reminder timing | @Platform Team — Maria Chen | Not started |

---

## Acceptance Criteria

1. System sends payment reminders to users with active installment plans before their due date
2. Reminders include the payment amount and due date
3. Users can tap the notification to navigate to the payment screen
4. System sends reminders at the appropriate time based on market configuration
5. Users can snooze a reminder, and it will reappear at a later time
6. In-app banner displays on the home screen when a payment is upcoming within the configured window
7. System respects quiet hours and does not send notifications between 10pm-7am local time
8. Reminders are sent in the user's preferred language
9. System handles users with multiple active installment plans and sends appropriate reminders for each

---

## Timeline

| Milestone | Target Date |
|-----------|-------------|
| Technical design complete | April 1, 2026 |
| Development complete | May 15, 2026 |
| QA complete | May 30, 2026 |
| Beta launch (Mexico) | June 15, 2026 |
| Full rollout | July 2026 |

---

## Open Questions

1. What is the optimal reminder timing for each market? Should we start with a default and iterate?
2. Should we allow users to configure their own reminder preferences in a future version?
3. How should reminders work for users who have auto-pay enabled with their bank?
