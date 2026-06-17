# Stage Model Reference

Use this reference for HarmonyOS application model, lifecycle, UIAbility, ExtensionAbility, AbilityStage, and migration from FA model.

## Defaults

- New HarmonyOS NEXT applications should use the Stage model.
- FA model is legacy and should only be recommended for migration context or legacy maintenance.
- Explain lifecycle and context usage in HarmonyOS terms, not Android Activity terms.

## Core concepts

- `AbilityStage`: application process-level initialization and callbacks.
- `UIAbility`: page window entry and foreground UI lifecycle.
- `WindowStage`: window creation and page loading.
- `ExtensionAbility`: background or system integration capability, depending on extension type.
- `module.json5`: declares abilities, permissions, and module metadata.

## Review checklist

- Correct ability type for the requested feature.
- No FA-model recommendation for new projects.
- Proper context passed to APIs that require ability context.
- Lifecycle side effects are placed in safe callbacks.
- Module configuration matches implementation code.
