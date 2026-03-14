# Codex Quickstart

Use these steps to bootstrap automation (or a fresh contributor machine) so Codex can run the same checks locally.

## Bootstrap
1. Install Python 3.11+.
2. Install dependencies: `pip3 install -r requirements-dev.txt`

## Fast checks (no ARM toolchain needed — complete in < 10 seconds)

```bash
# Run Python unit tests for build.py
python3 -m pytest tests/test_build_py.py -v
# Alternative if pytest is unavailable:
python3 -m unittest tests.test_build_py -v

# Validate CI matrix JSON output
python3 build.py --generate-matrix-release

# Lint Python files
flake8 build.py tools/callgraph.py tests/test_build_py.py
```

## Firmware builds (requires ARM cross-compiler)

Full firmware builds need `gcc-arm-none-eabi` and `make` (see `.github/workflows/pr-checks.yml`).

```bash
# Build default configuration (trackball_tps43, both sides)
python3 build.py

# Build a single variant
python3 build.py --build-single \
  --keyboard lily58/rev1 \
  --keymap vial \
  --left-device trackball \
  --right-device tps43 \
  --side left
```

## Key conventions
- Always update `tests/test_build_py.py` when changing `build.py`.
- Use conventional commits: `feat:`, `fix:`, `chore:`, `docs:`, `ci:`, `refactor:`, `test:`.
- Do **not** commit `.uf2` binaries or `build_lily58/` directories (they are in `.gitignore`).
