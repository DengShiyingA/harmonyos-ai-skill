# Skills

Claude Code skills for specialized domains. Each subdirectory is a self-contained skill with a `SKILL.md` describing when and how Claude should apply it.

## Available skills

| Skill | Purpose |
|---|---|
| [`adopting-liquid-glass`](./adopting-liquid-glass/) | Comprehensive guide to Apple's Liquid Glass material in SwiftUI / UIKit / AppKit for iOS 26, iPadOS 26, macOS Tahoe 26, watchOS 26, tvOS 26. Based on Apple's "Adopting Liquid Glass" technology overview. |
| [`harmonyos-development`](./harmonyos-development/) | Comprehensive guide to HarmonyOS NEXT (鸿蒙) native development with ArkTS and ArkUI, Stage model abilities, state-management decorators, HarmonyOS Kits, packaging, and samples catalog. |

## Installation

### User-level (recommended, global across all projects)

```bash
git clone https://github.com/dengshiyinga/skills.git
mkdir -p ~/.claude/skills
cp -r skills/adopting-liquid-glass ~/.claude/skills/
cp -r skills/harmonyos-development ~/.claude/skills/
```

Restart Claude Code. The skills will now be auto-loaded whenever the conversation matches their `description` frontmatter.

### Project-level (only this project)

```bash
mkdir -p .claude/skills
cp -r path/to/skills/adopting-liquid-glass .claude/skills/
```

### Symlink (track upstream updates)

```bash
git clone https://github.com/dengshiyinga/skills.git ~/src/skills
mkdir -p ~/.claude/skills
ln -s ~/src/skills/adopting-liquid-glass     ~/.claude/skills/adopting-liquid-glass
ln -s ~/src/skills/harmonyos-development     ~/.claude/skills/harmonyos-development
```

## How skills are invoked

These skills are **model-invoked**: Claude reads the `description` in each `SKILL.md` frontmatter and automatically loads the skill when a user question matches. You don't need to type a slash command.

You can also explicitly request one:

> "Use the adopting-liquid-glass skill to audit my toolbar code."
> "Apply the harmonyos-development skill — explain @ObjectLink."

## Verifying installation

After copying and restarting Claude Code, ask:

> "What skills are available?"

Claude will list the skills it has loaded. If you don't see the new ones, confirm the directory structure is:

```
~/.claude/skills/
├─ adopting-liquid-glass/
│  └─ SKILL.md
└─ harmonyos-development/
   └─ SKILL.md
```

## Writing your own skill

1. Create `~/.claude/skills/<your-skill-name>/SKILL.md`
2. Add YAML frontmatter with `name` and a rich `description` listing the trigger terms
3. Write the skill body as concise, actionable reference material

```markdown
---
name: my-skill
description: Trigger keywords that help Claude recognize when to apply this skill.
---

# My Skill

## When to apply this skill
...

## Reference
...
```

Keep skills **focused** (one domain each), **dense** (no filler), and **trigger-rich** (list all likely user phrasings in `description`).
