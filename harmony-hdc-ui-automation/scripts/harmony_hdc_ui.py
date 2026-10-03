#!/usr/bin/env python3
"""Small HDC/UiTest CLI helper for HarmonyOS device inspection and control."""

from __future__ import annotations

import argparse
import json
import locale
import os
import shlex
import shutil
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence


DEFAULT_REMOTE_DIR = "/data/local/tmp"
DEFAULT_MODULE_NAME = "entry"
DEFAULT_ABILITY_NAME = "EntryAbility"
DEFAULT_CONFIG_FILE = ".harmony-hdc.json"
DEFAULT_TIMEOUT_SECONDS = 30.0


@dataclass(frozen=True)
class ProjectConfig:
    """Project-scoped defaults loaded from .harmony-hdc.json."""

    path: Path | None = None
    bundle_name: str | None = None
    module_name: str = DEFAULT_MODULE_NAME
    ability_name: str = DEFAULT_ABILITY_NAME
    app_files_root: str | None = None


class CommandError(RuntimeError):
    """Raised when an HDC command exits with a non-zero status."""


def find_hdc(explicit_path: str | None) -> str:
    """Resolve the hdc binary from an explicit flag, HDC env var, or PATH."""
    candidates = [explicit_path, os.environ.get("HDC"), shutil.which("hdc")]
    for candidate in candidates:
        if candidate:
            return candidate
    raise CommandError("Cannot find hdc. Set --hdc, HDC, or add hdc to PATH.")


def build_hdc_command(hdc: str, target: str | None, args: Sequence[str]) -> list[str]:
    """Build an hdc command, injecting -t <target> when a device is selected."""
    cmd = [hdc]
    if target:
        cmd.extend(["-t", target])
    cmd.extend(args)
    return cmd


def render_command(cmd: Sequence[str]) -> str:
    """Render a command for diagnostics using host-appropriate quoting."""
    if os.name == "nt":
        return subprocess.list2cmdline(list(cmd))
    return shlex.join(cmd)


def run_command(
    cmd: Sequence[str],
    *,
    check: bool = True,
    timeout: float = DEFAULT_TIMEOUT_SECONDS,
) -> subprocess.CompletedProcess[str]:
    """Run a command and return captured text output for reliable reporting."""
    try:
        result = subprocess.run(
            list(cmd),
            text=True,
            encoding=locale.getpreferredencoding(False) or "utf-8",
            errors="replace",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired as exc:
        raise CommandError(
            f"Command timed out after {timeout:g}s: {render_command(cmd)}"
        ) from exc
    except OSError as exc:
        raise CommandError(f"Cannot run {render_command(cmd)}: {exc}") from exc
    if check and result.returncode != 0:
        rendered = render_command(cmd)
        raise CommandError(
            f"Command failed ({result.returncode}): {rendered}\n"
            f"stdout:\n{result.stdout}\n"
            f"stderr:\n{result.stderr}"
        )
    return result


def print_result(result: subprocess.CompletedProcess[str]) -> None:
    """Print command output without hiding stderr diagnostics."""
    if result.stdout:
        print(result.stdout, end="" if result.stdout.endswith("\n") else "\n")
    if result.stderr:
        print(result.stderr, end="" if result.stderr.endswith("\n") else "\n", file=sys.stderr)


def load_project_config(explicit_path: str | None) -> ProjectConfig:
    """Load optional project defaults without requiring a project-specific bundle name."""
    path = Path(explicit_path).expanduser() if explicit_path else Path.cwd() / DEFAULT_CONFIG_FILE
    if not path.exists():
        if explicit_path:
            raise CommandError(f"Config file does not exist: {path}")
        return ProjectConfig()
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise CommandError(f"Cannot read config file {path}: {exc}") from exc
    if not isinstance(payload, dict):
        raise CommandError(f"Config file must contain a JSON object: {path}")

    def optional_string(key: str) -> str | None:
        value = payload.get(key)
        if value is None:
            return None
        if not isinstance(value, str) or not value.strip():
            raise CommandError(f"Config field {key} must be a non-empty string.")
        return value.strip()

    return ProjectConfig(
        path=path.resolve(),
        bundle_name=optional_string("bundleName"),
        module_name=optional_string("moduleName") or DEFAULT_MODULE_NAME,
        ability_name=optional_string("abilityName") or DEFAULT_ABILITY_NAME,
        app_files_root=optional_string("appFilesRoot"),
    )


def project_config(args: argparse.Namespace) -> ProjectConfig:
    """Return the cached project configuration for a parsed command."""
    cached = getattr(args, "_project_config", None)
    if isinstance(cached, ProjectConfig):
        return cached
    loaded = load_project_config(getattr(args, "config", None))
    setattr(args, "_project_config", loaded)
    return loaded


def resolve_bundle(args: argparse.Namespace) -> str:
    """Resolve a required bundle name from a flag or project configuration."""
    bundle = getattr(args, "bundle", None) or project_config(args).bundle_name
    if not bundle:
        raise CommandError(
            "Bundle name is required. Pass --bundle <bundleName> or add bundleName "
            f"to {DEFAULT_CONFIG_FILE}."
        )
    return bundle


def resolve_module(args: argparse.Namespace) -> str:
    """Resolve the module name from a flag or project configuration."""
    return getattr(args, "module", None) or project_config(args).module_name


def resolve_ability(args: argparse.Namespace) -> str:
    """Resolve the ability name from a flag or project configuration."""
    return getattr(args, "ability", None) or project_config(args).ability_name


def default_app_files_dir(args: argparse.Namespace) -> str:
    """Resolve the app files root from config or the selected module name."""
    configured = project_config(args).app_files_root
    if configured:
        return configured
    return f"/data/storage/el2/base/haps/{resolve_module(args)}/files"


def parse_targets(output: str) -> list[str]:
    """Parse `hdc list targets` output into connect keys."""
    ignored = {"empty", "[empty]", "no targets found"}
    return [
        line.strip().split()[0]
        for line in output.splitlines()
        if line.strip() and line.strip().lower() not in ignored
    ]


def ensure_device_selection(args: argparse.Namespace) -> None:
    """Require an explicit target when multiple HDC devices are connected."""
    if getattr(args, "_device_selection_checked", False):
        return
    hdc = find_hdc(args.hdc)
    result = run_command(
        build_hdc_command(hdc, None, ["list", "targets"]),
        timeout=args.timeout,
    )
    targets = parse_targets(result.stdout)
    if not targets:
        raise CommandError("No HDC target is connected.")
    if args.target:
        if args.target not in targets:
            raise CommandError(
                f"Selected HDC target is not connected: {args.target}. "
                f"Available targets: {', '.join(targets)}"
            )
    elif len(targets) > 1:
        raise CommandError(
            "Multiple HDC targets are connected. Pass --target <connect-key>. "
            f"Available targets: {', '.join(targets)}"
        )
    setattr(args, "_device_selection_checked", True)


def hdc_shell(args: argparse.Namespace, shell_args: Sequence[str]) -> subprocess.CompletedProcess[str]:
    """Run a non-interactive hdc shell command."""
    ensure_device_selection(args)
    hdc = find_hdc(args.hdc)
    return run_command(
        build_hdc_command(hdc, args.target, ["shell", *shell_args]),
        timeout=args.timeout,
    )


def command_doctor(args: argparse.Namespace) -> None:
    """Print local Python/HDC diagnostics and connected devices."""
    hdc = find_hdc(args.hdc)
    config = project_config(args)
    print(f"python: {sys.executable}")
    print(f"platform: {sys.platform}")
    print(f"hdc: {hdc}")
    print(f"config: {config.path or '(none)'}")
    print(f"bundle: {config.bundle_name or '(not configured)'}")
    result = run_command(
        build_hdc_command(hdc, None, ["list", "targets"]),
        check=False,
        timeout=args.timeout,
    )
    print_result(result)
    if result.returncode != 0:
        raise CommandError("hdc list targets failed; check device connection and HDC permissions.")


def command_devices(args: argparse.Namespace) -> None:
    """List HDC targets."""
    hdc = find_hdc(args.hdc)
    print_result(run_command(
        build_hdc_command(hdc, None, ["list", "targets"]),
        timeout=args.timeout,
    ))


def command_start(args: argparse.Namespace) -> None:
    """Start a HarmonyOS ability."""
    shell_args = ["aa", "start", "-a", resolve_ability(args), "-b", resolve_bundle(args)]
    module = resolve_module(args)
    if module:
        shell_args.extend(["-m", module])
    print_result(hdc_shell(args, shell_args))


def command_stop(args: argparse.Namespace) -> None:
    """Force-stop a HarmonyOS bundle."""
    print_result(hdc_shell(args, ["aa", "force-stop", resolve_bundle(args)]))


def app_file_args(operation: str, bundle: str, source: str, destination: str) -> list[str]:
    """Build an hdc file send/recv command scoped to an application sandbox."""
    return ["file", operation, "-b", bundle, source, destination]


def app_shell_path(remote: str) -> str:
    """Normalize app sandbox paths for `hdc shell -b`, which expects ./data/... paths."""
    if remote.startswith("/data/storage/"):
        return "." + remote
    return remote


def command_file_send(args: argparse.Namespace) -> None:
    """Send a local file or directory into the application sandbox."""
    ensure_device_selection(args)
    hdc = find_hdc(args.hdc)
    local = Path(args.local).expanduser()
    if not local.exists():
        raise CommandError(f"Local path does not exist: {local}")
    remote = args.remote or default_app_files_dir(args) + "/"
    cmd = build_hdc_command(
        hdc,
        args.target,
        app_file_args("send", resolve_bundle(args), str(local), remote),
    )
    print_result(run_command(cmd, timeout=args.timeout))


def command_file_recv(args: argparse.Namespace) -> None:
    """Receive a file or directory from the application sandbox."""
    ensure_device_selection(args)
    hdc = find_hdc(args.hdc)
    local = Path(args.local).expanduser()
    local_destination = str(local)
    if args.remote.endswith("/") or local_destination.endswith(os.sep):
        local.mkdir(parents=True, exist_ok=True)
    else:
        local.parent.mkdir(parents=True, exist_ok=True)
    cmd = build_hdc_command(
        hdc,
        args.target,
        app_file_args("recv", resolve_bundle(args), args.remote, local_destination),
    )
    print_result(run_command(cmd, timeout=args.timeout))


def command_file_ls(args: argparse.Namespace) -> None:
    """List files inside the application sandbox."""
    ensure_device_selection(args)
    remote = app_shell_path(args.remote or default_app_files_dir(args))
    shell_args = ["-b", resolve_bundle(args), "ls"]
    if args.long:
        shell_args.append("-lZ")
    shell_args.extend(["-A", remote])
    hdc = find_hdc(args.hdc)
    print_result(run_command(
        build_hdc_command(hdc, args.target, ["shell", *shell_args]),
        timeout=args.timeout,
    ))


def command_file_mkdir(args: argparse.Namespace) -> None:
    """Create a directory inside the application sandbox."""
    ensure_device_selection(args)
    hdc = find_hdc(args.hdc)
    remote = app_shell_path(args.remote)
    print_result(run_command(build_hdc_command(
        hdc,
        args.target,
        ["shell", "-b", resolve_bundle(args), "mkdir", "-p", remote],
    ), timeout=args.timeout))


def remote_file(prefix: str, suffix: str) -> str:
    """Create a unique path in /data/local/tmp for transient device artifacts."""
    stamp = int(time.time() * 1000)
    return f"{DEFAULT_REMOTE_DIR}/{prefix}-{stamp}{suffix}"


def recv_remote(args: argparse.Namespace, remote: str, local: Path) -> None:
    """Pull a remote file from the device and remove the transient source."""
    ensure_device_selection(args)
    hdc = find_hdc(args.hdc)
    local.parent.mkdir(parents=True, exist_ok=True)
    try:
        print_result(run_command(
            build_hdc_command(hdc, args.target, ["file", "recv", remote, str(local)]),
            timeout=args.timeout,
        ))
    finally:
        run_command(
            build_hdc_command(hdc, args.target, ["shell", "rm", "-f", remote]),
            check=False,
            timeout=args.timeout,
        )


def warn_if_tiny_layout(path: Path, bundle: str | None) -> None:
    """Warn when dumpLayout likely returned an empty tree due to over-filtering."""
    if bundle and path.exists() and path.stat().st_size < 1024:
        print(
            "warning: layout tree is very small; if a system picker/dialog is in front, "
            "rerun without --bundle.",
            file=sys.stderr,
        )


def default_local_artifact(prefix: str, suffix: str) -> Path:
    """Create a timestamped local artifact path under the host temp directory."""
    stamp = int(time.time() * 1000)
    return Path(tempfile.gettempdir()) / f"{prefix}-{stamp}{suffix}"


def command_screencap(args: argparse.Namespace) -> None:
    """Capture a screenshot through the official uitest screenCap command."""
    remote = remote_file("codex-screen", ".png")
    print_result(hdc_shell(args, ["uitest", "screenCap", "-p", remote]))
    local = Path(args.out).expanduser().resolve() if args.out else default_local_artifact(
        "harmony-screen",
        ".png",
    )
    recv_remote(args, remote, local)
    print(f"screencap_out={local}")


def command_dump(args: argparse.Namespace) -> None:
    """Dump the live UI layout tree as JSON through uitest dumpLayout."""
    remote = remote_file("codex-layout", ".json")
    shell_args = ["uitest", "dumpLayout", "-p", remote]
    if args.bundle:
        shell_args.extend(["-b", args.bundle])
    if args.invisible:
        shell_args.append("-i")
    if args.merge_windows:
        shell_args.extend(["-m", "true"])
    print_result(hdc_shell(args, shell_args))
    local = Path(args.out).expanduser().resolve() if args.out else default_local_artifact(
        "harmony-layout",
        ".json",
    )
    recv_remote(args, remote, local)
    warn_if_tiny_layout(local, args.bundle)
    print(f"dump_out={local}")


def command_snapshot(args: argparse.Namespace) -> None:
    """Capture screenshot and layout tree with one reusable command."""
    prefix = Path(args.prefix).expanduser().resolve() if args.prefix else default_local_artifact(
        "harmony-state",
        "",
    )
    png_path = prefix.with_suffix(".png")
    json_path = prefix.with_suffix(".json")

    screen_remote = remote_file("codex-screen", ".png")
    print_result(hdc_shell(args, ["uitest", "screenCap", "-p", screen_remote]))
    recv_remote(args, screen_remote, png_path)

    layout_remote = remote_file("codex-layout", ".json")
    shell_args = ["uitest", "dumpLayout", "-p", layout_remote]
    if args.bundle:
        shell_args.extend(["-b", args.bundle])
    if args.invisible:
        shell_args.append("-i")
    if args.merge_windows:
        shell_args.extend(["-m", "true"])
    print_result(hdc_shell(args, shell_args))
    recv_remote(args, layout_remote, json_path)
    warn_if_tiny_layout(json_path, args.bundle)

    print(f"snapshot_png={png_path}")
    print(f"snapshot_json={json_path}")


def command_click(args: argparse.Namespace) -> None:
    """Inject a single click."""
    print_result(hdc_shell(args, ["uitest", "uiInput", "click", str(args.x), str(args.y)]))


def command_double_click(args: argparse.Namespace) -> None:
    """Inject a double click."""
    print_result(hdc_shell(args, ["uitest", "uiInput", "doubleClick", str(args.x), str(args.y)]))


def command_long_click(args: argparse.Namespace) -> None:
    """Inject a long click."""
    print_result(hdc_shell(args, ["uitest", "uiInput", "longClick", str(args.x), str(args.y)]))


def command_swipe(args: argparse.Namespace) -> None:
    """Inject a swipe gesture."""
    shell_args = [
        "uitest",
        "uiInput",
        "swipe",
        str(args.from_x),
        str(args.from_y),
        str(args.to_x),
        str(args.to_y),
    ]
    if args.velocity is not None:
        shell_args.append(str(args.velocity))
    print_result(hdc_shell(args, shell_args))


def command_text(args: argparse.Namespace) -> None:
    """Input text into the focused field or at a coordinate."""
    if args.x is None and args.y is None:
        shell_args = ["uitest", "uiInput", "text", args.value]
    elif args.x is not None and args.y is not None:
        shell_args = ["uitest", "uiInput", "inputText", str(args.x), str(args.y), args.value]
    else:
        raise CommandError("Pass both --x and --y, or neither.")
    print_result(hdc_shell(args, shell_args))


def command_key(args: argparse.Namespace) -> None:
    """Inject a key event such as BACK, HOME, or ENTER."""
    print_result(hdc_shell(args, ["uitest", "uiInput", "keyEvent", args.code]))


def build_hilog_query_args(args: argparse.Namespace) -> list[str]:
    """Build a finite hilog query with optional filters."""
    shell_args = ["hilog"]
    if args.head is not None:
        shell_args.extend(["-a", str(args.head)])
    else:
        shell_args.extend(["-z", str(args.lines)])
    if args.log_type:
        shell_args.extend(["-t", args.log_type])
    if args.level:
        shell_args.extend(["-L", args.level])
    if args.domain:
        shell_args.extend(["-D", args.domain])
    if args.pid:
        shell_args.extend(["-P", str(args.pid)])
    if args.regex:
        shell_args.extend(["-e", args.regex])
    return shell_args


def command_hilog_tail(args: argparse.Namespace) -> None:
    """Print or save a finite recent hilog buffer window."""
    result = hdc_shell(args, build_hilog_query_args(args))
    if args.out:
        out = Path(args.out).expanduser().resolve()
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(result.stdout, encoding="utf-8", errors="replace")
        if result.stderr:
            print(result.stderr, end="" if result.stderr.endswith("\n") else "\n", file=sys.stderr)
        print(f"hilog_out={out}")
        print(f"hilog_bytes={out.stat().st_size}")
        return
    print_result(result)


def command_hilog_clear(args: argparse.Namespace) -> None:
    """Clear device hilog buffers before a focused reproduction."""
    print_result(hdc_shell(args, ["hilog", "-r"]))


def command_hilog_disk(args: argparse.Namespace) -> None:
    """Manage device-side hilog persistence and explicit full log pulls."""
    ensure_device_selection(args)
    hdc = find_hdc(args.hdc)
    if args.action in ("start", "stop"):
        print_result(run_command(
            build_hdc_command(hdc, args.target, ["shell", "hilog", "-w", args.action]),
            timeout=args.timeout,
        ))
        return
    if args.action == "list":
        print_result(run_command(
            build_hdc_command(hdc, args.target, ["shell", "ls", "/data/log/hilog"]),
            timeout=args.timeout,
        ))
        return
    if not args.out:
        raise CommandError("hilog-disk recv requires --out <local-directory>.")
    out = Path(args.out).expanduser()
    out.mkdir(parents=True, exist_ok=True)
    print_result(run_command(
        build_hdc_command(hdc, args.target, ["file", "recv", "/data/log/hilog", str(out)]),
        timeout=args.timeout,
    ))


def add_common_flags(parser: argparse.ArgumentParser) -> None:
    """Add common HDC selection flags to a parser."""
    parser.add_argument(
        "--hdc",
        default=argparse.SUPPRESS,
        help="Path to hdc. Defaults to $HDC or hdc on PATH.",
    )
    parser.add_argument(
        "--target",
        default=argparse.SUPPRESS,
        help="HDC target/connect-key from `hdc list targets`.",
    )
    parser.add_argument(
        "--config",
        default=argparse.SUPPRESS,
        help=f"Project config path. Defaults to ./{DEFAULT_CONFIG_FILE} when present.",
    )
    parser.add_argument(
        "--timeout",
        type=positive_float,
        default=argparse.SUPPRESS,
        help=f"Per-command timeout in seconds. Default: {DEFAULT_TIMEOUT_SECONDS:g}.",
    )


def positive_float(value: str) -> float:
    """Parse a strictly positive timeout value for argparse."""
    parsed = float(value)
    if parsed <= 0:
        raise argparse.ArgumentTypeError("timeout must be greater than zero")
    return parsed


def build_parser() -> argparse.ArgumentParser:
    """Create the command-line parser."""
    common = argparse.ArgumentParser(add_help=False)
    add_common_flags(common)
    parser = argparse.ArgumentParser(
        description="HarmonyOS HDC/UiTest device helper",
        parents=[common],
    )
    sub = parser.add_subparsers(dest="command", required=True)

    doctor = sub.add_parser(
        "doctor",
        help="Show Python, HDC, and device diagnostics.",
        parents=[common],
    )
    doctor.set_defaults(func=command_doctor)

    devices = sub.add_parser("devices", help="List connected HDC targets.", parents=[common])
    devices.set_defaults(func=command_devices)

    start = sub.add_parser("start", help="Start an ability.", parents=[common])
    start.add_argument("--bundle", help=f"Bundle name or configure it in {DEFAULT_CONFIG_FILE}.")
    start.add_argument("--ability", help=f"Ability name. Config/default: {DEFAULT_ABILITY_NAME}.")
    start.add_argument("--module", help=f"Module name. Config/default: {DEFAULT_MODULE_NAME}.")
    start.set_defaults(func=command_start)

    stop = sub.add_parser("stop", help="Force-stop a bundle.", parents=[common])
    stop.add_argument("--bundle", help=f"Bundle name or configure it in {DEFAULT_CONFIG_FILE}.")
    stop.set_defaults(func=command_stop)

    file_send = sub.add_parser(
        "file-send",
        help="Send a local file or directory into the application sandbox.",
        parents=[common],
    )
    file_send.add_argument("local", help="Local file or directory to send.")
    file_send.add_argument(
        "remote",
        nargs="?",
        help="Remote sandbox destination. Defaults to the configured module files directory.",
    )
    file_send.add_argument("--bundle", help=f"Bundle name or configure it in {DEFAULT_CONFIG_FILE}.")
    file_send.add_argument("--module", help=f"Module name. Config/default: {DEFAULT_MODULE_NAME}.")
    file_send.set_defaults(func=command_file_send)

    file_recv = sub.add_parser(
        "file-recv",
        help="Receive a sandbox file or directory to the local machine.",
        parents=[common],
    )
    file_recv.add_argument("remote", help="Remote sandbox source path.")
    file_recv.add_argument("local", help="Local destination path.")
    file_recv.add_argument("--bundle", help=f"Bundle name or configure it in {DEFAULT_CONFIG_FILE}.")
    file_recv.add_argument("--module", help=f"Module name. Config/default: {DEFAULT_MODULE_NAME}.")
    file_recv.set_defaults(func=command_file_recv)

    file_ls = sub.add_parser(
        "file-ls",
        help="List files inside the application sandbox.",
        parents=[common],
    )
    file_ls.add_argument("remote", nargs="?", help="Remote sandbox path.")
    file_ls.add_argument("--bundle", help=f"Bundle name or configure it in {DEFAULT_CONFIG_FILE}.")
    file_ls.add_argument("--module", help=f"Module name. Config/default: {DEFAULT_MODULE_NAME}.")
    file_ls.add_argument("--long", action="store_true", help="Use ls -lZ -A instead of ls -A.")
    file_ls.set_defaults(func=command_file_ls)

    file_mkdir = sub.add_parser(
        "file-mkdir",
        help="Create a directory inside the application sandbox.",
        parents=[common],
    )
    file_mkdir.add_argument("remote", help="Remote sandbox directory path.")
    file_mkdir.add_argument("--bundle", help=f"Bundle name or configure it in {DEFAULT_CONFIG_FILE}.")
    file_mkdir.add_argument("--module", help=f"Module name. Config/default: {DEFAULT_MODULE_NAME}.")
    file_mkdir.set_defaults(func=command_file_mkdir)

    screencap = sub.add_parser(
        "screencap",
        help="Capture screenshot and pull it locally.",
        parents=[common],
    )
    screencap.add_argument("--out", help="Local output PNG path. Defaults to the host temp directory.")
    screencap.set_defaults(func=command_screencap)

    dump = sub.add_parser("dump", help="Dump UI layout tree and pull it locally.", parents=[common])
    dump.add_argument("--out", help="Local output JSON path. Defaults to the host temp directory.")
    dump.add_argument("--bundle", help="Filter dumpLayout by bundle name.")
    dump.add_argument("--invisible", action="store_true", help="Include invisible controls.")
    dump.add_argument("--merge-windows", action="store_true", help="Merge window information.")
    dump.set_defaults(func=command_dump)

    snapshot = sub.add_parser(
        "snapshot",
        help="Capture screenshot and UI layout tree with one command.",
        parents=[common],
    )
    snapshot.add_argument(
        "--prefix",
        help="Local output prefix; writes .png and .json. Defaults to the host temp directory.",
    )
    snapshot.add_argument("--bundle", help="Filter dumpLayout by bundle name.")
    snapshot.add_argument("--invisible", action="store_true", help="Include invisible controls in layout.")
    snapshot.add_argument("--merge-windows", action="store_true", help="Merge window information in layout.")
    snapshot.set_defaults(func=command_snapshot)

    click = sub.add_parser("click", help="Inject click at x y.", parents=[common])
    click.add_argument("x", type=int)
    click.add_argument("y", type=int)
    click.set_defaults(func=command_click)

    double_click = sub.add_parser(
        "double-click",
        help="Inject double click at x y.",
        parents=[common],
    )
    double_click.add_argument("x", type=int)
    double_click.add_argument("y", type=int)
    double_click.set_defaults(func=command_double_click)

    long_click = sub.add_parser(
        "long-click",
        help="Inject long click at x y.",
        parents=[common],
    )
    long_click.add_argument("x", type=int)
    long_click.add_argument("y", type=int)
    long_click.set_defaults(func=command_long_click)

    swipe = sub.add_parser(
        "swipe",
        help="Inject swipe from one coordinate to another.",
        parents=[common],
    )
    swipe.add_argument("from_x", type=int)
    swipe.add_argument("from_y", type=int)
    swipe.add_argument("to_x", type=int)
    swipe.add_argument("to_y", type=int)
    swipe.add_argument("--velocity", type=int, help="Swipe speed in px/s.")
    swipe.set_defaults(func=command_swipe)

    text = sub.add_parser(
        "text",
        help="Input text into focused field or coordinate.",
        parents=[common],
    )
    text.add_argument("value")
    text.add_argument("--x", type=int, help="X coordinate for inputText.")
    text.add_argument("--y", type=int, help="Y coordinate for inputText.")
    text.set_defaults(func=command_text)

    key = sub.add_parser("key", help="Inject key event.", parents=[common])
    key.add_argument("code", help="Key code name or numeric code, for example BACK.")
    key.set_defaults(func=command_key)

    hilog_tail = sub.add_parser(
        "hilog-tail",
        help="Print or save a finite recent hilog buffer window.",
        parents=[common],
    )
    hilog_tail.add_argument("--lines", type=int, default=300, help="Tail line count for -z. Default: 300.")
    hilog_tail.add_argument("--head", type=int, help="Use -a <n> instead of tailing with -z.")
    hilog_tail.add_argument("--type", dest="log_type", default="app", help="Log type for -t, for example app.")
    hilog_tail.add_argument("--level", choices=["D", "I", "W", "E", "F"], help="Minimum log level for -L.")
    hilog_tail.add_argument("--domain", help="Domain filter for -D, for example 01B06 or 0x3200.")
    hilog_tail.add_argument("--pid", type=int, help="Process id filter for -P.")
    hilog_tail.add_argument("--regex", help="Regex/keyword filter for -e.")
    hilog_tail.add_argument("--out", help="Local file path to save stdout instead of printing all logs.")
    hilog_tail.set_defaults(func=command_hilog_tail)

    hilog_clear = sub.add_parser(
        "hilog-clear",
        help="Clear hilog buffers before a focused reproduction.",
        parents=[common],
    )
    hilog_clear.set_defaults(func=command_hilog_clear)

    hilog_disk = sub.add_parser(
        "hilog-disk",
        help="Start/stop/list/receive device-side hilog persistence.",
        parents=[common],
    )
    hilog_disk.add_argument("action", choices=["start", "stop", "list", "recv"])
    hilog_disk.add_argument("--out", help="Local directory for `recv` from /data/log/hilog.")
    hilog_disk.set_defaults(func=command_hilog_disk)

    return parser


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    """Parse CLI arguments while preserving common flags before or after subcommands."""
    args = build_parser().parse_args(argv)
    defaults = {
        "hdc": None,
        "target": None,
        "config": None,
        "timeout": DEFAULT_TIMEOUT_SECONDS,
    }
    for name, value in defaults.items():
        if not hasattr(args, name):
            setattr(args, name, value)
    return args


def main(argv: Sequence[str] | None = None) -> int:
    """Run the CLI."""
    args = parse_args(argv)
    try:
        args.func(args)
    except CommandError as exc:
        print(str(exc), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
