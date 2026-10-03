<div align="center">

**English** | [简体中文](./README.md)

<img src="./assets/en/hero-banner.svg" alt="HarmonyOS AI Skill" width="100%"/>

# 🧠 HarmonyOS AI Skill

### The largest HarmonyOS knowledge pack for AI coding — make 11+ AI tools actually write ArkTS

*2 responsibility-separated skills · lightweight routing + 19 on-demand reference modules · HarmonyOS 7 / API 26 Release baseline, with API 24 compatibility*

[![License](https://img.shields.io/badge/License-MIT-yellow)](./LICENSE)
[![HarmonyOS](https://img.shields.io/badge/HarmonyOS-7%20%2F%20API%2026-black)](https://developer.huawei.com/consumer/cn/)
[![ArkTS](https://img.shields.io/badge/ArkTS-API%2022--26-blue)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V5/arkts-get-started-V5)
[![Kits](https://img.shields.io/badge/Kits-60+-orange)](#whats-inside-the-knowledge)
[![AI Tools](https://img.shields.io/badge/AI_Tools-11+-purple)](#supported-ai-tools)
[![AGENTS.md](https://img.shields.io/badge/AGENTS.md-Standard-green)](https://agents.md)

[![Stars](https://img.shields.io/github/stars/Fly0307/harmonyos-ai-skill?style=social)](https://github.com/Fly0307/harmonyos-ai-skill/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/Fly0307/harmonyos-ai-skill/zx-dev)](https://github.com/Fly0307/harmonyos-ai-skill/commits/zx-dev)
[![Issues](https://img.shields.io/github/issues/Fly0307/harmonyos-ai-skill)](https://github.com/Fly0307/harmonyos-ai-skill/issues)

<br/>

**Ask Cursor to write HarmonyOS — it hands you React.**
**Ask Claude to edit `module.json5` — it writes `package.json`.**
**Ask Copilot about `@ObjectLink` — it says "that API doesn't exist."**

General-purpose LLMs have never systematically learned HarmonyOS — their training data barely contains ArkTS, the Stage model, or HarmonyOS Kits.
So I organized Huawei's official documentation, best practices, and API references into a **lightweight router plus on-demand references**. Agents can retrieve ArkTS, 60+ Kits, Native API compatibility, and API 26 Release upgrade guidance precisely, while a separate HDC automation skill owns device operations.

**Two source skill directories produce drop-in configs for 11+ AI tools.** Native skill runtimes load only the relevant modules; single-file rule systems receive a generated complete knowledge pack.

<br/>

[🚀 Install](#installation) · [📖 What's Inside](#whats-inside-the-knowledge) · [🛠️ Supported Tools](#supported-ai-tools) · [✅ Verify It Works](#verifying-it-works)

</div>

---

<div align="center">
<img src="./assets/en/before-after.svg" alt="Before vs After comparison" width="100%"/>
</div>

---

## ⚡ Quick start (Claude Code, 30 seconds)

Pick the command set for your OS — **copy-paste straight into your terminal**:

### 🍎 macOS

```bash
git clone -b zx-dev https://github.com/Fly0307/harmonyos-ai-skill.git ~/src/harmonyos-ai-skill
mkdir -p ~/.claude/skills
ln -s ~/src/harmonyos-ai-skill/harmonyos-development ~/.claude/skills/harmonyos-development
ln -s ~/src/harmonyos-ai-skill/harmony-hdc-ui-automation ~/.claude/skills/harmony-hdc-ui-automation
# Restart Claude Code, then ask: "What skills are available?"
```

### 🐧 Linux

```bash
git clone -b zx-dev https://github.com/Fly0307/harmonyos-ai-skill.git ~/src/harmonyos-ai-skill
mkdir -p ~/.claude/skills
ln -s ~/src/harmonyos-ai-skill/harmonyos-development ~/.claude/skills/harmonyos-development
ln -s ~/src/harmonyos-ai-skill/harmony-hdc-ui-automation ~/.claude/skills/harmony-hdc-ui-automation
# Restart Claude Code, then ask: "What skills are available?"
```

### 🪟 Windows (PowerShell 7+)

> ⚠️ **Must run in PowerShell, not CMD (Command Prompt)** — `New-Item` is a PowerShell cmdlet; CMD doesn't know it. Right-click Start → "Windows PowerShell (Admin)".

```powershell
# First enable "Developer Mode" (one-time): Settings → Privacy & security → For developers → toggle on
git clone -b zx-dev https://github.com/Fly0307/harmonyos-ai-skill.git $HOME\src\harmonyos-ai-skill
New-Item -ItemType Directory -Force $HOME\.claude\skills | Out-Null
New-Item -ItemType SymbolicLink -Path $HOME\.claude\skills\harmonyos-development -Target $HOME\src\harmonyos-ai-skill\harmonyos-development
New-Item -ItemType SymbolicLink -Path $HOME\.claude\skills\harmony-hdc-ui-automation -Target $HOME\src\harmonyos-ai-skill\harmony-hdc-ui-automation
# Restart Claude Code, then ask: "What skills are available?"
```

> Don't want to enable Developer Mode? `Copy-Item -Recurse` both source
> directories into `$HOME\.claude\skills\` instead (you will need to re-copy
> after upstream updates).

Using a different tool (Cursor / Copilot / ChatGPT...)? See [all install options below](#installation).

---

## Why you need this

| Question | Plain AI | With the skill installed |
|---|---|---|
| What do I write the UI in? | "Use React Native" | "Use ArkUI — `@Component struct` declarative components" |
| How do I manage state? | "useState / Redux" | "`@State` / `@ObjectLink`; for new code use V2 decorators (stable in API 23)" |
| Page navigation? | "react-router or Vue Router" | "`Navigation` + `NavPathStack.pushPath()` — Router is being phased out" |
| HTTP requests? | "axios / fetch" | "`@kit.NetworkKit`'s `http.createHttp()`, or the `@ohos/axios` third-party lib" |
| Camera permission? | A snippet of Android Manifest | `module.json5` config + 3-step `abilityAccessCtrl` flow with settings fallback |
| Background audio? | Vague hints about a service | "You MUST create AVSession + request `KEEP_BACKGROUND_RUNNING` long-task" |

The knowledge isn't in the AI's head — you have to feed it in. **That's what this repo does.**

Development knowledge lives in the router and on-demand resources under [`harmonyos-development`](./harmonyos-development/). Device control stays in the separate [`harmony-hdc-ui-automation`](./harmony-hdc-ui-automation/) skill. The builder generates tool-specific artifacts from both source directories.

<details>
<summary><b>🤔 What is a "skill"?</b> (click to expand)</summary>

A skill is a chunk of domain knowledge (in Markdown) that an AI coding tool loads as background context when you chat with it. Once installed, the AI "knows" the domain — it will give you HarmonyOS-correct answers instead of generic TypeScript / React advice. Different tools call them different things (skills, rules, instructions, system prompt), but they all work the same way: **extra text prepended to the model's context**.

</details>

## 🧭 Progressive loading: route first, load knowledge on demand

The core mechanism is **progressive loading**. This repository does not put every HarmonyOS explanation into one giant Markdown file and inject it into every session. An agent reads a short routing entry first, then opens only the modules needed for the current task.

| Layer | Contents | Loading behavior |
|---|---|---|
| `harmonyos-development/SKILL.md` | Topic routing, official sources, and reference selection rules | Loaded first when the native skill is triggered |
| `references/` | ArkTS, ArkUI, projects, Kits, permissions, networking, and testing modules | Loaded by task topic |
| `recipes/`, `examples/` | Build debugging, code review, and runnable examples | Loaded only when a workflow or code sample is needed |
| `harmony-hdc-ui-automation/` | HDC, UiTest, hilog, screenshots, and device-file operations | Triggered separately for device tasks |
| `dist/agents-md/AGENTS.md` | Lightweight router for AGENTS.md-compatible tools | Loads a short entry first, then resolves sibling directories |
| `dist/*` single-file artifacts | Flattened router plus all references for compatibility | Used only by tools that cannot read multiple files |

Native skills and the lightweight `AGENTS.md` installation keep the context small. `AGENTS.full.md`, `dist/plain`, and `dist/system-prompt` are fallback artifacts for tools without progressive loading. Both modes are generated from the same source files and stay synchronized through the builder.

## 📌 Current API support

The current documentation baseline is **HarmonyOS 7 / API 26.0.0 Release**. The knowledge pack covers the API 26 SemVer rules, ArkUI `ContainerReader` and global reuse, `ComposeTitleBarV2`, the API Change Assistant, the Node.js 24 toolchain, and Kits including Agent Framework, Data Augmentation, Enterprise Space, Desktop Extension, and Spatial Recon. API 24 Release remains available as the older-device compatibility baseline.

API 26 project and upgrade guidance covers string-form `compileSdkVersion`, `targetSdkVersion`, and `compatibleSdkVersion`, API Change Assistant scans for behavior changes, and verification on both older devices and API 26 devices. The recorded Release toolchain is DevEco Studio 26.0.0.821, Hvigor 6.26.4, ohpm 26.0.0.630, and Node.js 24.14.1.

Official entry points:

- [HarmonyOS 26.0.0 release notes](https://developer.huawei.com/consumer/cn/doc/doccenter-release-notes/2600)
- [Upgrade and adaptation guide for 26.0.0](https://developer.huawei.com/consumer/en/doc/harmonyos-releases/upgrade-adaptation)
- [DevEco Studio 26.0.0 Release](https://developer.huawei.com/consumer/en/doc/harmonyos-releases/deveco-studio-new-features-2600)

**Requirements:** `git` and `curl` (or just copy-paste for web tools). No other dependencies.
**Freshness:** Tracks official release cadence. The current baseline covers HarmonyOS 7 / 26.0.0 Release (API 26; DevEco Studio 26.0.0.821), while retaining HarmonyOS 6.1.1 Release (API 24) compatibility guidance.

## What's inside the knowledge

<div align="center">
<img src="./assets/en/knowledge-map.svg" alt="Knowledge architecture" width="100%"/>
</div>

`harmonyos-development/SKILL.md` is only the topic router. Detailed knowledge lives in 19 references, 2 recipes, 2 source examples, and behavioral eval cases:

- **Language & framework** — ArkTS strictness rules, naming conventions, 13 high-performance coding rules (const, TypedArrays, HashMap, lazy import, etc.), coding style guide
- **App architecture** — Stage model: UIAbility, ExtensionAbility, AbilityStage, WindowStage lifecycles; module.json5 / app.json5 configuration
- **ArkUI components** — component lifecycle (7 callbacks + execution order), layout containers with performance comparison, `@Reusable` component reuse, **Tabs navigation**, **Swiper carousel**, **WaterFlow**, **Grid**, **TextInput**, **AlertDialog/Toast**, 10 form components quick reference, AttributeModifier reusable styles
- **State management (V2 now stable)** — V1 decorators (`@State`/`@Prop`/`@Link`/`@Provide`-`@Consume`/`@Observed`+`@ObjectLink`/`@Watch`) + V2 decorators (`@ComponentV2`/`@Local`/`@Param`+`@Once`/`@Param`+`@Event`/`@ObservedV2`+`@Trace`/`@Monitor`) + **AppStorageV2** + **PersistenceV2** (auto-persisted) + StateStore global state, with observation depth rules, batch update tips, decorator selection priority
- **Navigation** — `Navigation` + `NavPathStack` full API, `Router` basic routing (deprecated, with migration notes), `App Linking` deep links
- **Animation** — `animateTo()`, `.animation()`, `keyframeAnimateTo()`, Curve enum, spring curves, `geometryTransition` shared element transitions, animation performance tips
- **List operations** — pull-down refresh (Refresh), load-more (onReachEnd), swipe-to-delete (swipeAction), drag reorder, ListItemGroup sticky headers, scroll-to-bottom, maintain scroll position
- **Performance** — `LazyForEach` + IDataSource, `@Reusable`, `cachedCount`, `onVisibleAreaChange`, cold start optimization (lazy import), memory optimization (LRUCache/Purgeable)
- **HarmonyOS Kits** — 60+ Kits across 7 categories with import keys + code examples
- **Kit detailed sections** — Camera Kit (incl. API 24 "Follow the Person" subject tracking), Audio Kit, AVPlayer/AVRecorder, Image Kit (decode/transform/encode), Scan Kit, Account Kit, Payment Kit, Push Kit, Map Kit, **Weather Service Kit**, Core Vision Kit (OCR/face/segmentation), Form Kit (service cards), AVSession Kit, Location Kit, Notification Kit, Share Kit
- **Data persistence** — relationalStore (SQLite CRUD + sendable), preferences (KV storage), fileIo (file R/W), DocumentViewPicker (file picker)
- **Networking** — HTTP requests, WebSocket, network connectivity monitoring, background upload/download (request.agent with resume)
- **Concurrency** — TaskPool vs Worker comparison, `@Concurrent` rules, `@Sendable` shared-heap mechanism
- **System capabilities** — permission request full flow (check→request→settings fallback), immersive window (expandSafeArea), dark mode (resource qualifiers/colorMode), keyboard adaptation (KeyboardAvoidMode), screen orientation, clipboard, custom fonts, desktop shortcuts, gesture conflict resolution (hitTestBehavior/priorityGesture), EventHub, startAbilityByType
- **Web** — ArkWeb component, JS↔ArkTS bridge, cookie management, request interception
- **Cross-device** — app continuation (onContinue/onCreate data migration), cross-module resource access (HAR/HSP)
- **Engineering quality** — security coding rules + network security config (HTTPS/cert pinning), code obfuscation (ArkGuard), arkxtest testing (JsUnit + UiTest), 18 common gotchas
- **Third-party libraries** — @ohos/axios (HTTP client), @ohos/pulltorefresh, @ohos/lottie (JSON animation), @ohos/imageknife (image caching), dayjs (date utils)
- **API 23 / 24 new features** — Navigation routing stack binding, Menu anchorPosition, UDMF/drag/crypto C APIs, relationalStore sendable enhancement, AI super frame, Camera Kit "Follow the Person" subject tracking, delayed preview, DevEco Studio API 24 support
- **API 26 Release** — HarmonyOS 7 production baseline, 26.0.0 SemVer, ArkUI `ContainerReader`/global reuse/ComposeTitleBarV2, API Change Assistant, Node.js 24 toolchain, upgrade compatibility, and old-device verification
- **Current compatibility & diagnostics** — Native `APIAVAILABLE`/weak references, Linux CI, `jsLeakWatcher`, HWASan, `ContainerReader` breakpoints, and global component reuse
- **Multi-device** — responsive breakpoints (xs/sm/md/lg/xl), GridRow/GridCol, foldable support
- **Packaging & tooling** — HAP/HSP/HAR, atomic services, DevEco Studio 6.1+ (hvigor), OHPM, ArkCompiler

---

## Supported AI tools

### 1. Native skill format (auto-invoked by description matching)

| Tool | Install path | How it activates |
|---|---|---|
| **Claude Code CLI** | `~/.claude/skills/harmonyos-development/` | Claude reads `SKILL.md` frontmatter `description` and auto-loads when your question mentions HarmonyOS / ArkTS / ArkUI / Stage model / etc. Zero manual invocation. |
| **Claude Agent SDK** | Put the `harmonyos-development/` folder anywhere, point the SDK at it via the `skills` parameter when constructing the agent | Same as Claude Code — description-based auto-loading. |
| **OpenAI Codex project skills** | `.agents/skills/harmonyos-development/`, `.agents/skills/harmony-hdc-ui-automation/` | Development tasks load the core knowledge skill; device inspection, HDC, UiTest, hilog, and sandbox-file tasks load the automation skill. |

### 2. Project rules file (auto-attached to every session inside the project)

| Tool | Install path | Source file | Scope |
|---|---|---|---|
| **Cursor** (modern) | `.cursor/rules/harmonyos.mdc` | `dist/cursor/harmonyos.mdc` | Glob-matched on `*.ets`, `module.json5`, `oh-package.json5`, `build-profile.json5` |
| **Cursor** (legacy) | `.cursorrules` (repo root) | `dist/cursor/.cursorrules` | Always applied |
| **GitHub Copilot** | `.github/copilot-instructions.md` | `dist/copilot/copilot-instructions.md` | Always applied in this repo |
| **Windsurf / Codeium** | `.windsurfrules` (repo root) | `dist/windsurf/.windsurfrules` | Always applied |
| **Continue.dev** | `.continue/rules/harmonyos.md` | `dist/continue/harmonyos.md` | Always applied |
| **Cline / Roo Code** | Settings → Custom Instructions | `dist/cline/custom-instructions.md` | Per-workspace or global |
| **OpenAI Codex CLI · sst/opencode · Amp · Aider · Jules** | `AGENTS.md` (repo root) | `dist/agents-md/AGENTS.md` | Follows the shared [AGENTS.md](https://agents.md) standard |
| **Google Gemini CLI** | `GEMINI.md` (repo root) or `~/.gemini/GEMINI.md` (global) | `dist/gemini-cli/GEMINI.md` | Gemini CLI reads either path |

### 3. Generic — paste into any chat / API

| Tool | Where to paste | Source file |
|---|---|---|
| **ChatGPT / GPT-4 / GPT-5** | Settings → Personalization → Custom Instructions (or per-conversation system prompt) | `dist/plain/harmonyos-knowledge.md` |
| **Google Gemini / AI Studio** | System Instructions field | `dist/plain/harmonyos-knowledge.md` |
| **DeepSeek / Qwen / 文心一言 / Kimi / 智谱** | 系统提示 / 角色设定 field | `dist/plain/harmonyos-knowledge.md` |
| **Ollama local models** | `--system` flag | `dist/system-prompt/system.txt` |
| **Anthropic / OpenAI / any LLM API** | `system` message of your request body | `dist/system-prompt/system.txt` |

The two files differ only slightly: `plain/` is the raw Markdown; `system-prompt/` prepends a short role-framing sentence (*"You are an expert HarmonyOS NEXT developer…"*).

---

## Installation

The current upstream target is the [`zx-dev` branch of `Fly0307/harmonyos-ai-skill`](https://github.com/Fly0307/harmonyos-ai-skill/tree/zx-dev).

All `curl` commands below use a shell variable `$RAW` — **run this once in every new terminal before the commands**:

```bash
export RAW=https://raw.githubusercontent.com/Fly0307/harmonyos-ai-skill/zx-dev
```

> **Windows PowerShell users:** use `$env:RAW = "..."` and replace `curl -o foo` with `Invoke-WebRequest -Uri "..." -OutFile foo`.
> **HOME path differences:** macOS/Linux uses `~`; Windows PowerShell uses `$HOME`; CMD uses `%USERPROFILE%`.

### Claude Code CLI

Pick **one** of the three options below:

```bash
# Option A — quick copy (simplest, static snapshot)
git clone -b zx-dev https://github.com/Fly0307/harmonyos-ai-skill.git ~/src/harmonyos-ai-skill
mkdir -p ~/.claude/skills
cp -r ~/src/harmonyos-ai-skill/harmonyos-development ~/.claude/skills/

# Option B — symlink (recommended: auto-updates after upstream `git pull`)
git clone -b zx-dev https://github.com/Fly0307/harmonyos-ai-skill.git ~/src/harmonyos-ai-skill
mkdir -p ~/.claude/skills
ln -s ~/src/harmonyos-ai-skill/harmonyos-development ~/.claude/skills/harmonyos-development

# Option C — project-local only (commit it so your whole team gets the skill)
cd <your-harmonyos-project-root>
mkdir -p .claude/skills/harmonyos-development
curl -o .claude/skills/harmonyos-development/SKILL.md "$RAW/harmonyos-development/SKILL.md"
```

After installing, **restart Claude Code**. To verify, ask it: *"What skills are available?"* — it should list `harmonyos-development`.

### OpenAI Codex project-local installation

`harmonyos-development` provides ArkTS, ArkUI, Stage model, and
project-development knowledge. `harmony-hdc-ui-automation` handles real-device
HDC/UiTest control, screenshots, layout trees, hilog, app-sandbox file
transfer, and UI automation. They live in one repository but retain separate
activation boundaries. Install both in each HarmonyOS project:

```bash
python ~/src/harmonyos-ai-skill/scripts/install_skills.py \
  --project <your-harmonyos-project-root> \
  --mode link
```

Use `--mode copy` when Windows Developer Mode is disabled or the filesystem
does not support symbolic links. The installer refuses to overwrite existing
directories; use `--dry-run` to inspect destinations first.

The automation skill uses the current project's UV environment and does not
hard-code a `.venv` path. Copy
`harmony-hdc-ui-automation/assets/harmony-hdc.example.json` to
`.harmony-hdc.json` in the project root, set `bundleName`, `moduleName`, and
`abilityName`, then run:

```bash
uv run python .agents/skills/harmony-hdc-ui-automation/scripts/harmony_hdc_ui.py doctor
uv run python .agents/skills/harmony-hdc-ui-automation/scripts/harmony_hdc_ui.py devices
```

### Cursor

> **Run from:** your HarmonyOS project root (the one with `entry/` and `module.json5`)

```bash
# Recommended — modern glob-scoped .mdc rule
mkdir -p .cursor/rules
curl -o .cursor/rules/harmonyos.mdc "$RAW/dist/cursor/harmonyos.mdc"

# OR legacy single-file rules (if your Cursor version predates .mdc)
curl -o .cursorrules "$RAW/dist/cursor/.cursorrules"
```

The `.mdc` rule auto-activates only when you edit `.ets`, `module.json5`, etc., keeping context lean for non-HarmonyOS projects.

### GitHub Copilot

> **Run from:** your HarmonyOS project root

```bash
mkdir -p .github
curl -o .github/copilot-instructions.md "$RAW/dist/copilot/copilot-instructions.md"
```

Applies to Copilot Chat and inline suggestions whenever you're inside this repo. Commit it — your whole team benefits.

### Windsurf / Codeium

> **Run from:** your HarmonyOS project root

```bash
curl -o .windsurfrules "$RAW/dist/windsurf/.windsurfrules"
```

### Continue.dev

> **Run from:** your HarmonyOS project root

```bash
mkdir -p .continue/rules
curl -o .continue/rules/harmonyos.md "$RAW/dist/continue/harmonyos.md"
```

### Cline / Roo Code

1. Download the file: `curl -o harmonyos-instructions.md "$RAW/dist/cline/custom-instructions.md"`
2. In VS Code: open Cline / Roo settings → **Custom Instructions**
3. Paste the file contents into the workspace or global instructions field

### AGENTS.md standard (Codex CLI, opencode, Amp, Aider, Jules)

A single file at the repo root serves **every** tool that follows the [AGENTS.md standard](https://agents.md):

```bash
curl -o AGENTS.md "$RAW/dist/agents-md/AGENTS.md"
```

For user-level (global) scope, each tool reads a different path:

| Tool | Global path |
|---|---|
| OpenAI Codex CLI | `~/.codex/AGENTS.md` |
| sst/opencode | `~/.config/opencode/AGENTS.md` |
| Amp | `~/.config/amp/AGENTS.md` |
| Aider | uses `AGENTS.md` from current directory only |

Some tools layer multiple `AGENTS.md` files (nearest one wins / merged). Check each tool's docs.

### Google Gemini CLI

```bash
# Project-level (takes precedence):
curl -o GEMINI.md "$RAW/dist/gemini-cli/GEMINI.md"

# Global (applies to every Gemini CLI session):
mkdir -p ~/.gemini
curl -o ~/.gemini/GEMINI.md "$RAW/dist/gemini-cli/GEMINI.md"
```

### ChatGPT / Gemini web / DeepSeek / Qwen / Kimi / 文心一言

1. Open [`dist/plain/harmonyos-knowledge.md`](./dist/plain/harmonyos-knowledge.md) on GitHub
2. Click **Raw** → **Ctrl/Cmd + A** → **Ctrl/Cmd + C**
3. In your AI tool:
   - **ChatGPT:** Settings → Personalization → **Custom Instructions** → "How would you like ChatGPT to respond?" → paste
   - **Gemini web:** Start a new chat → enable **System Instructions** → paste
   - **DeepSeek / Qwen / 文心一言 / Kimi:** create a new "智能体" / "角色" / "Bot" → paste into system prompt
4. Start asking HarmonyOS questions — the model now has the knowledge loaded

### Ollama / local LLMs

```bash
# 1. Pull a capable model (qwen3-coder or qwen2.5-coder recommended for Chinese-heavy docs)
ollama pull qwen3-coder

# 2. One-liner launch with HarmonyOS system prompt baked in
ollama run qwen3-coder \
  --system "$(curl -s $RAW/dist/system-prompt/system.txt)"
```

Or bake it into a custom Modelfile (permanently saves this "HarmonyOS expert" model):

```bash
# 1. Download the system prompt
curl -o system.txt "$RAW/dist/system-prompt/system.txt"

# 2. Create a Modelfile
cat > Modelfile <<EOF
FROM qwen3-coder
SYSTEM """
$(cat system.txt)
"""
EOF

# 3. Register the custom model
ollama create harmonyos-coder -f Modelfile
ollama run harmonyos-coder
```

### Anthropic / OpenAI / any LLM API

```python
# First: pip install anthropic
import anthropic

# Assumes you've downloaded system.txt locally
# (curl -o system.txt "$RAW/dist/system-prompt/system.txt")
with open("system.txt") as f:
    system_prompt = f.read()

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from env
response = client.messages.create(
    model="claude-opus-4-7",            # latest Opus; or claude-sonnet-4-6 / claude-haiku-4-5
    system=system_prompt,
    max_tokens=2048,
    messages=[{"role": "user", "content": "How do I make a service card in HarmonyOS?"}],
)
print(response.content[0].text)
```

---

## 🪟 Windows users (native PowerShell)

> Don't want to use WSL/Git Bash? The following commands work in native
> PowerShell. Rule files and Python helpers are cross-platform; HDC/UiTest
> availability still depends on the local DevEco Studio, HarmonyOS SDK,
> drivers, and device connection.
> Recommended: **PowerShell 7+** (`winget install Microsoft.PowerShell`).

<details>
<summary><b>📋 Click to expand full PowerShell install commands</b></summary>

**Prereq: run this once in every new PowerShell window**

```powershell
$env:RAW = "https://raw.githubusercontent.com/Fly0307/harmonyos-ai-skill/zx-dev"
```

### Claude Code CLI (Windows)

```powershell
# Option A — quick copy (simplest)
git clone -b zx-dev https://github.com/Fly0307/harmonyos-ai-skill.git $HOME\src\harmonyos-ai-skill
New-Item -ItemType Directory -Force $HOME\.claude\skills | Out-Null
Copy-Item -Recurse $HOME\src\harmonyos-ai-skill\harmonyos-development $HOME\.claude\skills\
Copy-Item -Recurse $HOME\src\harmonyos-ai-skill\harmony-hdc-ui-automation $HOME\.claude\skills\

# Option B — symlink (recommended: needs admin or "Developer Mode" enabled)
git clone -b zx-dev https://github.com/Fly0307/harmonyos-ai-skill.git $HOME\src\harmonyos-ai-skill
New-Item -ItemType Directory -Force $HOME\.claude\skills | Out-Null
New-Item -ItemType SymbolicLink -Path $HOME\.claude\skills\harmonyos-development -Target $HOME\src\harmonyos-ai-skill\harmonyos-development
New-Item -ItemType SymbolicLink -Path $HOME\.claude\skills\harmony-hdc-ui-automation -Target $HOME\src\harmonyos-ai-skill\harmony-hdc-ui-automation

# Option C — project-local only
Set-Location <your-harmonyos-project-root>
New-Item -ItemType Directory -Force .claude\skills\harmonyos-development | Out-Null
Invoke-WebRequest -Uri "$env:RAW/harmonyos-development/SKILL.md" -OutFile .claude\skills\harmonyos-development\SKILL.md
```

> **Enable Developer Mode (one-time):** Settings → Privacy & security → For developers → toggle "Developer Mode" on. After that, `New-Item -ItemType SymbolicLink` no longer needs admin.

### OpenAI Codex project installation (Windows)

```powershell
py $HOME\src\harmonyos-ai-skill\scripts\install_skills.py `
  --project <your-harmonyos-project-root> `
  --mode link
```

Change `link` to `copy` if Windows cannot create symbolic links. Automation
commands use `uv run python ...`; no fixed `.venv\Scripts\python.exe` path is
required.

### Cursor (Windows)

```powershell
# Recommended: modern .mdc rule
New-Item -ItemType Directory -Force .cursor\rules | Out-Null
Invoke-WebRequest -Uri "$env:RAW/dist/cursor/harmonyos.mdc" -OutFile .cursor\rules\harmonyos.mdc

# Or: legacy single-file rules
Invoke-WebRequest -Uri "$env:RAW/dist/cursor/.cursorrules" -OutFile .cursorrules
```

### GitHub Copilot (Windows)

```powershell
New-Item -ItemType Directory -Force .github | Out-Null
Invoke-WebRequest -Uri "$env:RAW/dist/copilot/copilot-instructions.md" -OutFile .github\copilot-instructions.md
```

### Windsurf / Codeium (Windows)

```powershell
Invoke-WebRequest -Uri "$env:RAW/dist/windsurf/.windsurfrules" -OutFile .windsurfrules
```

### Continue.dev (Windows)

```powershell
New-Item -ItemType Directory -Force .continue\rules | Out-Null
Invoke-WebRequest -Uri "$env:RAW/dist/continue/harmonyos.md" -OutFile .continue\rules\harmonyos.md
```

### AGENTS.md standard (Codex CLI / opencode / Amp / Aider) (Windows)

```powershell
Invoke-WebRequest -Uri "$env:RAW/dist/agents-md/AGENTS.md" -OutFile AGENTS.md
```

Global paths (PowerShell):
| Tool | Path |
|---|---|
| OpenAI Codex CLI | `$HOME\.codex\AGENTS.md` |
| sst/opencode | `$HOME\.config\opencode\AGENTS.md` |
| Amp | `$HOME\.config\amp\AGENTS.md` |

### Google Gemini CLI (Windows)

```powershell
# Project-level
Invoke-WebRequest -Uri "$env:RAW/dist/gemini-cli/GEMINI.md" -OutFile GEMINI.md

# Global
New-Item -ItemType Directory -Force $HOME\.gemini | Out-Null
Invoke-WebRequest -Uri "$env:RAW/dist/gemini-cli/GEMINI.md" -OutFile $HOME\.gemini\GEMINI.md
```

### Ollama local LLM (Windows)

```powershell
# 1. Pull the model
ollama pull qwen3-coder

# 2. Download the system prompt
Invoke-WebRequest -Uri "$env:RAW/dist/system-prompt/system.txt" -OutFile system.txt

# 3. One-liner launch
ollama run qwen3-coder --system (Get-Content system.txt -Raw)

# Or: bake into a custom Modelfile
@"
FROM qwen3-coder
SYSTEM ```"
$(Get-Content system.txt -Raw)
```"
"@ | Set-Content Modelfile
ollama create harmonyos-coder -f Modelfile
ollama run harmonyos-coder
```

### Anthropic SDK Python (cross-platform, identical)

Python code is identical on Windows and macOS/Linux. See the [Anthropic section above](#anthropic--openai--any-llm-api).

</details>

> **Common pitfall:** PowerShell error `'curl' is not recognized as a cmdlet`?
> In Windows PowerShell, `curl` is an alias for `Invoke-WebRequest` but **the arguments are NOT compatible**. Use the `Invoke-WebRequest` commands above instead of `curl`.

---

## How activation differs by tool

| Tool category | Trigger mechanism | Always on? |
|---|---|---|
| **Claude Code / Agent SDK** | LLM reads skill `description` and decides whether to load for this turn | No — on-demand, saves context |
| **Cursor `.mdc`** | Glob pattern matches current file | Scoped to `.ets` / HarmonyOS config files |
| **Cursor `.cursorrules`, `.windsurfrules`, Copilot instructions, AGENTS.md, GEMINI.md, Continue / Cline rules** | Always prepended to every turn inside the project | Yes |
| **ChatGPT / Gemini Custom Instructions** | Always prepended to every conversation for that account | Yes |
| **Per-conversation paste / API `system`** | Only the conversations where you paste | Per-call |

**Rule of thumb:** for HarmonyOS-only projects, use the "always-on" rule files. For mixed repos (e.g. you have both Android and HarmonyOS code), prefer Cursor's scoped `.mdc` or Claude Code's description-based loading.

---

## Verifying it works

Ask the AI:

> *"Explain `@ObjectLink` in ArkUI and when to use it instead of `@State`."*

The answer is **properly primed** if it mentions:

- ✅ You must mark the class with `@Observed` for `@ObjectLink` to work
- ✅ `@State` on an array of objects only reacts to array mutations (push/splice/reassign), not per-item property changes
- ✅ Wrap items with `@Observed` + use `@ObjectLink` in the row component
- ✅ Or reassign the whole object to trigger a rerender

If the answer is vague or generic TS / React-like ("use a state hook"), the knowledge is **not loaded**.

Other good probes:

- "What's the difference between FA model and Stage model?"
- "How do I declare and request runtime permissions in HarmonyOS?"
- "Which Kit do I use for HTTP requests?"
- "How do I build a service card (服务卡片)?"

---

## Repository layout

```
harmonyos-ai-skill/
├─ .gitignore
├─ LICENSE
├─ README_EN.md
├─ harmonyos-development/
│  ├─ SKILL.md                          ← Lightweight topic router
│  ├─ agents/openai.yaml
│  ├─ references/                       ← 19 on-demand knowledge modules
│  ├─ recipes/                          ← Build diagnosis and code review workflows
│  ├─ examples/                         ← Permission and LazyForEach examples
│  └─ evals/cases.yaml                  ← Skill behavior regression cases
├─ harmony-hdc-ui-automation/
│  ├─ SKILL.md                          ← HDC, UiTest, and UI automation workflow
│  ├─ agents/openai.yaml
│  ├─ assets/harmony-hdc.example.json
│  ├─ references/official-ui-automation-notes.md
│  └─ scripts/harmony_hdc_ui.py
├─ scripts/
│  ├─ build_dist.py                     ← Cross-platform dist build/check
│  ├─ build-dist.sh                     ← POSIX compatibility wrapper
│  ├─ check-frontmatter.py              ← Metadata length and route validation
│  └─ install_skills.py                 ← Links or copies both skills
├─ tests/                               ← Builder, CLI, and installer unit tests
├─ .github/workflows/test.yml           ← macOS/Windows/Linux CI
├─ dist/                                ← Generated — do not edit by hand
│  ├─ claude-code/harmonyos-development/SKILL.md
│  ├─ claude-code/harmony-hdc-ui-automation/SKILL.md
│  ├─ cursor/harmonyos.mdc
│  ├─ cursor/.cursorrules
│  ├─ copilot/copilot-instructions.md
│  ├─ windsurf/.windsurfrules
│  ├─ continue/harmonyos.md
│  ├─ cline/custom-instructions.md
│  ├─ agents-md/AGENTS.md
│  ├─ agents-md/AGENTS.full.md
│  ├─ gemini-cli/GEMINI.md
│  ├─ plain/harmonyos-knowledge.md
│  └─ system-prompt/system.txt
└─ README.md
```

**Two skills, one repository workflow:**

1. Edit `harmonyos-development/` or `harmony-hdc-ui-automation/` according to its responsibility
2. Run `python scripts/build_dist.py`
3. Run `python -m unittest discover -s tests -v`
4. Run `python scripts/build_dist.py --check`
5. Commit both the source and regenerated `dist/`

---

## Updating to the latest version

```bash
cd /path/to/your/clone
git pull
python scripts/build_dist.py
# then re-copy whichever file your tool reads
```

If you installed via `ln -s`, you only need `git pull` — the symlink picks up changes automatically.

---

## Authoring your own skill

The source format is Claude Code's `SKILL.md` — YAML frontmatter plus a Markdown body:

```markdown
---
name: my-skill-name
description: >
  First sentence: what domain this skill covers.
  Then an exhaustive list of trigger phrases the AI might match:
  keywords, API names, command names, user questions, synonyms.
---

# My Skill

## When to apply this skill
- Bullet list of concrete scenarios

## Reference
Dense, cite-able reference material: tables, code snippets, API signatures,
rules, gotchas. Avoid prose filler. Favour bullets and compact examples.
```

### Guidelines

- **Focused** — one domain per skill. Don't combine HarmonyOS + iOS + Android.
- **Dense** — cut every sentence that doesn't teach the AI something it can cite.
- **Trigger-rich but concise** — cover the important user phrasings in `description` while staying within 1,024 characters.
- **Actionable** — prefer concrete code/config snippets over abstract explanations.
- **Honest about gaps** — if a feature is deprecated, say so. If you don't have data, leave it out.

After editing a source skill, run `python scripts/build_dist.py` to regenerate
every tool-specific drop-in under `dist/`. macOS/Linux users may continue to
use `./scripts/build-dist.sh`.

---

## Troubleshooting

**The AI still gives generic TypeScript/React answers.**
- Confirm the file landed in the right path (see table in *Supported AI tools*).
- For Claude Code, run *"What skills are available?"* — if `harmonyos-development` isn't listed, restart Claude Code or check `~/.claude/skills/` directly.
- For project-rule tools (Cursor, Copilot, etc.), make sure you're editing files **inside the repo** where the rule file lives. Rules don't apply outside the repo.
- For paste-based tools (ChatGPT, DeepSeek, …), the system prompt is per-conversation; start a **new chat** after pasting.

**Rule file is too long for the tool's context limit.**
Native skill runtimes and `dist/agents-md/AGENTS.md` do not load the full knowledge base at once: the root router selects only the required references, recipes, or examples. Single-file outputs such as `dist/plain/` intentionally embed everything; for strict context limits, use the native skill package or lightweight `AGENTS.md` instead of manually damaging source references.

**`curl` fails with 404.**
The branch in the URL may have moved. Check `https://github.com/Fly0307/harmonyos-ai-skill/branches` and update `$RAW` accordingly.

**How do I update after the upstream repo changes?**
See the *Updating to the latest version* section above.

---

## License & contributing

Licensed under the **MIT License** — use it freely in personal and commercial projects.

Contributions welcome:
1. Fork the repo
2. Edit the relevant source skill; do not edit `dist/` directly
3. Run `python -m unittest discover -s tests -v`
4. Run `python scripts/build_dist.py`, then verify with `--check`
5. Commit the source and matching `dist/`, then open a PR

Factual corrections, new gotchas, updated API names, and translations of the description field (for better trigger matching) are all welcome.
