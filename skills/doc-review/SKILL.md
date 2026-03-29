---
skill: doc-review
type: Analyzer
tier: 1
approval: draft-confirm
context-required: []
context-optional:
  - company/norms/team-process.md
  - company/facts/product.md
  - company/facts/customers.md
degradation: proceed-with-caveat
---

# doc-review

Evaluate a PM document against quality criteria appropriate to its type and produce structured, actionable feedback on what's strong, what's missing, and what needs sharpening.

Supports five document types: **PRD**, **ticket**, **project brief**, **technical spec**, and **general document** (catch-all for documents that don't match the four specialized types). The skill auto-detects the document type from its content and loads the appropriate evaluation criteria.

---

## Instructions

### 1. Read the input document

Read the full document before producing any output. Do not begin evaluating section-by-section as you read — understand the whole document first, then assess.

### 2. Detect the document type

Scan the document for structural signals to identify its type. State the detected type at the top of your output.

| Signal | Document Type |
|--------|--------------|
| Has Problem Statement + Success Metrics as primary structure | PRD |
| Has Acceptance Criteria or Given/When/Then as primary content | Ticket |
| Is a brief, framing, or scoping document — may be loosely structured, lacks metrics or AC | Project Brief |
| Describes system architecture, APIs, data models, or implementation approach | Tech Spec |
| Does not match any of the above signal patterns | General Document |

If the document has signals from more than one type, use the dominant structure. State your assumption and proceed — do not stop and ask. If the document doesn't match any of the four specialized types, classify it as **General Document** and note the specific subtype in parentheses (e.g., "General Document (GTM Strategy)", "General Document (SOP)").

### 3. Load reference files for the detected type

Load `references/pm-smell-test.md` for all document types — it applies universally.
Load `references/agent-readable-output.md` for all document types — defines Agent Block format and shared enum vocabulary including Criterion ID convention.

Then load the type-specific criteria file:

| Document Type | Load These Files |
|--------------|-----------------|
| PRD | `references/quality-criteria-prd.md`, `references/acceptance-criteria.md` |
| Ticket | `references/quality-criteria-ticket.md`, `references/acceptance-criteria.md`, `references/story-structure.md` |
| Project Brief | `references/quality-criteria-project-brief.md` |
| Tech Spec | `references/quality-criteria-tech-spec.md` |
| General Document | `references/quality-criteria-general-document.md` |

For all document types that include scope definitions or trade-off sections (PRDs, project briefs, tech specs), also consult `references/pushback-and-negotiation.md` — specifically the Scope Protection section. Check whether scope boundaries are written as confirmable contracts ("we are NOT doing X") or left as soft suggestions that will erode under pressure.

### 4. Load company context (if available)

If `company/norms/team-process.md` exists and is substantive, read it for context on how documents of this type are expected to work at this company.

If `company/facts/product.md` exists and is substantive, read it for context on the product landscape and existing functionality.

If `company/facts/customers.md` exists and is substantive, read it for customer segments, pain points, and buyer vs. user dynamics. This helps evaluate whether documents ground their problem statements and user stories in real customer context.

If any of these files exist but are still stub templates, treat them as unavailable and say so in the Context Note section of your output.

### 5. Evaluate against quality criteria

For each criterion in the type-specific reference file, determine:
- **Strong** — The criterion is clearly satisfied
- **Needs work** — Partially addressed but has gaps
- **Missing** — Not addressed at all

Don't just check boxes. For each criterion, engage with the *specific content* of this document. Reference exact sections, quote specific language, and name what's working or what's not. Generic feedback that could apply to any document is not useful.

For project briefs: calibrate to the document's maturity level before evaluating. A loose set of notes is not held to the same standard as a structured brief — but both should have the core signal present.

For general documents: evaluate against the six universal dimensions in the criteria file. Since these dimensions are deliberately broad, ground every assessment in the document's self-declared purpose and audience. If the document doesn't state its purpose, that is the first and most important finding.

### 6. Run the smell test

Scan for red flags in `references/pm-smell-test.md`. If a smell is present:
- Name it
- Point to the exact section where it appears
- Explain the risk it creates

If no smells are detected, say so. Don't invent problems.

### 7. Identify strengths

Name 2-3 things the document does well. Be specific — reference the section and explain what makes it strong. Acknowledging what works is not optional; it calibrates the review and builds trust. Keep it honest — don't praise mediocre sections to be polite.

### 8. Identify and prioritize gaps

Identify the most important gaps or weaknesses. List them in priority order — the first issue should be the most impactful to fix. For each gap:
- State what's wrong clearly
- Explain why it matters (what risk it creates, what confusion it causes)
- Describe what a stronger version would look like
- Assign a **severity level**: High (blocks launch or creates significant misalignment), Medium (causes confusion or rework but not blocking), Low (polish and clarity)
- Assign a **Criterion ID** matching the criterion from the loaded type-specific reference file that the issue violates. Format: `[TYPE-N]` where TYPE is the document type prefix (PRD, TICKET, TECH, BRIEF, GENERAL) and N is the criterion number. See `references/agent-readable-output.md` for the full convention.

Limit to the most important issues. A review that lists 15 minor issues buries the ones that matter. If there are genuinely 15 problems, the review should say: "This document has fundamental issues" and focus on the structural ones.

After completing the review, populate the Agent Block:
- Count issues by severity level
- Count smell test flags detected
- Set `overall_quality` to: Strong (mostly strengths, minor items), Adequate (fixable gaps that don't undermine the document), Needs Work (multiple Medium/High issues requiring significant revision), Fundamental Issues (core sections missing or so weak the document needs substantial rewriting)

### 9. Surface open questions

List questions you'd ask the PM before this document moves forward. These should be questions the document raises but doesn't answer — not questions the review already answered.

---

## Output Format

````markdown
## Doc Review: [Document Title]

**Document type:** [PRD / Ticket / Project Brief / Tech Spec / General Document (subtype)]

<!-- AGENT BLOCK -->
```yaml
agent_block:
  skill: doc-review
  document_type: [PRD / Ticket / Project Brief / Tech Spec / General Document]
  issue_count_high: [integer]
  issue_count_medium: [integer]
  issue_count_low: [integer]
  smell_test_flags: [integer — 0 if none detected]
  overall_quality: [Strong / Adequate / Needs Work / Fundamental Issues]
```
<!-- /AGENT BLOCK -->

### Summary
[2-3 sentence assessment. Overall quality level. The single biggest strength and the single biggest gap.]

### What's Strong
- [Specific strength with reference to the document section]
- [Specific strength]

### What Needs Work
1. **[Issue name]** `[High / Medium / Low]` `[CriterionID]` — [What's wrong. Why it matters. What a fix looks like.]
2. **[Issue name]** `[High / Medium / Low]` `[CriterionID]` — [Description]
3. **[Issue name]** `[High / Medium / Low]` `[CriterionID]` — [Description]

### Smell Test Flags
- [Red flags detected, with specific references — or "None detected"]

### Open Questions
- [Questions this document raises but doesn't answer]

> **Context note:** [State the detected document type and how it was identified. State which substantive company files were loaded, which were absent, and which were stub templates. Note what the review might miss as a result. For General Document reviews: note that general quality dimensions were used rather than type-specific criteria, and suggest re-running as a specialized type if the document might actually be one.]
````

---

## Quality Bar

The review should catch what a strong PM would catch. It should be specific enough that the PM can act on every piece of feedback without asking follow-up questions. It should not flag false positives on well-written sections just to appear thorough.

A good doc-review output meets these tests:
- **Would a PM find this useful?** Not just "technically correct" — genuinely useful for improving the document.
- **Is every piece of feedback actionable?** Each issue names the problem, the risk, and what better looks like.
- **Does it prioritize?** The most important issues are first. Minor issues don't crowd out fundamental ones.
- **Does it engage with this specific document?** The feedback references exact sections and content, not generic advice.
- **Is it honest about strengths?** It names what works without being performative about it.
- **Is it calibrated to the document type?** The criteria and tone match what's appropriate for a PRD vs. a loose project brief vs. a tech spec vs. a general document.
- **Does it handle the general case honestly?** When reviewing a general document, the review names the limitation of generic criteria and suggests a specialized type if the document might actually be one.
