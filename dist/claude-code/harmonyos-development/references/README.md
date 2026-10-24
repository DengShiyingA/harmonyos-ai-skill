# HarmonyOS Skill Reference Loading Guide

This directory contains supporting reference files for the `harmonyos-development` skill.

The root `SKILL.md` remains the discovery entry. These files are loaded only when the user request needs deeper guidance.

## Intent routing

| User intent | Read first | Then read |
|---|---|---|
| Version, SDK, DevEco Studio, API baseline | `platform-baseline.md` | `api26-release.md` for HarmonyOS 7 migration |
| DevEco Code/CLI, Agent Framework, app Skill, Intents, A2A | `ai-development-tools.md` | `api26-release.md` for HarmonyOS 7 details |
| ArkTS syntax or TypeScript migration | `arkts-rules.md` | `../examples/*.ets` |
| ArkUI layout, components, rendering | `arkui-components.md` | `state-management.md` |
| Native C/C++ API availability across OS versions | `native-api-compatibility.md` | `build-sign-release.md` |
| NDK/Node-API, TSFN, async work, handle/reference lifetime | `ndk-napi.md` | `native-api-compatibility.md` |
| Stage model lifecycle | `stage-model.md` | `../recipes/debug-build-error.md` |
| Navigation and page stack | `navigation.md` | `state-management.md` |
| State decorators and data flow | `state-management.md` | `arkts-rules.md` |
| Permissions and privacy prompts | `permissions.md` | `../examples/permission-request.ets` |
| Build, CI, signing, packaging, release | `build-sign-release.md` | `platform-baseline.md` |
| Performance and large lists | `performance.md` | `../examples/lazyforeach-list.ets` |

## Production default

Use API 26.0.0 Release for new-project guidance; preserve an existing project's API 24 or other baseline and choose minimum compatibility from device coverage.
