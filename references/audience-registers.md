# Audience Registers

Every PM communication has an audience, and each audience has a specific register — a combination of depth, tone, framing, and what's emphasized vs. omitted. Generic "know your audience" is useless. Specific behavioral profiles are actionable.

These registers are not templates. They're behavioral defaults — how a strong PM instinctively adjusts when switching from an engineering sync to a VP update to a cross-functional standup. Skills that produce communication artifacts should consult these profiles when calibrating output.

---

## 1. Engineers / Technical Partners

- Comfortable at system and API depth: product types, endpoints, schema tables, configurations. Stay in the what/why lane — not the how. Engineers own the how; the PM's job is to make the what and why unambiguous.
- Bring engineers into decisions early rather than handing them fully-baked requirements. Collaboration beats handoff. A PRD that arrives without prior engineering conversation has already failed the relationship.
- Hold to process standards explicitly. If the team agreed to a PR review cadence or a ticket format, name the standard when it slips — don't let it erode silently.
- Critical feedback surfaces in private channels, not public threads. A DM or a 1:1 is the right venue for "this isn't meeting the bar." A Slack channel is not.
- Produce technical artifacts (architecture diagrams, schema proposals, data flow sketches) and ask for verification — don't just delegate. Showing your own technical thinking earns credibility and produces better feedback than asking engineers to start from zero.

---

## 2. Designers

- Delegate with clarity: scope asks tightly (specific screens, components, timelines), provide existing designs as anchors. Vague asks like "can you take a look at the onboarding flow" create unnecessary ambiguity about what's being requested.
- Not prescriptive about visual solutions — give room to execute. Define the outcome and the constraints; let design own the execution. "Users need to understand their balance before confirming" is better than "put the balance in a blue box at the top."
- Feedback tied to outcome and consistency, not aesthetic preferences. "This doesn't match the pattern we use for confirmation screens" is actionable. "I don't love the color" is not PM feedback.
- Check org structure before assigning — respect design team processes. Design teams often have their own prioritization, sprint structure, and intake process. Route through the right channel rather than going directly to an individual designer.
- Critical quality feedback goes through back-channels. Same principle as engineering — public critique undermines trust. Private, specific, outcome-oriented feedback builds it.

---

## 3. Data / Analytics

- Arrive with hypotheses and metric definitions already formed — not "can you look into this?" The question "what's happening with retention?" creates a research project. "I think 30-day retention dropped because of the onboarding change on March 3rd — can you confirm?" creates a focused analysis.
- Specify expected behavior, not just labels. Define denominators, transaction types, cardinality changes, and edge cases. "DAU" means nothing without agreeing on what counts as active.
- Surface your own partial analysis to reduce back-and-forth. If you've already pulled numbers from a dashboard or done a rough cut in a spreadsheet, share it. It gives the analyst a starting point and demonstrates you've done your homework.
- Self-serve when the analytics team is bottlenecked — share methodology as a model. If you pulled the data yourself, document the query or the approach so the analyst can validate rather than rebuild.
- Maintain coordination infrastructure for analysis work (trackers, DRIs, timelines). Analysis requests without deadlines and owners drift. Treat data requests with the same rigor as engineering tickets.

---

## 4. Leadership / Stakeholders

- Structured headers consistently: Status, What's Great, Challenges/Risks, Next Steps. Leadership reads fast and scans for signals. Predictable structure means they know exactly where to look.
- Every risk paired with a mitigation — never surface ambiguity or open questions upward without a plan. "We're at risk of missing the deadline" creates anxiety. "We're at risk of missing the deadline — we've descoped feature X and moved the dependency to an async review to recover 3 days" creates confidence.
- Translate complexity into clean signals. Confident and resolved tone. Leadership doesn't need to understand the implementation detail — they need to understand the state, the risk, and the plan.
- Anticipate their questions — lead with what's NOT the problem before naming what is. "Team velocity is strong, no staffing concerns, and the integration is on track. The risk is on the vendor side: their API delivery slipped by a week." This eliminates three questions before they're asked.
- Frame proposals strategically: anticipate objections, name the right sponsor, sequence who needs to be on board first. A proposal that lands in a leadership meeting without pre-alignment is a proposal that gets tabled.

---

## 5. Direct Manager

- More raw and exploratory than any other register. This is the relationship where half-formed thinking is not just acceptable — it's valuable.
- Surface concerns before having answers. "I'm worried about X but I don't have a plan yet" is exactly the kind of signal a good manager wants early.
- Use as a sounding board for strategic framing before taking it wider. Test the narrative, the positioning, the trade-off framing. A direct manager can tell you whether your read on the room is right before you walk into it.
- Don't over-polish for this audience. The manager's value comes from seeing the thinking in progress, not the finished artifact. A rough draft with questions is more useful than a polished draft that hides uncertainty.

---

## 6. Cross-Functional Coordination

- Name DRIs, consolidate threads, create shared artifacts (trackers, summaries, docs) for a single source of truth. Cross-functional work fails when information lives in five Slack channels and nobody knows which one is current.
- Be both the connective tissue and the team advocate. The PM's job in cross-functional settings is to represent the team's capacity and constraints honestly while keeping the broader initiative moving.
- Even during ambiguity, give the team a clear standing instruction ("no changes to current sprint goals, proceed as planned"). Silence during uncertainty is worse than a provisional direction that might change.
- Actively protect the team from unnecessary context-switching and scope whiplash. If a cross-functional partner is requesting changes mid-sprint, the PM absorbs that conversation — not the engineers.
- When coordinating across teams, create the shared artifact first. Don't wait for someone else to set up the tracker or write the summary. The PM who creates the coordination doc becomes the coordination point — and that's the right place to be.

---

## 7. What Stays Constant

Across every audience, these elements don't change:

- **Structured formatting.** Headers, bullets, tables. The medium adapts; the commitment to scannability doesn't.
- **Mitigation-ready risk framing.** Every risk names what's being done about it. No audience gets naked risk.
- **Named ownership on every action.** "The team" is not an owner. A person is.
- **Doc-anchored communication.** Slack for coordination, but the source of truth is always a linked document, dashboard, or artifact — never a chat message.
- **Warmth as a constant.** The register changes — depth, tone, framing all shift by audience. The warmth doesn't. Every audience should feel respected, not processed.
