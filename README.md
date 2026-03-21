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
│   │   └── SKILL.md                  PRD review skill (Analyzer, Tier 1)
│   ├── prd-draft/
│   │   └── SKILL.md                  PRD drafting skill (Generator, Tier 1)
│   └── generate-tasks/
│       └── SKILL.md                  Story decomposition skill (Generator, Tier 1)
├── knowledge/                        Shared PM judgment patterns
│   ├── pm-philosophy.md              Core principles with rationale and behavioral depth
│   ├── prd-quality-criteria.md       What makes a good PRD (evaluative rubric)
│   ├── pm-smell-test.md              Red flags across all PM artifact types
│   ├── acceptance-criteria.md        AC standards optimized for agent implementation
│   └── story-structure.md            Story scoping, splitting, and structure standards
├── company/                          Company-specific context (rebuilt per role)
│   ├── onboarding.md                 Setup checklist for a new company
│   ├── facts/                        Product areas, team structure, glossary
│   ├── norms/                        Sprint process, decision-making, comms patterns
│   └── interfaces/                   Tool configs (Jira, Slack, data sources)
└── eval/                             Evaluation cases per skill
    ├── doc-review/
    │   ├── sample-prd-01.md          Deliberately flawed PRD for testing
    │   └── rubric.md                 Scoring criteria for doc-review output
    ├── prd-draft/
    │   ├── sample-input-01.md        Rough problem statement for drafting test
    │   └── rubric.md                 Quality criteria + bidirectionality test
    └── generate-tasks/
        ├── sample-input-01.md        Clean PRD for story decomposition test
        └── rubric.md                 Story quality + AC standards check
```

---

## Build Phases

Phases are defined by quality gates, not dates. Each phase proves something specific.

| Phase | Name | What it proves | Status |
|-------|------|----------------|--------|
| 1 | Prove the Format | Skill file body structure works. Layer 1 shapes output quality. | ✓ Complete |
| 2 | Prove It Generalizes | Generator skills use the same format. Knowledge layer is bidirectional. | → In progress |
| 3 | Prove Context Matters | Company context measurably improves output. Dual-mode skills work. | Upcoming |
| 4 | Prove Team-Readiness | Agent output passes the "would someone know this was agent-drafted?" test. | Upcoming |
| 5 | Tier 2 Skills | System handles weekly-cadence, multi-skill workflows. | Upcoming |
| 6 | Tier 3 Skills | Skills depending on external data and deep company context work. | Upcoming |
| 7 | Tier 4 Skills | Thinking stack integrates into high-judgment strategic artifacts. | Upcoming |
| 8 | Operators | Generator/Operator separation works. End-to-end workflow touches external systems. | Upcoming |

**Currently in Phase 2.** `prd-draft` and `generate-tasks` prove the format generalizes to Generator skills without breaking changes. The knowledge layer works bidirectionally — `prd-quality-criteria.md` is what `doc-review` evaluates against and what `prd-draft` generates toward; `acceptance-criteria.md` is what `doc-review` checks and what `generate-tasks` produces. Phase 3 adds the company context layer and `status-update`, the first dual-mode skill.

---

## Using the Agent

### Prerequisites

- [Claude Code](https://docs.anthropic.com/en/docs/claude-code) installed

### Setup

```bash
git clone https://github.com/nicoladevera/pm-agent-kit.git
cd pm-agent-kit

# Install all skills as slash commands
./install.sh

# Or install a specific skill
./install.sh doc-review
```

Skills are copied to `~/.claude/commands/` and available immediately — no restart required.

> **Note:** Skills reference knowledge files in the repo (e.g. `knowledge/prd-quality-criteria.md`). Open Claude Code from the repo root so these paths resolve correctly.

### Running a Skill

From the repo root, open Claude Code:

```bash
claude
```

Invoke a skill using its slash command:

```
/doc-review [paste PRD or point to file]
/prd-draft [paste problem statement or brief]
/generate-tasks [paste PRD]
```

Or invoke by name in natural language:

```
Run doc-review on this PRD: [paste or point to file]
```

Both invocation methods work. Slash commands are more reliable when CLAUDE.md auto-loading is inconsistent.

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

Skills have two dimensions: **type** (what they do technically) and **tier** (when they're built and what they require).

| Type | What it does | Current Skills |
|------|-------------|----------------|
| **Generator** | Produces an artifact from inputs (drafts a PRD, generates tasks, creates a launch checklist) | `prd-draft`, `generate-tasks` |
| **Analyzer** | Evaluates, critiques, or extracts signal (reviews a document, synthesizes feedback, interprets a metric) | `doc-review` |
| **Connector** | Connects to an external system to pull data or push output (queries Snowflake, posts to Jira, writes to Confluence) | Not included, always company-specific |

Generators and Analyzers work on inputs the PM provides — pasted text, exported files, local documents. Until Phase 8, the PM is the data pipeline: she exports from Amplitude, pastes support tickets, copies the draft to Google Docs. Connector skills (Phase 8) automate those handoffs by connecting directly to live systems. They are never portable — each one is built for a specific company's tooling.

Some Tier 2 skills are **dual-mode** (Generator + Analyzer) — they assess a situation and produce an artifact from the assessment. `status-update` and `sprint-plan` both work this way.

| Tier | Focus | Skills |
|-------|-------|--------|
| **1 — Operate** | High structure, tight feedback loop | `doc-review` (Analyzer), `prd-draft` (Generator), `generate-tasks` (Generator) |
| **2 — Communicate** | Weekly-cadence, team-visible output | `status-update` (Generator + Analyzer), `sprint-plan` (Generator + Analyzer), `retro-synthesis` (Analyzer), `meeting-brief` (Generator), `decision-log` (Generator) |
| **3 — Orient** | External data, deep company context | `user-feedback` (Analyzer), `competitive-intel` (Analyzer), `data-analysis` (Analyzer), `launch-checklist` (Generator) |
| **4 — Strategize** | High-judgment, composable reasoning | `business-case` (Generator), `presentation-deck` (Generator) |

All three Tier 1 skills are built. Tier 2+ skills are added as the format continues to prove out.

---

## Trust Model

All skills start at **draft-confirm** — the agent drafts, the PM reviews before using. Trust graduates through demonstrated quality, not on a schedule. Skills that produce team-visible output require **explicit approval** before the PM sends them.

---

## Knowledge Files

Knowledge files live in `knowledge/` and are referenced by multiple skills. They encode PM judgment patterns — what "good" looks like, what red flags to watch for, what standards to apply.

| File | What it encodes | Referenced by |
|------|----------------|---------------|
| `pm-philosophy.md` | Ten core PM heuristics with rationale and behavioral examples | All skills |
| `prd-quality-criteria.md` | Eight evaluative criteria for PRDs | `doc-review`, `prd-draft` |
| `pm-smell-test.md` | Red flags across all PM artifact types (specs, comms, decisions) | All reviewing/analyzing skills |
| `acceptance-criteria.md` | AC standards optimized for agent implementation | `doc-review`, `prd-draft`, `generate-tasks` |
| `story-structure.md` | Story scoping, splitting, structure, and data story separation | `generate-tasks` |

---

## Design Principles

- **Portable over company-specific.** PM identity travels. Company context is layered on and stripped away.
- **One skill end-to-end before parallelizing.** Build `doc-review` completely, validate the format, then build the next skill with what you learned.
- **Per-skill degradation rules.** A document review with missing company context can still be useful. A sprint plan without team capacity cannot. Each skill declares its own behavior when context is missing.
- **Knowledge files are shared, skill references are local.** If multiple skills need the same quality criteria, it lives in `knowledge/`. If only one skill needs a reference file, it lives in the skill's folder.
- **Eval before graduation.** No skill advances without at least one eval case: sample input, expected output, scoring rubric.
