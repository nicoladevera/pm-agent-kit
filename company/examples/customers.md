> **This is an example file.** Replace all content below with your company's actual context. The goal is to show what "substantive" means — enough detail that a skilled PM reading this file could immediately understand who the customers are, what drives them, where they show up in data, and what their signals of success or churn look like.

---

# Customer Context

## Buyer vs. User

**Spendulum is B2C — the buyer and the user are the same person.** No procurement layer, no admin buying for employees, no parent buying for a dependent (with rare exceptions). The person who downloads the app is the person who decides to keep using it.

The free-to-Plus conversion creates a meaningful economic buyer moment: the user who upgrades is making an active purchase decision. Their motivation differs from a new free user — they're not just curious about the product, they're committing to it. Upgrade candidates care more about reliability and depth of features than newcomers, who are primarily evaluating whether the app creates value before friction sets in.

**The one nuance:** A small segment of Plus subscribers are couples managing shared finances. One person typically drives the decision; the other is a passive beneficiary. This affects churn risk — if the driving partner stops engaging, the other rarely continues.

---

## Customer Segments

**Budget-Curious Newcomer** — 24–28 years old, first job or early career. Approximate volume: the largest acquisition segment (~55% of new installs). Has never built a consistent budgeting habit. Motivated by spending anxiety, not a specific financial goal. Low patience for setup friction or feature complexity. This segment defines the D7 churn problem — they download during a moment of financial stress, get some initial value, and disappear if the habit doesn't stick.

What they care about: Seeing their spending without effort. Immediate signal that the app is working. Not being lectured about money.

**Goal-Driven Saver** — 28–35 years old, mid-career, specific savings target (emergency fund, down payment, travel fund, wedding). Approximate volume: ~30% of active users, ~60% of Plus subscribers. This is the highest-LTV segment. Willing to connect a bank account if it reduces manual tracking. Stays engaged as long as they're making progress toward their goal; churns when a life event disrupts the routine (new job, move, relationship change).

What they care about: Tracking progress against a specific goal. Accurate, low-maintenance transaction categorization. Insight into where savings potential is hiding.

**Re-engager** — Previously used a budgeting app (Mint, YNAB, a spreadsheet), stopped, and is trying again. Approximate volume: ~15% of new installs. Has stronger opinions than newcomers — they know what they don't want (too complex, too much setup, too aggressive about upsell). Skeptical of onboarding promises. Responds to "pick up where you left off" framing and low-friction re-entry.

What they care about: Getting to value faster than last time. Feeling like the product understands them, not just acquired them.

---

## Pain Points and Buying Triggers

**Budget-Curious Newcomer:**
- Pain: Vague anxiety about overspending. Gets to the end of the month not knowing where money went. Feels out of control without visibility.
- Buying trigger: A specific moment of financial shock — overdraft, a large unexpected expense, first paycheck from a new job that felt smaller than expected.
- What "good enough" looks like: Any tool that gives them a picture of their spending with less friction than a spreadsheet.

**Goal-Driven Saver:**
- Pain: Has a target but no reliable way to track progress. Spreadsheet is too manual; other apps require too much setup upfront. Bank statements are retroactive, not predictive.
- Buying trigger: Life milestone with a financial component — engagement, planned home purchase, a friend hitting their savings goal and mentioning how they did it.
- What "good enough" looks like: A tool that syncs automatically and tells them if they're on track for their goal without requiring weekly maintenance.

**Re-engager:**
- Pain: Their previous app required too much setup, broke when they changed jobs or banks, or they simply lost the habit. They want to try again but are protecting themselves from wasted effort.
- Buying trigger: New Year, a stressful financial event, or an explicit recommendation from someone they trust.
- What "good enough" looks like: Getting to first value in under 5 minutes, without feeling like they're starting from zero.

---

## Key Accounts

Spendulum is B2C — no named enterprise accounts. The relevant high-value cohorts:

**Plus subscribers** — 4.2% of the active user base. Disproportionate LTV. Predominantly Goal-Driven Savers. Bank-synced users are twice as likely to convert to Plus. These users are the primary retention signal and the most important segment for monetization work.

**"First value moment" achievers** — Users who log a transaction within 24 hours of signup (currently 51% of users who complete onboarding). This cohort's D7 and D30 retention is ~2.5x the users who don't hit the first value moment. Used as the primary leading indicator for onboarding health.

**Bank-synced users** — A behavioral cohort, not a demographic one. Synced users show significantly higher 30-day retention regardless of segment. Sync failure rate (currently 8.3%) is an active risk to this cohort's engagement.

---

## Discovery and Evaluation

**Primary discovery channels:**
- App store search (organic, personal finance category) — highest-volume, lowest intent signal
- Word of mouth / friend recommendation — lower volume, highest conversion and LTV
- Personal finance content (YouTube, TikTok) — growing acquisition channel, skews younger, Budget-Curious Newcomer segment

**What customers compare us against during evaluation:**
- Mint (sunsetted December 2023 — significant migration opportunity, many users actively looking for alternatives)
- YNAB — direct alternative for Goal-Driven Savers; higher price point, steeper learning curve; users who find YNAB overwhelming become Spendulum prospects
- Copilot and Monarch Money — design-forward alternatives at similar or higher price points
- Spreadsheets — not a competitor product but the default fallback, especially for Re-engagers and Goal-Driven Savers who tried apps and stopped

**Common pre-purchase objections:**
- "Do I have to connect my bank account?" — No-bank-account path is a key differentiator; must be communicated early in evaluation
- "I've tried these before and stopped" — Re-engager objection; addressed by low-friction first session and fast time-to-value
- "Is my data safe?" — More common for bank sync users; legal requires "informational, not advice" framing

**What tips toward committing vs. walking away:**
- Committing: Seeing a picture of their spending within the first 5 minutes without being forced to connect a bank account
- Walking away: Setup friction before any value is visible; overly instructional or preachy tone in onboarding

---

## Voice-of-Customer Channels

**App store reviews (App Store + Google Play)**
- Signal type: Feature frustration, comparison to alternatives, churn reasons ("used to use Mint"), occasional praise
- Volume: ~15–25 new reviews per week across both platforms
- Cadence: Continuous; spikes after releases
- Bias: Strongly skews to extremes — very happy or very frustrated. Neutral users rarely review. Bank sync issues are over-represented because failures prompt visible, public frustration.
- Access: PM reviews weekly; Growth PM owns response cadence

**In-app NPS survey**
- Signal type: Quantitative score + open-ended verbatim on promoters and detractors
- Volume: ~200–300 responses per quarter
- Cadence: Quarterly batches; survey triggers at D30 for engaged users only
- Bias: Surveying D30 engaged users means it misses the D7 churners — the most important churn cohort isn't represented here
- Access: Growth PM owns NPS; verbatims available in Amplitude

**Support tickets (Zendesk)**
- Signal type: Problems, not praise. Dominated by bank sync failures, billing questions, and categorization errors
- Volume: ~80–120 tickets per week; spikes when sync provider has incidents
- Cadence: Daily; reviewed by support team, escalated to PM weekly
- Bias: Skews toward technical failure states and high-friction moments. Doesn't represent passive churn — users who quietly stop coming back don't file tickets.
- Access: Support lead owns; PM gets weekly summary

**User interviews**
- Signal type: Qualitative insight on motivations, workflow, and unmet needs; best source for understanding the "why" behind behavioral patterns
- Volume: 5–8 interviews per quarter, conducted by Growth PM
- Cadence: Quarterly; typically aligned to planning cycles
- Bias: Recruited from engaged users — similar sampling problem as NPS; churned users are rarely captured
- Access: Interview notes in Notion; synthesis lives in `knowledge/feedback/`

---

## Churn and Retention Signals

**Leading indicators of churn:**
- No second transaction logged after initial setup (strongest D7 churn predictor)
- Budget created but no check-in activity in days 3–7
- Bank sync failure with no re-authentication within 48 hours
- Push notification opt-out within first 3 days (correlates with low week-2 return rate)

**Leading indicators of retention and expansion:**
- Bank account connected (single strongest retention signal)
- 3+ sessions in the first week
- Savings goal created (correlates with Plus upgrade; Goal-Driven Savers who set a goal convert at ~3x the rate of those who don't)
- Weekly return rate in weeks 2–4 (users with 3 consecutive weekly returns have significantly higher D90 retention)

**Patterns in churned accounts:**
- Budget-Curious Newcomers churn most often at D7, before forming a return habit. The root cause is two failure modes: never logging a second transaction, or creating a budget but never returning to check progress. Both are active focus areas in Q1 2026.
- Goal-Driven Savers churn during life transitions — new job (income change disrupts budget categories), move (new expense patterns), or when a goal is reached without a new one to replace it.
- Re-engagers churn when the app fails to feel meaningfully different from their last attempt — too much friction, or a sync failure early in the experience.

**What re-engages lapsed users:**
- "You're back — here's where you left off" moment: showing previous data and progress without requiring re-setup
- Goal progress notification after a period of inactivity: "You're $400 away from your emergency fund goal"
- Not yet systematically tested; user interview feedback suggests it would resonate with Re-engagers and Goal-Driven Savers with dormant goals
