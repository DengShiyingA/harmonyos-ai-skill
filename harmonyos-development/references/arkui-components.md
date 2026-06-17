# ArkUI Components Reference

Use this reference when the user asks about ArkUI layout, components, rendering, interaction, or page implementation.

## Defaults

- Prefer declarative ArkUI component examples in `.ets` files.
- Use HarmonyOS-native components and APIs instead of React, DOM, Android View, or Jetpack Compose patterns.
- State the target SDK assumption when behavior depends on SDK version.

## Component guidance

| Need | Prefer |
|---|---|
| Vertical layout | `Column` |
| Horizontal layout | `Row` |
| Overlay / layered layout | `Stack` |
| Flexible wrapping layout | `Flex` |
| Large lists | `List` + `LazyForEach` |
| Grid content | `Grid` / `GridItem` |
| Paged tabs | `Tabs` / `TabContent` |
| Swipe carousel | `Swiper` |
| Navigation shell | `Navigation` / `NavDestination` |

## Review checklist

- Keep layout nesting reasonable.
- Avoid heavy computation inside `build()`.
- Use stable keys for dynamic list rendering.
- Keep component state ownership clear.
- Include permission, routing, or module configuration when the component depends on it.
