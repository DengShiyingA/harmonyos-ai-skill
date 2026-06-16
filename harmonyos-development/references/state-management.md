# ArkUI State Management

Use this file for ArkUI state decorators and reactive rendering decisions.

## Decision guide

| Need | Prefer |
|---|---|
| Local primitive state | `@State` |
| Parent to child one-way value | `@Prop` |
| Parent-child two-way binding | `@Link` |
| Object item passed into child row component | `@ObjectLink` with `@Observed` class |
| Cross-level dependency injection | `@Provide` / `@Consume` |
| App-level or storage-backed state | `@StorageLink` / `@StorageProp` |
| Page-level local storage | `@LocalStorageLink` / `@LocalStorageProp` |

## Rules

- Do not use `@ObjectLink` without an `@Observed` class.
- For list rows, prefer stable object models and stable keys.
- Explain whether changing an array element property triggers refresh in the chosen pattern.
- Avoid React hook analogies unless the user explicitly asks for comparison.

## Review checklist

- Correct decorator for ownership direction.
- No unnecessary global state.
- No accidental object identity loss.
- List updates have stable keys and predictable refresh behavior.
