# HarmonyOS AI Development Tools

Use this reference for DevEco Code, DevEco CLI, Agent Framework Kit, app Skills, Intents Kit, A2A, and HarmonyOS 7 AI-assisted development questions.

## Tool selection

| Need | Prefer |
|---|---|
| Full IDE editing, preview, profiling, signing, emulator, and graphical debugging | DevEco Studio |
| Agent-led HarmonyOS implementation and iterative build/run/verify/fix workflows | DevEco Code |
| Scriptable project, build, check, device, and debugging actions for Agents or CI/CD | DevEco CLI |
| General-purpose third-party coding Agent | Its native workflow plus DevEco CLI/Hvigor/HDC and this skill |

DevEco Code is a HarmonyOS-focused coding Agent, while DevEco CLI is the execution layer for command-line automation and Agent invocation. Use the project's SDK baseline; API 26.0.0 Release is the new-project default.

## Installation and verification

Official stable installation entries:

```sh
npm install -g @deveco/deveco-code@stable
npm install -g @deveco/deveco-cli@stable
npm list -g --depth=0
```

Record resolved versions for repeatable automation; `stable` can change. Use each installed package's help and official documentation for executable names, authentication, environment requirements, and commands. Verify a trusted test project's check/build/device-run flow before enabling CI. Installing these packages does not replace the matching SDK and signing environment.

HarmonyOS Dev Assistant is another plugin surface: it documents multi-device screen/camera adaptation, atomic-service generation, mini-program conversion, and library migration. Its Node.js requirements are plugin-specific; do not overwrite the SDK's bundled Node.js based on plugin advice.

## Agent capability boundaries

| Capability | Purpose |
|---|---|
| Agent Framework Kit | Let an app actively launch system Agent combinations through UI controls |
| Intents Kit | Declare app or atomic-service functions as system-recognizable intents |
| ArkTS script-based app Skill | Expose app business capabilities to system intelligent entry points through a declared contract |
| Device-side A2A | Connect an app-side Agent with system Agents using registered components, authenticated bidirectional communication, and interactive UI |
| AgentCard | Present Agent-related content or interaction through supported card capabilities |

Do not use these names interchangeably. First identify whether the user needs UI-triggered Agent invocation, intent exposure, an app Skill, Agent-to-Agent communication, or card presentation.

## HarmonyOS 7 capability notes

- Skill Vibe Coding assists app Skill development, debugging, review, and publishing.
- Visual AI, 3DGS, spatial-audio nodes, app/game quick start, cold-start network preconnection, QUIC, weak-network live-stream optimization, and LTPO variable frame rate are highlighted HarmonyOS 7 capability areas.
- Treat marketing-level capability descriptions as discovery signals, not stable API signatures. Verify the API 26 SDK reference, device category, permissions, and feature availability before generating production code.
- For cloud debugging, select API 26 Release devices; the historical `7.0.0.23` Beta image is not a Release validation substitute.

## Answer rules

1. State whether the request is about DevEco Studio, DevEco Code, DevEco CLI, or a third-party Agent.
2. Preserve existing API 24 settings; use API 26 Release guidance for new projects or deliberate upgrades.
3. Name the exact Agent capability layer instead of using generic terms such as "HarmonyOS Agent API."
4. Do not invent DevEco CLI command names. Use installed-tool help or official documentation for exact commands and flags.
5. For device-dependent capabilities such as LTPO or spatial audio, require SDK and hardware support verification.

Sources: [official tools](https://developer.huawei.com/consumer/cn/deveco-studio/), [Dev Assistant requirements](https://developer.huawei.com/consumer/cn/doc/start/hosdevassistant-install-deveco-0000002588359018), [September bulletin](https://developer.huawei.com/consumer/cn/monthly/202609).
