# Discovery Methods

What makes a discovery plan rigorous and useful for product decisions. Use this to identify assumptions, rank them by risk, select appropriate research methods, and define what "good enough" evidence looks like before committing to a solution. The pre-evidence counterpart to `user-feedback-analysis.md` — that file covers how to synthesize feedback that already exists; this file covers how to plan the research that generates it.

Discovery planning is not research execution. A discovery plan identifies what you don't know, what it would cost to be wrong, and the cheapest credible way to reduce uncertainty. "Let's do some user interviews" is not a plan. "We need to validate whether enterprise users actually experience onboarding friction before committing to a redesign — 6-8 interviews segmented by company size, looking for workflow breakdowns in the first 14 days" is a plan.

---

## Assumption Mapping

### What Counts as an Assumption

An assumption is anything the team believes to be true that hasn't been validated with direct evidence. Assumptions hide in problem statements, user stories, business cases, and casual conversation. They're most dangerous when they're invisible — treated as facts when they're actually guesses.

Every initiative rests on a stack of assumptions. The job of discovery is to find the load-bearing ones and test them before the stack collapses.

### Assumption Taxonomy

| Type | What it covers | Example |
|------|---------------|---------|
| **User assumptions** | Who the user is, what they need, how they behave, what they value | "Enterprise users churn because onboarding is too complex" |
| **Problem assumptions** | Whether the problem exists, how severe it is, who it affects, whether it's growing | "Support ticket volume for cancellations is increasing quarter over quarter" |
| **Solution assumptions** | Whether the proposed approach will solve the problem, whether users will adopt it, whether it's technically feasible | "A self-service flow will capture 70% of cancellation requests" |
| **Viability assumptions** | Whether the business can sustain the solution — unit economics, regulatory constraints, operational capacity | "The cost of building and maintaining self-service is less than the support cost it displaces" |

### Extraction

To surface assumptions from an initiative or problem area:

1. **State the current belief** — what does the team think is true about the problem, user, solution, and business model?
2. **Ask "how do we know?"** — for each belief, is the evidence direct observation, inferred from adjacent data, or assumed without evidence?
3. **Distinguish facts from assumptions** — facts have evidence. Assumptions don't. If the answer to "how do we know?" is "it seems obvious" or "everyone agrees," it's an assumption.
4. **Check for hidden assumptions** — assumptions embedded in the framing itself. "We need to improve onboarding" assumes onboarding is the problem. "Enterprise users need X" assumes enterprise users are a coherent segment with shared needs.

**Red flag:** An assumption map with fewer than 5 assumptions for a non-trivial initiative. Either the team hasn't looked hard enough, or they're treating assumptions as facts.

---

## Risk Ranking

### Cost-of-Being-Wrong Framework

Not all assumptions are equally dangerous. Rank by the cost of being wrong, not by how uncertain you feel.

| Dimension | Question |
|-----------|----------|
| **Consequence** | If this assumption is wrong, what happens? Does the initiative fail? Does it underperform? Or does it just need adjustment? |
| **Reversibility** | If we proceed on this assumption and it's wrong, can we course-correct cheaply? Or are we locked in? |
| **Dependency** | Do other assumptions depend on this one? If this is wrong, does the whole chain collapse? |
| **Current confidence** | How much evidence do we actually have? Strong signal, weak signal, or none? |

### Prioritization Matrix

| | High consequence | Low consequence |
|---|---|---|
| **Low confidence** | Test first — this is where discovery earns its keep | Test if cheap — or accept the risk and monitor |
| **High confidence** | Verify — high stakes warrant confirmation even when you're fairly sure | Skip — the risk doesn't justify the research cost |

Assumptions in the high-consequence / low-confidence quadrant are the discovery plan's priority. Everything else is secondary.

**Red flag:** A discovery plan that tests easy assumptions while ignoring hard ones. Validating what you already believe is comfortable but useless.

---

## Method Menu

Select the method that fits the assumption type, the evidence strength needed, and the constraints. No method is universally best — the right choice depends on what you're trying to learn.

| Method | Best for | Evidence strength | Cost / Time | When to avoid |
|--------|----------|-------------------|-------------|---------------|
| **User interviews** | Understanding motivations, workflows, pain points, mental models. Discovering problems you didn't know existed. | Qualitative — rich but not generalizable from small samples | Low-medium cost. 1-3 weeks for recruiting + sessions. | When you need quantitative validation. When the question is "how many?" not "why?" |
| **Surveys** | Validating frequency, severity, or preference across a population. Quantifying qualitative findings. | Quantitative — generalizable if sample is representative | Low cost. 1-2 weeks for design + collection. | When you don't yet know what questions to ask. When the population is too small for statistical significance. |
| **Prototype tests** | Testing whether a proposed solution is usable, understandable, and solves the problem | Behavioral — what users do, not what they say | Medium cost. 2-4 weeks for prototype + testing. | When the problem itself hasn't been validated yet. Testing solutions before problems is the most common discovery mistake. |
| **Concierge tests** | Testing whether a workflow delivers value before building it. Manual delivery of the promised experience. | Behavioral + value signal. Strong for viability. | Low build cost, high operational cost. 2-6 weeks. | When the workflow can't be manually simulated. When scale matters for the test. |
| **A/B experiments** | Testing whether a specific change causes a measurable outcome difference in production | Causal — the gold standard for "does X cause Y?" | Medium-high cost. Requires existing traffic, instrumentation, and statistical rigor. 2-6 weeks runtime. | When sample size is insufficient for statistical power. When the change can't be isolated. When the risk of a bad variant is too high. |
| **Diary studies** | Understanding behavior over time. Habits, routines, workarounds, longitudinal experience. | Qualitative — rich longitudinal context | Medium cost. 1-4 weeks of participant journaling. | When you need quick answers. When the behavior doesn't vary over time. |
| **Data mining** | Discovering patterns in existing behavioral or operational data. Validating whether a problem exists at the scale claimed. | Quantitative — based on actual behavior, not self-report | Low cost if data infrastructure exists. Days to weeks depending on query complexity. | When the data doesn't exist or is unreliable. When the question is "why?" not "what?" or "how many?" |
| **Competitive proxy analysis** | Inferring market viability or user expectations from competitors' choices | Inferential — suggestive but not conclusive | Low cost. Days. | When competitors serve a fundamentally different segment. When you need direct evidence, not inference. |
| **Concept tests** | Testing whether a value proposition resonates before building anything. Landing pages, mockups, pitch decks shown to target users. | Attitudinal — what users say they'd want (weaker than behavioral) | Low cost. 1-2 weeks. | When the concept is too abstract to evaluate. When stated preference diverges from actual behavior (which is often). |
| **Wizard of Oz tests** | Testing a full experience where the user believes the product works but a human is behind the scenes | Behavioral — strong. Users interact with what they think is the real product. | Medium cost. High operational overhead during the test. 2-4 weeks. | When the experience can't be faked convincingly. When the human behind the curtain can't replicate the proposed behavior. |

### Method Selection Logic

1. **Start with the assumption type.** User and problem assumptions often need qualitative methods first (interviews, diary studies). Solution assumptions need behavioral methods (prototype tests, A/B). Viability assumptions need quantitative or operational methods (data mining, concierge tests).
2. **Match evidence strength to stakes.** High-consequence assumptions need stronger evidence. A decision to invest $2M in a platform rewrite requires more than 5 interviews. A decision to tweak onboarding copy does not require an A/B test with 10,000 users.
3. **Sequence qualitative before quantitative.** Interviews surface the right questions. Surveys validate the answers at scale. Running a survey before you know what to ask produces precisely measured nonsense.
4. **Check constraints.** No existing users? Can't do A/B tests or data mining. No budget for recruiting? Can't do formal interviews. Small market? Can't get statistical significance from surveys. Constraints narrow the menu — name them explicitly.

---

## Evidence Thresholds

### What "Good Enough" Looks Like

Not every assumption needs the same level of proof. The threshold depends on the cost of being wrong and the cost of gathering more evidence.

| Evidence level | When it's sufficient | Example |
|----------------|---------------------|---------|
| **Directional signal** (3-5 interviews showing a consistent pattern) | Low-stakes assumptions. Early-stage exploration. When you need to decide "is this worth investigating further?" not "should we commit?" | 4 of 5 enterprise users describe the same onboarding confusion — enough to justify deeper research, not enough to justify a redesign |
| **Convergent qualitative** (8-12 interviews with saturation — new interviews stop surfacing new themes) | Medium-stakes assumptions. Problem validation. Understanding user mental models and workflows. | After 10 interviews, the same 3 pain points recur and no new themes emerge — problem is validated qualitatively |
| **Quantitative validation** (survey or behavioral data with statistical significance) | High-stakes assumptions. Sizing claims. Arguments that need to convince skeptical stakeholders. | Survey of 200 users confirms that 68% (±5%) experience the pain point identified in interviews — ready for a business case |
| **Causal evidence** (controlled experiment with measurable outcome) | Highest-stakes assumptions. Solution effectiveness claims. "Will this change actually cause the outcome we predict?" | A/B test shows the new onboarding flow increases 14-day retention by 8pp (p < 0.05) — solution validated |

### Stopping Rules

- **Qualitative research:** Stop when new sessions stop surfacing new themes (saturation). For most product research, this happens between 8-12 participants per segment. If themes are still diverging after 12 sessions, either the segment definition is wrong or the problem space is broader than expected.
- **Quantitative research:** Define the minimum detectable effect and required confidence level before starting. If you need to detect a 5% conversion improvement with 95% confidence, calculate the sample size first — don't just "run the experiment for two weeks."
- **All methods:** Define success and failure criteria before starting. "What result would make us proceed?" and "What result would make us stop?" If you can't answer both, the research plan is incomplete.

**Red flag:** Research that runs until it finds the answer the team wants. Moving goalposts on sample size. "Let's do a few more interviews" when the data already has a clear answer the team doesn't like.

---

## Research Operations

### Participant Counts

These are guidelines, not rules. Adjust for segment complexity and research maturity.

| Method | Typical range | Notes |
|--------|---------------|-------|
| **Generative interviews** | 8-12 per segment | Saturation-based. More segments = more participants, not more per segment. |
| **Usability tests** | 5-8 per round | Nielsen's research shows 5 users find ~85% of usability issues. Multiple rounds beat larger samples. |
| **Surveys** | 100-300 for directional; 300+ for segmented analysis | Depends on the number of segments and the precision needed. Use a sample size calculator for significance requirements. |
| **Diary studies** | 8-15 participants | Dropout is common. Recruit 20-30% more than you need. |
| **A/B experiments** | Calculate per-experiment | Depends entirely on baseline rate, minimum detectable effect, and traffic. Use a power calculator. |

### Recruiting

- **Screener quality matters more than speed.** A bad screener produces participants who don't represent the target user, which produces misleading data. Invest time in the screener.
- **Internal users are not proxies for external users** unless they genuinely match the target segment. Dog-fooding provides useful signal but introduces bias — internal users have context that external users don't.
- **Incentive appropriateness.** Under-incentivizing produces no-shows and low engagement. Over-incentivizing attracts participants motivated by the incentive, not by genuine product use.
- **Diversity of perspective.** Within the target segment, recruit for variation — different company sizes, usage patterns, tenure, technical sophistication. Homogeneous samples produce homogeneous insights.

### Bias Awareness

| Bias | What it is | How to mitigate |
|------|-----------|----------------|
| **Confirmation bias** | Interpreting findings as supporting existing beliefs | Pre-register hypotheses. Have someone outside the project review findings. |
| **Leading questions** | Questions that suggest the desired answer | Review interview guides for neutral framing. "Tell me about your experience with X" not "Don't you find X frustrating?" |
| **Survivorship bias** | Only studying current users, ignoring churned users or non-adopters | Actively recruit churned users or prospects who didn't convert. They often have the most useful feedback. |
| **Selection bias** | Participants who volunteer are systematically different from those who don't | Acknowledge the limitation. Triangulate with behavioral data when possible. |
| **Social desirability** | Participants say what they think you want to hear | Ask about behavior, not opinions. "Walk me through what you did" not "Do you think this is useful?" |

---

## Red Flags

Anti-patterns that indicate a discovery plan needs more work:

- **Defaulting to interviews for everything.** Interviews are powerful for "why" questions but weak for "how many" questions. If the assumption is about frequency or scale, interviews alone won't validate it.
- **Testing solutions before validating problems.** Building a prototype to test before confirming the problem exists is the most expensive form of confirmation bias. Validate the problem first.
- **"We already know" as a reason to skip discovery.** If you already know, show the evidence. If the evidence is "everyone agrees," that's a belief, not knowledge.
- **Confirmation bias in study design.** Research designed to prove a hypothesis rather than test it. Leading questions, cherry-picked participants, post-hoc reframing of results.
- **No stopping criteria.** Research without pre-defined success/failure criteria will run until it produces the desired answer or the team loses patience — neither is a good outcome.
- **Studying the wrong segment.** Internal users, power users, or whoever's easiest to recruit — rather than the users the assumption is actually about.
- **One method for everything.** Different assumption types need different methods. A plan that uses only interviews or only surveys hasn't matched method to question.
- **No connection to the decision.** Discovery that isn't tied to a specific decision or initiative produces interesting findings that sit in a deck and change nothing. Every research activity should name the decision it informs.

---

## Using These Standards

**For discovery planning (`discovery-plan` skill):** Map assumptions from the problem space or initiative. Rank by cost-of-being-wrong. Select methods from the menu with explicit rationale. Define evidence thresholds and stopping criteria before starting. Sequence by dependency and information value.

**For interpreting discovery results in other skills:** When discovery findings appear as input to other skills — as evidence in a business case, as validation in a PRD, as signal in a competitive analysis — apply these standards to assess the evidence quality. Five interviews with a consistent theme is directional signal, not proof. An A/B test with insufficient sample size is noise, not causal evidence. Name the evidence level when citing discovery results.

**For connecting discovery to downstream work:** Discovery plan outputs (validated/invalidated assumptions, evidence collected) feed directly into `prd-draft` (the validated problem becomes the PRD's foundation), `business-case` (the evidence grounds impact sizing and risk assessment), and `roadmap-prioritization` (evidence quality per initiative informs sequencing decisions). A discovery plan that doesn't name what decisions it informs hasn't finished the planning.
