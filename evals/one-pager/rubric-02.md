# Evaluation Rubric — one-pager (Compression: API Integration Business Case)

**Target input:** `evals/one-pager/sample-input-02.md`
**Skill under test:** `.claude/skills/one-pager/SKILL.md`
**Purpose:** Determine whether `one-pager` correctly compresses a full business case into a single page, recalibrates from an internal decision-making audience to a cross-functional partnership audience, preserves the core argument without distortion, applies the Feedback ask type correctly, and maintains the one-page constraint under compression pressure.
**Coverage:** Compression workflow. Tests information triage, audience recalibration, compression fidelity, Feedback ask type handling, and one-page constraint enforcement when source material is long.

---

## Compression Detection

The input provides a full business case (1,200+ words of source material) with explicit framing: "I need a one-pager version of it." The skill should recognize this as a compression job without the PM having to flag it.

**Pass:** Skill identifies this as compression (not from-scratch) and adapts accordingly — reading the full business case before compressing. The `source_artifact` field in the Agent Block reflects the compression source. **Fail:** Skill treats this as a from-scratch job and ignores the business case content, or asks unnecessary questions when the input is already rich.

---

## Audience Recalibration

This is the primary trap in this eval case. The business case was written for internal decision-making — evaluating whether to invest. The one-pager is for the **Head of Partnerships**, who needs to understand the opportunity from a partnership perspective.

**Good recalibration:** The one-pager leads with the partnership opportunity — co-investment, shared customers, co-marketing potential, early integration partner status. The $2.1M ARR overlap segment is framed as "340+ shared customers" rather than internal revenue protection. The competitive threat (FreshTrack and InventoryPro) is reframed as a market validation signal rather than a defensive posture.

**Bad recalibration:** The one-pager reads like a shortened version of the internal business case — leading with churn risk, internal ROI, and opportunity cost of engineering time. The Head of Partnerships doesn't care about internal sprint trade-offs. She cares about whether this is good for partnerships.

**Critical tests:**

**Partnership value proposition must be the lead framing.** The business case frames this as "protect our ARR." The one-pager for the Head of Partnerships should frame it as "here's a partnership opportunity with VendorHub that benefits our shared customers."

**Internal metrics should be translated to partnership language.** "23% of catalog-related support tickets" becomes "our shared customers are experiencing friction that a joint integration would solve." "6-8 weeks of engineering time" becomes "the engineering investment from our side — we want to understand if your team would co-invest."

**Competitive framing should shift from defensive to validating.** "Two competitors launched VendorHub integrations" is a threat in the business case. In the partnership one-pager, it's evidence that the market is moving toward this integration and VendorHub should want a strong partner in the space.

**Pass:** Framing centered on partnership opportunity. Internal metrics translated to partnership language. Competitive intelligence reframed as market validation. The Head of Partnerships would read this and think about her team's investment, not about our internal ROI. **Fail:** One-pager reads like a shortened internal business case. Churn protection framing survives. Internal cost model included without partnership context.

---

## Compression Fidelity

The one-pager must accurately represent the business case's argument without distorting it. Compression requires triage — choosing what survives — but the surviving content must be faithful.

**What should survive compression:**
- The core problem (manual catalog sync across 340+ customers)
- The demand signal (38% overlap, support ticket data, churn data)
- The proposed solution (bi-directional API integration with VendorHub)
- The key risk (VendorHub API timeline)
- The recommendation direction (build the integration, start with inbound sync)

**What should be cut:**
- Full impact sizing table (replace with a single magnitude signal)
- Detailed cost model (not relevant for partnership feedback)
- Alternatives analysis (the Head of Partnerships isn't choosing between options — she's giving feedback on the recommended path)
- Full stress test (premortem, blindspot check, conviction) — the confidence signal can be compressed to one sentence
- Detailed risk assessment table (compress to 2-3 key risks)

**What must NOT be distorted:**
- The recommendation must not be overstated — the business case says confidence 7/10 and names VendorHub API timeline as the main uncertainty. The one-pager must not present this as a certainty.
- The overlap segment size must not be inflated.
- The competitive situation must not be exaggerated.

**Pass:** Core argument faithfully preserved. Demand signal and recommendation direction survive. Detailed tables and analyses appropriately cut. No distortion of confidence level or data points. **Fail:** Core argument distorted (e.g., presenting the recommendation as certain when the business case flags uncertainty). Important demand signals lost. Too much detail survived (making it not a one-pager) or too much cut (making the argument unsubstantiated).

---

## Feedback Ask Type Handling

The ask is Feedback — "would her team want to co-invest?" Per the skill's conditional section logic:

| Expected Section | Should Appear? | Reason |
|-----------------|---------------|--------|
| Cost / Resource Ask | No | Not asking for budget — asking for feedback |
| Success Criteria | No | Not seeking approval |
| Impact / Sizing | No | Not a prioritization ask |
| Alternatives Considered | No | Not choosing between options |

All conditional sections should be absent. The core sections (Problem/Opportunity, Proposed Approach, Why Now, Key Risks, Next Steps) are sufficient for a feedback ask.

**However:** The one-pager should frame the feedback ask specifically — what kind of feedback is sought. Not "what do you think?" but "would your team co-invest engineering resources, and what would you need to see to make that decision?"

**Pass:** No conditional sections present. Feedback ask is specific about what feedback is sought. Next Steps section frames the follow-up conversation clearly. **Fail:** Conditional sections inappropriately included. Feedback ask is vague ("let me know your thoughts").

---

## One-Page Constraint Under Compression Pressure

This is the harder compression test. The source material is 1,200+ words with multiple tables, detailed analysis, and a full stress test. The temptation is to include too much.

**Pass:** Content is 400-600 words. The one-pager reads as a self-contained argument, not as a table of contents for the business case. No tables survive from the source (tables are too space-expensive for a one-pager). Data points are woven into prose. The reader doesn't feel like they're reading a summary — they feel like they're reading a pitch. **Fail:** Over 600 words. Tables copied from the business case. Reads like an executive summary rather than a standalone pitch. Important sections feel rushed or incomplete because too much content was kept.

---

## Open Items Quality

For compression jobs, the Open Items section should flag important nuance that didn't survive compression. This is how the PM prepares for the follow-up conversation.

**Expected open items:**
- The detailed cost model (if the Head of Partnerships asks "what's the investment from your side?")
- The alternatives analysis (if she asks "have you considered a simpler approach?")
- The VendorHub API timeline dependency (if she asks "what's the risk?")
- The competitive detail (if she asks "who else has done this?")

**Pass:** Open items list nuance the PM should be prepared to discuss. Items are specific enough to be useful in conversation prep. **Fail:** Open items absent for a compression job, or items are generic ("there's more detail in the business case").

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| Audience recalibration | 25% | Partnership framing, not internal ROI framing; metrics translated to partnership language; competitive intelligence reframed |
| Compression fidelity | 20% | Core argument preserved; no distortion; appropriate triage of what survived vs. what was cut |
| One-page constraint | 15% | 400-600 words; no surviving tables; reads as standalone pitch, not executive summary |
| Feedback ask type handling | 15% | No conditional sections; specific feedback ask; clear follow-up framing in Next Steps |
| Open items quality | 10% | Compression-specific prep items for follow-up conversation |
| Output format compliance | 15% | Agent Block populated (source_artifact reflects business case); smell test present; context note included |
