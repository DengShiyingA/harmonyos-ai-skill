# Build, Signing, and Release Reference

Use this reference for DevEco Studio builds, Hvigor, ohpm, HAP/HAR/HSP packaging, signing, and release preparation.

## Defaults

- Confirm the production baseline before suggesting SDK or toolchain changes.
- API 24 Release is the default production target unless the user explicitly targets API 26 preview.
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

## Packaging notes

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
