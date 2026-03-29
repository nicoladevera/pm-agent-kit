# Ticket: Express Checkout for Returning Customers

**Type:** Feature
**Priority:** P1
**Epic:** Checkout Optimization
**Assignee:** TBD
**Sprint:** Sprint 31

---

## Story

As a returning customer, I want to complete a purchase in one click so that I don't have to re-enter my payment and shipping details every time I buy something.

---

## Background

Our checkout abandonment rate is highest at the payment and address entry steps. Returning customers who have previously completed a purchase have their payment method and shipping address on file, but they're still required to go through the full checkout flow. This creates unnecessary friction for our most loyal buyers.

Express checkout removes that friction by letting returning customers confirm their saved details and complete the purchase without re-entering anything. The checkout button should be highlighted and labeled "Buy Now" to distinguish it from the standard checkout flow and draw attention to the faster option.

Rollout will be limited to returning customers (defined as: account with at least 1 previous completed order, saved payment method on file, saved default shipping address on file). New customers and guests see the standard checkout flow.

---

## Acceptance Criteria

1. **Given** a returning customer is on a product page with an item in stock, **When** they see the express checkout option, **Then** the "Buy Now" button is displayed prominently below the "Add to Cart" button, highlighted in the brand's primary action color with the label "Buy Now."

2. **Given** a returning customer clicks "Buy Now," **When** the order summary is displayed, **Then** the customer's saved default shipping address and last-used payment method are pre-populated in the order summary for review.

3. **Given** a returning customer reviews the pre-populated order summary, **When** they click "Confirm Purchase," **Then** the order is submitted using the system's saved payment method and the customer is taken to the order confirmation page.

4. **Given** a returning customer has multiple saved addresses, **When** the order summary is displayed, **Then** the address marked as "default" is pre-selected, with a link to change to another saved address.

---

## Notes

- The feature should work across all device types (desktop, mobile web, native app).
- Performance target: the order summary screen should load in under 2 seconds.
- Legal has reviewed and confirmed no additional consent is needed beyond what was captured during the initial payment method save.

---

## Dependencies

- Design team to provide final UI specs for the "Buy Now" button and order summary screen
- QA to define regression test suite for standard checkout to ensure no regressions

---

## Definition of Done

- Express checkout flow available to all eligible returning customers in production
- All AC pass QA review
- No regressions on standard checkout flow
- Performance target validated in load testing
