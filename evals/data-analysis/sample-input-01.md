# Data Question: Why did activation drop?

Our activation rate dropped 12% this week compared to the prior 4-week average. Can you figure out what's going on?

**Context:** "Activation" for us means a user completes their first installment plan setup within 7 days of signing up. Our baseline activation rate has been steady at ~38% for the past 2 months with ±2% weekly variance.

**This week's numbers (March 15-21):**

| Metric | This Week | 4-Week Avg | Change |
|--------|-----------|------------|--------|
| New signups | 4,280 | 4,150 | +3.1% |
| Activated (plan setup within 7 days) | 1,412 | 1,577 | -10.5% |
| Activation rate | 33.0% | 38.0% | -5.0pp (-13.2%) |

**Activation funnel this week:**

| Step | Users | Conversion | Prior 4-Week Avg Conversion |
|------|-------|------------|---------------------------|
| 1. Signup complete | 4,280 | — | — |
| 2. View plan options | 3,852 | 90.0% | 91.2% |
| 3. Select a plan | 2,782 | 72.2% | 74.0% |
| 4. Enter payment details | 1,948 | 70.0% | 71.5% |
| 5. Link bank account (if ACH) or add card | 1,584 | 81.3% | 88.2% |
| 6. Confirm and activate plan | 1,412 | 89.1% | 90.5% |

**Breakdown by platform:**

| Platform | Signups | Activation Rate | Prior 4-Week Avg |
|----------|---------|----------------|-----------------|
| iOS app | 1,820 | 37.5% | 39.1% |
| Android app | 1,290 | 36.8% | 38.5% |
| Mobile web | 1,170 | 23.8% | 36.2% |

**What else happened this week:**
- March 17: We deployed v2.4.1 which included a redesigned payment details page (step 4-5 in the funnel). The deploy touched all platforms.
- March 18: Our brand marketing campaign on Instagram ended after running for 3 weeks. The campaign drove ~400 signups/week according to the marketing team's attribution.
- March 19: Brief server outage (45 min) that affected all platforms. Resolved by 2pm ET.

**What I'm specifically wondering:** Is this the deploy? The marketing campaign ending? Something else? Should I be worried?
