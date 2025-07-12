import json
import subprocess
from pathlib import Path


def test_hk_keymap_c2json():
    repo_root = Path(__file__).resolve().parents[2]
    keymap = repo_root / "keyboards" / "lily58" / "keymaps" / "hk" / "keymap.c"
    result = subprocess.run(
        [
            "qmk",
            "c2json",
            str(keymap),
            "-kb",
            "lily58/rev1",
            "-km",
            "hk",
            "--no-cpp",
        ],
        capture_output=True,
        text=True,
        cwd=repo_root,
    )
    assert result.returncode == 0, result.stderr
    data = json.loads(result.stdout)
    assert data["keyboard"] == "lily58/rev1"
    assert data["keymap"] == "hk"
