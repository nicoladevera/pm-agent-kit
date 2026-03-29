# PRD: Automated Appointment Reminder System

**Author:** PM Lead, Patient Engagement
**Status:** Approved
**Last Updated:** 2026-03-20

---

## Problem Statement

Medical practices using HealthSchedule (our B2B scheduling platform) see a 15-20% patient no-show rate. Each missed appointment costs the practice approximately $150 in lost revenue — the slot could have been filled by another patient but wasn't, and staff time was allocated. Across our 400+ practice clients, this represents tens of millions in lost revenue annually.

Practices currently rely on front desk staff to call patients 1-2 days before appointments. This is inconsistent — staff often skip reminder calls during busy periods — and doesn't scale. Practices with 50+ appointments per day cannot reliably staff manual reminder calls.

The solution is an automated reminder system that sends SMS and email reminders without requiring any staff action, and allows patients to confirm, reschedule, or cancel via reply so the practice has real-time confirmation status before the appointment day.

---

## Success Metrics

| Metric | Baseline | Target | Timeframe | Data Source |
|--------|----------|--------|-----------|-------------|
| No-show rate across active practices | 17% average | 10% (7pp reduction) | 3 months post-launch | Appointment outcome events |
| Reminder confirmation rate | N/A (new) | 65% of sent reminders receive a response (C/R/X) | 1 month post-launch | reminder_confirmed + reminder_rescheduled + reminder_cancelled events |
| Practice opt-in rate for reminder feature | N/A (new) | 70% of eligible practices enable reminders within 90 days | 90 days post-launch | Feature flag activation per practice |

---

## Proposed Solution

Automated SMS and email reminders sent at configurable intervals before each scheduled appointment. Patients respond via text (C to confirm, R to request reschedule, X to cancel). Practice staff see real-time confirmation status in the scheduling dashboard. Practices configure reminder timing and message templates through the admin portal.

### User Flows

**Practice Admin (Configuration):**
1. Admin navigates to Settings > Reminders
2. Admin enables the reminder feature for the practice
3. Admin sets reminder timing: one or more of 48h, 24h, 2h before appointment
4. Admin customizes message template for each reminder (or uses default)
5. Admin saves configuration — reminders will be sent automatically for all future appointments

**Patient (Receiving Reminders):**
1. Patient receives SMS and/or email reminder at configured times
2. Reminder includes: appointment date, time, provider name, practice name, and response instructions
3. Patient replies C to confirm, R to request reschedule, X to cancel
4. Patient receives a confirmation reply acknowledging their response
5. If patient replies anything else, they receive a "We didn't understand your response" message and the instructions again

**Practice Staff (Dashboard):**
1. Staff opens the scheduling dashboard
2. Each appointment row now shows reminder status: Pending, Confirmed, Reschedule Requested, Cancelled, No Response
3. Staff can filter by status to identify patients who haven't responded before the appointment

---

## Scope

### In Scope
- Automated SMS via Twilio API
- Automated email via SendGrid API
- Configurable reminder timing: 48h, 24h, and/or 2h before appointment (practice chooses which intervals to enable)
- Patient reply parsing: C (confirm), R (reschedule request), X (cancel)
- Automated acknowledgment reply to patient upon response
- HIPAA-compliant opt-out: patients can reply STOP to opt out permanently; opt-out must be logged and permanently honored
- Practice admin configuration UI in Settings > Reminders
- Confirmation status column in scheduling dashboard
- 5 analytics events (listed in Data Requirements)

### Out of Scope
- Automated rescheduling (staff must manually reschedule when R is received — this release only captures the request)
- Multi-language support (English only in v1)
- Push notification reminders (app-based)
- Patient-initiated appointment booking via text
- Voice call reminders

---

## User Segments

**Practice Admin:** Configures reminder settings. Needs a simple interface to set timing and templates. Typically performs this setup once and rarely changes it. Does not interact with individual reminders.

**Patient:** Receives reminders on their mobile device or email. May be any age or technical skill level. Response must be as simple as possible — single-character reply.

**Practice Staff (Front Desk / Schedulers):** Views confirmation status for upcoming appointments in the dashboard. Needs to identify which patients haven't confirmed so they can follow up manually if desired.

---

## Acceptance Criteria

Practices can enable automated reminders through Settings > Reminders in the admin portal. The configuration screen allows admins to select which reminder intervals to activate (48h, 24h, 2h) with at least one required, and to customize the SMS and email message templates for each active interval. Default templates are provided. Changes take effect immediately for appointments not yet within an active reminder window.

Reminders are sent automatically at the configured times before each appointment. SMS is delivered via Twilio to the patient's phone number on file. Email is delivered via SendGrid to the patient's email address on file. If both are on file, both channels are used. If only one is available, only that channel is used. Reminders include the appointment date, time, provider name, and practice name.

When a patient replies C (case-insensitive), the appointment status updates to "Confirmed" in the dashboard. The patient receives an automated acknowledgment: "Got it — your appointment is confirmed. See you then." When a patient replies R, the status updates to "Reschedule Requested" and the patient receives: "We've received your reschedule request. Our office will follow up to find a new time." When a patient replies X, the status updates to "Cancelled" and the patient receives: "Your appointment has been cancelled. Please call us to reschedule."

A patient who replies STOP must be immediately opted out of all future SMS reminders from this practice. The opt-out is permanent — it persists if the patient's record is updated or if they book new appointments. Email reminders are not affected by SMS opt-out; patients must unsubscribe from email separately. Opt-out events must be logged with patient ID, practice ID, timestamp, and the channel (SMS).

The scheduling dashboard shows a Reminder Status column for each appointment displaying one of: Pending (no reminders sent yet), Sent (reminder sent, no response), Confirmed, Reschedule Requested, Cancelled, or Opted Out. Staff can filter the appointment list by reminder status.

---

## Data Requirements

The following events must be instrumented:

| Event Name | Trigger | Payload |
|------------|---------|---------|
| `reminder_sent` | Reminder delivered to patient via SMS or email | `patient_id`, `practice_id`, `appointment_id`, `channel: 'sms' \| 'email'`, `hours_before: 48 \| 24 \| 2`, `template_id` |
| `reminder_confirmed` | Patient replies C | `patient_id`, `practice_id`, `appointment_id`, `channel`, `response_delay_minutes: integer` |
| `reminder_rescheduled` | Patient replies R | `patient_id`, `practice_id`, `appointment_id`, `channel`, `response_delay_minutes: integer` |
| `reminder_cancelled` | Patient replies X | `patient_id`, `practice_id`, `appointment_id`, `channel`, `response_delay_minutes: integer` |
| `opt_out_received` | Patient replies STOP | `patient_id`, `practice_id`, `channel: 'sms'`, `opted_out_at: ISO-8601 timestamp` |

Dashboard requirements: per-practice no-show rate trend (30-day rolling), reminder response rate by channel, opt-out rate by practice, reminder delivery failure rate by Twilio/SendGrid error code.

---

## Technical Notes

- **SMS delivery:** Twilio Programmable Messaging API. Inbound reply webhooks must be configured to route responses to our parser.
- **Email delivery:** SendGrid Transactional Email API. Unsubscribe links in every email must route to our opt-out logging endpoint.
- **Appointment data source:** Existing appointment DB schema — `appointments` table. Reminder scheduler reads from this table. No schema changes required for appointment data.
- **Opt-out storage:** New `patient_opt_outs` table. Fields: `patient_id`, `practice_id`, `channel`, `opted_out_at`, `opted_in_at` (nullable, for future opt-back-in). This table must be checked before every outbound reminder.

---

## Open Questions

1. **Opt-out scope:** Should an SMS opt-out from Practice A also apply to Practice B if the patient is a patient at both practices? Current assumption is per-practice, but HIPAA counsel has not reviewed this specific scenario. This affects the `patient_opt_outs` table schema (include `practice_id` or not).

2. **SMS delivery failure handling:** What should happen when Twilio returns a delivery failure error (e.g., invalid number, carrier rejection)? Options: (a) log and move on, (b) fall back to email-only for that reminder, (c) flag the appointment in the dashboard. The current spec does not define this behavior.
