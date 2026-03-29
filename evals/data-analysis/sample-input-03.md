# Data Question: Why do customers from different acquisition sources retain so differently?

Our retention looks really different depending on how a customer first found us. Can you help me understand what's actually going on? I'm trying to figure out where to put our CAC budget.

**Context:** We're a two-sided home services marketplace — customers book jobs (cleaning, handyman, lawn care, etc.) and professionals provide them. We operate in 14 US metro areas. "Retention" for us means booking at least one job in a given time window after first booking. We track it at D1, D7, D30, and D90 from a customer's first completed booking.

**The data:**

| Source | N (cohort size) | D1 | D7 | D30 | D90 | Avg. jobs booked by D90 | Avg. order value |
|--------|----------------|-----|-----|-----|-----|------------------------|-----------------|
| Paid Social (Facebook/Instagram) | 3,200 | 52% | 38% | 19% | 8% | 1.3 | $95 |
| Organic Search (Google) | 1,800 | 48% | 35% | 28% | 18% | 2.1 | $120 |
| Referral (customer referral program) | 620 | 61% | 52% | 41% | 31% | 3.4 | $130 |

Cohort window: all customers who made their first booking in Q4 of last year. D1/D7/D30/D90 are measured from their first booking date.

**Current spend breakdown:**
- Paid social: ~$45,000/month (our biggest channel)
- Organic search: Not a direct spend — traffic comes from our SEO blog and content. Marginal cost is low.
- Referral: ~$20 credit per referral given to the referring customer. Cost scales with referral volume.

**What I know about the channels:**
- Paid social targeting has been optimized for early conversions — specifically, for users who complete a first booking. That's what our acquisition dashboard tracks and what we've been optimizing our Meta campaigns toward.
- Organic search we mostly don't control directly — customers find us through how-to content and service area landing pages.
- The referral program gives existing customers $20 off their next booking when a friend completes their first booking.

**What feels off:** We've been optimizing our paid social targeting for first bookings because that's what our dashboard tracks. But when I look at the D30/D90 numbers, something doesn't add up. Paid social looks decent in week 1 and then falls off a cliff. I don't fully understand why, but it feels like we might be optimizing for the wrong thing.

**What I'm asking:** Walk me through what this retention data actually means and how it should inform where we invest our CAC budget going forward. I have a marketing budget review in two weeks and need a clear recommendation.
