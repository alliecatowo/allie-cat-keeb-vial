# Agent Instructions — Allie Cat Keeb Vial

This repository is a **Vial-enabled QMK firmware** fork for holykeebs split keyboards with
pointing devices (trackballs, touchpads, trackpoints). The primary keyboard target is the
Lily58 Rev1 with an RP2040 controller.

---

## Quick orientation

| Path | What it is |
|------|-----------|
| `build.py` | Main build/CI orchestration script (Python) |
| `keyboards/lily58/` | Lily58 keyboard definition; keymaps in `rev1/keymaps/` |
| `users/holykeebs/` | Holykeebs userspace — pointing-device rules (`rules.mk`) and C sources |
| `drivers/` | Low-level device drivers (SPI, I²C, pointing devices) |
| `quantum/` | QMK core — modify with **extreme care** |
| `tests/` | Python unit tests (`test_build_py.py`) — run without any C toolchain |
| `tools/callgraph.py` | Generates the Azoteq IQS5xx call-graph SVG |
| `.github/workflows/` | CI/CD workflows |

---

## Bootstrap (one-time setup)

```bash
pip3 install -r requirements-dev.txt
```

No other setup is required to run the fast checks below.

---

## Fast checks — no ARM toolchain needed (< 10 seconds)

Run these first. They validate all Python/build-system logic without compiling C.

```bash
# 1. Unit tests for build.py
python3 -m pytest tests/test_build_py.py -v
# Alternative without pytest:
python3 -m unittest tests.test_build_py -v

# 2. Validate CI matrix JSON
python3 build.py --generate-matrix-release

# 3. Lint Python files
flake8 build.py tools/callgraph.py tests/test_build_py.py
```

---

## Firmware builds — requires ARM cross-compiler

Full firmware builds need `gcc-arm-none-eabi` and `make`.

```bash
# Build default personal config (trackball_tps43, both sides)
python3 build.py

# Build a single variant
python3 build.py --build-single \
  --keyboard lily58/rev1 \
  --keymap vial \
  --left-device trackball \
  --right-device tps43 \
  --side left

# Generate CI build matrix JSON
python3 build.py --generate-matrix-release
```

Build outputs (`.uf2` files) land in `build_lily58/`. They are **gitignored** — never commit them.

---

## Key conventions

### Build system
- `POINTING_DEVICE` must be a value from `VALID_POINTING_DEVICE_CONFIGURATIONS`
  (defined in `users/holykeebs/rules.mk`).
- Dual-device configs (e.g. `trackball_tps43`) require `SIDE=left|right`.
- Single-device configs use `POINTING_DEVICE_POSITION=left|right|thumb`.
- When building `keymap=vial` directly with `make`, always pass `VIAL_ENABLE=yes`.
  `build.py --build-single` handles this automatically.

### Testing
- All `build.py` logic has fast Python unit tests in `tests/test_build_py.py`.
- **Always** update or add tests when changing `build.py`.
- The CI matrix currently emits **2 entries** (left + right sides of `trackball_tps43`
  on `lily58/rev1`). Expanding it means editing `generate_matrix()` in `build.py`
  **and** updating the corresponding test assertions.

### Commit style
Use conventional commits: `feat:`, `fix:`, `chore:`, `docs:`, `ci:`, `refactor:`, `test:`.

### Things to avoid
- Do **not** modify `quantum/` unless you fully understand QMK internals.
- Do **not** add new Python dependencies without updating `requirements.txt` (runtime)
  or `requirements-dev.txt` (dev/test).
- Do **not** commit `.uf2` firmware binaries or `build_lily58/` output directories.
- Do **not** change `VIAL_ENABLE` handling in `users/holykeebs/rules.mk` without testing
  both the `vial` and `via` keymaps.
