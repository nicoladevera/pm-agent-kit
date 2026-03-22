# PM Agent Kit

A portable AI agent system that encodes senior product manager judgment into invocable skills. Built for Claude Code.

The agent doesn't replace PM thinking — it removes friction from expressing it. The agent synthesizes, drafts, and structures. The PM evaluates and decides.

---

## How It Works

The system has three layers. The first two are portable across companies. The third changes per role.

**Layer 1 — Identity + Operating Principles** (`CLAUDE.md`)
Who the agent is. How a strong PM thinks. What "good" looks like. What the agent will and won't do. Every skill inherits from this file.

**Layer 2 — Skills** (`skills/`)
Discrete, invocable capabilities. Each skill declares what it does, what context it needs, what approval tier it requires, and how it behaves when context is missing.

**Layer 3 — Company Context** (`company/`)
What makes generic output specific and credible. Product areas, team structure, sprint process, tool configs. Rebuilt at each new company using the onboarding checklist.

---

## Repo Structure

```
pm-agent-kit/
├── CLAUDE.md                         Identity + operating principles
├── skills/                           Invocable capabilities
│   ├── doc-review/
│   │   └── SKILL.md                  PRD review (Analyzer, Tier 1)
│   ├── prd-draft/
│   │   └── SKILL.md                  PRD drafting (Generator, Tier 1)
│   ├── generate-tasks/
│   │   └── SKILL.md                  Story decomposition (Generator, Tier 1)
│   ├── decision-log/
│   │   └── SKILL.md                  Decision capture + framing (Generator, Tier 2)
│   ├── meeting-brief/
│   │   └── SKILL.md                  Pre-meeting prep (Generator, Tier 2)
│   ├── status-update/
│   │   └── SKILL.md                  Delivery assessment + status comms (Gen + Ana, Tier 2)
│   ├── sprint-plan/
│   │   └── SKILL.md                  Sprint planning + backlog health (Gen + Ana, Tier 2)
│   ├── retro-synthesis/
│   │   └── SKILL.md                  Retro pattern synthesis (Analyzer, Tier 2)
│   ├── launch-checklist/
│   │   └── SKILL.md                  Feature launch checklists (Generator, Tier 3)
│   ├── user-feedback/
│   │   └── SKILL.md                  Customer feedback synthesis (Analyzer, Tier 3)
│   ├── data-analysis/
│   │   └── SKILL.md                  Product data interpretation (Analyzer, Tier 3)
│   ├── competitive-intel/
│   │   └── SKILL.md                  Competitive monitoring + deep dives (Analyzer, Tier 3)
│   ├── business-case/
│   │   └── SKILL.md                  Initiative business cases (Generator, Tier 4)
│   └── presentation-deck/
│       └── SKILL.md                  Structured presentation narratives + .pptx (Generator, Tier 4)
├── references/                       Shared PM judgment patterns
│   ├── pm-philosophy.md              Core principles with rationale and behavioral depth
│   ├── prd-quality-criteria.md       What makes a good PRD (evaluative rubric)
│   ├── pm-smell-test.md              Red flags across all PM artifact types
│   ├── acceptance-criteria.md        AC standards optimized for agent implementation
│   ├── story-structure.md            Story scoping, splitting, and structure standards
│   ├── communication-quality.md      Quality criteria for PM communications
│   ├── sprint-planning.md            Sprint goals, capacity, backlog health standards
│   ├── decision-frameworks.md        Decision anatomy, options quality, reversibility
│   ├── launch-readiness.md           Launch readiness dimensions and standards by type
│   ├── feedback-analysis.md          Feedback clustering, severity, signal vs. noise
│   ├── data-interpretation.md        Metric interpretation, funnel analysis, anomaly investigation
│   ├── competitive-analysis.md       Signal classification, monitoring, deep dive structure
│   ├── business-case-standards.md    Impact sizing, cost models, risk assessment, alternatives
│   ├── narrative-structure.md        Narrative arc, deck types, slide-level thinking, audience calibration
│   └── branding-guidelines.md        Presentation branding standards, slide layouts, visual consistency
├── knowledge/                        Accumulated PM work product (artifacts produced by skills)
│   ├── README.md                     Folder purpose, conventions, naming guide
│   ├── prds/                         PRDs produced by prd-draft
│   ├── tasks/                        Story sets produced by generate-tasks
│   ├── decisions/                    Decision records produced by decision-log
│   ├── meeting-briefs/               Pre-meeting briefs produced by meeting-brief
│   ├── status-updates/               Status communications produced by status-update (Draft mode)
│   ├── sprint-plans/                 Sprint plans produced by sprint-plan (Draft mode)
│   ├── retros/                       Retro syntheses produced by retro-synthesis
│   ├── launch-checklists/            Launch checklists produced by launch-checklist
│   ├── feedback/                     Feedback syntheses produced by user-feedback
│   ├── data-analyses/                Data analysis reports produced by data-analysis
│   ├── competitive/                  Competitive snapshots and deep dives produced by competitive-intel
│   ├── business-cases/               Business cases produced by business-case
│   └── presentations/                Presentation narratives and .pptx files produced by presentation-deck
├── company/                          Company-specific context (rebuilt per role)
│   ├── onboarding.md                 Setup checklist for a new company
│   ├── facts/                        Product areas, team structure, glossary
│   │   ├── product.md                Product context (stub — populate per company)
│   │   ├── team.md                   Team structure (stub)
│   │   ├── glossary.md               Company glossary (stub)
│   │   └── competitors.md            Competitive landscape (stub)
│   ├── norms/                        Sprint process, decision-making, comms patterns
│   │   ├── process.md                Team process (stub)
│   │   ├── decisions.md              Decision-making norms (stub)
│   │   ├── communication.md          Communication norms (stub)
│   │   └── launch-process.md         Launch process by type (stub)
│   └── interfaces/                   Tool configs (Jira, Slack, data sources)
│       ├── tools.md                  Tool configuration (stub)
│       ├── templates.md              Company templates (stub)
│       ├── data-sources.md           Data and feedback sources (stub)
│       └── branding.md               Company brand colors, fonts, logo, slide defaults (stub)
└── evals/                            Evaluation cases per skill
    ├── doc-review/
    │   ├── sample-prd-01.md          Deliberately flawed PRD for testing
    │   ├── sample-ticket-01.md       Deliberately flawed ticket for testing
    │   ├── sample-project-brief-01.md  Deliberately flawed project brief for testing
    │   ├── sample-tech-spec-01.md    Deliberately flawed tech spec for testing
    │   ├── rubric-prd.md             Scoring criteria for PRD review output
    │   ├── rubric-ticket.md          Scoring criteria for ticket review output
    │   ├── rubric-project-brief.md   Scoring criteria for project brief review output
    │   └── rubric-tech-spec.md       Scoring criteria for tech spec review output
    ├── prd-draft/
    │   ├── sample-input-01.md        Rough problem statement for drafting test
    │   └── rubric.md                 Quality criteria + bidirectionality test
    ├── generate-tasks/
    │   ├── sample-input-01.md        Clean PRD for story decomposition test
    │   └── rubric.md                 Story quality + AC standards check
    ├── decision-log/
    │   ├── sample-input-01.md        Slack thread with implicit decision debate
    │   └── rubric.md                 Structure extraction + options quality
    ├── meeting-brief/
    │   ├── sample-input-01.md        Overloaded meeting with vague agenda
    │   └── rubric.md                 Decision surfacing + attendee stakes
    ├── status-update/
    │   ├── sample-input-01.md        Sprint board dump with hidden risks
    │   └── rubric.md                 Risk inference + audience calibration
    ├── sprint-plan/
    │   ├── sample-input-01.md        Mixed-readiness backlog with capacity info
    │   └── rubric.md                 Backlog health + realistic capacity math
    ├── retro-synthesis/
    │   ├── sample-input-01.md        3 retros with recurring + improving patterns
    │   └── rubric.md                 Cross-retro synthesis + action item tracking
    ├── launch-checklist/
    │   ├── sample-input-01.md        Beta launch with missing rollback + monitoring
    │   └── rubric.md                 Dimension coverage + gap detection + owner assignment
    ├── user-feedback/
    │   ├── sample-input-01.md        Multi-channel feedback with noise + high-severity signal
    │   └── rubric.md                 Clustering quality + severity accuracy + signal vs. noise
    ├── data-analysis/
    │   ├── sample-input-01.md        Activation drop with funnel data + red herring
    │   └── rubric.md                 Root cause identification + hypothesis ranking
    ├── competitive-intel/
    │   ├── sample-input-01.md        5 signals: noise, signals, and strategic shift
    │   └── rubric.md                 Signal classification + landscape assessment
    ├── business-case/
    │   ├── sample-input-01.md        Rough initiative proposal with partial data + missing alternatives
    │   └── rubric.md                 Impact sizing + alternatives + stress test novelty
    └── presentation-deck/
        ├── sample-input-01.md        Business case needing exec review deck for VP
        └── rubric.md                 Audience calibration + headline quality + narrative arc
```

---

## Build Phases

Phases are defined by quality gates, not dates. Each phase proves something specific.

| Phase | Name | What it proves | Status |
|-------|------|----------------|--------|
| 1 | Prove the Format | Skill file body structure works. Layer 1 shapes output quality. | ✓ Complete |
| 2 | Prove It Generalizes | Generator skills use the same format. Knowledge layer is bidirectional. | ✓ Complete |
| 3 | Prove Context Matters | Company context measurably improves output. Dual-mode skills work. | → In progress |
| 4 | Prove Team-Readiness | Agent output passes the "would someone know this was agent-drafted?" test. | Upcoming |
| 5 | Tier 2 Skills | System handles weekly-cadence, multi-skill workflows. | → In progress |
| 6 | Tier 3 Skills | Skills depending on external data and deep company context work. | → In progress |
| 7 | Tier 4 Skills | Structured stress-testing integrates into high-judgment strategic artifacts. | → In progress |
| 8 | Operators | Generator/Operator separation works. End-to-end workflow touches external systems. | Upcoming |

**Currently in Phases 3 + 7.** Phase 5 added all five Tier 2 skills. Phase 6 added all four Tier 3 skills: `launch-checklist`, `user-feedback`, `data-analysis`, and `competitive-intel`. Phase 7 adds both Tier 4 skills: `business-case` and `presentation-deck`. These are the first skills to integrate structured stress-testing steps (premortem analysis, blindspot checks, conviction assessment) directly into their instruction flow, and `presentation-deck` introduces dual-mode output — markdown narrative and `.pptx` slide generation via `python-pptx`. Three new reference files were added for business case standards, narrative structure, and branding guidelines, plus a company context stub for brand values. Phase 3 (proving context measurably improves output) runs in parallel as company context gets populated.

---

## Using the Agent

### Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed
- `python-pptx` Python package (only needed for `presentation-deck` Slides mode: `pip install python-pptx`)

### Setup

```bash
git clone https://github.com/nicoladevera/pm-agent-kit.git
cd pm-agent-kit

# Register all skills as slash commands for this repo checkout
./install.sh

# Or register a specific skill
./install.sh doc-review
```

`install.sh` copies command files to `~/.claude/commands/`, but those commands still depend on the `references/` and `company/` files in this repo. It sets up slash commands to use this repo, rather than installing a self-contained portable package.

> **Important:** Open Claude Code from this repo root. The registered commands depend on repo-relative paths such as `references/prd-quality-criteria.md` and `company/...`; if you run them outside this checkout, context resolution will break.

### Running a Skill

From the repo root, open Claude Code:

```bash
claude
```

Invoke a skill using its slash command:

```
/doc-review [paste document or point to file — PRD, ticket, project brief, or tech spec]
/prd-draft [paste problem statement or brief]
/generate-tasks [paste PRD]
/decision-log [paste decision context or Slack thread]
/meeting-brief [paste agenda or calendar invite]
/status-update [paste sprint data + specify audience]
/sprint-plan [paste backlog + capacity]
/retro-synthesis [paste retro notes]
/launch-checklist [paste feature description or PRD + launch type]
/user-feedback [paste customer feedback from any channel]
/data-analysis [paste data question + data]
/competitive-intel [paste competitive signals or ask about a competitor]
/business-case [paste problem/opportunity description + any data you have]
/presentation-deck [paste content + specify audience and deck type]
```

Or invoke by name in natural language:

```
Run doc-review on this document: [paste or point to file]
```

Both invocation methods work within this repo checkout. Slash commands are more reliable when CLAUDE.md auto-loading is inconsistent.

### Slides Mode

Slides mode is a runtime workflow, not a shipped renderer. When invoked to generate slides, the skill uses `python-pptx` plus `references/branding-guidelines.md` and `company/interfaces/branding.md` (when substantive) to produce a `.pptx` saved to `knowledge/presentations/`.

Install the dependency if needed:

```bash
python3 -m pip install python-pptx
```

If company branding is missing or still stub-level, the skill should fall back to the clean defaults documented in `references/branding-guidelines.md` and note that in the context note.

### Setting Up Company Context

When starting at a new company, follow the checklist in `company/onboarding.md`. Not every file in `company/` is consumed by shipped skills today.

| File | Status | Current consumers | Missing impact today |
|------|--------|-------------------|----------------------|
| `company/facts/product.md` | Active runtime input | Most shipped skills | Broad quality loss across most skills |
| `company/facts/team.md` | Active runtime input | Planning, status, meeting, decision, launch, business-case, and deck skills | Weaker ownership, stakeholder, and capacity reasoning |
| `company/norms/process.md` | Active runtime input | Planning, status, drafting, decomposition, and retro skills | Weaker planning and process calibration |
| `company/norms/communication.md` | Active runtime input | Status, meeting, competitive, launch, and deck skills | Weaker audience calibration |
| `company/norms/decisions.md`, `company/facts/competitors.md`, `company/norms/launch-process.md`, `company/interfaces/data-sources.md`, `company/interfaces/branding.md` | Conditional runtime input | Only specific skills or Slides mode | Localized quality loss in those paths |
| `company/facts/glossary.md`, `company/interfaces/tools.md`, `company/interfaces/templates.md` | Future-facing / not currently consumed | None | No runtime effect today |

---

## Portability

The system is designed to travel across companies:

- **Portable:** `CLAUDE.md`, `skills/`, `references/`, `evals/` — these encode PM identity and judgment, not company-specific knowledge.
- **Rebuilt per company:** `company/` — product context, team norms, and tool configs change with every role. The onboarding checklist defines what to populate.

Clone the repo, populate `company/`, and the agent produces useful output in context.

---

## Skill Taxonomy

Skills have two dimensions: **type** (what they do technically) and **tier** (when they're built and what they require).

| Type | What it does | Current Skills |
|------|-------------|----------------|
| **Generator** | Produces an artifact from inputs (drafts a PRD, generates tasks, creates a launch checklist, builds a business case, drafts a presentation) | `prd-draft`, `generate-tasks`, `decision-log`, `meeting-brief`, `launch-checklist`, `business-case`, `presentation-deck` |
| **Analyzer** | Evaluates, critiques, or extracts signal (reviews a document, synthesizes feedback, interprets a metric) | `doc-review`, `retro-synthesis`, `user-feedback`, `competitive-intel`, `data-analysis` |
| **Generator + Analyzer** | Assesses a situation and produces an artifact from the assessment (dual-mode) | `status-update`, `sprint-plan` |
| **Connector** | Connects to an external system to pull data or push output (queries Snowflake, posts to Jira, writes to Confluence) | Not included, always company-specific |

Generators and Analyzers work on inputs the PM provides — pasted text, exported files, local documents. Until Phase 8, the PM is the data pipeline: she exports from Amplitude, pastes support tickets, copies the draft to Google Docs. Connector skills automate those handoffs by connecting directly to live systems. They are never portable — each one is built for a specific company's tooling.

Some Tier 2 skills are **dual-mode** (Generator + Analyzer) — they assess a situation and produce an artifact from the assessment. `status-update` and `sprint-plan` both work this way.

### Skill Reference

| Skill | Type | What It Does |
|-------|------|--------------|
| `doc-review` | Analyzer | Evaluate any PM document — PRD, ticket, project brief, or tech spec — against quality criteria appropriate to its type |
| `prd-draft` | Generator | Draft a PRD from a problem statement, user context, and constraints |
| `generate-tasks` | Generator | Generate stories/tasks with acceptance criteria from any source artifact: PRD, EDD, meeting notes, rough notes |
| `status-update` | Generator + Analyzer | Assess delivery state across workstreams and/or produce status comms calibrated to a specific audience |
| `sprint-plan` | Generator + Analyzer | Draft sprint goals from priorities and capacity; flag backlog issues: missing AC, unclear scope, dependency risks |
| `retro-synthesis` | Analyzer | Synthesize retro notes into patterns; track action items across retros and flag which ones were never addressed |
| `meeting-brief` | Generator | Pre-meeting prep: relevant context, open questions, decision points, and attendee stakes |
| `decision-log` | Generator | Capture a decision or structure a problem for resolution — what was decided, by whom, why, options considered |
| `launch-checklist` | Generator | Generate a launch checklist calibrated to launch type (internal/alpha/beta/GA), covering all readiness dimensions |
| `user-feedback` | Analyzer | Cluster and summarize customer feedback into themes with frequency, severity, and representative quotes |
| `competitive-intel` | Analyzer | Monitor the competitive landscape or deep-dive on a specific competitor's approach to a specific problem |
| `data-analysis` | Analyzer | Answer a data question in product context — metric interpretation, funnel analysis, anomaly investigation |
| `business-case` | Generator | Build the argument for or against an initiative: problem, impact sizing, cost, risks, alternatives considered. Includes structured stress test: premortem, blindspot check, conviction assessment. |
| `presentation-deck` | Generator | Draft a structured narrative or generate a branded `.pptx` for a specific audience — exec review, QBR, board update, new stakeholder onboarding |

| Tier | Focus | Skills |
|-------|-------|--------|
| **1 — Operate** | High structure, tight feedback loop | `doc-review`, `prd-draft`, `generate-tasks` |
| **2 — Communicate** | Weekly-cadence, team-visible output | `status-update`, `sprint-plan`, `retro-synthesis`, `meeting-brief`, `decision-log` |
| **3 — Orient** | External data, deep company context | `user-feedback`, `competitive-intel`, `data-analysis`, `launch-checklist` |
| **4 — Strategize** | High-judgment, composable reasoning | `business-case`, `presentation-deck` |

All 14 skills across Tiers 1-4 are built. Tier 4 skills integrate structured stress-testing (premortem, blindspot check, conviction assessment) directly into their instruction flow.

---

## Trust Model

All skills start at **draft-confirm** — the agent drafts, the PM reviews before using. Trust graduates through demonstrated quality, not on a schedule. Skills that produce team-visible output require **explicit approval** before the PM sends them.

---

## Reference Files

Reference files live in `references/` and are consulted by multiple skills. They encode PM judgment patterns — what "good" looks like, what red flags to watch for, what standards to apply.

| File | What it encodes | Referenced by |
|------|----------------|---------------|
| `pm-philosophy.md` | Ten core PM heuristics with rationale and behavioral examples | Foundational for CLAUDE.md; explicitly referenced by `retro-synthesis` |
| `pm-smell-test.md` | Red flags across all PM artifact types (specs, comms, decisions) | All reviewing/analyzing skills |
| `project-brief-quality-criteria.md` | Evaluative criteria for project briefs, calibrated to document maturity level | `doc-review` |
| `prd-quality-criteria.md` | Eight evaluative criteria for PRDs | `doc-review`, `prd-draft` |
| `tech-spec-quality-criteria.md` | Evaluative criteria for technical specs / EDDs, from a PM perspective | `doc-review` |
| `ticket-quality-criteria.md` | Evaluative criteria for user stories and tickets | `doc-review` |
| `story-structure.md` | Story scoping, splitting, structure, and data story separation | `doc-review`, `generate-tasks`, `sprint-plan` |
| `acceptance-criteria.md` | AC standards optimized for agent implementation | `doc-review`, `prd-draft`, `generate-tasks`, `sprint-plan` |
| `sprint-planning.md` | Sprint goals, capacity, backlog health, carryover standards | `sprint-plan`, `status-update` |
| `decision-frameworks.md` | Decision anatomy, options quality, reversibility, escalation signals | `decision-log`, `meeting-brief`, `business-case` |
| `communication-quality.md` | Quality criteria for PM communications (status updates, briefs, stakeholder comms) | `status-update`, `meeting-brief`, `decision-log`, `retro-synthesis` |
| `launch-readiness.md` | Launch readiness dimensions and standards by launch type (internal/alpha/beta/GA) | `launch-checklist` |
| `feedback-analysis.md` | Feedback clustering, severity assessment, signal vs. noise, source channel weighting | `user-feedback` |
| `data-interpretation.md` | Metric interpretation, funnel analysis, anomaly investigation, confidence calibration | `data-analysis` |
| `competitive-analysis.md` | Signal classification, monitoring framework, deep dive structure, reactivity checks | `competitive-intel` |
| `business-case-standards.md` | Impact sizing frameworks, cost model standards, risk assessment, alternatives quality | `business-case` |
| `narrative-structure.md` | Narrative arc (SCR), deck types, slide-level thinking, audience calibration, visual guidance | `presentation-deck` |
| `branding-guidelines.md` | Presentation branding standards, slide layouts, visual consistency, and Slides-mode implementation guidance | `presentation-deck` (Slides mode) |

---

## Design Principles

- **Portable over company-specific.** PM identity travels. Company context is layered on and stripped away.
- **One skill end-to-end before parallelizing.** Build `doc-review` completely, validate the format, then build the next skill with what you learned.
- **Per-skill degradation rules.** A document review with missing company context can still be useful. A sprint plan's Analyze mode can proceed similarly — but its Draft mode cannot produce a plan without capacity data, and the skill explicitly stops there. The frontmatter rule governs missing context files; skills with multiple modes may enforce mode-specific stops within their instruction bodies.
- **Reference files are shared, skill references are local.** If multiple skills need the same quality criteria, it lives in `references/`. If only one skill needs a reference file, it lives in the skill's folder.
- **Eval before graduation.** No skill advances without at least one eval case: sample input plus a scoring rubric.
