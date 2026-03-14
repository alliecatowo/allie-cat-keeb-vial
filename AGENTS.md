# Agent & Codex Setup — Allie Cat Keeb Vial

This file is read automatically by OpenAI Codex and GitHub Copilot Coding Agent to bootstrap the
environment before any tool calls or sub-agent invocations (including explore, task, and
general-purpose agents).

---

## Environment Bootstrap

**Run these commands first in every new shell session before executing any project commands:**

```bash
export ORIG_CWD="$PWD"
export QMK_HOME="$PWD"
export QMK_FIRMWARE="$PWD"
export PYTHONPATH="$PWD/lib/python"
export PATH="$PWD/bin:$PATH"
```

**Install Python dependencies** (if not already installed):

```bash
python3 -m pip install -r requirements-dev.txt
```

---

## Quick Checks (no firmware toolchain required)

```bash
# 1. Python unit tests for build.py logic (~5 seconds)
python3 -m unittest tests.test_build_py -v

# 2. Validate CI matrix JSON
python3 build.py --generate-matrix-release

# 3. Lint Python files
flake8 build.py tools/callgraph.py tests/test_build_py.py \
  --max-line-length=120 --extend-ignore=E501,W503

# 4. QMK CLI smoke tests (requires env exports above)
python3 -m nose2 -v
```

---

## Repository Layout

| Path | Purpose |
|------|---------|
| `build.py` | Main build/CI orchestration script |
| `keyboards/lily58/` | Lily58 keyboard definition; keymaps under `rev1/keymaps/` |
| `users/holykeebs/` | Holykeebs userspace: pointing-device rules and C sources |
| `drivers/` | Low-level device drivers (SPI, I²C, pointing devices) |
| `quantum/` | QMK core — modify with caution |
| `tests/` | Python unit tests (`test_build_py.py`) and firmware C++ tests |
| `tools/callgraph.py` | Generates the Azoteq IQS5xx driver call-graph SVG |
| `docs/` | Documentation; `azoteq_callgraph.svg` lives here |
| `.github/workflows/` | CI/CD workflows |

---

## Key Rules for Agents

- Always set the environment variables above before running any `python3`, `qmk`, or `make` command.
- Use `python3 -m unittest tests.test_build_py -v` to verify build logic — it runs in seconds with no C toolchain.
- Do **not** modify `quantum/` unless you fully understand QMK internals.
- Full firmware builds require an ARM cross-compiler (`gcc-arm-none-eabi`). Skip them during rapid iteration.
- Use conventional commits: `feat:`, `fix:`, `chore:`, `docs:`, `ci:`, `refactor:`, `test:`.

---

## Firmware Build (when ARM toolchain is available)

```bash
# Build default config (lily58, trackball left + TPS43 right, both sides)
python3 build.py

# Build a single variant
python3 build.py --build-single \
  --keyboard lily58/rev1 \
  --keymap vial \
  --left-device trackball \
  --right-device tps43 \
  --side left
```

See `docs/codex.md` for additional bootstrap details.
