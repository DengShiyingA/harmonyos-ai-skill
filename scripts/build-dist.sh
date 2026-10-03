#!/usr/bin/env bash
# POSIX wrapper for the cross-platform Python distribution builder.
set -euo pipefail

PYTHON_BIN="${PYTHON:-python3}"
exec "$PYTHON_BIN" scripts/build_dist.py "$@"
