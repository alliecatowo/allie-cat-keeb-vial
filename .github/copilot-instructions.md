# GitHub Copilot Instructions — Allie Cat Keeb Vial

This repository is a **Vial-enabled fork** of the [holykeebs/qmk_firmware](https://github.com/idank/qmk_firmware)
codebase. It adds real-time keyboard configuration (Vial) to holykeebs' pointing-device drivers for
split keyboards (primarily the Lily58).

---

## Repository layout (key paths)

| Path | What it is |
|------|-----------|
| `build.py` | Main build/CI orchestration script |
| `keyboards/lily58/` | Lily58 keyboard definition (keymaps live in `rev1/keymaps/`) |
| `users/holykeebs/` | Holykeebs userspace: pointing-device rules (`rules.mk`), C sources |
| `drivers/` | Low-level device drivers (SPI, I²C, pointing devices) |
| `quantum/` | QMK core — modify with extreme care |
| `tests/` | Firmware C++ unit tests *and* Python `test_build_py.py` |
| `tools/callgraph.py` | Generates the Azoteq IQS5xx driver call-graph SVG |
| `docs/` | QMK + project documentation; `azoteq_callgraph.svg` lives here |
| `.github/workflows/` | CI/CD workflows |

---

## How to build & test **quickly** (no firmware compile needed)

```bash
# 1. Run Python unit tests for build.py (completes in < 5 seconds)
python3 -m unittest tests.test_build_py -v
# or with pytest (if installed):
python3 -m pytest tests/test_build_py.py -v

# 2. Validate the CI matrix JSON
python3 build.py --generate-matrix-release

# 3. Lint Python files
flake8 build.py tools/callgraph.py tests/test_build_py.py

# 4. Generate the call-graph without building firmware
python3 tools/callgraph.py
```

Full firmware builds require ARM cross-compiler toolchain + QMK CLI (`qmk`) and take several
minutes. Avoid them during rapid iteration — the Python tests above cover all `build.py` logic.

---

## Firmware build commands

```bash
# Build the default personal config (lily58, trackball left + TPS43 right, both sides)
python3 build.py

# Build a single variant
python3 build.py --build-single \
  --keyboard lily58/rev1 \
  --keymap vial \
  --left-device trackball \
  --right-device tps43 \
  --side left

# Generate CI matrix JSON (used by build-firmware.yml)
python3 build.py --generate-matrix-release
```

---

## Key conventions & rules

### Build system (`build.py` + `users/holykeebs/rules.mk`)

- `POINTING_DEVICE` must be one of the values in `VALID_POINTING_DEVICE_CONFIGURATIONS`
  (defined in `users/holykeebs/rules.mk`).
- Dual-device configs (e.g. `trackball_tps43`) require a `SIDE=left|right` argument;
  single-device configs use `POINTING_DEVICE_POSITION=left|right|thumb`.
- The holykeebs userspace only activates when `POINTING_DEVICE` is set.
- Pass `VIAL_ENABLE=yes` when building `keymap=vial` via direct `make` — `build.py --build-single`
  does **not** add this flag automatically (the keymap `rules.mk` handles it instead).

### CI matrix

`generate_matrix()` in `build.py` currently emits exactly **two entries**: left and right sides of
the `trackball_tps43` configuration for `lily58/rev1`. Expanding the matrix means editing that
function — keep the JSON schema consistent (`keyboard`, `keyboard_name`, `keymap`, `left_device`,
`right_device`, `side`, `debug`).

### Testing (`tests/test_build_py.py`)

All `build.py` logic is covered by Python unit tests that run without any C toolchain. Always
update or add tests when changing `build.py`. Run them with:

```bash
python3 -m unittest tests.test_build_py -v
```

### Commit style

Use conventional commits: `feat:`, `fix:`, `chore:`, `docs:`, `ci:`, `refactor:`, `test:`.

---

## Common tasks for agents

### Add a new pointing-device combination to the CI matrix

1. Edit `generate_matrix()` in `build.py` — add entries following the existing schema.
2. Update `tests/test_build_py.py` to assert the new matrix length and entry content.
3. Run `python3 -m unittest tests.test_build_py -v` — must pass.

### Add support for a new keyboard

1. Create `keyboards/<name>/rev1/keymaps/vial/` with `keymap.c`, `rules.mk`, `config.h`,
   and a `.vil` definition file.
2. Add matrix entries in `build.py` for the new keyboard.
3. Update `build.py --build-single` logic if the new keyboard has a different `build_dir`
   convention.

### Fix a pointing-device driver

Drivers live in `drivers/` (C) and are glued in `users/holykeebs/`.
After editing, validate with a firmware build:

```bash
python3 build.py --build-single --keyboard lily58/rev1 --keymap vial \
  --left-device trackball --right-device tps43 --side left
```

### Update documentation

- Project-level docs: edit `readme.md` or files under `docs/`.
- Call-graph: regenerate with `python3 tools/callgraph.py`; the SVG is committed to `docs/`.

---

## Workflow permissions reference

| Workflow | Key permissions needed |
|----------|----------------------|
| `build-firmware.yml` | `contents: read` globally; `contents: write` for release job only |
| `pr-checks.yml` | `contents: read`, `pull-requests: write` |
| `pr-assistant.yml` | `contents: read`, `pull-requests: write`, `issues: write` |
| `changelog.yml` | `contents: write`, `pull-requests: write` |
| `sync-upstreams.yml` | `contents: write` |

All workflows use `actions/checkout@v4`, `actions/setup-python@v4` (Python 3.11), and
`actions/upload-artifact@v4`.

---

## Secrets & environment variables

| Variable | Purpose |
|----------|---------|
| `GITHUB_TOKEN` | Auto-provided; used for releases, PR comments, labeling |

No additional secrets are required for standard builds.

---

## Things to avoid

- Do **not** modify `quantum/` unless you fully understand QMK internals — breaking changes here
  affect all keyboards.
- Do **not** add new Python dependencies without adding them to `requirements.txt` (runtime) or
  `requirements-dev.txt` (dev/test only).
- Do **not** commit `.uf2` firmware binaries or `build_lily58/` output directories — they are in
  `.gitignore`.
- Do **not** change `VIAL_ENABLE` handling in `users/holykeebs/rules.mk` without testing both the
  `vial` and `via` keymaps.
