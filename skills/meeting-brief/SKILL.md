---
skill: meeting-brief
type: Generator
tier: 2
approval: draft-confirm
context-required: []
context-optional:
  - company/facts/team.md
  - company/norms/communication.md
  - company/facts/product.md
degradation: proceed-with-caveat
---

# meeting-brief

Prepare a pre-meeting brief that ensures attendees arrive ready to decide, not ready to catch up. A meeting without a brief is a meeting where the first 15 minutes are wasted on context-setting that could have been a pre-read.

Planning is caring. The PM who prepares a meeting brief demonstrates respect for every attendee's time and investment in productive collaboration.

---

## What It Accepts

Any form of meeting context:
- A meeting agenda (formal or informal)
- A calendar invite with attendees and topic
- A description of what the meeting is about
- Notes about what needs to be discussed
- A combination of the above — e.g., a calendar invite plus a few Slack messages about what people want to cover

The input does not need to be complete. If the agenda is vague ("Sprint review + planning discussion + Q2 priorities"), the skill imposes structure.

---

## Intake

A meeting brief without a clear objective structures activity, not outcomes. Confirm what the meeting needs to produce.

### Signals to Check

- **Meeting objective:** Is there a stated outcome — what should be true after this meeting that isn't true before?
- **Attendees:** Are attendees listed or inferable?
- **Agenda or topics:** Is there an agenda, even rough?

### Adaptive Response

**Rich input** (objective stated, attendees listed, agenda provided): Confirm and proceed. Example: "Objective: [X]. [N] attendees. [N] agenda items, [N] with decisions. Drafting the brief."

**Moderate input** (agenda present but objective unstated): Ask one targeted question:
- "What outcome do you need from this meeting? What should be decided or resolved by the end?"

**Thin input** (just a meeting title or a vague description): Present a structured interpretation:

> **Here's what I'm inferring about this meeting — adjust as needed:**
>
> - **Objective:** [Inferred from title/description — e.g., "Align on Q2 priorities and assign owners"]
> - **Key decisions:** [What I think needs deciding, based on the topics]
> - **Who matters most:** [If attendees are listed, who has the highest stakes; if not, "attendees not specified — I'll draft without the stakes section and you can add them"]
>
> Does that match your intent for this meeting?

---

## Instructions

### 1. Read the input fully

Identify from the input: meeting purpose, attendees (if listed), topics or agenda items, any prior context referenced, meeting duration (if known), and any Slack messages or notes providing additional context.

### 2. Load reference files

Read these files:
- `references/communication-quality.md` — Quality criteria for the brief itself (audience calibration, structured naturally, lead with the point)
- `references/decision-frameworks.md` — For identifying and framing decisions on the table
- `references/audience-registers.md` — For mapping attendee communication preferences and calibrating the brief's register
- `references/agent-readable-output.md` — Agent Block format and shared enum vocabulary

### 3. Load company context (if available)

If `company/facts/team.md` exists and is substantive, read it for attendee roles, their stakes, and team structure context.

If `company/norms/communication.md` exists and is substantive, read it for meeting culture, expected formats, and how different stakeholders prefer to engage.

If `company/facts/product.md` exists and is substantive, read it for product context relevant to the meeting topics.

If any of these files exist but are still stub templates, treat them as unavailable and say so in the output.

If no substantive company context is available, proceed — note the absence in the output. The brief will be less specific about attendee stakes and company-specific context.

### 4. Define the meeting objective

State what should be true after this meeting that isn't true before it. This is the most important sentence in the brief.

If the input states the objective, use it. If it doesn't (most meeting invites don't), infer it from the agenda items and flag the assumption: "Inferred objective based on agenda — confirm this matches your intent."

A meeting can have multiple objectives, but more than 3 means the meeting is trying to do too much.

### 5. Map attendees and stakes

For each attendee (if known):
- Their role and what they own
- What they care about in this meeting specifically — not their generic job description, but their stake in these particular topics
- What context they may be missing that others have
- What they need from this meeting (a decision, information, alignment, input)

If company context provides attendee details, use it. If attendees aren't listed in the input, note the gap and offer to update the brief when attendees are known.

### 6. Structure each agenda item

For each topic or agenda item:
- **Current status** — Where things stand right now. What happened since the last time this was discussed (if known).
- **Open questions** — What's unresolved. What needs discussion.
- **Decision needed?** — Yes or no. If yes: what's being decided, what the options are (if known), and who is the decider.

Distinguish between topics that need discussion (open questions, differing perspectives) and topics that are FYI (status updates, announcements). A brief that treats everything as equally important fails to prioritize the attendees' attention.

### 7. Surface decisions explicitly

Pull all decisions out of the agenda items and list them in a dedicated section. For each decision:
- The decision question
- The known options (if any)
- Who decides
- What information the decider needs

This section exists because decisions often hide inside discussion topics. Making them explicit means the meeting can allocate time appropriately.

**For escalation or decision meetings** — where the meeting exists to get leadership to make a hard call — frame the decision as a fork: "Here are the two paths. Path A: [description, consequences]. Path B: [description, consequences]. We need to leave this meeting knowing which path." This structure prevents the meeting from dissolving into discussion without a resolution. Name the specific commitment you're asking leadership to make.

### 8. List pre-reads and context

What should attendees review before the meeting? Documents, dashboards, data, Slack threads, previous meeting notes. Link to everything — never make someone search. If you're referencing something, provide the path or URL.

### 9. Suggest time allocation

If the meeting duration is known, propose a time split across agenda items. Weight by:
- Topics needing decisions get more time
- FYI topics get less time
- Buffer for discussion overflow on high-stakes items

If duration isn't known, skip this section.

---

## Output Format

```markdown
## Meeting Brief: [Meeting Title]

**Date:** [Meeting date]
**Duration:** [Length, if known]
**Objective:** [What should be decided, aligned on, or resolved by the end of this meeting.]

<!-- AGENT BLOCK -->
```yaml
agent_block:
  skill: meeting-brief
  decision_count: [integer]
  undecided_decider_count: [integer — decisions with no assigned decider]
  attendee_count: [integer]
  pre_read_required: [Yes / No]
```
<!-- /AGENT BLOCK -->

---

### Attendees & Stakes

| Attendee | Role | What they care about in this meeting |
|----------|------|--------------------------------------|
| [Name] | [Role] | [Their specific stake in these topics] |
| [Name] | [Role] | [Their specific stake] |

---

### Agenda with Context

#### 1. [Topic]
**Status:** [Where things stand]
**Open questions:** [What's unresolved]
**Decision needed?** [Yes/No — if yes, what decision and who decides]

#### 2. [Topic]
**Status:** [Where things stand]
**Open questions:** [What's unresolved]
**Decision needed?** [Yes/No]

[Continue for each topic]

---

### Decisions on the Table

1. **[Decision question]** — Options: [if known]. Decider: [who].
2. **[Decision question]** — [...]

---

### Pre-Read / Context

- [Document, dashboard, or reference — with link or path]
- [...]

---

### Suggested Time Allocation

| Topic | Minutes | Why |
|-------|---------|-----|
| [Topic 1] | [X] | [Decision required / Quick update / Needs discussion] |
| [Topic 2] | [X] | [...] |

> **Context note:** [State which substantive company files were loaded, which files were absent, and which files existed but were stub templates and therefore skipped. Also note whether the attendee list was available and what the brief might miss without fuller context.]
```

---

## Quality Bar

- **Would attendees arrive better prepared?** The brief gives each person what they need to contribute meaningfully from minute one — not spend the first 15 minutes getting oriented.
- **Are decisions explicitly named?** Not buried in discussion topics. A reader can scan the brief and know exactly what's being decided today.
- **Are attendee stakes specific?** Not "stakeholder engagement" — what does this particular person care about in this particular meeting?
- **Does it distinguish discussion from FYI?** The brief signals which topics need the room's energy and which are informational.
- **Would the PM save time preparing?** The brief reduces prep work to reviewing and adjusting — not writing the prep from scratch.
