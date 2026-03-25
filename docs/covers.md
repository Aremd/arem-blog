# Cover generation

## Purpose

This repository uses a centralized script to generate article cover assets.

The goal is to keep cover production consistent across the blog and avoid manual one-off workflows.

## Script location

scripts/generate-covers.py

## Current usage

Run the script from the repository root:

python3 scripts/generate-covers.py <theme> <article-dir>

Example:

python3 scripts/generate-covers.py governance content/en/post/my-article/

## Supported themes

The script currently supports:

- pharos
- governance

## Generated files

The script generates the following files inside the target article directory:

- cover.svg
- cover.png

## Output format

The current templates use a fixed canvas of:

- 1200 × 630

The PNG is generated from the SVG through macOS sips.

## Expected article configuration

The generated cover is referenced in front matter with:

image: cover.png

## Typical workflow

1. Create the article directory.
2. Run the generator from the repository root.
3. Verify that cover.svg and cover.png were created.
4. Reference cover.png in the article front matter.
5. Run Hugo locally and verify rendering.

## Verification

Useful checks:

find content/en/post/my-article -maxdepth 1 -type f | sort
file content/en/post/my-article/cover.png

## Current limitations

The current generator is centralized but still manual:

- the theme must be passed explicitly as a script argument
- the script only supports a limited number of themes
- it does not read article front matter
- it does not produce a dedicated social-only image variant

## Planned evolution

The preferred next step is to improve the existing generator rather than create a parallel system.

Planned direction:

- read the article front matter
- use a dedicated field such as coverTheme
- support additional visual families
- eventually support a dedicated social image output such as social-cover.png

## Working rule

Do not create article covers through a separate manual workflow if the centralized generator can be extended cleanly.

The preferred method is:

- understand the current generator
- improve it in place
- keep one coherent cover generation system across the repository
