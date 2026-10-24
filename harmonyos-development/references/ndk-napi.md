# NDK / Node-API Development Rules

Use for ArkTS-to-C/C++ bindings, Native callbacks, TSFN, async work, handle leaks, and `.so` loading failures. Verified against official guidance on 2026-10-24. Check HarmonyOS SDK headers for availability; upstream Node.js support does not imply HarmonyOS support.

## Build and declaration contract

- Use the DevEco-generated Native C++ scaffold and its matched CMake/toolchain.
- Link Node-API bindings with `libace_napi.z.so` and include `napi/native_api.h`.
- Keep the CMake library target, `napi_module.nm_modname`, imported `lib<name>.so`, package metadata, and `.d.ts` exports aligned.
- Declare precise ArkTS parameter, callback, and Promise types; declarations do not validate runtime input.
- Package every dependent SO for the supported ABIs. A desktop binary is not a device library.
- Guard newer C APIs and link their providers; see `native-api-compatibility.md`.

## Thread and environment ownership

`napi_env`, `napi_value`, and `napi_ref` are environment-bound, not process-wide cross-thread handles. Use them only on their owning ArkTS thread while that environment is alive. A strong reference prevents collection; it does not make an object thread-safe. Multiple Workers require per-environment state rather than a single global env/callback.

Do not create/destroy an extra Ark runtime on an existing VM thread. Explicit runtime creation belongs on a dedicated native thread following the SDK lifecycle contract.

## One-shot asynchronous work

| Phase | Responsibility |
|---|---|
| Node-API entry | Validate arguments; copy native inputs; create Promise/callback reference and work context |
| `execute` | Compute using native data; do not access JS values through the originating env |
| `complete` | Check status; create JS results on the owning thread; settle the Promise or invoke callback; free work/reference/context |

Check both work creation and queueing. Queue failure needs immediate rollback; successful queueing transfers cleanup to completion. Cancellation does not prove completion: retain context until the completion path reports its status. Delete each `napi_async_work` once; do not reuse it or assume separate jobs execute in submission order.

## Native producer callbacks (TSFN)

Create `napi_threadsafe_function` on the owning ArkTS thread. Producers submit owned native data with `napi_call_threadsafe_function`; create JS values in `call_js_cb`.

- Size the queue from measured rate/latency. Zero means unlimited; use bounded queues with throttling/coalescing for high-frequency producers.
- `napi_tsfn_nonblocking` returns `napi_queue_full` when full. Failed submission retains payload ownership at the producer; successful submission transfers it to the receiving cleanup path.
- Stop submitting on `napi_closing`. Never use a TSFN after releasing that thread's ownership.
- Balance initial thread count and acquire/release. Environment teardown may deliver queued cleanup without a usable env/callback: free native payloads without executing JS.
- Stop/unsubscribe producers, synchronize in-flight callbacks, then release ownership. Do not block the ArkTS thread waiting for a producer blocked on its queue.

## Handles, memory, and error paths

- Check `napi_status`, argument count/types, lengths, and null pointers before using outputs. Preserve pending exceptions; stop normal execution when one is pending.
- Local handles expire with their scope. Pair opened handle scopes on every exit path; escape a returned handle when using an escapable scope.
- Use `napi_create_reference` for retained callbacks/objects and `napi_delete_reference` when finished on the owning thread. Weak references may no longer resolve.
- Give each wrapped/external allocation one owner. Coordinate explicit disposal and finalization to avoid double-free; finalizers must not depend on a live UI or arbitrary JS execution.
- Copy borrowed string/buffer data for asynchronous use unless lifetime and synchronization are explicitly guaranteed. TypedArray operations must respect byte offsets and lengths.
- Prevent C++ exceptions from escaping C callbacks. Keep creation, queue failure, cancellation, completion, and environment cleanup paths consistent.
- Use `napi_add_env_cleanup_hook` where supported to stop native sources on environment exit; coordinate it with normal disposal so resources are not freed twice. Never invoke JS after environment destruction.

## libuv and verification

Prefer Node-API async work and TSFN for common tasks. Do not run or close the system-owned loop, manipulate its timers from another thread, or use empty `uv_queue_work` jobs as cross-thread messaging. `uv_async_send` may coalesce notifications; do not assume one send equals one callback. Free a libuv handle only from its `uv_close` completion callback.

Verify release builds on supported ABIs and minimum/new API devices. Exercise invalid input, repeated start/stop, queue saturation, cancellation, page exit, and Worker/environment teardown; inspect crash logs and Native Leaks/HWASan results. A successful build does not verify lifetime safety.

## Sources

- [Huawei async-work guidance](https://developer.huawei.com/consumer/cn/doc/doccenter-capabilities/use-napi-asynchronous-task)
- [Huawei native-to-ArkTS communication](https://developer.huawei.com/consumer/cn/doc/doccenter-capabilities/native_subthread-to-uimain)
- [Huawei environment/thread FAQ](https://developer.huawei.com/consumer/cn/doc/doccenter-dev-faq/faqs-ndk-development-22)
- [Huawei libuv rules](https://developer.huawei.com/consumer/cn/doc/doccenter-references/api/libuv)
- [Upstream Node-API ownership and TSFN semantics](https://nodejs.org/api/n-api.html) (shared semantics only; confirm HarmonyOS API support)
