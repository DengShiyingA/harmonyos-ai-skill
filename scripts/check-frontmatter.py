#!/usr/bin/env python3
"""Validate a SKILL.md file for agent-skill discovery quality."""
from __future__ import annotations

import re
import sys
from pathlib import Path


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        fail("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---", 4)
    if end == -1:
        fail("SKILL.md frontmatter must be closed with ---")
    return text[4:end].strip(), text[end + 4 :]


def get_field(frontmatter: str, field: str) -> str:
    match = re.search(rf"^{field}:\s*(.*)$", frontmatter, re.MULTILINE)
    if not match:
        fail(f"missing required frontmatter field: {field}")
    value = match.group(1).strip()
    if value in {"", ">", "|"}:
        lines = frontmatter.splitlines()
        start = next(i for i, line in enumerate(lines) if line.startswith(f"{field}:")) + 1
        collected: list[str] = []
        for line in lines[start:]:
            if re.match(r"^[a-zA-Z0-9_-]+:\s*", line):
                break
            collected.append(line.strip())
        value = " ".join(part for part in collected if part)
    if not value:
        fail(f"frontmatter field is empty: {field}")
    return value


def main() -> None:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "harmonyos-development/SKILL.md")
    if not path.exists():
        fail(f"file not found: {path}")

    text = path.read_text(encoding="utf-8")
    frontmatter, body = parse_frontmatter(text)
    name = get_field(frontmatter, "name")
    description = get_field(frontmatter, "description")

    if name != "harmonyos-development":
        fail("skill name must be harmonyos-development")
    if len(description) > 900:
        fail("description is too long; keep discovery metadata concise")
    if "HarmonyOS" not in description or "ArkTS" not in description:
        fail("description should mention HarmonyOS and ArkTS for discovery")
    if "API 26" in body and "preview" not in body.lower():
        fail("API 26 must be marked as preview/Beta somewhere in SKILL.md")
    if "API 24" not in body:
        fail("SKILL.md must state API 24 production baseline")

    print(f"OK: {path}")


if __name__ == "__main__":
    main()
