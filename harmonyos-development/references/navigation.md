# Navigation Reference

Use this reference when the user asks about routing, page stacks, Navigation, NavDestination, NavPathStack, or replacing legacy router patterns.

## Defaults

- Prefer Navigation and NavPathStack for new HarmonyOS NEXT applications.
- Keep route names, parameters, and page registration explicit.
- Mention SDK version assumptions when using newer Navigation behavior.

## Guidance

- Use a single source of truth for the navigation stack when possible.
- Avoid mixing unrelated routing approaches in one page tree.
- Keep page parameters typed and serializable.
- For nested navigation, explain stack ownership and back behavior clearly.

## Review checklist

- The navigation stack is owned by the right component or page shell.
- Back navigation is predictable.
- Parameters are typed and validated.
- Destination pages have clear names and lifecycle assumptions.
