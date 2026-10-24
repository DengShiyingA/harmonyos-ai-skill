# Build, Signing, and Release Reference

Use this reference for DevEco Studio builds, Hvigor, ohpm, HAP/HAR/HSP packaging, signing, and release preparation.

## Defaults

- Confirm the production baseline before suggesting SDK or toolchain changes.
- Use the project's configured SDK baseline; new-project guidance uses API 26.0.0 Release. See `platform-baseline.md` for the matched toolchain and minimum-device policy.
- Keep generated `dist/` output separate from source skill files.

## Build debugging checklist

Ask for or inspect:

- DevEco Studio version
- compile SDK
- target SDK
- compatible SDK
- module configuration
- app configuration
- package configuration
- Hvigor error log
- signing profile or certificate error message

## Linux CI baseline

- Use a 64-bit Linux environment with GLIBC 2.28 or newer.
- Use JDK 17.
- Prefer the Node.js bundled with the matching Command Line Tools.
- The Command Line Tools include the matching HarmonyOS SDK, `hdc`, Hvigor, and ohpm.
- Run commands only for a trusted project.
- Keep signing keys and passwords in CI secrets, never in the repository.

Install dependencies at the project root and in every module that declares dependencies:

```sh
ohpm install --all
```

Build with `--no-daemon` in CI:

```sh
hvigorw clean --no-daemon
hvigorw assembleHap --mode module -p product=default -p buildMode=debug --no-daemon
hvigorw assembleHsp --mode module -p module=library@default -p product=default --no-daemon
hvigorw assembleHar --mode module -p module=library@default -p product=default --no-daemon
hvigorw assembleApp --mode project -p product=default -p buildMode=release --no-daemon
```

Linux is case-sensitive. Enable the project-level strict check so Windows/macOS development does not hide import or resource filename mismatches:

```json5
{
  "app": {
    "products": [
      {
        "name": "default",
        "compatibleSdkVersion": "26.0.0",
        "runtimeOS": "HarmonyOS",
        "buildOption": {
          "strictMode": {
            "caseSensitiveCheck": true
          }
        }
      }
    ]
  }
}
```

Use the configuration location generated for the installed toolchain if its project schema differs.

## Signing and device smoke test

- Prefer a project `signingConfigs` entry populated from CI secrets.
- For manual signing, use the Command Line Tools copy of `hap-sign-tool.jar`.
- Never print `.p12` passwords, private keys, or complete signing commands containing secrets.

Install and launch a signed HAP:

```sh
hdc file send entry-signed.hap data/local/tmp/entry-signed.hap
hdc shell bm install -p data/local/tmp/entry-signed.hap
hdc shell aa start -a EntryAbility -b com.example.myapplication -m entry
hdc shell rm -f data/local/tmp/entry-signed.hap
```

When multiple devices are connected, select the target explicitly. Capture HiLog and make the pipeline fail when installation, launch, or the smoke test fails.

## Packaging notes

DevEco Studio 26.0.0 Release adds `packOptions.deduplicateSo` in project `build-profile.json5` to remove duplicate SOs from app bundles, standalone merged bytecode HAR packaging, and dependencies selected by target/product/buildMode. Check the installed schema and test the packaged native libraries on each supported ABI before enabling these options.

| Package | Use |
|---|---|
| HAP | Entry or feature module output |
| HAR | Static shared library archive |
| HSP | Shared package for runtime reuse |

## Release checklist

- SDK versions are aligned.
- Permissions are declared.
- Signing profile is correct.
- Release build uses expected obfuscation and resource settings.
- Generated `dist/` is reproducible through CI.

Official CI reference: https://developer.huawei.com/consumer/cn/doc/harmonyos-guides/ide-command-line-building-app
