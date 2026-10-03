# Navigation, Routing, and State Management

## Contents
- Router — basic page navigation
- EventHub — UIAbility ↔ page communication
- State-management decorators
- V2 state decorators (API 12+, **stable since API 23** — recommended for new code)
- StateStore — global state management (2026, officially recommended for mid-large apps)
- Navigation (recommended: Navigation component, not Router)

Load this file only when the user request matches these topics. For newer SDK claims, verify against official Huawei documentation when current accuracy matters.

## Official Source Lookup

- Huawei Developer Docs: `https://developer.huawei.com/consumer/cn/doc/`
- HarmonyOS guide pages: use page-specific docs under `developer.huawei.com/consumer/cn/doc/harmonyos-guides/...`; do not open the prefix as a standalone URL.
- HarmonyOS API reference pages: use page-specific docs under `developer.huawei.com/consumer/cn/doc/harmonyos-references/...`; do not open the prefix as a standalone URL.
- Context7 Library IDs: `/websites/developer_huawei_consumer_cn_doc`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-guides`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-references`
- Suggested query keywords: `HarmonyOS Navigation, NavPathStack, Router, EventHub, @State, @Prop, @Link, @Observed, @Trace, StateStore`

Use the local notes below as a snapshot. For latest/current SDK behavior, exact API signatures, permission policy, or deprecation status, verify against Huawei official docs or Context7 before answering.

### Router — basic page navigation

```ts
import { router } from '@kit.ArkUI';

// Push to new page (with params)
router.pushUrl({
  url: 'pages/Detail',
  params: { id: '123', title: 'Hello' }
});

// Get params on target page
const params = router.getParams() as Record<string, string>;

// Go back
router.back();

// Replace current page (no back stack)
router.replaceUrl({ url: 'pages/Login' });
```

> **Note**: For Navigation-based apps, prefer `NavPathStack.pushPath()` over Router.


### EventHub — UIAbility ↔ page communication

```ts
// In UIAbility — emit event
this.context.eventHub.emit('dataReady', { items: [...] });

// In page — subscribe
const context = getContext(this) as common.UIAbilityContext;
context.eventHub.on('dataReady', (data: Record<string, ESObject>) => {
  this.items = data.items;
});

// Unsubscribe
context.eventHub.off('dataReady');
```


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


### V2 state decorators (API 12+, **stable since API 23** — recommended for new code)

> V2 decorators have **graduated from experimental to stable** as of HarmonyOS 6.1 (API 23). Official recommendation: migrate to V2 for new projects.

| V1 | V2 replacement | Change |
|---|---|---|
| `@Component` | `@ComponentV2` | Clearer semantics |
| `@State` | `@Local` | Cannot be initialized externally — internal state only |
| `@Prop` | `@Param` + `@Once` | Read-only inputs; `@Once` for one-time init |
| `@Link` | `@Param` + `@Event` | Two-way: input via `@Param`, output via callback `@Event` |
| `@Observed` + `@ObjectLink` | `@ObservedV2` + `@Trace` | **Deep observation** across multiple nested levels |
| `@Watch` | `@Monitor('prop')` | More precise deep listener |
| `AppStorage` | `AppStorageV2` | Unified with `@ObservedV2` + `@Trace` |
| (none) | `PersistenceV2` | Persistent storage with V2 observation; auto-saved to disk |
| `@Provide` / `@Consume` | `@Provider()` / `@Consumer()` | Renamed; same semantics |

```ts
@ObservedV2
class UserInfo {
  @Trace name: string = '';    // changes to this trigger UI refresh
  @Trace age: number = 0;     // changes to this trigger UI refresh
  address: string = '';        // NO @Trace → changes do NOT trigger refresh
}
```
Rules: `@ObservedV2` and `@Trace` must be used together (either alone has no effect). Only `@Trace`-decorated properties participate in UI rendering.

**AppStorageV2 — global reactive state:**
```ts
import { AppStorageV2 } from '@kit.ArkUI';

@ObservedV2
class UserState { @Trace name: string = 'Guest'; }

// Connect (creates if not exists)
const user = AppStorageV2.connect(UserState, 'user', () => new UserState())!;

// In component
@ComponentV2
struct Header {
  user: UserState = AppStorageV2.connect(UserState, 'user')!;
  build() { Text(this.user.name) }
}
```

**PersistenceV2 — auto-persisted state (survives app restart):**
```ts
import { PersistenceV2, Type } from '@kit.ArkUI';

@ObservedV2
class Settings {
  @Trace @Type(String) theme: string = 'light';
  @Trace @Type(Number) fontSize: number = 14;
}

// Connect — auto-loads from disk if exists, writes on change
const settings = PersistenceV2.connect(Settings, 'app_settings', () => new Settings())!;

// Optional: error/success callback
PersistenceV2.notifyOnError((key, reason, msg) => { console.error(reason, msg); });
```
> `@Type` decorator is required for PersistenceV2 to serialize correctly.


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

The older `router` module (`@ohos.router`) still works but **is being phased out** — `Navigation` + `NavPathStack` is the official replacement since API 12+. Huawei publishes a [transition guide](https://device.harmonyos.com/en/docs/apiref/harmonyos-guides/arkts-router-to-navigation) for migrating from router to Navigation. For new projects, always use Navigation; for legacy code, migrate when convenient.

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
