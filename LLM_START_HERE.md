# LLM Start Here — How to Work in This Repo

This repository is worked on with multiple LLMs.
Your job is not just to produce a working patch.
Your job is to produce changes that are correct, clean, explainable, maintainable, and proportionate to the problem.

Before doing anything, read this file fully.

---

## 1. Operating philosophy

In this repo, speed is not the primary value.
Correct classification of the task is.

A change is not considered good just because it works.
It must also:
- act at the right level
- preserve structural clarity
- remain easy to explain
- remain easy to modify later
- avoid unnecessary system drift
- use a validation level proportionate to the actual risk

Small-looking requests may hide multi-system compatibility problems.
Do not act on apparent simplicity.

---

## 2. Which rules file to use

This repo provides two rule layers:

### `LLM_WORKING_RULES_SHORT.md`
Use this by default.

It is the operational ruleset.
It tells you how to qualify a task, how to decide whether to act or map first, how to keep scope tight, and how to validate proportionately.

Read and apply it:
- for any normal code task
- for design/UI refinements
- for local template/content-structure changes
- for small to medium modifications
- whenever the task seems straightforward

### `LLM_WORKING_RULES_FULL.md`
Use this when the task is structurally ambiguous, sensitive, or multi-system.

Read it in addition to the short version when:
- multiple systems interact
- the entry point is not yet proven
- branding, theme logic, metadata, assets, generation, workflows, or delivery chain are involved
- the task touches build, deploy, artifact generation, or live-served behavior
- a local fix may create hidden side effects
- you are unsure whether the task is truly local
- you need to justify architectural choices more carefully

### Rule of thumb
- Start with `SHORT`
- Escalate to `FULL` when uncertainty or system interaction rises

If in doubt, use both.

---

## 3. Required behavior before acting

Before proposing any patch, you must first provide a short qualification of the task.

Your qualification must state:
1. the real object of change
2. the systems touched
3. whether the entry point is proven or only plausible
4. whether this is the exact system or only a similar case
5. the stop / requalification threshold
6. the success criteria
7. the smallest credible validation level

Do not skip this step.

---

## 4. What “good work” means in this repo

A successful change is not only:
- functional

It must also be:
- visually/right in intention when rendering matters
- structurally clean
- maintainable
- easy for another contributor to understand
- elegant in scope
- evolvable later
- validated at the right level
- cleanly integrated in the delivery chain if relevant

A patch that works but introduces unnecessary complexity is a failed success.

---

## 5. When to stop and requalify

Do not keep patching to save a weak direction.

Stop and requalify if:
- two iterations do not clearly improve the result
- technical success diverges from intended/rendered success
- the change starts spreading across files without a clear center
- you are compensating for a weak initial hypothesis
- the solution becomes harder to explain than the original issue
- validation/delivery logic becomes too heavy for the actual problem

---

## 6. Validation philosophy

Always choose the smallest credible validation layer.

Possible levels include:
- no extra validation
- manual local validation
- targeted automated test
- smoke test
- staged delivery-chain validation

Do not over-test by reflex.
Do not under-validate when regression risk is real.

If build, artifacts, deploy, workflows, or live-served behavior are touched, think beyond local source validation.

---

## 7. Repository cleanliness requirement

Leave no:
- temporary files
- backup files
- abandoned experiments
- dead CSS
- orphaned assets
- unnecessary parallel systems
- avoidable workflow/tooling debt

This repo should remain understandable after your intervention.

---

## 8. Output format expected from you

Before implementation, provide:

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
- why this is the correct entry point
- what you will not touch
- how you will validate

### Then only
- implementation
- validation summary
- residual uncertainty if any

---

## 9. Final rule

Do not optimize for immediate patch production.

Optimize for:
- correct task classification
- smallest clean intervention
- proportionate validation
- long-term clarity of the repo

If the task only looks small, treat that as a warning, not as permission to rush.
