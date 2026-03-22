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
│   └── retro-synthesis/
│       └── SKILL.md                  Retro pattern synthesis (Analyzer, Tier 2)
├── references/                       Shared PM judgment patterns
│   ├── pm-philosophy.md              Core principles with rationale and behavioral depth
│   ├── prd-quality-criteria.md       What makes a good PRD (evaluative rubric)
│   ├── pm-smell-test.md              Red flags across all PM artifact types
│   ├── acceptance-criteria.md        AC standards optimized for agent implementation
│   ├── story-structure.md            Story scoping, splitting, and structure standards
│   ├── communication-quality.md      Quality criteria for PM communications
│   ├── sprint-planning.md            Sprint goals, capacity, backlog health standards
│   └── decision-frameworks.md        Decision anatomy, options quality, reversibility
├── knowledge/                        Accumulated PM work product (artifacts produced by skills)
│   ├── README.md                     Folder purpose, conventions, naming guide
│   ├── prds/                         PRDs produced by prd-draft
│   ├── tasks/                        Story sets produced by generate-tasks
│   ├── decisions/                    Decision records produced by decision-log
│   ├── meeting-briefs/               Pre-meeting briefs produced by meeting-brief
│   ├── status-updates/               Status communications produced by status-update (Draft mode)
│   ├── sprint-plans/                 Sprint plans produced by sprint-plan (Draft mode)
│   └── retros/                       Retro syntheses produced by retro-synthesis
├── company/                          Company-specific context (rebuilt per role)
│   ├── onboarding.md                 Setup checklist for a new company
│   ├── facts/                        Product areas, team structure, glossary
│   │   ├── product.md                Product context (stub — populate per company)
│   │   ├── team.md                   Team structure (stub)
│   │   └── glossary.md               Company glossary (stub)
│   ├── norms/                        Sprint process, decision-making, comms patterns
│   │   ├── process.md                Team process (stub)
│   │   ├── decisions.md              Decision-making norms (stub)
│   │   └── communication.md          Communication norms (stub)
│   └── interfaces/                   Tool configs (Jira, Slack, data sources)
│       ├── tools.md                  Tool configuration (stub)
│       └── templates.md              Company templates (stub)
└── evals/                            Evaluation cases per skill
    ├── doc-review/
    │   ├── sample-prd-01.md          Deliberately flawed PRD for testing
    │   └── rubric-prd.md                 Scoring criteria for doc-review output
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
    └── retro-synthesis/
        ├── sample-input-01.md        3 retros with recurring + improving patterns
        └── rubric.md                 Cross-retro synthesis + action item tracking
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
| 6 | Tier 3 Skills | Skills depending on external data and deep company context work. | Upcoming |
| 7 | Tier 4 Skills | Thinking stack integrates into high-judgment strategic artifacts. | Upcoming |
| 8 | Operators | Generator/Operator separation works. End-to-end workflow touches external systems. | Upcoming |

**Currently in Phases 3 + 5.** Phase 2 proved the format generalizes — `prd-draft` and `generate-tasks` use the same file structure without breaking changes, and the references layer works bidirectionally. Phase 5 added all five Tier 2 skills: `decision-log`, `meeting-brief`, `status-update`, `sprint-plan`, and `retro-synthesis`. This introduced dual-mode skills (Generator + Analyzer) and three new reference files for communication, planning, and decision-making. Company context stubs are in place and ready for population. Phase 3 (proving context measurably improves output) runs in parallel as company context gets populated.

---

## Using the Agent

### Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed

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
```

Or invoke by name in natural language:

```
Run doc-review on this document: [paste or point to file]
```

Both invocation methods work within this repo checkout. Slash commands are more reliable when CLAUDE.md auto-loading is inconsistent.

### Setting Up Company Context

When starting at a new company, follow the checklist in `company/onboarding.md`. Populate the files in `company/facts/`, `company/norms/`, and `company/interfaces/` during your first two weeks. Skills improve as context is added.

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
| **Generator** | Produces an artifact from inputs (drafts a PRD, generates tasks, creates a launch checklist) | `prd-draft`, `generate-tasks`, `decision-log`, `meeting-brief` |
| **Analyzer** | Evaluates, critiques, or extracts signal (reviews a document, synthesizes feedback, interprets a metric) | `doc-review`, `retro-synthesis` |
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
| `user-feedback`* | Analyzer | Cluster and summarize customer feedback into themes with frequency, severity, and representative quotes |
| `competitive-intel`* | Analyzer | Monitor the competitive landscape or deep-dive on a specific decision |
| `data-analysis`* | Analyzer | Answer a data question in product context — metric interpretation, funnel analysis, anomaly investigation |
| `launch-checklist`* | Generator | Generate a go-to-market checklist tailored to how this company does launches |
| `business-case`* | Generator | Build the argument for or against an initiative: problem, impact sizing, cost, risks, alternatives considered |
| `presentation-deck`* | Generator | Draft a structured narrative for a specific audience — exec review, QBR, board update, new stakeholder onboarding |

*Not yet built.

| Tier | Focus | Skills |
|-------|-------|--------|
| **1 — Operate** | High structure, tight feedback loop | `doc-review`, `prd-draft`, `generate-tasks` |
| **2 — Communicate** | Weekly-cadence, team-visible output | `status-update`, `sprint-plan`, `retro-synthesis`, `meeting-brief`, `decision-log` |
| **3 — Orient** | External data, deep company context | `user-feedback`, `competitive-intel`, `data-analysis`, `launch-checklist` |
| **4 — Strategize** | High-judgment, composable reasoning | `business-case`, `presentation-deck` |

All Tier 1 and Tier 2 skills are built. Tier 3+ skills are added as company context proves out.

---

## Trust Model

All skills start at **draft-confirm** — the agent drafts, the PM reviews before using. Trust graduates through demonstrated quality, not on a schedule. Skills that produce team-visible output require **explicit approval** before the PM sends them.

---

## Reference Files

Reference files live in `references/` and are consulted by multiple skills. They encode PM judgment patterns — what "good" looks like, what red flags to watch for, what standards to apply.

| File | What it encodes | Referenced by |
|------|----------------|---------------|
| `pm-philosophy.md` | Ten core PM heuristics with rationale and behavioral examples | All skills |
| `pm-smell-test.md` | Red flags across all PM artifact types (specs, comms, decisions) | All reviewing/analyzing skills |
| `project-brief-quality-criteria.md` | Evaluative criteria for project briefs, calibrated to document maturity level | `doc-review` |
| `prd-quality-criteria.md` | Eight evaluative criteria for PRDs | `doc-review`, `prd-draft` |
| `tech-spec-quality-criteria.md` | Evaluative criteria for technical specs / EDDs, from a PM perspective | `doc-review` |
| `ticket-quality-criteria.md` | Evaluative criteria for user stories and tickets | `doc-review` |
| `story-structure.md` | Story scoping, splitting, structure, and data story separation | `doc-review`, `generate-tasks`, `sprint-plan` |
| `acceptance-criteria.md` | AC standards optimized for agent implementation | `doc-review`, `prd-draft`, `generate-tasks`, `sprint-plan` |
| `sprint-planning.md` | Sprint goals, capacity, backlog health, carryover standards | `sprint-plan`, `status-update` |
| `decision-frameworks.md` | Decision anatomy, options quality, reversibility, escalation signals | `decision-log`, `meeting-brief` |
| `communication-quality.md` | Quality criteria for PM communications (status updates, briefs, stakeholder comms) | `status-update`, `meeting-brief`, `decision-log`, `retro-synthesis` |
---

## Design Principles

- **Portable over company-specific.** PM identity travels. Company context is layered on and stripped away.
- **One skill end-to-end before parallelizing.** Build `doc-review` completely, validate the format, then build the next skill with what you learned.
- **Per-skill degradation rules.** A document review with missing company context can still be useful. A sprint plan without team capacity cannot. Each skill declares its own behavior when context is missing.
- **Reference files are shared, skill references are local.** If multiple skills need the same quality criteria, it lives in `references/`. If only one skill needs a reference file, it lives in the skill's folder.
- **Eval before graduation.** No skill advances without at least one eval case: sample input, expected output, scoring rubric.
