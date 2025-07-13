#!/usr/bin/env python3
"""Generate keymap diagrams for selected boards."""
import os
import subprocess
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]

BOARDS = [
    {
        "id": "lily58/rev1",
        "name": "lily58",
        "info": None,
        "output": REPO_ROOT / "docs" / "keymap_lily58.svg",
    },
    {
        "id": "holykeebs/sweeq",
        "name": "sweeq",
        "info": REPO_ROOT / "keyboards" / "holykeebs" / "sweeq" / "keyboard.json",
        "output": REPO_ROOT / "docs" / "keymap_sweeq.svg",
    },
    {
        "id": "holykeebs/spankbd",
        "name": "spankbd",
        "info": REPO_ROOT / "keyboards" / "holykeebs" / "spankbd" / "keyboard.json",
        "output": REPO_ROOT / "docs" / "keymap_spankbd.svg",
    },
    {
        "id": "crkbd",
        "name": "corne",
        "info": REPO_ROOT / "keyboards" / "crkbd" / "info.json",
        "output": REPO_ROOT / "docs" / "keymap_corne.svg",
    },
]


def run(cmd, **kwargs):
    print("Running:", " ".join(str(c) for c in cmd))
    subprocess.run(cmd, check=True, **kwargs)


def generate(board):
    env = os.environ.copy()
    env["QMK_HOME"] = str(REPO_ROOT)
    with tempfile.TemporaryDirectory() as tmp:
        json_path = Path(tmp) / f"{board['name']}.json"
        yaml_path = Path(tmp) / f"{board['name']}.yaml"
        run([
            "qmk",
            "c2json",
            "-kb",
            board["id"],
            "-km",
            "vial",
            "--no-cpp",
            "-o",
            str(json_path),
        ], env=env)
        run(["keymap", "parse", "-q", str(json_path), "-o", str(yaml_path)])
        cmd = ["keymap", "draw"]
        if board.get("info"):
            cmd.extend(["-j", str(board["info"])])
        else:
            cmd.extend(["-k", board["id"]])
        cmd.extend([str(yaml_path), "-o", str(board["output"])])
        run(cmd)


def main():
    for board in BOARDS:
        generate(board)


if __name__ == "__main__":
    main()
