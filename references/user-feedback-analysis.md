# Feedback Analysis Standards

What makes a feedback synthesis useful for product decisions. Use this to cluster customer feedback into themes, assess severity and frequency, distinguish signal from noise, and connect feedback to product work. The analytical counterpart to `communication-quality.md` — that file covers how to communicate findings; this file covers how to find what's worth communicating.

Feedback synthesis is not summarization. Summarizing feedback restates what customers said. Synthesizing feedback identifies what customers need — which is often different from what they asked for. "Users want dark mode" is a summary. "Users are experiencing eye strain during extended evening sessions" is a synthesis that opens up a broader solution space.

---

## Clustering Standards

### Cluster by Need, Not by Request

Group feedback by the underlying problem or need, not by the surface feature request. Multiple different requests often point to the same underlying issue.

**Good clustering:**
- "Can't find the payment history" + "Where do I see past transactions?" + "I need a receipt for my last payment" → **Theme: Payment history is not discoverable**
- "Add dark mode" + "The app is too bright at night" + "I get headaches using this" → **Theme: Visual comfort during extended or nighttime use**

**Bad clustering:**
- Grouping by exact feature request ("dark mode requests," "receipt requests") — this misses the shared underlying need
- Grouping by channel ("support ticket themes," "NPS themes") — channel is metadata, not a clustering dimension

### What Makes a Valid Theme

A theme is valid when it meets three criteria:
1. **Minimum frequency:** At least 2-3 distinct feedback items converge on the same underlying issue. A single report is an observation, not a theme.
2. **Internal coherence:** The items grouped under a theme genuinely relate to the same underlying need. If you have to stretch to explain why they're connected, they're not a theme.
3. **Distinctness:** The theme is meaningfully different from other themes. If two themes overlap substantially, merge them or sharpen the distinction.

**Red flag:** A "theme" with only one data point. Themes so broad they capture everything ("users want the product to be better"). Themes that are really just categories ("billing issues" — what specifically about billing?).

---

## Severity Assessment

### Four Levels, Two Dimensions

Assess each theme on two dimensions: **user impact** and **scope**.

**User impact** (how badly it hurts):
| Level | Definition | Signal |
|-------|------------|--------|
| **Blocking** | Users cannot accomplish their goal. They are stuck or forced to find a workaround. | "I can't do X," "This is broken," "I had to call support to get this done" |
| **Painful** | Users can accomplish their goal but the experience is frustrating, slow, or error-prone. | "This is really frustrating," "It took me forever to figure out," "I almost gave up" |
| **Annoying** | Users notice the issue and it degrades the experience, but it doesn't materially affect their ability to get things done. | "This is kind of annoying," "It would be nice if," "Minor thing but" |
| **Cosmetic** | The issue is noticed but has negligible impact on the user's experience or success. | Polish issues, visual inconsistencies, minor copy errors |

**Scope** (how many users it affects):
| Level | Definition |
|-------|------------|
| **Widespread** | Affects most or all users in a segment. Shows up across multiple channels. |
| **Moderate** | Affects a meaningful subset of users. Shows up in multiple reports but not everywhere. |
| **Isolated** | Affects a small number of users or a very specific use case. |

**Priority signal:** Blocking + Widespread is urgent. Cosmetic + Isolated is noise. Everything in between requires judgment — and that judgment should be explicit in the output.

---

## Trend Assessment

### Direction Matters as Much as Magnitude

When a prior feedback synthesis exists, compare themes across time periods:

| Trend | Definition | What it signals |
|-------|------------|----------------|
| **Growing** | Theme frequency or severity is increasing compared to the prior period | Problem is getting worse or affecting more users. Prioritization urgency increases. |
| **Stable** | Theme frequency and severity are roughly consistent | Known issue. Still worth addressing but not escalating. |
| **Declining** | Theme frequency or severity is decreasing | Problem may be resolving (through fixes, workarounds, or users leaving). Verify before deprioritizing. |
| **New** | Theme did not appear in the prior period | Could be a regression, a new user segment discovering the product, or a real emerging issue. Warrants investigation. |

**Red flag:** Treating a declining trend as resolved without verifying why it declined. A theme can decline because the problem was fixed — or because frustrated users churned.

---

## Signal vs. Noise

### Not All Feedback Deserves Equal Weight

Some feedback is strong product signal. Some is noise. Distinguishing them requires understanding who is saying what and why.

**Likely signal:**
- The same issue reported by multiple users across different channels
- Feedback from users in the core ICP (ideal customer profile)
- Issues that connect to product metrics (churn, activation, conversion)
- Feedback that correlates with usage patterns (users who hit the issue churn at higher rates)

**Likely noise:**
- Single reports of edge-case issues
- Requests from users well outside the target segment
- Feedback that reflects personal preference rather than a product problem ("I prefer blue buttons")
- Misattributed issues (infrastructure outage reported as a product bug, third-party integration failures blamed on the product)

**Nuance:** Low-frequency, high-severity feedback is signal even if it's rare. A single report of data loss matters more than 50 reports of a visual glitch. Frequency alone does not determine importance — frequency × severity does.

---

## Source Channel Weighting

### Every Channel Has a Bias

Different feedback channels surface different types of issues from different user segments. Acknowledge this when synthesizing.

| Channel | What it captures well | Known bias |
|---------|----------------------|------------|
| **Support tickets** | Blocking issues, specific bugs, workflow failures | Skews toward users who hit problems. Over-represents power users and users with high stakes. Under-represents users who quietly churn. |
| **NPS / satisfaction surveys** | Overall sentiment, experience-level feedback | Skews toward extremes (very satisfied or very dissatisfied). Timing-dependent — captures the user's state at survey time, not their full experience. |
| **App store reviews** | First impressions, onboarding issues, core value proposition feedback | Skews toward new users and recent updates. Ratings are sticky — a bad first experience stays in reviews long after a fix. |
| **User interviews** | Deep qualitative signal, workflow context, unmet needs | Small sample. Interviewer bias possible. Users may rationalize or describe aspirational behavior. |
| **Sales feedback** | Pre-purchase objections, competitive comparisons, feature gaps | Skews toward prospects (not current users). Reflects what prospects say they want, which may differ from what they'd actually use. |
| **Slack / community** | Real-time frustrations, feature enthusiasm, workarounds | Self-selecting — only vocal users participate. Skews toward engaged power users. |

**Red flag:** Drawing strong conclusions from a single channel. Treating NPS verbatims as representative of all users. Ignoring source bias when prioritizing themes.

---

## Quote Selection

### Representative, Not Dramatic

Select 2-3 quotes per theme that illustrate the theme clearly. Quotes should be:

- **Representative:** The quote captures the typical expression of this theme, not the most extreme or the most mild
- **Illustrative:** Reading the quote, you understand the theme without additional explanation
- **Attributed:** Include the source channel (and date if available) so the reader can assess the context
- **Varied:** If possible, select quotes from different channels or user segments to show breadth

**Red flag:** Cherry-picking the most dramatic quote to amplify urgency. Selecting only mild quotes to minimize severity. All quotes from the same channel or user type.

---

## Connecting Feedback to Product Work

### Themes Should Land Somewhere

When product context is available, connect each theme to existing work:

- **Existing backlog item:** "This aligns with PMT-234, which has been in the backlog for 3 sprints"
- **Active PRD or project:** "This reinforces the problem statement in the Onboarding Redesign PRD"
- **Known gap:** "We've known about this gap since Q1 but haven't prioritized it"
- **New signal:** "This theme doesn't map to any current work — it may represent an unrecognized need"

The goal is to help the PM translate themes into action — not just "here's what users said" but "here's what this means for what we're building."

---

## Using These Standards

**For feedback synthesis (`user-feedback` skill):** Cluster feedback by underlying need. Assess severity and frequency for each theme. Distinguish signal from noise. Select representative quotes. Connect to product work when context is available. Prioritize by impact (frequency × severity × trend).

**For interpreting feedback in other skills:** When customer feedback appears as input to other skills (e.g., as context for a PRD, as signal in a status update), apply these standards to assess its weight. A single NPS comment is not the same as a cross-channel theme.
