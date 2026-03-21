# Retro Notes: Sprints 10, 11, and 12

**Request from PM:** "Synthesize the last three retros. I feel like we keep talking about the same things but I can't tell if anything is actually improving."

---

## Sprint 10 Retro (February 14, 2026)

**What went well:**
- Shipped the loan detail screen redesign on time
- Dev and James paired effectively on the API integration — fewer review cycles than usual
- Ana's design specs were detailed enough that implementation matched mocks perfectly

**What didn't go well:**
- Carryover from Sprint 9: the payment history feature carried over because we underestimated the complexity of the pagination logic. Ended up taking 3 extra days.
- Cross-team dependency surprise: the risk team changed the fraud detection rules mid-sprint without notifying us. Broke two of our test cases. Took a day to debug.
- Code review bottleneck: Sarah was the only reviewer for 5 PRs in the last two days of the sprint. Everything queued up.

**Action items:**
- [ ] **Reduce carryover:** Break large stories into smaller pieces before sprint planning. Owner: Maria. Target: Start in Sprint 11.
- [ ] **Cross-team communication:** Set up a shared Slack channel with the risk team for change notifications. Owner: Sarah. Target: Before Sprint 11.
- [ ] **Code review distribution:** Add Dev as a secondary reviewer to reduce Sarah's bottleneck. Owner: Sarah. Target: Sprint 11.

---

## Sprint 11 Retro (February 28, 2026)

**What went well:**
- Code review was faster this sprint! Dev reviewed 3 PRs, which took pressure off Sarah. Review turnaround went from ~2 days to ~1 day.
- The shared Slack channel with the risk team is up and running. They posted a change notification this sprint — first time we had advance warning.
- Sprint goal was clear and the team felt focused.

**What didn't go well:**
- Carryover again: PMT-180 (installment calculator) carried over because scope expanded mid-sprint when we discovered an edge case with partial prepayments. Started as a 3-point story, ended up being 5+.
- QA found 3 bugs in the last day of the sprint that should have been caught earlier. We're not doing enough testing during development.
- Sprint planning took 2.5 hours — too long. Felt like we were refining stories during planning instead of before.

**Action items:**
- [ ] **Reduce carryover:** Implement story point buffer — don't plan to 100% capacity. Owner: Maria. Target: Sprint 12.
- [ ] **Earlier testing:** Engineers write unit tests before marking stories as "in review." Owner: Dev (champion). Target: Sprint 12.
- [ ] **Shorten planning:** Refine stories in a separate session (Wednesday before planning). Owner: Maria. Target: Sprint 12.

---

## Sprint 12 Retro (March 14, 2026)

**What went well:**
- The separate refinement session on Wednesday worked great. Sprint planning was 75 minutes (down from 2.5 hours). Team felt more prepared.
- Code review speed continues to improve. Average turnaround is now ~1 day. Dev reviewing has become routine.
- No cross-team surprises this sprint. The risk team Slack channel is working.

**What didn't go well:**
- Carryover: PMT-195 (payment confirmation flow) carried over. This time it was blocked — design wasn't finalized until day 4 of the sprint, so engineering only had 6 days instead of 10.
- Still finding bugs late in the sprint. James found a critical bug in the payment flow on day 9. The "unit tests before review" commitment from Sprint 11 hasn't been consistently followed — Dev estimates maybe 60% compliance.
- Estimation still feels off. Two stories were significantly underestimated this sprint. We're not accounting for integration complexity.

**Action items:**
- [ ] **Reduce carryover:** Design must be finalized before sprint start — no stories enter the sprint without design sign-off. Owner: Maria + Ana. Target: Sprint 13.
- [ ] **Testing compliance:** Add a checklist item to the PR template requiring test evidence. Owner: Sarah. Target: Sprint 13.
- [ ] **Better estimation:** Try planning poker or relative sizing for complex stories. Owner: Maria. Target: Sprint 13.

---

## Previous Action Item Status (as reported informally)

From Sprint 10 action items:
- "Break large stories into smaller pieces" — Maria says she's been doing this but the team still encounters scope expansion mid-sprint
- "Shared Slack channel with risk team" — Done. Working well.
- "Add Dev as secondary reviewer" — Done. Working well.

From Sprint 11 action items:
- "Story point buffer" — Maria planned to 85% capacity in Sprint 12. Unclear if it helped — still had carryover.
- "Unit tests before review" — Partially adopted (~60% compliance per Dev's estimate)
- "Separate refinement session" — Done. Working well. Planning time cut significantly.

From Sprint 12 action items:
- Not yet assessed (Sprint 13 hasn't completed).
