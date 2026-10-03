# Testing, Debugging, Performance, and Memory

## Contents
- Testing — arkxtest framework
- JsUnit
- Debugging & tooling
- Memory-leak diagnostics (`jsLeakWatcher`, JS Heap, HWASan)
- UiTest — common patterns (arkxtest)
- Cold start optimization
- Lazy-import (`import()`)
- Network requests — defer until after first frame
- Other cold start rules
- Memory optimization
- `onMemoryLevel` callback
- LRUCache — bounded image / data cache
- Purgeable memory (large bitmaps)
- General memory rules

Load this file only when the user request matches these topics. For newer SDK claims, verify against official Huawei documentation when current accuracy matters.

## Official Source Lookup

- Huawei Developer Docs: `https://developer.huawei.com/consumer/cn/doc/`
- HarmonyOS guide pages: use page-specific docs under `developer.huawei.com/consumer/cn/doc/harmonyos-guides/...`; do not open the prefix as a standalone URL.
- HarmonyOS API reference pages: use page-specific docs under `developer.huawei.com/consumer/cn/doc/harmonyos-references/...`; do not open the prefix as a standalone URL.
- Context7 Library IDs: `/websites/developer_huawei_consumer_cn_doc`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-guides`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-references`
- Suggested query keywords: `arkxtest, JsUnit, UiTest, DevEco Testing, HiLog, AppFreeze, cold start, memory optimization, performance analysis`

Use the local notes below as a snapshot. For latest/current SDK behavior, exact API signatures, permission policy, or deprecation status, verify against Huawei official docs or Context7 before answering.

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

Test files in `entry/src/ohosTest/ets/test/`. For UI automation, see the **UiTest** section below.

**仓颉 (Cangjie)** is Huawei's new language (beta) — use ArkTS for all production apps until Cangjie is stable.


## Debugging & tooling

- **DevEco Studio** — primary IDE, includes emulator, previewer, profiler, HiLog viewer
- **hdc** — Harmony Device Connector (like adb): `hdc shell`, `hdc file send`, `hdc hilog`
- **HiLog** — logging: `hilog.info(0x0001, 'TAG', 'message %{public}s', arg)`
- **Instruments: SmartPerf / DevEco Profiler** — CPU/GPU/memory/energy profiling
- **DevEco Testing** — UI automation, performance testing, monkey/stress, compatibility

## Memory-leak diagnostics

Choose the smallest tool that can identify the suspected ownership layer:

| Suspected area | Prefer |
|---|---|
| ArkTS component or lifecycle object | `@ohos.hiviewdfx.jsLeakWatcher` during development |
| ArkTS heap retention path | DevEco Studio JS Heap / heap snapshot |
| Native allocation, free, or out-of-bounds error | HWASan / AddrSanitizer in development or test |
| Freeze or runtime resource pressure | AppFreeze, HiAppEvent, HiLog, DevEco Testing |

`jsLeakWatcher` periodically checks registered lifecycle objects that remain alive after they should be collectible. Treat it as a development diagnostic. If production diagnosis is unavoidable, limit it to a small gray-release population instead of enabling it permanently for all users.

Do not claim a leak is fixed from one snapshot. Reproduce the same lifecycle, collect comparable evidence, identify the retained ownership path, apply the fix, and repeat the scenario.

Use `$harmony-hdc-ui-automation` when the investigation needs focused HiLog capture, screenshots, layout trees, or repeated device-side reproduction.

Official reference: https://developer.huawei.com/consumer/cn/doc/best-practices/bpta-stability-memleak-detection-overview


## UiTest — common patterns (arkxtest)

```ts
import { describe, it, Level } from '@ohos/hypium';
import { abilityDelegatorRegistry, Driver, ON } from '@kit.TestKit';

export default function uiTest(): void {
  describe('UiTestSuite', () => {
    it('opens the target page', Level.LEVEL0, async () => {
      const delegator = abilityDelegatorRegistry.getAbilityDelegator();
      const bundleName = abilityDelegatorRegistry.getArguments().bundleName;
      await delegator.startAbility({
        bundleName,
        abilityName: 'EntryAbility'
      });

      const driver = Driver.create();
      await driver.waitForIdle(1000, 10_000);
      await driver.assertComponentExist(ON.text('首页'));

      const button = await driver.findComponent(ON.text('打开'));
      await button.click();
      await driver.waitForIdle(1000, 10_000);

      await driver.assertComponentExist(ON.text('详情'));
      await driver.pressBack();
    });
  });
}
```

Key rules:
- Every UiTest API call inside `it()` must be `await`ed
- After any click/input that changes state, component references may be stale — always re-`findComponent`
- Tests only run on real device or emulator — **Previewer does not support UiTest**
- `Driver.create()` fresh per `it` block (don't share across tests)
- Prefer `waitForIdle` / `delayMs` over fixed host-side sleeps
- Use `$harmony-hdc-ui-automation` for HDC execution, screenshots, layout dumps, hilog evidence,
  app sandbox transfer, and host-side Hypium Python automation


## Cold start optimization

HarmonyOS measures cold start as: **app launch → first frame rendered**. Target: < 1000ms on mid-range device.


### Lazy-import (`import()`)

```ts
// ❌ Eager — all modules parsed at startup even if unused
import { HeavyModule } from '../utils/HeavyModule';

// ✓ Lazy — parsed only when first used
let heavyModule: typeof import('../utils/HeavyModule') | null = null;

async function useHeavy() {
  if (!heavyModule) {
    heavyModule = await import('../utils/HeavyModule');
  }
  heavyModule.HeavyModule.doWork();
}
```


### Network requests — defer until after first frame

```ts
// EntryAbility.ets
onWindowStageCreate(windowStage: window.WindowStage) {
  windowStage.loadContent('pages/Index', (err) => {
    if (!err) {
      // First frame committed — now safe to start network
      AppStartupData.prefetch();
    }
  });
}
```


### Other cold start rules

- Avoid heavy synchronous work in `onCreate()` / `onWindowStageCreate()` — use TaskPool for >10ms tasks
- Minimize global singleton construction at module load time
- Use `@Reusable` on list item components to avoid remeasure/relayout on first display
- Avoid `hilog` calls inside tight rendering loops (I/O cost)
- Profile with DevEco Profiler → **Launch** task to see exact frame timeline


## Memory optimization


### `onMemoryLevel` callback

```ts
// AbilityStage.ets or UIAbility.ets
onMemoryLevel(level: AbilityConstant.MemoryLevel): void {
  if (level === AbilityConstant.MemoryLevel.MEMORY_LEVEL_CRITICAL) {
    // Release non-essential caches immediately
    ImageCache.instance.clear();
    DataCache.instance.trimToSize(10);
  } else if (level === AbilityConstant.MemoryLevel.MEMORY_LEVEL_LOW) {
    DataCache.instance.trimToSize(50);
  }
}
```


### LRUCache — bounded image / data cache

```ts
import { util } from '@kit.ArkTS';

class ImageCache {
  static instance = new ImageCache();
  private lru = new util.LRUCache<string, PixelMap>(50);  // max 50 entries

  put(key: string, pm: PixelMap) { this.lru.put(key, pm); }
  get(key: string): PixelMap | undefined { return this.lru.get(key); }
  clear() { this.lru.clear(); }
  trimToSize(n: number) {
    while (this.lru.length > n) {
      this.lru.afterRemoval(false, this.lru.keys()[0], undefined, undefined);
    }
  }
}
```


### Purgeable memory (large bitmaps)

```ts
import { image } from '@kit.ImageKit';

// Create PixelMap as purgeable — OS can reclaim when memory is tight,
// and will regenerate it from the source on next access
const pixelMap = await image.createPixelMap(buffer, {
  size: { width: 1920, height: 1080 },
  editable: false
});
// No extra API needed — PixelMap is automatically purgeable when editable=false
// and created from a decodable source (file path or buffer)
```


### General memory rules

- **Unregister listeners** in `aboutToDisappear()` / `onBackground()` to prevent leaks
- **Avoid capturing `this`** in long-lived closures (keeps component alive)
- **Reuse PixelMap objects** instead of recreating them for repeated renders
- Use `image.ImageSource` + lazy decode for thumbnails — don't decode full resolution
- TaskPool threads share no heap — `@Sendable` objects avoid copy but transfer ownership
