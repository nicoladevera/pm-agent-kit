# Competitive Deep Dive Request: Linear — Sprint Planning and Backlog Prioritization

Hey — can you do a competitive deep dive on Linear? Specifically their sprint planning and backlog prioritization workflows. I'm not looking for a feature checklist — I want to understand their philosophy and how they think about this problem.

**Why this matters right now:** We're heading into Series B conversations in the next 90 days. One of the things investors are going to probe is our product differentiation in a market where Linear has momentum and Jira is the default. We're deciding whether to invest significant engineering time in building sprint and velocity tooling before those conversations — or whether to double down on something else. That decision needs to happen in the next two weeks.

**Where we are today:** We have ~200 B2B customers, mostly 10-50 person teams. Our product has basic kanban boards — you can create cards, move them through columns, add assignees and due dates. No sprint tooling, no velocity tracking, no backlog prioritization workflow beyond manual drag-and-drop ordering. It works fine, but it's not differentiated. A number of customers have asked for "sprint planning" — I don't yet know if they mean Linear-style sprints, classic Scrum, or just "a way to group work into time boxes."

**What I've already observed about Linear:**

1. **Issue hierarchy / project structure:** Linear uses a three-level hierarchy: Teams → Projects → Cycles. Issues belong to teams and can be added to cycles. The organization is flatter and more intentional than Jira's — there's no epic/story/sub-task nesting that goes four levels deep. Linear's structure feels like it's designed to reduce overhead, not accommodate every possible org structure.

2. **Cycle-based planning vs. sprints:** Linear calls them "Cycles" not "Sprints." From what I've seen, this is more than naming — they don't default to story points or velocity. You plan cycles by selecting which issues you want to complete. There's a "scope" concept (total issues) and completion tracking, but the system doesn't push you to estimate every ticket in points first. This is a deliberate design choice, not an oversight.

3. **Keyboard-first UX:** Linear is aggressively keyboard-driven. You can do nearly everything with keyboard shortcuts — create issues, change status, move between projects. The experience is clearly built for engineers, not PMs managing a Jira board. I've seen their team describe this as a core principle: "every interaction should feel like using a well-designed IDE."

4. **"No estimates" philosophy:** Linear has been pretty public about not believing story point estimation is useful. Their founder and team have written about this — the idea that points are a proxy for time that doesn't hold up, and that teams are better off shipping and iterating than spending time in planning poker. This isn't just a product gap; it's a stated belief.

What I want to understand: what are the trade-offs behind these choices? What does Linear's philosophy imply about who sprint tooling is actually for, and what it takes to make sprint tooling work? And ultimately — does this help us figure out whether we should build it, and if so, what kind?

This isn't a "should we copy Linear" question. It's a "what can we learn from their approach that helps us make a smarter product bet" question.

— Priya
