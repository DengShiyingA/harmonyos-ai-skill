# ArkTS Language, Strictness, and Concurrency

## Contents
- ArkTS language — strictness rules
- Naming conventions (official coding style guide)
- High-performance ArkTS rules (from official best practices)
- ArkCompiler — runtime details
- TaskPool vs Worker
- @Concurrent rules
- @Sendable — shared-heap reference passing
- Worker pattern

Load this file only when the user request matches these topics. For newer SDK claims, verify against official Huawei documentation when current accuracy matters.

## Official Source Lookup

- Huawei Developer Docs: `https://developer.huawei.com/consumer/cn/doc/`
- HarmonyOS guide pages: use page-specific docs under `developer.huawei.com/consumer/cn/doc/harmonyos-guides/...`; do not open the prefix as a standalone URL.
- HarmonyOS API reference pages: use page-specific docs under `developer.huawei.com/consumer/cn/doc/harmonyos-references/...`; do not open the prefix as a standalone URL.
- Context7 Library IDs: `/websites/developer_huawei_consumer_cn_doc`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-guides`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-references`
- Suggested query keywords: `ArkTS strict mode, ArkTS coding rules, TaskPool, Worker, @Concurrent, @Sendable, ArkCompiler`

Use the local notes below as a snapshot. For latest/current SDK behavior, exact API signatures, permission policy, or deprecation status, verify against Huawei official docs or Context7 before answering.

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
11. Use `HashMap` instead of `Record` for key-value operations — faster lookup/insert
12. Reduce multi-level indirect exports — prefer direct `export { foo } from './module'`
13. Use lazy import (`import lazy { Foo } from './heavy'`) for modules not needed at startup


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
