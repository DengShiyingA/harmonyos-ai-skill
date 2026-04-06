---
name: harmonyos-development
description: >
  1400+ lines of production-ready HarmonyOS 6.0.2(22) / NEXT (鸿蒙) development knowledge.
  Covers: ArkTS strict-mode rules & 10 perf coding rules, ArkUI declarative UI (7 lifecycle
  callbacks, 6 layout containers with perf ranking, LazyForEach + @Reusable 69% faster),
  state management V1 (@State/@Prop/@Link/@Observed/@ObjectLink) + V2 (@ComponentV2/@Local/
  @ObservedV2/@Trace/@Monitor) + StateStore global state, NavPathStack full API with route
  interception, animation (animateTo/geometryTransition/spring), HarmonyOS 6.0 visual effects
  (液态玻璃/BlurStyle 13 values/backgroundEffect/systemMaterialEffect/pointLight), 50+ Kit
  catalog with import keys, concurrency (TaskPool/TaskGroup/Worker/@Concurrent/@Sendable 100x
  faster), crash handling (JS_ERROR/CPP_CRASH/APP_FREEZE/ErrorObserver/HiAppEvent), 4 background
  task types, 10 security coding rules, arkxtest testing (JsUnit 16+ assertions/UiTest), multi-device
  responsive layout (breakpoints/GridRow), DevEco Studio 6.0.2 setup, OHPM, ArkCompiler, Cangjie.
  All extracted from official Huawei documentation with 80+ verified reference URLs.

  Trigger keywords (EN): HarmonyOS, HarmonyOS NEXT, HarmonyOS 6.0.2, API 22, ArkTS, ArkUI,
  .ets file, DevEco Studio, Stage model, UIAbility, ExtensionAbility, AbilityStage, WindowStage,
  @State, @Prop, @Link, @Provide, @Consume, @Observed, @ObjectLink, @Watch, @Builder, @Styles,
  @Extend, @StorageLink, @LocalStorageLink, @ComponentV2, @Local, @ObservedV2, @Trace, @Monitor,
  AppStorageV2, StateStore, aboutToAppear, onDidBuild, aboutToReuse, aboutToRecycle, onPageShow,
  Navigation, NavPathStack, navDestination, router, setInterception,
  Column, Row, Stack, Flex, List, RelativeContainer, GridRow, GridCol,
  LazyForEach, ForEach, @Reusable, cachedCount, IDataSource,
  animateTo, .animation(), Curve, geometryTransition, spring animation, springMotion,
  Ability Kit, Network Kit, Media Kit, Location Kit, Core Speech Kit, Core Vision Kit,
  Scan Kit, Push Kit, IAP Kit, Payment Kit, Live View Kit, Camera Kit, Media Library Kit,
  Audio Kit, Image Kit, ArkGraphics 2D, ArkGraphics 3D, Notification Kit, ArkData, ArkWeb,
  Form Kit, Connectivity Kit, Crypto Architecture Kit, Agent Framework Kit, MindSpore Lite,
  http.createHttp, preferences, relationalStore, distributedKVStore, fileIo, photoAccessHelper,
  geoLocationManager, speechRecognizer, notificationManager, hilog, wantAgent,
  TaskPool, TaskGroup, Worker, @Concurrent, @Sendable, taskpool.execute, SharedArrayBuffer,
  long-time task, taskpool.Priority, taskpool.executeDelayed, taskpool.executePeriodically,
  HAP, HSP, HAR, app.json5, module.json5, oh-package.json5, build-profile.json5,
  FormExtensionAbility, WorkSchedulerExtensionAbility, ServiceExtensionAbility,
  sys.symbol, SymbolGlyph, OHPM, ohpm, ArkCompiler, Cangjie,
  hvigor, hvigorw, hdc, HiLog, SmartPerf, DevEco Profiler, DevEco Testing,
  AppGallery Connect, hvigorw assembleApp,
  ErrorObserver, HiAppEvent, APP_FREEZE, JS_ERROR, CPP_CRASH, OOM,
  backgroundTaskManager, requestSuspendDelay, startBackgroundRunning, workScheduler,
  abilityAccessCtrl, requestPermissionsFromUser, HUKS,
  arkxtest, @ohos/hypium, JsUnit, UiTest, Driver, ON,
  $r(), $rawfile(), Resource, getContext,
  systemMaterialEffect, hdsMaterial, MaterialType, MaterialLevel,
  backgroundBlurStyle, BlurStyle, foregroundBlurStyle, backdropBlur, backgroundEffect,
  foregroundEffect, backgroundBrightness, pointLight, IlluminatedType, bloom,
  visualEffect, backgroundFilter, foregroundFilter, uiEffect,
  HDS, HarmonyOS Design System, liquid glass, immersive light

  触发关键词（中文）：鸿蒙, 鸿蒙开发, 鸿蒙应用, 鸿蒙NEXT, 鸿蒙6.0, 鸿蒙6.0.2,
  华为开发者, 华为手机开发, 方舟语言, 方舟编译器, 方舟UI, 声明式UI,
  鸿蒙组件, 鸿蒙页面, 组件生命周期, 组件复用,
  状态管理, 全局状态, StateStore, 组件通信, 页面跳转, 页面路由, 导航路由,
  鸿蒙动画, 显式动画, 隐式动画, 转场动画, 共享元素,
  鸿蒙列表, 懒加载, 虚拟列表, 长列表优化,
  鸿蒙网络请求, 鸿蒙数据存储, 鸿蒙文件操作, 鸿蒙数据库,
  鸿蒙权限, 权限申请, 动态权限, 鸿蒙安全, 加密等级,
  鸿蒙测试, 单元测试, UI自动化测试, 断言,
  鸿蒙后台任务, 后台运行, 长时任务, 短时任务, 延迟任务,
  鸿蒙打包, 鸿蒙发布, 应用上架, 华为应用市场, 签名,
  鸿蒙分布式, 跨设备, 流转, 多设备适配, 折叠屏, 平板适配, 一多, 响应式布局,
  原子化服务, 元服务, 服务卡片, 桌面卡片,
  鸿蒙调试, hdc命令, 日志, 性能优化, 布局优化, 内存优化, 崩溃, 卡顿, ANR,
  鸿蒙图标, 主题图标, 仓颉语言, 并发, 多线程, 任务池, 工作线程,
  液态玻璃, 沉浸光感, 沉浸光感视效, 通透质感, 玻璃效果, 模糊效果, 毛玻璃, 点光源,
  ArkTS和TypeScript区别, 怎么写鸿蒙应用, 鸿蒙入门, 鸿蒙教程, 鸿蒙最佳实践
---

# HarmonyOS (鸿蒙) Development

Covers HarmonyOS 6.0.2(22) / HarmonyOS NEXT native app development — the Huawei mobile OS family that runs independently of Android (AOSP-free since HarmonyOS NEXT, released 2024). Primary language is **ArkTS** (a strict, statically-checked superset of TypeScript) and the primary UI framework is **ArkUI** (declarative, state-driven). HarmonyOS 6.0 adds system-level "Immersive Light Perception" visual effects (液态玻璃/沉浸光感视效).

## When to use this skill

- Building, reading, or refactoring HarmonyOS / HarmonyOS NEXT apps (.hap / .hsp / .har modules)
- Writing ArkTS + ArkUI components with declarative `@Component`/`build()` syntax
- Questions about Stage model abilities, lifecycle, routing, or configuration files
- Debugging state-management decorators, rendering, or Observable propagation
- Choosing and calling HarmonyOS Kits (Ability, ArkUI, Network, Media, Location, HiAI, etc.)
- Building 原子化服务 (atomic services / meta-services) or cross-device distributed features
- Consulting the official samples catalog at https://developer.huawei.com/consumer/cn/samples/

## Platform snapshot

| Item | Value |
|---|---|
| OS | **HarmonyOS 6.0.2(22)** (current stable, Pure HarmonyOS, AOSP-free) |
| Language | **ArkTS** (primary), **Cangjie** (beta), C/C++ via NAPI |
| UI framework | **ArkUI** declarative (ArkUI-X for cross-platform) |
| Compiler | **ArkCompiler** — AOT to native machine code; LiteActor concurrency |
| Package manager | **ohpm** — `oh-package.json5`; registry at DevEco Service (OHPM Central) |
| IDE | **DevEco Studio 6.0.2 Release** (Hvigor 6.22.x, IntelliJ-based) |
| App model | **Stage model** (FA model is legacy — don't use in new apps) |
| Packaging | HAP (entry/feature), HSP (shared package), HAR (static archive), atomic .app |
| Recommended API | **API 20+ (strongly recommend API 22)** |
| Sample catalog | https://developer.huawei.com/consumer/cn/samples/ |

## Project layout (Stage model)

```
MyApp/
├─ AppScope/
│  ├─ app.json5                 # global app config (bundleName, icon, label)
│  └─ resources/                # shared resources
├─ entry/                       # main HAP (entry module)
│  ├─ src/main/
│  │  ├─ ets/
│  │  │  ├─ entryability/EntryAbility.ets   # UIAbility subclass
│  │  │  ├─ entrybackupability/
│  │  │  └─ pages/Index.ets                 # ArkUI pages
│  │  ├─ resources/              # strings, colors, media, profiles
│  │  └─ module.json5            # module config, abilities, permissions
│  └─ build-profile.json5
├─ oh-package.json5              # ohpm dependencies
└─ build-profile.json5           # project-level
```

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

## ArkTS language — strictness rules

ArkTS = TypeScript MINUS dynamic patterns, PLUS stricter static typing for AOT perf.

**Prohibited / changed vs TS:**
- No `any` / `unknown` as everyday escape hatches — declare real types
- No dynamic property add/delete on objects (`obj.foo = bar` on untyped object is a compile error)
- No `Function.prototype.bind`, `call`, `apply` with reshaped `this`
- No structural typing shortcuts — use nominal classes / interfaces
- No `Object.keys`/`Object.assign` for arbitrary reshaping
- `Record<K,V>` for true dictionary maps
- Use `class` / `interface` with explicit fields

```ts
// Prefer:
class User { constructor(public id: number, public name: string) {} }
// Over:
// const user: any = { id: 1, name: 'A' }
```

### Naming conventions (official coding style guide)

| Element | Convention | Example |
|---|---|---|
| Classes, Structs, Enums | **UpperCamelCase** | `PersonInfo`, `ColorType` |
| Variables, Parameters, Methods | **lowerCamelCase** | `userName`, `getUserInfo()` |
| Constants | **UPPER_SNAKE_CASE** | `MAX_VALUE`, `DEFAULT_TIMEOUT` |
| Boolean variables | Prefix with `is`, `has`, `can` | `isVisible`, `hasPermission` |

Formatting: 2-space indent, max 120 chars/line, K&R braces, always use `{}` for if/for/while.

### High-performance ArkTS rules (from official best practices)

1. Use `const` for unchanging values — enables engine optimization
2. Never mix int and float in same variable — `let n = 1; n = 1.1;` causes boxing overhead
3. Use TypedArrays (`Int8Array`, `Float32Array`) for numerical computation
4. Avoid sparse arrays — `arr[9999] = 0` forces hash-table storage (much slower)
5. Don't mix types in arrays — `[1, "a", 2]` deoptimizes
6. Cache property lookups outside hot loops
7. Avoid exception throwing in perf-critical loops — use sentinel values
8. Minimize closures in hot paths — pass variables via function params instead
9. Use Array methods (`forEach`, `map`, `filter`, `reduce`) — internally optimized
10. Keep `build()` pure and declarative — no side effects, load data in `aboutToAppear()`

## ArkUI — declarative UI

### Custom component basics

```ts
@Entry                      // marks route/page entry
@Component
struct Index {
  @State count: number = 0;

  build() {
    Column({ space: 12 }) {
      Text(`Count: ${this.count}`)
        .fontSize(24)
        .fontWeight(FontWeight.Bold)
      Button('Increment')
        .onClick(() => { this.count++; })
    }
    .width('100%').height('100%').justifyContent(FlexAlign.Center)
  }
}
```

### Component lifecycle callbacks

**All `@Component`:**

| Callback | When | Notes |
|---|---|---|
| `aboutToAppear()` | After created, BEFORE `build()` | Can change state here; changes apply in first `build()` |
| `onDidBuild()` | After `build()` completes | Do NOT change state or call `animateTo()`. API 12+ |
| `aboutToDisappear()` | Before destruction | Do NOT change state (especially `@Link`). No async/await |
| `aboutToReuse(params)` | Reusable component re-added from cache | Update state with new params. API 10+ |
| `aboutToRecycle()` | Component moving to reuse cache | Release heavy resources. API 10+ |

**Only `@Entry`:**

| Callback | When |
|---|---|
| `onPageShow()` | Each time page is displayed |
| `onPageHide()` | Each time page is hidden |
| `onBackPress(): boolean` | User taps Back. Return `true` to override default |

**Execution order (cold start):**
`Parent aboutToAppear → Parent build → Parent onDidBuild → Child aboutToAppear → Child build → Child onDidBuild → onPageShow`

### Layout containers

| Container | When to use | Performance |
|---|---|---|
| `Column` / `Row` | Linear arrangement | **Best** — single-pass layout |
| `Stack` | Overlapping / stacking | Good |
| `Flex` | Items need stretch/shrink | **Slower** — extra pass for flexGrow/flexShrink |
| `RelativeContainer` | Complex layouts, avoid deep nesting | Good — flat structure |
| `GridRow` / `GridCol` | Responsive multi-device grids | Good |
| `List` | Scrollable list with recycling | Best for long lists (with `LazyForEach`) |

**Column/Row alignment:**
- Main axis: `justifyContent(FlexAlign.Start | .Center | .End | .SpaceBetween | .SpaceAround | .SpaceEvenly)`
- Cross axis: Column → `alignItems(HorizontalAlign.Start | .Center | .End)`, Row → `alignItems(VerticalAlign.Top | .Center | .Bottom)`

**Stack:** `alignContent` takes 9 positions (TopStart, Top, TopEnd, Start, Center, End, BottomStart, Bottom, BottomEnd). `zIndex` controls layer order.

**Flex vs Column/Row:** Flex requires re-layout for `flexShrink`/`flexGrow`. Always prefer `Column`/`Row` when you don't need flex behavior.

**RelativeContainer:** Use `__container__` as anchor ID for the container itself. Each child needs `.id()`. Set `.alignRules({ top: { anchor: 'id', align: VerticalAlign.Bottom } })`.

### Performance-critical patterns

**`LazyForEach` for large lists** (only renders visible items):
```ts
class MyDataSource implements IDataSource {
  private data: string[] = []
  totalCount(): number { return this.data.length }
  getData(index: number): string { return this.data[index] }
  registerDataChangeListener(listener: DataChangeListener): void { /* ... */ }
  unregisterDataChangeListener(listener: DataChangeListener): void { /* ... */ }
}

List() {
  LazyForEach(this.dataSource, (item: string, index: number) => {
    ListItem() { Text(item) }
  }, (item: string) => item)  // key generator — MUST produce unique keys
}
.cachedCount(5)  // preload 5 items off-screen
```

**`@Reusable` components** (69% faster component creation):
```ts
@Reusable
@Component
struct MyListItem {
  @State message: Message = new Message('default')

  aboutToReuse(params: Record<string, ESObject>) {
    this.message = params.message as Message
  }
  aboutToRecycle() { /* release heavy resources */ }
  build() { Text(this.message.value) }
}
```
Rules: only works within same parent; don't nest `@Reusable` inside `@Reusable`; combine with `LazyForEach`.

**Layout performance rules:**
- Max 3 levels of nesting — each level adds layout cost
- Use `if/else` over `.visibility()` — hidden components still participate in layout
- Use `RelativeContainer` to flatten deep Row/Column/Flex hierarchies (documented 26% improvement)
- Set explicit dimensions on `List` inside `Scroll` — without them ALL children load at once
- Avoid `@StorageLink` for frequently-changing data — propagates to all subscribers

### Animation

**Explicit animation (`animateTo`)** — state changes in closure animate:
```ts
this.getUIContext()?.animateTo({
  duration: 300,
  curve: Curve.EaseOut,
  onFinish: () => { console.info('done') }
}, () => {
  this.width = 200  // this change animates
})
```

**Property animation (`.animation()`)** — implicit, applied to preceding attributes:
```ts
Text('Hello')
  .width(this.myWidth)
  .animation({ duration: 500, curve: Curve.EaseIn })
```

**Curve values:** `Curve.Linear | .Ease | .EaseIn | .EaseOut | .EaseInOut | .FastOutSlowIn | .Friction | .Sharp | .Smooth`

**Spring curves (string):** `'spring(velocity,mass,stiffness,damping)'`, `'springMotion(response,dampingFraction)'`, `'responsiveSpringMotion(response,dampingFraction)'`

**Shared element transition:**
```ts
// Bind same geometryTransition ID on source and target
Image($r('app.media.photo')).geometryTransition('picture')
// Wrap state change in animateTo
this.getUIContext()?.animateTo({ duration: 300 }, () => { this.isExpanded = !this.isExpanded })
```

### HarmonyOS 6.0 visual effects (沉浸光感视效 / 液态玻璃)

HarmonyOS 6.0 (API 23) introduces system-level "Immersive Light Perception" visual effects. Users enable via Settings → Desktop & Personalization → Immersive Light Effect (强/均衡/弱). Developers achieve similar effects through these ArkUI attributes:

**BlurStyle enum (API 9–11):**

| Name | Since | Level |
|---|---|---|
| `Thin` / `Regular` / `Thick` | API 9 | Material blur |
| `BACKGROUND_THIN` / `BACKGROUND_REGULAR` / `BACKGROUND_THICK` / `BACKGROUND_ULTRA_THICK` | API 10 | Depth-of-field (min→max) |
| `COMPONENT_ULTRA_THIN` / `COMPONENT_THIN` / `COMPONENT_REGULAR` / `COMPONENT_THICK` / `COMPONENT_ULTRA_THICK` | API 11 | Component-level material |
| `NONE` | API 10 | No blur |

**backgroundBlurStyle (API 9+):**
```ts
Column() { /* content */ }
  .backgroundBlurStyle(BlurStyle.Thin, {
    colorMode: ThemeColorMode.LIGHT,     // SYSTEM | LIGHT | DARK
    adaptiveColor: AdaptiveColor.DEFAULT, // DEFAULT | AVERAGE
    scale: 1.0                            // 0.0–1.0 (blur intensity)
  })
```

**foregroundBlurStyle (API 10+):**
```ts
Image($r('app.media.photo'))
  .foregroundBlurStyle(BlurStyle.Regular)
```

**backgroundEffect (API 11+) — fine-grained control:**
```ts
Column() { /* content */ }
  .backgroundEffect({
    radius: 20,          // blur radius
    saturation: 15,      // [0, 50] recommended
    brightness: 0.6,     // [0, 2] recommended
    color: '#80FFFFFF'   // mask color
  })
```

**blur / backdropBlur (API 7+) — numeric radius:**
```ts
Column() { /* content */ }
  .backdropBlur(20, { grayscale: [30, 50] })  // background blur
  .blur(10)                                    // foreground blur
```

**backgroundBrightness (API 12+):**
```ts
Column() { /* content */ }
  .backgroundBrightness({ rate: 0.5, lightUpDegree: 0.2 })
```

**Visual effect filters (API 12+):**
```ts
import { uiEffect } from '@kit.ArkGraphics2D';

const blurFilter = uiEffect.createFilter().blur(10);
Column() { /* content */ }
  .backgroundFilter(blurFilter)    // background filter
  .foregroundFilter(blurFilter)    // content filter
```

**pointLight (API 11+, System API only — NOT available for third-party apps):**
```ts
// System apps only! Supports: Image, Column, Flex, Row, Stack, Button, Toggle
Flex()
  .pointLight({
    lightSource: { positionX: '50%', positionY: '50%', positionZ: 80, intensity: 2, color: Color.White },
    illuminated: IlluminatedType.BORDER,  // NONE | BORDER | CONTENT | BORDER_CONTENT
    bloom: 0.5                            // luminous intensity 0–1
  })
```
Up to 12 light sources can illuminate a single component. HarmonyOS 6.0 adds dual-edge flow light and UV background flow light effects.

**systemMaterialEffect (HDS layer, API 23+, HarmonyOS-only SDK):**
```ts
import { hdsMaterial } from '@kit.ArkUI';

Column() { /* content */ }
  .systemMaterialEffect({
    materialType: hdsMaterial.MaterialType.ADAPTIVE,
    materialLevel: hdsMaterial.MaterialLevel.ADAPTIVE
  })
```
Note: `hdsMaterial` is part of the closed-source HarmonyOS Design System (HDS), not OpenHarmony. Requires HarmonyOS 6.0 SDK (API 23+).

### State-management decorators

| Decorator | Scope | Purpose |
|---|---|---|
| `@State` | within component | Owned mutable state; triggers re-render |
| `@Prop` | parent → child | One-way copy (child has local copy) |
| `@Link` | parent ↔ child | Two-way binding (use `$var` to pass) |
| `@Provide` / `@Consume` | ancestor → descendant | Cross-level implicit binding by key |
| `@Observed` (class) + `@ObjectLink` (prop) | class instances | Observe changes to class properties |
| `@Watch('handler')` | any of above | Callback on value change |
| `@StorageLink` / `@StorageProp` | app-wide `AppStorage` | Global reactive state |
| `@LocalStorageLink` / `@LocalStorageProp` | page-scoped | Scoped reactive state |

**Passing `@Link`:**
```ts
@Entry @Component struct Parent {
  @State val: number = 0;
  build() { Child({ val: $val }) }     // $ prefix for @Link
}
@Component struct Child {
  @Link val: number;
  build() { Button(`${this.val}`).onClick(() => this.val++) }
}
```

**Observing class objects:**
```ts
@Observed class Task { constructor(public title: string, public done: boolean) {} }

@Component struct TaskRow {
  @ObjectLink task: Task;            // re-renders when task.title/done changes
  build() { Text(this.task.title) }
}
```

Arrays of `@Observed` instances require `@ObjectLink` in the row component — parent `@State tasks: Task[]` only reacts to array mutations (push/splice/reassign), not per-item changes.

**State management performance rules (from official docs):**
- Minimize state scope: only `@State` variables that directly affect UI
- `@Prop` creates **deep copy** on every update — for large objects, prefer `@Link` (by reference) or `@ObjectLink`
- `@Link` is preferred for inter-component communication — avoids unnecessary re-renders
- `@Observed` + `@ObjectLink` for nested objects — fine-grained property observation
- `@ObjectLink` is **READ-ONLY** — cannot reassign whole object (`this.task = new Task()` breaks binding)
- Avoid `@StorageLink` for frequently-changing data — global state changes propagate to ALL subscribers
- **Observation depth (V1):** `@State`/`@Prop`/`@Link` observe ONLY first-level properties. Nested changes are NOT detected. Array: only push/splice/reassign/length, NOT item mutations.

### V2 state decorators (API 12+)

| V1 | V2 replacement | Change |
|---|---|---|
| `@Component` | `@ComponentV2` | Clearer semantics |
| `@State` | `@Local` | Cannot be initialized externally — internal state only |
| `@Observed` + `@ObjectLink` | `@ObservedV2` + `@Trace` | **Deep observation** across multiple nested levels |
| `@Watch` | `@Monitor('prop')` | More precise deep listener |
| `AppStorage` | `AppStorageV2` | Unified with `@ObservedV2` + `@Trace` |

```ts
@ObservedV2
class UserInfo {
  @Trace name: string = '';    // changes to this trigger UI refresh
  @Trace age: number = 0;     // changes to this trigger UI refresh
  address: string = '';        // NO @Trace → changes do NOT trigger refresh
}
```
Rules: `@ObservedV2` and `@Trace` must be used together (either alone has no effect). Only `@Trace`-decorated properties participate in UI rendering.

### StateStore — global state management (2026, officially recommended for mid-large apps)

Separates state logic from UI components entirely. Works with `@ObservedV2` + `@Trace`.

```ts
import { StateStore } from '@kit.ArkUI';

@ObservedV2
class CounterStore {
  @Trace count: number = 0;

  increment(): void {
    this.count++;
  }
}

// Create global store (do this once, e.g. in EntryAbility or top-level)
const counterStore = StateStore.createStore(new CounterStore());

// In any component — read state
@Entry
@Component
struct CounterPage {
  build() {
    Column() {
      Text(`Count: ${counterStore.getState().count}`)
      Button('Add').onClick(() => {
        counterStore.getState().increment();
      })
    }
  }
}
```

**When to use:** Multiple pages/components share the same state; state logic is complex; need thread-safe updates (TaskPool workers can safely update StateStore).

Docs: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-global-state-management-state-store

### Builders, styles, extends

```ts
@Builder function Label(text: string) { Text(text).fontSize(16) }

@Styles function Card() { .padding(12).borderRadius(12).backgroundColor('#FFF') }

@Extend(Text) function title() { .fontSize(22).fontWeight(FontWeight.Bold) }

// Usage:
Text('Hello').title()
Column() { Label('x') } .Card()
```

### Navigation (recommended: Navigation component, not Router)

```ts
@Entry @Component struct App {
  @Provide('pathStack') pathStack: NavPathStack = new NavPathStack();
  build() {
    Navigation(this.pathStack) {
      Button('Go').onClick(() => this.pathStack.pushPath({ name: 'Detail', param: 42 }))
    }
    .navDestination((name: string, param: Object) => {
      if (name === 'Detail') Detail({ id: param as number })
    })
  }
}
```

The older `router` module (`@ohos.router`) still works but `Navigation` + `NavPathStack` is the modern API for HarmonyOS NEXT.

**NavPathStack full API:**
```ts
// Push
pathStack.pushPath({ name: 'Page', param: data });
pathStack.pushPathByName('Page', data);
pathStack.pushPathByName('Page', data, (popInfo) => {
  console.info('Pop result: ' + JSON.stringify(popInfo.result));
});

// Pop, Replace, Remove
pathStack.pop();
pathStack.replacePath({ name: 'Page', param: data });
pathStack.removeIndex(0);
pathStack.movePageToTop('Page');

// Query
pathStack.getParamByIndex(index);
pathStack.getParamByName('Page');
pathStack.getAllPathName();
pathStack.size();
```

**Route interception:**
```ts
pathStack.setInterception({
  willShow: (from, to, operation) => { /* validate/redirect */ },
  didShow: (from, to, operation) => { /* analytics */ }
});
```

Display modes: **Stack** (single column), **Split** (two columns), **Auto** (adaptive, 600vp threshold).

## HarmonyOS Kits (common imports)

```ts
import { UIAbility, Want, common, abilityAccessCtrl } from '@kit.AbilityKit';
import { window, display, promptAction } from '@kit.ArkUI';
import { http, webSocket, connection } from '@kit.NetworkKit';
import { photoAccessHelper } from '@kit.MediaLibraryKit';   // photo/video picker
import { fileIo as fs } from '@kit.CoreFileKit';
import { geoLocationManager } from '@kit.LocationKit';
import { relationalStore, preferences, distributedKVStore } from '@kit.ArkData';
import { notificationManager } from '@kit.NotificationKit';
import { speechRecognizer } from '@kit.CoreSpeechKit';       // ASR / TTS
import { hilog } from '@kit.PerformanceAnalysisKit';
```

### Full Kit catalog — official SDK categories (developer.huawei.com/consumer/cn/sdk/)

**应用框架 Application Framework**

| Kit | Import key | Purpose |
|---|---|---|
| Ability Kit | `AbilityKit` | UIAbility, ExtensionAbility, Want, context, routing |
| Accessibility Kit | `AccessibilityKit` | Screen reader, universal design, a11y services |
| ArkData | `ArkData` | relationalStore, preferences, distributedKVStore |
| ArkTS | — | Language spec & Ark compiler tooling |
| ArkUI | `ArkUI` | window, display, promptAction, Navigation, components |
| ArkWeb | `ArkWeb` | WebView / Web component embedding |
| Background Tasks Kit | `BackgroundTasksKit` | Deferred/scheduled background work, transient tasks |
| Core File Kit | `CoreFileKit` | fileIo, picker, sandbox paths |
| Form Kit | `FormKit` | FormExtensionAbility, home-screen service cards/widgets |
| IME Kit | `IMEKit` | Input method engine development |
| IPC Kit | `IPCKit` | Inter-process communication (Parcel, RemoteObject) |
| Localization Kit | `LocalizationKit` | i18n, l10n, RTL, pseudo-localization |

**应用服务 Application Services**

| Kit | Import key | Purpose |
|---|---|---|
| Account Kit | `AccountKit` | One-click Huawei ID login, OAuth 2.0 |
| Ads Kit | `AdsKit` | Advertising SDK (banner, native, interstitial) |
| App Linking Kit | `AppLinkingKit` | Deep links, deferred deep links |
| Calendar Kit | `CalendarKit` | Calendar events, reminders |
| Contacts Kit | `ContactsKit` | Contact read/write/search |
| IAP Kit | `IAPKit` | In-app purchases (consumable, non-consumable, subscription) |
| Live View Kit | `LiveViewKit` | Live activities on lock screen / notification center |
| Location Kit | `LocationKit` | geoLocationManager, geofencing, geocoding |
| Map Kit | `MapKit` | Huawei Maps SDK, routing, place search |
| Notification Kit | `NotificationKit` | Local + push notifications, badges |
| Payment Kit | `PaymentKit` | Huawei Pay transaction processing |
| Push Kit | `PushKit` | Push notification delivery service |
| Scan Kit | `ScanKit` | QR/barcode scanning |
| Share Kit | `ShareKit` | Cross-app content sharing |

**系统 System**

| Kit | Import key | Purpose |
|---|---|---|
| Asset Store Kit | `AssetStoreKit` | Secure credential/secret storage |
| Basic Services Kit | `BasicServicesKit` | Battery, vibration, thermal, brightness, clipboard |
| Connectivity Kit | `ConnectivityKit` | Bluetooth, Wi-Fi, NFC, USB, hotspot |
| Crypto Architecture Kit | `CryptoArchitectureKit` | Encryption, key management, certificates |
| Distributed Service Kit | `DistributedServiceKit` | deviceManager, cross-device discovery |

**媒体 Media**

| Kit | Import key | Purpose |
|---|---|---|
| Audio Kit | `AudioKit` | Audio playback, recording, routing, focus |
| AVCodec Kit | `AVCodecKit` | Hardware-accelerated encode/decode (H.264, H.265, AAC…) |
| Camera Kit | `CameraKit` | Camera preview, photo capture, video recording |
| Image Kit | `ImageKit` | Image decoding, transformation, EXIF |
| Media Kit | `MediaKit` | AVPlayer, AVRecorder (unified playback/recording) |
| Media Library Kit | `MediaLibraryKit` | photoAccessHelper, media library CRUD |
| Scan Kit | `ScanKit` | QR/barcode scanning |

**图形 Graphics**

| Kit | Import key | Purpose |
|---|---|---|
| ArkGraphics 2D | `ArkGraphics2D` | 2D Canvas drawing, effects, blur, shadow |
| ArkGraphics 3D | `ArkGraphics3D` | 3D scene graph, glTF rendering |
| XComponent | (ArkUI built-in) | Native OpenGL ES / Vulkan surface via NAPI |

**AI**

| Kit | Import key | Purpose |
|---|---|---|
| Core Speech Kit | `CoreSpeechKit` | On-device ASR / TTS engine |
| Core Vision Kit | `CoreVisionKit` | OCR, face detection, image segmentation, super-resolution |
| Intents Kit | `IntentsKit` | Intent recognition (30+ domains, 60+ built-in intents) |
| MindSpore Lite | `MindSporeLiteKit` | Edge model inference (Caffe/TF/ONNX/MindIR) |
| Natural Language Kit | `NaturalLanguageKit` | Word segmentation, NER, keyword extraction |

**Performance & DevTools**

| Kit | Import key | Purpose |
|---|---|---|
| Performance Analysis Kit | `PerformanceAnalysisKit` | hilog, HiAppEvent, crash analysis |

### Photo/video picker (correct API — `picker.PhotoViewPicker` is deprecated)

```ts
import { photoAccessHelper } from '@kit.MediaLibraryKit';

const phAccessHelper = photoAccessHelper.getPhotoAccessHelper(context);
const picker = new photoAccessHelper.PhotoViewPicker();
const result = await picker.select({
  MIMEType: photoAccessHelper.PhotoViewMIMETypes.IMAGE_TYPE,
  maxSelectNumber: 9
});
const uris: string[] = result.photoUris;
```

### CoreSpeechKit — ASR audio format requirements

```ts
import { speechRecognizer } from '@kit.CoreSpeechKit';

const engine = await speechRecognizer.createEngine({
  language: 'zh-CN',
  online: 0   // 0=on-device, 1=cloud
});
// Audio MUST be: PCM, 16kHz, mono, 16-bit
// Chunk size: 640 or 1280 bytes, write every 20ms or 40ms
engine.startListening({
  sessionId: `asr_${Date.now()}`,
  audioInfo: {
    audioType: 'pcm',
    sampleRate: 16000,
    soundChannel: 1,
    sampleBit: 16
  }
});
```

### HTTP request example

```ts
import { http } from '@kit.NetworkKit';

async function fetchJson(url: string): Promise<string> {
  const req = http.createHttp();
  try {
    const res = await req.request(url, {
      method: http.RequestMethod.GET,
      header: { 'Content-Type': 'application/json' },
      connectTimeout: 5000, readTimeout: 10000
    });
    return res.result as string;
  } finally {
    req.destroy();
  }
}
```

### Permissions

Declare in `module.json5` → `requestPermissions`. For user-granted permissions, request at runtime via `abilityAccessCtrl.createAtManager().requestPermissionsFromUser(context, [...])`.

### Persistent storage options

- **Preferences** — lightweight key-value (`@kit.ArkData` → `preferences`)
- **Relational Store** — SQLite (`relationalStore`)
- **Distributed KV Store** — cross-device sync
- **File I/O** — `@kit.CoreFileKit` `fileIo` / sandbox paths

## Atomic Services / Meta-Services (原子化服务 / 元服务)

Installation-free, small (≤10MB) apps launched from:
- Service cards (home-screen widgets built with `FormExtensionAbility`)
- Search, scan, NFC, cross-device continuation

Configured via `module.json5` with `"installationFree": true`. Build-time they produce `.app` packages containing multiple HAPs.

## Distributed features

- **Cross-device continuation** (流转) — `continueAbility` / `onContinue`/`onNewWant` lifecycle
- **Distributed data object** — synced state across devices
- **Distributed file system** — shared sandbox
- **Device manager** — discover trusted devices

## Packaging types

| Type | Purpose |
|---|---|
| **HAP** (Harmony Ability Package) | Runnable module: `entry` or `feature` type |
| **HSP** (Harmony Shared Package) | In-app shared module, dynamic-linked at runtime |
| **HAR** (Harmony Archive) | Static library, packaged into HAP at build time |

Distribute via AppGallery Connect (华为应用市场).

## Sample catalog (developer.huawei.com/consumer/cn/samples)

The official samples repo is organized by the following **10 official categories** (as shown on the HarmonyOS developer samples page):

| 类别 | Category | What it covers |
|---|---|---|
| **HarmonyOS特征** | HarmonyOS Features | Platform-differentiating capabilities: 一多 (one-develop multi-deploy) responsive layout, 分布式流转 cross-device continuation, 原子化服务 / 服务卡片 atomic services & service cards, 超级终端 super device, 方舟编译器 Ark compiler features, 鸿蒙智联 HarmonyOS Connect |
| **技术质量** | Technical Quality | Performance optimization (startup time, frame rate, memory), stability (crash/ANR), power consumption, security hardening, code quality, HiAppEvent / HiLog diagnostics, DFX capabilities |
| **应用框架开发** | Application Framework | UIAbility / ExtensionAbility lifecycle, Ability routing & want, AppStartup, state management (@State/@Link/@Provide/@Observed), ArkUI components & layouts, Navigation / NavPathStack, Router, window management, internationalization, resource management, notifications, background tasks |
| **系统开发** | System Development | Power/battery APIs, telephony (call/SMS), account system, device management, settings, accessibility, input method, wallpaper, system apps, low-level OS integration |
| **媒体开发** | Media Development | AVPlayer / AVRecorder audio & video playback/recording, camera (CameraKit), image codec (ImageKit), media library, AVSession, audio focus, DRM, HDR |
| **图形开发** | Graphics Development | ArkGraphics 2D, XComponent + native OpenGL ES / Vulkan, 3D rendering, Canvas, animations & transitions, effects, WebGL, SVG, drawing APIs |
| **应用服务开发** | Application Service | Location (LocationKit / geoLocationManager), maps, push notifications, payments, account sign-in (Huawei ID), sharing, scanning, health/fitness, wallet, in-app purchase |
| **AI功能开发** | AI Function Development | HiAI Foundation Kit, CoreVisionKit (image classification, OCR, face detection), SpeechKit (ASR/TTS), natural language, MindSpore Lite on-device inference, AI image enhancement, generative models |
| **应用专项测试** | Application Testing | Unit testing (ohUnit / Hypium), UI automation testing, performance testing, compatibility testing, monkey / stress testing, smartperf profiling, DevEco Testing |
| **开发工具** | Development Tools | DevEco Studio plugins & workflows, hvigor build scripts, ohpm package management, hdc device connector, Previewer, Profiler, Code Linter, debugging & logging tools |

> Browse the live catalog at https://developer.huawei.com/consumer/cn/samples/ — filter by category or search by Kit name / API (e.g. "relationalStore", "FormExtensionAbility", "AVPlayer").

**When helping the user pick a sample:**
1. Identify which of the 10 categories the feature belongs to
2. Narrow by the specific Kit (AbilityKit, MediaKit, HiAIVisionKit, LocationKit, etc.)
3. Match by API name or scenario (e.g. "service card" → 应用框架开发 + FormExtensionAbility)

## Multi-device (一多) responsive layout

HarmonyOS supports a single codebase across phone, tablet, 2-in-1, watch, smartscreen, and automotive. Use breakpoints in **vp** (not px).

### Breakpoints

| Breakpoint | vp width | Target |
|---|---|---|
| xs | < 320 | watch |
| sm | 320–600 | phone portrait |
| md | 600–840 | phone landscape / small tablet |
| lg | 840–1440 | tablet / 2-in-1 |
| xl | ≥ 1440 | large screen |

**Always convert px → vp before comparing:**
```ts
import { display } from '@kit.ArkUI';
function getBreakpoint(): string {
  const dm = display.getDefaultDisplaySync();
  const w = dm.width / dm.densityPixels; // vp
  if (w < 600) return 'sm';
  if (w < 840) return 'md';
  return 'lg';
}
```

### GridRow / GridCol (recommended for responsive grids)

```ts
GridRow({ columns: { sm: 4, md: 8, lg: 12 }, gutter: { x: 12 } }) {
  GridCol({ span: { sm: 4, md: 4, lg: 6 } }) { LeftPanel() }
  GridCol({ span: { sm: 4, md: 4, lg: 6 } }) { RightPanel() }
}
```

### Foldable / hover mode
Listen for display change and re-check breakpoint:
```ts
display.on('change', (_id: number) => { this.bp = getBreakpoint(); });
display.off('change');
```

## sys.symbol — icon glyph system

HarmonyOS Symbol is a 1500+ vector icon font with multi-layer color and 7 animation types.

```ts
SymbolGlyph($r('sys.symbol.bell_fill'))
  .fontSize(24)
  .fontColor([Color.Blue, Color.Green])
  .symbolEffect(new BounceSymbolEffect(EffectScope.WHOLE), true)
```

**Confirmed working names** (SDK 6.0.1): `xmark` · `plus` · `minus` · `checkmark` · `chevron_right` · `chevron_left` · `star` · `star_fill` · `bell` · `bell_fill` · `doc` · `video` · `mic` · `mic_fill` · `clock` · `trash` · `pencil` · `image` · `person`

**Names that do NOT exist** (common mistakes): `photo` · `doc_richtext` · `sparkles` · `checklist`

Find valid names: https://developer.huawei.com/consumer/cn/design/harmonyos-symbol

## DevEco Studio 6.x — Project Setup

DevEco Studio 6.x requires **additional Hvigor infrastructure files**. Without them the IDE shows "工程结构及配置需要升级".

### hvigorfile.ts (root + each module)

```ts
// root
import { appTasks } from '@ohos/hvigor-ohos-plugin';
export default { system: appTasks, plugins:[] }

// entry/hvigorfile.ts
import { hapTasks } from '@ohos/hvigor-ohos-plugin';
export default { system: hapTasks, plugins:[] }
```

### hvigor/wrapper/hvigor-config.json5

```json5
{
  "hvigorVersion": "5.0.0",
  "dependencies": {
    "@ohos/hvigor-ohos-plugin": "5.0.0"
  }
}
```

### build-profile.json5 — SDK version placement

SDK versions go in **one place only** — either under `app` OR inside each `product`, not both. Mixing them causes "Sync Failed".

**Recommended workflow:** Always let DevEco Studio generate the scaffold (`新建项目` → Empty Ability), then copy your source files in.

## ArkTS strict-mode compiler errors (SDK 6.0.1)

### No object literals as types
```ts
// ❌
parseOutput(): { text: string; tags: string[] } { ... }
// ✅
interface ParsedOutput { text: string; tags: string[]; }
parseOutput(): ParsedOutput { ... }
```

### No `any` / `unknown`
```ts
const task = JSON.parse(rawStr) as AgentTask;  // ✅ cast immediately
```

### `navDestination` requires a `@Builder` function reference
```ts
// ❌ inline lambda
.navDestination((name, param) => { if (name==='X') MyPage() })
// ✅ top-level @Builder
@Builder function PageRouter(name: string) { if (name==='X') MyPage() }
Navigation(stack) { ... }.navDestination(PageRouter)
```

### `@Entry` build() root must be a container
Wrap in `Stack()`, `Column()`, or `Row()` — a custom component alone is not a container.

### `display.width` is pixels, not vp
```ts
function isTablet(): boolean {
  const dm = display.getDefaultDisplaySync();
  return (dm.width / dm.densityPixels) >= 840;
}
```

### All user_grant permissions need `reason` + `usedScene`
```json5
{
  "name": "ohos.permission.READ_MEDIA",
  "reason": "$string:permission_media_reason",
  "usedScene": { "abilities": ["EntryAbility"], "when": "inuse" }
}
```
`INTERNET` is system_grant — no extra fields needed.

## Common gotchas

1. **Don't mix FA and Stage models** — FA is legacy; HarmonyOS NEXT only supports Stage.
2. **`this` in ArkUI callbacks** — arrow functions are required; regular `function () {}` loses `this`.
3. **`@State` on nested objects** — changes to nested props don't trigger updates; use `@Observed`/`@ObjectLink` or reassign the whole object.
4. **Array item updates** — replace the item (`arr[i] = newItem`) or use `@Observed` on the item class.
5. **Resource references** — use `$r('app.string.foo')`, `$r('app.media.icon')`, not string paths.
6. **`getContext(this)`** inside a component returns the `UIAbilityContext`; cast explicitly.
7. **Async in `build()`** is forbidden — load data in `aboutToAppear()` and store in `@State`.
8. **Permissions must be declared AND requested at runtime** for user-grant permissions.
9. **ohpm** is the package manager (similar to npm) — dependencies live in `oh-package.json5`.
10. **Preview on device** — DevEco Previewer doesn't fully simulate; always test on real HarmonyOS device or emulator.

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

// Request (if user previously rejected, use requestPermissionOnSetting instead)
atManager.requestPermissionsFromUser(context,
  ['ohos.permission.CAMERA', 'ohos.permission.MICROPHONE']);
```

**Data encryption levels:** EL1 (device-level) → EL2 (user-level, default) → EL3 (accessible while locked) → EL4 (inaccessible when locked)

## Testing — arkxtest framework

Package: `@ohos/hypium` (Mocha-style). Three sub-frameworks: **JsUnit** (unit), **UiTest** (UI automation), **PerfTest** (performance).

### JsUnit

```ts
import { describe, it, expect, beforeAll, beforeEach, afterEach, afterAll } from '@ohos/hypium';

export default function abilityTest() {
  describe('MyTestSuite', () => {
    beforeAll(() => { /* once before all */ });
    beforeEach(() => { /* before each */ });
    afterEach(() => { /* after each */ });
    afterAll(() => { /* once after all */ });

    it('sync_test', 0, () => {
      expect(1 + 1).assertEqual(2);
    });

    it('async_test', 0, async (done: Function) => {
      let result = await someAsyncOp();
      expect(result).assertContain('expected');
      done();
    });
  });
}
```

**Key assertions:** `assertEqual(v)` · `assertContain(v)` · `assertTrue()` · `assertFalse()` · `assertNull()` · `assertUndefined()` · `assertNaN()` · `assertInstanceOf(type)` · `assertThrowError(fn)` · `assertDeepEquals(v)` · `assertClose(v, tolerance)` · `assertLarger(v)` · `assertLess(v)` · `not()` (negation) · `assertPromiseIsResolved()` · `assertPromiseIsRejected()`

### UiTest — UI automation

```ts
import { Driver, ON } from '@kit.TestKit';

it('ui_test', 0, async () => {
  let driver = Driver.create();

  let btn = await driver.findComponent(ON.text('Submit'));
  await btn.click();

  let input = await driver.findComponent(ON.id('username'));
  await input.inputText('test_user');

  await driver.assertComponentExist(ON.text('Success'));
});
```

**ON selectors:** `.text()` · `.id()` · `.type()` · `.above()` · `.below()` · `.leftOf()` · `.rightOf()`

**Component actions:** `click()` · `doubleClick()` · `longClick()` · `swipe()` · `drag()` · `inputText()` · `setText()` · `keyEvent()`

Test files in `entry/src/ohosTest/ets/test/`. Always `await` UiTest async APIs; component references become stale after UI changes.

## 仓颉 (Cangjie) — alternative language (Beta)

| | ArkTS | Cangjie |
|---|---|---|
| Status | **Production** (use this now) | **Beta / developer preview** |
| Base | TypeScript superset | New language (Huawei-designed) |
| Key feature | Familiar TS syntax, strict AOT typing | Concurrent GC, embedded AgentDSL for AI |
| Use for | All current HarmonyOS NEXT apps | Experimentation only until stable |

## ArkCompiler — runtime details

- **AOT mode** — static type info generates optimized native machine code; no JIT warm-up
- **LiteActor concurrency** — Actor model with isolated memory per thread; communication via message passing

### TaskPool vs Worker

| Feature | TaskPool | Worker |
|---|---|---|
| Thread management | Automatic (create/reuse/destroy) | Manual lifecycle |
| Max threads | Auto-scaled to physical cores | Max 64 per process |
| Task duration limit | **3 minutes** (excluding async I/O) | Unlimited |
| Priority | HIGH / MEDIUM / LOW / IDLE | API 18+ only |
| Cancellation | Supported | Not supported |
| Thread reuse | Yes | No |
| Task groups | Yes | No |
| Delayed/periodic | Yes | No |

**Use Worker when:** tasks exceed 3 minutes, need persistent state, or strongly associated synchronous tasks.

### @Concurrent rules
- **Required** on all TaskPool functions, **only in `.ets` files**
- Allowed: regular functions, async functions
- **Prohibited:** arrow functions, class methods, anonymous functions, generator functions
- **No closure variables** — cannot reference outer scope; only local vars, params, and imports
- Cannot call other same-file functions (closure violation) — must import them

```ts
import { taskpool } from '@kit.ArkTS';

@Concurrent
function heavyCalc(n: number): number { return n * n; }

const result = await taskpool.execute(heavyCalc, 42);

// With priority
const task = new taskpool.Task(heavyCalc, 42);
await taskpool.execute(task, taskpool.Priority.HIGH);

// Delayed and periodic
taskpool.executeDelayed(heavyCalc, 2000, 42);      // after 2s
taskpool.executePeriodically(heavyCalc, 5000, 42);  // every 5s

// TaskGroup — execute multiple tasks as a group
const group = new taskpool.TaskGroup();
group.addTask(heavyCalc, 10);
group.addTask(heavyCalc, 20);
group.addTask(heavyCalc, 30);
const results = await taskpool.execute(group);  // returns array of results
```

**Long-time tasks:** async code (Promise/IO) in TaskPool has NO time limit (only CPU-bound sync code is capped at 3 minutes). HarmonyOS 6.0 officially supports long-running async tasks in TaskPool.

### @Sendable — shared-heap reference passing
Objects on SharedHeap (process-level, all threads can access) — **100x faster** than serialization for 1MB data.

```ts
@Sendable
class SharedData {
  value: number = 0;  // must be explicitly initialized
}
```

**Constraints:** Can only inherit from Sendable classes. Property types limited to: primitives, Sendable classes, `@arkts.collections` containers. Cannot add/delete properties at runtime. No computed properties. No `#` private (use `private` keyword).

### Worker pattern
```ts
// Main thread
const worker = new worker.ThreadWorker('entry/ets/workers/myWorker.ets');
worker.postMessage({ type: 'compute', data: payload });
worker.onmessage = (e) => { /* handle result */ };
worker.terminate();

// Worker thread (myWorker.ets)
const workerPort = worker.workerPort;
workerPort.onmessage = (e) => {
  const result = processData(e.data);
  workerPort.postMessage(result);
};
```

**Both TaskPool and Worker:** Cannot access AppStorage or UI libraries from worker threads. Different thread contexts prevent context object sharing.

## OHPM — package manager

```bash
ohpm install @ohos/axios          # install a library
ohpm install                      # install all from oh-package.json5
```

**oh-package.json5 example:**
```json5
{
  "name": "entry",
  "dependencies": {
    "@ohos/axios": "^2.0.0"
  }
}
```

OHPM Central Repository: https://developer.huawei.com/consumer/cn/deveco-service

## Debugging & tooling

- **DevEco Studio** — primary IDE, includes emulator, previewer, profiler, HiLog viewer
- **hdc** — Harmony Device Connector (like adb): `hdc shell`, `hdc file send`, `hdc hilog`
- **HiLog** — logging: `hilog.info(0x0001, 'TAG', 'message %{public}s', arg)`
- **Instruments: SmartPerf / DevEco Profiler** — CPU/GPU/memory/energy profiling
- **DevEco Testing** — UI automation, performance testing, monkey/stress, compatibility

## Publishing

1. Obtain a HarmonyOS developer account, complete real-name verification
2. Generate signing certificate + profile in AppGallery Connect
3. Configure signing in `build-profile.json5`
4. Build release HAP/APP bundle: `hvigorw assembleApp`
5. Upload to **AppGallery Connect** for review

## Best practices (official)

Portal: https://developer.huawei.com/consumer/cn/best-practices
Overview: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-best-practices-overview

### By topic

**Performance**
- ArkTS high-perf programming: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-arkts-high-performance
- Layout optimization: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-improve-layout-performance
- Component drawing optimization: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-pptimized-component-drawing
- High-load frame rendering: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-dispose-highly-loaded-component-render
- Memory analysis: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-analyze-memory-problem
- Runtime performance detection: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-performance-runtime-detection

**Stability**
- Stability overview: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-overview
- Crash detection: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-runtime-crash-detection
- JS memory leak detection: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-js-memleak-detection
- Thread leak detection: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-thread-leak-detection

**Power / Battery**
- Power optimization: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-application-power-optimization
- Power testing: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-application-power-test

**Media (Audio/Video)**
- AVPlayer basic control: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-avplayer-basic-control
- AVPlayer network video: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-avplayer-embeded-network-video
- AudioCapturer recording: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-audio-record-base-on-audiocapturer
- AVRecorder recording: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-audio-record-base-on-avrecorder-arkts
- Video playback optimization: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-online-video-playback-lags-practice
- Custom camera recording: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-custom-camera-video
- Live stream audio call: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-hmos-live-stream-audio-call

**Cross-device / 自由流转**
- Free flow overview: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-hopping
- App continuation: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-continue-cast
- Cross-device migration: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-cross-end-migration

**Multi-device**
- PC app development: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-pc-guide
- Wearable development: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-wear

**UI / Layout**
- Custom dialogs: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-customdialog-selection-and-development
- Custom fonts: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-custom-font-settings
- Soft keyboard adaptation: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-keyboard-layout-adapt

**Security**
- App security coding: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-harmony-application-security
- ArkWeb security: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-arkweb-component-security

**Web**
- Web cross-domain: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-cross-domain-solutions-for-web-pages
- Web performance: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-web-performance-optimization

## Codelabs (hands-on tutorials)

Portal: https://developer.huawei.com/consumer/cn/codelabsPortal/serviceTypes

| Codelab | Topic |
|---|---|
| [Hello World](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_Next-HelloWorld) | Getting started |
| [ArkTS Algorithm](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_NEXT-ArkTSAlgorithm) | ArkTS basics |
| [Account Kit Login](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_NEXT-AccountKit-QuickLogin) | One-click Huawei ID login |
| [Core Vision Kit](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_Next-CoreVisionKit) | ML / image recognition |
| [Scan Kit](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_ScanKit-Codelab-Clientdemo-ArkTS) | QR/barcode scanning |
| [Push Token](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_NEXT-Push-Get-Token) | Push notifications |
| [Payment Kit](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_NEXT-Paymentkit) | In-app payment |
| [Live View Delivery](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_NEXT-Live-View-Delivery) | Lock-screen live activity |
| [Pedometer App](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_NEXT-PedometerApp) | Health/fitness sensors |
| [Ads Kit](https://developer.huawei.com/consumer/cn/codelabsPortal/carddetails/tutorials_AdsKit-Native-ArkTS) | Native ads integration |

## Training & certification

- HarmonyOS basic cert: https://developer.huawei.com/consumer/cn/training/dev-cert-detail/101666948302721398
- HarmonyOS advanced cert: https://developer.huawei.com/consumer/cn/training/dev-cert-detail/101684223987951077
- Game dev cert: https://developer.huawei.com/consumer/cn/training/dev-cert-detail/101748228483629752
- ArkUI development course (Part 1): https://developer.huawei.com/consumer/cn/training/course/video/C101727405259250407
- ArkUI development course (Part 2): https://developer.huawei.com/consumer/cn/training/course/video/C101716428085146011
- ArkTS syntax course: https://developer.huawei.com/consumer/cn/training/course/slightMooc/C101717496870909384
- SDK open capabilities study path: https://developer.huawei.com/consumer/cn/training/study-path/101722568130701625

## Useful references

**Core docs**
- Official docs home: https://developer.huawei.com/consumer/cn/doc/
- Getting started: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/application-dev-guide
- ArkTS language: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts
- ArkTS high-perf: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-high-performance-programming
- ArkUI framework: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkui
- State management: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-state-management-overview
- Navigation & routing: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-set-navigation-routing
- Animations: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-use-animation
- Concurrency: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/arkts-concurrency
- ArkData: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/data-mgmt-overview
- GC / garbage collection: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/gc-introduction

**Kit guides**
- Account Kit: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/account-kit-guide
- IAP Kit: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/iap-kit-guide
- Payment Kit: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/payment-kit-guide
- Push Kit: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/push-kit-guide
- Location Kit: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/location-kit
- Scan Kit: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/scan-kit-guide
- Live View Kit: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/live-view-kit-guide
- Core Vision Kit: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/core-vision-kit-guide
- Ads Kit: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ads-kit-guide

**IDE & tooling**
- DevEco Studio: https://developer.huawei.com/consumer/cn/deveco-studio/
- DevEco Testing: https://developer.huawei.com/consumer/cn/deveco-testing
- AI programming assistant (CodeGenie): https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-codegenie
- Code debugging: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-debugging
- Code linter: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-code-linter
- ArkUI previewer: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-previewer-arkui
- Layout inspector: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-arkui-inspector
- Emulator: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-emulator-create
- hvigorw CLI build: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-hvigor-commandline
- Testing overview: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/app-testing-overview

**Ecosystem**
- SDK / Kit overview: https://developer.huawei.com/consumer/cn/sdk
- OHPM package registry: https://developer.huawei.com/consumer/cn/deveco-service
- Samples catalog: https://developer.huawei.com/consumer/cn/samples/
- Knowledge map: https://developer.huawei.com/consumer/cn/app/knowledge-map
- Quick-start Codelab: https://developer.huawei.com/consumer/cn/codelabsPortal/getstarted/101718800110527001
- Design resources: https://developer.huawei.com/consumer/cn/design/resource
- HarmonyOS Symbol icons: https://developer.huawei.com/consumer/cn/design/harmonyos-symbol
- AppGallery Connect: https://developer.huawei.com/consumer/cn/agconnect
- App review policy: https://developer.huawei.com/consumer/cn/doc/app/50000
- Meta-service review: https://developer.huawei.com/consumer/cn/doc/app/50129
- Cangjie beta: https://developer.huawei.com/consumer/cn/activityDetail/cangjie-beta
- Doc change log: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/doc-updates
- API Diff (6.0.2): https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/apidiff-602
- Release overview (6.0): https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/overview-600
- StateStore best practice: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-global-state-management-state-store
- ArkCompiler: https://developer.huawei.com/consumer/cn/arkcompiler
