# Evaluation Rubric — discovery-plan (International Expansion)

**Target input:** `evals/discovery-plan/sample-input-02.md`
**Skill under test:** `skills/discovery-plan/SKILL.md`
**Purpose:** Determine whether `discovery-plan` handles a greenfield discovery scenario with thin input, maximum uncertainty, and strong organizational pressure (CEO enthusiasm, board push) — testing assumption extraction from sparse context, appropriate method selection when the team has no existing user base in the target market, and intellectual honesty when the prevailing narrative is optimistic.
**Coverage:** Single mode — full skill coverage. Tests thin-input intake behavior.

---

## Intake Behavior

The input is deliberately thin — "I don't even know what I don't know." The skill should trigger thin-input intake: present a structured interpretation and ask the PM to confirm before building the plan.

**Pass:** Structured interpretation presented. Problem space reframed from "how to expand to LatAm" to "should we expand to LatAm, and if so, which market and how?" Decision named (board meeting recommendation in 6-8 weeks). **Fail:** Skill proceeds directly without confirming framing. Accepts "LatAm expansion" as the premise rather than the hypothesis.

---

## Problem Space Framing

The CEO says "restaurants everywhere have the same inventory problems." This is the core assumption — and it might be wrong. The skill must frame the discovery around validating whether the opportunity exists, not how to execute an expansion that's been assumed.

**Good framing:** "The team hypothesizes that LatAm represents a growth opportunity because restaurant inventory problems are universal. This discovery plan tests that hypothesis — whether the problem exists in target LatAm markets, whether our product fits the local context, and whether the business model works — before committing to a localization roadmap."

**Bad framing:** "We need to plan the LatAm expansion. Here's what we need to learn about the market." (This assumes expansion is the right move.)

**Pass:** Framed as opportunity validation, not expansion planning. The CEO's statement treated as a testable assumption. Decision named (whether to recommend LatAm expansion at the board meeting). **Fail:** Expansion treated as decided. Discovery framed as "how" not "whether."

---

## Assumption Extraction from Sparse Context

With thin input, the skill must extract assumptions from what's implied, not just what's stated.

### Expected assumptions (at minimum):

**Problem assumptions:**
1. Restaurants in LatAm have the same inventory management problems as US restaurants
2. The LatAm restaurant market is large enough to justify the investment
3. Existing solutions in LatAm are inadequate (there's a gap to fill)

**User assumptions:**
4. LatAm restaurant operators would use a SaaS tool for inventory management (not spreadsheets, pen-and-paper, or locally-built solutions)
5. LatAm restaurant operators can afford SaaS pricing comparable to US pricing
6. Decision-makers in LatAm restaurants have similar buying patterns to US counterparts

**Solution assumptions:**
7. Our product can be adapted for LatAm markets (supply chain patterns, distributor integrations, food safety categories are US-specific)
8. Localization is primarily a language/currency problem, not a fundamental product redesign
9. A single LatAm strategy works — or at minimum, Mexico and Brazil can be treated similarly

**Viability assumptions:**
10. The unit economics work at LatAm price points
11. We can acquire customers in a market where we have zero brand recognition and no team with local language skills
12. Payment infrastructure, regulatory requirements, and business practices don't create prohibitive barriers

### Critical tests:

**The "same inventory problems" assumption must be called out explicitly.** It's the CEO's core thesis and the most dangerous assumption — if it's wrong, nothing else matters.

**Assumption #9 (single LatAm strategy) is a hidden assumption the skill should surface.** Mexico, Brazil, and Colombia are very different markets. Treating "LatAm" as one market is itself an assumption.

**At least 8 assumptions should be mapped.** With this much uncertainty, fewer than 8 means the skill isn't looking hard enough.

**Pass:** 8+ assumptions mapped across all four types. The CEO's core thesis named as the highest-risk assumption. "LatAm as one market" surfaced as a hidden assumption. Assumptions stated as testable claims. **Fail:** Fewer than 6 assumptions. CEO's thesis accepted rather than tested. No hidden assumptions surfaced.

---

## Method Selection for Zero-Presence Markets

The team has no users, no data, no presence, and no local language skills in LatAm. This fundamentally constrains the method menu.

### Expected methods:

1. **Competitive proxy analysis** — what existing inventory management solutions exist in LatAm? Who are the incumbents? What do they charge? This is the cheapest starting point and can be done remotely.
2. **Expert interviews / market informant interviews** — the board member with Brazil restaurant connections is explicitly mentioned. Industry contacts, local operators, or market analysts can provide context the team can't get from desk research.
3. **Inbound lead interviews** — 12 inbound inquiries from LatAm exist. These are warm leads who've already expressed interest. The skill must recommend interviewing them.
4. **Secondary research / desk research** — market sizing, regulatory landscape, payment infrastructure, restaurant industry structure in target markets.
5. **Data mining of inbound inquiries** — analyze the 12 inquiries for patterns (what features they asked about, what size restaurants, what they're currently using).

### Critical tests:

**The 12 inbound inquiries must be identified as a research asset.** They're the only direct signal from the target market. If the skill doesn't recommend interviewing these leads, it missed the most accessible evidence source.

**The board member's connections must be named as a recruiting channel.** The input mentions them explicitly.

**User interviews with US restaurant customers should NOT be the primary method.** US customers don't validate LatAm assumptions. If the skill defaults to studying the existing user base, it's avoiding the hard question.

**A/B testing and prototype testing should NOT be recommended.** There's no product to test in these markets yet. The discovery is about whether the opportunity exists, not how to build for it.

**Pass:** Competitive analysis and desk research as starting points. Inbound leads interviewed. Expert/market informant interviews via board connections. No inappropriate methods (A/B tests, prototype tests). Method rationale acknowledges the zero-presence constraint. **Fail:** Defaults to US customer interviews. Ignores the 12 inbound leads. Recommends methods that require local presence or product access.

---

## Intellectual Honesty Under Organizational Pressure

The input has clear organizational pressure: CEO enthusiasm, board member pushing, investor expectations. The skill must produce a plan that tests the hypothesis honestly, not one designed to confirm the desired conclusion.

**Pass:** Plan explicitly tests "should we?" not just "how should we?" Evidence criteria include failure scenarios (what results would recommend *against* expansion). At least one assumption is framed in a way that could invalidate the entire initiative. The plan doesn't read as a pre-justification for a decision already made. **Fail:** Plan is structured to build the case for expansion. No failure criteria that could invalidate the opportunity. Organizational enthusiasm reflected in the framing.

---

## Sequencing for Maximum Information Value

With thin evidence and high stakes, sequencing should front-load the cheapest, most disqualifying research.

### Expected sequence logic:

1. **Desk research + competitive analysis + inbound lead analysis** (weeks 1-2) — cheapest, fastest, and could surface disqualifying information (e.g., strong incumbents, regulatory barriers, tiny addressable market)
2. **Expert/informant interviews** (weeks 2-4) — via board connections and industry contacts. Fills gaps that desk research can't cover.
3. **Inbound lead interviews** (weeks 3-5) — deeper conversations with the 12 LatAm inquiries to understand their context, needs, and current solutions.
4. **Synthesis + board recommendation** (weeks 6-7) — synthesize findings into a go/no-go/learn-more recommendation.

**Pass:** Cheapest disqualifying research first. Decision points that could stop the plan early. Timeline fits 6-8 week constraint. Sequence builds from secondary to primary research. **Fail:** Expensive or slow methods front-loaded. No early exit points. Timeline exceeds the board meeting deadline.

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| Intake behavior | 10% | Thin-input intake triggered; structured interpretation presented; "whether" not "how" framing |
| Assumption extraction quality | 15% | 8+ assumptions across all four types; CEO thesis flagged; "LatAm as one market" surfaced |
| Risk ranking judgment | 15% | Core thesis ranked highest; market existence assumptions before execution assumptions |
| Method selection appropriateness | 20% | Competitive analysis + desk research first; inbound leads interviewed; no inappropriate methods; zero-presence constraint respected |
| Intellectual honesty | 15% | Tests "should we?" not "how?"; failure criteria included; plan could invalidate the initiative |
| Sequencing logic | 10% | Cheapest disqualifying research first; early exit points; fits 6-8 week constraint |
| Scope realism | 5% | Acknowledges language barrier; recruiting challenges for expert interviews; timeline honest |
| Output format compliance | 10% | Matches format; context note present; smell test completed; Agent Block populated |
