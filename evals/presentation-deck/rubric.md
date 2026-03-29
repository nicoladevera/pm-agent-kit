# Evaluation Rubric — presentation-deck (Narrative Mode)

**Target input:** `evals/presentation-deck/sample-input-01.md`
**Skill under test:** `skills/presentation-deck/SKILL.md`
**Purpose:** Determine whether `presentation-deck` correctly identifies the deck type, calibrates to the specific audience (VP Sarah), produces takeaway headlines, maintains a coherent narrative arc, proactively addresses the VP's known concerns, and applies the stress test for this high-stakes deck.

## Coverage

**This rubric tests:** Narrative mode — markdown slide-by-slide structure with headlines, speaker notes, and visual guidance.
**Not covered here:** Slides mode (.pptx generation via python-pptx) — deferred pending environment dependency.

---

## Deck Type Identification

The input specifies "exec review" and describes a VP who needs to make a funding decision in 30 minutes.

**Pass:** Deck type identified as Exec Review. Length calibrated to 8-12 slides (appropriate for 30 minutes). **Fail:** Wrong deck type. More than 15 slides for a 30-minute VP meeting.

---

## Audience Calibration

The input provides specific information about VP Sarah:
- Skeptical about technical debt
- Values data-driven arguments
- Will ask about the Q2 OKR connection
- Wants to hear you've thought about risks
- Decides quickly with clear data, stalls with hand-wavy analysis

### Critical tests:

**Recommendation appears early.** For a VP exec review, the recommendation should be in the first 2-3 slides, not buried after 8 slides of context. Sarah decides quickly if the data is clear — give her the answer first.

**Data-first framing.** The argument should lead with numbers (480 hours, $135K/year, CSAT 2.1 → 3.8), not qualitative statements. Sarah values data over narrative.

**Tech debt concern addressed proactively.** The business case mentions compliance complexity as a risk. The deck should address Sarah's tech debt concern directly — probably by highlighting the two-way door (feature flag), the compliance review already completed by legal, and the phased approach that minimizes rushed execution.

**Q2 OKR connection explicit.** The input mentions a Q2 OKR to "reduce support cost per user by 15%." The deck should connect the initiative directly to this OKR — it's the strongest alignment argument.

**Risk surfaced prominently.** Sarah asks "what's the biggest risk?" The deck should have a slide that names the biggest risk (cancellation rate increase from removing friction) and shows the mitigation (feature flag, monitoring, rollback criteria). This builds credibility.

**Pass:** Recommendation in first 2-3 slides. Data leads the argument. Tech debt concern addressed. Q2 OKR connected explicitly. Risk has its own slide with mitigation. **Fail:** Recommendation buried. Qualitative lead. Sarah's concerns not addressed. OKR not mentioned. Risks in a footnote.

---

## Headline Quality

Every slide headline must be a takeaway, not a topic label.

| Topic label (wrong) | Takeaway headline (right) |
|---------------------|--------------------------|
| Problem Overview | 40% of support tickets are cancellation requests costing 480 agent-hours/month |
| Proposed Solution | Self-service cancellation reclaims $135K/year and moves CSAT from 2.1 to 3.8 |
| Cost Analysis | $180K investment pays back in 16 months on cost savings alone |
| Risks | Removing friction may increase cancellations — feature flag allows controlled rollback |
| Recommendation | Fund self-service cancellation for Q2; defer referral program one quarter |

**Test:** Can you read only the headlines, in order, and follow the full argument from problem through evidence to recommendation?

**Pass:** Every headline states a takeaway. The headline sequence tells the story independently. **Fail:** Any headline is a topic label ("Background," "Next Steps," "Cost"). Headlines don't form a coherent sequence.

---

## Narrative Arc Coherence

The deck should follow a clear Situation → Complication → Resolution arc:

- **Situation:** We have 85K MAU, support handles 6K+ tickets/month, Q2 OKR targets 15% support cost reduction.
- **Complication:** 40% of tickets are cancellations (480 hours/month, CSAT 2.1). Current flow requires email + 6-hour wait. We're behind competitive table stakes.
- **Resolution:** Self-service cancellation flow, $180K investment, 16-month payback, direct OKR contribution.

**Test:** Each slide earns the next. No slide feels randomly placed. The "so what?" between adjacent slides is clear.

**Pass:** Clear SCR arc. Logical progression. No random topic jumps. **Fail:** Slides could be reordered without losing meaning. The reader loses the thread.

---

## Source Material Adaptation

The input provides a summarized business case. The deck should transform this content for slides, not copy it.

### Critical tests:

**Content is restructured for the audience.** The business case presents information in standard order (problem → impact → solution → cost → risk → alternatives → recommendation). The deck should reorder for a VP: recommendation → impact → problem evidence → cost/ROI → risks/mitigation → ask.

**Detail level is appropriate.** A VP doesn't need all four alternatives described in full. She needs to know the recommended option, the strongest alternative, and why the recommendation wins.

**The referral program trade-off is addressed.** The input says Sarah needs to "decide whether to fund this and deprioritize the referral program." The deck must frame this trade-off explicitly — not pretend the referral program doesn't exist.

**Pass:** Content restructured for VP audience. Not a copy-paste of the business case. Referral program trade-off addressed directly. **Fail:** Business case sections mapped 1:1 to slides. All four alternatives given equal space. Referral program trade-off omitted.

---

## Risk Surfacing

The business case identifies three risks. The deck should surface them — especially the most interesting one (cancellation rate increase from removing friction).

**The cancellation-friction risk is the key test.** This is the risk Sarah will ask about — it's counterintuitive and shows the PM has thought deeply. It should be on a slide with a clear mitigation (feature flag, monitoring, rollback criteria).

**Tech debt concern addressed.** The deck should proactively address Sarah's known skepticism about rushed features creating production incidents. The two-way door, legal's pre-review, and phased approach all help here.

**Pass:** Risks on a dedicated slide, not buried. Cancellation-friction risk named with mitigation. Tech debt concern addressed proactively. **Fail:** Risks in a footnote. Cancellation-friction risk not mentioned. Sarah's tech debt concern not addressed.

---

## Stress Test Application

This is an Exec Review — the stress test should always be applied for this deck type.

### Narrative Premortem

**Expected failure modes:**
- Sarah sees this as a "nice to have" not a strategic priority — the deck fails to connect to Q2 OKR
- The data feels hand-wavy and Sarah stalls — impact sizing isn't concrete enough
- Sarah fixates on the tech debt risk because of last quarter's incident — the deck doesn't address it proactively
- The ask is unclear — Sarah leaves without knowing exactly what she's approving

### Audience Blindspot

**Expected blindspots:**
- Sarah may want to know what happens to the 2 agents whose work gets automated — staffing implications
- Sarah may ask about the competitive landscape — who else has self-service and how does ours compare
- Sarah may want a phased approach — can we ship a partial version to validate before committing the full $180K

**Pass:** Stress test applied. At least 2 specific premortem failure modes relevant to this audience. At least 1 blindspot that addresses something not in the main narrative. **Fail:** Stress test omitted. Generic failure modes. Blindspots repeat what's already in the deck.

---

## Speaker Notes and Visual Guidance

### Speaker notes should:
- Anticipate Sarah's likely questions at key slides
- Note where to pause for her input (she decides quickly — give her room to)
- Add context about the competitive landscape or comparable implementations
- Flag the transition logic between slides

### Visual guidance should:
- Specify chart types for data slides (e.g., "Bar chart: current cancellation ticket volume by month")
- Suggest the right visualization for the ROI argument
- Note where a simple data callout is better than a chart

**Pass:** Speaker notes anticipate specific questions from Sarah. Visual guidance is specific (chart type, data to show). **Fail:** Speaker notes are generic ("discuss this slide"). Visual guidance is "add a visual."

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| Deck type correctly identified | 10% | Exec Review, 8-12 slides, calibrated for 30-minute decision meeting |
| Audience calibration | 20% | Recommendation first, data-driven, tech debt addressed, Q2 OKR connected, risk prominent |
| Headline quality | 15% | Every headline is a takeaway; headline sequence tells the story |
| Narrative arc coherence | 15% | Clear SCR arc; logical progression; each slide earns the next |
| Source material faithfully adapted | 10% | Restructured for VP (not copy-paste), referral trade-off addressed, appropriate detail level |
| Risk surfacing | 10% | Dedicated risk slide, cancellation-friction risk named with mitigation, tech debt concern addressed |
| Speaker notes and visual guidance | 10% | Anticipates Sarah's questions, specific visual types, transition logic noted |
| Output format and stress test | 10% | Matches Narrative format; stress test applied with specific failure modes and blindspots |
