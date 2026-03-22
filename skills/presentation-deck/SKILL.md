---
skill: presentation-deck
type: Generator
tier: 4
approval: draft-confirm
context-required: []
context-optional:
  - company/facts/product.md
  - company/facts/team.md
  - company/norms/communication.md
  - company/interfaces/branding.md
degradation: proceed-with-caveat
---

# presentation-deck

Draft a structured narrative for a specific audience and purpose, then optionally generate an actual `.pptx` presentation file. Two modes: **Narrative** (markdown slide-by-slide structure with headlines, content, visual guidance, and speaker notes) and **Slides** (generates a branded `.pptx` file using `python-pptx` at runtime). The narrative is the thinking; the slides are the delivery.

---

## What It Accepts

Any content that needs to become a presentation narrative:
- A business case (from `knowledge/business-cases/` or pasted inline)
- A PRD or product proposal
- A status update or quarterly results
- A competitive analysis or data analysis
- A decision that needs stakeholder alignment
- Rough notes, bullet points, or a verbal download
- A combination of the above

The input provides the content. The skill provides the narrative structure, audience calibration, and visual translation.

**Required invocation inputs:** Two things must be specified:
1. **Audience** — Who is this presentation for? (e.g., "my VP," "the board," "the engineering team," "a new stakeholder")
2. **Purpose / deck type** — What type of presentation? (e.g., "exec review," "QBR," "product explainer," "board update," "stakeholder onboarding")

If either is missing, ask: "Who is the audience for this presentation, and what type of deck is it (exec review, QBR, product explainer, board update, stakeholder onboarding)?"

---

## Modes

This skill operates in two modes. The PM selects the mode through how they invoke it.

### Narrative

Produce a markdown slide-by-slide structured narrative. Each slide has a takeaway headline, supporting content, visual guidance, and speaker notes. Use this when the PM wants to draft the story before building slides, or when working in a tool that isn't PowerPoint.

**Triggered by:** "draft a deck," "outline the presentation," "structure the deck," "create a presentation narrative," or any invocation that doesn't explicitly request a file.

### Slides

Generate an actual `.pptx` file using `python-pptx`, with branding applied from `company/interfaces/branding.md` when substantive. Produces a presentation-ready file the PM can open in PowerPoint or Google Slides. If a requested visual or template behavior can't be rendered cleanly, use a simpler treatment and note that fallback.

**Triggered by:** "generate slides," "create the .pptx," "build the PowerPoint," "make the presentation file," "generate a slide deck," or any invocation that explicitly requests a file output.

**Default:** If the mode is ambiguous, use Narrative and note: "This is a narrative draft. If you'd like a .pptx file, invoke with 'generate slides' or 'create the .pptx.'"

---

## Instructions

### Shared Steps (Both Modes)

#### 1. Read the input fully

Absorb all content before structuring. Understand what's being communicated, who the audience is, what purpose the presentation serves, and what the PM wants the audience to do or take away. Note what the input provides and what's missing.

#### 2. Load reference files

Read these files:
- `references/narrative-structure.md` — Narrative arc (SCR), deck types, slide-level thinking, audience calibration, visual guidance conventions, speaker notes standards
- `references/communication-quality.md` — Lead with the answer, assessment over activity, audience calibration, risk surfaced not buried
- `references/pm-smell-test.md` — Check for smells 4 (audience mismatch), 6 (activity reported as progress), and 12 (risk buried or absent)

#### 3. Load company context (if available)

If `company/facts/product.md` exists and is substantive, read it for product landscape context that may need to appear in the presentation.

If `company/facts/team.md` exists and is substantive, read it for organizational context, stakeholder relationships, and who reports to whom — this informs audience calibration.

If `company/norms/communication.md` exists and is substantive, read it for how the company communicates and specific stakeholder preferences (e.g., "VP prefers data-first presentations," "board expects a strategic frame before operational detail").

If any of these files exist but are still stub templates, treat them as unavailable and say so in the context note.

#### 4. Identify deck type

From the PM's stated purpose and audience, classify the deck type per `references/narrative-structure.md`:

- **Exec Review** — Decision-oriented. VP/C-suite. Problem, data, recommendation, ask. 8-12 slides.
- **QBR** — Assessment-oriented. Leadership + cross-functional. Results, learnings, priorities. 15-20 slides.
- **Product Explainer** — Education-oriented. New stakeholders, partners. What, who, how, what's coming. 10-15 slides.
- **Board Update** — Strategic. Board members. Market position, metrics, decisions, asks. 8-12 slides.
- **Stakeholder Onboarding** — Context-setting. New team member, exec, partner. Landscape, team, process, current state. 12-18 slides.

If the deck type is ambiguous from the invocation, ask. State the identified deck type and why.

#### 5. Determine the narrative arc

Every presentation follows the Situation → Complication → Resolution (SCR) arc from `references/narrative-structure.md`:

- **Situation:** Where we are. What the audience already agrees is true. Current state, context, shared understanding.
- **Complication:** Why the current situation isn't sufficient. What changed, what's at risk, what opportunity exists.
- **Resolution:** What we propose. The recommendation, the plan, the ask.

Map the input content to this arc. The situation might be one slide or three. The complication might unfold across data and competitive context. The resolution might span a recommendation, plan, and explicit ask. But the macro arc must be clear.

#### 6. Calibrate to audience

Per `references/narrative-structure.md` and `references/communication-quality.md`, calibrate for the specific audience:

- **VP/C-suite:** Start with the recommendation. Evidence follows. High-level. One chart, not five.
- **Board:** Start with the strategic question. Market context before operational detail. Every slide matters at board scale.
- **Peer/team:** Start with context. Full analytical depth. Peers expect the detail.
- **Cross-functional:** Start with "what this means for you." Dependencies, timeline, their involvement.

If `company/norms/communication.md` has specific stakeholder preferences, apply them.

#### 7. Draft the slide sequence

Create each slide as a markdown section. Per `references/narrative-structure.md` slide-level thinking:

For every slide:
- **Headline:** A takeaway, not a topic label. The reader should be able to read all headlines in order and follow the full argument. "Q3 Results" is a topic. "Q3 activation exceeded target by 12%, driven by onboarding redesign" is a takeaway.
- **Content:** Supporting evidence, data, or narrative that proves the headline. Structured for a slide (bullets, short text, or data), not a document paragraph.
- **Visual:** What visual would support this content — chart type, diagram, screenshot, or text-only. Per visual guidance conventions in `references/narrative-structure.md`.
- **Speaker notes:** Context the slide doesn't show, anticipated questions, what to emphasize, transition to the next slide. Per speaker notes standards in `references/narrative-structure.md`.

Each slide earns the next. The implicit "so what?" at the end of each slide is answered by the following one. If two adjacent slides have no logical connection, the narrative is broken.

Include appendix slides for supporting data, detailed analysis, or backup for anticipated questions. Appendix slides don't clutter the main narrative but are available if needed.

#### 8. Stress-test the narrative

For **Exec Review** and **Board Update** decks (high-stakes, decision-oriented), always run:

**Narrative Premortem:**
*"If this presentation fails to land, what went wrong?"*
- Is the ask buried instead of up front?
- Is there an audience mismatch (wrong detail level, wrong framing)?
- Is critical data missing or unconvincing?
- Is the narrative arc unclear — would the audience lose the thread?

**Audience Blindspot:**
*"What does this audience care about that I haven't addressed? What question will they ask that I haven't anticipated?"*
- What's the audience's known concern that the deck should address proactively?
- What context does the audience have (or lack) that affects how they'll receive this?
- What's the most likely pushback, and is it addressed in the narrative?

For other deck types (QBR, Product Explainer, Stakeholder Onboarding), these stress-test steps are optional but recommended for any deck where the stakes warrant it.

#### 9. Run the smell test

Check for:
- **Smell 4 (Audience Mismatch):** Is the content calibrated for who's reading it? Engineering detail for a board? Strategic framing for a sprint review? Feature walkthrough for a VP who needs to make a funding decision?
- **Smell 6 (Activity Reported as Progress):** Does the presentation tell the audience where things stand, or just what was done? A QBR that lists completed features without assessing impact. A status deck that reports activity without assessment.
- **Smell 12 (Risk Buried or Absent):** Are risks surfaced prominently, or tucked into the last slide? Would the audience walk away with an accurate picture of what's at risk?

---

### Slides Mode (Additional Steps)

#### 10. Load branding context

Read `references/branding-guidelines.md` for slide layout standards, visual consistency rules, and how to apply branding.

If `company/interfaces/branding.md` exists and is substantive, read it for company-specific brand values: color palette (hex values), typography (font names), logo (file paths), and slide defaults.

If branding context is missing or stub-level, use the clean professional defaults from `references/branding-guidelines.md` and flag that default branding was applied in the context note.

#### 11. Generate .pptx file

**Dependency:** Slides mode requires the `python-pptx` Python package (`pip install python-pptx`).

Using `python-pptx`, generate a presentation file that applies branding to the narrative drafted in step 7:

- Create a slide for each section in the narrative (including title slide and section dividers)
- Apply the appropriate slide layout per slide type (title, content, data, comparison, quote, closing) from `references/branding-guidelines.md`
- Set fonts to the brand typography (or documented defaults if unavailable)
- Apply brand colors to headlines, accents, and chart elements
- Place the logo per brand guidelines (if a logo file path is provided)
- Add speaker notes from the narrative draft to each slide's notes section
- If a requested visual cannot be rendered cleanly with `python-pptx`, use a simpler text or table treatment and note the fallback in the context note
- Save the file to `knowledge/presentations/` using the naming convention: `YYYY-MM-DD-descriptive-slug.pptx`

Report the file path, branding source, any fallback behavior, and a summary of the slide sequence in the conversation.

---

## Output Format

### Narrative Mode

```markdown
## Presentation: [Title]

**Deck type:** [Exec Review / QBR / Product Explainer / Board Update / Stakeholder Onboarding]
**Audience:** [Who — be specific]
**Purpose:** [What the audience should decide, learn, or take away]
**Estimated length:** [N slides]

---

### Narrative Arc

**Situation:** [Where we are — 1-2 sentences]
**Complication:** [Why that's not enough — 1-2 sentences]
**Resolution:** [What we propose — 1-2 sentences]

---

### Slide 1: [Takeaway headline — not a topic label]

[Content — data, narrative, key points. Structured for a slide, not a document paragraph.]

**Visual:** [Chart type, diagram, screenshot, or text-only. Specific enough that the PM knows what to create.]
**Speaker notes:** [What to say beyond what's on the slide. Anticipated questions. Emphasis points. Transition to next slide.]

---

### Slide 2: [Takeaway headline]

[Content]

**Visual:** [Guidance]
**Speaker notes:** [Notes]

---

[Continue for each slide in the main narrative]

---

### Appendix

#### A1: [Backup Slide Title]

[Supporting data or detail for anticipated questions]

**Visual:** [Guidance]

---

[Continue for each appendix slide]

---

### Stress Test

<!-- Included for Exec Review and Board Update. Recommended for other high-stakes deck types. -->

#### Narrative Premortem
*"If this presentation fails to land, what went wrong?"*
- [Potential failure mode — and whether the narrative addresses it]

#### Audience Blindspot
*"What does this audience care about that I haven't addressed?"*
- [Missing perspective or anticipated question — and whether it's in the deck]

---

### Smell Test

- **Smell 4 (Audience Mismatch):** [Finding — or "Clear — content calibrated for stated audience"]
- **Smell 6 (Activity as Progress):** [Finding — or "Clear — assessment over activity throughout"]
- **Smell 12 (Risk Buried):** [Finding — or "Clear — risks surfaced prominently"]

> **Context note:** [State the identified deck type and how it was determined. State which substantive company files were loaded, which were absent, and which were stub templates. Note how missing context may have affected audience calibration or content completeness.]
```

### Slides Mode

Output in conversation:

```markdown
## Generated Presentation: [Title]

**File:** `knowledge/presentations/[filename].pptx`
**Deck type:** [Type]
**Audience:** [Who]
**Slides:** [N total — N main + N appendix]
**Branding:** [Company brand applied / Default branding (company branding unavailable)]

### Slide Sequence

1. **[Slide 1 headline]** — [Slide type: title / content / data / etc.]
2. **[Slide 2 headline]** — [Slide type]
3. ...

### Stress Test

[Same as Narrative mode, if applicable]

### Smell Test

[Same as Narrative mode]

> **Context note:** [Same as Narrative mode, plus note on branding source]
```

---

## Quality Bar

- **Does every slide headline state a takeaway, not a topic?** "Q3 Results" fails. "Q3 activation exceeded target by 12%" passes. The reader knows the point of every slide from the headline alone.
- **Is the narrative arc coherent?** The deck tells a story from situation through complication to resolution. Each slide earns the next. A reader could follow the headline sequence alone and understand the argument.
- **Is it calibrated to the audience?** A VP gets the recommendation first. A board gets the strategic frame first. A new stakeholder gets the context first. The right level of detail, the right framing, the right emphasis.
- **Would the PM save real time?** The output is a complete draft the PM can transfer to slides (Narrative mode) or open directly (Slides mode), not a generic outline the PM has to fill in. Specific content, not placeholder text.
- **Are speaker notes useful?** They add context the slide doesn't show, anticipate questions, and guide delivery. Not just "discuss this slide."
- **Does the visual guidance help?** The PM knows what type of chart, diagram, or visual to create for each slide. Not just "add a visual."
- **[Slides mode] Is branding applied consistently?** Fonts, colors, logo placement, and layouts are consistent across all slides. The output looks professional, not like a default template with content pasted in.
- **[Slides mode] Are Slides limitations handled honestly?** If a requested visual or template behavior couldn't be rendered cleanly in `python-pptx`, the output uses a simpler treatment and notes the fallback instead of implying custom-template fidelity it doesn't have.
