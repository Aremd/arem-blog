# arem-blog — Working Method

This document describes how work is done in this repository.
It is written for any contributor — human or LLM — who needs to understand the project and intervene in it cleanly.

---

## 1. About this repository

**arem-blog** is the source code of [arem.blog](https://arem.blog), a bilingual (FR/EN) personal publication at the intersection of philosophy and DeFi, written under the name *Arem* (subtitle: *Philo & DeFi*).

- **Author and sole maintainer:** Arem ([@aremd_](https://x.com/aremd_) on X, [@arem_d](https://t.me/arem_d) on Telegram)
- **Live site:** https://arem.blog
- **Canonical repo:** https://github.com/Aremd/arem-blog

### Stack

- **Hugo 0.158.0 extended** with the **Stack** theme (converted from submodule to tracked files)
- **Vercel** for deployment
- **Umami Cloud** for analytics
- **HackMD** for drafting
- Writing happens in HackMD → versioning in GitHub → deployment via Vercel

---

## 2. Repository structure

```
arem-blog/
├── content/
│   ├── fr/post/[slug]/index.md    Page bundles — French articles
│   └── en/post/[slug]/index.md    Page bundles — English articles
├── assets/                         custom.scss, custom.html, icons
├── layouts/                        Template overrides on top of Stack
├── scripts/
│   └── generate-covers.py          Cover generation (SVG → PNG via sips)
├── themes/stack/                   Tracked theme files (not a submodule)
├── static/                         Static assets (avatar, etc.)
├── hugo.toml                       Hugo configuration
└── vercel.json                     Root `/` redirects to `/en/`
```

### Multilingual setup

- `contentDir` is set per language
- `defaultContentLanguage = "en"`
- `defaultContentLanguageInSubdir = true`
- Cross-language linking uses the `translationKey` field in front matter

---

## 3. Conventions

These conventions are **non-negotiable**. They were established through specific incidents and exist to prevent their recurrence.

### Page bundles

- **Folder name = exact slug from front matter.** Example: an article with `slug: "gentle-power"` lives in `content/en/post/gentle-power/index.md`.
- To rename a bundle, use `git mv` — this preserves history.
- Always copy the slug verbatim from the front matter. Never reformulate it from memory.

### Article titles

- **No em dashes (`—`) in titles.** X (Twitter) fails to crawl preview images for URLs whose titles contain em dashes. Confirmed through live testing. Use a colon, a period, or rephrase.
- Example: `"Intro: Self-Custody, But How Far?"` — not `"Intro — Self-Custody, But How Far?"`.

### Hugo page bundle resources

- **No `?v=2` or any query parameter** on references to page bundle resources (`image: "cover.png"`, not `image: "cover.png?v=2"`). This broke cover display on the live site in a past incident.

### Tags and categories

- All tags and categories are in **English**, in both FR and EN versions of articles.
- Hugo's related-content engine matches tags as exact strings within the same language scope. `Gouvernance` does not match `Governance`. English-only avoids the divergence.

### Covers (visual charter — "intensité B")

- Dark gradient background: `#0e1c2f → #172b45`
- Luminous strokes with radial halos, strong opacity
- One distinctive visual motif per article (concentric circles, fluid curves, horizontal strata, etc.)
- Generated programmatically as SVG, then converted to PNG:
  ```
  sips -s format png --resampleWidth 1200 cover.svg --out cover.png
  ```
- Script: `scripts/generate-covers.py`

### Color variables (defined in `custom.scss`)

- Accent: `#5b9bd5`
- Body background: `#0f1419`
- Card background: `#1c2530`
- Separator: `#2a3542`

### Commit messages

- Prefix with `chore:`, `feat:`, `fix:`, `docs:`, or `refactor:`
- One commit = one coherent intent

---

## 4. Operating philosophy

### Core principle

**Do not act on apparent simplicity.**

A request that looks small may hide multi-system compatibility problems. Speed is not the primary value here. Correct classification of the task is.

### What a good change must do

A change is not successful just because it works. It must also:
- act at the right level
- preserve structural clarity
- remain easy to explain
- remain easy to modify later
- avoid unnecessary system drift
- use a validation level proportionate to the actual risk

A solution that works but degrades the codebase is not acceptable.

---

## 5. Qualification filter — before acting

Before any non-trivial change to code, templates, styling, workflows, or content structure, answer these seven questions briefly:

1. **Real object of change.** What is actually being changed? (content, style, template, rendering logic, routing, configuration, asset pipeline, metadata, etc.)
2. **Systems touched.** One isolated system, or several interacting? Typical multi-system combinations include: theme + branding, template + CSS, content + metadata, asset generation + social sharing.
3. **Entry point certainty.** Is the intended entry point *proven* or only *plausible*? Do not implement from a plausible entry point as if it were confirmed.
4. **Exact system or similar case.** Is this the actual mechanism in use here, or only something that looks familiar from another project?
5. **Stop / requalification threshold.** What concrete signal will trigger a stop and reclassification instead of further patching?
6. **Success criteria.** What does success mean here across function, rendering, architecture, maintainability, and evolvability?
7. **Minimal validation.** What is the smallest credible validation layer — local manual check, targeted test, smoke test, or staged pre/post-deploy validation?

Do not implement before answering these.

---

## 6. Decision rule

### Act directly only if
- one system is touched
- the entry point is proven
- the change is local and reversible
- success criteria are clear
- validation is straightforward

### Map first if
- several systems interact
- the entry point is only plausible
- branding, templates, theme logic, metadata, assets, workflows, or external platform behavior are involved
- a local fix may create hidden side effects
- the clean solution is not yet clearly formulable

### Stop and requalify if
- two iterations do not clearly improve the result
- technical correctness and rendered/intended correctness diverge
- the fix starts spreading across files without a clear center
- new fixes are compensating for a weak initial hypothesis
- the change becomes harder to explain than the original problem

---

## 7. Intervention principles

- **One problem = one scope = one coherent intervention.** Avoid patch chains.
- **Map the real system before acting.** Identify the actual source of truth — never assume the obvious file is the real driver.
- **Intervene at one legitimate point.** Prefer central, reversible, explainable changes over scattered overrides.
- **Use the project's extension layer.** Refinements go in `custom.scss` / `custom.html` / `layouts/`, not in theme/vendor sources, unless structural necessity forces it.
- **Validate locally before concluding from production.** Distinguish local behavior, build output, cache/platform behavior, and external-service behavior.
- **Aggregate commands.** Chain with `&&`. No inline comments. Minimum number of steps that still preserve verification points.
- **Clean before finishing.** No temporary files, backups, abandoned experiments, dead CSS, or orphaned assets.

---

## 8. Known pitfalls

These are concrete traps discovered through past incidents. Worth reading before intervening.

- **X preview cache is aggressive.** URLs with prior 404 history may stay cached for a while. Cache issues sometimes resolve on their own — watch the real-time crawl indicator before assuming a code problem.
- **HackMD-to-GitHub pushes can silently overwrite front matter.** After every push from HackMD, verify `image:` and `title:` casing in the committed file.
- **`git add` staging nothing despite edits** means the replacement string didn't match exactly. Verify with `grep` before assuming success.
- **Stray files** (`cover-A.svg`, `cover (1).svg`, etc.) must be explicitly `rm`'d before `git add -A` if they shouldn't be committed.
- **Avatar config in `hugo.toml`** must be a simple string (`avatar = "img/avatar.png"`). Nested config causes a fatal build error.
- **Sidebar overrides** (e.g., menu padding) must go as inline styles in `themes/stack/layouts/_partials/sidebar/left.html`. SCSS and external stylesheets do not reliably override Stack's compiled CSS.
- **In-article language switcher** is intentionally disabled via `$showTranslations := false`.
- **Footer credits** removed via root-level override at `layouts/partials/footer/footer.html`.

---

## 9. Git workflow

### Standard flow

```
git add -A && git commit -m "chore: …" && git push
```

### When push is rejected (remote has new commits)

```
git pull --rebase && git push
```

### Renaming files or folders

Always use `git mv` — it preserves history and lets Git detect the rename at 100%, keeping the log clean.

### Verifying production after deploy

```
curl -sL -o /dev/null -w "%{http_code}\n" https://arem.blog/[lang]/post/[slug]/
```

Expect `200`. Vercel redeploys automatically on push; allow ~30 seconds.

---

## Forbidden mistakes

- Implementing before minimal mapping
- Classifying by surface simplicity instead of real dependencies
- Relying on a similar case instead of verifying the exact mechanism
- Stacking overrides to save a weak hypothesis
- Confusing "it displays" with "it is successful"
- Sacrificing cleanliness for speed
- Creating a second system when a coherent one already exists
- Leaving failed experiments in the repo

---

## One-line operating principle

> Do not act quickly on apparent simplicity. First verify whether the request is truly local or actually a multi-system compatibility problem, then implement the smallest clean solution and protect it with the smallest credible validation.
