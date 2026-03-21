# PM Agent Kit

A portable AI agent system that encodes senior PM judgment into invocable skills. Built for Claude Code.

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
│   └── doc-review/
│       └── SKILL.md                  PRD review skill (Analyzer, Tier 1)
├── knowledge/                        Shared PM judgment patterns
│   ├── pm-philosophy.md              Core principles with rationale and behavioral depth
│   ├── prd-quality-criteria.md       What makes a good PRD (evaluative rubric)
│   ├── pm-smell-test.md              Red flags across all PM artifact types
│   └── acceptance-criteria.md        AC standards optimized for agent implementation
├── company/                          Company-specific context (rebuilt per role)
│   ├── onboarding.md                 Setup checklist for a new company
│   ├── facts/                        Product areas, team structure, glossary
│   ├── norms/                        Sprint process, decision-making, comms patterns
│   └── interfaces/                   Tool configs (Jira, Slack, data sources)
└── eval/                             Evaluation cases per skill
    └── doc-review/
        ├── sample-prd-01.md          Deliberately flawed PRD for testing
        └── rubric.md                 Scoring criteria for doc-review output
```

---

## Current State

**Phase 1 — Prove the Format.** The scaffold is built. `doc-review` is the first complete skill, scoped to PRD review. The knowledge files encode PM judgment patterns that skills reference for quality criteria. The eval case provides a way to test whether `doc-review` catches what a strong PM would catch.

Phase 1 is done when `doc-review` produces output the PM would put her name on without editing.

---

## Using the Agent

### Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed
- Open a terminal session in this repo's root directory

### Running a Skill

Open Claude Code in the repo root. Skills are invoked by name:

```
Run doc-review on this PRD: [paste or point to file]
```

The agent reads the skill's `SKILL.md`, loads the referenced knowledge files, and produces structured output.

### Setting Up Company Context

When starting at a new company, follow the checklist in `company/onboarding.md`. Populate the files in `company/facts/`, `company/norms/`, and `company/interfaces/` during your first two weeks. Skills improve as context is added.

---

## Portability

The system is designed to travel across companies:

- **Portable:** `CLAUDE.md`, `skills/`, `knowledge/`, `eval/` — these encode PM identity and judgment, not company-specific knowledge.
- **Rebuilt per company:** `company/` — product context, team norms, and tool configs change with every role. The onboarding checklist defines what to populate.

Clone the repo, populate `company/`, and the agent produces useful output in context.

---

## Skill Taxonomy

Skills are categorized by type and build tier. Type describes what a skill does technically. Tier defines the build sequence.

| Type | What it does |
|------|-------------|
| **Generator** | Produces an artifact from inputs (drafts a PRD, generates tasks, creates a launch checklist) |
| **Analyzer** | Evaluates, critiques, or extracts signal (reviews a document, synthesizes feedback, interprets a metric) |
| **Operator** | Takes action in an external system (posts to Jira, queries a database) — always company-specific |

| Tier | Focus | Skills |
|------|-------|--------|
| **1 — Operate** | High structure, tight feedback loop | `doc-review`, `prd-draft`, `generate-tasks` |
| **2 — Communicate** | Weekly-cadence, team-visible output | `status-update`, `sprint-plan`, `retro-synthesis`, `meeting-brief`, `decision-log` |
| **3 — Orient** | External data, deep company context | `user-feedback`, `competitive-intel`, `data-analysis`, `launch-checklist` |
| **4 — Strategize** | High-judgment, composable reasoning | `business-case`, `presentation-deck` |

Only Tier 1 skills are built in Phase 1. Others are added as the format is proven.

---

## Trust Model

All skills start at **draft-confirm** — the agent drafts, the PM reviews before using. Trust graduates through demonstrated quality, not on a schedule. Skills that produce team-visible output require **explicit approval** before the PM sends them.

---

## Knowledge Files

Knowledge files live in `knowledge/` and are referenced by multiple skills. They encode PM judgment patterns — what "good" looks like, what red flags to watch for, what standards to apply.

| File | What it encodes | Referenced by |
|------|----------------|---------------|
| `pm-philosophy.md` | Ten core PM heuristics with rationale and behavioral examples | All skills |
| `prd-quality-criteria.md` | Eight evaluative criteria for PRDs | `doc-review`, future `prd-draft` |
| `pm-smell-test.md` | Red flags across all PM artifact types (specs, comms, decisions) | All reviewing/analyzing skills |
| `acceptance-criteria.md` | AC standards optimized for agent implementation | `doc-review`, future `generate-tasks` |

---

## Design Principles

- **Portable over company-specific.** PM identity travels. Company context is layered on and stripped away.
- **One skill end-to-end before parallelizing.** Build `doc-review` completely, validate the format, then build the next skill with what you learned.
- **Per-skill degradation rules.** A document review with missing company context can still be useful. A sprint plan without team capacity cannot. Each skill declares its own behavior when context is missing.
- **Knowledge files are shared, skill references are local.** If multiple skills need the same quality criteria, it lives in `knowledge/`. If only one skill needs a reference file, it lives in the skill's folder.
- **Eval before graduation.** No skill advances without at least one eval case: sample input, expected output, scoring rubric.
