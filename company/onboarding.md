# Company Onboarding Checklist

Populate these files during your first two weeks at a new company. Skills improve as context is added — the checklist notes which skill tiers benefit from each file.

---

## facts/

Company-specific knowledge that changes quarterly.

- [ ] **product.md** — Product areas, what each does, user segments, key metrics, how products relate to each other
  - *Unlocks:* More specific doc-review feedback; future skills can reference product context
- [ ] **team.md** — Team structure, who owns what, reporting lines relevant to PM work, key engineering leads
  - *Unlocks:* Tier 2 skills (status-update, sprint-plan) that reference team ownership
- [ ] **glossary.md** — Company-specific terms, acronyms, internal jargon that appear in documents and conversations
  - *Unlocks:* Accurate use of company language in generated artifacts

## norms/

How work gets done. Changes with reorgs or process shifts.

- [ ] **process.md** — Sprint cadence, planning process, how tickets move through the board, definition of done, release process
  - *Unlocks:* Tier 2 skills (sprint-plan, retro-synthesis) that need to understand the team's rhythm
- [ ] **decisions.md** — How decisions get made, who approves what, escalation paths, RFC/ADR process if one exists
  - *Unlocks:* decision-log skill; doc-review can check whether the PRD follows company decision norms
- [ ] **communication.md** — Where conversations happen (Slack channels, meetings, async docs), status update expectations, stakeholder communication patterns
  - *Unlocks:* status-update and meeting-brief skills that need to match company communication style

## interfaces/

Tool configurations. Changes with tooling migrations.

- [ ] **tools.md** — Jira project keys, Confluence spaces, Slack channel names, data sources (Amplitude, Looker, Snowflake), dashboarding tools
  - *Unlocks:* Tier 3 skills and future Operator skills that interact with external systems
- [ ] **templates.md** — Links to company PRD template, ticket template, status update template, or other document templates if they exist
  - *Unlocks:* Generated artifacts can follow company document conventions
- [ ] **branding.md** — Company color palette (hex values), typography (heading/body fonts), logo files, slide layout defaults
  - *Unlocks:* presentation-deck Slides mode generates on-brand .pptx files

---

## Onboarding Priority

**Week 1 (minimum viable context):**
- `facts/product.md` — Know what the company builds
- `norms/process.md` — Know how the team works
- `facts/glossary.md` — Speak the company's language

**Week 2 (full context):**
- Everything else

**Ongoing:**
- Review and update these files quarterly, or when a reorg, process change, or tooling migration happens. Stale context is worse than missing context — it produces confidently wrong output.
