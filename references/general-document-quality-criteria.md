# General Document Quality Criteria

What makes a good PM document when it doesn't fit a specialized type — GTM plans, SOPs, positioning docs, runbooks, onboarding guides, or any other document a PM produces or reviews. These six dimensions apply universally.

Because these criteria are broad, always anchor evaluation in the document's own stated purpose. A runbook and a positioning doc are held to different standards, and these criteria accommodate that. The evaluator's job is to judge the document against what it's trying to be, not against a template it never claimed to follow.

---

## Calibrating to Document Intent

Before applying the criteria, identify three things:

- **What type of document is this?** Name the subtype (GTM plan, SOP, runbook, positioning doc, etc.) — this frames the entire evaluation.
- **What is the document trying to accomplish?** Inform, align, enable execution, record a decision, propose a strategy, or something else?
- **Who is the intended audience?** The criteria for "completeness" and "structure" depend entirely on the reader.

If the document doesn't state these things explicitly, that is the first and most important finding. A document that doesn't declare its purpose can't be evaluated — the reader doesn't know what "good" looks like.

---

## The Criteria

### 1. Purpose Clarity

The document states why it exists and what it's trying to accomplish. This is the foundation — every other criterion depends on knowing the document's intent. A document without a declared purpose forces the reader to guess what they're supposed to take away, and two readers will guess differently.

**Evaluate:** Can you state in one sentence what this document is for? Is the purpose explicit, or did you have to infer it? Would two readers independently agree on what this document is trying to do? Is the "why" present — not just what the document covers, but why it matters?

### 2. Audience Fit

The content, detail level, and tone match the intended reader. A runbook for an on-call engineer needs step-by-step precision. A positioning doc for a marketing team needs strategic framing. A process doc for a cross-functional audience needs to avoid team-specific jargon. The same information, presented wrong for the audience, fails.

**Evaluate:** Is the audience named or clearly implied? Is the level of detail right for that audience — not too granular, not too abstract? Does the document assume context the reader might not have? Does it include detail the reader doesn't need? Would the intended reader be able to act on this without asking clarifying questions?

### 3. Logical Structure

The document is organized so that each section follows naturally from the previous one. The reader can navigate it without re-reading. Headings, if present, accurately describe their contents. The structure serves the document's purpose — a decision-support doc builds to a recommendation, a process doc follows the workflow sequence, a strategy doc moves from context to approach to execution.

**Evaluate:** Does the document have a clear organizational logic? Could you summarize its structure in 3–5 bullet points? Are there sections that feel misplaced or that break the flow? Would the document be clearer with a different ordering? Do the headings accurately predict what's in each section?

### 4. Completeness Relative to Intent

The document covers what it needs to cover given its stated purpose — no more, no less. A runbook that omits a critical failure mode is incomplete. A positioning doc that includes implementation timelines is overscoped. Completeness is measured against what the document is trying to do, not against an abstract ideal of thoroughness.

**Evaluate:** Given the document's purpose, what topics must it cover? Are any of those missing? Does it include material that doesn't serve the purpose and should be removed or moved elsewhere? Are there gaps that would block the reader from acting on the document? Is there anything the reader would need to go find elsewhere that should have been included here?

### 5. Actionability

The reader knows what to do after reading the document. If the document is meant to drive a decision, the decision is framed and the options are clear. If it's meant to enable execution, the steps are concrete and sequenced. If it's purely informational, the takeaways are stated explicitly rather than left for the reader to synthesize. A document that informs but doesn't enable action has done half the job.

**Evaluate:** After reading, does the reader know what action to take — or what they now understand that they didn't before? Are next steps, owners, or decisions named where appropriate? If the document is informational, are the key takeaways stated rather than implied? Could someone act on this document without a follow-up conversation?

### 6. Evidence and Grounding

Claims are supported. Data is cited with sources. Assertions that could be challenged are backed by evidence or explicitly flagged as assumptions. The document distinguishes between what is known and what is believed. A document that states opinions as facts undermines its own credibility — and a reader who catches one unsupported claim will question every claim that follows.

**Evaluate:** Are key claims supported by evidence, data, or references? Are assumptions labeled as assumptions? Is there anything stated as fact that should carry a caveat? Would a skeptical reader find the document credible? Are data points sourced, or do they appear without attribution?

---

## Using These Criteria

**For review (`doc-review`):** Identify the document subtype and audience first, then evaluate against each criterion. Ground every assessment in the document's own purpose — don't impose criteria that don't apply to this type of document. A runbook doesn't need a "why now" section. A positioning doc doesn't need step-by-step instructions. Let the document's intent set the bar.

**Rating scale:**
- **Strong** — The criterion is clearly satisfied.
- **Needs work** — Partially addressed but has gaps worth naming.
- **Missing** — Not addressed; the gap undermines the document's effectiveness.
- **Not applicable** — The criterion doesn't apply to this document type (e.g., "Actionability" may not apply to a purely archival record).
