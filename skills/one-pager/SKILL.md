---
name: one-pager
description: Compresses any argument — initiative, proposal, budget request, process change — into a single-page artifact calibrated for a specific audience and ask. Use when asked to "write a one-pager", "distill this into a one-pager", "I need a one-page pitch for X", "compress this for my VP", or "summarize this as a one-pager".
metadata:
  type: Generator
  tier: 4
  approval: draft-confirm
  context-required: []
  context-optional:
    - company/facts/product.md
    - company/facts/team.md
    - company/norms/communication.md
  degradation: proceed-with-caveat
---

# one-pager

Compress any argument into a single page calibrated for a specific audience and a specific ask. The one-pager is the written equivalent of a 60-second hallway pitch — every sentence is load-bearing, the ask is up front, and the reader can act without a follow-up conversation.

This skill covers the class of PM work that falls between a Slack message and a full artifact. An initiative pitch that needs VP approval before you write the PRD. A budget request for a tool the team wants to pilot. A hackathon proposal. A process change that needs cross-functional buy-in. The content could be a product feature, an internal program, a tool adoption case, or a strategic pivot — the skill's job is compression and audience-targeting, not domain-specific structuring.

The one-pager is distinct from neighboring skills:
- `prd-draft` is exhaustive by design — a full specification
- `business-case` is an analytical argument with impact sizing, cost models, and alternatives
- `presentation-deck` is multi-slide with narrative arcs and speaker notes
- `alignment-memo` is an internal operating document (frameworks, standards) designed to establish norms over time

The one-pager is what you produce when any of those would be too much for the moment, but informal communication would be too little.

---

## What It Accepts

Any form of input that needs to become a single-page argument:
- Raw ideas with no prior artifact ("I want to pitch a hackathon to my VP")
- Existing kit artifacts as source material ("compress this business case into a one-pager for the head of partnerships") — from `knowledge/` or pasted inline
- Rough notes, bullet points, Slack threads, or a verbal download
- A data analysis, competitive snapshot, or user feedback synthesis that needs to be turned into a pitch
- A combination of the above

The input provides the substance. The skill provides compression, structure, and audience calibration.

**Two workflows, same output:** If the input references or includes a longer artifact (a business case, PRD, discovery plan), the skill compresses it. If the input is raw notes or an idea, the skill generates from scratch. The output format is the same either way — the skill detects the workflow from the input, not from a mode flag.

---

## Required Invocation Inputs

Two things must be specified:
1. **Audience** — Who reads this? (e.g., "my VP of Engineering," "the head of partnerships," "the leadership team," "cross-functional partners in marketing")
2. **The ask** — What should the reader do after reading? (e.g., "approve this," "fund this," "prioritize this," "give me feedback," "be aware of this")

If either is missing, ask: "Who is the audience for this one-pager, and what's the ask — what should the reader do after reading it? (approve, fund, prioritize, give feedback, be aware)"

---

## Intake

A one-pager built on a misunderstood ask or aimed at the wrong audience wastes a precious opportunity — the reader gives it one minute, and if the framing is wrong, the PM doesn't get a second chance. Confirm the foundation before compressing.

### Signals to Check

- **Audience:** Named? Specific enough to calibrate register? (A "VP" is different from "the engineering team." A "cross-functional partner" is different from "someone new to the project.")
- **The ask:** Stated? Specific? (There's a meaningful difference between "approve this" and "give me feedback." The conditional sections and framing change based on the ask.)
- **Source material richness:** Is this a compression job (existing artifact or substantial notes) or a from-scratch job (an idea, a few bullets, a vague prompt)? Compression requires information triage — what survives, what gets cut. From-scratch requires more inference and confirmation.

### Adaptive Response

**Rich input** (audience named, ask stated, substantial source material or detailed notes): Restate the argument in 1-2 sentences and confirm the one most consequential inference. Example: "Got it — compressing the API integration business case into a one-pager for the head of partnerships, asking for feedback on whether they'd want to co-invest. I'll lead with the partnership opportunity rather than the internal ROI framing. Proceeding."

**Moderate input** (some signals present, some gaps): Ask up to 3 targeted questions. Examples:
- "Who specifically is reading this — the VP of Engineering for approval, or the broader leadership team for awareness? That changes the register and the ask framing."
- "What's the ask — do you need approval and budget, or are you looking for feedback before you refine the pitch?"
- "Is there existing material I should compress (a business case, a PRD, meeting notes), or am I working from what you've given me here?"

**Thin input** (a sentence, a vague idea, or "write a one-pager for the hackathon thing"): Present a structured interpretation:

> **Here's how I'd frame this — tell me what needs adjusting:**
>
> - **Audience:** [Best inference from context]
> - **The ask:** [Approve / Fund / Prioritize / Feedback / Awareness — inferred]
> - **Core argument:** [Translated problem-first — the problem or opportunity, not the solution]
> - **Why now:** [Timing argument — inferred or "I don't have a read on this yet"]
>
> Anything off? I'll adjust before drafting.

---

## Instructions

### 1. Read the input fully

Absorb all context before compressing. If the input references a `knowledge/` artifact, read it in full — compression requires understanding the whole argument before deciding what survives. Note what's provided, what's missing, and what the strongest version of this argument would emphasize.

### 2. Load reference files

Read these files:
- `references/communication-quality.md` — Lead with the answer, audience calibration, structured naturally, warmth as load-bearing structure
- `references/audience-registers.md` — Per-audience registers: what each stakeholder type needs, what to emphasize, what to omit
- `references/pm-smell-test.md` — Check for smells 1 (missing why), 4 (audience mismatch), and 5 (false precision)
- `references/agent-readable-output.md` — Agent Block format and shared enum vocabulary

### 3. Load company context (if available)

If `company/facts/product.md` exists and is substantive, read it for product landscape and organizational priorities. This grounds the argument in the company's actual context.

If `company/facts/team.md` exists and is substantive, read it for team structure, stakeholder landscape, and who cares about what. This informs audience calibration and the "who needs to be on board" framing.

If `company/norms/communication.md` exists and is substantive, read it for internal communication patterns and conventions. This helps match the one-pager's tone to what the audience expects.

If any of these files exist but are still stub templates, treat them as unavailable and say so in the context note.

### 4. Identify the argument type

Determine what kind of case is being compressed. This drives which conditional sections appear and how the argument is framed:

- **Initiative pitch** — proposing a product initiative, feature, or project for prioritization or approval
- **Budget / resource request** — requesting funding, headcount, tool licenses, or capacity allocation
- **Process proposal** — proposing a new practice, workflow change, or organizational initiative (hackathon, pilot, working group)
- **Awareness brief** — informing a stakeholder of something they need to know — a risk, a decision, a market shift
- **Feedback request** — seeking input on an approach, direction, or draft before committing

The argument type is inferred from the ask and content, not declared by the PM.

### 5. Establish the problem or opportunity

Start with why this matters, not what's proposed. Per the Problem-First operating heuristic from `CLAUDE.md`:

- If the PM's input leads with a solution ("we should run a hackathon," "we need to buy this tool"), translate back to the underlying problem or opportunity.
- Quantify the gap where possible — even a rough order of magnitude helps the reader calibrate importance.
- For compression jobs, extract the problem framing from the source artifact and compress it, preserving the strongest evidence.

### 6. Draft the one-pager

Write each section following the output format below. Two critical rules:

**The ask goes first.** The reader knows what they're being asked to do within the first two sentences — before the problem, before the approach, before anything. Per `references/communication-quality.md` criterion 1: lead with the answer or the ask.

**Every sentence must be load-bearing.** A one-pager has no room for setup paragraphs, throat-clearing, or restating what the reader already knows. Each sentence either advances the argument or provides evidence. If a sentence could be removed without weakening the case, remove it.

### 7. Include conditional sections based on ask type

| Ask Type | Conditional Sections to Include |
|----------|-------------------------------|
| Approve | Success Criteria |
| Fund | Cost / Resource Ask, Success Criteria |
| Prioritize | Impact / Sizing |
| Feedback | *(none — core sections are sufficient)* |
| Awareness | *(none — core sections are sufficient)* |

If the ask involves choosing between options (e.g., "approve option A or B"), include **Alternatives Considered** — but keep it compressed: one sentence per option with the trade-off, not a full analysis.

### 8. Enforce the one-page constraint

This is the hardest and most important step. After drafting, review the full output against the word budget: **400-600 words of content** (excluding the YAML Agent Block and context note).

- Count the words. If over 600, cut.
- Cut by compressing, not by omitting sections. A one-pager with a missing "Why Now" is worse than one with a tighter "Why Now."
- Every sentence must pass the test: "Does this sentence directly serve the ask?" If not, cut it.
- Prefer specific evidence over general claims. "Support tickets about this increased 40% last quarter" survives compression. "This is a growing problem" does not.
- Resist the urge to be thorough. The one-pager's job is to make the reader want to say yes (or ask one clarifying question), not to answer every possible objection.

### 9. Calibrate for audience

Apply the appropriate register from `references/audience-registers.md`:

- **Leadership / stakeholders:** Strategic framing, clean signals, every risk paired with a mitigation. Anticipate their questions — lead with what's NOT the problem.
- **Engineers / technical partners:** Stay in the what/why lane. Show you've done your homework. Don't tell them how to build it.
- **Cross-functional partners:** Name what they need to know, what they need to do, what's coming their way. Be the connective tissue.
- **Direct manager:** More raw, exploratory. Surface the uncertainty honestly.

The audience register affects word choice, framing, and what's emphasized — not the structure.

### 10. Run the smell test

Check for:
- **Smell 1 (Missing Why):** Does the one-pager establish why this matters before describing what's proposed? Can you answer "why should I care?" from the first paragraph?
- **Smell 4 (Audience Mismatch):** Is the content calibrated for the named audience? Would a different audience need a fundamentally different version?
- **Smell 5 (False Precision):** Are estimates presented honestly? A one-pager can say "we estimate 2-3 weeks of engineering effort" — it should not say "14.5 engineering days."

### 11. Populate the Agent Block

After completing the smell test, fill in the Agent Block:
- `ask_type`: Approve / Fund / Prioritize / Feedback / Awareness
- `audience`: the named audience
- `source_artifact`: path to the `knowledge/` artifact if compression, or `original` if from scratch
- `confidence`: 1-10 integer reflecting how well the one-pager represents the underlying argument
- `time_sensitivity`: Immediate (days) / Near-term (1-2 sprints) / Strategic (quarter+) / None

### 12. Flag open items

If the one-pager omits important nuance that the reader might need in a follow-up conversation, note it in the open items. This is especially important for compression jobs — the source artifact may contain caveats, risks, or alternatives that didn't survive compression but that the PM should be prepared to discuss.

---

## Output Format

````markdown
## One-Pager: [Title]

**Status:** Draft
**Date:** [Current date]
**Audience:** [Named audience]
**Ask:** [One sentence — what the reader is being asked to do]

<!-- AGENT BLOCK -->
```yaml
agent_block:
  skill: one-pager
  ask_type: "[Approve / Fund / Prioritize / Feedback / Awareness]"
  audience: "[Named audience]"
  source_artifact: "[knowledge/ path or 'original']"
  confidence: [1-10]
  time_sensitivity: "[Immediate (days) / Near-term (1-2 sprints) / Strategic (quarter+) / None]"
```
<!-- /AGENT BLOCK -->

---

**The Ask:** [What the reader should do, stated directly. 1-2 sentences. This is the first thing the reader sees after the header.]

---

### Problem / Opportunity

[Why this matters. The gap, the pain, the opportunity — stated independently from the proposed solution. Quantified where possible. Compressed to 2-4 sentences.]

---

### Proposed Approach

[What's being proposed, at high level. Not a full specification — just enough for the reader to understand what they're evaluating. 2-4 sentences.]

---

### Why Now

[The timing argument. What makes this urgent or timely. A planning window closing, a competitive move, a cost escalating, a dependency aligning. If there's no genuine urgency, say so honestly — "this is important but not urgent" is better than manufactured time pressure.]

---

### Impact / Sizing

*(Include when ask is Prioritize or Fund. Omit for Feedback or Awareness.)*

[Rough magnitude of impact. Not a full sizing model — an order-of-magnitude signal that helps the reader calibrate importance. State assumptions.]

---

### Cost / Resource Ask

*(Include when ask is Fund. Omit otherwise.)*

[What's needed — budget, headcount, capacity, time. Be specific enough that the reader can evaluate feasibility.]

---

### Success Criteria

*(Include when ask is Approve or Fund. Omit for Feedback or Awareness.)*

[How we'll know this worked. 2-3 specific, measurable criteria. Not a metrics plan — a definition of success the reader can hold the PM to.]

---

### Alternatives Considered

*(Include only when the ask involves choosing between options. Omit otherwise.)*

[One sentence per alternative with the key trade-off. Not a full analysis — just enough to show the recommendation was chosen, not assumed.]

---

### Key Risks or Open Questions

[What could go wrong or what's still unknown. 2-3 items. Each risk named with a mitigation or explicit "we don't have a mitigation yet — here's what we'd do to find one." Honesty here builds trust.]

---

### Next Steps

[What happens if the reader says yes. Concrete, owned, time-bound. 2-4 items.]

---

### Open Items

*(Omit if none.)*

- [Important nuance from the source artifact that didn't survive compression]
- [Context the PM should be prepared to discuss if the reader asks]

---

### Smell Test

- **Smell 1 (Missing Why):** [Finding — or "Clear — problem established before solution"]
- **Smell 4 (Audience Mismatch):** [Finding — or "Clear — calibrated for [audience] register"]
- **Smell 5 (False Precision):** [Finding — or "Clear — estimates presented as ranges with stated assumptions"]

> **Context note:** [State which substantive company files were loaded, which were absent, and which were stub templates. Note how missing context may have affected audience calibration or argument grounding.]
````

---

## Quality Bar

- **Is it actually one page?** 400-600 words of content (excluding Agent Block and context note). If you printed this with normal margins and 11pt font, it would fit on a single page. If not, it's not a one-pager — it's a short document that needs further compression.
- **Is the ask stated in the first two sentences?** The reader knows what they're being asked to do before they know the background. No throat-clearing, no "as you know" setup.
- **Could the reader act on it without a follow-up conversation?** The one-pager contains enough for the ask to be fulfilled — or explicitly states what the next conversation needs to cover.
- **Does the "Why Now" create real urgency?** Not manufactured urgency — real timing logic. A planning window, a competitive move, an escalating cost. If "why now" is weak, the one-pager will sit in a queue regardless of how good the argument is.
- **Would this survive the hallway test?** If the PM ran into the target reader in a hallway, could they verbally deliver the same pitch in 60 seconds? The one-pager is the written version of that encounter.
- **For compression jobs: does the compressed version accurately represent the source argument?** The one-pager preserves the core argument without distorting it. The strongest evidence survived. The recommendation is faithfully represented. A reader of both the source and the one-pager would agree they make the same case.
- **Is every sentence load-bearing?** No setup paragraphs, no generic framing, no restating what the reader already knows. Each sentence advances the argument or provides evidence. Remove any sentence and the case gets weaker.

---

## Save

After producing the artifact, write it to `knowledge/one-pagers/` using the naming convention: `YYYY-MM-DD-topic-slug-one-pager.md`, where the date is the creation date and the slug describes the topic. Report the saved file path in the conversation.
