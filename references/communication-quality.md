# Communication Quality Criteria

What makes PM communication worth reading. Use this to evaluate status updates, meeting briefs, stakeholder messages, and any artifact meant to inform, align, or drive action. The communication analog to `quality-criteria-prd.md`.

These criteria apply across formats — Slack messages, emails, status docs, meeting prep. The medium changes; the standard doesn't.

---

## The Criteria

### 1. Lead with the Answer or the Ask

The reader should know the point within the first two sentences. Assessment first, then supporting context. Ask first, then background. Never bury the conclusion after three paragraphs of setup.

**Evaluate:** Can you restate the main point from just the opening? If you have to read the whole thing to figure out what it's saying, it's structured wrong.

### 2. Risk Surfaced, Not Buried

Risks are stated early, stated clearly, and stated with severity. Not softened, not minimized, not tucked into the last bullet point. "Slight delay" for a two-week slip is dishonest framing. The "all green" status update is almost always wrong — if everything is genuinely fine, say so explicitly and say why you're confident.

**Evaluate:** Where do risks appear in the communication? Are they in the first half or the last? Is severity stated (high/medium/low, timeline impact, blast radius)? Would a reader who only skimmed the top get an accurate picture?

### 3. Risk Paired with Mitigation

Never name a risk without a proposed mitigation or next step alongside it. A risk without a mitigation creates anxiety; a risk with a mitigation creates confidence that it's being managed. This is a stronger standard than "risk surfaced" (criterion 2) — that criterion ensures risks appear; this one ensures they appear *with a plan*.

**Evaluate:** For every risk named, is there a mitigation, workaround, or next step right next to it? A risk list without actions is an alarm, not a status update.

### 4. Assessment Over Activity

Communication artifacts tell the reader where things stand, not what was done. "We completed 6 stories" is activity. "We're on track for the sprint goal — 6 of 8 stories shipped, the remaining 2 are in review" is assessment. Activity is evidence; assessment is the point.

**Evaluate:** Does the update answer "should I be worried?" or does it just answer "what happened?" If a reader walks away feeling informed but not oriented, it's a list, not an assessment.

### 5. Audience Calibration

Every communication has a reader. VP updates and team updates have different density, different framing, different emphasis. A VP needs the strategic picture — are we on track, what's at risk, what do you need from me. A team needs the operational picture — what's next, what's blocked, what changed. Cross-functional partners need the interface picture — what they need to know, what they need to do, what's coming their way.

**Evaluate:** Is the content pitched at the right level for the reader? Would a different audience need a fundamentally different version? Does it assume context the reader has — or context they don't?

### 6. Resource-Rich

Link to everything referenced — Jira tickets, dashboards, docs, Figma, Slack threads, spreadsheets. Never make the reader go find something. This signals situational awareness and respect for others' time. A status update that says "the dashboard shows a spike" without linking the dashboard creates work for the reader.

**Evaluate:** Could the reader access every artifact mentioned without leaving the communication? Are links inline and specific (not "see Confluence"), or does the reader need to search?

### 7. Name Owners Explicitly

Every action, dependency, risk, and open question has a named person — not "the team" or "engineering" or "TBD." Distinguish between responsible (owns the work) and informed (cc'd for awareness). Unnamed ownership is unowned work.

**Evaluate:** For every action item or risk, can you answer "whose problem is this?" from what's written? Are responsibility and awareness distinguished?

### 8. Structured Naturally

Complex information gets structure — numbered lists, bullet points, nested sub-points, tables. Not because a template demands it, but because structure serves clarity. A five-paragraph wall of text about three workstreams is harder to read than three clearly labeled sections. Structure is a kindness to the reader.

**Evaluate:** Would reformatting the content into a different structure improve readability? If yes, the structure isn't serving the content. Could the reader scan the communication and know where to look for what they care about?

### 9. Warm but Efficient

Acknowledgments are quick and sincere. Tone is collegial, not corporate. Appreciation is genuine, not performative — and it doesn't consume half the message. Warmth in PM communication means the reader feels respected, not managed. Efficiency means every sentence does real work.

**Evaluate:** Does the communication sound like a person who cares about the reader, or like a process generating output? Is the warmth present but not diluting the content?

### 10. Warmth as Load-Bearing Structure

Warmth in PM communication is not decorative — it's what makes directness receivable. "We understand the criticality of the project, and while we will do our best to adapt..." before the delivery risk caveat. "My team has been such champs in adapting fast..." before asking "is this actually final?" The acknowledgment is genuine and brief, and it's placed deliberately so the direct message that follows lands without defensiveness.

**Evaluate:** Is warmth present where directness is highest? Does it feel genuine and brief, or performative and diluting?

### 11. Traffic-Light Signaling for Trade-Off States

Use clear, named status levels (green/yellow/red or equivalent) when communicating evolving trade-off situations. "Last week we were green — we had confidence. As of today, we are in yellow mode — there is more risk than anticipated." This gives the reader a signal they can act on without decoding a paragraph of nuance. Always name what changed, who makes the final call, and when.

**Evaluate:** When communicating a state change or evolving risk, is the signal immediately scannable? Could a reader understand the severity from a single phrase?

### 12. Explicit "Not Doing" List

When communicating priorities under pressure, explicitly name what is NOT getting done — not just what is prioritized. This serves two purposes: it protects the team from inbound requests on deprioritized work, and it makes the trade-off visible rather than silent.

**Evaluate:** When priorities are communicated, would someone reading it know what's been deprioritized? Or would they have to guess?

---

## Using These Criteria

**For evaluation (Analyzer skills):** Check each communication artifact against these criteria. The most important question is always: does the reader walk away knowing what they need to know and what they need to do?

**For generation (Generator skills):** Generate toward these criteria. Every status update, meeting brief, or stakeholder message should satisfy all twelve even under time pressure. It's better to have a shorter, well-structured update than a longer one that buries the point.

**Priority order when time is limited:**
1. Lead with the answer (criterion 1) — nothing else matters if the reader can't find the point
2. Risk surfaced (criterion 2) — the most dangerous failure is a communication that hides bad news
3. Risk paired with mitigation (criterion 3) — a risk without a plan is just an alarm
4. Assessment over activity (criterion 4) — activity without assessment is noise
5. Audience calibration (criterion 5) — wrong audience pitch wastes the reader's time
6. Everything else follows from there
