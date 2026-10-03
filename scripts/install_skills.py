#!/usr/bin/env python3
"""Install both HarmonyOS skills into a target project's .agents directory."""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path
from typing import Sequence


SKILL_NAMES = ("harmonyos-development", "harmony-hdc-ui-automation")


class InstallError(RuntimeError):
    """Raised when a skill cannot be installed safely."""


def install_skill(source: Path, destination: Path, mode: str, dry_run: bool) -> str:
    """Install one skill without overwriting an unrelated existing path."""
    if not (source / "SKILL.md").is_file():
        raise InstallError(f"Invalid skill source: {source}")
    if destination.is_symlink():
        if destination.resolve() == source.resolve():
            return f"unchanged {destination}"
        raise InstallError(f"Destination is a different symlink: {destination}")
    if destination.exists():
        raise InstallError(
            f"Destination already exists: {destination}. Move it aside or remove it explicitly."
        )
    if dry_run:
        return f"would-{mode} {source} -> {destination}"

    destination.parent.mkdir(parents=True, exist_ok=True)
    if mode == "copy":
        shutil.copytree(source, destination)
    else:
        try:
            destination.symlink_to(source.resolve(), target_is_directory=True)
        except OSError as exc:
            hint = (
                "On Windows, enable Developer Mode or run an elevated terminal; "
                "otherwise rerun with --mode copy."
            )
            raise InstallError(f"Cannot create symlink {destination}: {exc}. {hint}") from exc
    action = "copied" if mode == "copy" else "linked"
    return f"{action} {source} -> {destination}"


def build_parser() -> argparse.ArgumentParser:
    """Create the installer CLI parser."""
    parser = argparse.ArgumentParser(
        description="Install HarmonyOS development and HDC automation skills into a project."
    )
    parser.add_argument(
        "--project",
        type=Path,
        default=Path.cwd(),
        help="Target project root. Default: current directory.",
    )
    parser.add_argument(
        "--mode",
        choices=("link", "copy"),
        default="link",
        help="Install with symlinks or copies. Default: link.",
    )
    parser.add_argument(
        "--skills",
        nargs="+",
        choices=SKILL_NAMES,
        default=list(SKILL_NAMES),
        help="Skills to install. Default: both.",
    )
    parser.add_argument("--dry-run", action="store_true", help="Print actions without writing.")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    """Install the selected skills and report each resolved destination."""
    args = build_parser().parse_args(argv)
    repo_root = Path(__file__).resolve().parents[1]
    destination_root = args.project.expanduser().resolve() / ".agents" / "skills"
    try:
        # Validate the complete install set before writing, so one collision does
        # not leave the project with only the first skill installed.
        for name in args.skills:
            install_skill(
                repo_root / name,
                destination_root / name,
                args.mode,
                True,
            )
        for name in args.skills:
            print(install_skill(
                repo_root / name,
                destination_root / name,
                args.mode,
                args.dry_run,
            ))
    except InstallError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
