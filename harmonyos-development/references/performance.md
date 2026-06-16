# HarmonyOS Performance Reference

Use this file for ArkUI performance, large lists, rendering, memory, and startup reviews.

## Checklist

- Prefer `LazyForEach` for large or dynamic lists.
- Use stable keys for list items.
- Avoid excessive nested layout containers.
- Avoid heavy work in render/build functions.
- Move IO, parsing, and expensive computation out of UI rendering.
- Use component reuse only when it matches the target SDK and the page pattern.
- Check image size, decode cost, cache policy, and lazy loading.
- Check ability lifecycle side effects and resource cleanup.

## Debug questions

Ask for:

- target SDK
- device model or emulator
- page route
- reproduction steps
- HiLog / AppFreeze / performance report
- screenshot or screen recording when UI jank is visual

## Output rule

Give prioritized fixes: quick wins first, then structural changes, then SDK/tooling checks.
