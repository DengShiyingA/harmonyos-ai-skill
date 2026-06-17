# HarmonyOS Skill Reference Loading Guide

This directory contains supporting reference files for the `harmonyos-development` skill.

The root `SKILL.md` remains the discovery entry. These files are loaded only when the user request needs deeper guidance.

## Intent routing

| User intent | Read first | Then read |
|---|---|---|
| Version, SDK, DevEco Studio, API baseline | `platform-baseline.md` | `api26-preview.md` only for preview requests |
| ArkTS syntax or TypeScript migration | `arkts-rules.md` | `../examples/*.ets` |
| ArkUI layout, components, rendering | `arkui-components.md` | `state-management.md` |
| Stage model lifecycle | `stage-model.md` | `../recipes/debug-build-error.md` |
| Navigation and page stack | `navigation.md` | `state-management.md` |
| State decorators and data flow | `state-management.md` | `arkts-rules.md` |
| Permissions and privacy prompts | `permissions.md` | `../examples/permission-request.ets` |
| Build, signing, packaging, release | `build-sign-release.md` | `platform-baseline.md` |
| Performance and large lists | `performance.md` | `../examples/lazyforeach-list.ets` |

## Production default

Use API 24 Release as the production default unless the user explicitly targets HarmonyOS 7 / API 26 preview.
