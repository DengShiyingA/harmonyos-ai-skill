# Abilities, Permissions, Background Tasks, and App Entry Points

## Contents
- The Stage model — core concepts
- Component types
- UIAbility lifecycle
- Launching another ability
- module.json5 essentials
- Launch app by type (startAbilityByType)
- Permissions
- Stability — crash types and error handling
- Background Tasks — 4 types
- Security coding rules (from official best practices)
- App continuation (应用接续) — cross-device migration
- Enable continuation in `module.json5`
- Source device — save migration data
- Target device — restore data
- Dynamic migration control
- Cross-device migration with different Ability names
- Prerequisites
- App Linking — deep links & app-to-app navigation
- Configure deep link in module.json5
- Handle incoming link — cold start (onCreate)
- Handle link — app already running (onNewWant)
- Desktop shortcuts (桌面快捷方式)
- 1. Create `resources/base/profile/shortcuts_config.json`
- 2. Register in module.json5
- 3. Route based on shortcut parameter

Load this file only when the user request matches these topics. For newer SDK claims, verify against official Huawei documentation when current accuracy matters.

## Official Source Lookup

- Huawei Developer Docs: `https://developer.huawei.com/consumer/cn/doc/`
- HarmonyOS guide pages: use page-specific docs under `developer.huawei.com/consumer/cn/doc/harmonyos-guides/...`; do not open the prefix as a standalone URL.
- HarmonyOS API reference pages: use page-specific docs under `developer.huawei.com/consumer/cn/doc/harmonyos-references/...`; do not open the prefix as a standalone URL.
- Context7 Library IDs: `/websites/developer_huawei_consumer_cn_doc`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-guides`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-references`
- Suggested query keywords: `UIAbility, AbilityStage, Want, startAbility, permissions, requestPermissionsFromUser, background tasks, app linking, continuation, shortcuts`

Use the local notes below as a snapshot. For latest/current SDK behavior, exact API signatures, permission policy, or deprecation status, verify against Huawei official docs or Context7 before answering.

## The Stage model — core concepts


### Component types

- **UIAbility** — has UI, handles user interaction. Entry points. One instance per task.
- **ExtensionAbility** — background / extension scenarios:
  - `ServiceExtensionAbility` — background services (system apps)
  - `FormExtensionAbility` — home-screen widget (服务卡片)
  - `WorkSchedulerExtensionAbility` — deferred tasks
  - `InputMethodExtensionAbility`, `WallpaperExtensionAbility`, `BackupExtensionAbility`, etc.
- **AbilityStage** — module-level lifecycle container (one per HAP)
- **WindowStage** — window container scoped to a UIAbility


### UIAbility lifecycle

```ts
import { UIAbility, Want, AbilityConstant } from '@kit.AbilityKit';
import { window } from '@kit.ArkUI';

export default class EntryAbility extends UIAbility {
  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void { }
  onDestroy(): void { }
  onWindowStageCreate(windowStage: window.WindowStage): void {
    windowStage.loadContent('pages/Index', (err) => { /* ... */ });
  }
  onWindowStageDestroy(): void { }
  onForeground(): void { }
  onBackground(): void { }
  onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void { }
}
```


### Launching another ability

```ts
import { common, Want } from '@kit.AbilityKit';

const ctx = getContext(this) as common.UIAbilityContext;
const want: Want = {
  bundleName: 'com.example.app',
  abilityName: 'DetailAbility',
  parameters: { id: 42 }
};
ctx.startAbility(want);
// or startAbilityForResult for a return value
```


### module.json5 essentials

```json5
{
  "module": {
    "name": "entry",
    "type": "entry",                // entry | feature | shared
    "srcEntry": "./ets/entryability/EntryAbility.ets",
    "deviceTypes": ["phone", "tablet", "2in1"],
    "abilities": [{
      "name": "EntryAbility",
      "srcEntry": "./ets/entryability/EntryAbility.ets",
      "startWindowIcon": "$media:startIcon",
      "startWindowBackground": "$color:start_window_background",
      "skills": [{
        "actions": ["action.system.home"],
        "entities": ["entity.system.home"]
      }]
    }],
    "requestPermissions": [
      { "name": "ohos.permission.INTERNET" }
    ]
  }
}
```


### Launch app by type (startAbilityByType)

```ts
import { common } from '@kit.AbilityKit';

const context = getContext(this) as common.UIAbilityContext;

// Open navigation app with destination
context.startAbilityByType('navigation', {
  sceneType: 1,
  destinationLatitude: 39.9042,
  destinationLongitude: 116.4074,
  destinationName: 'Beijing',
} as Record<string, Object>);

// Open browser
context.startAbilityByType('browser', {
  uri: 'https://example.com',
} as Record<string, Object>);
```

Supported types: `navigation`, `browser`, `email`, `finance`, `transit`, etc.


### Permissions

Declare in `module.json5` → `requestPermissions`. For user-granted permissions, request at runtime via `abilityAccessCtrl.createAtManager().requestPermissionsFromUser(context, [...])`.


## Stability — crash types and error handling

| Type | Description |
|---|---|
| **JS_ERROR** | ArkTS/JS runtime exceptions (most common) — `TypeError: Cannot read property 'x' of undefined` |
| **CPP_CRASH** | Native C/C++ crash (SIGSEGV, SIGABRT) |
| **APP_FREEZE** | Main thread blocked >6s (ANR equivalent). Root causes: thread locks (57%), system resources (14%), heavy main-thread work (9%) |
| **OOM** | Out-of-memory kill |

**Global error handler:**
```ts
import { errorManager } from '@kit.AbilityKit';

const observer: errorManager.ErrorObserver = {
  onUnhandledException(errMsg: string): void {
    console.error('Uncaught: ' + errMsg);
  },
  onException?(errObject: Error): void {  // API 10+
    console.error(errObject.name + ': ' + errObject.message);
  }
};
const observerId = errorManager.on('error', observer);
```

**Crash event subscription (HiAppEvent):**
```ts
import { hiAppEvent } from '@kit.PerformanceAnalysisKit';

hiAppEvent.addWatcher({
  name: "crashWatcher",
  appEventFilters: [{
    domain: hiAppEvent.domain.OS,
    names: [hiAppEvent.event.APP_CRASH]
  }],
  onReceive: (domain, appEventGroups) => { /* process crash */ }
});
```


## Background Tasks — 4 types

| Type | API | Duration | Use case |
|---|---|---|---|
| **Transient** | `requestSuspendDelay` | ~3 min max | Save data, upload logs |
| **Continuous** | `startBackgroundRunning` | Unlimited (needs notification) | Music, navigation, recording |
| **Deferred** | `workScheduler.startWork` | System-determined | Timed sync, cleanup |
| **Agent Reminders** | `ReminderRequestTimer` | System-managed | Alarms, timers |

**Continuous task example:**
```ts
import { backgroundTaskManager } from '@kit.BackgroundTasksKit';
import { wantAgent, WantAgent } from '@kit.AbilityKit';

// module.json5: "abilities": [{ "backgroundModes": ["audioRecording"] }]
// permission: ohos.permission.KEEP_BACKGROUND_RUNNING

const info: wantAgent.WantAgentInfo = {
  wants: [{ bundleName: 'com.example.app', abilityName: 'MainAbility' }],
  actionType: wantAgent.OperationType.START_ABILITY,
  requestCode: 0, actionFlags: [wantAgent.WantAgentFlags.UPDATE_PRESENT_FLAG]
};
const agent = await wantAgent.getWantAgent(info);
backgroundTaskManager.startBackgroundRunning(
  this.context, backgroundTaskManager.BackgroundMode.AUDIO_RECORDING, agent
);
```

9 background modes: `dataTransfer` · `audioPlayback` · `audioRecording` · `location` · `bluetoothInteraction` · `multiDeviceConnection` · `taskKeeping` (2-in-1 only)

**Deferred task frequency by user activity:** Active=2h, Frequent=4h, Regular=24h, Rare=48h, Never used=prohibited.


## Security coding rules (from official best practices)

1. Set `exported: false` for non-interactive abilities
2. Validate all parameters crossing trust boundaries (Want intents, rpc.RemoteObject)
3. Use parameterized queries — never string concat for SQL
4. Replace HTTP with HTTPS; validate SSL certificates
5. Never store personal data in clipboard
6. Use `Asset Store Kit` for sensitive short data (passwords, tokens)
7. Avoid passing personal data through implicit intents
8. Use code obfuscation for production builds
9. Use precise `InputType` (`.USER_NAME`, `.Password`) for system-level protection
10. Never use debug signatures for production releases

**Permission check + request pattern:**
```ts
import { abilityAccessCtrl, bundleManager } from '@kit.AbilityKit';

// Check
const atManager = abilityAccessCtrl.createAtManager();
const bundleInfo = await bundleManager.getBundleInfoForSelf(
  bundleManager.BundleFlag.GET_BUNDLE_INFO_WITH_APPLICATION);
const status = await atManager.checkAccessToken(
  bundleInfo.appInfo.accessTokenId, 'ohos.permission.CAMERA');

// Step 1 — Request from user
const result = await atManager.requestPermissionsFromUser(context,
  ['ohos.permission.CAMERA', 'ohos.permission.MICROPHONE']);
if (result.authResults[0] === 0) {
  // Granted
} else if (result.dialogShownResults?.[0]) {
  // User saw dialog but denied — show in-app guidance, don't re-pop
} else {
  // Step 2 — Fallback: open settings dialog (user previously denied permanently)
  atManager.requestPermissionOnSetting(context,
    ['ohos.permission.CAMERA']).then((statuses) => {
    // statuses[0]: 0 = granted, -1 = denied
  });
}
```

**Data encryption levels:** EL1 (device-level) → EL2 (user-level, default) → EL3 (accessible while locked) → EL4 (inaccessible when locked)

**Network security config** — HTTPS/certificate pinning for production apps:

Create `src/main/resources/base/profile/network_config.json`:
```json
{
  "network-security-config": {
    "domain-config": [{
      "domains": [{ "include-subdomains": true, "name": "api.example.com" }],
      "trust-anchors": [{ "certificates": "/data/storage/el1/bundle/entry/resources/resfile/ca_cert.pem" }]
    }]
  }
}
```
Reference in `module.json5`: `"metadata": [{ "name": "NetworkSecurityConfig", "resource": "$profile:network_config" }]`.


## App continuation (应用接续) — cross-device migration

Enable cross-device task handoff: migrate UIAbility state from device A to device B.


### Enable continuation in `module.json5`

```json5
{
  "module": {
    "abilities": [{
      "name": "EntryAbility",
      "continuable": true   // enable cross-device migration
    }]
  }
}
```


### Source device — save migration data

```ts
// In UIAbility
onContinue(wantParam: Record<string, Object>): AbilityConstant.OnContinueResult {
  // Save data to migrate (keep under 100KB, use distributed data object for larger data)
  wantParam['currentPage'] = 'DetailPage';
  wantParam['articleId'] = this.articleId;

  // Check target app version compatibility
  const targetVersion = wantParam['version'] as number;
  if (targetVersion < 2) {
    return AbilityConstant.OnContinueResult.MISMATCH;
  }

  return AbilityConstant.OnContinueResult.AGREE;
}
```


### Target device — restore data

```ts
// Cold start
onCreate(want: Want, launchParam: AbilityConstant.LaunchParam) {
  if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
    // Restore migrated data
    this.articleId = want.parameters?.['articleId'] as number;
    // Restore page stack
    this.context.restoreWindowStage(this.storage);
  }
}

// Hot start (single-instance)
onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam) {
  if (launchParam.launchReason === AbilityConstant.LaunchReason.CONTINUATION) {
    this.articleId = want.parameters?.['articleId'] as number;
    this.context.restoreWindowStage(this.storage);
  }
}
```


### Dynamic migration control

```ts
// Disable migration on certain pages
this.context.setMissionContinueState(AbilityConstant.ContinueState.INACTIVE);

// Re-enable when on a migrateable page
this.context.setMissionContinueState(AbilityConstant.ContinueState.ACTIVE);
```


### Cross-device migration with different Ability names

Use `continueType` in `module.json5` to link different Abilities across devices:

```json5
// Device A
{ "name": "PhoneAbility", "continueType": ["myApp_main"] }

// Device B
{ "name": "TabletAbility", "continueType": ["myApp_main"] }
```


### Prerequisites

- Both devices logged into same Huawei Account
- Wi-Fi + Bluetooth enabled (or "Multi-device Collaboration Enhanced" enabled)
- "Settings → Multi-device Collaboration → Continuation" enabled
- App installed on both devices


## App Linking — deep links & app-to-app navigation


### Configure deep link in module.json5

```json5
{
  "module": {
    "abilities": [{
      "name": "EntryAbility",
      "skills": [{
        "entities": ["entity.system.home", "entity.system.browsable"],
        "actions": ["ohos.want.action.home", "ohos.want.action.viewData"],
        "uris": [{ "scheme": "https", "host": "example.com", "path": "/detail" }],
        "domainVerify": true       // enable App Linking verification
      }]
    }]
  }
}
```


### Handle incoming link — cold start (onCreate)

```ts
import { url } from '@kit.ArkTS';

export default class EntryAbility extends UIAbility {
  private targetPage: string = '';
  private linkParams: Record<string, string> = {};

  onCreate(want: Want, launchParam: AbilityConstant.LaunchParam): void {
    this.parseUri(want);
  }

  private parseUri(want: Want): void {
    if (want?.uri) {
      const urlObj = url.URL.parseURL(want.uri);
      this.linkParams = Object.fromEntries(urlObj.params.entries());
      this.targetPage = urlObj.pathname;        // e.g. "/detail"
    }
  }

  onWindowStageCreate(windowStage: window.WindowStage): void {
    const page = this.targetPage === '/detail' ? 'pages/Detail' : 'pages/Index';
    if (this.linkParams['id']) {
      AppStorage.setOrCreate('linkId', this.linkParams['id']);
    }
    windowStage.loadContent(page);
  }
}
```


### Handle link — app already running (onNewWant)

```ts
onNewWant(want: Want, launchParam: AbilityConstant.LaunchParam): void {
  this.parseUri(want);
  if (this.linkParams['id']) {
    AppStorage.setOrCreate('linkId', this.linkParams['id']);
    AppStorage.setOrCreate('newWantFlag', true);   // notify UI to navigate
  }
}
```

Page listens for `newWantFlag` via `@StorageLink` + `@Watch` and navigates accordingly.


## Desktop shortcuts (桌面快捷方式)


### 1. Create `resources/base/profile/shortcuts_config.json`

```json
{
  "shortcuts": [
    {
      "shortcutId": "id_scan",
      "label": "$string:shortcut_scan",
      "icon": "$media:ic_scan",
      "wants": [{
        "bundleName": "com.example.myapp",
        "moduleName": "entry",
        "abilityName": "EntryAbility",
        "parameters": { "shortcutKey": "ScanPage" }
      }]
    }
  ]
}
```


### 2. Register in module.json5

```json5
"abilities": [{
  "name": "EntryAbility",
  "metadata": [{
    "name": "ohos.ability.shortcuts",
    "resource": "$profile:shortcuts_config"
  }]
}]
```


### 3. Route based on shortcut parameter

```ts
// In EntryAbility — onCreate / onNewWant
const shortcutKey = want?.parameters?.shortcutKey as string;
if (shortcutKey === 'ScanPage') {
  AppStorage.setOrCreate('targetPage', 'pages/Scan');
}
```

Page reads `@StorageProp('targetPage')` and navigates accordingly.
