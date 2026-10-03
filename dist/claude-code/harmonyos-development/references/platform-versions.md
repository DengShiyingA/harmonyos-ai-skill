# Platform Versions and Release Baselines

## Overview

Covers HarmonyOS 6.1 (API 23, stable) / 6.1.1 (API 24, Release) / HarmonyOS 7 (API 26.0.0, Release) / NEXT native app development — the Huawei mobile OS family that runs independently of Android (AOSP-free since HarmonyOS NEXT, released 2024). Primary language is **ArkTS** (a strict, statically-checked superset of TypeScript) and the primary UI framework is **ArkUI** (declarative, state-driven). Use API 26.0.0 Release for new projects and upgrades; keep API 24 Release as a compatibility baseline when the product still supports older devices.

## Contents
- Platform snapshot
- What's new in API 23 (HarmonyOS 6.1)
- What's new in API 24 (HarmonyOS 6.1.1 Release)
- HarmonyOS 7 / API 26.0.0 Release (latest official version)
- API 26 release behavior-scope and upgrade notes

Load this file only when the user request matches these topics. For newer SDK claims, verify against official Huawei documentation when current accuracy matters.

## Official Source Lookup

- Huawei Developer Docs: `https://developer.huawei.com/consumer/cn/doc/`
- HarmonyOS guide pages: use page-specific docs under `developer.huawei.com/consumer/cn/doc/harmonyos-guides/...`; do not open the prefix as a standalone URL.
- HarmonyOS API reference pages: use page-specific docs under `developer.huawei.com/consumer/cn/doc/harmonyos-references/...`; do not open the prefix as a standalone URL.
- Context7 Library IDs: `/websites/developer_huawei_consumer_cn_doc`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-guides`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-references`
- Suggested query keywords: `HarmonyOS SDK release notes, API version, DevEco Studio release, HarmonyOS NEXT, API 23, API 24, API 26`

Use the local notes below as a snapshot. For latest/current SDK behavior, exact API signatures, permission policy, or deprecation status, verify against Huawei official docs or Context7 before answering.

## Platform snapshot

| Item | Value |
|---|---|
| OS | **HarmonyOS 6.1** (stable, released 2026/04/20, API 23). **HarmonyOS 6.1.1** (Release, released 2026/05/26, API 24). **HarmonyOS 7 / 26.0.0 Release** (latest official version, API 26). Pure HarmonyOS, AOSP-free |
| Language | **ArkTS** (primary), **Cangjie** (beta), C/C++ via NAPI |
| UI framework | **ArkUI** declarative (ArkUI-X for cross-platform) |
| Compiler | **ArkCompiler** — AOT to native machine code; LiteActor concurrency |
| Package manager | **ohpm** — `oh-package.json5`; registry at DevEco Service (OHPM Central) |
| IDE | **DevEco Studio 26.0.0 Release** (26.0.0.821; API 26). DevEco Studio 6.1.1 Release (6.1.1.280; API 24 compatibility) |
| App model | **Stage model** (FA model is legacy — don't use in new apps) |
| Packaging | HAP (entry/feature), HSP (shared package), HAR (static archive), atomic .app |
| Recommended API | **Use API 26.0.0 Release for new work and upgrades. Keep API 24 Release as `compatibleSdkVersion` when older-device support is required.** |
| Sample catalog | https://developer.huawei.com/consumer/cn/samples/ |

**Release timeline (recent):**
- HarmonyOS 6.0.1(21) — 2025/11/25 (initial stable with Mate 80 series)
- HarmonyOS 6.0.2(22) — 2026/01/23 (incremental update)
- HarmonyOS 6.0.0.328 Pollen Beta(23) — 2026/02/28 (closed beta, 25 models)
- HarmonyOS 6.1(23) — 2026/04/20 (stable general release)
- HarmonyOS 6.1.1(24) Beta 1 — 2026/04/30 (developer beta)
- HarmonyOS 6.1.1(24) Release — 2026/05/26 (API 24 Release; DevEco Studio 6.1.1.280)
- HarmonyOS 7 / 26.0.0 Beta1 — 2026/06/12 (API 26 developer preview; DevEco Studio 26.0.0.461)
- HarmonyOS 7 / 26.0.0 Release — 2026/08 (API 26 official release; DevEco Studio 26.0.0.821)


### What's new in API 23 (HarmonyOS 6.1)

**ArkUI enhancements:**
- `Navigation` supports binding the routing stack to the component itself and specifying a `NavDestination` as the navigation bar (home page) — no more separate root container needed
- `Menu` adds `anchorPosition` property: control popup position relative to upper-left of anchor with horizontal/vertical offsets
- `Image` component improved SVG parsing capabilities
- Batch of new C APIs for attribute styles (Native side)

**New C-side capabilities (Native/NAPI):**
- UDMF (Unified Data Management Framework) C APIs
- Component drag-and-drop C APIs
- Cryptographic algorithm C APIs

**Data:**
- `relationalStore` enhanced `sendable` function — better cross-thread data passing

**Graphics & AI:**
- AI super frame feature in Graphics Accelerate Kit (frame interpolation for smoother animations)

**ArkWeb:** further capability enhancements (intercept/cookies)


### What's new in API 24 (HarmonyOS 6.1.1 Release)

**Version baseline:** API 24 is now a Release SDK (not only Beta). Use DevEco Studio 6.1.1 Release (6.1.1.280), HarmonyOS SDK 6.1.1 Release, Hvigor 6.24.2, ohpm 6.1.2.268, and Node.js 18.20.1 for API 24 projects.

**Release additions over Beta1:**
- **Ability Kit** — `AbilityStage` adds callbacks before the first Ability is created and when a process starts from an application snapshot.
- **ArkTS** — adds `enableLocalHandleDetection` to keep EventHandler/libuv tasks inside the intended scope and avoid leaks; XML parsing adds `XmlSAXHandler` callbacks for SAX-style parsing.
- **ArkWeb** — download completion callbacks can retrieve the original URL and referrer URL.
- **Call Service Kit** — enterprise call service lookup for incoming/outgoing phone numbers.
- **Camera Kit professional controls** — flash-state event subscribe/unsubscribe; OIS query/set; lens focal length/equivalent focal length/min focus distance/distortion/intrinsic calibration/sensor size/pixel array/color-filter data; logical camera composition; auto/manual exposure; manual focus; ISO; physical aperture.
- **CANN Kit** — large-language-model inference acceleration APIs on PC devices.
- **MDM Kit** — manage hidden settings entries for the current user.

**Beta1 additions still relevant in API 24 Release:**
- **Camera Kit "Follow the Person"** — automatic camera tracking API that keeps a person centered in frame via real-time crop/zoom. Useful for video calls, workout recording, vlogging:
  ```ts
  // Conceptual API — full signature in official docs
  cameraSession.enableSubjectTracking(camera.TrackingMode.PERSON);
  ```
- **Delayed preview output** — add delayed preview directly to the stream pipeline instead of normal preview output, and configure its Surface separately.
- **ArkTS VM diagnostics** — heap information per VM thread, heap-warning callbacks after GC, and `taskpool.execute()` timeout settings.
- **ArkUI** — parallel-window state query, custom component migration across Ability instances, dynamic layout container, root node lookup for `UIContext`, async drag-drop decisions, `onNeedSoftkeyboard`, Canvas/OffscreenCanvas `antialias`, Tabs nested scrolling, multiline ellipsis modes (`MULTILINE_START`, `MULTILINE_CENTER`).
- **ArkWeb** — User-Agent Client Hints, default context-menu switch, URL whitelist and load/jump security controls.
- **Audio Kit** — independent audio session strategy/behavior for capture/rendering, plus OH_MIDI C APIs for USB/BLE MIDI devices.
- **New/expanded Kits** — Content Embed Kit, Enterprise Threat Protection Kit, FAST Kit, NearLink Kit, Network Boost Kit, Screen Time Guard Kit, Device Security Kit, Desktop Extension Kit.
- **DevEco Studio** — API 24 projects, Hot Reload for C++ and resource edits, expanded AppFreeze parsing, ComMemory UI memory analysis, `strictCheckerOnly` for faster strict syntax checks.


### HarmonyOS 7 / API 26.0.0 Release

**Status (official release notes checked 2026/10/03):** 26.0.0 is the latest HarmonyOS version and the corresponding API for HarmonyOS 7. Use it as the default baseline for new projects and upgrades. The official release notes separate Release, Beta2, and Beta1 changes; do not describe 26.0.0 as preview material. Keep API 24 as a compatibility target when the product still supports older devices.

**Release toolchain:** DevEco Studio **26.0.0 Release (26.0.0.821)**, HarmonyOS **26.0.0 Release SDK**, HarmonyOS Emulator **26.0.0.400**, Hvigor/hvigorw **6.26.4**, ohpm **26.0.0.630**, Node.js **24.14.1**, and hstack **6.1.0**. Use `compileSdkVersion: "26.0.0"`; `targetSdkVersion` must be between `compatibleSdkVersion` and `26.0.0`, with the earliest compatible version listed by Huawei as `4.0.0(10)`.

Official release entry points: [26.0.0 version overview](https://developer.huawei.com/consumer/cn/doc/doccenter-release-notes/2600), [upgrade and adaptation guide](https://developer.huawei.com/consumer/en/doc/harmonyos-releases/upgrade-adaptation), and [DevEco Studio 26.0.0 release notes](https://developer.huawei.com/consumer/en/doc/harmonyos-releases/deveco-studio-new-features-2600).

**Version-number rule:** Starting with API **26.0.0**, HarmonyOS developer kit API versions use SemVer (`X.Y.Z`) instead of the legacy `X.Y.Z(N)` format. `X` means a major version with substantial capabilities or adaptation-impacting changes, `Y` means a minor version with new capabilities, and `Z` means compatible fixes/small improvements.

**High-value API 26 changes carried into the Release SDK:**
- **Ability Kit** — AgentCard support; ArkTS script-based app Skill development; package-name + clone-index app name lookup; ArkTS APIs for script management; C APIs for `ModularObjectExtensionAbility`.
- **Accessibility Kit** — system care mode integration for elder-friendly app experiences.
- **Accessory Kit** — new Kit for accessory wake-up, system service linkage, on-demand scheduling, and secure trust management.
- **Account Kit** — `LoginWithHuaweiIDButton` supports custom multilingual text and loading animation.
- **AR Engine** — C API camera flash control; ArkTS preview stream image access; 3D Gaussian model loading; ArkTS/C APIs for external camera and sensor data.
- **ArkUI / UI Design** — system material configuration for Toggle, Tips, Toast, dialogs, menus, popups, custom dialogs, half modals, and Popup; component-level immersive light perception; global reuse pools for `@Reusable` / `@ReusableV2`; standard floating windows; title-area customization updates.
- **ArkWeb** — Chromium kernel upgraded from 132 to 144; new security configuration options.
- **AVCodec Kit** — H.265 hardware encoder CBRHQ mode; Audio Vivid encoding and C APIs.
- **AVSession Kit** — new extra-key enum values for scenario-specific AVSession metadata.
- **Background Tasks Kit** — reminder countdown instances add `repeatInterval` and `repeatCount`.
- **Core File Kit** — `UNCACHE` open option, recursive `listFileExt`, mmap-based file mapping, and sharing an app sandbox directory as system-visible.
- **Core Vision Kit** — image super-resolution and semantic text search over images.
- **Data Augmentation Kit** — mail intelligence handler for classification, summarization, and todo extraction.
- **Device Security Kit** — enhanced Star Shield confidential risk-control engine, unified risk-control credentials, privacy policy controls for camera/microphone/location, and file-event subscription/filtering.
- **Driver Development Kit** — query external USB hubs and develop user-mode drivers.
- **Enterprise Data Guard Kit** — file classification policy APIs `getPolicy` and `isKia`.
- **Enterprise Space Kit** — query dual-space state and determine whether the workspace is enterprise space.
- **FAST Kit** — real-number FFT and inverse FFT; intelligent sequence prediction.
- **Graphics Accelerate Kit** — game prelaunch feature to improve startup experience.
- **Image Kit** — metadata classes for GIF/JFIF/TIFF/PNG/AVIS plus XMP metadata.
- **Input Kit** — keyboard and mouse input event injection.
- **Live View Kit** — auxiliary-area template with percentage progress ring.
- **NDK / JSVM** — create `ArrayBuffer` from external memory.
- **NearLink Kit** — `startScan` scans all discoverable nearby NearLink devices.
- **Network Boost Kit** — `netBoost.setDataFlowDesc` sets flow descriptions from five-tuple data.
- **Notification Kit** — stronger notification management/display, including half-modal notification settings entry.
- **Online Authentication Kit** — DID (Decentralized Identifier) key generation, credential import/query/delete, and data signing.
- **PDF Kit** — convert specified regions across multiple pages into one image.
- **Performance Analysis Kit** — gray release fault-log collection and HiAppEvent app-freeze warning subscriptions.
- **Preview Kit** — file acceleration scanning, preload strategy customization, availability query, and file-operation event reporting.
- **Push Kit** — Live View push messages support Wearable devices.
- **Remote Communication Kit** — `HttpVersionSelectCallback` for HTTP version selection, `HMS_Rcp_SetRequestGetDataCallback()` for streaming upload, `HMS_Rcp_SetFormOrder()` for ordered forms, and QUIC C API.
- **Scenario Fusion Kit** — scenario sharing Button supports image, video, and text.
- **Share Kit** — phone-to-PC/2in1/tablet tap sharing can expose tap position on the receiving side.
- **Spatial Recon Kit** — 3DGS gaussian editing and spatial photo generation from a single photo.
- **Scan Kit** — query support for default/custom scan UI on the current device.

**Release-only additions and upgrade signals:**
- **ArkUI** — `ComposeTitleBarV2` and related title-area APIs are available from 26.0.0; immersive material and container/reuse capabilities should be checked against the installed Release SDK before use.
- **Accessibility Kit** — senior-mode status can be queried and observed with `isSeniorModeEnabled`, `onSeniorModeStateChange`, and `offSeniorModeStateChange`.
- **Media Kit** — `videoProcessing` adds `createVideoProcessor`, status callbacks, and AI HDR status; `AVDownloaderManager.setRequestTimeout` uses the `timeout` parameter name.
- **Notification Kit** — 26.0.0 adds explicit error codes for notification publishing and distributed-state queries; handle `BusinessError` codes rather than assuming every publish succeeds.
- **DevEco Studio** — the Release toolchain adds API-version distribution when creating projects, external USB/virtual cameras and network-disconnection simulation in the emulator, emulator CLI UI actions, coredump/HWASan diagnostics, incremental coverage, `deduplicateSo`, merged HAR packaging, multi-target dependencies, and the `arktsdoc` generator.

**API 26 behavior and UX changes to watch during adaptation:**
- **Ability Kit** — public package-change common events (`COMMON_EVENT_PACKAGE_ADDED`, `REMOVED`, `CHANGED`, `CACHE_CLEARED`) add controls for In-House apps when `targetSdkVersion >= 26.0.0`; In-House apps must configure `allowListenBundleChangedEvent` in `app.json5` for third-party listeners.
- **ArkTS / JSVM** — Chromium/V8 core upgrades 132 → 144; async function type detection is fixed; Wasm jitless default behavior changes; `fastConvertToJSObject` now preserves sibling text nodes when parsing XML.
- **ArkUI** — `NodeAdapter.onAttachToNode`, mouse `rawDeltaX/rawDeltaY`, `LayoutPolicy.matchParent`, `EmbeddedComponent` focus, `WithTheme`, `queryNavDestinationInfo`, `NODE_SWIPER_EVENT_ON_CONTENT_DID_SCROLL`, and shadow blur radius behavior have adaptation-impacting changes.
- **Permissions** — `ohos.permission.READ_IMAGEVIDEO`, `getUidRxBytes`, `getUidTxBytes`, and general permission policy behavior change under API 26 rules.
- **UX** — form controls minimum touch target changes from 28vp to 32vp for Button/Button-style Toggle/Select/Chip/ChipGroup; built-in text line breaking and small-language line height are optimized; Dialog, Toast, AlphabetIndexer, and text selection menu enable immersive system material by default. Disable globally with `metadata` name `ohos.arkui.UIMaterial.state` value `disable`, or per component with `uiMaterial.Material.empty`.

**API 26 V2 behavior scope:**
- **Always effective after the runtime/system upgrade:** JSVM/ArkWeb Chromium 132 to 144 changes, async-function type correction, XML sibling-text preservation, mouse raw deltas, Stage-only ArkUI API constraints, home `NavDestination` query callbacks, `@ReusableV2` dynamic reuse identifiers, `READ_IMAGEVIDEO` behavior, and small-language font updates.
- **Effective when `targetSdkVersion >= 26.0.0`:** In-House package-event controls, Wasm jitless defaults, `NodeAdapter.onAttachToNode`, leading `CustomSpan`/`ImageAttachment` paragraph behavior, `LayoutPolicy.matchParent`, `EmbeddedComponent` focus, `WithTheme`, Swiper content-scroll events, shadow blur radius, UID traffic queries, permission policy changes, 32vp form-control targets, text-style updates, immersive materials, and half-modal centered-dialog height.

Do not infer the scope of an individual behavior from the summary alone. Check the page-specific compatibility note for the target API before changing production code.

**DevEco Studio 26.0.0 Release additions:**
- AI coding: custom Agent token usage display, conversation rollback, built-in Inline Chat commands such as File Comments and Parameter Validation, `UI Verification` tool, and custom Commands.
- Editing/debugging: API 26.0.0 projects, Load/Unload Modules, ArkUI state-variable relation viewer, Code Scanner resource-leak checks, custom Clang-Tidy, ACL permission requests, 8-breakpoint preview, Car multi-screen emulator, scenario simulation, remote emulator control, Native debug startup acceleration, device projection, SQL-highlight database debugging, dump-file stack parsing, HiLog tag filtering, AppAnalyzer report diagnosis, and diagnostics for OOM/app-freeze/resource leaks.
- Build/release: `apiCompatibilityCheck`, `tsImportSoCheck`, module `nativeLib.enableSoDirCollection`, `syncNative`, Hvigor `getAllDependencyInfo`, AppGallery package re-signing, Linux emulator support, and ohpmrc `auto_skip_install`, `metadata_cache_effective`, `metadata_cache`, plus exact-version metadata queries.
- Compatibility changes: DevEco Studio and Command Line Tools use Node.js **24.14.1**; custom Hvigor/ohpm/ohpm-repo plugins must be tested on Node.js 24. `ohpm-repo 5.5.1` no longer depends on `node-fetch`; plugins that relied on that bundled dependency must replace it or install `node-fetch@2.7.0` themselves.

**DevEco Testing 26.0.0:**
- Stability testing can target specified entry points to trigger stability issues and expands memory-leak detection coverage.
- UX testing supports multi-device layout comparison across straight-screen and foldable devices.
- Test-service matrix includes local app listing precheck, performance baseline/monitoring, stability baseline, memory-leak testing, UX baseline and multi-device layout comparison, security baseline, power baseline, functional-experience baseline, exploratory testing, regression testing, device projection, UIViewer, app graph management, performance report auto-analysis, and report comparison.

**Upgrade workflow:** If `targetSdkVersion` is omitted, the upgraded DevEco Studio may align it with the matching SDK, and the default `compileSdkVersion` also moves to that SDK. Set `compatibleSdkVersion` deliberately when older devices must remain supported. Use DevEco Studio's **Tools > API Change Assistant** to scan ArkTS/C API behavior changes, then build with the matching Command Line Tools and test on both old and API 26 devices before release.
