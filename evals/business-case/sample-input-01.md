# Business Case Input — Self-Service Cancellation

Hey, I want to put together a business case for building a self-service cancellation flow. Here's what I know:

---

## The Problem

Our support team is drowning in cancellation requests. I pulled some numbers last week:

- 40% of our support tickets are cancellation-related (people wanting to cancel their installment plan, pause it, or modify it)
- Each cancellation ticket takes about 12 minutes of agent time on average
- We're handling roughly 2,400 cancellation tickets per month
- Support team morale is tanking because they're doing repetitive work instead of helping with real issues
- Our CSAT for cancellation interactions is 2.1 out of 5 — it's our worst-rated support category

Customers are frustrated too. They have to email support, wait for a response (average 6 hours), then go back and forth confirming their identity and plan details. One customer in a recent NPS survey said: "I shouldn't need to talk to a human to cancel something I signed up for online in 30 seconds."

---

## What I'm Thinking

We should build a self-service cancellation flow in the app. Let users cancel, pause, or modify their installment plans themselves. Mobile-first since 70% of our users are on mobile.

There are some compliance considerations — we're in regulated financial services, so there are disclosure requirements around early cancellation (fees, impact on credit score, remaining balance settlement). Legal reviewed this last quarter and said self-service is fine as long as we show specific disclosures before the user confirms. They have the requirements doc.

---

## Some Context

- We have about 85,000 monthly active users
- Average plan value is $1,200 spread over 6 months
- We charge a $25 early cancellation fee (which we'd still collect via self-service)
- Our support team is 8 agents, fully loaded cost of about $65K/year each
- We're also looking at building a referral program and upgrading our analytics dashboard — those are the other two big things competing for engineering time this quarter

---

## What I Need

This would save a lot of support time and make customers happier. Can you build out the full business case? I want to present this to my VP next week.
