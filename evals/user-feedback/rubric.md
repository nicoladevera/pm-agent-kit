# Evaluation Rubric — user-feedback

**Target input:** `evals/user-feedback/sample-input-01.md`
**Skill under test:** `.claude/skills/user-feedback/SKILL.md`
**Purpose:** Determine whether `user-feedback` correctly clusters feedback by underlying need, assesses severity and frequency, distinguishes signal from noise, and produces a synthesis a PM would trust for prioritization.
**Coverage:** Single mode — full skill coverage.

---

## Expected Themes

The sample contains 22 feedback items across 3 channels with deliberate patterns. The synthesis should identify these major themes:

| # | Expected Theme | Items | Severity | Must Catch? | What good detection looks like |
|---|---------------|-------|----------|-------------|-------------------------------|
| 1 | **Autopay charges wrong payment method after update** | Tickets #4821, #4856, #4871; NPS score-3; App review ★★★☆☆ | **Blocking** — users are charged incorrectly on a financial app. 5 items across all 3 channels. | Yes | Clustered as a single theme about payment method updates not propagating to autopay. Severity assessed as Blocking (financial impact, trust violation). Cross-channel presence noted. This should be the #1 priority. |
| 2 | **Payment history / receipts not accessible** | Tickets #4847, #4911; NPS score-6, score-5; App review ★★★☆☆ | **Painful** — users can't accomplish a legitimate task (get receipts). 5 items across all 3 channels. | Yes | Clustered as a single theme about payment history discoverability, not split into "receipts" and "history" as separate themes. The underlying need is the same. |
| 3 | **App crashes / page load failures** | Tickets #4835, #4902; NPS score-2; App review ★★☆☆☆ | **Blocking** — users can't access core functionality. 4 items. | Yes | Recognized as a stability/performance theme. Note: the NPS score-2 user mentions switching to [CompetitorX], which is a churn signal worth calling out. |
| 4 | **Payment status not updating after payment** | Tickets #4889; NPS score-4 | **Painful** — user almost paid twice. Financial risk. 2 items. | Yes | Despite low frequency (2 items), this should be surfaced as a high-severity signal. Delayed status updates on a payment app create real financial risk (double payment). |

---

## Noise Items

The sample deliberately includes items that should be classified as noise or edge cases:

| Item | Why it's noise | Must Identify? |
|------|---------------|----------------|
| App review ★☆☆☆☆ ("company server was down") | **Misattributed** — this is an infrastructure complaint, not a product issue. The user is blaming the app for a server outage outside the product's control. | Yes |
| NPS score-8 ("dark mode") and App review ★★★★☆ ("dark theme") | **Personal preference / cosmetic** — 2 mentions, low severity, doesn't block any workflow. Valid feedback but not a product problem requiring urgent action. | Should note as low-priority, not as a major theme |

**Critical test:** The infrastructure complaint (★☆☆☆☆) must be flagged as misattributed. Including it in an app stability theme would be a false positive that inflates the severity assessment.

---

## High-Severity / Low-Frequency Signal

| Item | Why it matters |
|------|---------------|
| **Payment status delay** (2 items) | Despite only 2 mentions, this represents financial risk — a user almost paid twice. The synthesis should surface this in the "low-frequency, high-severity" section even though it's not the highest-frequency theme. |

**Fail:** If payment status delay is dismissed because it only has 2 mentions. Frequency alone doesn't determine priority — severity matters.

---

## Intentional Strengths in the Input

These items are positive feedback. The synthesis should not manufacture themes from them.

| Item | What it represents |
|------|-------------------|
| NPS score-9 ("easy to set up") | Positive signal about onboarding. |
| NPS score-7 ("notification reminders are helpful") | Feature working as intended. |
| NPS score-9 ("great experience setting up installments") | Core flow is strong. |
| App review ★★★★★ ("simple and works") | Core value proposition landing. |

**False positive check:** If the synthesis identifies "users want easier setup" as a theme, that's wrong — the setup experience is explicitly praised.

---

## Competitive Mentions

Two items mention [CompetitorX]:
- NPS score-2: "About to switch to [CompetitorX] — at least their app works" (churn risk, stability-driven)
- NPS score-5: "[CompetitorX] has better reporting and you can actually see your payment history" (competitive gap, feature-driven)

The synthesis should note competitive mentions and connect them to the relevant themes (stability → churn risk; payment history → competitive gap).

---

## Quality Checks

### Clustering Quality
- Autopay payment method issue: Must be one theme, not split into "card update" and "bank update"
- Payment history: Must be one theme, not split into "receipts" and "payment history"
- App crashes + page load: Should be one stability theme, not separate "crash" and "loading" themes
- Infrastructure complaint: Must NOT be folded into the app stability theme

**Pass:** 4 major themes correctly clustered. **Fail:** Over-splitting (6+ themes) or under-clustering (2 themes that merge distinct issues).

### Severity Assessment Accuracy
- Autopay wrong method: Must be assessed as **Blocking** (financial impact on a payment app)
- Payment history: Should be **Painful** (can't accomplish goal but no financial risk)
- App crashes: Should be **Blocking** (can't access core functionality)
- Payment status delay: Should be **Painful** to **Blocking** (financial risk from potential double payment)

**Pass:** Severity levels match the actual user impact described in the feedback. **Fail:** All themes rated the same severity, or the autopay issue rated below Blocking.

### Quote Selection
- Quotes should represent the typical expression of each theme
- At least some themes should have quotes from multiple channels
- No cherry-picking the most extreme or mildest expressions

**Pass:** Quotes are representative and attributed. **Fail:** Only the angriest quotes selected, or quotes all from one channel.

### Prioritization
The autopay payment method issue should be the #1 priority:
- Highest severity (Blocking — financial impact)
- Highest frequency (5 items)
- Cross-channel (all 3 sources)

**Pass:** Autopay issue ranked first. **Fail:** Payment history or crashes ranked above autopay despite lower severity.

### Channel Source Weighting

Feedback from different channels has different selection biases. Support tickets are filed by users who hit a specific problem and decided to report it — they undersample passive frustration. NPS is filed by users who received a survey — they oversample recent experience. App store reviews skew toward extreme sentiment (very happy or very frustrated).

The synthesis should note when a theme is concentrated in a single channel, because channel concentration affects confidence in the severity and frequency assessment.

**In this sample:**
- The autopay payment method issue appears across all 3 channels (tickets + NPS + app store) — cross-channel presence strengthens the signal
- Dark mode requests appear in 2 NPS responses — single-channel, low severity; appropriate to note as low-priority personal preference rather than a product problem
- App crashes appear across tickets and NPS — cross-channel, which strengthens the Blocking assessment

**Pass:** When a theme is significantly concentrated in one channel, the synthesis notes this and calibrates confidence accordingly (e.g., "5 support tickets on this theme — likely undercounts users who experienced it but didn't file a ticket"). Cross-channel themes noted as stronger signals.

**Fail:** All themes treated as equally representative regardless of channel distribution. The fact that dark mode requests only appear in NPS (self-selected survey) is not noted, despite it affecting confidence in the frequency assessment.

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| All 4 major themes identified | 25% | Correct clustering by underlying need, not surface request |
| Severity assessment accuracy | 15% | Levels match actual user impact; autopay = Blocking |
| Infrastructure complaint flagged as noise | 10% | Explicitly identified as misattributed |
| Payment status delay surfaced despite low frequency | 10% | Appears in high-severity/low-frequency section |
| Competitive mentions noted | 10% | [CompetitorX] references connected to relevant themes |
| No false positives on strengths | 5% | Positive feedback not manufactured into a theme |
| Quote selection quality | 7% | Representative, attributed, varied across channels |
| Prioritization order | 10% | Autopay issue ranked #1 |
| Channel source weighting | 5% | Cross-channel themes noted as stronger signals; single-channel themes noted with appropriate confidence caveat |
| Output format compliance | 3% | Matches declared format; context note and data quality section present |
