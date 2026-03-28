# Acceptance Criteria Standards

What good acceptance criteria look like. Use this when evaluating AC in a PRD or ticket, or when generating stories and tasks.

**Primary audience for AC:** AI coding agents (implementing code and tests) with human engineer oversight. This means AC must be precise enough for an agent to implement without clarifying questions — because unlike a human engineer, an agent won't interrupt the PM to ask what "appropriate" means. It will guess. And it will guess wrong.

---

## What Good AC Are

**Specific.** Name the exact behavior, not a category of behavior. "User can view remaining installment schedule" is specific. "User can manage their plan" is not. An agent given vague AC will make implementation decisions the PM didn't intend.

**Testable.** Each criterion can be translated directly into an automated test. The AC should be close to test language — given/when/then structure is preferred because it maps directly to test cases an agent can generate.

**Bounded.** Each AC describes one verifiable behavior, not a compound requirement. If an AC contains "and" connecting two distinct behaviors, it should be split. Agents treat compound AC as one unit — if one part fails, the whole thing is unclear.

**Data-aware.** Include data requirements where relevant — events fired, schemas updated, fields captured, with explicit field names and types. Agents will implement exactly what you specify. If the event name is missing, the agent will name it — and it may not match your naming conventions.

**Scoped to what can be verified.** Don't include business outcomes as AC. "Reduce late payments by 15%" is a success metric, not an acceptance criterion. "System sends a push notification 24 hours before payment due date" is verifiable by code and tests.

**Input/output explicit.** State what goes in and what comes out. What parameters does the function/endpoint/UI accept? What does it return? What does the user see? Agents don't infer I/O contracts from context — they need them stated.

**Boundary conditions declared.** State the limits. Maximum values, minimum values, empty states, null handling. What happens at the edges? "Supports up to 12 installments" is a boundary. Without it, an agent may not handle the 13th installment case.

**Error handling specified.** State what happens when things fail. What does the user see on error? What does the system log? What's the fallback? If error handling isn't in the AC, it won't be in the implementation — or it will be, but the agent will choose how, and the PM loses control of the experience.

---

## Writing AC for Agent Implementation

When AC will be implemented by coding agents, apply these additional patterns:

### Use Given/When/Then Structure

This maps directly to test cases. Agents can translate this format into code with high fidelity.

**Instead of:** "User can view their payment schedule"

**Write:**
- **Given** a user with an active installment plan with 6 remaining payments
- **When** the user navigates to the loan detail screen
- **Then** the screen displays a table with columns: payment number, amount, due date, status (paid/upcoming/overdue)

### Name the Exact Data Contract

Agents implement exactly what you specify. If you want a specific event name, field name, or schema shape — state it.

**Instead of:** "Track order creation"

**Write:**
- **On** successful order submission, fire event `order_placed`
- **Payload:** `{ user_id: string, order_id: string, total_amount: number, currency: string, item_count: integer, placed_at: ISO-8601 timestamp }`
- **Destination:** analytics event pipeline

### Declare Boundary Conditions Explicitly

What an agent doesn't see, it won't handle.

**Instead of:** "Supports installment plans"

**Write:**
- Minimum installments: 2
- Maximum installments: 12
- If user requests more than 12, display error: "Installment plans support 2-12 payments"
- If user requests fewer than 2, display error: "Minimum 2 installments required"
- Minimum installment amount: $5.00 per payment

### Specify Error States as AC

Each error scenario should be its own AC with a defined user-facing message and system behavior.

**Instead of:** "Handle errors gracefully"

**Write:**
- **Given** a welcome email fails to deliver (mail provider returns a bounce or timeout error)
- **When** the retry limit (3 attempts, 10-minute intervals) is exhausted
- **Then** log a `welcome_email_failed` event with `user_id`, `email_address`, `error_code`, and flag the account for manual review — do not surface an error to the user

### Reference External Contracts

If the AC depends on an API, service, or database schema, name the source of truth.

**Instead of:** "Pull payment data from the backend"

**Write:**
- Retrieve payment schedule from `GET /api/v2/loans/{loan_id}/installments`
- Response schema defined in `docs/api/installments.yaml`
- If the endpoint returns 404, display empty state: "No active installment plan found"

---

## Good vs. Bad Examples

### Example 1: User-facing behavior

**Bad:** "User can manage their installment plan"
- Why it's bad: "Manage" is undefined. An agent given this will decide what "manage" means and build something the PM didn't spec.

**Good:**
- **Given** a user with an active installment plan
- **When** the user taps "View Plan" on the loan detail screen
- **Then** display: payment schedule table (payment number, amount, due date, status), total remaining balance, next payment date and amount highlighted
- The table is sorted by due date ascending
- Overdue payments display in red with status "Overdue"

### Example 2: Edge case handling

**Bad:** "System handles edge cases"
- Why it's bad: An agent will either ignore this entirely or implement arbitrary edge case handling.

**Good:**
- **Given** a user attempts to upload a 50 MB file when only 20 MB of storage remains in their workspace
- **When** the upload is submitted
- **Then** the system rejects the upload before transfer begins, displays: "You need 50 MB but only 20 MB is available. Free up space or upgrade your plan to continue.", and does not partially upload the file

### Example 3: Data tracking

**Bad:** "Data is tracked"
- Why it's bad: An agent will either skip it or invent event names and payloads.

**Good:**
- **On** installment plan creation, fire `installment_plan_created` event
- **Payload:** `{ user_id: string, plan_id: string, total_amount: number, num_installments: integer, first_payment_date: ISO-8601 }`
- **On** each scheduled payment completion, fire `installment_payment_completed` event
- **Payload:** `{ user_id: string, plan_id: string, payment_number: integer, amount: number, days_before_due: integer }`
- Both events route to the analytics pipeline via the existing event bus

### Example 4: Notification timing

**Bad:** "System sends reminders at the appropriate time"
- Why it's bad: An agent will choose a time. It might choose midnight.

**Good:**
- **Given** a user's free trial expires on March 15
- **When** it is March 12 at 10:00 AM in the user's local timezone
- **Then** send an email: "Your trial ends in 3 days. Upgrade now to keep access to your data."
- Delivery window: 10:00 AM - 11:00 AM local timezone only
- If the user has already upgraded to a paid plan, do not send the reminder
- If the user has opted out of marketing emails, do not send (no in-app fallback in v1)

---

## Common AC Problems

- **Scope creep hiding in AC:** An acceptance criterion that introduces functionality not described in the scope section. An agent will implement it without questioning whether it belongs.
- **Business outcomes disguised as AC:** Success metrics framed as acceptance criteria. "Reduce late payments by 15%" isn't something an agent can implement — it's a result of many things working together.
- **Compound AC:** Two or more distinct behaviors joined with "and." Split them. Agents may implement the first clause and miss the second, or treat them as one atomic behavior when they should be independent.
- **Implicit assumptions:** AC that assume the reader (or agent) knows current system behavior. An agent has no memory of how the system works today unless you tell it. State expected behavior explicitly.
- **Missing negative cases:** What should the system *not* do? An agent won't infer constraints you don't state. If reminders should not be sent for paid-off plans, say so. If the feature should not work for line-of-credit products, say so.
