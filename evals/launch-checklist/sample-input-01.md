# Feature: Installment Schedule Payments via ACH

**Context:** We're adding ACH (bank transfer) as a new payment method for installment plans. Currently users can only pay via debit card. ACH adds a lower-cost payment rail that benefits both users (lower fees on some plans) and the company (lower processing costs).

**What's shipping:**
- Users can link a bank account during installment plan setup or from payment settings
- ACH payments are initiated 3 business days before the due date (to account for ACH settlement time)
- Users see ACH as a payment option alongside debit card
- If ACH payment fails, the system falls back to the user's debit card on file
- New "Payment Method" section in account settings where users can manage linked bank accounts

**Who it affects:**
- All users with active or new installment plans (US market only for now)
- Support team will get questions about the new payment option
- The payments infrastructure team has built the ACH integration with Plaid for bank linking and Stripe for ACH debits

**Timeline:**
- Engineering complete: April 5
- Target launch: April 14
- This is a beta launch — we want to roll out to 20% of new installment plan users first, then expand based on results

**Team:**
- PM: Nicola (me)
- Engineering lead: Marcus
- Backend: Priya, David
- Frontend: Sarah
- Design: Leo
- QA: Jamie

**What I'm worried about:**
- ACH failures are harder to communicate to users than card declines — the failure happens days later
- The fallback-to-card logic needs to be bulletproof
- Bank linking via Plaid can be flaky with certain banks
- We need to make sure the settlement timing is communicated clearly so users don't think their payment is late

**Notes:**
- Legal has already reviewed and approved the ACH integration
- The payments team has been testing in staging for two weeks
- We don't have a dashboard for ACH-specific metrics yet
