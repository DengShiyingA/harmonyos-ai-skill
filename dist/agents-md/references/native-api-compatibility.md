# Native API Compatibility Reference

Use this reference when C/C++ code calls APIs newer than `compatibleSdkVersion`, or when a low-version device fails while loading a native library.

## Official Source Lookup

- Huawei Developer Docs: `https://developer.huawei.com/consumer/cn/doc/`
- Direct compatibility reference: `https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/c-api-compatibility-warning`
- Context7 Library IDs: `/websites/developer_huawei_consumer_cn_doc`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-guides`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-references`
- Suggested query keywords: `C API compatibility warning, weak reference, APIAVAILABLE, compatibleSdkVersion, weak library, target_link_options`

Context7 may not surface this release-note page for every query. Verify the direct official page and the headers/toolchain installed in the target project before changing compiler or linker settings.

## Core rule

Starting with SDK API 22, HarmonyOS can use C API weak references together with `APIAVAILABLE` to keep one native codebase compatible across system versions. This is an advanced mechanism: missing link dependencies can still compile successfully and then crash at runtime.

Do not treat any one of these as sufficient by itself:

- `compileSdkVersion`
- SystemCapability checks
- a preprocessor version check
- exception handling
- `APIAVAILABLE` without correct link configuration

## Hvigor projects

1. Use matching DevEco Studio and SDK versions.
2. Pass `compatibleSdkVersion` to the compiler to enable availability checks.
3. Link every library that provides a referenced API.
4. If the providing dynamic library does not exist on older devices, configure it as a weak library as well as a link dependency.
5. Wrap every newer API call with `APIAVAILABLE` and provide a fallback.
6. Test both the oldest compatible device and a device that supports the new API.

For DevEco Studio versions newer than 6.0.2.640 Release, except 6.1.0.830, add the matching argument in the module-level `build-profile.json5`:

```json5
{
  "buildOption": {
    "externalNativeOptions": {
      "arguments": "-DOHOS_COMPATIBLE_SDK_VERSION=20.0.0"
    }
  }
}
```

Use the exact configuration shape generated or documented for the installed DevEco Studio version. DevEco Studio 6.1.0.830 derives this value automatically; a stale manual value must be removed or kept synchronized.

## Link behavior

If the providing library exists on the old device, add it to `target_link_libraries`. If the library itself is absent on the old device, also mark it as weak:

```cmake
target_link_libraries(entry PUBLIC libohi18n.so)
target_link_options(entry PUBLIC "-Wl,--ohos-weak-library=libohi18n.so")
```

Temporarily disabling weak-reference support is a useful link-completeness check: the project should still identify every required library during a strong-link build.

## Runtime guard

`APIAVAILABLE` wraps the compiler availability check. The version must be at least the API version that introduced the function:

```cpp
if (APIAVAILABLE(26, 0, 0)) {
  // Call the API introduced in 26.0.0.
} else {
  // Compatible fallback for older devices.
}
```

Legacy HarmonyOS version `X.Y.Z(N)` and OpenHarmony API `N` use `N.0.0` in availability checks. The API version format changed to SemVer at 26.0.0, but the compatibility ordering remains:

`26.0.0 > 6.1.1(24) > 6.1.0(23) > 6.0.2(22)`.

## Required runtime verification

- Cold-start the app on a device matching `compatibleSdkVersion`.
- Exercise the old-device fallback path.
- Exercise the new API path on its supported SDK/device.
- Verify every referenced native library is linked.
- For libraries absent on old devices, verify weak-library configuration.
- Do not accept compilation alone as evidence: weak references can hide missing dependencies until runtime.

Official reference: https://developer.huawei.com/consumer/cn/doc/harmonyos-releases/c-api-compatibility-warning
