# Backlog Health Check — Sprint 22

Hey — sprint planning is tomorrow morning at 10am and I want to make sure we're actually ready before we walk in. Can you check if our backlog is in good shape for next sprint? Just tell me what's ready, what needs work, and what I should fix before tomorrow.

**Team:** 5 engineers, 2-week sprints. Sasha is part-time this sprint (about 80% availability) and Daniel has a 2-day conference at the start of the sprint (Monday–Tuesday of week 1), so he's at roughly 80% too. Everyone else is full.

**No carryover** from Sprint 21 — we shipped clean.

**The ask is just a health check.** I'm not asking for a sprint plan yet — I want to know what stories need work before I can use them.

---

## Backlog

| Ticket | Title | Points | AC? | Notes |
|--------|-------|--------|-----|-------|
| PR-104 | Refactor legacy webhook handler | 3 | Yes — 4 AC | Has been in backlog for 3 sprints, kept getting bumped. Team says "we'll get to it." |
| PR-108 | Build PR diff view component | 8 | Yes — 13 AC | Core feature for the diff viewer. Big one. |
| PR-109 | Add GitHub OAuth login | 3 | Yes — 5 AC | Prerequisite for GitHub integration. Clear scope. |
| PR-110 | Webhook retry logic | 2 | Yes — 4 AC | Retry + backoff for failed webhook deliveries. Straightforward. |
| PR-111 | PR comment threading UI | 3 | Yes — 6 AC | Threaded comments on PR diff. Design handoff done. |
| PR-112 | Author notification settings | 3 | No AC yet | PM hasn't written AC. Idea is clear but nothing written up. |
| PR-115 | Reviewer load balancing | 5 | No AC yet, but Dev knows what to do | Auto-assign reviewers based on workload. Marcus says he's got it in his head. |
| PR-116 | Email notification for review complete | 2 | Yes — 4 AC | Notifies PR author when review is submitted. Clean scope. |
| PR-119 | Dashboard home page | 5 | Yes — 7 AC | New main dashboard. Shows open PRs, review queue, recent activity. |

---

## Quick notes on a few stories

**PR-108 (diff view component):** This is a big story. The 13 AC cover rendering the diff, syntax highlighting, file tree navigation, inline comment anchoring, keyboard navigation between hunks, collapsed/expanded sections, handling binary files, handling large diffs (10K+ lines), mobile responsiveness, and a few edge cases. I know it's large, but we've been deferring it.

**PR-112 (author notification settings):** This is one I need to write up. The feature is clear in my head — authors should be able to control which events trigger notifications — but I haven't had time to write the AC yet. Was hoping to sneak it into this sprint.

**PR-115 (reviewer load balancing):** Marcus scoped this out and has a clear picture of the implementation. He said he doesn't need AC written up since he knows exactly what he's building. I've been taking his word for it.

**PR-119 (dashboard home page):** This one has good AC — covers what sections appear, what the empty state looks like, loading behavior, and responsive layout. We're good here I think.

**PR-104 (webhook refactor):** This has been sitting in the backlog since Sprint 19. Every sprint we say "maybe this sprint" and then it gets bumped. It's not broken, just messy code.

Looking forward to your assessment — need to know what to fix tonight before planning tomorrow.

— Reza
