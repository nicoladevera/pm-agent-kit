# Company Onboarding Checklist

Populate these files in the order they affect current runtime behavior. Not every file in `company/` is consumed by shipped skills today.

---

## Status Legend

- **Active runtime input** — Read by shipped skills regularly. Missing content degrades output quality today.
- **Conditional runtime input** — Read only by specific skills or modes. Missing content affects those paths, not the whole system.
- **Future-facing / not currently consumed** — Useful context to keep, but not read by shipped skills today.

## Company Context Matrix

| File | Status | Current consumers | Missing impact today |
|------|--------|-------------------|----------------------|
| `facts/product.md` | Active runtime input | `doc-review`, `prd-draft`, `generate-tasks`, `status-update`, `sprint-plan`, `meeting-brief`, `decision-log`, `data-analysis`, `user-feedback`, `competitive-intel`, `launch-checklist`, `business-case`, `presentation-deck` | Broad quality loss across most skills |
| `facts/team.md` | Active runtime input | `status-update`, `sprint-plan`, `retro-synthesis`, `meeting-brief`, `decision-log`, `launch-checklist`, `business-case`, `presentation-deck` | Weaker ownership, stakeholder, and capacity reasoning |
| `norms/process.md` | Active runtime input | `doc-review`, `prd-draft`, `generate-tasks`, `status-update`, `sprint-plan`, `retro-synthesis` | Weaker planning, delivery, and document calibration |
| `norms/communication.md` | Active runtime input | `status-update`, `meeting-brief`, `competitive-intel`, `launch-checklist`, `presentation-deck` | Weaker audience calibration and comms fit |
| `norms/decisions.md` | Conditional runtime input | `decision-log`, `business-case` | Mainly affects decision framing and approval context |
| `facts/competitors.md` | Conditional runtime input | `competitive-intel`, `user-feedback` | Mainly affects competitive baseline and competitor mentions |
| `norms/launch-process.md` | Conditional runtime input | `launch-checklist` | Mainly affects launch-type calibration and approvals |
| `interfaces/data-sources.md` | Conditional runtime input | `data-analysis`, `user-feedback` | Mainly affects data-source interpretation and channel bias handling |
| `interfaces/branding.md` | Conditional runtime input | `presentation-deck` Slides mode only | Slides fall back to defaults; narrative mode unaffected |
| `facts/glossary.md` | Future-facing / not currently consumed | None | No runtime effect today |
| `interfaces/tools.md` | Future-facing / not currently consumed | None | No runtime effect today |
| `interfaces/templates.md` | Future-facing / not currently consumed | None | No runtime effect today |

---

## Onboarding Priority

**Week 1 core context:**
- `facts/product.md` — Know what the company builds and how success is measured.
- `facts/team.md` — Know who owns what and who needs to be informed.
- `norms/process.md` — Know how work moves and what "ready" or "done" means.
- `norms/communication.md` — Know how updates and stakeholder communication actually work.

**Week 2 conditional context:**
- `norms/decisions.md` — Add approval paths, escalation rules, and decision conventions.
- `facts/competitors.md` — Add the actual competitive baseline for analysis-heavy skills.
- `interfaces/data-sources.md` — Add analytics and feedback-channel context for data work.
- `norms/launch-process.md` — Add launch-type rules and approval expectations.

**Optional or future-facing:**
- `interfaces/branding.md` — Fill this in if you plan to use `presentation-deck` Slides mode.
- `facts/glossary.md`, `interfaces/tools.md`, `interfaces/templates.md` — Good to keep current, but shipped skills do not read them today.

**Ongoing:**
- Review and update active and conditional runtime inputs quarterly, or whenever a reorg, process change, tooling migration, or launch-policy change happens. Stale context is worse than missing context — it produces confidently wrong output.
