# knowledge/

This folder holds accumulated PM work product — artifacts produced by skills over time. It is the institutional memory of what this PM has built, decided, and shipped.

This is distinct from `references/`, which holds static PM judgment patterns (quality criteria, smell tests, frameworks) that skills consult. Everything in `references/` is portable and pre-populated. Everything in `knowledge/` is produced here and grows over time.

---

## What Goes Here

Artifacts produced by skills when they run in Generator or Draft mode. Only substantive, completed outputs — not in-progress drafts or Analyze mode assessments (those are ephemeral).

| Subfolder | Skill that produces it | What it contains |
|-----------|----------------------|-----------------|
| `prds/` | `prd-draft` | Product requirement documents |
| `tasks/` | `generate-tasks` | Story sets with acceptance criteria |
| `decisions/` | `decision-log` | Decision records — captured or structured |
| `meeting-briefs/` | `meeting-brief` | Pre-meeting briefs |
| `one-pagers/` | `one-pager` | Compressed single-page pitches and proposals |
| `status-updates/` | `status-update` (Draft mode) | Status communications |
| `sprint-plans/` | `sprint-plan` (Draft mode) | Sprint plans |
| `retros/` | `retro-synthesis` | Retro synthesis reports |
| `launch-checklists/` | `launch-checklist` | Feature launch checklists |
| `user-feedback/` | `user-feedback` | Feedback synthesis reports |
| `data-analyses/` | `data-analysis` | Data analysis reports (`.md`) and accompanying chart files (`.png`) |
| `competition/` | `competitive-intel` | Competitive monitoring snapshots and deep dives |
| `business-cases/` | `business-case` | Business cases for initiatives |
| `presentations/` | `presentation-deck` | Structured presentation narratives and `.pptx` files |
| `discovery-plans/` | `discovery-plan` | Discovery plans — assumption maps, research plans, evidence criteria |
| `roadmaps/` | `roadmap-prioritization` | Prioritization rationales — candidate comparisons, sequencing, trade-offs |
| `memos/` | `alignment-memo` | Internal alignment artifacts — frameworks, standards, proposals |

---

## What Doesn't Go Here

- Analyze mode outputs from `status-update` and `sprint-plan` — delivery assessments and backlog health reports are ephemeral by default. If you want to save one, store it in the relevant subfolder with a filename that makes the mode clear (e.g., `2026-sprint-42-plan.md`).
- `doc-review` feedback — evaluative feedback on a document is transient; the value lands in the improved document, not as a stored artifact.
- Company context — team structure, sprint process, and tool configs belong in `company/`.
- PM judgment patterns, quality criteria, and smell tests — those live in `references/`.

---

## Naming Convention

Use consistent naming so artifacts are findable later:

- **Time-ordered artifacts** (status updates, decisions, meeting briefs, user feedback, data analyses, competitive monitor updates, competitive deep dives, discovery plans, alignment memos, one-pagers): `YYYY-MM-DD-descriptive-slug.md`
  - Example: `2026-03-22-q1-launch-status.md`, `2026-03-29-auth-provider-decision.md`, `2026-03-29-q2-planning-brief.md`, `2026-04-14-notion-onboarding-deep-dive.md`, `2026-04-01-enterprise-onboarding-discovery-plan.md`, `2026-04-04-ai-adoption-framework.md`, `2026-04-04-hackathon-q3-one-pager.md`
  - Chart files from data analyses use the same date-slug prefix: `YYYY-MM-DD-descriptive-slug-chart.png` (append `_2`, `_3` for additional charts from the same analysis). Example: `2026-04-04-nwsl-chance-creation-efficiency-chart.png`
- **Feature-scoped artifacts** (PRDs, task sets, launch checklists, business cases): `feature-name-artifact-type.md`
  - Example: `bulk-export-prd.md`, `subscription-pricing-tasks.md`, `android-app-launch-checklist.md`
- **Sprint-scoped artifacts** (sprint plans, retro syntheses): `YYYY-sprint-NN-artifact-type.md`
  - Example: `2026-sprint-20-plan.md`, `2026-sprint-22-retro.md`, `2026-sprint-20-22-retro.md`
- **Planning-period artifacts** (prioritization rationales): `YYYY-QN-prioritization-rationale.md`
  - Example: `2026-Q3-prioritization-rationale.md`

These are conventions, not rules. Adjust for your workflow.
