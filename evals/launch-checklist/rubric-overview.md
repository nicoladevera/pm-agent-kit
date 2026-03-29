# Evaluation Rubric — launch-checklist (Overview Mode)

**Target input:** `evals/launch-checklist/sample-input-02.md`
**Skill under test:** `skills/launch-checklist/SKILL.md`
**Purpose:** Determine whether `launch-checklist` Overview mode produces a complete multi-stage launch journey (Internal → Alpha → Beta → GA), with per-stage requirements, compliance dimensions at every stage, accurate exit criteria, and red flags surfaced for the high-risk elements in this scenario.

## Coverage

**This rubric tests:** Overview mode — full multi-stage launch journey map for a Healthcare B2B SaaS feature.
**Not covered here:** Checklist mode (operational checklist for a specific launch stage) — see `rubric.md`.

---

## Mode Detection

The PM asks for "the full launch path" and "stage by stage" — she explicitly states she is not asking for a checklist for a specific stage. This framing must trigger Overview mode, not Checklist mode.

**Pass:** Produces a multi-stage journey map (Internal → Alpha → Beta → GA) with per-stage details, aligned with the Overview output format in the skill.
**Fail:** Produces a single-stage checklist (e.g., a Beta checklist only) or asks for clarification about which stage to generate a checklist for when the input clearly requests the full journey.

---

## All 4 Stages Present with Per-Stage Detail

Each stage should include: audience and scale, feature capability requirements, internal readiness requirements across all dimensions, and exit criteria. This is a B2B enterprise product — audience descriptions must reflect hospital clients as units, not individual end users.

| Stage | Expected audience/scale | Key feature gate | Critical readiness requirement |
|-------|------------------------|-----------------|-------------------------------|
| Internal | Hospital employees acting as test users + synthetic/fake patient data, 5–10 people, 1–2 weeks | Core form flow works end-to-end; Epic integration validates in sandbox | EHR sandbox connection confirmed; synthetic patient data pipeline established; no real PHI |
| Alpha | 1–2 pilot hospital clients (contracted), selected admin staff, controlled real PHI under signed BAA | Full Epic integration live in production; consent capture works; form writes to patient record | HIPAA BAA signed with each pilot client; IT approval received at pilot site; real-data incident response plan in place |
| Beta | 5–10 hospital clients, broader admin + patient portal users, multiple EHR environments | All 3 EHR integrations (Epic, Cerner, legacy) working; patient-facing portal flow complete; kiosk and portal tested | Support trained on HIPAA incidents; monitoring for PHI exposure events; rollback without data loss; Cerner and legacy integrations certified |
| GA | All contracted clients, all users across all EHR environments | Feature complete across all documented use cases; performance validated at scale; all EHR certifications complete | Full compliance audit complete; all EHR certifications; support fully enabled; rollback tested |

**Pass:** All 4 stages present with audience/scale description, feature gate requirements, and per-stage readiness details covering key dimensions.
**Fail:** Fewer than 4 stages, or stages present as headings only without per-stage content, or stages without exit criteria defined.

---

## HIPAA/Compliance Dimension at Every Stage

This is the highest-stakes dimension for healthcare B2B. HIPAA is not a GA checklist item — it must appear at every stage, with requirements calibrated to the risk and scope of that stage. An overview that treats HIPAA as a final-step certification has fundamentally misread the compliance posture of healthcare software.

**What to look for per stage:**

| Stage | Minimum HIPAA/compliance requirement |
|-------|-------------------------------------|
| Internal | Explicit statement that no real PHI is used; synthetic data pipeline or test accounts specified; internal team HIPAA training confirmed |
| Alpha | HIPAA BAA signed with each pilot client before real data is accessed; PHI authorization documented; real-data incident response plan ready; limited data scope |
| Beta | Compliance audit underway (not deferred to GA); breach response tested; monitoring for PHI exposure live; support trained on HIPAA incident handling |
| GA | Full compliance certification; BAAs in place for all clients; audit complete; ongoing compliance posture documented |

**Pass:** HIPAA compliance dimension is explicitly addressed at Internal (synthetic data requirement), Alpha (BAA and PHI authorization), Beta (audit in progress, breach response tested), and GA (full certification).
**Fail:** HIPAA only mentioned at GA as a final step; framed as a one-time certification rather than a continuous thread; Internal or Alpha stages treated as HIPAA-exempt.

---

## EHR Integration as a Red Flag and Critical Path Item

The PM identified EHR integration as the highest-risk item in this launch — Epic alone took 6 months, and Cerner and the legacy system are unscoped. The Overview must treat EHR integration not as a checklist item but as the primary timeline driver, with explicit implications for stage gating.

The "3 EHRs, potentially 3 timelines" insight is the highest-value observation the Overview can make. If EHR integrations require separate Alpha/Beta tracks or explicit sequencing by EHR, naming this saves the PM from discovering it in the executive planning session.

**Pass:**
- EHR integration named as the critical path item for Alpha/Beta/GA transitions
- The structural observation surfaced: 3 separate EHR integrations (Epic, Cerner, legacy) may require separate alpha/beta validation tracks or explicit sequencing (e.g., Epic-only Alpha, then multi-EHR Beta)
- IT approval cycle risk named: hospital IT approval typically runs 3–6 months, meaning Beta client recruitment must begin significantly before the target Beta start date
- Cerner and legacy integration timelines flagged as open unknowns that must be scoped before a GA date can be committed

**Fail:** EHR integration listed as a dependency item but not called out as the primary timeline driver; "3 EHRs = potentially 3 timelines" insight absent; IT approval cycle not connected to stage planning.

---

## Exit Criteria Specificity

Stage transitions are gates, not suggestions. Each exit criterion should be measurable. For criteria where the PM must supply the threshold, mark them explicitly as "PM to define before this stage begins" rather than leaving the threshold blank or inventing a number.

Healthcare-specific criteria (HIPAA incidents, form completion under real conditions, EHR write success rates) should appear alongside standard criteria from the reference.

**Pass:** Exit criteria include quantitative thresholds where deterministic (e.g., "0 HIPAA incidents during Internal," "0 P0/P1 bugs"), and mark variable thresholds as "PM to define" (e.g., "form completion rate ≥ [X]% on synthetic data — PM to define before Internal begins," "minimum [X] admin staff feedback sessions completed — PM to define before Alpha begins"). At least one healthcare-specific criterion appears at each transition.

**Fail:** Exit criteria are qualitative only ("when the team feels confident"), absent entirely, or have thresholds invented without PM input.

---

## Synthetic Data Requirement for Internal Stage

The PM explicitly called out: "We can't expose real patient data in early testing — we need to work with synthetic data or fake patients." The Internal stage must directly address this, including how synthetic data gets set up — not just stating the requirement but providing enough detail that the PM knows what to put on her pre-Internal task list.

**Pass:** Internal stage explicitly requires synthetic patient data (no real PHI permitted); includes at least one concrete implementation note (e.g., synthetic data pipeline, fake patient accounts seeded in the test environment, de-identified data from a compliant source); notes the gate condition for crossing from synthetic to real PHI (signed BAA + IT approval at Alpha).

**Fail:** Internal stage does not address data type; assumes real patient data is acceptable for testing; acknowledges synthetic data without specifying how to achieve it.

---

## Recommended Entry Point

The skill's Overview mode requires a recommended entry point based on current feature context. The input states the feature works end-to-end in the test environment with Epic, validated by internal team members with synthetic data. This maps to late Internal stage or Internal exit readiness — the feature has cleared the basic internal validation bar and is approaching readiness for Alpha.

**Pass:** Recommends Internal (specifically: confirms the feature has met or nearly met Internal exit criteria and should move to Alpha preparation) with a clear rationale tied to the input context. Flags the open items that must be resolved before Alpha can begin (synthetic data setup confirmed, BAA templates ready, Epic production readiness, IT approval runway initiated at target pilot clients).

**Fail:** Recommends skipping Internal (feature isn't ready for Alpha until PHI authorization and BAA are in place); or recommends starting over at Internal without acknowledging the validation already completed.

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| Mode detection (Overview, not Checklist) | 10% | Multi-stage journey map produced; not a single-stage checklist |
| All 4 stages with per-stage audience/scale/requirements | 20% | All stages present with feature gates, readiness details, and exit criteria |
| HIPAA compliance dimension present at every stage | 20% | Explicitly addressed at Internal, Alpha, Beta, and GA — not just GA |
| EHR integration flagged as critical path with timeline implications | 20% | Named as primary timeline driver; 3-EHR sequencing insight surfaced; IT approval cycle addressed |
| Exit criteria specific with quantitative thresholds or "PM to define" markers | 15% | Measurable criteria at each transition; unset thresholds marked for PM |
| Synthetic data requirement addressed in Internal stage | 10% | Internal stage requires synthetic PHI with implementation notes |
| Output format compliance | 5% | Matches Overview mode format from skill; context note present |
