# Platform Baseline

## Default policy

- Current production baseline: HarmonyOS 7 / API 26.0.0 Release (verified 2026-10-24).
- Existing API 24 Release projects remain valid; preserve their configured baseline unless migration is requested.
- New apps should use the Stage model.
- FA model is legacy and should only appear in migration explanations.

## Answering rules

1. Inspect the project SDK settings first. For a new project without settings, use API 26.0.0 Release as the toolchain baseline.
2. Choose `compatibleSdkVersion` from the intended device coverage; compiling with API 26 does not require a minimum device API of 26.
3. Keep `compatibleSdkVersion <= targetSdkVersion <= compileSdkVersion`. Review behavior changes before increasing the target; guard newer calls and provide fallbacks for older devices.
4. For debugging, request or inspect:
   - DevEco Studio version
   - compileSdkVersion
   - compatibleSdkVersion / targetSdkVersion
   - module.json5
   - oh-package.json5
   - full build error log

## Toolchain notes

- API 24 projects must not receive unguarded API 26-only calls.
- API 26 Release toolchain: DevEco Studio / Command Line Tools 26.0.0.821, SDK 26.0.0 Release, Hvigor 6.26.4, ohpm 26.0.0.630, Node.js 24.14.1, Emulator 26.0.0.400, hstack 6.1.0.
- This is a verified Release pairing, not a claim that no newer IDE patch exists. Check official updates before choosing a patch.
- Pin `targetSdkVersion` explicitly during an IDE upgrade: if omitted, it may move to the bundled SDK version and enable new target-dependent behavior.

Sources: [Upgrade guide](https://developer.huawei.com/consumer/en/doc/harmonyos-releases/upgrade-adaptation), [toolchain pairing](https://developer.huawei.com/consumer/en/doc/harmonyos-releases/deveco-studio-new-features-2600).
