#!/usr/bin/env bash
set -euo pipefail

python3 scripts/check-frontmatter.py harmonyos-development/SKILL.md

test -f harmonyos-development/references/README.md
test -f harmonyos-development/references/platform-baseline.md
test -f harmonyos-development/references/api26-preview.md
test -f harmonyos-development/references/arkts-rules.md
test -f harmonyos-development/references/arkui-components.md
test -f harmonyos-development/references/stage-model.md
test -f harmonyos-development/references/navigation.md
test -f harmonyos-development/references/state-management.md
test -f harmonyos-development/references/permissions.md
test -f harmonyos-development/references/performance.md
test -f harmonyos-development/references/build-sign-release.md
test -f harmonyos-development/recipes/debug-build-error.md
test -f harmonyos-development/recipes/review-arkts-code.md
test -f harmonyos-development/examples/permission-request.ets
test -f harmonyos-development/examples/lazyforeach-list.ets
test -f harmonyos-development/evals/cases.yaml

echo "OK: skill package validated"
