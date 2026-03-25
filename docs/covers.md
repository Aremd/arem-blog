# Cover generation

## Purpose

This repository uses a centralized script to generate article cover assets.

The goal is to keep cover production consistent across the blog and avoid manual one-off workflows.

## Script location

scripts/generate-covers.py

## Recommended usage

Run the script from the repository root with the article directory only:

python3 scripts/generate-covers.py <article-dir>

Example:

python3 scripts/generate-covers.py content/en/post/pharos-watch-analysis/

In this mode, the script reads the article front matter and uses the value of `coverTheme`.

## Backward-compatible manual usage

The previous manual mode is still supported:

python3 scripts/generate-covers.py <theme> <article-dir>

Example:

python3 scripts/generate-covers.py governance content/en/post/le-doux-pouvoir/

## Supported themes

The script currently supports:

- pharos
- governance

## Required article configuration

The article front matter should include:

coverTheme: pharos|governance
image: cover.png

Example:

coverTheme: pharos
image: cover.png

## Generated files

The script generates the following files inside the target article directory:

- cover.svg
- cover.png

## Output format

The current templates use a fixed canvas of:

- 1200 × 630

The PNG is generated from the SVG through macOS sips.

## Typical workflow

1. Create or update the article directory.
2. Set `coverTheme` in the article front matter.
3. Run the generator from the repository root.
4. Verify that cover.svg and cover.png were created or updated.
5. Run Hugo locally and verify rendering.

## Verification

Useful checks:

find content/en/post/my-article -maxdepth 1 -type f | sort
file content/en/post/my-article/cover.png

## Current limitations

The current generator is centralized and more robust than before, but it still has limits:

- it only supports a limited number of themes
- it does not yet generate a dedicated social-only image variant
- it does not yet inject article titles into the generated cover

## Planned evolution

The preferred next step is to improve the existing generator rather than create a parallel system.

Planned direction:

- support additional visual families
- eventually support a dedicated social image output such as social-cover.png
- possibly support title-aware composition for social sharing

## Working rule

Do not create article covers through a separate manual workflow if the centralized generator can be extended cleanly.

The preferred method is:

- define the visual intention in article front matter
- generate covers from the centralized script
- keep one coherent cover generation system across the repository
