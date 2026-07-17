#!/bin/sh
# Lint em-dash : lignes AJOUTEES uniquement (non retroactif par construction).
added=$(git diff --cached -U0 -- content | grep '^+' | grep -v '^+++' | grep '—' || true)
if [ -n "$added" ]; then
  echo "Em-dash dans les lignes ajoutees :"
  echo "$added" | cut -c1-120
  echo ""
  echo "Corriger selon le contexte : virgule, parentheses ou deux-points."
  exit 1
fi
exit 0
