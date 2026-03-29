# Feature: Patient Intake Form Digitization

**What I need:** I need to map out the full launch path for our patient intake form feature before I commit to a timeline for the executive team. What does the journey look like, stage by stage?

We're heading into a quarterly planning cycle and the CEO wants a realistic GA date on the roadmap. I'm not going to give her a date until I understand what's actually standing between us and GA — the compliance overhead, the EHR integrations, the IT approval cycles at our hospital clients. I need the full map before I can estimate anything.

**What's shipping:**

This feature replaces paper intake forms at hospital check-in kiosks and via the patient portal. When a patient arrives for an appointment, instead of filling out a paper form at the front desk, they complete the form digitally — either on a check-in kiosk in the lobby or on their personal device via a portal link sent before the visit.

The form collects:
- Insurance information (carrier, policy number, group ID)
- Demographic data (name, DOB, address, emergency contact)
- Medical history and current medications (free-text and structured fields)
- Consent signatures (for treatment, for data sharing, for HIPAA acknowledgment)

**EHR integrations:**
We integrate with three EHR systems to write the intake data back to the patient record:
- **Epic** — our largest client segment. Epic integration took 6 months to build. It's live in our test environment.
- **Cerner** — our second-largest segment. Integration is designed but not yet built.
- **Legacy custom system** — one specific client (our largest by revenue) runs a homegrown EHR. We've done a technical scoping call but haven't started the build.

**Who it affects:**
- Hospital admin staff at check-in desks (primary users)
- Patients completing forms via portal link or kiosk (secondary users)
- Hospital IT departments (they control the infrastructure where our software runs)
- Our support team (will handle setup, troubleshooting, and escalations)

**Current state:**
The feature works end-to-end in our test environment using the Epic integration. We've validated the core flow with internal team members playing the role of admin and patient. We have not run this on real patient data in a production environment.

**My specific concerns going into this planning conversation:**

1. **Real patient data in testing.** We can't expose real patient data in early testing — we need to work with synthetic data or fake patient accounts. I need to understand when in the journey we're working with synthetic data and when we cross over to real PHI.

2. **Hospital IT approval cycles.** Our hospital clients have long IT approval processes — security reviews, vendor assessments, sign-off from hospital leadership. That runway needs to be in the plan, not discovered three months before our target GA.

3. **EHR integration sequencing.** Epic alone took 6 months to build and certify. Cerner and the legacy system are unknowns. I don't know yet if we can run a single Beta or if we need separate tracks by EHR. That uncertainty is going to affect my timeline estimate significantly.

This is a B2B feature — our customers are hospital systems, not individual consumers. Every pilot requires a signed contract, a business associate agreement, and IT approval at the hospital. This is not a feature I can roll out to 1% of users via a feature flag.

I'm not asking for a checklist for a specific launch stage. I need the full map from where we are today to GA, so I can walk into the executive planning session with a realistic picture of the road ahead.
