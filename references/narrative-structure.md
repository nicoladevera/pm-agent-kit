# Narrative Structure

What makes a structured narrative effective for different audiences and purposes. Use this to draft presentations, structure executive communications, and translate analytical work into persuasive storytelling. The presentation counterpart to `communication-quality.md` — that file covers quality criteria for PM communications generally; this file covers the specific craft of building a narrative for a deck.

A presentation is not a document reformatted as slides. A document explains. A presentation persuades, informs, or aligns — and it does so through a narrative arc where each slide earns the next. If you can reorder the slides without losing meaning, there's no narrative.

---

## Narrative Arc

### Situation → Complication → Resolution (SCR)

Every PM presentation follows this core structure, adapted from the Minto Pyramid Principle:

| Element | What it does | In a PM context |
|---------|-------------|-----------------|
| **Situation** | Establishes shared context. Where we are. What the reader already agrees is true. | Current product state, market position, recent results, established goals. |
| **Complication** | Introduces tension. Why the current situation isn't sufficient. What changed, what's at risk, what opportunity exists. | A gap, a competitive threat, a user problem, a missed target, a market shift. |
| **Resolution** | Proposes the path forward. What we should do about the complication. | The recommendation, the plan, the investment case, the decision. |

**The arc shapes the entire deck, not just the introduction.** The first few slides establish the situation. The middle slides develop the complication with evidence. The final slides present the resolution with enough support to act on.

**Not every slide maps to one element.** The situation might be one slide or three. The complication might unfold across a data section and a competitive section. The resolution might span a recommendation, a plan, and an ask. But the macro arc — we're here, this is the problem, here's what we should do — must be clear.

**Red flag:** A deck where the resolution appears on slide 2 and the remaining 15 slides are supporting evidence. That's a document, not a presentation. Lead with the conclusion when the audience wants efficiency (VP update), but the arc should still be present in the structure.

---

## Deck Types and Their Purposes

Different presentations serve different purposes and have different structural expectations.

| Deck Type | Purpose | Typical Audience | What They Decide or Take Away | Key Sections | Typical Length |
|-----------|---------|-----------------|------------------------------|-------------|----------------|
| **Exec Review** | Get a decision or approval on a specific initiative. | VP, C-suite, leadership team | Whether to fund, prioritize, or approve the initiative. | Recommendation (up front), problem, impact, plan, risks, ask. | 8-12 slides |
| **QBR** | Assess performance and align on priorities for next quarter. | Leadership + cross-functional | What worked, what didn't, what to focus on next. | Results vs. targets, key learnings, themes, next quarter priorities, resource asks. | 15-20 slides |
| **Product Explainer** | Educate someone on what the product does and why. | New stakeholders, partners, cross-functional teams | Understanding of the product, its users, and its direction. | What it does, who it's for, how it works, key metrics, what's coming. | 10-15 slides |
| **Board Update** | Provide strategic context and surface decisions that need board input. | Board members | Market position confidence, strategic alignment, resource needs. | Market context, key metrics, strategic decisions, risks, asks. | 8-12 slides |
| **Stakeholder Onboarding** | Bring someone up to speed on the product landscape and current work. | New team member, new exec, new partner | Sufficient context to be a productive contributor or stakeholder. | Product overview, team, process, current state, recent history, upcoming work. | 12-18 slides |

### Choosing the Right Type

If the PM specifies the deck type, use it. If they specify audience and purpose but not a type, match based on the table above. If the match is ambiguous, ask.

---

## Slide-Level Thinking

### Headlines Are Takeaways, Not Topics

Every slide headline should state the conclusion or takeaway of that slide. The reader should be able to read the headlines in sequence and understand the full argument.

| Topic label (wrong) | Takeaway headline (right) |
|---------------------|--------------------------|
| Q3 Results | Q3 activation exceeded target by 12%, driven by onboarding redesign |
| Competitive Landscape | PayFlex's free tier launch signals a pricing war we're not positioned for |
| User Feedback | Three of five top pain points trace to a single onboarding flow |
| Proposed Investment | A $200K investment in self-service tooling would eliminate 40% of support tickets |
| Next Steps | We need a decision on funding by March 15 to hit the Q2 launch window |

**Test:** Can you read just the headlines of the entire deck, in order, and follow the argument? If yes, the headlines are working. If no, they're topic labels.

### Supporting Content Proves the Headline

The content below the headline is evidence: data, analysis, examples, or context that supports the claim the headline makes. If the headline says "activation exceeded target by 12%," the content shows the numbers. If the headline says "three pain points trace to one flow," the content shows the mapping.

**Red flag:** Content that contradicts or doesn't support the headline. A headline that claims success with content showing mixed results. This destroys credibility faster than a weak headline.

### "So What" Connects to the Next Slide

Every slide should make the reader want to see the next one. The implicit question at the end of each slide is "so what?" — and the next slide answers it.

- Slide: "Activation exceeded target by 12%." → So what? → Next slide: "The gain was driven by onboarding redesign, validating our Q2 bet."
- Slide: "The gain was driven by onboarding redesign." → So what? → Next slide: "This validates extending the approach to the upgrade flow in Q3."

If two adjacent slides have no logical connection, the narrative is broken.

---

## Audience Calibration for Decks

Different audiences need different framing of the same content.

### VP / C-suite
- **Start with:** The recommendation or the headline finding. They want to know the answer before the evidence.
- **Emphasis:** Strategic impact, resource implications, risks, what they need to decide.
- **Detail level:** High-level. Numbers that matter, not numbers that exist. One chart, not five.
- **Avoid:** Engineering-level detail, methodology deep-dives, caveats that belong in an appendix.

### Board
- **Start with:** The strategic question or context that frames everything else. Boards think in terms of market position, competitive dynamics, and long-term trajectory.
- **Emphasis:** Market context, financial implications, strategic alignment, long-term risks.
- **Detail level:** Executive summary level. Every slide should matter at the scale a board thinks in.
- **Avoid:** Feature-level detail, sprint metrics, internal process discussion.

### Peer / Team
- **Start with:** The context that makes the rest of the presentation make sense. Peers need to understand the full picture before evaluating the conclusion.
- **Emphasis:** The analysis, the evidence, the trade-offs, the methodology.
- **Detail level:** Full analytical depth. This audience can handle and expects the detail.
- **Avoid:** Oversimplifying. Peers see through skipped steps and will question what's missing.

### Cross-Functional Partners
- **Start with:** What this means for them. Engineering, design, support, sales — each partner cares about the interface: what they need to do, what changes in their world, what the timeline is.
- **Emphasis:** Dependencies, timeline, their specific involvement, how success is measured from their perspective.
- **Detail level:** Enough to act on. Not so much that they need to care about parts that don't affect them.
- **Avoid:** Internal PM deliberation they don't need visibility into. Strategic framing they didn't ask for.

---

## Visual Guidance Conventions

Since the output is markdown (not actual slide files), each slide section includes a `Visual:` annotation suggesting what visual would support the content. This helps the PM translate to actual slides.

### When to Suggest Each Visual Type

| Visual Type | When to use | Example |
|-------------|------------|---------|
| **Bar chart** | Comparing discrete categories or time periods. | Q1 vs. Q2 activation rates. Feature adoption by segment. |
| **Line chart** | Showing trends over time. | Monthly active users over 12 months. Support ticket volume trend. |
| **Pie/donut chart** | Showing composition of a whole (use sparingly — bar charts are usually clearer). | Revenue mix by product line (only if there are 3-5 segments). |
| **Table** | Comparing multiple dimensions across multiple items. | Feature comparison matrix. Cost model breakdown. |
| **Funnel** | Showing drop-off through a sequential process. | Signup → activation → first purchase → repeat purchase. |
| **Diagram/flowchart** | Showing relationships, architecture, or process flow. | System architecture. User journey. Decision tree. |
| **Screenshot/mockup** | Showing the actual product or a proposed design. | Current vs. proposed UX. Competitor product comparison. |
| **Text-only** | When the headline and a few bullet points are sufficient. | Recommendation slides. Context-setting slides. Next steps. |
| **Quote/callout** | Highlighting a key user quote, metric, or finding. | "I've been trying to cancel for 20 minutes" — user research participant. |

### Visual Guidance Standards

- **One visual per slide.** If a slide needs two charts, it's two slides.
- **The visual supports the headline.** If the headline says "activation exceeded target," the chart shows that. Don't make the reader hunt for the data point.
- **Label everything.** Axes, units, time periods, data sources. A chart without labels is a chart without credibility.
- **Note the data source.** "Source: Amplitude, Q3 2026" or "Source: Support ticket analysis, last 90 days."

---

## Speaker Notes Standards

Each slide section includes speaker notes that extend the slide content for the presenter.

### What Speaker Notes Should Include

- **Context the slide doesn't show.** Background information, caveats, or nuance that's too detailed for the slide but important for the conversation.
- **Anticipated questions.** What will the audience ask when they see this slide? Prepare the presenter.
- **What to emphasize.** Where to draw attention. What number matters most. What implication to underscore.
- **Transition guidance.** How this slide connects to the next one. What to say to bridge the narrative.
- **Discussion prompts** (for interactive decks). Where to pause and invite input. What decision to frame.

### What Speaker Notes Should Not Be

- A script. The presenter should know their material — notes are support, not a teleprompter.
- A repeat of what's on the slide. If the note just restates the headline, it's wasting the presenter's time.
- Generic filler. "Discuss this slide with the audience" is not a speaker note.

---

## Red Flags

Presentation smells that indicate the narrative needs work:

- **Topic-label headlines.** "Q3 Results" instead of "Q3 activation exceeded target by 12%." The reader can't follow the argument from headlines alone.
- **Data without interpretation.** A chart with no headline takeaway. Numbers presented without explaining what they mean or why they matter.
- **No clear ask or decision point.** The presentation ends without stating what the audience should do with the information. Every presentation is asking the audience for something — attention, alignment, approval, resources. Name it.
- **Deck-as-document.** Slides with full paragraphs of text. If you can read the slides as a document, they're not slides — they're a formatted report. Each slide should have minimal text, with depth in the speaker notes.
- **Audience mismatch.** Engineering detail for a board. Strategic framing for a sprint review. Feature walkthrough for a VP who needs to make a funding decision.
- **No narrative arc.** A collection of slides that could be reordered without losing meaning. Each slide exists independently instead of building on the previous one.
- **Missing "so what" between sections.** Two sections of content with no logical bridge. The reader can't see how the first section leads to the second.
- **Buried ask.** The request — for funding, approval, resources, a decision — appears on the last slide after 20 slides of context. For decision-oriented decks (exec review, board update), the ask should appear early and be reinforced at the end.
