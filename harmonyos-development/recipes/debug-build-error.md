# Recipe: Debug HarmonyOS Build Errors

Use this recipe when the user shares a DevEco Studio, Hvigor, ohpm, ArkTS, signing, or packaging error.

## Steps

1. Identify the error type:
   - ArkTS compile error
   - Hvigor build error
   - ohpm dependency error
   - SDK version mismatch
   - `module.json5` / `app.json5` configuration error
   - signing or certificate error
   - native / NAPI error
2. Confirm project baseline:
   - DevEco Studio version
   - compile SDK
   - target SDK
   - compatible SDK
   - Node.js version if relevant
3. Check whether the answer must use API 24 production rules or API 26 preview rules.
4. Provide one minimal fix first.
5. Provide a verification command or IDE action.

## Response format

- Problem type
- Likely cause
- Minimal fix
- Why it works
- Verification steps
- Follow-up data needed if still failing
