#!/usr/bin/env bash
# Build distribution files for multiple AI tools from the HarmonyOS skill package.
# Run from repo root:  ./scripts/build-dist.sh
set -euo pipefail

SKILL_DIR="harmonyos-development"
SRC="$SKILL_DIR/SKILL.md"
DIST="dist"

if [[ ! -f "$SRC" ]]; then
  echo "ERROR: $SRC not found. Run from repo root." >&2
  exit 1
fi

# Extract body = everything after the second "---" line (skip YAML frontmatter)
BODY=$(awk '
  /^---$/ { n++; if (n == 2) { in_body = 1; next } else next }
  in_body { print }
' "$SRC")

# Optional support files are kept for native skill runtimes and appended for single-file tools.
SUPPORT_FILES=()
for dir in references recipes examples; do
  if [[ -d "$SKILL_DIR/$dir" ]]; then
    while IFS= read -r file; do
      SUPPORT_FILES+=("$file")
    done < <(find "$SKILL_DIR/$dir" -type f | sort)
  fi
done

build_combined_body() {
  printf '%s\n' "$BODY"

  if (( ${#SUPPORT_FILES[@]} > 0 )); then
    echo
    echo "---"
    echo
    echo "# Supporting Skill Files"
    echo
    echo "The following sections are generated from supporting files for AI tools that only accept a single instruction file. Native Agent Skill runtimes should use the directory version instead."

    for file in "${SUPPORT_FILES[@]}"; do
      echo
      echo "---"
      echo
      echo "## $file"
      echo
      cat "$file"
    done
  fi
}

# Clean + recreate dist
rm -rf "$DIST"
mkdir -p \
  "$DIST/claude-code" \
  "$DIST/plain" \
  "$DIST/cursor" \
  "$DIST/copilot" \
  "$DIST/continue" \
  "$DIST/windsurf" \
  "$DIST/cline" \
  "$DIST/agents-md" \
  "$DIST/gemini-cli" \
  "$DIST/system-prompt"

# 1. Claude Code / native Agent Skill package: preserve SKILL.md plus supporting files.
cp -R "$SKILL_DIR" "$DIST/claude-code/$SKILL_DIR"

# Materialize combined body once for single-file rule systems.
COMBINED_BODY="$(build_combined_body)"

# 2. Plain Markdown - for ChatGPT / Gemini / DeepSeek / Qwen / Ollama custom instructions
printf '%s\n' "$COMBINED_BODY" > "$DIST/plain/harmonyos-knowledge.md"

# 3. Cursor modern MDC rule (place in .cursor/rules/harmonyos.mdc)
{
  cat <<'HDR'
---
description: >
  HarmonyOS NEXT development expert — ArkTS, ArkUI, Stage model, API 24 production baseline,
  API 26 preview boundary, state management, Navigation, permissions, networking, data persistence,
  build/sign/release, testing, and performance optimization.
globs:
  - "**/*.ets"
  - "**/module.json5"
  - "**/app.json5"
  - "**/oh-package.json5"
  - "**/build-profile.json5"
alwaysApply: false
---
HDR
  printf '%s\n' "$COMBINED_BODY"
} > "$DIST/cursor/harmonyos.mdc"

# 4. Cursor legacy single-file rules (.cursorrules at repo root)
printf '%s\n' "$COMBINED_BODY" > "$DIST/cursor/.cursorrules"

# 5. GitHub Copilot (place at .github/copilot-instructions.md)
printf '%s\n' "$COMBINED_BODY" > "$DIST/copilot/copilot-instructions.md"

# 6. Continue.dev rule (place in .continue/rules/)
printf '%s\n' "$COMBINED_BODY" > "$DIST/continue/harmonyos.md"

# 7. Windsurf rules (.windsurfrules at repo root)
printf '%s\n' "$COMBINED_BODY" > "$DIST/windsurf/.windsurfrules"

# 8. Cline / Roo Code custom instructions
printf '%s\n' "$COMBINED_BODY" > "$DIST/cline/custom-instructions.md"

# 9. AGENTS.md standard — used by OpenAI Codex CLI, sst/opencode, Amp, Aider, Cursor (read), etc.
printf '%s\n' "$COMBINED_BODY" > "$DIST/agents-md/AGENTS.md"

# 10. Google Gemini CLI (reads GEMINI.md at repo root or ~/.gemini/GEMINI.md globally)
printf '%s\n' "$COMBINED_BODY" > "$DIST/gemini-cli/GEMINI.md"

# 11. Universal system prompt (prepend role framing)
{
  echo "You are an expert HarmonyOS NEXT developer with deep knowledge of ArkTS, ArkUI, Stage model, HarmonyOS Kit APIs, and the HarmonyOS ecosystem. Apply the following domain knowledge when answering HarmonyOS development questions."
  echo
  printf '%s\n' "$COMBINED_BODY"
} > "$DIST/system-prompt/system.txt"

echo "Built $(find "$DIST" -type f | wc -l | tr -d ' ') files:"
find "$DIST" -type f | sort
