#!/bin/sh
files=$(git diff --cached --name-only --diff-filter=ACM | grep '^content/.*\.md$')
[ -z "$files" ] && exit 0
found=$(grep -l '—' $files 2>/dev/null)
if [ -n "$found" ]; then
  echo "Em-dash détecté dans :" && echo "$found"
  exit 1
fi
