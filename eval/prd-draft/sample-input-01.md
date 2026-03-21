# Sample Input: Rough Problem Statement

This is what a PM might drop into a conversation when they want to draft a PRD. It's deliberately messy, incomplete, and conversational.

---

Hey, I need to write a PRD for something we've been hearing about for a while.

So we recently changed the loan structure — we moved from single-repayment loans to installment plans in Mexico. The thing is, users are confused about their repayment schedules. Support tickets about "when is my next payment" have spiked 40% since we launched installments. A lot of users are also missing their first payment because they didn't realize the schedule changed from what they were used to.

The product team talked about building some kind of repayment schedule visibility thing. Like, right now when a user goes to their loan screen, they just see the total amount owed and the next payment date. But with installments, they need to see the full schedule — all the payments, amounts, dates, what's paid and what's upcoming.

We also want to make sure users coming from single-repayment loans understand that their experience is different now. There might need to be some kind of onboarding or education moment when they get their first installment plan.

Some constraints:
- We can't change the payment infrastructure — this is a frontend/UX problem
- The backend API for installment schedules already exists (the `/api/v2/loans/{id}/installments` endpoint)
- This needs to work in Spanish (Mexico market first)
- The mobile team is stretched, so we need to keep the scope tight
- We have about 150K active installment plan users in Mexico right now

I haven't really thought about metrics yet. And I'm not sure if we should include payment history or just the upcoming schedule. Also wondering if this should be a separate screen or integrated into the existing loan detail view.
