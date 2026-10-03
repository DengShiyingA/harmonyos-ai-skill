# HarmonyOS AI Development Tools

Use this reference for DevEco Code, DevEco CLI, Agent Framework Kit, app Skills, Intents Kit, A2A, and HarmonyOS 7/API 26 AI-assisted development questions.

## Official Source Lookup

- Huawei Developer Docs: `https://developer.huawei.com/consumer/cn/doc/`
- Use page-specific guide/reference URLs returned by official search or Context7; do not invent a documentation slug.
- Context7 Library IDs: `/websites/developer_huawei_consumer_cn_doc`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-guides`, `/websites/developer_huawei_consumer_cn_doc_harmonyos-references`
- Suggested query keywords: `DevEco Code, DevEco CLI, CodeGenie, Agent Framework Kit, Intents Kit, app Skill, AgentCard, device-side A2A`

Treat this file as a capability-routing snapshot. Verify current product names, installed CLI commands, SDK availability, and API signatures before answering.

## Tool selection

| Need | Prefer |
|---|---|
| Full IDE editing, preview, profiling, signing, emulator, and graphical debugging | DevEco Studio |
| Agent-led HarmonyOS implementation and iterative build/run/verify/fix workflows | DevEco Code |
| Scriptable project, build, check, device, and debugging actions for Agents or CI/CD | DevEco CLI |
| IDE-integrated AI assistant/plugin workflow | CodeGenie |
| General-purpose third-party coding Agent | Its native workflow plus DevEco CLI/Hvigor/HDC and this skill |

DevEco Code is a HarmonyOS-focused coding Agent, DevEco CLI is the command-line execution layer for automation and Agent invocation, and CodeGenie remains an IDE-integrated assistant surface. The current production SDK baseline is API 26.0.0 Release; retain API 24 Release only when the application explicitly supports older devices.

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
- For AGC cloud debugging, filter remote devices by API 26 or system version `7.0.0.23` when validating HarmonyOS 7 compatibility.

## Answer rules

1. State whether the request is about DevEco Studio, DevEco Code, DevEco CLI, or a third-party Agent.
2. Keep API 26.0.0 Release guidance separate from API 24 compatibility guidance.
3. Name the exact Agent capability layer instead of using generic terms such as "HarmonyOS Agent API."
4. Do not invent DevEco CLI command names. Use installed-tool help or official documentation for exact commands and flags.
5. For device-dependent capabilities such as LTPO or spatial audio, require SDK and hardware support verification.
