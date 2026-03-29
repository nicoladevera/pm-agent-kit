# Delivery State Assessment — Seller Onboarding Flow, Sprint 8

Hey — we're mid-sprint, day 6 of 10, and I want to understand where we actually stand before the team sync this afternoon. Can you assess our delivery state for the seller onboarding flow? Not writing anything up for stakeholders — just need an honest read on where we are.

---

## Sprint Goals

1. Ship a functional seller onboarding flow through background check submission
2. Have provider profiles visible in the marketplace by end of sprint

---

## Sprint Board State (Day 6 of 10)

| Ticket | Title | Status | Assignee | Notes |
|--------|-------|--------|----------|-------|
| SEL-201 | Onboarding entry screen and routing logic | Done | Marcus | Shipped day 2 |
| SEL-202 | Service category selection UI | Done | Priya | Shipped day 3 |
| SEL-203 | Availability and rate setting form | Done | Takoda | Shipped day 4 |
| SEL-204 | Background check consent form | Done | Marcus | Shipped — consent copy in English, legal sign-off pending on final copy |
| SEL-205 | Checkr integration — submit background check | In Review | Marcus | PR open, waiting for review sign-off |
| SEL-206 | Profile completion UI — photo and bio | Not Started | Priya | — |
| SEL-207 | Profile completion UI — service details | Not Started | Priya | — |
| SEL-208 | Marketplace profile card component | Not Started | Takoda | Depends on SEL-206 and SEL-207 being complete |
| SEL-209 | Provider profile page | Not Started | Takoda | Depends on SEL-208 |
| SEL-210 | Onboarding completion screen + confirmation email | Not Started | Marcus | — |
| SEL-211 | Admin tool — flag incomplete profiles | Not Started | Dev (shared services) | — |
| SEL-212 | Error handling for Checkr submission failures | Not Started | Marcus | Depends on SEL-205 |
| SEL-213 | Analytics events for onboarding funnel | Not Started | Takoda | — |
| SEL-214 | QA smoke test pass — full onboarding flow | Not Started | QA | Depends on SEL-201 through SEL-210 |

**Summary:** 4 done, 1 in review, 9 not started. 10 days total, 6 elapsed.

---

## Blockers and Notes

**Blocker — Legal review delayed:** The background check consent form (SEL-204) is technically "done" in the sense that the engineering work is complete, but legal hasn't signed off on the final consent copy yet. Their team has been heads-down on a compliance audit for another product line and pushed our review. Marcus is holding off on finalizing the consent flow story and doing integration testing until he gets that sign-off — he doesn't want to wire up the production Checkr integration against a consent form that might change. Legal said they'd get back to us "by end of next week" in an email on Monday.

**Team availability — Priya:** Priya has been out sick since Tuesday (day 4). She called in Wednesday morning and again Thursday — she's dealing with something and isn't sure when she'll be back. SEL-206 and SEL-207 are both assigned to her and haven't been touched since she went out.

**Checkr API dependency:** We're integrating with Checkr for background checks. I pinged their solutions engineer last week for confirmation on the API spec — specifically the required fields for the consent object and whether their sandbox environment mirrors production behavior. Haven't heard back yet. Marcus said he thinks we're fine with what we have from the initial docs, but he wants to confirm before writing tests for SEL-212. He's been going on the assumption that the docs are current.

**Downstream dependency — next sprint:** SEL-206 and SEL-207 (Priya's profile completion stories) are prerequisites for SEL-208 (marketplace profile card), which is the foundation for the marketplace visibility work we have lined up for Sprint 9. If those two stories slip, Sprint 9's first week is blocked.

---

## Previous Sprint

Sprint 7 delivered the seller registration and authentication flow. We shipped on goal. No carryover.
