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
| `status-updates/` | `status-update` (Draft mode) | Status communications |
| `sprint-plans/` | `sprint-plan` (Draft mode) | Sprint plans |
| `retros/` | `retro-synthesis` | Retro synthesis reports |
| `launch-checklists/` | `launch-checklist` | Feature launch checklists |
| `user-feedback/` | `user-feedback` | Feedback synthesis reports |
| `data-analyses/` | `data-analysis` | Data analysis reports |
| `competition/` | `competitive-intel` | Competitive monitoring snapshots and deep dives |
| `business-cases/` | `business-case` | Business cases for initiatives |
| `presentations/` | `presentation-deck` | Structured presentation narratives and `.pptx` files |

---

## What Doesn't Go Here

- Analyze mode outputs from `status-update` and `sprint-plan` — delivery assessments and backlog health reports are ephemeral by default. If you want to save one, store it in the relevant subfolder with a filename that makes the mode clear (e.g., `sprint-42-assessment.md` vs. `sprint-42-plan.md`).
- `doc-review` feedback — evaluative feedback on a document is transient; the value lands in the improved document, not as a stored artifact.
- Company context — team structure, sprint process, and tool configs belong in `company/`.
- PM judgment patterns, quality criteria, and smell tests — those live in `references/`.

---

## Naming Convention

Use consistent naming so artifacts are findable later:

- **Time-ordered artifacts** (status updates, retros): `YYYY-MM-DD-descriptive-slug.md`
  - Example: `2026-03-22-q1-launch-status.md`
- **Feature-scoped artifacts** (PRDs, task sets, decisions, meeting briefs): `feature-name-artifact-type.md`
  - Example: `installment-schedule-prd.md`, `payment-reminders-tasks.md`
- **Sprint-scoped artifacts** (sprint plans): `sprint-NN-plan.md`
  - Example: `sprint-42-plan.md`

These are conventions, not rules. Adjust for your workflow.
