# Retro Notes: Sprints Atlas-1, Atlas-2, and Atlas-3

**Request from PM:** "We're three sprints into the Kubernetes migration project. Can you synthesize the retros? I want to know what's actually improving and what's still broken."

---

## Sprint Atlas-1 Retro (February 6, 2026)

**What went well:**
- Migration of first two services (auth-service and user-service) to K8s completed ahead of schedule — wrapped on day 8 instead of day 10. Helm chart templating saved a ton of boilerplate. Priya said it made the second service migration way faster than the first.
- New deployment pipeline is noticeably faster. Team feels good about the tooling direction.

**What didn't go well:**
- Service discovery issues caused 2 production incidents this sprint. Both were DNS-related — pods couldn't resolve each other's hostnames. We spent about 3 days collectively debugging. Nobody on the team had seen this specific K8s DNS behavior before.
- On-call was brutal. Jamie got paged 11 times in one week. That's not sustainable. The incidents weren't evenly distributed — they clustered on Jamie's rotation.

**Action items:**
- [ ] **Document K8s DNS troubleshooting runbook** — Owner: Priya. Target: Before next sprint. *We can't afford to spend 3 days on this again.*
- [ ] **Review on-call rotation and load** — Owner: Marcus. Target: End of Atlas-2. *Jamie needs relief.*

---

## Sprint Atlas-2 Retro (February 20, 2026)

**What went well:**
- The DNS runbook Priya wrote last sprint actually worked! We had another DNS issue this sprint and resolved it in about 30 minutes instead of 3 days. That's a huge win. The documentation is paying off.
- Two more services migrated to K8s (billing-service, notification-service). On track with overall migration timeline.

**What didn't go well:**
- Incident response time is still too slow. We had 3 incidents this sprint and the average response time was 47 minutes. Our SLA is 30 minutes. We're not meeting it.
- On-call load is still high. Jamie and Priya were both paged 8+ times this sprint. The on-call rotation review from Atlas-1 hasn't happened yet.
- Alert volume is really noisy. The team estimates about 40% of alerts are false positives — things that fire but turn out to be nothing. This is probably contributing to the slow response times because people are getting numb to alerts.

**Action items:**
- [ ] **On-call load review** — Owner: Marcus (carryover from Atlas-1). Target: Atlas-3. *This has to actually happen this time.*
- [ ] **Alert tuning session** — Owner: Priya. Target: Mid-Atlas-3. *Goal: get false positive rate below 20%.*

---

## Sprint Atlas-3 Retro (March 6, 2026)

**What went well:**
- Alert tuning is done and it made a real difference. False positive rate dropped from ~40% down to ~12%. Team says on-call "feels way less exhausting" now. Incident volume this sprint was 1 (down from 3 last sprint).
- Three more services migrated. Over halfway through the migration.

**What didn't go well:**
- Incident response time is still slow. We only had 1 incident this sprint but our response time was 45 minutes — still above the 30-minute SLA. Fewer incidents but not faster responses. These feel like different problems now.
- The product team came to us with 3 unplanned requests mid-sprint. One was urgent (a data migration they needed for a release), one was important-but-not-urgent, and one was frankly could-have-waited. All three disrupted the team's focus. Two K8s migration stories slipped because of the interruptions.
- On-call rotation review still hasn't happened. This is the third sprint it's been on the list under Marcus.

**Action items:**
- [ ] **On-call load review** — Owner: Marcus (now 3 sprints outstanding). Target: Before Atlas-4 planning. *This is becoming a joke.*
- [ ] **Formalize intake process for product team requests** — Owner: Jamie. Target: Atlas-4. *We need a way to triage these instead of just absorbing them.*
