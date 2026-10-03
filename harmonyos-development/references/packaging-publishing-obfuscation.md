# Packaging, Publishing, and ArkGuard Obfuscation

## Contents
- Packaging types
- Publishing
- Linux CI, signing, and device smoke testing
- Code obfuscation (ArkGuard)
- Key obfuscation options
- Common whitelist scenarios (`-keep-property-name`)
- Whitelist for file names (`-keep-file-name`)
- Preserve specific names in source (`@KeepSymbol`)
- Gotchas

Load this file only when the user request matches these topics. For newer SDK claims, verify against official Huawei documentation when current accuracy matters.

## Official Source Lookup

- Huawei Developer Docs: `https://developer.huawei.com/consumer/cn/doc/`
- HarmonyOS guide pages: use page-specific docs under `developer.huawei.com/consumer/cn/doc/harmonyos-guides/...`; do not open the prefix as a standalone URL.
- HarmonyOS API reference pages: use page-specific docs under `developer.huawei.com/consumer/cn/doc/harmonyos-references/...`; do not open the prefix as a standalone URL.
- Context7 Library IDs: `/websites/developer_huawei_consumer_cn_doc`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-guides`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-references`
- Suggested query keywords: `HAP packaging, HSP, HAR, AppGallery Connect, publishing, ArkGuard, obfuscation-rules.txt, keep symbol`

Use the local notes below as a snapshot. For latest/current SDK behavior, exact API signatures, permission policy, or deprecation status, verify against Huawei official docs or Context7 before answering.

## Packaging types

| Type | Purpose |
|---|---|
| **HAP** (Harmony Ability Package) | Runnable module: `entry` or `feature` type |
| **HSP** (Harmony Shared Package) | In-app shared module, dynamic-linked at runtime |
| **HAR** (Harmony Archive) | Static library, packaged into HAP at build time |

Distribute via AppGallery Connect (华为应用市场).

Official samples: https://developer.huawei.com/consumer/cn/samples/


## Publishing

1. Obtain a HarmonyOS developer account, complete real-name verification
2. Generate signing certificate + profile in AppGallery Connect
3. Configure signing in `build-profile.json5`
4. Build release HAP/APP bundle: `hvigorw assembleApp`
5. Upload to **AppGallery Connect** for review

## Linux CI, signing, and device smoke testing

Use a 64-bit Linux environment with GLIBC 2.28 or newer, JDK 17, and the Command Line Tools that match the project SDK. Prefer the Node.js, Hvigor, ohpm, SDK, and HDC versions bundled with that toolchain instead of mixing globally installed versions.

Install dependencies at the project root and in modules that declare their own dependencies:

```sh
ohpm install --all
```

Run Hvigor without a persistent daemon in CI:

```sh
hvigorw clean --no-daemon
hvigorw assembleHap --mode module -p product=default -p buildMode=debug --no-daemon
hvigorw assembleHsp --mode module -p module=library@default -p product=default --no-daemon
hvigorw assembleHar --mode module -p module=library@default -p product=default --no-daemon
hvigorw assembleApp --mode project -p product=default -p buildMode=release --no-daemon
```

Linux is case-sensitive. Enable the project-level strict check so Windows and default macOS filesystems do not hide import or resource-name mismatches:

```json5
{
  "app": {
    "products": [{
      "name": "default",
      "compatibleSdkVersion": "<project-compatible-sdk>",
      "runtimeOS": "HarmonyOS",
      "buildOption": {
        "strictMode": {
          "caseSensitiveCheck": true
        }
      }
    }]
  }
}
```

Use the schema produced by the installed DevEco toolchain if it differs. Keep signing certificates, `.p12` files, profiles, passwords, and private keys in CI secrets; never print complete signing commands containing secrets.

After producing a signed HAP, use `$harmony-hdc-ui-automation` to select the target device, install and launch the package, capture HiLog evidence, and fail the pipeline when the smoke test fails. Keep exact HDC commands in that automation skill.

Official CI reference: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-command-line-building-app


## Code obfuscation (ArkGuard)

Enable in `build-profile.json5` → `arkOptions.obfuscation`. ArkGuard supports name obfuscation, code compression, and comment removal for ArkTS/TS/JS.


### Key obfuscation options

```
# obfuscation-rules.txt

-enable-property-obfuscation       # obfuscate property names
-enable-toplevel-obfuscation       # obfuscate top-level scope names
-enable-export-obfuscation         # obfuscate import/export names
-enable-filename-obfuscation       # obfuscate file/folder names
-enable-string-property-obfuscation  # also obfuscate string literal property names
-compact                           # remove whitespace and newlines
-remove-log                        # delete console.* statements
-print-namecache ./nameCache.json  # save name mapping (keep for crash analysis!)
```


### Common whitelist scenarios (`-keep-property-name`)

These properties **must** be whitelisted to avoid runtime errors:

```
-keep-property-name
# 1. Dynamic property access
# obj['x' + i]  → keep x0, x1, x2 ...
# Object.defineProperty(obj, 'y', {})  → keep y

# 2. JSON parsing fields
# JSON.parse / JSON.stringify → keep all serialized field names

# 3. Network request fields
# http.request extraData: { username, password } → keep field names

# 4. Database fields (ValuesBucket keys)
# relationalStore column names → keep

# 5. NAPI / .so interop
# import from 'libentry.so' → keep exported function names

# 6. ArkUI @Component @State properties are auto-preserved (no action needed)
# SDK API names are auto-preserved (no action needed)
```


### Whitelist for file names (`-keep-file-name`)

```
-keep-file-name
# System-loaded files that must not be renamed:
# - Worker thread files
# - Ability entry files  (auto-collected since DevEco 5.0.3.500)
# - Dynamic import paths:  const m = await import('./SomePath')
# - System route table paths (pageSourceFile in route_map.json, auto since API 20)
```


### Preserve specific names in source (`@KeepSymbol`)

```ts
// Since API 19: use comments to mark names as non-obfuscatable
// @KeepSymbol
class ImportantClass {
  // @KeepSymbol
  criticalProp: string = '';
}
```


### Gotchas

- ArkGuard uses **global** property whitelisting — if you keep `name`, ALL properties named `name` across all files are kept
- `enum` members are auto-collected into whitelist when building HAR with property obfuscation
- Always save `nameCache.json` per release — needed to decode obfuscated crash stacks
- `-compact` removes all newlines → crash stack line numbers become useless (column info not provided in release builds)
- String properties matching SDK API constants (e.g., `'ohos.want.action.home'`) are NOT auto-whitelisted — add them manually if used as property keys
