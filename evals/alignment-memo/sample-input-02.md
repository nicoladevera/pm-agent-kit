# Alignment Memo Input — Data Requirements Standard

I want to write a standard for what good data requirements look like and how they should be part of every stage of how we build software. This is for the full product and engineering org — PMs, engineers, data analysts, and QA.

---

## Why I Want This

We keep getting burned. Here are some examples from the last two quarters:

**Subscription tiers launch (Q4):** We launched the new subscription tier structure and had no way to measure conversion between tiers for 3 weeks. The data team got pulled in post-launch to build dashboards that should have been speced in the PRD. We were flying blind during the most critical adoption window.

**Mobile checkout redesign (Q1):** Engineering shipped the redesign but the event tracking was inconsistent with the old flow. We couldn't do before/after comparison because the events had different schemas. The data analyst spent two sprints reconciling the data instead of analyzing it.

**Referral program (Q1):** PM wrote a solid PRD with clear success metrics (referral conversion rate, viral coefficient). But nobody speced which events needed to fire, what the event schema should look like, or where the data would land. Engineering implemented tracking ad hoc during the build, and half the events were wrong or missing. We discovered this a week after launch when the data analyst couldn't reproduce the numbers from the PRD.

**Fraud detection rules (Q4):** We needed historical transaction data to train the fraud model, but the data warehouse didn't have the fields we needed at the granularity we needed. Nobody checked data availability during the spec phase. The project slipped 3 weeks while the data engineering team backfilled the missing data.

---

## What I Know

Some PMs already include event schemas in their PRDs — Aisha on the payments team is great about it. But it's inconsistent. Other PMs don't think about data until after launch. Engineers sometimes add tracking on their own but without coordinating with the data team on schemas. QA doesn't test analytics at all — they test functionality.

The data team is frustrated. They keep getting pulled in after the fact to fix things that should have been part of the original spec. Our lead data analyst, Marcus, told me last week: "If I got involved in the PRD review instead of the post-launch fire, we'd save 30% of my time."

We don't have a formal process for this. There's no data section in our PRD template. There's no analytics QA step. There's no checkpoint where someone asks "do we have the data we need?" before we ship.

---

## What I Need

Can you draft this into a proper standard? I want something that's prescriptive enough that people actually follow it, but not so bureaucratic that it slows us down. The goal is to make data requirements a natural part of how we build — not an afterthought and not a bottleneck.
