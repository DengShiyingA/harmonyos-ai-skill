---
name: harmony-hdc-ui-automation
description: Use when working in a HarmonyOS project to inspect or control a real HDC-connected device or emulator from the command line, launch or stop the app, capture screenshots, dump the live UI tree, capture/filter hilog logs for debugging, transfer files to or from the current app sandbox, inject UiTest uiInput actions, design ArkTS UiTest cases, or write/run Hypium Python UI automation with the project's UV/.venv Python environment.
---

# Harmony HDC UI Automation

## Core Rule

Run the helper from the target HarmonyOS project root. Use the project environment through the
portable `uv run` form on both macOS and Windows:

```bash
uv run python .agents/skills/harmony-hdc-ui-automation/scripts/harmony_hdc_ui.py doctor
```

Examples in this skill assume a Codex project-local installation under `.agents/skills`. If the
skill is installed in another agent directory such as `~/.claude/skills`, resolve the actual skill
directory and substitute that prefix; do not copy the helper into the application repository.

`uv run` selects the project environment without hard-coding `.venv/bin/python` or
`.venv\Scripts\python.exe`. Use `--active` only when the user explicitly wants the currently
activated `VIRTUAL_ENV`.

Copy `assets/harmony-hdc.example.json` to `.harmony-hdc.json` in the target project and update its
bundle, module, ability, and sandbox paths. Flags override configuration values.

Inside the Codex sandbox, `uv run` may fail on `~/.cache/uv` permissions. If the command is needed for the user request, rerun it with escalation instead of switching to global Python.

## Missing Tool Handling

When a local tool or runtime is missing, do not silently switch to a weaker path. Diagnose first:

```bash
command -v uv
command -v hdc
uv run python .agents/skills/harmony-hdc-ui-automation/scripts/harmony_hdc_ui.py doctor
```

On Windows PowerShell, use `Get-Command uv` and `Get-Command hdc` instead of `command -v`.

If `uv`, `hdc`, DevEco/Hvigor, UiTest command-line support, or Hypium Python packages are missing, read `references/official-ui-automation-notes.md` and suggest the matching install/setup command. Ask before installing packages, downloading SDK/test artifacts, changing shell startup files, or enabling persistent device test mode.

## Continuous Improvement Rule

Prefer extending `scripts/harmony_hdc_ui.py` over repeating raw HDC commands. If the same command pattern is used three or more times in one task, or if it combines multiple fragile steps such as screenshot plus layout dump, add or reuse a script subcommand before continuing long manual testing.

When a command fails because the syntax, path style, option shape, or sandbox behavior is wrong,
record the corrected command and failure trigger. Modify this skill only when its source repository
is inside the user's authorized scope; otherwise report the proposed correction without writing to
the installed skill.

## Coordination With HarmonyOS Development

Use `$harmonyos-development` for ArkTS/ArkUI implementation, project configuration, SDK/API
selection, build failures, and test-code design. Use this skill for connected-device evidence and
execution. Load both for tasks that implement a change and verify it on a device or emulator.

## Workflow

1. Verify device connectivity before acting.

   ```bash
   uv run python .agents/skills/harmony-hdc-ui-automation/scripts/harmony_hdc_ui.py devices
   ```

   If multiple devices are listed, pass `--target <connect-key>` to every script command. The
   helper rejects ambiguous or unknown targets instead of guessing.

2. Launch or stop the app with HDC.

   ```bash
   uv run python .agents/skills/harmony-hdc-ui-automation/scripts/harmony_hdc_ui.py start
   uv run python .agents/skills/harmony-hdc-ui-automation/scripts/harmony_hdc_ui.py stop
   ```

   Pass `--bundle`, `--ability`, or `--module` when overriding `.harmony-hdc.json`.

3. Inspect the real UI before changing tests.

   ```bash
   uv run python .agents/skills/harmony-hdc-ui-automation/scripts/harmony_hdc_ui.py screencap
   uv run python .agents/skills/harmony-hdc-ui-automation/scripts/harmony_hdc_ui.py dump
   uv run python .agents/skills/harmony-hdc-ui-automation/scripts/harmony_hdc_ui.py snapshot --merge-windows
   ```

   Omit output paths to use the host temporary directory portably. Use screenshots for visual
   state and `dumpLayout` JSON for robust selectors. Prefer `snapshot` when both are needed. Prefer
   text, id, type, description, or bundle filters over hard-coded coordinates.

4. Capture hilog when a UI action fails, data looks stale, navigation is unexpected, or native/cloud/model behavior needs attribution.

   ```bash
   uv run python .agents/skills/harmony-hdc-ui-automation/scripts/harmony_hdc_ui.py hilog-clear
   uv run python .agents/skills/harmony-hdc-ui-automation/scripts/harmony_hdc_ui.py hilog-tail --lines 500 --type app --level D --regex "Exception|Error" --out artifacts/harmony-hilog.txt
   uv run python .agents/skills/harmony-hdc-ui-automation/scripts/harmony_hdc_ui.py hilog-tail --lines 300 --type app --pid <pid> --out artifacts/harmony-app-hilog.txt
   ```

   Use hilog with screenshot/layout evidence: first capture or clear the focused log window, perform the UI action, then save filtered logs. Prefer `--out` for large logs so the final response can summarize evidence instead of pasting noisy output. Ask before receiving full `/data/log/hilog` disk logs because they can be large and may contain private data.

5. Pull or update app sandbox files when debugging stateful behavior.

   ```bash
   uv run python .agents/skills/harmony-hdc-ui-automation/scripts/harmony_hdc_ui.py file-ls
   uv run python .agents/skills/harmony-hdc-ui-automation/scripts/harmony_hdc_ui.py file-send fixtures/example.json
   uv run python .agents/skills/harmony-hdc-ui-automation/scripts/harmony_hdc_ui.py file-recv /data/storage/el2/base/haps/entry/files/config.json artifacts/config.json
   ```

   Resolve the bundle and default app-files directory from `.harmony-hdc.json`. Ask before
   overwriting device files or pulling large/private data.

6. Use command-line UI control only for exploration or simple smoke checks.

   ```bash
   uv run python .agents/skills/harmony-hdc-ui-automation/scripts/harmony_hdc_ui.py click 540 1800
   uv run python .agents/skills/harmony-hdc-ui-automation/scripts/harmony_hdc_ui.py swipe 540 1900 540 600
   uv run python .agents/skills/harmony-hdc-ui-automation/scripts/harmony_hdc_ui.py text "hello"
   uv run python .agents/skills/harmony-hdc-ui-automation/scripts/harmony_hdc_ui.py key BACK
   ```

   Ask before injecting actions that could delete data, send messages, purchase items, grant permissions broadly, or affect another user's account.

7. For repeatable UI assertions, write ArkTS UiTest cases under `entry/src/ohosTest/ets/test/` and run them with the project Hvigor test flow. Use `$harmony-hvigor-unit-test` when compiling/running those tests.

8. For host-side Python automation, write Hypium Python cases with `TestCase`, `UiDriver`, and
   `BY` selectors, then run them through the project UV environment. Keep Python dependencies in
   the project environment, not global Python, and confirm that the Hypium package matches the
   target DevEco/HarmonyOS release.

## Official Notes

Read `references/official-ui-automation-notes.md` when writing or modifying test cases, when explaining official API behavior, or when choosing between HDC command-line control, ArkTS UiTest, and Hypium Python.

## Practical Defaults

- Use `hdc list targets` before acting; use `hdc -t <SN>` when more than one device is connected.
- Put common project values in `.harmony-hdc.json`; use command flags only for overrides.
- Pass common options either before or after the subcommand.
- Use `--timeout <seconds>` when a device or network transport needs a longer command window.
- Start the app with `aa start -a <abilityName> -b <bundleName> -m <moduleName>`.
- Stop the app with `aa force-stop <bundleName>`.
- Capture screenshots with `uitest screenCap -p /data/local/tmp/<file>.png`, then pull with `hdc file recv`.
- Dump the UI tree with `uitest dumpLayout -p /data/local/tmp/<file>.json`.
- Use `snapshot --prefix <path>` when a task repeatedly needs both screenshot and UI tree.
- Use `hilog-clear` before focused reproductions and `hilog-tail --out <file>` after the action to capture debuggable evidence.
- Transfer app files with `hdc file send/recv -b <bundleName>`; use `hdc shell -b <bundleName>` for `ls`, `mkdir`, and other sandbox inspection.
- For directory pulls, a remote path ending with `/` means pull the directory contents into the local destination directory.
- Inject exploratory actions with `uitest uiInput`, but convert important flows into ArkTS UiTest or Hypium Python tests.
