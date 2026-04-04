# Evaluation Rubric — user-feedback (B2B SaaS: Project Management Tool)

**Target input:** `evals/user-feedback/sample-input-02.md`
**Skill under test:** `.claude/skills/user-feedback/SKILL.md`
**Purpose:** Determine whether `user-feedback` correctly clusters feedback by underlying need, distinguishes the search/filter functional failure from cosmetic complaints, avoids manufacturing themes from positive feedback, and notes the competitive mention in context.

**Coverage:** Single mode — full skill coverage.

---

## Expected Themes

The sample contains 20 feedback items across 3 channels with deliberate patterns. The synthesis must identify these 3 major themes:

| # | Expected Theme | Items | Severity | Must Catch? | What good detection looks like |
|---|---------------|-------|----------|-------------|-------------------------------|
| 1 | **Search and filter is unreliable — core functionality broken** | Tickets #4201, #4218, #4239; NPS score-3, score-5 (mentions filters); G2 ★★☆☆☆ (search + combined filters), ★★☆☆☆ (filters not saving) | **Blocking** — users cannot accomplish their core task (finding and filtering tasks). 6 items across all 3 channels. | Yes | Clustered as ONE theme about search/filter unreliability, not split into "search doesn't work" and "filters reset" as separate themes. The underlying failure is the same: the search and filter system is unreliable. Severity assessed as Blocking (users are screenshotting and tracking work outside the tool — a clear "I can't do X" signal). Cross-channel presence noted as a strong signal. This should be the #1 priority. |
| 2 | **Notification fatigue — no priority tiers, everything feels urgent** | Tickets #4205, #4231; NPS score-4; G2 ★★★☆☆ (notification fatigue) | **Painful** — users can accomplish tasks but are cognitively overloaded; high-priority notifications are missed because everything is treated the same. 5 items across all 3 channels. | Yes | Named as a notification fatigue or notification hierarchy theme — the underlying need is "differentiate important notifications from low-priority updates." Not split into "too many notifications" and "no settings" as separate themes. Severity Painful (users are creating workarounds — secondary Slack channels for urgent items — but haven't fully stopped using the tool). |
| 3 | **New workspace setup is too long — adoption friction for growing teams** | NPS score-5, score-6; G2 ★★★☆☆ (setup wizard) | **Painful** — teams that scale frequently face a repeated multi-hour configuration burden before users can start working. 4 items across 2 channels (NPS and G2). | Yes | Named as onboarding or workspace setup friction. The underlying need is "reduce time-to-value for new workspaces." Severity Painful (it's not blocking day-to-day use, but it creates adoption friction every time a new team spins up — high frequency for growing organizations). Cross-channel confirmation noted even if 2-channel vs. 3-channel breadth. |

---

## Noise Items

The sample deliberately includes items that should be classified as noise or low-priority.

| Item | Why it's noise | Must identify? |
|------|---------------|----------------|
| G2 ★★☆☆☆ comment: "dark mode colors are ugly and straining on my eyes. The dark teal on near-black is genuinely hard to read." | Personal aesthetic preference / cosmetic complaint. Mentioned by one user. Does not represent a functional failure or widespread problem. | Yes — must NOT be included as a major theme. May be noted as a cosmetic observation in Signal vs. Noise. |
| G2 ★★★☆☆: "Would love a Gantt chart view... not a dealbreaker but it's the main thing missing for our use case." | Product direction feedback / feature request. One user citing a missing feature that doesn't represent an underlying problem with what exists. Different from the search/filter failure — the timeline view exists, the user just wants a different visualization type. | Should be noted as a low-priority feature request in Signal vs. Noise, not as a theme about product gaps. |

**Critical test for dark mode:** If the synthesis includes "visual comfort" or "dark mode" as a major theme from a single G2 review, that is an over-clustering failure. One item does not meet the minimum frequency threshold for a theme.

---

## Positive Signal — False Positives Check

The Slack and GitHub integration praise represents positive feedback about features that are working well. This should NOT be converted into an action item about integrations.

| Positive signal | What it means | False positive to avoid |
|-----------------|--------------|------------------------|
| Slack integration: NPS score-9 ("saves me an hour a week"), G2 ★★★★★ ("bidirectional sync is flawless") | The Slack integration is a genuine strength — working as intended, valued by users. | "Users want more integrations" must NOT appear as a recommended action. The signal here is that integrations are a competitive advantage — not that more are needed. |
| GitHub integration: NPS score-8, G2 ★★★★★ | Same — the integration is praised, not complained about. | "Expand GitHub integration capabilities" or "build more developer integrations" must NOT appear as a theme derived from this feedback. |

**Pass:** Slack and GitHub integration praise noted explicitly as a product strength in the synthesis. Strength is characterized accurately: "integrations are working well and are a differentiator." **Fail:** "Users want more integrations" appears as a recommended action. Or the positive signal is omitted entirely without acknowledgment.

---

## Search/Filter Clustering Quality

The 6 search/filter items describe 3 different symptoms:
- Simultaneous multi-field filter failure (tickets can't filter assignee + due date together) — Tickets #4201, NPS score-3, G2 ★★☆☆☆
- Search surfacing archived content — Ticket #4218, NPS score-5
- Filters resetting on view navigation — Ticket #4239, G2 ★★☆☆☆ (second review)

All 3 symptoms point to the same underlying issue: the search and filter system is unreliable. They must be clustered as ONE theme.

**Pass:** All 6 items clustered under a single "search/filter unreliable" or equivalent theme. The synthesis notes that symptoms vary but the underlying problem is a single system reliability failure. **Fail:** "Search returns archived tasks" and "filters reset on navigation" appear as separate themes. Or only 4 of the 6 items are included (missing one channel's contribution to the theme).

---

## Competitive Mention

NPS score-4 includes: "We tried switching to Notion but the task management isn't as good. Honestly neither tool is great for what we need."

This is an ambiguous competitive mention — the user is frustrated with both the product AND the competitor. It should NOT be elevated to a churn risk signal.

**Pass:** Competitive mention noted with appropriate hedging: "One user mentions Notion as a comparison point but expresses dissatisfaction with both tools — this does not represent an imminent switch risk to Notion. The user's underlying frustration (notification overload) is captured in Theme 2." **Fail:** "Competitive threat from Notion" or "churn risk to Notion" appears as a major finding. Or the competitive mention is treated as strong evidence of platform switching intent.

---

## Prioritization

Search/filter (Blocking severity, 6 items, 3 channels) must be ranked first.

Priority order should be:
1. Search/filter unreliable — Blocking, 6 items, 3 channels
2. Notification fatigue — Painful, 5 items, 3 channels
3. New workspace setup friction — Painful, 4 items, 2 channels

**Pass:** Search/filter ranked #1. Notification fatigue ranked #2. Workspace setup friction ranked #3. **Fail:** Notification fatigue (Painful) ranked above or equal to search/filter (Blocking) despite lower severity. Or workspace setup ranked #1 despite lower frequency and severity.

---

## Severity Accuracy

| Theme | Expected severity | Reasoning |
|-------|------------------|-----------|
| Search/filter unreliable | Blocking | Users are screenshotting and tracking work outside the tool — explicit "I can't do X" signal. Core functionality is unavailable. |
| Notification fatigue | Painful | Users can still use the tool but have created workarounds (secondary Slack channels). Not blocking but significantly degrades the experience. |
| Workspace setup friction | Painful | Teams can complete setup, but it takes multiple hours and recurs every time a new workspace is created — high frequency pain for growing orgs. |

**Pass:** Severity levels match the actual user impact. Search/filter assessed as Blocking. Notification fatigue and workspace setup both assessed as Painful (not Blocking). **Fail:** All themes rated the same severity level. Search/filter rated Painful when users are explicitly doing work outside the tool.

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| All 3 major themes correctly identified | 30% (10% each) | Search/filter, notification fatigue, and workspace setup all named with correct underlying need framing (not surface feature request framing) |
| Severity levels accurate | 15% | Search/filter = Blocking; notification fatigue = Painful; workspace setup = Painful |
| Noise items correctly classified | 15% | Dark mode complaint NOT elevated to a theme; Gantt chart noted as low-priority feature request, not a product problem theme |
| No false positives on integration strength | 10% | Slack/GitHub integrations noted as a strength; "users want more integrations" does NOT appear as a recommended action |
| Search/filter clustered as one theme (not split by symptom) | 10% | All 6 items under one theme; note that symptoms vary but underlying failure is unified |
| Competitive mention noted with appropriate hedging | 10% | Notion mention characterized as mixed frustration, not imminent churn signal; tied to notification fatigue theme |
| Prioritization order correct | 10% | Search/filter ranked #1; Blocking above Painful themes |
