# Evaluation Rubric — generate-tasks (Healthcare SaaS: Appointment Reminder)

**Target input:** `evals/generate-tasks/sample-input-02.md`
**Skill under test:** `skills/generate-tasks/SKILL.md`
**Purpose:** Determine whether `generate-tasks` correctly decomposes a healthcare SaaS PRD into well-scoped stories, separates HIPAA-critical opt-out handling into its own story, creates a dedicated data story, and flags the unresolved SMS failure handling as needing PM input.

**Coverage:** Single mode — full skill coverage.

---

## Story Decomposition

The sample PRD describes an automated appointment reminder system with three distinct user flows and several components that should resolve into separate stories.

### Expected Stories

The exact decomposition may vary, but the output should cover these natural boundaries:

| Area | Should be separate? | Why |
|------|---------------------|-----|
| Reminder configuration UI (admin portal — Settings > Reminders) | Yes | Different user (admin), different interface, different flow from sending reminders |
| Reminder sending engine (SMS via Twilio + email via SendGrid) | Yes | Core functionality; integrates with external APIs; can be built and tested independently |
| Patient reply parsing and status updates (C/R/X) | Could be separate or bundled with sending engine | Either is valid if well-scoped — bundling is acceptable if AC count stays under 8-10 |
| Opt-out handling (STOP reply, logging, HIPAA compliance) | Yes — must be separate | HIPAA-critical; requires specific logging AC; different compliance concern than reminder sending |
| Staff dashboard — reminder status column + filtering | Yes | Different user (staff), different interface, different interaction pattern |
| Data/analytics story (5 events + dashboard) | Yes — mandatory | Per story-structure.md, data stories must be separate from feature stories |

**Pass:** Stories cover all functionality. Opt-out is its own story. Data story is separate. Each story is a deployable unit.
**Fail:** Opt-out handling buried inside the reminder sending story. No data story. Configuration UI and sending engine merged into one mega-story.

### Decomposition Quality

- **No mega-stories** — If any story has more than 8-10 AC, it should be flagged for splitting
- **Natural boundaries** — Stories split along user flows (admin vs. patient vs. staff), not arbitrary lines
- **HIPAA-critical work isolated** — Opt-out is its own story because it carries compliance obligations that deserve dedicated AC, dedicated review, and dedicated testing

---

## Opt-Out Story Specificity

The opt-out story is HIPAA-relevant and must not be treated as a minor edge case bundled into the reminder sending story. Its AC must be specific enough for a coding agent to implement the compliance behavior correctly.

**Pass:** The opt-out story includes AC that cover all of the following:
- Patient replies STOP and is opted out immediately (not on next reminder cycle)
- `opt_out_received` event logged with `patient_id`, `practice_id`, `channel: 'sms'`, and `opted_out_at` ISO-8601 timestamp
- Opt-out persists — new appointment bookings for the same patient do not reset the opt-out
- `patient_opt_outs` table checked before every outbound SMS reminder
- Patient receives a confirmation SMS upon opt-out: "You have been unsubscribed from appointment reminders from [practice name]. Reply START to resubscribe."
- Email reminders are not blocked by an SMS opt-out (separate channels)

**Fail:** AC says "patient can opt out" without specifying permanent logging, the opt_out_received event, or the check-before-send behavior. Opt-out AC appear as the last two items in the reminder sending story.

---

## Data Story Completeness

Per `references/story-structure.md`, analytics instrumentation should be its own story, not buried in feature stories.

**Pass:** Data story covers all 5 events from the PRD with exact field names and types as specified:
- `reminder_sent`: patient_id, practice_id, appointment_id, channel, hours_before, template_id
- `reminder_confirmed`: patient_id, practice_id, appointment_id, channel, response_delay_minutes
- `reminder_rescheduled`: patient_id, practice_id, appointment_id, channel, response_delay_minutes
- `reminder_cancelled`: patient_id, practice_id, appointment_id, channel, response_delay_minutes
- `opt_out_received`: patient_id, practice_id, channel, opted_out_at

Dashboard requirements captured as part of the data story (per-practice no-show rate trend, reminder response rate by channel, opt-out rate, delivery failure rate).

**Fail:** Events mentioned in passing but no field-level specification. Dashboard omitted. Data story merged with a feature story as final AC items.

---

## Open Questions Preserved

The PRD has 2 open questions that require PM or legal input. The decomposition must not silently resolve them.

**Pass:** Both open questions surfaced in the Flagged Items section:
1. Opt-out scope (per-practice vs. platform-wide) — flagged with note that this affects the `patient_opt_outs` table schema and must be resolved before the opt-out story can be finalized
2. SMS delivery failure behavior — flagged with the three options from the PRD and a note that the opt-out story and reminder sending story both have unresolved AC until this is answered

Decomposition notes where the answer to each question affects AC in specific stories.

**Fail:** Open questions disappear from the output. Decomposition makes an assumption (e.g., opts for per-practice without flagging it, or silently chooses "log and move on" for SMS failures).

---

## AC Format and Quality

Apply `references/acceptance-criteria.md` standards to every AC in every story.

| Check | What to verify |
|-------|----------------|
| **Given/When/Then format** | Every AC uses the structured format |
| **Specificity** | No subjective language. Exact behaviors named. Response codes (C/R/X) explicitly referenced. |
| **Boundary conditions** | What happens if neither SMS nor email is on file? What if the appointment is within the reminder window when practice enables the feature? |
| **Error states as separate AC** | Twilio failure, SendGrid failure, and unrecognized reply (not C/R/X) each have their own AC |
| **Data contracts** | Event names and payloads match what the PRD specifies exactly |
| **Testable** | Each AC could be translated into an automated test |

**Pass:** All AC meet acceptance-criteria.md standards. Error states are their own AC, not embedded in happy-path AC. Unrecognized reply behavior specified separately.
**Fail:** Prose descriptions in AC. Error states implied but not stated. Unrecognized reply handling missing.

---

## Implementation Sequence

- Foundation stories first: `patient_opt_outs` table schema must be agreed upon before the opt-out story can be finalized (depends on open question resolution)
- Reminder sending engine can be built in parallel with configuration UI
- Dashboard story depends on reminder status data flowing correctly from the sending engine
- Data story can be built alongside feature stories once event names are agreed

**Pass:** A team could follow the sequence without getting blocked. Dependency on opt-out scope resolution is called out explicitly.
**Fail:** No sequence provided. Dashboard story scheduled before the reminder status data model is defined.

---

## Scoring

| Dimension | Weight | Pass Criteria |
|-----------|--------|---------------|
| Stories cover all functionality, natural boundaries identified | 20% | All PRD functionality covered. Opt-out is separate. Dashboard is separate. Data story is separate. Each story is a deployable unit. |
| Opt-out as separate story with HIPAA-specific AC | 20% | Opt-out story present. AC covers: immediate opt-out, event logged with full payload, persistence across new bookings, check-before-send, email channel not affected. |
| Data story separated with all 5 event field specifications | 15% | All 5 events present with exact fields as specified in PRD. Dashboard requirements captured. |
| Open questions preserved and flagged with story impact | 15% | Both open questions in Flagged Items. Each flags which stories are affected and which AC are incomplete. |
| AC in Given/When/Then, error states as separate AC | 20% | Every AC uses G/W/T. Error states (Twilio failure, unrecognized reply) are separate AC, not embedded. |
| Implementation sequence logical, open question dependency visible | 10% | Sequence present. Opt-out schema dependency on open question resolution is explicit. |
