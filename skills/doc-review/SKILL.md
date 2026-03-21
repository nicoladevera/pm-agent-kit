---
skill: doc-review
type: Analyzer
tier: 1
approval: draft-confirm
context-required: []
context-optional:
  - company/norms/process.md
  - company/facts/product.md
degradation: proceed-with-caveat
---

# doc-review

Evaluate a PRD against PM quality criteria and produce structured, actionable feedback on what's strong, what's missing, and what needs sharpening.

**v1 scope: PRD review only.** This skill will eventually evaluate tickets, A/B test designs, and technical specs. v1 targets PRD review specifically — one document type, one rubric, one quality bar. Broaden scope after the format is proven.

---

## Instructions

### 1. Read the input document

Read the full PRD before producing any output. Do not begin evaluating section-by-section as you read — understand the whole document first, then assess.

### 2. Load knowledge files

Read these files in full. They are your evaluation rubric:
- `knowledge/prd-quality-criteria.md` — The eight criteria you evaluate against
- `knowledge/pm-smell-test.md` — Red flags to scan for
- `knowledge/acceptance-criteria.md` — The standard for evaluating AC quality

### 3. Load company context (if available)

If `company/norms/process.md` exists and is substantive, read it for context on how PRDs are expected to work at this company (sprint process, document standards, review expectations).

If `company/facts/product.md` exists and is substantive, read it for context on the product landscape, user segments, and existing functionality.

If either file exists but is still a stub template, treat it as unavailable and say so in the Context Note section of your output.

If neither substantive file is available, proceed — note the absence in the Context Note section of your output.

### 4. Evaluate against quality criteria

For each criterion in `knowledge/prd-quality-criteria.md`, determine:
- **Strong** — The criterion is clearly satisfied
- **Needs work** — Partially addressed but has gaps
- **Missing** — Not addressed at all

Don't just check boxes. For each criterion, engage with the *specific content* of this PRD. Reference exact sections, quote specific language, and name what's working or what's not. Generic feedback that could apply to any PRD is not useful.

### 5. Run the smell test

Scan for each red flag in `knowledge/pm-smell-test.md`. If a smell is present:
- Name it
- Point to the exact section where it appears
- Explain the risk it creates

If no smells are detected, say so. Don't invent problems.

### 6. Identify strengths

Name 2-3 things the PRD does well. Be specific — reference the section and explain what makes it strong. Acknowledging what works is not optional; it calibrates the review and builds trust. But keep it honest — don't praise mediocre sections to be polite.

### 7. Identify and prioritize gaps

Identify the most important gaps or weaknesses. List them in priority order — the first issue should be the most impactful to fix. For each gap:
- State what's wrong clearly
- Explain why it matters (what risk it creates, what confusion it causes)
- Describe what a stronger version would look like

Limit to the most important issues. A review that lists 15 minor issues buries the ones that matter. If there are genuinely 15 problems, the review should say: "This PRD has fundamental issues" and focus on the structural ones.

### 8. Surface open questions

List questions you'd ask the PM before this PRD moves forward. These should be questions the document raises but doesn't answer — not questions the review already answered.

---

## Output Format

```markdown
## Doc Review: [Document Title]

### Summary
[2-3 sentence assessment. Overall quality level. The single biggest strength and the single biggest gap.]

### What's Strong
- [Specific strength with reference to the document section]
- [Specific strength]

### What Needs Work
1. **[Issue name]** — [What's wrong. Why it matters. What a fix looks like.]
2. **[Issue name]** — [Description]
3. **[Issue name]** — [Description]

### Smell Test Flags
- [Red flags detected, with specific references — or "None detected"]

### Open Questions
- [Questions this PRD raises but doesn't answer]

> **Context note:** [State which substantive company files were loaded, which files were absent, and which files existed but were stub templates and therefore skipped. Note what the review might miss as a result.]
```

---

## Quality Bar

The review should catch what a strong PM would catch. It should be specific enough that the PM can act on every piece of feedback without asking follow-up questions. It should not flag false positives on well-written sections just to appear thorough.

A good doc-review output meets these tests:
- **Would a PM find this useful?** Not just "technically correct" — genuinely useful for improving the document.
- **Is every piece of feedback actionable?** Each issue names the problem, the risk, and what better looks like.
- **Does it prioritize?** The most important issues are first. Minor issues don't crowd out fundamental ones.
- **Does it engage with this specific PRD?** The feedback references exact sections and content, not generic PRD advice.
- **Is it honest about strengths?** It names what works without being performative about it.
