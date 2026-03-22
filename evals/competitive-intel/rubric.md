# Evaluation Rubric — competitive-intel (Monitor Mode)

**Target input:** `evals/competitive-intel/sample-input-01.md`
**Skill under test:** `skills/competitive-intel/SKILL.md`
**Purpose:** Determine whether `competitive-intel` correctly classifies signals, distinguishes noise from strategic shifts, produces implications connected to product decisions, and avoids recency bias.

---

## Mode Detection

The input provides a batch of competitive signals and asks for "a competitive update." This should trigger **Monitor mode**.

**Pass:** Monitor mode selected. **Fail:** Deep Dive mode selected, or mode not stated.

---

## Signal Classification

The five signals are deliberately designed to test all three classification levels:

| # | Signal | Correct Classification | Why |
|---|--------|----------------------|-----|
| 1 | PayFlex dashboard redesign | **Noise** | Minor visual changes, no new functionality. A "refreshed look and feel" with rounded corners and updated colors is cosmetic. Doesn't change the competitive picture. |
| 2 | PayFlex pricing model change | **Signal** | A structural pricing change: flat fee → tiered with a free tier and an API. This changes how they acquire users (free tier lowers barrier), how they monetize (tiered upsell), and signals a platform direction (API access). This is the kind of change that directly affects competitive dynamics. |
| 3 | SplitPay $45M Series C + consumer expansion | **Strategic shift** | A B2B company entering the consumer market with $45M in fresh funding is a market entry event. This introduces a new competitor in our space with significant resources. The "platform for both sides" language signals long-term ambition beyond a feature add. |
| 4 | LendEasy adding installment plan management | **Signal** | A BNPL company adding installment plan management means a previously indirect competitor is moving into adjacent territory. Not a full strategic shift (they're adding a feature, not pivoting), but it narrows the competitive gap. |
| 5 | PayFlex enterprise job postings | **Signal** (potentially early indicator of strategic shift) | Three enterprise-specific hires when they've historically been consumer-only is a meaningful hiring signal. It's early — hiring plans don't always materialize — but it suggests PayFlex may be moving up-market. |

### Critical tests:

**Signal 1 must be classified as Noise.** This is the easiest test. If the dashboard redesign is analyzed as significant, the skill is over-indexing on competitor activity.

**Signal 3 must be classified as Strategic Shift.** This is the most significant signal in the batch: a well-funded company entering our market from an adjacent space. If this is classified merely as "signal," the analysis is underweighting market entry events.

**Signal 2 should not be treated as noise.** The pricing change is structural — introducing a free tier and an API signals a meaningful strategy shift in how PayFlex acquires and retains users.

**Pass:** All 5 signals classified correctly. Signal 1 = Noise, Signal 3 = Strategic Shift. **Fail:** Signal 1 treated as significant, or Signal 3 not given top prominence.

---

## Analysis Quality

### SplitPay (Strategic Shift) should receive the deepest analysis

The SplitPay entry is the most strategically important signal. The analysis should:
- Identify that this is a new market entrant, not just a competitor update
- Note the $45M in funding as a capability signal (they have resources to execute)
- Assess what "platform for both sides" means for the market structure
- Evaluate how their B2B DNA might be an advantage or disadvantage in consumer
- Connect to implications: does this change our urgency? Our positioning? Our roadmap?

**Pass:** SplitPay receives the most analytical depth. Implications are concrete. **Fail:** SplitPay gets the same treatment as a PayFlex job posting.

### PayFlex pricing change should be analyzed concretely

The analysis should:
- Note the free tier as a user acquisition lever (reduces barrier to entry)
- Identify the API access in Pro tier as a platform signal
- Compare to our pricing model (if product context is available) or flag that comparison requires product context
- Assess whether this changes competitive dynamics on price

**Pass:** Pricing change analyzed with specific implications. **Fail:** Pricing change merely described without interpretation.

### PayFlex enterprise hiring should be flagged as an early signal

The analysis should:
- Note that this is the first time enterprise roles appear
- Assess it as an early indicator of potential up-market move
- Appropriately hedge — hiring signals are forward-looking and uncertain
- Connect to Signal 2 (API access in Pro tier could also be an enterprise play)

**Pass:** Enterprise hiring noted as forward-looking signal, connected to the API offering. Hedged appropriately. **Fail:** Stated as fact that PayFlex is pivoting to enterprise, or dismissed entirely.

---

## Landscape Assessment

The overall landscape should be assessed as **Shifting**, based on:
- A new entrant (SplitPay) entering the consumer market with significant funding
- An existing competitor (PayFlex) restructuring pricing and potentially moving up-market
- An adjacent competitor (LendEasy) expanding into installment management

The key trend should capture that the installment plan space is attracting investment and adjacent players are converging on it.

**Pass:** Landscape assessed as Shifting or Disrupting with a clear key trend. **Fail:** Assessed as Stable despite three meaningful competitive moves.

---

## Recency Bias Check

The SplitPay Series C announcement (Signal 3) is the "loudest" signal — a TechCrunch article with a big funding number. The analysis should not let this dominate at the expense of the PayFlex pricing change (Signal 2), which may be more immediately impactful.

The PayFlex pricing change directly affects current competitive dynamics today. The SplitPay entry is strategic but further out — they haven't launched a consumer product yet.

**Pass:** Both signals receive appropriate weight. The analysis acknowledges that SplitPay is strategically more significant but PayFlex's pricing change is more immediately relevant. **Fail:** SplitPay dominates to the point where PayFlex pricing barely gets mentioned, or vice versa.

---

## Recommended Actions

The analysis should produce recommendations that are:
- **Specific** — not "keep monitoring" but "monitor SplitPay's consumer product launch timeline and PayFlex's pricing impact on our trial-to-paid conversion"
- **Calibrated** — major signals warrant concrete action; noise warrants dismissal
- **Actionable** — the PM knows what to do next

Expected recommendations should include:
- Assess our pricing model in light of PayFlex's free tier (respond or note)
- Monitor SplitPay's consumer product development (note — they haven't launched yet)
- Watch PayFlex enterprise hiring for pattern confirmation (note)
- No action needed on dashboard redesign (ignore) or LendEasy feature add (note)

**Pass:** At least 3 specific, calibrated recommendations. **Fail:** Generic "continue monitoring the competitive landscape."

---

## Noise Handling

Signal 1 (PayFlex dashboard redesign) should be explicitly classified as noise and dismissed in the "Noise (Noted, No Action)" section with a brief explanation of why.

**Pass:** Dashboard redesign appears in the noise section, not in significant signals. **Fail:** Dashboard redesign analyzed alongside the pricing change and enterprise hiring.

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| All 5 signals classified correctly | 20% | Noise = noise, signals = signals, strategic shift = strategic shift |
| SplitPay given top strategic prominence | 15% | Deepest analysis, market entry implications, funding as capability signal |
| PayFlex pricing analyzed concretely | 15% | Free tier, API, and platform signals identified; competitive impact assessed |
| PayFlex enterprise hiring appropriately hedged | 10% | Flagged as early signal, not stated as fact; connected to API offering |
| Dashboard redesign dismissed as noise | 5% | Appears in noise section, not analyzed as significant |
| Landscape assessed as Shifting | 10% | Key trend captures convergence of adjacent players into installment space |
| Recency bias avoided | 10% | SplitPay and PayFlex pricing both given appropriate weight |
| Recommendations are specific and calibrated | 10% | At least 3 concrete, actionable recommendations |
| Output format compliance | 5% | Matches monitor mode format; context note present |
