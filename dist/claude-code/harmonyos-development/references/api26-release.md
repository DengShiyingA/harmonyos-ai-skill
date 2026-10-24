# API 26 Release and Migration

HarmonyOS 7 / API 26.0.0 is Release, confirmed by Huawei's August 2026 developer bulletin. Beta1 and Beta2 are historical versions.

Use this reference for HarmonyOS 7 production development and upgrades from API 24 or earlier.

## Rule

Read `platform-baseline.md` first. An SDK upgrade, target-SDK upgrade, and minimum-supported-device change are separate decisions. Preserve an existing project's settings until the migration impact is assessed.

## Migration workflow

1. Record IDE, SDK, Node.js, compile/target/compatible SDK, and native dependencies.
2. Upgrade using the matched Release tools. Review custom plugins for Node.js 24 compatibility.
3. Use the IDE API Change Assistant and the official API changes to assess deprecated APIs, permissions, UI behavior, and target-dependent changes.
4. Pin the target explicitly. Guard newer ArkTS/C APIs and implement old-device fallbacks; see `native-api-compatibility.md` for native linking.
5. Test startup, fallback paths, permissions, UI, and native calls on both minimum-compatible and API 26 devices. Validate release signing and obfuscation before publishing.

## Newly documented scenarios

- Audio recording: select AudioCapturer or OH_AudioCapturer according to the implementation language; verify authorization, capture scope, and device restrictions for system-audio recording.
- Audio editing: OHAudioSuite provides C/C++ effect nodes. Check supported effects and release every node/resource through its matching API.
- AVSession controller: distinguish controlling another media session from publishing the app's own session. Check access constraints before generating controller code.
- Multi-device adaptation: test wide phones, fold states, split windows, keyboard/mouse interaction, and camera changes using actual container dimensions.

These are documentation entry points, not evidence that every interface was first introduced in API 26. Verify each API's `since` and device support.

Sources: [August bulletin](https://developer.huawei.com/consumer/cn/monthly/202608), [upgrade guide](https://developer.huawei.com/consumer/en/doc/harmonyos-releases/upgrade-adaptation).
