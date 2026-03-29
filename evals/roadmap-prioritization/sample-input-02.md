# Prioritization Input — Platform Investment vs. Growth Features

I'm stuck on a prioritization question and I need help thinking through it. It's really just two big bets competing for the same team.

---

## The Situation

We're a mid-stage B2B SaaS company (~$15M ARR, 180 customers, avg deal size $85K). We just closed our Series B and the board wants to see "path to $50M ARR" in the next 18 months. Our current growth rate is 40% YoY.

The engineering team is 12 people. After the Series B, we have budget to hire 4 more, but they won't be productive for 2-3 months after joining. So for the next quarter, we have 12 engineers.

---

## Option A: Multi-Tenant Architecture Migration

Our CTO is pushing hard for this. Right now, every customer runs on a dedicated instance. This made sense at 20 customers but at 180 it's an operational nightmare:

- Deployments take 3 days instead of 3 hours because we're deploying to 180 instances
- Infrastructure costs are $48K/month and growing linearly with customer count
- We can't ship features that require cross-tenant data (benchmarking, aggregate analytics)
- The on-call team spends 40% of their time on instance-specific issues
- Every new customer adds ~$270/month in incremental infra cost regardless of their contract size

The CTO estimates this is a 2-quarter effort requiring 6-8 engineers. During migration, feature velocity drops by ~60% because most of the team is focused on the migration.

The CTO says: "If we don't do this now, it only gets harder. At 300 customers this becomes a 4-quarter effort. At 500 it might require a full rewrite."

---

## Option B: Enterprise Analytics Suite

Our Head of Sales is pushing this. Enterprise buyers (deals >$150K) keep asking for advanced analytics — benchmarking against industry peers, predictive churn indicators, custom reporting. The 3 largest deals we lost this year ($200K+) all cited analytics gaps in their evaluation.

The Head of Sales says:
- "I have 6 qualified enterprise prospects in the pipeline right now totaling $1.2M in ACV"
- "3 of them have told me explicitly that benchmarking is a must-have"
- "If we ship this by end of Q3, I can close at least 4 of the 6"
- "Our main competitor launched benchmarking last quarter and it's in every competitive deal now"

The engineering lead estimates 8-10 engineers for one quarter to build a competitive analytics suite. This is a one-quarter effort if we commit the full team.

---

## The Tension

We can't do both. Not even close. Option A needs 6-8 engineers for 2 quarters. Option B needs 8-10 for 1 quarter. We have 12 engineers.

The CTO and Head of Sales aren't even in the same meeting anymore because the discussion got heated. The CEO asked me to bring a recommendation to the leadership team.

To make it more complicated:
- Option B (analytics) technically needs cross-tenant data for the benchmarking feature — which is exactly what Option A (multi-tenant) would enable. But Sales says we could do a "good enough" version with anonymized sample data.
- The CTO says the "good enough" version would be a dead-end — we'd have to rebuild it after the multi-tenant migration anyway.
- If we do Option A first, we lose the 6 enterprise prospects (the sales cycle won't wait 6 months). If we do Option B first with the workaround, we ship faster but accumulate more technical debt.

---

## What I Need

I need a clear-headed recommendation that I can defend in a room where the CTO and Head of Sales are both going to push back. What should we do and why?
