# Codex Quickstart

Use these steps to bootstrap automation (or a fresh contributor machine) so Codex can run the same checks locally.

## Bootstrap
1. Install Python 3.11+.
2. Install dependencies: `python -m pip install -r requirements-dev.txt`
3. Point the CLI at this checkout:
   ```bash
   export ORIG_CWD="$PWD"
   export QMK_HOME="$PWD"
   export QMK_FIRMWARE="$PWD"
   export PYTHONPATH="$PWD/lib/python"
   export PATH="$PWD/bin:$PATH"
   ```

## Fast checks to run
- `flake8 lib/python` – lint the Python helpers we rely on for builds.
- `python -m nose2 -v` – run the QMK CLI smoke tests (uses the local `bin/qmk` shim).

## Firmware builds
For full firmware builds you also need the cross-compilers used in CI (see `.github/workflows/pr-checks.yml`). The Codex checks above run without those toolchains.
