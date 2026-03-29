# Sample Input: Rough Problem Statement (B2B SaaS)

This is what a PM might drop into a conversation when they want to draft a PRD. It's deliberately messy, mixed together, and conversational.

---

Hey, I need a PRD for a shared inbox feature we've been talking about for months. Here's my brain dump — sorry it's messy.

So here's the situation. Right now all our enterprise customer support agents are handling incoming requests through a shared Gmail inbox, and it's a total disaster. The core problem is collision: two agents will sometimes reply to the same customer ticket without realizing it, the customer gets two contradictory answers, and then we have a mess to clean up. We also have zero visibility into who's working on what — there's no audit trail, no way to see if someone already picked up a ticket, and no way for a team lead to understand workload distribution.

We interviewed 8 support leads across our enterprise customers and every single one of them cited inbox chaos as their top operational pain. These are 10-50 person support teams with dozens of incoming requests per day. The quotes were brutal: "we've had customers get 3 different answers in one day," "my agents are stepping on each other constantly," "I have no idea who owns what on any given day."

**What I want to build:**

A shared team inbox inside our platform where support agents can collaborate on incoming customer requests. The core idea is that each incoming message becomes a "ticket" and only one agent can be actively working it at a time (claimed/unclaimed states). Agents should be able to reassign tickets to their teammates. We could add internal notes so agents can leave context for each other without the customer seeing it. When an agent claims a ticket, other agents can see it's taken and move on to unclaimed ones.

**How it should work (roughly):**

When a new customer message comes in, it appears in the shared inbox as unclaimed. Any agent can open it and claim it — at that point, it moves from the unclaimed queue to their personal queue and other agents see it as "in progress / owned by [name]." The agent responds to the customer, and once the issue is resolved, they mark it closed. If they can't handle it, they can reassign to another agent with a note explaining why. Internal notes should be visible to the whole team but hidden from the customer.

**Constraints:**
- We already have a customer messaging API that delivers inbound messages — this is a UI/workflow layer on top of that
- Mobile web needs to work (agents use tablets in some support centers) but native mobile is out of scope for this phase
- Our platform is already multi-tenant; this feature needs to respect team boundaries (Agent A from Company X can't see Company Y's inbox)
- Engineering team is 4 people and we have one sprint until our enterprise renewals cycle starts — scope needs to be tight

**What I haven't figured out yet:**
- We want to reduce response time but I don't know what our current average response time actually is — I should probably pull that from Zendesk before we launch
- Not sure if we should launch to all customers at once or gate this to enterprise tier first

I think this is a strong enough problem that we should move fast. Can you draft the PRD?
