# Permissions Reference

Use this reference for HarmonyOS permission declaration and user authorization flows.

## Defaults

- Mention static declaration and runtime request when user authorization is required.
- Prefer HarmonyOS permission names, for example camera permission constants from Ability Kit.
- Include module configuration notes when code requires permissions.

## Answering pattern

1. Identify the required permission.
2. Add or verify the declaration in module configuration.
3. Request authorization at runtime when required.
4. Handle denied authorization gracefully.
5. Explain SDK-version-specific behavior when relevant.

## Review checklist

- Permission names are HarmonyOS permissions.
- Runtime request uses ability context correctly.
- Denial path is handled.
- API 26 permission behavior changes are not applied to API 24 production answers unless requested.
