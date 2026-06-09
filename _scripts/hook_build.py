#!/usr/bin/env python3
"""
PostToolUse hook — auto-rebuilds skill index when Skills/ files change.

Registered in: D:\Claude Repo\Claude Skills Vault\.claude\settings.json
Triggers on:   Write or Edit tool use where file_path contains "Skills/"
"""

import json
import sys
import subprocess
from pathlib import Path

VAULT = Path(r"D:\Claude Repo\Claude Skills Vault")
SKILLS_DIR = VAULT / "Skills"


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        sys.exit(0)

    tool = data.get("tool_name", "")
    tool_input = data.get("tool_input", {})

    # Works for both Write (file_path) and Edit (file_path)
    file_path = tool_input.get("file_path", "")

    if not file_path:
        sys.exit(0)

    # Only trigger for files inside the Skills/ directory
    try:
        Path(file_path).relative_to(SKILLS_DIR)
    except ValueError:
        sys.exit(0)  # Not a Skills/ file

    if tool not in ("Write", "Edit"):
        sys.exit(0)

    # Run the build script
    result = subprocess.run(
        [sys.executable, str(VAULT / "_scripts" / "build_skill_brain.py")],
        cwd=str(VAULT),
        capture_output=True,
        text=True,
    )

    if result.returncode == 0:
        # Print to stdout so Claude sees it
        summary = result.stdout.strip().split("\n")[-1]  # Last line (Done.)
        print(f"[hook:build] Index rebuilt — {summary}")
    else:
        print(f"[hook:build] Build failed:\n{result.stderr.strip()}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
