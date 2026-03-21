# Decision Input: Build vs. Buy — Notification System

**Source:** Slack thread excerpts from #lending-platform, March 12-13

---

**@sarah.chen (Engineering Lead)** — Mar 12, 2:14 PM
So the payment reminder PRD requires a notification service that can handle scheduling, templating, multi-channel delivery (push + in-app for now, SMS later). We don't have anything like this today. I've been looking at a few options and honestly I think we should just build it. We already have Kafka for event streaming and FCM for push — we'd just need the scheduling layer and template engine.

**@dev.patel (Backend Engineer)** — Mar 12, 2:31 PM
I've used Customer.io at my last company and it handled all of this out of the box. Scheduling, templates, multi-channel, analytics. Took maybe 2 weeks to integrate vs the 6-8 weeks I'd estimate for building our own.

**@sarah.chen** — Mar 12, 2:45 PM
True but then we're dependent on a third-party for a critical path. If their API goes down during a payment window, users miss reminders. Plus the per-message pricing gets expensive at our volume — 150K active installment users, multiple reminders per cycle.

**@dev.patel** — Mar 12, 3:02 PM
Fair point on the volume pricing. But building our own means we also own the maintenance, the on-call, the edge cases. We're already stretched thin this quarter.

**@maria.gonzalez (PM Lead)** — Mar 12, 3:15 PM
This is a good debate. A few things I want us to consider:
- We need reminders live for the Mexico launch in Q2. That's ~10 weeks from now.
- Whatever we build needs to support at least 3 markets by Q4 (Mexico, Philippines, Kenya)
- The lending support agent also needs notification capabilities for case updates, so this isn't just for payment reminders

**@sarah.chen** — Mar 12, 3:30 PM
The multi-product point is actually strong for building our own. If lending support, payment reminders, and eventually marketing all need notifications, a shared service pays for itself. Customer.io would be a separate integration for each use case.

**@james.wu (SRE)** — Mar 12, 4:15 PM
From an ops perspective, I'd rather own the critical path than depend on Customer.io SLA for payment reminders. We can build in the retry and fallback logic we actually need. Their reliability page shows 99.9% uptime which sounds fine but that's ~8.7 hours of downtime per year, some of which could land on payment windows.

**@dev.patel** — Mar 13, 9:00 AM
After sleeping on it, I think the build approach makes sense IF we can staff it properly. My concern is that we're committing to 6-8 weeks of eng time when we're already carrying over work from last sprint. Can we actually absorb this?

**@maria.gonzalez** — Mar 13, 9:30 AM
Good question. @sarah.chen — can you put together a rough resource plan? I want to make sure we're not just saying "build" without being honest about the capacity cost. Let's discuss in Thursday's planning meeting and make the call then.

**@sarah.chen** — Mar 13, 10:00 AM
Will do. I'll have estimates by Thursday.

---

**Note from PM:** I think we're leaning build, but I want to make sure we've properly thought through this. The thread kind of trailed off — I don't think we actually made a final decision yet. Can you help me structure this for Thursday's meeting?
