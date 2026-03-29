# PRD: Round-Robin Meeting Distribution

**Author:** PM, Scheduling Products
**Status:** Draft
**Last Updated:** 2026-03-22

---

## Problem Statement

Teams using shared calendars have no way to distribute inbound meeting requests fairly — one person gets overbooked while others have open slots. When a customer or prospect visits a booking page and selects a time, the booking goes to whoever is assigned to handle it, which in most setups means the first person in the rotation or the team lead by default. The result: some team members are buried in back-to-back meetings while colleagues have availability sitting unused.

This problem is especially acute for sales teams, customer success teams, and support teams that field a high volume of inbound booking requests from external visitors.

---

## Users

**Team admins** configure round-robin rules: who's in the pool, what weights to apply (equal distribution vs. priority), how to handle members who are out of office.

**External bookers** (customers, prospects, candidates) visit a booking page and select a time. They don't see the distribution logic — they just book a time and get assigned to a team member automatically.

These two groups have distinct workflows and distinct success criteria. Admins care about fair distribution and easy configuration. Bookers care about a seamless, fast booking experience.

---

## Proposed Solution

Build a round-robin meeting distribution engine that automatically routes inbound booking requests to the team member with the most availability, ensuring equitable distribution across the pool.

**Key capabilities:**

- Admins configure a round-robin pool with team members and their calendar connections
- When a booker requests a meeting, the system checks all pool members' availability and selects the next eligible member in rotation
- The booking is confirmed with the selected team member and the booker receives confirmation with that person's calendar invite
- Timezone detection automatically adjusts display of available times for the booker's local timezone
- Calendar sync works with Google Calendar and Outlook — the system reads availability from both
- Admins can set minimum buffer time between meetings per team member

---

## Success Metrics

- We want to improve booking completion rate
- Reduce time to first available slot for incoming booking requests
- Reduce manual rescheduling and rebalancing by team admins

---

## Scope

### In Scope

- Round-robin distribution logic for inbound booking requests
- Admin configuration UI for pool membership, weights, and buffer time
- Google Calendar and Outlook integration for availability reads
- Timezone detection and display conversion for bookers
- Booking confirmation with calendar invite for both booker and assigned team member
- Admin dashboard showing distribution stats (who received how many bookings)

---

## Behavior

When a user submits the booking form, the system will find the next available slot across team members and present it to the booker. The system evaluates each pool member's calendar for availability in the requested time range and selects the member with the fewest bookings assigned in the current distribution cycle. The booker is not shown which team member they're being routed to until after the slot is confirmed.

If a team member is out of office or has blocked their calendar, they are automatically skipped in the rotation. Admins receive a weekly summary email showing distribution metrics.

When an admin adds a new team member to a pool, that person is treated as starting a fresh rotation cycle so they can receive bookings immediately without waiting for others to catch up to them.

---

## Functional Requirements

1. The distribution engine must evaluate calendar availability in real time (not cached) when a booker submits a request.
2. Admins can set pool member weights — a senior rep with 1.5x weight receives 50% more bookings than a standard-weight member in the same cycle.
3. Pool configuration changes take effect immediately, not at the next cycle reset.
4. Admins can temporarily pause a pool member without removing them (e.g., for vacation coverage).

---

## Dependencies

| Dependency | Owner | Status |
|------------|-------|--------|
| Google Calendar API integration | @Platform Team — Sione Tuilagi | In progress — OAuth scopes confirmed |
| Outlook Calendar API integration | @Platform Team — Sione Tuilagi | Not started |
| Booking confirmation email templates | @Marketing — Rachel Wu | Pending design review |
| Admin dashboard component library | @Design — Farida Nasseh | Available — v2 components ready |

---

## Open Questions

1. Should bookers be able to express a preference for a specific team member, and if so, how does that interact with round-robin logic?
2. What happens if all pool members are unavailable for the booker's preferred window — do we show the next available time or return an error state?
3. Should the distribution cycle reset daily, weekly, or by total booking count?
