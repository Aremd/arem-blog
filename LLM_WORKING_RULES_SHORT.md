# LLM Working Rules — Short

## Core rule

Do not act on apparent simplicity.

First qualify the task.
Then choose the right mode of work.
Then implement the smallest clean solution.
Then validate it with the smallest credible safety net.

---

## Qualification required before acting

Before any code, design, UI, template, workflow, or structural content change, answer briefly:

1. What is the real object of change?
2. What systems are touched?
3. Is the entry point proven or only plausible?
4. Is this the exact system or only a similar case?
5. What is the stop / requalification threshold?
6. What does success mean here across:
   - function
   - rendering
   - architecture
   - maintainability
   - evolvability
7. What is the smallest credible validation level?
   - manual local validation
   - targeted test
   - smoke test
   - staged delivery validation if relevant

Do not implement before answering these questions.

---

## Decision rule

### Act directly only if
- one system is touched
- the entry point is proven
- the change is local and reversible
- success criteria are clear
- validation is straightforward

### Map first if
- several systems interact
- the entry point is only plausible
- branding, theme logic, templates, metadata, assets, workflows, or platform behavior are involved
- side effects are possible
- the clean solution is not yet clearly formulable

### Stop and requalify if
- two iterations do not clearly improve the result
- technical success and intended/rendered success diverge
- the solution starts spreading across files without a clear center
- new fixes are compensating for a weak initial hypothesis
- the solution becomes harder to explain than the original problem

---

## Intervention rule

- Map the real system before acting
- Identify the real source of truth
- Intervene at one legitimate point
- Prefer central, reversible, explainable changes
- Avoid patch chains
- Avoid parallel systems when an existing pipeline already exists
- Keep scope tight
- Validate locally first
- Clean before finishing

One problem = one scope = one coherent intervention.

---

## Success rule

A solution is successful only if it is:

- functionally correct
- right in rendering and intention
- structurally clean
- maintainable
- easy to explain
- evolvable
- validated at the right level
- proportionate to the problem

A solution that works but degrades the codebase is not acceptable.

---

## Delivery-chain rule

If the change touches build, artifacts, deploy, metadata, generation, or live-served behavior, also determine:

1. whether scope detection is needed
2. the smallest staged validation chain
3. any artifact implications
4. any workflow/tooling maintenance implications

Do not route every change through the same heavy path.

---

## Forbidden mistakes

Do not:
- implement before minimal mapping
- classify by surface simplicity instead of real dependencies
- rely on a similar case instead of the exact mechanism
- stack overrides to save a weak hypothesis
- confuse “it displays” with “it is successful”
- sacrifice cleanliness for speed
- create a second system when a coherent one already exists
- leave failed experiments in the repo
- add tests mechanically without assessing runtime cost and signal value

---

## Required response format

Before acting, provide:

### Qualification
- object of change
- systems touched
- entry point: proven or plausible
- exact system or similar case
- stop threshold
- success criteria
- validation level

### Plan
- where you will act
- why this is the right entry point
- what you will not touch
- how you will validate

### Validation
- what was checked
- what remains uncertain
- what was intentionally left untouched
