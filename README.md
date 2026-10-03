<div align="center">

[English](./README_EN.md) | **简体中文**

<img src="./assets/hero-banner.svg" alt="HarmonyOS AI Skill" width="100%"/>

# 🧠 HarmonyOS AI Skill

### 鸿蒙最大的 AI 编程知识库 · 让 11+ AI 工具真正会写 ArkTS

*2 个职责分离的 Skill · 轻量路由 + 19 个按需 reference 模块 · 生产覆盖 HarmonyOS 7 / API 26 Release，兼容 API 24*

[![License](https://img.shields.io/badge/License-MIT-yellow)](./LICENSE)
[![HarmonyOS](https://img.shields.io/badge/HarmonyOS-7%20%2F%20API%2026-black)](https://developer.huawei.com/consumer/cn/)
[![ArkTS](https://img.shields.io/badge/ArkTS-API%2022--26-blue)](https://developer.huawei.com/consumer/cn/doc/harmonyos-guides-V5/arkts-get-started-V5)
[![Kits](https://img.shields.io/badge/Kits-60+-orange)](#知识包内容)
[![AI Tools](https://img.shields.io/badge/AI_Tools-11+-purple)](#支持的-ai-工具)
[![AGENTS.md](https://img.shields.io/badge/AGENTS.md-Standard-green)](https://agents.md)

[![Stars](https://img.shields.io/github/stars/Fly0307/harmonyos-ai-skill?style=social)](https://github.com/Fly0307/harmonyos-ai-skill/stargazers)
[![Last Commit](https://img.shields.io/github/last-commit/Fly0307/harmonyos-ai-skill/zx-dev)](https://github.com/Fly0307/harmonyos-ai-skill/commits/zx-dev)
[![Issues](https://img.shields.io/github/issues/Fly0307/harmonyos-ai-skill)](https://github.com/Fly0307/harmonyos-ai-skill/issues)

<br/>

**问 Cursor 怎么写 ArkUI，它给你输出 React 组件？**
**让 Claude 改 `module.json5`，它当 `package.json` 改？**
**问 Copilot `@ObjectLink` 怎么用，它说"这 API 不存在"？**

通用大模型从来没系统学过鸿蒙——它们的训练数据里几乎没有 ArkTS、Stage 模型、HarmonyOS Kit。
所以我把华为官方文档、最佳实践、API 参考整理成**轻量路由 + 按需 references** 的知识库，从 ArkTS 严格语法到 60+ Kit、从 Native API 兼容到 API 26 Release 升级适配都可精确检索；设备操作则由独立的 HDC 自动化 Skill 负责。

**两套原生 Skill，开发知识自动适配 11+ AI 工具。** 支持原生 Skill 的
Agent 只按需加载相关模块；单文件规则工具使用构建生成的完整开发知识包。

<br/>

[🚀 安装](#安装) · [📖 知识内容](#知识包内容) · [🛠️ 支持的工具](#支持的-ai-工具) · [✅ 验证效果](#验证是否生效)

</div>

---

<div align="center">
<img src="./assets/before-after.svg" alt="装前 vs 装后对比" width="100%"/>
</div>

---

## ⚡ 快速开始（Claude Code，30 秒）

按你的系统选择对应命令——**直接复制粘贴**到终端即可：

### 🍎 macOS

```bash
git clone -b zx-dev https://github.com/Fly0307/harmonyos-ai-skill.git ~/src/harmonyos-ai-skill
mkdir -p ~/.claude/skills
ln -s ~/src/harmonyos-ai-skill/harmonyos-development ~/.claude/skills/harmonyos-development
ln -s ~/src/harmonyos-ai-skill/harmony-hdc-ui-automation ~/.claude/skills/harmony-hdc-ui-automation
# 重启 Claude Code，然后问："What skills are available?"
```

### 🐧 Linux

```bash
git clone -b zx-dev https://github.com/Fly0307/harmonyos-ai-skill.git ~/src/harmonyos-ai-skill
mkdir -p ~/.claude/skills
ln -s ~/src/harmonyos-ai-skill/harmonyos-development ~/.claude/skills/harmonyos-development
ln -s ~/src/harmonyos-ai-skill/harmony-hdc-ui-automation ~/.claude/skills/harmony-hdc-ui-automation
# 重启 Claude Code，然后问："What skills are available?"
```

### 🪟 Windows（PowerShell 7+）

> ⚠️ **必须在 PowerShell 中运行，不要用 CMD（命令提示符）**——`New-Item` 是 PowerShell 命令，CMD 不认识。右键开始菜单 → "Windows PowerShell（管理员）"。

```powershell
# 先开启「开发人员模式」：设置 → 隐私和安全性 → 开发者选项 → 打开（一次性）
git clone -b zx-dev https://github.com/Fly0307/harmonyos-ai-skill.git $HOME\src\harmonyos-ai-skill
New-Item -ItemType Directory -Force $HOME\.claude\skills | Out-Null
New-Item -ItemType SymbolicLink -Path $HOME\.claude\skills\harmonyos-development -Target $HOME\src\harmonyos-ai-skill\harmonyos-development
New-Item -ItemType SymbolicLink -Path $HOME\.claude\skills\harmony-hdc-ui-automation -Target $HOME\src\harmonyos-ai-skill\harmony-hdc-ui-automation
# 重启 Claude Code，然后问："What skills are available?"
```

> 不想开启开发者模式？可将两个目录分别 `Copy-Item -Recurse` 到
> `$HOME\.claude\skills\`（但上游更新后需要重新复制）。

用其他工具（Cursor / Copilot / ChatGPT ...）？查看[下方完整安装指南](#安装)。

---

## 为什么需要这个？

| 问题 | 普通 AI | 装上 Skill 后 |
|---|---|---|
| 用什么写 UI？ | "用 React Native 啊" | "用 ArkUI，`@Component struct` 声明式组件" |
| 状态怎么管？ | "useState / Redux" | "`@State` / `@ObjectLink`，新项目用 V2 装饰器（API 23 已稳定）" |
| 路由跳转？ | "react-router 或 Vue Router" | "`Navigation` + `NavPathStack.pushPath()`，Router 已被淘汰" |
| HTTP 请求？ | "axios / fetch" | "`@kit.NetworkKit` 的 `http.createHttp()`，或 `@ohos/axios` 三方库" |
| 申请相机权限？ | 给一段 Android Manifest | `module.json5` 配置 + `abilityAccessCtrl` 三步流程（含 settings 降级） |
| 后台播放音乐？ | 模糊提示需要 service | "必须创建 AVSession + 申请 `KEEP_BACKGROUND_RUNNING` 长时任务" |

知识不在 AI 脑子里，得喂进去。**这就是这个仓库做的事。**

开发知识维护在 [`harmonyos-development`](./harmonyos-development/) 的路由层与按需资源中；设备控制维护在独立的 [`harmony-hdc-ui-automation`](./harmony-hdc-ui-automation/) Skill 中。构建器会完整分发两套原生 Skill，并将开发知识转换为各工具所需的规则文件。

<details>
<summary><b>🤔 什么是 "skill"（技能包）？</b>（点击展开）</summary>

Skill 是一段领域知识（Markdown 格式），AI 编程工具会在对话时自动加载为背景上下文。安装后，AI 就"知道"了这个领域——它会给出符合 HarmonyOS 规范的回答，而不是泛泛的 TypeScript / React 建议。不同工具叫法不同（skills、rules、instructions、system prompt），但原理一样：**额外文本被插入到模型的上下文中**。

</details>

## 🧭 渐进式加载：先路由，再按需取知识

这个仓库的核心机制是**渐进式加载**。它不会把所有 HarmonyOS 说明一次性塞进一个巨型 Markdown，再让每次会话重复加载全部内容；Agent 先读取一个很短的路由入口，再根据当前任务打开最小必要的模块。

| 层级 | 内容 | 加载方式 |
|---|---|---|
| `harmonyos-development/SKILL.md` | 主题路由、官方来源、reference 选择规则 | 原生 Skill 触发时先加载 |
| `references/` | ArkTS、ArkUI、工程、Kit、权限、网络、测试等领域模块 | 根据任务主题按需加载 |
| `recipes/`、`examples/` | 编译排错、代码审查和可运行示例 | 只有需要工作流或代码时加载 |
| `harmony-hdc-ui-automation/` | HDC、UiTest、hilog、截图和设备文件操作 | 设备任务单独触发 |
| `dist/agents-md/AGENTS.md` | 面向 AGENTS.md 工具的轻量路由入口 | 每次会话先加载短文件，再解析同级目录 |
| `dist/*` 单文件产物 | 将路由和全部 references 展平后的兼容版本 | 仅供无法读取多个文件的工具使用 |

因此，原生 Skill 和轻量 `AGENTS.md` 安装方式能保持较小上下文；`AGENTS.full.md`、`dist/plain` 和 `dist/system-prompt` 是兼容不支持渐进加载的工具的后备产物。两种方式来自同一套源文件，运行构建器即可同步更新。

## 📌 当前 API 支持

当前文档基线是 **HarmonyOS 7 / API 26.0.0 Release**。知识库覆盖 API 26 的 SemVer 版本规则、ArkUI `ContainerReader` 和全局复用、`ComposeTitleBarV2`、API Change Assistant、Node.js 24 工具链，以及 Agent Framework、Data Augmentation、Enterprise Space、Desktop Extension、Spatial Recon 等 Kit。API 24 Release 仍作为旧设备兼容基线保留。

API 26 工程配置和升级指导重点包括：`compileSdkVersion`、`targetSdkVersion`、`compatibleSdkVersion` 使用字符串版本号；升级后用 API Change Assistant 检查行为变化，并在旧设备与 API 26 设备上分别验证。当前记录的 Release 工具链为 DevEco Studio 26.0.0.821、Hvigor 6.26.4、ohpm 26.0.0.630、Node.js 24.14.1。

官方入口：

- [HarmonyOS 26.0.0 版本说明](https://developer.huawei.com/consumer/cn/doc/doccenter-release-notes/2600)
- [升级到 26.0.0 适配指南](https://developer.huawei.com/consumer/en/doc/harmonyos-releases/upgrade-adaptation)
- [DevEco Studio 26.0.0 Release](https://developer.huawei.com/consumer/en/doc/harmonyos-releases/deveco-studio-new-features-2600)

**使用规则文件：** 只需 `git` 和 `curl`（或直接复制文件）。
**使用双 Skill 安装器、HDC 自动化或参与开发：** 需要 Python 3.10+；
推荐使用 `uv` 和项目现有的 `.venv`。真机能力还需要 DevEco Studio /
HarmonyOS SDK、`hdc` 以及已连接的设备或模拟器。
**保鲜度：** 跟随官方版本节奏更新。当前基线覆盖到 HarmonyOS 7 / 26.0.0 Release（API 26；DevEco Studio 26.0.0.821），同时保留 HarmonyOS 6.1.1 Release（API 24）兼容指引。

## 知识包内容

<div align="center">
<img src="./assets/knowledge-map.svg" alt="知识架构图" width="100%"/>
</div>

`harmonyos-development/SKILL.md` 只负责主题路由，详细知识分布在 19 个 references、2 个 recipes、2 个可运行示例和行为 eval 中：

- **语言与框架** — ArkTS 严格模式规则、命名规范、13 条高性能编码规则（const、TypedArray、HashMap、lazy import 等）、编码风格指南
- **应用架构** — Stage 模型：UIAbility、ExtensionAbility、AbilityStage、WindowStage 生命周期；module.json5 / app.json5 配置
- **ArkUI 组件** — 组件生命周期（7 个回调 + 执行顺序）、布局容器（Column/Row/Stack/Flex/RelativeContainer/List）性能对比、`@Reusable` 组件复用、**Tabs 底部导航**、**Swiper 轮播**、**WaterFlow 瀑布流**、**Grid 网格**、**TextInput 输入框**、**AlertDialog/Toast**、10 种表单组件速查、AttributeModifier 可复用样式
- **状态管理（V2 已稳定）** — V1 装饰器（`@State`/`@Prop`/`@Link`/`@Provide`-`@Consume`/`@Observed`+`@ObjectLink`/`@Watch`）+ V2 装饰器（`@ComponentV2`/`@Local`/`@Param`+`@Once`/`@Param`+`@Event`/`@ObservedV2`+`@Trace`/`@Monitor`）+ **AppStorageV2** + **PersistenceV2**（自动持久化）+ StateStore 全局状态，含观察深度规则、批量更新、装饰器选择优先级
- **导航路由** — `Navigation` + `NavPathStack` 完整 API、`Router` 基础路由（已弃用，含迁移说明）、`App Linking` 深链接
- **动画** — `animateTo()`、`.animation()`、`keyframeAnimateTo()`、Curve 枚举、弹簧曲线、`geometryTransition` 共享元素转场、动画性能提示
- **列表操作** — 下拉刷新（Refresh）、上拉加载（onReachEnd）、左滑删除（swipeAction）、拖拽排序、ListItemGroup 分组粘性头、滚动到底部、保持滚动位置
- **性能优化** — `LazyForEach` + IDataSource、`@Reusable`、`cachedCount`、`onVisibleAreaChange`、冷启动优化（lazy import）、内存优化（LRUCache/Purgeable）
- **HarmonyOS Kits** — 7 大类 60+ Kit 含 import key + 代码示例
- **Kit 详细章节** — Camera Kit（含 API 24 Follow the Person 主体追踪）、Audio Kit、AVPlayer/AVRecorder、Image Kit（decode/transform/encode）、Scan Kit、Account Kit、Payment Kit、Push Kit、Map Kit、**Weather Service Kit**、Core Vision Kit（OCR/人脸/抠图）、Form Kit（服务卡片）、AVSession Kit、Location Kit、Notification Kit、Share Kit
- **数据持久化** — relationalStore（SQLite CRUD + sendable）、preferences（KV 存储）、fileIo（文件读写）、DocumentViewPicker（文件选择器）
- **网络** — HTTP 请求、WebSocket、网络状态监听、后台上传下载（request.agent 断点续传）
- **并发** — TaskPool vs Worker 对比、`@Concurrent` 规则、`@Sendable` 共享堆机制
- **系统能力** — 权限申请完整流程（check→request→settings 降级）、沉浸式窗口（expandSafeArea/避让区）、深色模式（资源限定词/colorMode 监听）、软键盘适配（KeyboardAvoidMode）、横竖屏切换、剪贴板、自定义字体、桌面快捷方式、手势冲突处理（hitTestBehavior/priorityGesture）、EventHub 事件通信、startAbilityByType
- **Web** — ArkWeb 组件、JS↔ArkTS 桥接、Cookie 管理、请求拦截
- **跨设备** — 应用接续（onContinue/onCreate 数据迁移）、跨模块资源访问（HAR/HSP）
- **工程质量** — 安全编码规则 + 网络安全配置（HTTPS/证书固定）、代码混淆（ArkGuard）、arkxtest 测试框架（JsUnit + UiTest）、18 条常见陷阱（gotchas）
- **三方库** — @ohos/axios（HTTP 客户端）、@ohos/pulltorefresh（下拉刷新）、@ohos/lottie（JSON 动画）、@ohos/imageknife（图片缓存）、dayjs（日期处理）
- **API 23 / 24 新特性** — Navigation 路由栈绑定、Menu anchorPosition、UDMF/drag/crypto C API、relationalStore sendable 增强、AI super frame、Camera Kit "Follow the Person" 主体追踪、延迟预览、DevEco Studio API 24 支持
- **API 26 Release** — HarmonyOS 7 生产基线、26.0.0 SemVer、ArkUI `ContainerReader`/全局复用/ComposeTitleBarV2、API Change Assistant、Node.js 24 工具链、升级兼容与旧设备验证
- **最新兼容与调测** — Native `APIAVAILABLE`/弱引用、Linux CI、`jsLeakWatcher`、HWASan、`ContainerReader` 容器断点、全局组件复用
- **多设备** — 响应式断点（xs/sm/md/lg/xl）、GridRow/GridCol、折叠屏适配
- **打包与工具** — HAP/HSP/HAR、原子化服务、DevEco Studio 6.1+（hvigor）、OHPM、ArkCompiler

---

## 支持的 AI 工具

### 先选择正确的分发方式

| 使用场景 | 推荐产物 | 上下文行为 | HDC 自动化 |
|---|---|---|---|
| Codex、Claude Code 等支持原生 Skill 的 Agent | `harmonyos-development/` + `harmony-hdc-ui-automation/` | 先加载短 `SKILL.md`，再按任务读取 references、recipes 或 examples | 支持，独立按需触发 |
| 支持项目级 `AGENTS.md` 且能读取仓库文件的 Agent | `dist/agents-md/AGENTS.md` + 同目录的 `references/`、`recipes/`、`examples/` | 轻量渐进加载 | 不包含执行器；需要时另装 HDC Skill |
| 只能接收一个规则文件的工具 | 对应 `dist/` 文件，或 `dist/agents-md/AGENTS.full.md` | 一次性内嵌完整开发知识 | 不包含执行器 |

不要只复制原生 Skill 的 `SKILL.md`，也不要单独复制轻量
`AGENTS.md`：它们都依赖同级的按需资源目录。

### 1. 原生 skill 格式（按描述自动匹配加载）

| 工具 | 安装路径 | 激活方式 |
|---|---|---|
| **Claude Code CLI** | `~/.claude/skills/harmonyos-development/`、`~/.claude/skills/harmony-hdc-ui-automation/` | Claude 根据两份 `SKILL.md` 的 `description` 分别加载开发知识或设备自动化能力 |
| **Claude Agent SDK** | 将两个完整 Skill 目录放在任意位置，通过 SDK 的 `skills` 参数指定 | 同 Claude Code，按职责分别触发 |
| **OpenAI Codex 项目 skill** | `.agents/skills/harmonyos-development/`、`.agents/skills/harmony-hdc-ui-automation/` | 开发类任务加载核心知识 skill；真机检查、HDC、UiTest、hilog 和沙箱文件操作加载自动化 skill |

### 2. 项目规则文件（项目内每次会话自动附加）

| 工具 | 安装路径 | 源文件 | 作用域 |
|---|---|---|---|
| **Cursor**（现代版） | `.cursor/rules/harmonyos.mdc` | `dist/cursor/harmonyos.mdc` | 按 glob 匹配 `*.ets`、`module.json5`、`oh-package.json5`、`build-profile.json5` |
| **Cursor**（旧版） | `.cursorrules`（仓库根目录） | `dist/cursor/.cursorrules` | 始终生效 |
| **GitHub Copilot** | `.github/copilot-instructions.md` | `dist/copilot/copilot-instructions.md` | 仓库内始终生效 |
| **Windsurf / Codeium** | `.windsurfrules`（仓库根目录） | `dist/windsurf/.windsurfrules` | 始终生效 |
| **Continue.dev** | `.continue/rules/harmonyos.md` | `dist/continue/harmonyos.md` | 始终生效 |
| **Cline / Roo Code** | Settings → Custom Instructions | `dist/cline/custom-instructions.md` | 按工作区或全局 |
| **OpenAI Codex CLI · sst/opencode · Amp · Aider · Jules** | `AGENTS.md`（仓库根目录） | `dist/agents-md/AGENTS.md` | 遵循 [AGENTS.md](https://agents.md) 标准 |
| **Google Gemini CLI** | `GEMINI.md`（仓库根目录）或 `~/.gemini/GEMINI.md`（全局） | `dist/gemini-cli/GEMINI.md` | Gemini CLI 读取任一路径 |

### 3. 通用 —— 粘贴到任何聊天 / API

| 工具 | 粘贴位置 | 源文件 |
|---|---|---|
| **ChatGPT / GPT-4 / GPT-5** | Settings → Personalization → Custom Instructions（或单次对话 system prompt） | `dist/plain/harmonyos-knowledge.md` |
| **Google Gemini / AI Studio** | System Instructions 字段 | `dist/plain/harmonyos-knowledge.md` |
| **DeepSeek / Qwen / 文心一言 / Kimi / 智谱** | 系统提示 / 角色设定字段 | `dist/plain/harmonyos-knowledge.md` |
| **Ollama 本地模型** | `--system` 参数 | `dist/system-prompt/system.txt` |
| **Anthropic / OpenAI / 任意 LLM API** | 请求体的 `system` 消息 | `dist/system-prompt/system.txt` |

两个文件区别很小：`plain/` 是原始 Markdown；`system-prompt/` 在前面加了一句角色定位（*"You are an expert HarmonyOS NEXT developer…"*）。

---

## 安装

当前上游目标为 [`Fly0307/harmonyos-ai-skill` 的 `zx-dev` 分支](https://github.com/Fly0307/harmonyos-ai-skill/tree/zx-dev)。

下方所有 `curl` 命令都使用环境变量 `$RAW` —— **每个新终端首次使用前都需要先运行一次**：

```bash
export RAW=https://raw.githubusercontent.com/Fly0307/harmonyos-ai-skill/zx-dev
```

> **Windows PowerShell 用户：** 用 `$env:RAW = "..."`，并把下方 `curl -o foo` 改为 `Invoke-WebRequest -Uri "..." -OutFile foo`。
> **HOME 路径差异：** macOS/Linux 是 `~`；Windows PowerShell 是 `$HOME`；CMD 是 `%USERPROFILE%`。

### Claude Code CLI

以下方式都会安装两个完整 Skill。不要只下载 `SKILL.md`，否则开发 Skill
无法继续读取 references、recipes 和 examples，自动化 Skill 也会缺少脚本与配置模板。

```bash
# 方式 A — 符号链接（推荐：仓库 git pull 后立即同步）
git clone -b zx-dev https://github.com/Fly0307/harmonyos-ai-skill.git ~/src/harmonyos-ai-skill
mkdir -p ~/.claude/skills
ln -s ~/src/harmonyos-ai-skill/harmonyos-development ~/.claude/skills/harmonyos-development
ln -s ~/src/harmonyos-ai-skill/harmony-hdc-ui-automation ~/.claude/skills/harmony-hdc-ui-automation

# 方式 B — 直接复制（获得静态快照）
cp -R ~/src/harmonyos-ai-skill/harmonyos-development ~/.claude/skills/
cp -R ~/src/harmonyos-ai-skill/harmony-hdc-ui-automation ~/.claude/skills/

# 方式 C — 仅当前鸿蒙项目使用
cd <你的鸿蒙项目根目录>
mkdir -p .claude/skills
cp -R ~/src/harmonyos-ai-skill/harmonyos-development .claude/skills/
cp -R ~/src/harmonyos-ai-skill/harmony-hdc-ui-automation .claude/skills/
```

安装后**重启 Claude Code**。验证方法：问 *"What skills are available?"*，
应同时列出 `harmonyos-development` 和 `harmony-hdc-ui-automation`。

### OpenAI Codex 项目内安装

`harmonyos-development` 负责 ArkTS、ArkUI、Stage 模型和工程开发知识；
`harmony-hdc-ui-automation` 负责真实设备的 HDC/UiTest 控制、截图、布局树、
hilog、应用沙箱文件传输及 UI 自动化。它们位于同一仓库但保持独立触发，
在 HarmonyOS 项目中应同时安装：

```bash
cd <你的鸿蒙项目根目录>
source .venv/bin/activate
uv run --active python ~/src/harmonyos-ai-skill/scripts/install_skills.py \
  --project . \
  --mode link
```

Windows 未开启开发人员模式，或文件系统不支持符号链接时，改用
`--mode copy`。安装器不会覆盖已有目录；可用 `--dry-run` 先检查目标。
只需要其中一个 Skill 时，可追加
`--skills harmonyos-development` 或
`--skills harmony-hdc-ui-automation`。

自动化 skill 使用当前项目的 UV 环境，不依赖固定的 `.venv` 路径。首次使用时，
把配置模板复制为项目根目录的 `.harmony-hdc.json`，填写 `bundleName`、
`moduleName` 和 `abilityName`，然后运行：

```bash
cp .agents/skills/harmony-hdc-ui-automation/assets/harmony-hdc.example.json \
  .harmony-hdc.json
uv run --active python .agents/skills/harmony-hdc-ui-automation/scripts/harmony_hdc_ui.py doctor
uv run --active python .agents/skills/harmony-hdc-ui-automation/scripts/harmony_hdc_ui.py devices
```

### Cursor

> **执行位置：** 你的鸿蒙项目根目录（含 `entry/`、`module.json5` 那个）

```bash
# 推荐 —— 现代 .mdc 规则，按文件类型激活
mkdir -p .cursor/rules
curl -o .cursor/rules/harmonyos.mdc "$RAW/dist/cursor/harmonyos.mdc"

# 或：旧版单文件规则（Cursor 不支持 .mdc 时使用）
curl -o .cursorrules "$RAW/dist/cursor/.cursorrules"
```

`.mdc` 规则仅在编辑 `.ets`、`module.json5` 等文件时自动激活，非鸿蒙项目不会占用上下文。

### GitHub Copilot

> **执行位置：** 你的鸿蒙项目根目录

```bash
mkdir -p .github
curl -o .github/copilot-instructions.md "$RAW/dist/copilot/copilot-instructions.md"
```

在仓库内对 Copilot Chat 和内联建议始终生效。提交后团队共享。

### Windsurf / Codeium

> **执行位置：** 你的鸿蒙项目根目录

```bash
curl -o .windsurfrules "$RAW/dist/windsurf/.windsurfrules"
```

### Continue.dev

> **执行位置：** 你的鸿蒙项目根目录

```bash
mkdir -p .continue/rules
curl -o .continue/rules/harmonyos.md "$RAW/dist/continue/harmonyos.md"
```

### Cline / Roo Code

1. 下载文件：`curl -o harmonyos-instructions.md "$RAW/dist/cline/custom-instructions.md"`
2. 在 VS Code 中打开 Cline / Roo 设置 → **Custom Instructions**
3. 将文件内容粘贴到工作区或全局 Instructions 字段

### AGENTS.md standard (Codex CLI, opencode, Amp, Aider, Jules)

推荐复制轻量路由及其三个配套目录。Agent 每次会话只读取约 90 行的
`AGENTS.md`，再按任务加载需要的模块：

```bash
cd <你的鸿蒙项目根目录>
cp ~/src/harmonyos-ai-skill/dist/agents-md/AGENTS.md ./AGENTS.md
cp -R ~/src/harmonyos-ai-skill/dist/agents-md/references ./references
cp -R ~/src/harmonyos-ai-skill/dist/agents-md/recipes ./recipes
cp -R ~/src/harmonyos-ai-skill/dist/agents-md/examples ./examples
```

如果项目根目录已经存在同名资源目录，先检查冲突，不要直接覆盖。无法同时部署
配套目录时，改用完整单文件：

```bash
cp ~/src/harmonyos-ai-skill/dist/agents-md/AGENTS.full.md ./AGENTS.md
```

`AGENTS.full.md` 可独立使用，但会在每次会话加载完整开发知识。它不包含
`harmony-hdc-ui-automation` 的 Python 执行器；Codex 项目建议优先使用上方的
双 Skill 安装器。

轻量包优先安装到项目根目录，因为其中的路由使用项目相对路径。配置为用户级
规则前，确认工具能从全局规则位置解析配套目录；否则使用
`AGENTS.full.md`，或改装原生双 Skill。常见的全局规则发现路径：

| 工具 | 全局路径 |
|---|---|
| OpenAI Codex CLI | `~/.codex/AGENTS.md` |
| sst/opencode | `~/.config/opencode/AGENTS.md` |
| Amp | `~/.config/amp/AGENTS.md` |
| Aider | 仅读取当前目录的 `AGENTS.md` |

部分工具支持多层 `AGENTS.md`（最近的优先 / 合并），详见各工具文档。

### Google Gemini CLI

```bash
# Project-level (takes precedence):
curl -o GEMINI.md "$RAW/dist/gemini-cli/GEMINI.md"

# Global (applies to every Gemini CLI session):
mkdir -p ~/.gemini
curl -o ~/.gemini/GEMINI.md "$RAW/dist/gemini-cli/GEMINI.md"
```

### ChatGPT / Gemini web / DeepSeek / Qwen / Kimi / 文心一言

1. 在 GitHub 上打开 [`dist/plain/harmonyos-knowledge.md`](./dist/plain/harmonyos-knowledge.md)
2. 点击 **Raw** → **Ctrl/Cmd + A** → **Ctrl/Cmd + C**
3. 在你的 AI 工具中：
   - **ChatGPT:** Settings → Personalization → **Custom Instructions** → "How would you like ChatGPT to respond?" → 粘贴
   - **Gemini web:** 新建对话 → 启用 **System Instructions** → 粘贴
   - **DeepSeek / Qwen / 文心一言 / Kimi:** 创建"智能体" / "角色" / "Bot" → 粘贴到系统提示
4. 开始提问鸿蒙开发问题 —— AI 已加载知识

### Ollama / 本地模型

```bash
# 1. 拉取模型（推荐 qwen3-coder 或 qwen2.5-coder，对中文支持好）
ollama pull qwen3-coder

# 2. 一行命令带鸿蒙系统提示启动
ollama run qwen3-coder \
  --system "$(curl -s $RAW/dist/system-prompt/system.txt)"
```

或写入自定义 Modelfile（永久保存这个"鸿蒙专家"模型）：

```bash
# 1. 下载系统提示
curl -o system.txt "$RAW/dist/system-prompt/system.txt"

# 2. 创建 Modelfile
cat > Modelfile <<EOF
FROM qwen3-coder
SYSTEM """
$(cat system.txt)
"""
EOF

# 3. 注册自定义模型
ollama create harmonyos-coder -f Modelfile
ollama run harmonyos-coder
```

### Anthropic / OpenAI / 任意 LLM API

```python
# 先安装：pip install anthropic
import anthropic

# 假设你已经把 system.txt 下载到本地（curl -o system.txt "$RAW/dist/system-prompt/system.txt"）
with open("system.txt") as f:
    system_prompt = f.read()

client = anthropic.Anthropic()  # 自动读取 ANTHROPIC_API_KEY 环境变量
response = client.messages.create(
    model="claude-opus-4-7",            # 最新 Opus；可换 claude-sonnet-4-6 / claude-haiku-4-5
    system=system_prompt,
    max_tokens=2048,
    messages=[{"role": "user", "content": "如何在 HarmonyOS 中开发服务卡片？"}],
)
print(response.content[0].text)
```

---

## 🪟 Windows 用户专用（PowerShell）

> 不用 WSL/Git Bash？想直接在 PowerShell 里装？下面给出原生 PowerShell
> 命令。规则文件和 Python 辅助工具跨平台；HDC/UiTest 是否可用仍取决于
> 本机 DevEco Studio、HarmonyOS SDK、驱动和设备连接。
> 推荐使用 **PowerShell 7+**（`winget install Microsoft.PowerShell`）。

<details>
<summary><b>📋 点击展开 PowerShell 完整安装命令</b></summary>

**前置：每个新 PowerShell 窗口先运行一次**

```powershell
$env:RAW = "https://raw.githubusercontent.com/Fly0307/harmonyos-ai-skill/zx-dev"
```

### Claude Code CLI（Windows）

```powershell
# 方式 A — 直接复制（最简单）
git clone -b zx-dev https://github.com/Fly0307/harmonyos-ai-skill.git $HOME\src\harmonyos-ai-skill
New-Item -ItemType Directory -Force $HOME\.claude\skills | Out-Null
Copy-Item -Recurse $HOME\src\harmonyos-ai-skill\harmonyos-development $HOME\.claude\skills\
Copy-Item -Recurse $HOME\src\harmonyos-ai-skill\harmony-hdc-ui-automation $HOME\.claude\skills\

# 方式 B — 符号链接（推荐：需要管理员权限或开启「开发者模式」）
git clone -b zx-dev https://github.com/Fly0307/harmonyos-ai-skill.git $HOME\src\harmonyos-ai-skill
New-Item -ItemType Directory -Force $HOME\.claude\skills | Out-Null
New-Item -ItemType SymbolicLink -Path $HOME\.claude\skills\harmonyos-development -Target $HOME\src\harmonyos-ai-skill\harmonyos-development
New-Item -ItemType SymbolicLink -Path $HOME\.claude\skills\harmony-hdc-ui-automation -Target $HOME\src\harmonyos-ai-skill\harmony-hdc-ui-automation

# 方式 C — 仅项目级别
Set-Location <你的鸿蒙项目根目录>
New-Item -ItemType Directory -Force .claude\skills | Out-Null
Copy-Item -Recurse $HOME\src\harmonyos-ai-skill\harmonyos-development .claude\skills\
Copy-Item -Recurse $HOME\src\harmonyos-ai-skill\harmony-hdc-ui-automation .claude\skills\
```

> **开启开发者模式（一次性）：** 设置 → 隐私和安全性 → 开发者选项 → 打开「开发人员模式」。开启后 `New-Item -ItemType SymbolicLink` 不再需要管理员。

### OpenAI Codex 项目安装（Windows）

```powershell
Set-Location <你的鸿蒙项目根目录>
.\.venv\Scripts\Activate.ps1
uv run --active python $HOME\src\harmonyos-ai-skill\scripts\install_skills.py `
  --project . `
  --mode link
```

若系统不允许创建符号链接，将 `link` 改为 `copy`。自动化命令使用
`uv run --active python ...`，无需写死 `.venv\Scripts\python.exe`。

### Cursor（Windows）

```powershell
# 推荐：现代 .mdc 规则
New-Item -ItemType Directory -Force .cursor\rules | Out-Null
Invoke-WebRequest -Uri "$env:RAW/dist/cursor/harmonyos.mdc" -OutFile .cursor\rules\harmonyos.mdc

# 或：旧版单文件规则
Invoke-WebRequest -Uri "$env:RAW/dist/cursor/.cursorrules" -OutFile .cursorrules
```

### GitHub Copilot（Windows）

```powershell
New-Item -ItemType Directory -Force .github | Out-Null
Invoke-WebRequest -Uri "$env:RAW/dist/copilot/copilot-instructions.md" -OutFile .github\copilot-instructions.md
```

### Windsurf / Codeium（Windows）

```powershell
Invoke-WebRequest -Uri "$env:RAW/dist/windsurf/.windsurfrules" -OutFile .windsurfrules
```

### Continue.dev（Windows）

```powershell
New-Item -ItemType Directory -Force .continue\rules | Out-Null
Invoke-WebRequest -Uri "$env:RAW/dist/continue/harmonyos.md" -OutFile .continue\rules\harmonyos.md
```

### AGENTS.md 标准（Codex CLI / opencode / Amp / Aider）（Windows）

```powershell
Copy-Item $HOME\src\harmonyos-ai-skill\dist\agents-md\AGENTS.md .\AGENTS.md
Copy-Item -Recurse $HOME\src\harmonyos-ai-skill\dist\agents-md\references .\references
Copy-Item -Recurse $HOME\src\harmonyos-ai-skill\dist\agents-md\recipes .\recipes
Copy-Item -Recurse $HOME\src\harmonyos-ai-skill\dist\agents-md\examples .\examples
```

无法部署配套目录时，使用
`Copy-Item $HOME\src\harmonyos-ai-skill\dist\agents-md\AGENTS.full.md .\AGENTS.md`。

全局路径（PowerShell）：
| 工具 | 路径 |
|---|---|
| OpenAI Codex CLI | `$HOME\.codex\AGENTS.md` |
| sst/opencode | `$HOME\.config\opencode\AGENTS.md` |
| Amp | `$HOME\.config\amp\AGENTS.md` |

### Google Gemini CLI（Windows）

```powershell
# 项目级
Invoke-WebRequest -Uri "$env:RAW/dist/gemini-cli/GEMINI.md" -OutFile GEMINI.md

# 全局
New-Item -ItemType Directory -Force $HOME\.gemini | Out-Null
Invoke-WebRequest -Uri "$env:RAW/dist/gemini-cli/GEMINI.md" -OutFile $HOME\.gemini\GEMINI.md
```

### Ollama 本地模型（Windows）

```powershell
# 1. 拉取模型
ollama pull qwen3-coder

# 2. 下载系统提示
Invoke-WebRequest -Uri "$env:RAW/dist/system-prompt/system.txt" -OutFile system.txt

# 3. 一行启动（用反引号续行）
ollama run qwen3-coder --system (Get-Content system.txt -Raw)

# 或：写自定义 Modelfile
@"
FROM qwen3-coder
SYSTEM ```"
$(Get-Content system.txt -Raw)
```"
"@ | Set-Content Modelfile
ollama create harmonyos-coder -f Modelfile
ollama run harmonyos-coder
```

### Anthropic SDK Python（跨平台一致）

Python 代码在 Windows 上和 macOS/Linux 完全相同，参考[上方 Anthropic 章节](#anthropic--openai--任意-llm-api)。

</details>

> **常见问题：** PowerShell 报错 `无法将"curl"识别为 cmdlet`？
> Windows PowerShell 中 `curl` 是 `Invoke-WebRequest` 的别名，**参数不兼容**，请使用上面的 `Invoke-WebRequest` 命令而非 `curl`。

---

## 各工具的激活方式

| 工具类别 | 触发机制 | 始终开启？ |
|---|---|---|
| **Codex / Claude Code / Agent SDK 原生 Skill** | LLM 先根据 `description` 选择 Skill，再读取任务相关模块 | 否 —— 按职责、按模块加载 |
| **轻量 `AGENTS.md` 包** | 每次注入路由，Agent 再读取同级 references、recipes 或 examples | 仅短路由始终开启 |
| **Cursor `.mdc`** | Glob 模式匹配当前文件 | 仅 `.ets` / 鸿蒙配置文件 |
| **Cursor `.cursorrules`、`.windsurfrules`、Copilot instructions、GEMINI.md、Continue / Cline rules** | 项目内每次对话注入构建后的完整开发知识 | 是 |
| **ChatGPT / Gemini Custom Instructions** | 账号下每次对话都会注入 | 是 |
| **单次粘贴 / API `system`** | 仅粘贴的那次对话 | 按次 |

**经验法则：** 优先使用原生双 Skill 或轻量 `AGENTS.md` 包。只有工具无法读取
配套文件时，才使用完整单文件；混合仓库可使用 Cursor `.mdc` 的文件匹配。

---

## 验证是否生效

问 AI：

> *"解释 ArkUI 中 `@ObjectLink` 是什么，什么时候用它代替 `@State`？"*

回答**正确加载**的标志：

- ✅ 提到必须用 `@Observed` 装饰类，`@ObjectLink` 才能工作
- ✅ 提到 `@State` 作用于对象数组时，只响应数组操作（push/splice/重新赋值），不响应单个元素的属性变化
- ✅ 提到在行组件中用 `@ObjectLink` 来观察元素级别的变化
- ✅ 或提到整体重新赋值对象来触发重新渲染

如果回答模糊或像 React（"用 state hook"），说明知识**未加载**。

其他验证问题：

- "FA 模型和 Stage 模型有什么区别？"
- "鸿蒙中如何声明和动态申请权限？"
- "HTTP 请求用哪个 Kit？"
- "怎么开发服务卡片？"

---

## 仓库结构

```
harmonyos-ai-skill/
├─ .github/workflows/test.yml           ← 跨平台测试与元数据校验
├─ .gitignore
├─ LICENSE
├─ README.md
├─ README_EN.md
├─ harmonyos-development/
│  ├─ SKILL.md                          ← 轻量主题路由
│  ├─ agents/openai.yaml
│  ├─ references/                       ← 19 个按需知识模块
│  ├─ recipes/                          ← 构建诊断与代码审查流程
│  ├─ examples/                         ← 权限与 LazyForEach 示例
│  └─ evals/cases.yaml                  ← Skill 行为回归用例
├─ harmony-hdc-ui-automation/
│  ├─ SKILL.md                          ← HDC、UiTest 与 UI 自动化工作流
│  ├─ agents/openai.yaml
│  ├─ assets/harmony-hdc.example.json
│  ├─ references/official-ui-automation-notes.md
│  └─ scripts/harmony_hdc_ui.py
├─ scripts/
│  ├─ build_dist.py                     ← 跨平台重建/校验 dist
│  ├─ build-dist.sh                     ← POSIX 兼容入口
│  ├─ check-frontmatter.py              ← 元数据长度与路由完整性校验
│  └─ install_skills.py                 ← 同时链接或复制两个 skill
├─ tests/                               ← 构建器、CLI 与安装器单元测试
└─ dist/                                ← 65 个自动生成文件，不要手动编辑
   ├─ claude-code/                      ← 两个完整原生 Skill 副本
   │  ├─ harmonyos-development/
   │  └─ harmony-hdc-ui-automation/
   ├─ agents-md/
   │  ├─ AGENTS.md                      ← 轻量路由
   │  ├─ AGENTS.full.md                 ← 完整单文件
   │  ├─ references/
   │  ├─ recipes/
   │  └─ examples/
   ├─ cursor/
   │  ├─ harmonyos.mdc
   │  └─ .cursorrules
   ├─ copilot/copilot-instructions.md
   ├─ windsurf/.windsurfrules
   ├─ continue/harmonyos.md
   ├─ cline/custom-instructions.md
   ├─ gemini-cli/GEMINI.md
   ├─ plain/harmonyos-knowledge.md
   └─ system-prompt/system.txt
```

**双 skill、单仓库工作流：**

1. 根据职责编辑 `harmonyos-development/` 或 `harmony-hdc-ui-automation/`
2. 激活当前仓库环境：`source .venv/bin/activate`
3. 校验 Skill：`uv run --active python scripts/check-frontmatter.py`
4. 生成产物：`uv run --active python scripts/build_dist.py`
5. 运行测试：`uv run --active python -m unittest discover -s tests -v`
6. 确认无漂移：`uv run --active python scripts/build_dist.py --check`
7. 同时提交源文件、测试和重新生成的 `dist/`

---

## 更新到最新版本

```bash
cd /path/to/your/clone
git pull origin zx-dev
```

通过符号链接安装双 Skill 的用户到此即可；复制安装的用户需要重新复制两个完整
Skill 目录。使用 `dist` 规则文件的用户重新复制对应产物。`dist` 已随仓库提交，
普通使用者不需要本地重建；只有修改源 Skill 时才运行构建器。

---

## 编写你自己的 skill

源格式是 Claude Code 的 `SKILL.md` —— YAML frontmatter + Markdown 正文：

```markdown
---
name: my-skill-name
description: >
  第一句：这个 skill 涵盖的领域。
  然后列出 AI 可能匹配的所有触发短语：
  关键词、API 名称、命令名、用户问题、同义词。
---

# My Skill

## 何时使用
- 具体场景的列表

## 参考资料
密集、可引用的资料：表格、代码片段、API 签名、
规则、陷阱。避免废话，多用列表和紧凑示例。
```

### 编写指南

- **聚焦** —— 一个 skill 一个领域，不要混合鸿蒙 + iOS + Android
- **密集** —— 删掉每一句不能教会 AI 新知识的话
- **触发词丰富但精简** —— 在 `description` 中覆盖关键用户表达，并保持在 1024 字符以内
- **可操作** —— 优先用具体的代码/配置片段，而非抽象解释
- **诚实面对空白** —— 如果某功能已弃用就说明，没有数据就不写

编辑源文件后，在已激活的 `.venv` 中运行
`uv run --active python scripts/check-frontmatter.py`，再运行
`uv run --active python scripts/build_dist.py` 重新生成 `dist/`。
macOS/Linux 也可继续使用 `./scripts/build-dist.sh`。

---

## 故障排除

**AI 仍然给出泛泛的 TypeScript/React 回答**
- 确认文件放在了正确的路径（见上方*支持的 AI 工具*表格）
- Claude Code：运行 *"What skills are available?"* —— 如果没有同时列出两个 Skill，重启 Claude Code 或检查 `~/.claude/skills/`
- Codex：确认 `.agents/skills/` 下存在两个完整 Skill 目录，而不是只有两份 `SKILL.md`
- 项目规则工具（Cursor、Copilot 等）：确保你编辑的文件在**规则文件所在的仓库内**，规则不会在仓库外生效
- 粘贴类工具（ChatGPT、DeepSeek 等）：系统提示是按对话生效的，粘贴后要**开新对话**

**规则文件太长，超出工具的上下文限制？**
原生 Skill 和 `dist/agents-md/AGENTS.md` 不会一次加载完整知识库：根路由只负责选择 references、recipes 或 examples。`dist/plain/` 等单文件格式会有意嵌入完整内容；遇到严格上下文限制时，优先使用原生 Skill 或轻量 `AGENTS.md`，不要手工破坏源 references。

**`curl` 返回 404？**
URL 中的分支可能已变更。检查 `https://github.com/Fly0307/harmonyos-ai-skill/branches` 并更新 `$RAW`。

**上游仓库更新后怎么同步？**
见上方*更新到最新版本*章节。

---

## 许可证与贡献

基于 **MIT 协议** 开源 —— 个人和商业项目均可自由使用。

欢迎贡献：
1. Fork 本仓库
2. 编辑对应的源 skill；不要直接编辑 `dist/`
3. 运行 `uv run --active python scripts/check-frontmatter.py`
4. 运行 `uv run --active python scripts/build_dist.py`
5. 运行 `uv run --active python -m unittest discover -s tests -v`
6. 运行 `uv run --active python scripts/build_dist.py --check`
7. 提交源文件、测试和对应的 `dist/`，然后开 PR

欢迎提交：事实纠正、新的 gotcha、更新的 API 名称、description 字段的翻译（提高触发匹配率）。
