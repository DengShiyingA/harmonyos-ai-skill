# Recipe: Debug HarmonyOS Build Errors

Use this recipe when the user shares a DevEco Studio, Hvigor, ohpm, ArkTS, signing, or packaging error.

## Steps

1. Identify the error type:
   - ArkTS compile error
   - Hvigor build error
   - ohpm dependency error
   - SDK version mismatch
   - module or app configuration error
   - signing or certificate error
   - native / NAPI error
2. Confirm project baseline:
   - DevEco Studio version
   - compile SDK
   - target SDK
   - compatible SDK
   - Node.js version if relevant
3. Read the project's SDK configuration; distinguish an existing API 24 project from an API 26 Release upgrade. For Native/Node-API errors read `../references/ndk-napi.md` and `../references/native-api-compatibility.md`.
4. Provide one minimal fix first.
5. Provide a verification command or IDE action.

## Response format

- Problem type
- Likely cause
- Minimal fix
- Why it works
- Verification steps
- Follow-up data needed if still failing
