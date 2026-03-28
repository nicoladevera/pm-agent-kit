# Competitive Analysis Standards

What makes competitive intelligence useful for product decisions. Use this to monitor the competitive landscape, analyze specific competitors, classify signals, and connect competitive intelligence to product strategy. The external-facing counterpart to `user-feedback-analysis.md` — that file covers what users tell you; this file covers what the market shows you.

Competitive intelligence is not a news summary. A summary says "CompetitorX launched feature Y." Intelligence says "CompetitorX launched feature Y, which addresses the same onboarding friction we identified in Q1. Their approach prioritizes speed over accuracy, which works for SMB but won't satisfy enterprise buyers — where we're stronger. No action needed on our roadmap, but this strengthens the case for accelerating our onboarding redesign."

---

## Signal Classification

### Not Everything Matters

Competitors do things constantly. Most of it is noise. The skill is in knowing what to pay attention to.

| Classification | Definition | Examples | Appropriate response |
|---------------|------------|---------|---------------------|
| **Noise** | Routine activity that doesn't change the competitive picture. | Minor UI tweaks, blog posts, small feature additions that don't affect positioning. | Note and dismiss. No analysis needed. |
| **Signal** | Meaningful product, pricing, or positioning change that could affect the competitive dynamic. | New pricing tier, significant feature launch, new market entry, major partnership. | Analyze: what changed, what it means for us, whether any action is warranted. |
| **Strategic shift** | A change in the competitor's fundamental direction — their ICP, business model, platform strategy, or market positioning. | Pivoting from SMB to enterprise. Launching a platform/ecosystem play. Changing pricing model from per-seat to usage-based. Major acquisition. | Deep analysis: what they're doing, why, what it means for the market, how it affects our positioning and roadmap. |

**Red flag:** Treating noise as signal (overreacting to minor competitor activity). Treating strategic shifts as noise (missing fundamental market changes). The classification should be explicit, not implicit.

---

### Signal Sources and Reliability

Different sources provide different quality of intelligence. Weight them accordingly.

| Source | What it reveals | Reliability | Bias |
|--------|----------------|-------------|------|
| **Product teardowns** | What they actually built, how it works, UX quality | High — you can verify firsthand | Limited to what's publicly visible. Enterprise features behind paywalls or sales gates aren't visible. |
| **Pricing and packaging pages** | How they segment the market, what they value most | High — pricing is a strategic signal | Changes may lag the actual strategy. Pricing experiments aren't always permanent. |
| **Changelogs / release notes** | Cadence and direction of product development | Medium — they control the narrative | Companies highlight strengths and downplay weaknesses. Not everything shipped appears in the changelog. |
| **Job postings** | Where they're investing (teams, technologies, markets) | Medium — forward-looking signal | Hiring plans don't always materialize. Postings may lag actual needs by months. |
| **Press releases / blog posts** | Strategic narrative, market positioning, partnerships | Low-medium — heavily curated | Maximum spin. Designed to impress investors, customers, and press. Trust the signal direction, not the specifics. |
| **Customer feedback (mentioning competitors)** | How users perceive the competitive dynamic | Medium — reflects real perception | Users may have outdated information about competitors. Mentions in churn reasons are stronger signal than casual mentions. |
| **G2 / Capterra reviews** | Feature gaps, satisfaction, competitive positioning | Medium — aggregated user perception | Self-selecting reviewers. Reviews are sticky and may reflect old product versions. |
| **Patent filings** | Where they're investing in R&D, future direction | Low — very forward-looking | Most patents never become products. Useful as a weak signal of investment direction. |

**Red flag:** Treating a press release as fact. Ignoring product teardowns in favor of blog posts. Drawing strategic conclusions from a single source.

---

## Monitoring Framework

### What to Track

When monitoring the competitive landscape, track across these dimensions:

| Dimension | What to watch for | Why it matters |
|-----------|------------------|---------------|
| **Product changes** | New features, removed features, UX changes, platform shifts | Indicates where they're investing and what problems they're solving |
| **Pricing** | Price changes, new tiers, model changes (per-seat → usage), free tier changes | Pricing is the most direct competitive lever. Changes signal strategy. |
| **Positioning** | How they describe themselves, who they say they're for, value propositions on homepage | Positioning changes often precede product changes. "We're now an enterprise platform" → expect enterprise features. |
| **Hiring** | What roles they're hiring, what teams are growing, what technologies they mention | Reveals investment priorities months before product ships |
| **Partnerships / integrations** | New integration partners, channel partnerships, ecosystem plays | Shows who they're trying to be adjacent to and what workflows they want to own |
| **Funding / financial** | Fundraising rounds, revenue signals, layoffs, cost-cutting | Signals whether they have runway to compete aggressively or are under pressure |

### Monitoring Cadence

Regular monitoring (monthly or per competitive signal batch) should:
1. Review signals from all dimensions
2. Classify each as noise / signal / strategic shift
3. Analyze significant signals
4. Assess the overall landscape direction
5. Compare to the prior monitoring snapshot

---

## Deep Dive Framework

### Structure for Analyzing a Specific Competitor's Approach

When analyzing how a specific competitor approaches a specific problem or area:

**1. Their approach**
- What they built — the actual product solution, not the marketing description
- How it works — user flow, architecture (if visible), key design decisions
- Who it's for — their target user for this capability
- How they position it — the language, the value proposition, the competitive framing

**2. Strengths**
- Where their approach genuinely works well
- What they do better than us in this specific area
- Evidence: product teardown observations, user reviews, feature comparisons

**3. Weaknesses**
- Where their approach falls short
- What they got wrong or haven't solved
- Evidence: user complaints, feature gaps, architectural limitations

**4. Comparison to our approach**
- Not just feature-by-feature, but philosophical: What trade-offs did they make vs. what trade-offs did we make?
- Where are we genuinely stronger? Where are they genuinely stronger?
- What's the same, and what are the meaningful differences?

**5. Learnings**
- What can we learn from their approach?
- Not "copy this feature" but "this principle or technique is worth considering"
- What did they validate that we hypothesized? What surprised us?

**6. Strategic implications**
- Does this change our positioning? Our roadmap? Our urgency?
- Is action warranted, or is this informational?
- What would change our assessment? (e.g., "if they extend this to enterprise, it becomes a direct threat")

---

## Avoiding Reactivity

### Respond, Note, or Ignore

Not every competitive signal requires a response. The instinct to react to every competitor move is a trap — it pulls the roadmap away from user needs toward competitive parity chasing.

| Assessment | When to use | Response |
|-----------|-------------|----------|
| **Respond** | The competitive move directly threatens our position in a way users will notice. Revenue or retention impact is likely. | Adjust roadmap, accelerate a competing initiative, or change positioning. |
| **Note** | The move is meaningful but doesn't require immediate action. It changes the competitive picture but doesn't threaten our core position. | Track it. Revisit at next planning cycle. |
| **Ignore** | The move is noise, doesn't affect our ICP, or is in a market segment we don't compete in. | Dismiss explicitly and move on. |

**Red flag:** Responding to every competitive launch as if it's a crisis. Ignoring a strategic shift because "we're not worried about them." The right response depends on how the move affects our users and our position, not how loud the signal is.

---

## Implications Framework

### "So What?"

Every piece of competitive intelligence should answer "so what?" — how does this connect to decisions we need to make?

| Category | Question to answer |
|----------|-------------------|
| **Product** | Does this change what we should build or when? |
| **Positioning** | Does this change how we should describe ourselves or differentiate? |
| **Pricing** | Does this change how we should price or package? |
| **Urgency** | Does this increase or decrease the urgency of any current initiative? |
| **Risk** | Does this introduce a new risk we weren't tracking? |

If the answer to all five is "no," the signal is informational — worth noting but not worth acting on. Say so explicitly. "No action needed" is a valid and valuable conclusion.

---

## Competitive Landscape Structure

### How to Map the Competitive Picture

When assessing the overall landscape (not a single competitor):

- **Market segments:** How is the market divided? Where do we play? Where don't we?
- **Positioning map:** Where does each competitor sit? Who's going up-market? Down-market? Lateral?
- **Feature comparison:** On the dimensions that matter to our ICP, where is each competitor strong/weak? (Not every feature — only the ones users compare.)
- **Trend direction:** Is the market consolidating? Fragmenting? Is a new entrant disrupting? Is a segment being abandoned?

**Red flag:** Feature comparison matrices that list every feature regardless of relevance. Positioning maps that don't account for where the market is moving, only where it is now.

---

## Using These Standards

**For competitive monitoring (`competitive-intel` monitor mode):** Classify signals. Analyze what's significant. Dismiss what's noise. Assess the overall landscape direction. Connect to product decisions.

**For competitive deep dives (`competitive-intel` deep dive mode):** Analyze the competitor's actual approach, not their marketing. Compare philosophically, not just feature-by-feature. Identify learnings and implications. Check reactivity.

**For interpreting competitive mentions in other skills:** When competitors come up in customer feedback, PRDs, status updates, or business cases, apply these standards to assess the competitive significance. A user mentioning a competitor is signal; it's not necessarily a mandate to match their feature set.
