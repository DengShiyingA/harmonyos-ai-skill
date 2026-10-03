"""Unit tests for installing both source skills into another project."""

from __future__ import annotations

import importlib.util
import os
import sys
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "scripts" / "install_skills.py"


def load_module():
    """Load the installer directly from the repository."""
    spec = importlib.util.spec_from_file_location("install_skills", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


installer = load_module()


class InstallTests(unittest.TestCase):
    """Cover copy, link, idempotence, and collision safety."""

    def test_copy_both_skills(self):
        with tempfile.TemporaryDirectory() as temp:
            project = Path(temp)
            exit_code = installer.main(["--project", str(project), "--mode", "copy"])
            self.assertEqual(0, exit_code)
            for name in installer.SKILL_NAMES:
                self.assertTrue((project / ".agents" / "skills" / name / "SKILL.md").is_file())

    @unittest.skipIf(os.name == "nt", "Windows CI may not permit symbolic links")
    def test_link_is_idempotent(self):
        with tempfile.TemporaryDirectory() as temp:
            project = Path(temp)
            first = installer.main(["--project", str(project), "--mode", "link"])
            second = installer.main(["--project", str(project), "--mode", "link"])
            self.assertEqual(0, first)
            self.assertEqual(0, second)

    def test_existing_directory_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as temp:
            project = Path(temp)
            destination = project / ".agents" / "skills" / installer.SKILL_NAMES[0]
            destination.mkdir(parents=True)
            exit_code = installer.main([
                "--project",
                str(project),
                "--mode",
                "copy",
                "--skills",
                installer.SKILL_NAMES[0],
            ])
            self.assertEqual(1, exit_code)

    def test_collision_preflight_prevents_partial_install(self):
        with tempfile.TemporaryDirectory() as temp:
            project = Path(temp)
            second = project / ".agents" / "skills" / installer.SKILL_NAMES[1]
            second.mkdir(parents=True)
            exit_code = installer.main(["--project", str(project), "--mode", "copy"])
            first = project / ".agents" / "skills" / installer.SKILL_NAMES[0]
            self.assertEqual(1, exit_code)
            self.assertFalse(first.exists())


if __name__ == "__main__":
    unittest.main()
