# Evaluation Rubric — data-analysis

**Target input:** `evals/data-analysis/sample-input-01.md`
**Skill under test:** `.claude/skills/data-analysis/SKILL.md`
**Purpose:** Determine whether `data-analysis` correctly identifies the root cause of an activation drop by analyzing funnel data, segmenting by platform, evaluating competing hypotheses, and stating confidence appropriately.

## Coverage

**This rubric tests:** Anomaly investigation with funnel analysis as the primary method.
**Not covered here:** Metric interpretation (`rubric-metric.md`), Cohort analysis (`rubric-cohort.md`).

---

## Analysis Type Classification

The input asks "why did activation drop?" with funnel data showing a week-over-week decline. This should be classified as an **anomaly investigation** (unexpected metric change) with **funnel analysis** as the primary analytical method.

**Pass:** Classified as anomaly investigation or funnel analysis (either is acceptable). **Fail:** Classified as cohort analysis or metric interpretation without recognizing the funnel structure.

---

## Key Finding

The data contains a clear signal: the activation drop is **concentrated in mobile web** (23.8% vs 36.2% baseline — a 12.4pp drop) while iOS and Android show only minor declines (1.6pp and 1.7pp respectively). The biggest funnel drop is at **step 5 (link bank account / add card)** where conversion fell from 88.2% to 81.3% — a 6.9pp drop, by far the largest deterioration in the funnel.

The v2.4.1 deploy on March 17 redesigned the payment details page (steps 4-5), and the mobile web platform shows the most severe impact. The most likely explanation is that **the deploy introduced a regression in the payment/bank-linking flow on mobile web**.

**Must identify:**
- Mobile web is the outlier platform (12.4pp drop vs ~1.6pp for native apps)
- Step 5 (bank linking / card entry) is the biggest funnel deterioration
- The v2.4.1 deploy is the most likely cause

**Pass:** Key finding connects the mobile web platform drop + step 5 funnel drop + deploy timing. **Fail:** Key finding doesn't segment by platform, or attributes the drop to the marketing campaign ending.

---

## Hypothesis Evaluation

The input deliberately provides three competing explanations. The analysis should evaluate all three:

| # | Hypothesis | Correct Assessment | Why |
|---|-----------|-------------------|-----|
| 1 | **v2.4.1 deploy (payment page redesign)** | **Most likely** (High) | Timing matches (March 17). The redesigned pages are steps 4-5, exactly where the funnel drops. Mobile web is most affected, which is consistent with a responsive design regression that doesn't affect native apps as severely. |
| 2 | **Marketing campaign ended** | **Red herring** (Low) | The campaign drove ~400 signups/week. This week's signups actually *increased* by 3.1% (130 more than average). If the campaign ending reduced traffic, you'd expect fewer signups, not more. Also, campaign-sourced users might have lower activation rates, so losing them should *improve* the activation rate, not worsen it. |
| 3 | **Server outage (March 19)** | **Minor contributor at most** (Low) | 45 minutes on March 19 could explain a small number of lost activations across all platforms, but can't explain the sustained mobile web drop or the magnitude of the funnel deterioration at step 5. The outage affected all platforms equally, but the drop is concentrated in mobile web. |

### Critical test: Marketing campaign as red herring
The marketing campaign ending is the most tempting wrong answer. The analysis **must** reason about it carefully and conclude it's unlikely:
- Signups didn't decrease (they increased)
- Campaign-attributed signups ending would remove lower-quality traffic, which should improve activation rate
- The drop is platform-specific (mobile web), not traffic-source-specific

**Pass:** All three hypotheses evaluated. Deploy ranked highest. Marketing campaign debunked with reasoning. **Fail:** Marketing campaign ranked as primary or co-primary cause. Or server outage given equal weight to the deploy.

---

## Funnel Analysis Quality

The analysis should walk through the funnel data meaningfully:

| Check | What to look for |
|-------|-----------------|
| Step-by-step conversion analysis | Each step's conversion compared to baseline, with the magnitude of change noted |
| Biggest drop identified | Step 5 (81.3% vs 88.2% = -6.9pp) is the single biggest deterioration |
| Absolute vs percentage | The analysis should note that step 5's 6.9pp drop accounts for the majority of the activation loss |
| Upstream effects noted | Steps 2-4 also show small declines (1-2pp each), which compound but aren't individually dramatic |
| Platform segmentation connected to funnel | The mobile web activation rate (23.8% vs 36.2%) implies the step 5 problem is much worse on mobile web specifically |

**Pass:** Funnel analysis identifies step 5 as the critical point and connects it to the mobile web platform data. **Fail:** Funnel analyzed in aggregate only, without noting that mobile web drives the majority of the drop.

---

## Confidence and Limitations

### Confidence calibration
The finding (deploy caused a mobile web regression at step 5) should be stated at **medium-to-high confidence**:
- Strong evidence: timing, platform concentration, funnel step correlation
- Caveat: we only have one week of post-deploy data; the effect should be confirmed with a few more days

**Fail:** High confidence stated without any caveats. Or low confidence despite strong convergent evidence.

### Limitations that should be named
- Only one week of post-deploy data — the pattern should be confirmed with additional days
- No pre/post deploy segmentation within the week (we don't know if the drop started exactly on March 17)
- Mobile web's step 5 conversion isn't broken out separately in the funnel data — the analysis infers it from the platform-level activation rate
- We don't have a control group (no A/B test on the deploy)

**Pass:** At least 2-3 meaningful limitations named. **Fail:** No limitations section, or limitations are trivially generic.

---

## Recommended Next Steps

The analysis should recommend actionable next steps:

| Priority | Recommendation | Why |
|----------|---------------|-----|
| 1 | Check mobile web specifically on the payment/bank-linking page | The platform data points here; manual QA or session recordings would confirm |
| 2 | Pull daily activation rates by platform for the week to see if the drop aligns with the March 17 deploy date | This would strengthen/weaken the deploy hypothesis |
| 3 | Consider rolling back or hotfixing the mobile web payment flow if the regression is confirmed | The activation impact is significant (12.4pp drop on mobile web) |
| 4 | Don't attribute to marketing campaign without further evidence | The data doesn't support it |

**Pass:** At least 2 actionable next steps that would confirm or rule out the deploy hypothesis. **Fail:** Generic recommendations ("investigate further") without specifying what to investigate.

---

## Reproducibility and Verification

Numeric `data-analysis` runs are incomplete unless they produce a verified replay bundle. For this case, the output should be saved under a run folder in `knowledge/data-analyses/` and include:
- `report.md`
- `analysis.py`
- `calc-log.jsonl`
- `manifest.yaml`
- `verification.json`
- at least one chart file
- `replay/` with regenerated chart and derived outputs

The report should cite key numeric claims with `[calc:...]` references, and `verification.json` should show `status: Passed`.

**Pass:** The run folder exists, required reproducibility artifacts are present, key numeric claims are calc-cited, and replay verification passed. **Fail:** Flat-file output only; missing code, manifest, calc log, or verification artifact; or verification status is not `Passed`.

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| Mobile web identified as outlier | 17% | Platform segmentation performed; mobile web's 12.4pp drop highlighted |
| Step 5 identified as critical funnel point | 13% | Step 5's 6.9pp drop identified as the biggest deterioration |
| Deploy ranked as most likely cause | 13% | v2.4.1 deploy connected to steps 4-5 redesign and mobile web concentration |
| Marketing campaign debunked | 12% | Reasoning explains why the campaign ending doesn't explain the data |
| Confidence appropriately calibrated | 10% | Medium-to-high, with caveats about single week of data |
| Limitations stated | 10% | At least 2-3 meaningful limitations named |
| Next steps are actionable | 10% | Specific investigations recommended (not generic "look into it") |
| Reproducibility and replay verification | 10% | Run folder includes required bundle artifacts and `verification.json` shows `Passed` |
| Output format compliance | 5% | Matches declared format; context note present; Visualizations section present with run-folder chart paths, calc citations, and reproducibility section |
