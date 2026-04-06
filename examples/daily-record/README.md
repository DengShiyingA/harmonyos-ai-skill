# Daily Record — 每日记录

HarmonyOS NEXT 示例应用，用于训练 [harmonyos-ai-skills](../../) 知识包。

## 覆盖的 SKILL.md 知识点

| 阶段 | 功能 | 触发的知识 |
|---|---|---|
| Day 1 | 首页列表 | Stage model, ArkUI, LazyForEach, @Reusable, @Observed/@ObjectLink |
| Day 2 | 发布 + 拍照/选图 | Camera Kit, Media Library Kit, 权限申请 |
| Day 3 | 多页导航 + 动画 | NavPathStack, animateTo, geometryTransition |
| Day 4 | 本地数据持久化 | relationalStore, preferences |
| Day 5 | 定位 + 通知提醒 | Location Kit, Notification Kit, Background Tasks |
| Day 6 | 平板/折叠屏适配 | GridRow/GridCol, breakpoints, display |
| Day 7 | 测试 + 性能优化 | arkxtest, JsUnit, UiTest, @Reusable |

## 安装

1. 在 DevEco Studio 中新建 Empty Ability 项目
2. 将本目录下的源文件复制到项目对应位置：
   - `entry/src/main/ets/` → 覆盖到项目的 `entry/src/main/ets/`
   - `entry/src/main/module.json5` → 覆盖（注意合并你的签名配置）
3. Sync Project with Hvigor Files
4. Run on device or emulator

## 使用技巧

遇到 AI 回答有误时，直接说：
```
"这个不对，正确的写法是 xxx，请更新 skill"
```
Claude Code 会自动更新 `~/harmonyos-ai-skills/harmonyos-development/SKILL.md`。
