"""Unit tests for the cross-platform HDC helper without requiring a device."""

from __future__ import annotations

import importlib.util
import subprocess
import sys
import tempfile
import unittest
from argparse import Namespace
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[1]
SCRIPT = REPO_ROOT / "harmony-hdc-ui-automation" / "scripts" / "harmony_hdc_ui.py"


def load_module():
    """Load the hyphenated skill script as a testable Python module."""
    spec = importlib.util.spec_from_file_location("harmony_hdc_ui", SCRIPT)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load {SCRIPT}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


hdc = load_module()


class ParserTests(unittest.TestCase):
    """Cover common-option placement and portable defaults."""

    def test_common_target_before_or_after_subcommand(self):
        before = hdc.parse_args(["--target", "SERIAL", "devices"])
        after = hdc.parse_args(["devices", "--target", "SERIAL"])
        self.assertEqual("SERIAL", before.target)
        self.assertEqual("SERIAL", after.target)

    def test_timeout_before_or_after_subcommand(self):
        before = hdc.parse_args(["--timeout", "5", "devices"])
        after = hdc.parse_args(["devices", "--timeout", "6"])
        self.assertEqual(5.0, before.timeout)
        self.assertEqual(6.0, after.timeout)

    def test_timeout_must_be_positive(self):
        with self.assertRaises(SystemExit):
            hdc.parse_args(["devices", "--timeout", "0"])


class ConfigurationTests(unittest.TestCase):
    """Cover generic project defaults instead of repository-specific values."""

    def test_load_project_config(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / ".harmony-hdc.json"
            path.write_text(
                '{"bundleName":"com.example.test","moduleName":"feature",'
                '"abilityName":"FeatureAbility"}',
                encoding="utf-8",
            )
            config = hdc.load_project_config(str(path))
        self.assertEqual("com.example.test", config.bundle_name)
        self.assertEqual("feature", config.module_name)
        self.assertEqual("FeatureAbility", config.ability_name)

    def test_bundle_requires_flag_or_config(self):
        args = Namespace(bundle=None, config=None)
        with mock.patch.object(hdc.Path, "cwd", return_value=Path("/missing-project")):
            with self.assertRaises(hdc.CommandError):
                hdc.resolve_bundle(args)


class DeviceSelectionTests(unittest.TestCase):
    """Ensure ambiguous device operations are rejected before HDC side effects."""

    def make_args(self, target=None):
        return Namespace(
            hdc="hdc",
            target=target,
            timeout=5.0,
            config=None,
        )

    def completed(self, output):
        return subprocess.CompletedProcess(["hdc"], 0, output, "")

    def test_parse_targets(self):
        self.assertEqual(["A", "B"], hdc.parse_targets("A\nB device\n"))
        self.assertEqual([], hdc.parse_targets("[Empty]\n"))

    @mock.patch.object(hdc, "run_command")
    @mock.patch.object(hdc, "find_hdc", return_value="hdc")
    def test_multiple_targets_require_selection(self, _find_hdc, run_command):
        run_command.return_value = self.completed("A\nB\n")
        with self.assertRaises(hdc.CommandError):
            hdc.ensure_device_selection(self.make_args())

    @mock.patch.object(hdc, "run_command")
    @mock.patch.object(hdc, "find_hdc", return_value="hdc")
    def test_known_target_is_accepted(self, _find_hdc, run_command):
        run_command.return_value = self.completed("A\nB\n")
        args = self.make_args("B")
        hdc.ensure_device_selection(args)
        self.assertTrue(args._device_selection_checked)

    @mock.patch.object(hdc, "run_command")
    @mock.patch.object(hdc, "find_hdc", return_value="hdc")
    def test_unknown_target_is_rejected(self, _find_hdc, run_command):
        run_command.return_value = self.completed("A\nB\n")
        with self.assertRaises(hdc.CommandError):
            hdc.ensure_device_selection(self.make_args("C"))


class CommandTests(unittest.TestCase):
    """Cover host-independent command and path construction."""

    def test_build_hdc_command(self):
        self.assertEqual(
            ["hdc", "-t", "SERIAL", "shell", "hilog", "-r"],
            hdc.build_hdc_command("hdc", "SERIAL", ["shell", "hilog", "-r"]),
        )

    def test_app_shell_path(self):
        self.assertEqual(
            "./data/storage/el2/base",
            hdc.app_shell_path("/data/storage/el2/base"),
        )

    @mock.patch.object(hdc.subprocess, "run", side_effect=FileNotFoundError("missing"))
    def test_missing_executable_is_reported_as_command_error(self, _run):
        with self.assertRaisesRegex(hdc.CommandError, "Cannot run"):
            hdc.run_command(["missing-hdc"])


if __name__ == "__main__":
    unittest.main()
