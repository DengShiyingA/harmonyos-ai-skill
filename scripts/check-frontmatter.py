#!/usr/bin/env python3
"""Validate local skill metadata and directly routed support files."""
from __future__ import annotations

import ast
import re
import sys
from pathlib import Path


MAX_DESCRIPTION_LENGTH = 1024
DEFAULT_SKILLS = (
    Path("harmonyos-development/SKILL.md"),
    Path("harmony-hdc-ui-automation/SKILL.md"),
)
ROUTED_PATH_PATTERN = re.compile(
    r"`((?:references|recipes|examples)/[A-Za-z0-9_.@/+~-]+)`"
)


class ValidationError(ValueError):
    """Raised when a skill package is not discoverable or internally consistent."""


def parse_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---\n"):
        raise ValidationError("SKILL.md must start with YAML frontmatter")
    end = text.find("\n---", 4)
    if end == -1:
        raise ValidationError("SKILL.md frontmatter must be closed with ---")
    return text[4:end].strip(), text[end + 4 :]


def get_field(frontmatter: str, field: str) -> str:
    match = re.search(rf"^{field}:\s*(.*)$", frontmatter, re.MULTILINE)
    if not match:
        raise ValidationError(f"missing required frontmatter field: {field}")
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
        raise ValidationError(f"frontmatter field is empty: {field}")
    if value[:1] in {"'", '"'}:
        try:
            parsed = ast.literal_eval(value)
        except (SyntaxError, ValueError) as error:
            raise ValidationError(f"invalid quoted {field}: {error}") from error
        if not isinstance(parsed, str):
            raise ValidationError(f"frontmatter field must be text: {field}")
        value = parsed
    return value


def validate(path: Path) -> list[str]:
    """Return validation errors for one skill entrypoint."""
    errors: list[str] = []
    if not path.exists():
        return [f"file not found: {path}"]

    text = path.read_text(encoding="utf-8")
    try:
        frontmatter, body = parse_frontmatter(text)
        name = get_field(frontmatter, "name")
        description = get_field(frontmatter, "description")
    except ValidationError as error:
        return [str(error)]

    fields = set(re.findall(r"^([A-Za-z0-9_-]+):", frontmatter, re.MULTILINE))
    if fields != {"name", "description"}:
        errors.append(
            f"frontmatter fields must be exactly name and description; found {sorted(fields)}"
        )
    if name != path.parent.name:
        errors.append(f"skill name {name!r} must match directory {path.parent.name!r}")
    if not re.fullmatch(r"[a-z0-9-]{1,64}", name):
        errors.append("skill name must use 1-64 lowercase letters, digits, or hyphens")
    if len(description) > MAX_DESCRIPTION_LENGTH:
        errors.append(
            f"description is {len(description)} characters; maximum is "
            f"{MAX_DESCRIPTION_LENGTH}"
        )
    if not body.strip():
        errors.append("SKILL.md body must not be empty")
    if not (path.parent / "agents" / "openai.yaml").is_file():
        errors.append("agents/openai.yaml is missing")

    for relative_path in sorted(set(ROUTED_PATH_PATTERN.findall(body))):
        if not (path.parent / relative_path).is_file():
            errors.append(f"routed support file is missing: {relative_path}")
    return errors


def main() -> None:
    paths = [Path(argument) for argument in sys.argv[1:]] or list(DEFAULT_SKILLS)
    failed = False
    for path in paths:
        errors = validate(path)
        if errors:
            failed = True
            for error in errors:
                print(f"ERROR: {path}: {error}", file=sys.stderr)
        else:
            print(f"OK: {path}")
    if failed:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
