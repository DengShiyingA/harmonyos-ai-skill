#!/usr/bin/env bash
# Validate the HarmonyOS agent skill package.
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

python3 scripts/check-frontmatter.py harmonyos-development/SKILL.md

required=(
  harmonyos-development/references/README.md
  harmonyos-development/references/platform-baseline.md
  harmonyos-development/references/api26-preview.md
  harmonyos-development/references/arkts-rules.md
  harmonyos-development/references/state-management.md
  harmonyos-development/references/performance.md
  harmonyos-development/recipes/debug-build-error.md
  harmonyos-development/recipes/review-arkts-code.md
  harmonyos-development/examples/permission-request.ets
  harmonyos-development/examples/lazyforeach-list.ets
  harmonyos-development/evals/cases.yaml
)

for file in "${required[@]}"; do
  if [[ ! -f "$file" ]]; then
    echo "ERROR: missing required skill support file: $file" >&2
    exit 1
  fi
done

echo "OK: skill support files present"
