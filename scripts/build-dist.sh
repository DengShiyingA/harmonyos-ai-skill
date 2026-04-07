#!/usr/bin/env bash
# Build distribution files for multiple AI tools from the single source SKILL.md.
# Run from repo root:  ./scripts/build-dist.sh
set -euo pipefail

SRC="harmonyos-development/SKILL.md"
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

# Clean + recreate dist
rm -rf "$DIST"
mkdir -p \
  "$DIST/claude-code/harmonyos-development" \
  "$DIST/plain" \
  "$DIST/cursor" \
  "$DIST/copilot" \
  "$DIST/continue" \
  "$DIST/windsurf" \
  "$DIST/cline" \
  "$DIST/agents-md" \
  "$DIST/gemini-cli" \
  "$DIST/system-prompt"

# 1. Claude Code native (original format, for reference / direct copy)
cp "$SRC" "$DIST/claude-code/harmonyos-development/SKILL.md"

# 2. Plain Markdown - for ChatGPT / Gemini / DeepSeek / Qwen / Ollama custom instructions
printf '%s\n' "$BODY" > "$DIST/plain/harmonyos-knowledge.md"

# 3. Cursor modern MDC rule (place in .cursor/rules/harmonyos.mdc)
{
  cat <<'HDR'
---
description: >
  HarmonyOS NEXT development expert — ArkTS, ArkUI, Stage model, 60+ Kit APIs,
  UI components (Tabs/Swiper/WaterFlow/Grid/List), state management (V1/V2/StateStore),
  navigation, animation, networking, data persistence, Camera/Audio/AVPlayer/Image Kit,
  Scan/Account/Payment/Push/Map/Share Kit, dark mode, immersive window, keyboard,
  gestures, permissions, testing, code obfuscation, performance optimization,
  third-party libraries (@ohos/axios, lottie, imageknife, pulltorefresh).
globs:
  - "**/*.ets"
  - "**/module.json5"
  - "**/app.json5"
  - "**/oh-package.json5"
  - "**/build-profile.json5"
alwaysApply: false
---
HDR
  printf '%s\n' "$BODY"
} > "$DIST/cursor/harmonyos.mdc"

# 4. Cursor legacy single-file rules (.cursorrules at repo root)
printf '%s\n' "$BODY" > "$DIST/cursor/.cursorrules"

# 5. GitHub Copilot (place at .github/copilot-instructions.md)
printf '%s\n' "$BODY" > "$DIST/copilot/copilot-instructions.md"

# 6. Continue.dev rule (place in .continue/rules/)
printf '%s\n' "$BODY" > "$DIST/continue/harmonyos.md"

# 7. Windsurf rules (.windsurfrules at repo root)
printf '%s\n' "$BODY" > "$DIST/windsurf/.windsurfrules"

# 8. Cline / Roo Code custom instructions
printf '%s\n' "$BODY" > "$DIST/cline/custom-instructions.md"

# 9. AGENTS.md standard — used by OpenAI Codex CLI, sst/opencode, Amp, Aider, Cursor (read), etc.
printf '%s\n' "$BODY" > "$DIST/agents-md/AGENTS.md"

# 10. Google Gemini CLI (reads GEMINI.md at repo root or ~/.gemini/GEMINI.md globally)
printf '%s\n' "$BODY" > "$DIST/gemini-cli/GEMINI.md"

# 11. Universal system prompt (prepend role framing)
{
  echo "You are an expert HarmonyOS NEXT developer with deep knowledge of ArkTS, ArkUI, Stage model, 60+ Kit APIs, and the HarmonyOS ecosystem. Apply the following comprehensive domain knowledge (4200+ lines, 237 sections) when answering HarmonyOS development questions."
  echo
  printf '%s\n' "$BODY"
} > "$DIST/system-prompt/system.txt"

echo "Built $(find "$DIST" -type f | wc -l | tr -d ' ') files:"
find "$DIST" -type f | sort
