# Evaluation Rubric — doc-review (Ticket: Consumer E-Commerce Express Checkout)

**Target input:** `evals/doc-review/sample-ticket-02.md`
**Skill under test:** `skills/doc-review/SKILL.md`
**Purpose:** Determine whether `doc-review` correctly identifies the 4 planted issues in this e-commerce checkout ticket, preserves the valid story framing, and provides criterion-referenced feedback.

**Coverage:** Single mode — doc-review on a Ticket document type.

---

## Document Type Detection

The document is a Ticket. Signals: user story in "As a / I want / So that" format, Acceptance Criteria as primary evaluation structure, Definition of Done section, Sprint assignment, Priority field.

**Pass:** Identified as Ticket type. Ticket-specific quality criteria applied (from `references/quality-criteria-ticket.md`). **Fail:** Treated as a PRD or general document, which would cause wrong criteria to be applied — e.g., flagging absence of "Success Metrics" as a problem on a ticket.

---

## Planted Issues (Must Catch)

The ticket contains 4 deliberate quality failures. The review must identify all of them.

| # | Issue | Criterion ID | What good detection looks like | What failure looks like |
|---|-------|-------------|-------------------------------|------------------------|
| 1 | **AC #1 describes UI appearance, not system behavior** | TICKET-3 (Acceptance Criteria) | Flags specifically: AC #1 describes what the button looks like ("highlighted in the brand's primary action color," "labeled 'Buy Now'") — this is a visual design spec, not a behavioral AC. Names what's missing: what does the system DO when the button is displayed? Is the express checkout option shown only when eligibility conditions are met (saved payment + saved address)? What is the system response time expectation? Severity: High. Recommends: AC #1 should specify the eligibility check ("Given a returning customer with at least 1 prior completed order, a saved payment method, and a saved default address") and the system behavior that presents the option — visual specs belong in the design file. | Review acknowledges the button spec without noting it describes UI appearance rather than testable system behavior. |
| 2 | **Missing error states — expired payment, missing address, out-of-stock** | TICKET-3 (Acceptance Criteria) | Flags that the 4 ACs cover only the happy path and a minor branching case (multiple addresses). Names specifically: (a) What happens when the saved payment method is expired? (b) What happens when the default address is incomplete or invalid? (c) What happens when the item goes out of stock between the customer clicking "Buy Now" and confirming? Each is a distinct AC that is entirely absent. Severity: High. Notes consequence: an engineer implementing only the 4 existing ACs would have no guidance on these failure modes and would make independent decisions about behavior — inconsistent with other checkout error handling. | Review notes "error states could be more complete" without naming the 3 specific missing scenarios. |
| 3 | **Implicit dependency on payment service team not flagged** | TICKET-6 (Dependencies) | Flags: the ticket says "the system will use the system's saved payment method" (AC #3) but never names the payment service team, the stored credentials endpoint, or its API contract. "Saved payment method" is not a self-contained system capability — it relies on a third-party payment processor's tokenized card vault (or equivalent internal service). The dependency on that team is not listed. Names it explicitly: the payment processing team (or external payment processor) owns the stored card credentials; this ticket must declare that dependency, confirm the API contract for submitting a payment with a stored token, and identify what happens if that service is unavailable. Severity: Medium. | Review accepts the dependencies section as adequate without noting the payment service gap. Or flags "design team" as a dependency concern (which is already listed) without addressing the missing payment service dependency. |
| 4 | **No tracking events specified** | TICKET-4 (Definition of Done) | Flags the complete absence of analytics requirements. The Definition of Done says nothing about events firing. Names what's needed: `express_checkout_initiated` (fires when "Buy Now" button is displayed to an eligible user), `express_checkout_order_summary_viewed` (fires when order summary renders), `express_checkout_completed` (fires on successful order submission, with order_id, payment_method_type), `express_checkout_failed` (fires when submission fails, with failure_reason). Without these events, the team cannot measure: how many eligible users see the feature, the conversion rate through the express flow, or failure reasons. Severity: High. | Review omits the missing tracking requirement entirely. Or mentions "analytics" without naming specific events. |

---

## False Positives Check

The 2 intentional strengths must NOT be flagged as issues.

| Strength | Why it's strong | False positive to avoid |
|----------|----------------|------------------------|
| Well-formed user story | "As a returning customer, I want to complete a purchase in one click so that I don't have to re-enter my payment and shipping details." Names the user, the action, and the outcome. Not an implementation task dressed as a story. | Review should not flag the story framing as "unclear" or suggest it needs to be rewritten. |
| Core happy-path AC is reasonably specific | ACs #2, #3, and #4 describe testable behaviors in Given/When/Then format with reasonable specificity for the primary flow. AC #4 correctly handles the multiple-saved-addresses branch. | Review should not flag the existing ACs as vague or poorly structured — the issue is what's absent (error states, tracking), not what's present. The existing happy-path coverage is adequate. |

**Pass:** Both strengths explicitly acknowledged — story framing noted as strong, existing happy-path ACs noted as adequately structured. **Fail:** Well-formed story flagged as weak, or existing ACs criticized for format issues they don't have.

---

## Feedback Quality

Each identified issue should include what's wrong, why it matters, and what a stronger version looks like.

**Pass:** For each of the 4 issues:
1. The specific problem is named (not just "error states missing" but "no AC for expired payment method, invalid address, or out-of-stock scenario")
2. The consequence is explained (e.g., "without error state ACs, the engineer will make independent decisions about what to show the user when payment fails — likely inconsistent with other checkout error handling")
3. A concrete fix or example is provided (e.g., "Add: Given a returning customer clicks Confirm Purchase, When the payment processing service returns a card declined error, Then the user sees an inline error message with a link to update their payment method, and the order is not submitted")

**Fail:** Issues bullet-pointed without explanation of why they matter or what a better version looks like.

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| Document type correctly identified as Ticket | 10% | Ticket-specific criteria applied; type stated; ticket not evaluated as PRD |
| AC #1 UI-only spec flagged (system behavior missing) | 10% | Visual spec identified as AC gap; eligibility check and system behavior named as what's needed |
| Missing error states flagged (expired payment, invalid address, out-of-stock) | 10% | All 3 specific missing scenarios named; severity High |
| Implicit payment service dependency flagged | 10% | Payment service team / stored credentials endpoint named as missing dependency; severity Medium |
| Missing tracking events flagged with named events | 10% | At least 3 specific event names provided; connection to feature measurement explained |
| No false positives on strengths | 15% | User story and happy-path ACs acknowledged as strong — not flagged as weak |
| Feedback quality (problem + consequence + fix for each issue) | 25% | All 4 issues include what's wrong, why it matters, and what a stronger version looks like |
| Output format compliance | 10% | What's Strong / What Needs Work / Smell Test / Open Questions / Agent Block all present |
