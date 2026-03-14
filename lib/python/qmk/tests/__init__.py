"""Shared test setup for QMK CLI tests."""
import os
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]
BIN_DIR = REPO_ROOT / "bin"

sys.path.insert(0, str(REPO_ROOT / "lib" / "python"))

os.environ.setdefault("ORIG_CWD", str(REPO_ROOT))
os.environ.setdefault("QMK_HOME", str(REPO_ROOT))
os.environ.setdefault("QMK_FIRMWARE", str(REPO_ROOT))

if BIN_DIR.exists():
    os.environ["PATH"] = os.pathsep.join([str(BIN_DIR), os.environ.get("PATH", "")])
