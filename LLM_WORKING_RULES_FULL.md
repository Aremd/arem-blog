# LLM Working Rules — Full

## Purpose

Produce changes that are not only functionally correct, but also right in rendering and intention, structurally clean, maintainable, easy to explain, elegant in solution design, and evolvable over time.

A solution that “works” but degrades the codebase, introduces avoidable complexity, or weakens the delivery chain is not acceptable.

---

## Core operating principle

Do not execute on the apparent simplicity of a request.

First classify the task correctly.
Then choose the right mode of work.
Then implement the smallest clean intervention.
Then validate it with the smallest credible safety net.
If relevant, qualify its place in the delivery chain as well.

---

## Mandatory qualification filter

Before any code, design, UI, template, workflow, asset, or content-structure change, answer these questions briefly.

### 1) Real object of change
What is actually being changed?
- content
- local style
- component
- template
- rendering logic
- routing
- configuration
- asset pipeline
- branding integration
- generation script
- workflow / CI / deploy logic
- metadata / social sharing
- other

### 2) Systems touched
Which systems are involved?
- one isolated system
- multiple interacting systems

Typical multi-system combinations:
- theme + branding
- template + CSS
- content + metadata
- asset generation + social sharing
- dark/light mode + iconography
- local rendering + platform-specific behavior
- source code + build output + deployment chain

### 3) Entry point certainty
Is the intended entry point:
- proven
- or only plausible?

Do not implement from a plausible entry point as if it were confirmed.

### 4) Exact system or similar case
Is this the exact mechanism in use, or only something that looks familiar?

Do not rely on a neighboring pattern or prior resemblance.
Confirm the actual system in this project.

### 5) Stop / requalification threshold
What concrete signal will trigger a stop and reclassification instead of further patching?

Examples:
- the second correction does not clearly improve the result
- rendering and technical behavior diverge
- the fix starts spreading across unrelated files
- the “simple” change requires several special cases
- the rationale for the entry point becomes hard to explain
- local success depends on increasingly fragile exceptions

### 6) Success criteria
What does success mean here across:
- function
- rendering
- architecture
- maintainability
- elegance
- future extensibility

A task is not successful just because it technically works.

### 7) Minimal validation / testing / delivery requirement
What is the smallest runtime-efficient validation layer — and, if relevant, the smallest staged delivery-chain validation — that gives meaningful confidence for the critical behavior touched by this change?

Possible answers:
- no extra validation needed
- manual local validation is enough
- targeted unit test
- minimal integration test
- smoke test for a critical path
- build validation
- artifact validation
- pre-deploy smoke test
- post-deploy live smoke test

Do not add more validation by reflex.
Do not skip validation when regression risk is real.

---

## Decision rule

### Execute directly only if
- one system is touched
- the entry point is proven
- the change is local and reversible
- success criteria are clear
- validation is straightforward
- there is no hidden delivery-chain implication

### Map first if
- several systems interact
- the entry point is only a hypothesis
- branding, templates, theme logic, responsive behavior, dark/light mode, generation scripts, metadata, workflows, or external platform behavior are involved
- a local fix may create side effects
- the clean solution is not yet clearly formulable
- the change may affect build output, artifact generation, or deployment behavior

### Stop and requalify if
- two iterations do not clearly improve the result
- technical correctness and visual/intended correctness diverge
- the solution starts spreading without a clear center
- new fixes are compensating for a weak initial hypothesis
- the change becomes harder to explain than the original problem
- delivery or validation logic starts becoming more complex than the change itself

---

## Intervention method

### 1. Map the existing system before acting
Identify:
- the real files in use
- the real partials, wrappers, hooks, templates, classes, workflows, and pipelines
- the actual source of truth for the behavior being changed

Never assume the obvious file or selector is the real driver.

### 2. Identify the winning rule
Find the correct level of intervention:
- content
- config
- template
- style layer
- component layer
- asset layer
- generation layer
- workflow / delivery layer

Do not solve a structural problem with decorative overrides.

### 3. Intervene at one legitimate point
Prefer the most central correct entry point.

A good intervention should feel:
- local
- justified
- reversible
- easy to reason about

### 4. Centralize refinements when appropriate
Use the project’s extension layer instead of modifying core/theme/vendor sources unless structural necessity makes that unavoidable.

Centralize:
- style refinements in the proper style layer
- generation refinements in the existing generator
- workflow changes in the actual delivery chain
- metadata rules in the real metadata source of truth

### 5. Keep code explainable
Every change should remain:
- easy to read
- easy to justify
- easy to modify later

Prefer short, explicit blocks over clever or scattered fixes.

### 6. Keep scope tight
One problem = one scope = one coherent intervention.

Avoid patch chains.

### 7. Validate locally first
Distinguish clearly between:
- local behavior
- production behavior
- cache/platform behavior
- external service behavior
- workflow/build behavior

Do not conclude too early from the wrong environment.

### 8. Clean before finishing
Leave no:
- temporary files
- backup files
- abandoned experiments
- dead CSS
- redundant special-case logic
- orphaned assets
- unnecessary workflow branches

---

## Success criteria

A change is successful only if the relevant criteria below are satisfied.

### Function
The intended behavior works.

### Rendering
The visible result is correct, legible, proportionate, and faithful to the intended outcome.

### Architecture
The solution acts at the right level and does not create an unnecessary side system.

### Maintainability
Another contributor can quickly understand, explain, and modify the change.

### Elegance
The solution is proportionate, sober, and avoids unnecessary complexity.

### Evolvability
The solution can be adapted later without forcing redesign of the area.

### Validability
The change can be checked through a minimal but credible validation mechanism.

### Delivery fit
If relevant, the change is correctly placed in the build/deploy chain, with no unnecessary delivery complexity or avoidable workflow/tooling debt.

---

## Minimal testing rule

For every non-trivial change, determine the smallest runtime-efficient validation layer that gives meaningful confidence on the critical behavior being touched.

Do not optimize for broad test quantity.
Optimize for fast, high-value protection of critical paths.

Before implementing, answer:
1. Is a critical path affected?
2. What regression risk is introduced?
3. What is the smallest credible validation mechanism?
4. Is manual validation enough, or do we need targeted automation?
5. Why is this level sufficient and proportionate?

### Testing principles
- No extra tests for purely cosmetic, truly local, low-risk changes
- Targeted tests for behavior that is critical, reusable, or regression-prone
- Prefer a few fast tests with high signal over wide but slow, low-value coverage
- If a change affects generation, metadata, routing, rendering logic, repeated UI behavior, or external integration, explicitly assess test value before proceeding

---

## Delivery-chain qualification

For any non-trivial change, determine whether the impact is limited to source behavior or extends into the delivery chain.

Ask:
1. Is the change local, or does it affect build, artifact generation, deployment, or live-served behavior?
2. Do we need scope detection before running broader validation?
3. What is the smallest staged validation chain that gives meaningful confidence?
   - source-only validation
   - build validation
   - artifact validation
   - pre-deploy smoke test
   - post-deploy live smoke test
4. What artifacts are produced, transformed, or shipped by this change?
5. Does this change touch workflow/tooling areas that require CI/CD maintenance checks?

Do not route every change through the same heavy path.
Prefer scope-aware, staged validation.

A change is not fully successful if it is correct in code but badly placed in the delivery chain, weakly validated for its risk level, or introduces avoidable workflow/tooling debt.

---

## Artifact awareness rule

If a change touches generation, build, export, or deploy packaging, identify:
- what artifact is produced
- what artifact is intermediate
- what artifact is the actual deliverable
- what consumes each artifact downstream

Do not modify a generation or delivery chain without understanding what is being produced and why.

---

## CI/CD maintenance awareness rule

If a task touches workflows, actions, runners, deployment logic, or build tooling, assess not only whether the chain works now, but also whether it introduces or preserves avoidable maintenance debt.

Check for:
- deprecated actions or runtimes
- fragile workflow branching
- unnecessary artifact handoffs
- redundant stages
- validation stages that are too weak or too heavy for the risk level

A delivery chain that passes while silently aging into breakage is not healthy.

---

## Forbidden mistakes

Do not:
- implement before minimal mapping
- classify by surface simplicity instead of real dependencies
- rely on a similar case instead of the exact mechanism in use
- stack overrides to save a weak hypothesis
- confuse “it displays” with “it is successful”
- sacrifice code cleanliness for short-term speed
- create a second system when an existing coherent pipeline already exists
- judge a local change through production/platform behavior alone
- leave failed experiments in the repo
- add tests mechanically without assessing runtime cost and signal value
- send every change through the same delivery path without scope qualification
- ignore workflow/tooling debt when touching CI/CD areas

---

## Required response format before acting

For each code, design, UI, template, workflow, or structural content task, provide:

### 1. Qualification
In short form:
- real object of change
- systems touched
- entry point: proven or plausible
- exact system or similar case
- stop threshold
- success criteria
- minimal validation / testing / delivery level

### 2. Intervention plan
- where you will act
- why this is the right entry point
- what you will not touch
- how you will validate

### 3. Implementation
- minimal patch
- centralized scope
- no drift
- no opportunistic side changes

### 4. Validation
- what was checked
- what remains uncertain
- what was intentionally left untouched
- any residual doubt stated explicitly

---

## What the user should demand in return

The user should require that the LLM:
1. qualifies the task before acting
2. names the exact intended entry point
3. distinguishes proof from hypothesis
4. states a stop/requalification threshold
5. defines success beyond mere functionality
6. explains why the proposed solution is the cleanest sufficient one
7. avoids opening a parallel system without strong justification
8. proposes the smallest credible validation layer
9. keeps validation runtime cost proportionate
10. identifies whether the change affects only source behavior or also the delivery chain
11. proposes the smallest relevant staged validation sequence
12. names any artifact or workflow implication when generation/build/deploy is touched
13. flags avoidable CI/CD tooling debt when workflows or actions are in scope
14. leaves the repo clean
15. knows when to stop instead of forcing a bad direction

---

## One-line operating principle

Do not act quickly on apparent simplicity.
First verify whether the request is truly local or actually a multi-system compatibility problem, then implement the smallest clean solution and protect it with the smallest credible validation layer and, when relevant, the smallest justified staged delivery-chain validation.
