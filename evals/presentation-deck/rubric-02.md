# Evaluation Rubric — presentation-deck (Consumer Media: Recommendation Algorithm Review)

**Target input:** `evals/presentation-deck/sample-input-02.md`
**Skill under test:** `skills/presentation-deck/SKILL.md`
**Purpose:** Determine whether `presentation-deck` correctly calibrates for a data-first VP audience, leads with the recommendation (not a data walkthrough), surfaces the conversion drop prominently despite the PM's instinct to lead with engagement wins, and structures a coherent SCR arc that names the tension between metrics as the complication.

**Coverage:** Narrative mode tested. Slides mode (.pptx generation) not covered.

---

## Deck Type Identification

The PM is presenting results + a recommendation to their VP of Product. The VP needs to make a decision: keep, roll back, or run follow-up experiment.

**Pass:** Deck type identified as Exec Review. Length calibrated to 8-12 slides (appropriate for a VP decision meeting). Not a Business Review (too operational) and not a Research Readout (too findings-oriented — a decision is required).
**Fail:** Deck type identified as Research/Discovery Readout or Business Review. More than 15 slides for a VP decision meeting.

---

## VP Audience Calibration

The input explicitly states: Priya is data-first and wants the recommendation upfront. She'll be skeptical of spin. She needs to decide.

### Critical tests:

**Recommendation appears on slide 1 or slide 2.** Priya doesn't want a build-up.

**Pass:** Slide 1 or executive summary opens with the recommendation: "Keep the algorithm update — engagement gains are real — but the conversion drop requires investigation before we declare success. Recommendation: keep the update and run a conversion experiment."
**Fail:** Opens with "Background on Our Recommendation Algorithm" or slides 1-3 are context-setting before the recommendation appears. Priya will ask "so what?" before the answer appears.

**Data framed as evidence, not as a walkthrough.** Numbers presented to support the recommendation, not to walk through a methodology.

**Pass:** The engagement numbers (CTR: 8.2% → 11.4%, watch time: 42 → 47 min) appear alongside the recommendation as evidence, not as a separate "Results" section the reader has to evaluate on their own.
**Fail:** A "Results" section with four metrics before any recommendation or interpretation. The reader has to decide what the data means before the PM tells them.

**Priya's known skepticism acknowledged.** She's already told the PM she'll be skeptical of spin. The PM's instinct to lead with wins is explicitly flagged as risky in the input.

**Pass:** The narrative explicitly resists the "wins first, problems later" structure. Conversion drop appears in the first 2 slides alongside the engagement wins.
**Fail:** Engagement wins dominate slides 1-4. Conversion drop appears in slide 5 or later under "risks" or "areas for improvement."

---

## Headline Quality

Every slide headline must state a takeaway, not a topic label.

| Topic label (wrong) | Takeaway headline (right) |
|---------------------|--------------------------|
| Algorithm Update Results | Personalization drove a 39% lift in recommendations clicked — and a conversion drop we need to address |
| Engagement Metrics | Watch time per session is up 12%, confirming users are engaging more deeply with recommended content |
| Conversion Impact | Trial-to-paid conversion dropped 0.7pp — likely linked to the algorithm, not explained yet |
| Recommendation | Keep the update and run a conversion experiment before declaring success |
| Next Steps | We need 4-6 weeks of A/B data to test the satisfaction-trap hypothesis |

**Test:** Can you read only the headlines, in order, and understand that (a) engagement improved, (b) conversion dropped, (c) these are in tension, and (d) the recommendation is to keep the update while investigating the conversion problem?

**Pass:** Every headline is a takeaway. The headline sequence conveys the tension between metrics and names the recommendation. A reader scanning only headlines understands the argument.
**Fail:** Any headline is a topic label ("Algorithm Overview," "Data," "Risks"). Headlines form a chronological walkthrough rather than an argument.

---

## Conversion Drop Surfaced Prominently

This is the most important test in this rubric. The PM explicitly asked to "lead with engagement wins" — an instinct the narrative should not honor uncritically.

**Pass:** The conversion drop (-0.7pp trial-to-paid) appears in the first 2 slides alongside the engagement wins. Not in a caveats section. Not in appendix. The framing acknowledges the tension directly: "The algorithm update produced strong engagement gains but introduced a conversion risk we don't yet fully understand." The narrative treats the conversion drop as the central unresolved question, not as a footnote to an otherwise positive story.

The SCR complication is this tension: "Personalization improved engagement significantly, but trial conversion dropped — and we don't yet know if these are causally linked or whether one is acceptable given the other."

**Fail:** Engagement wins in slides 1-3 with conversion drop mentioned in slide 4+. Conversion drop under "risks" or "concerns" at the end. The PM's instinct to "lead with the wins" honored without challenge.

**The narrative should push back on the PM's framing.** The skill should produce a narrative that says, in effect: "Leading with wins without surfacing the conversion drop early would undermine your credibility with Priya." This doesn't need to be explicit in the output — but the structure should reflect it.

---

## SCR Arc Coherent

**Situation:** We updated our recommendation algorithm from popularity-based to personalized taste graph. It's been live for 3 weeks at 100% of users.

**Complication:** Engagement improved substantially (+39% CTR, +12% watch time) but trial-to-paid conversion dropped (-0.7pp). These metrics are in tension. We have a hypothesis (the "satisfaction trap") but no causal evidence yet. MAU is flat.

**Resolution:** Keep the update — rolling back would sacrifice the engagement gains with no guarantee it restores conversion. Run a conversion experiment to test the satisfaction-trap hypothesis and identify a fix.

**Pass:** All three SCR components present and logically connected. The complication is the tension between two metrics, not just "we have a problem." The resolution is a recommendation with a follow-up action, not just "keep" or "roll back."
**Fail:** Complication is missing — just good news then a pivot to next steps. Or SCR elements appear but aren't logically connected (complication doesn't set up the resolution).

---

## Stress Test: Anticipating Priya's Questions

The VP will ask "is this causal?" about the conversion drop. She'll want to know if we have evidence the algorithm caused the drop, or if it's coincidental.

**Pass:** The narrative anticipates this question and provides: (a) the "satisfaction trap" hypothesis as the working explanation, (b) honest acknowledgment that we don't have causal proof (no holdback group was run), and (c) the proposed experiment design to test the hypothesis. The presenter doesn't claim the link is proven — they acknowledge the causal uncertainty and show they have a plan to resolve it.

**Pass also:** Anticipates the follow-up question "why didn't you run a holdback group?" with a brief note (e.g., "we rolled out to 100% — in retrospect a holdback would have given us cleaner data on causality").

**Fail:** Conversion drop presented as "possibly due to the algorithm" without anticipating Priya's causal question. No experiment proposed to test the hypothesis. The presenter seems to hope the question won't be asked.

---

## Risk Prominent, Not Buried

**Pass:** Conversion risk appears alongside the engagement wins — not in a risks section after the recommendation. The structure treats both the wins and the conversion drop as headline findings of equal standing. The risk is the reason the recommendation is "keep and investigate" rather than "declare success."

**Fail:** Conversion risk in a "Risks and Considerations" section after the recommendation. Or in an appendix. Or framed as a minor qualification on an otherwise positive story.

---

## Output Format Compliance

**Pass:** Narrative mode output with: header block (deck type, audience, purpose, estimated length), agent block (YAML), narrative arc stated, slide-by-slide structure with takeaway headlines, content, visual guidance, and speaker notes. Stress test section (Exec Review — required). Smell test section. Context note.
**Fail:** Missing agent block. Missing stress test. Headlines are topic labels. No speaker notes. Fewer than 8 slides or more than 12 for a VP decision meeting.

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| VP audience calibration (recommendation upfront, no spin) | 15% | Recommendation on slide 1 or 2; data used as evidence, not walkthrough; Priya's skepticism-of-spin acknowledged in structure |
| Headline quality (takeaway not topic) | 15% | Every headline states an insight; headline sequence conveys the argument and the tension |
| Conversion drop surfaced prominently in first half | 25% | Conversion drop appears in first 2 slides alongside engagement wins; not in a caveats section; narrative resists PM's "wins first" instinct |
| SCR arc coherent with metric tension as the complication | 20% | Situation, complication (two metrics in tension), and resolution (keep + experiment) all present and logically connected |
| Stress test anticipates Priya's causal question | 15% | "Is this causal?" anticipated; satisfaction-trap hypothesis named; experiment proposed; holdback group absence acknowledged |
| Output format compliance | 10% | Narrative mode format; agent block; stress test section; context note; 8-12 slides |
