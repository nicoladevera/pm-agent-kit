# Agent-Readable Output

Standard vocabulary for Agent Blocks across all skill outputs. Load this reference when generating any artifact to understand the block format, shared enum vocabulary, and parsing contract.

---

## Purpose

All pm-agent-kit artifact-producing skills include an Agent Block in their output. The Agent Block is a machine-parseable YAML section that extracts key decision signals into structured form alongside the human-readable narrative. Narrative prose sections remain intact and unchanged; the Agent Block supplements them for downstream agent consumption.

---

## Block Format

The Agent Block uses a YAML fenced code block wrapped in HTML comment delimiters. It is placed **immediately after the document header metadata** (Status / Date / Author / equivalent fields) and **before the first prose section**. This placement is consistent so agents always find the block in position 2 of any artifact without full-document scanning.

```
<!-- AGENT BLOCK -->
```yaml
agent_block:
  skill: [skill-name]
  [skill-specific fields — see each SKILL.md for the field list]
```
<!-- /AGENT BLOCK -->
```

**Parsing contract for downstream agents:**
- Locate the `<!-- AGENT BLOCK -->` delimiter, or the ` ```yaml ` fenced block immediately following the document header
- Parse the YAML within the block
- Unknown fields should be ignored (forward compatibility)
- All fields are optional unless the skill's output format specifies otherwise

---

## Shared Enum Vocabulary

Use these exact strings — match case and spacing precisely. Agents compare field values as literals.

### Status

| Concept | Values |
|---|---|
| Delivery status | `On Track` / `At Risk` / `Blocked` / `Complete` |
| Decision status | `Decided` / `Pending` |
| Document status | `Draft` / `Review` / `Approved` |

### Assessment

| Concept | Values |
|---|---|
| Severity / Priority (named) | `High` / `Medium` / `Low` |
| Confidence (categorical) | `High` / `Medium` / `Low` |
| Confidence (integer) | `1` through `10` |
| Overall quality | `Strong` / `Adequate` / `Needs Work` / `Fundamental Issues` |

### Decision Signals

| Concept | Values |
|---|---|
| Reversibility | `One-way door` / `Two-way door` |
| Risk category | `Execution` / `Market` / `Technical` / `Adoption` / `Organizational` |
| Action signal | `Respond` / `Monitor` / `Ignore` |
| Urgency | `Immediate (days)` / `Near-term (1-2 sprints)` / `Strategic (quarter+)` / `None` |
| Boolean | `Yes` / `No` |

### Planning

| Concept | Values |
|---|---|
| Requirement priority | `P0` / `P1` / `P2` |
| Backlog health | `Healthy` / `Needs Attention` / `Critical` |
| Launch readiness | `Ready` / `At Risk` / `Not Ready` |
| Launch type | `Internal` / `Alpha` / `Beta` / `GA` |

---

## Confidence Scale Note

Two confidence formats are used intentionally:

- **Integer (1–10):** Used in decision-heavy skills (`business-case`, `decision-log`) where conviction is reasoned from evidence and stakeholders may want nuanced signaling. Drawn from the Conviction section of the Stress Test or the Rationale section.
- **Categorical (High / Medium / Low):** Used in analytical skills (`data-analysis`, `doc-review`) where the meaningful distinctions are bounded and map directly to data quality or issue severity.

Do not compare integer and categorical confidence values across skill types.

---

## Criterion ID Convention

Used in `doc-review` output to tag each feedback item with the quality criterion it violates. Format: `[Type prefix]-[criterion number]`

| Document type | Prefix | Reference file |
|---|---|---|
| PRD | `PRD` | `references/prd-quality-criteria.md` |
| Ticket | `TICKET` | `references/ticket-quality-criteria.md` |
| Tech Spec | `TECH` | `references/tech-spec-quality-criteria.md` |
| Project Brief | `BRIEF` | `references/project-brief-quality-criteria.md` |
| General Document | `GENERAL` | `references/general-document-quality-criteria.md` |

Criterion numbers map to the numbered headings in each reference file (e.g., `### 1.`, `### 2.`). Example: `PRD-3` = criterion 3 in `prd-quality-criteria.md` (Scope Is Explicitly Bounded).
