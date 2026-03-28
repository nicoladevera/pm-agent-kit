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
├── CLAUDE.md              Identity + operating principles
├── skills/                Invocable capabilities (one folder per skill)
├── references/            Shared PM judgment patterns
├── knowledge/             Accumulated PM work product (artifacts produced by skills)
├── company/               Company-specific context (rebuilt per role)
└── evals/                 Evaluation cases per skill (sample inputs + rubrics)
```

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

> **Important:** Open Claude Code from this repo root. The registered commands depend on repo-relative paths such as `references/quality-criteria-prd.md` and `company/...`; if you run them outside this checkout, context resolution will break.

### Running a Skill

From the repo root, open Claude Code:

```bash
claude
```

Invoke a skill using its slash command:

```
/doc-review [paste document or point to file — PRD, ticket, project brief, tech spec, or any document]
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

Follow the checklist in `company/onboarding.md`. Most skills degrade noticeably without substantive `company/facts/product.md`, `company/facts/team.md`, and `company/facts/customers.md` — these three files have the broadest impact. Other files in `company/` have localized or conditional impact and are noted in the onboarding checklist.

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
| **Generator** | Produces an artifact from inputs (drafts a PRD, generates tasks, creates a launch checklist, builds a business case, drafts a presentation) | `prd-draft`, `generate-tasks`, `decision-log`, `meeting-brief`, `launch-checklist`, `business-case`, `presentation-deck`, `status-update`, `sprint-plan` |
| **Analyzer** | Evaluates, critiques, or extracts signal (reviews a document, synthesizes feedback, interprets a metric) | `doc-review`, `retro-synthesis`, `user-feedback`, `competitive-intel`, `data-analysis` |
| **Connector** | Connects to an external system to pull data or push output (queries Snowflake, posts to Jira, writes to Confluence) | Not included, always company-specific |

Generators and Analyzers work on inputs the PM provides — pasted text, exported files, local documents. The PM is the data pipeline: she exports from Amplitude, pastes support tickets, copies the draft to Google Docs. Connector skills automate those handoffs by connecting directly to live systems. They are never portable — each one is built for a specific company's tooling.


### Skill Reference

| Skill | Type | What It Does |
|-------|------|--------------|
| `doc-review` | Analyzer | Evaluate any PM document — PRD, ticket, project brief, tech spec, or any general document — against quality criteria appropriate to its type |
| `prd-draft` | Generator | Draft a PRD from a problem statement, user context, and constraints |
| `generate-tasks` | Generator | Generate stories/tasks with acceptance criteria from any source artifact: PRD, EDD, meeting notes, rough notes |
| `status-update` | Generator | Assess delivery state across workstreams and/or produce status comms calibrated to a specific audience |
| `sprint-plan` | Generator | Draft sprint goals from priorities and capacity; flag backlog issues: missing AC, unclear scope, dependency risks |
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
| `quality-criteria-general-document.md` | Six universal quality dimensions for documents that don't fit specialized types | `doc-review` |
| `quality-criteria-project-brief.md` | Evaluative criteria for project briefs, calibrated to document maturity level | `doc-review` |
| `quality-criteria-prd.md` | Eight evaluative criteria for PRDs | `doc-review`, `prd-draft` |
| `quality-criteria-tech-spec.md` | Evaluative criteria for technical specs / EDDs, from a PM perspective | `doc-review` |
| `quality-criteria-ticket.md` | Evaluative criteria for user stories and tickets | `doc-review` |
| `story-structure.md` | Story scoping, splitting, structure, and data story separation | `doc-review`, `generate-tasks`, `sprint-plan` |
| `acceptance-criteria.md` | AC standards optimized for agent implementation | `doc-review`, `prd-draft`, `generate-tasks`, `sprint-plan` |
| `sprint-planning.md` | Sprint goals, capacity, backlog health, carryover standards | `sprint-plan`, `status-update` |
| `decision-frameworks.md` | Decision anatomy, options quality, reversibility, escalation signals | `decision-log`, `meeting-brief`, `business-case` |
| `audience-registers.md` | Per-audience communication registers — tone, depth, and framing calibrated by stakeholder type (engineers, designers, data, leadership, cross-functional) | `status-update`, `meeting-brief`, `presentation-deck` |
| `pushback-and-negotiation.md` | Scope protection, saying no, problem reframing, escalation as fork-framing, navigating disagreement | `doc-review`, `sprint-plan`, `decision-log`, `status-update`, `meeting-brief` |
| `communication-quality.md` | Quality criteria for PM communications (status updates, briefs, stakeholder comms) | `status-update`, `meeting-brief`, `decision-log`, `retro-synthesis` |
| `launch-readiness.md` | Launch readiness dimensions and standards by launch type (internal/alpha/beta/GA) | `launch-checklist` |
| `user-feedback-analysis.md` | Feedback clustering, severity assessment, signal vs. noise, source channel weighting | `user-feedback` |
| `data-interpretation.md` | Metric interpretation, funnel analysis, anomaly investigation, confidence calibration | `data-analysis` |
| `competitive-analysis.md` | Signal classification, monitoring framework, deep dive structure, reactivity checks | `competitive-intel` |
| `business-case-standards.md` | Impact sizing frameworks, cost model standards, risk assessment, alternatives quality | `business-case` |
| `narrative-structure.md` | Narrative arc (SCR), deck types, slide-level thinking, audience calibration, visual guidance | `presentation-deck` |
| `slide-design.md` | Visual composition: information hierarchy, layout patterns, density budgets, typography, color strategy, visual storytelling, designed-vs-default checklist | `presentation-deck` (Slides mode) |
| `branding-guidelines.md` | Presentation branding standards, slide layouts, visual consistency, and Slides-mode implementation guidance | `presentation-deck` (Slides mode) |

---

## Design Principles

- **Portable over company-specific.** PM identity travels. Company context is layered on and stripped away.
- **One skill end-to-end before parallelizing.** Each skill is complete and self-contained. The tier progression is intentional: Tier 1 proved the format; each subsequent tier built on that proof.
- **Per-skill degradation rules.** A document review with missing company context can still be useful. A sprint plan's Analyze mode can proceed similarly — but its Draft mode cannot produce a plan without capacity data, and the skill explicitly stops there. The frontmatter rule governs missing context files; skills with multiple modes may enforce mode-specific stops within their instruction bodies.
- **Reference files are shared, skill references are local.** If multiple skills need the same quality criteria, it lives in `references/`. If only one skill needs a reference file, it lives in the skill's folder.
- **Eval before graduation.** No skill advances without at least one eval case: sample input plus a scoring rubric.
