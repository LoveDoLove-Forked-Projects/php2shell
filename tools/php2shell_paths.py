#!/usr/bin/env python3
"""Shared path resolution for the upstream PHP2Shell checkout."""

from __future__ import annotations

import os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
VENDOR = ROOT / "vendor" / "php2shell-upstream"
FALLBACK = Path("/tmp/php2shell-rce")


def default_repo_dir() -> str:
    """Prefer the bootstrapped checkout, then the historical /tmp clone."""
    env = os.environ.get("P2S_REPO_DIR")
    if env:
        return env
    if (VENDOR / "exploit.py").is_file():
        return str(VENDOR)
    return str(FALLBACK)
