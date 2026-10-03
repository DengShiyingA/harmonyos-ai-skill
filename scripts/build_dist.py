#!/usr/bin/env python3
"""Build deterministic multi-agent distribution files from the source skills."""

from __future__ import annotations

import argparse
import hashlib
import shutil
import tempfile
from pathlib import Path
from typing import Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]
DEVELOPMENT_SKILL = REPO_ROOT / "harmonyos-development"
AUTOMATION_SKILL = REPO_ROOT / "harmony-hdc-ui-automation"
DIST = REPO_ROOT / "dist"
EMBEDDED_SUPPORT_DIRS = ("references", "recipes", "examples")

CURSOR_HEADER = """\
---
description: >
  HarmonyOS NEXT development expert — ArkTS, ArkUI, Stage model, 60+ Kit APIs,
  UI components (Tabs/Swiper/WaterFlow/Grid/List), state management (V1/V2/StateStore),
  navigation, animation, networking, data persistence, Camera/Audio/AVPlayer/Image Kit,
  Scan/Account/Payment/Push/Map/Share Kit, dark mode, immersive window, keyboard,
  gestures, permissions, testing, code obfuscation, performance optimization,
  third-party libraries (@ohos/axios, lottie, imageknife, pulltorefresh).
globs:
  - "**/*.ets"
  - "**/module.json5"
  - "**/app.json5"
  - "**/oh-package.json5"
  - "**/build-profile.json5"
alwaysApply: false
---
"""


class BuildError(RuntimeError):
    """Raised when source skills or generated output are invalid."""


def read_text(path: Path) -> str:
    """Read UTF-8 text and normalize only trailing newlines."""
    return path.read_text(encoding="utf-8").rstrip("\n")


def routing_body(skill_file: Path) -> str:
    """Extract the body after the YAML frontmatter."""
    lines = skill_file.read_text(encoding="utf-8").splitlines()
    separators = [index for index, line in enumerate(lines) if line == "---"]
    if len(separators) < 2:
        raise BuildError(f"Missing YAML frontmatter delimiters: {skill_file}")
    return "\n".join(lines[separators[1] + 1:]).lstrip("\n").rstrip("\n")


def support_files(skill_dir: Path) -> list[Path]:
    """Return deterministic text support files for single-file targets."""
    files: list[Path] = []
    for directory_name in EMBEDDED_SUPPORT_DIRS:
        directory = skill_dir / directory_name
        if directory.is_dir():
            files.extend(path for path in directory.rglob("*") if path.is_file())
    return sorted(files, key=lambda path: path.relative_to(skill_dir).as_posix())


def full_body(router: str, skill_dir: Path) -> str:
    """Build the single-file body used by non-native agent formats."""
    parts = [
        router,
        "",
        "# Embedded HarmonyOS Support Files",
        "",
        "The following sections inline references, recipes, and examples for single-file distribution targets.",
    ]
    for support_file in support_files(skill_dir):
        relative_path = support_file.relative_to(skill_dir).as_posix()
        parts.extend([
            "",
            f"<!-- Source: {relative_path} -->",
            read_text(support_file),
        ])
    return "\n".join(parts).rstrip("\n") + "\n"


def write_text(path: Path, content: str) -> None:
    """Write deterministic UTF-8/LF text."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip("\n") + "\n", encoding="utf-8", newline="\n")


def copy_skill(source: Path, destination: Path) -> None:
    """Copy a native skill while excluding runtime cache files."""
    shutil.copytree(
        source,
        destination,
        ignore=shutil.ignore_patterns("__pycache__", "*.pyc"),
    )


def build_into(destination: Path) -> int:
    """Build all distribution files into an empty destination directory."""
    source_file = DEVELOPMENT_SKILL / "SKILL.md"
    references = DEVELOPMENT_SKILL / "references"
    if not source_file.is_file() or not references.is_dir():
        raise BuildError("HarmonyOS development skill source is incomplete.")
    if not (AUTOMATION_SKILL / "SKILL.md").is_file():
        raise BuildError("Harmony HDC automation skill source is incomplete.")

    destination.mkdir(parents=True, exist_ok=True)
    copy_skill(DEVELOPMENT_SKILL, destination / "claude-code" / DEVELOPMENT_SKILL.name)
    copy_skill(AUTOMATION_SKILL, destination / "claude-code" / AUTOMATION_SKILL.name)

    router = routing_body(source_file)
    embedded = full_body(router, DEVELOPMENT_SKILL)

    write_text(destination / "plain" / "harmonyos-knowledge.md", embedded)
    write_text(destination / "cursor" / "harmonyos.mdc", CURSOR_HEADER + embedded)
    write_text(destination / "cursor" / ".cursorrules", embedded)
    write_text(destination / "copilot" / "copilot-instructions.md", embedded)
    write_text(destination / "continue" / "harmonyos.md", embedded)
    write_text(destination / "windsurf" / ".windsurfrules", embedded)
    write_text(destination / "cline" / "custom-instructions.md", embedded)
    write_text(destination / "gemini-cli" / "GEMINI.md", embedded)
    write_text(
        destination / "system-prompt" / "system.txt",
        "You are an expert HarmonyOS NEXT developer with deep knowledge of ArkTS, ArkUI, "
        "Stage model, Kit APIs, and the HarmonyOS ecosystem. Apply the following comprehensive "
        "domain knowledge when answering HarmonyOS development questions.\n\n" + embedded,
    )

    agents_dir = destination / "agents-md"
    write_text(agents_dir / "AGENTS.md", router)
    write_text(agents_dir / "AGENTS.full.md", embedded)
    for directory_name in EMBEDDED_SUPPORT_DIRS:
        source_directory = DEVELOPMENT_SKILL / directory_name
        if source_directory.is_dir():
            shutil.copytree(source_directory, agents_dir / directory_name)
    return sum(1 for path in destination.rglob("*") if path.is_file())


def snapshot(root: Path) -> dict[str, str]:
    """Return stable SHA-256 hashes for every generated file."""
    return {
        path.relative_to(root).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in sorted(root.rglob("*"))
        if path.is_file()
    }


def check_dist() -> int:
    """Verify that committed dist files match a clean build."""
    with tempfile.TemporaryDirectory(prefix="harmonyos-skill-dist-") as temp:
        generated = Path(temp) / "dist"
        build_into(generated)
        expected = snapshot(generated)
        actual = snapshot(DIST) if DIST.is_dir() else {}
    if expected == actual:
        print(f"dist is current ({len(expected)} files)")
        return 0
    expected_names = set(expected)
    actual_names = set(actual)
    for name in sorted(expected_names - actual_names):
        print(f"missing: {name}")
    for name in sorted(actual_names - expected_names):
        print(f"unexpected: {name}")
    for name in sorted(expected_names & actual_names):
        if expected[name] != actual[name]:
            print(f"changed: {name}")
    return 1


def build_dist() -> int:
    """Replace dist only after a clean deterministic build succeeds."""
    with tempfile.TemporaryDirectory(prefix=".dist-build-", dir=REPO_ROOT) as temp:
        generated = Path(temp) / "dist"
        count = build_into(generated)
        if DIST.exists():
            shutil.rmtree(DIST)
        shutil.move(str(generated), str(DIST))
    print(f"Built {count} files:")
    for path in sorted(DIST.rglob("*")):
        if path.is_file():
            print(path.relative_to(REPO_ROOT).as_posix())
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    """Run build or verification mode."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify dist without modifying it.")
    args = parser.parse_args(argv)
    return check_dist() if args.check else build_dist()


if __name__ == "__main__":
    raise SystemExit(main())
