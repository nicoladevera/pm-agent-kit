# Tech Spec: Loan Summary API — Home Dashboard Widget

**Author:** [Engineering]
**Date:** March 2026
**Status:** Draft
**Related Ticket:** LOAN-1847

---

## Overview

This spec describes the backend changes needed to support the new Loan Summary Widget on the home dashboard. The widget needs to display a borrower's current loan balance, next payment amount, next payment date, and payment status for all active loans.

---

## Proposed Solution

We will add a new `GET /v2/borrowers/{borrower_id}/loan-summary` endpoint to the Loans API. This endpoint will:

- Return summary data for all active loans for the given borrower
- Aggregate multi-loan data into a summary object
- Cache responses in Redis with a 5-minute TTL to reduce load on the loan database

### Response Schema

```json
{
  "total_active_loans": 1,
  "next_payment": {
    "amount_cents": 50000,
    "due_date": "2026-04-01",
    "status": "upcoming"
  },
  "total_outstanding_balance_cents": 350000
}
```

### Caching Strategy

Responses will be cached in Redis using the key `loan_summary:{borrower_id}` with a 5-minute TTL. Cache is invalidated on any payment event from the payment service.

---

## Database Changes

No schema changes required. The endpoint aggregates from existing `loans` and `payment_schedule` tables.

---

## Dependencies

- Redis cluster (already provisioned)
- Payment service to publish payment events for cache invalidation

---

## Open Questions

- Should the response include loan-level detail (individual loan summaries) in addition to the aggregate? The frontend may want this for the "See all loans" expanded view.
- What is the expected p99 latency target for this endpoint?
