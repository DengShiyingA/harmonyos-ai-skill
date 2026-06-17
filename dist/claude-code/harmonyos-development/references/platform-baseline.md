# Platform Baseline

## Default policy

- Production default: HarmonyOS 6.1.1 Release / API 24.
- Preview-only: HarmonyOS 7 / API 26 Beta1.
- New apps should use the Stage model.
- FA model is legacy and should only appear in migration explanations.

## Answering rules

1. If the user does not provide a target SDK, assume API 24 Release for production code.
2. Do not mix API 26-only APIs into API 24 production examples.
3. When discussing API 26, clearly mark it as preview/adaptation-only.
4. For debugging, request or inspect:
   - DevEco Studio version
   - compileSdkVersion
   - compatibleSdkVersion / targetSdkVersion
   - module.json5
   - oh-package.json5
   - full build error log

## Toolchain notes

- API 24 production examples should avoid API 26 preview-only syntax, behavior, or configuration.
- API 26 examples should mention Node.js 24 / newer DevEco Studio only when the user explicitly targets preview adaptation.
