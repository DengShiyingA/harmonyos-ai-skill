from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from scripts import build_dist


class BuildDistTests(unittest.TestCase):
    def test_build_preserves_progressive_and_single_file_formats(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / "dist"
            build_dist.build_into(destination)

            router = (destination / "agents-md" / "AGENTS.md").read_text(
                encoding="utf-8"
            )
            full = (destination / "agents-md" / "AGENTS.full.md").read_text(
                encoding="utf-8"
            )

            self.assertNotIn("# Embedded HarmonyOS Support Files", router)
            self.assertIn("<!-- Source: references/ai-development-tools.md -->", full)
            self.assertIn("<!-- Source: recipes/debug-build-error.md -->", full)
            self.assertIn("<!-- Source: examples/permission-request.ets -->", full)
            self.assertNotIn("evals/cases.yaml", full)

            self.assertTrue(
                (destination / "agents-md" / "recipes" / "review-arkts-code.md").is_file()
            )
            self.assertTrue(
                (destination / "agents-md" / "examples" / "lazyforeach-list.ets").is_file()
            )
            self.assertTrue(
                (
                    destination
                    / "claude-code"
                    / "harmonyos-development"
                    / "evals"
                    / "cases.yaml"
                ).is_file()
            )
            self.assertTrue(
                (
                    destination
                    / "claude-code"
                    / "harmony-hdc-ui-automation"
                    / "SKILL.md"
                ).is_file()
            )


if __name__ == "__main__":
    unittest.main()
