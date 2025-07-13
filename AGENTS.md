
# Repository Guidelines

- Run `pytest -q` before committing changes to verify unit tests.
- If tests fail due to missing dependencies, install them with `pip install -r requirements-dev.txt`.
- The CI workflows build firmware from the `dev` branch by default, so ensure pull requests target `dev` unless otherwise noted.

# Repo Guide for Codex Agents

This file provides instructions for OpenAI Codex (and similar agents) when working in this repository.

## Overview
- **Project**: Vial-enabled fork of holykeebs QMK firmware
- **Purpose**: Add and maintain Vial support while syncing with the holykeebs fork. Provides build scripts, GitHub Actions, and documentation.
- **Important docs**: [docs.holykeebs.com](https://docs.holykeebs.com), [docs.qmk.fm](https://docs.qmk.fm), [docs.getvial.today](https://docs.getvial.today), and [agentsmd.net](https://agentsmd.net).
- **Outstanding tasks**: see `ISSUES_TO_CREATE.md` for the planned roadmap.

## Local Setup
1. Install QMK dependencies. Example for Debian/Ubuntu:
   ```bash
   sudo apt-get update
   sudo apt-get install -y git python3-pip
   pip3 install qmk
   qmk setup -y
   ```
2. Optionally use `shell.nix` for a reproducible environment (`nix-shell`).
3. Clone with submodules:
   ```bash
   git clone --recurse-submodules https://github.com/YOUR_USERNAME/allie-cat-keeb-vial.git
   ```
4. If submodules are missing after cloning, run `scripts/init_submodules.sh`.

## Building Firmware
- Preferred: use `build.py`.
  ```bash
  python build.py                    # default trackball_tps43 build
  python build.py --build-all        # all configs
  python build.py --build-single \
    --keyboard lily58/rev1 \
    --keymap vial \
    --left-device trackball \
    --right-device tps43 \
    --side left
  ```
- Manual make example:
  ```bash
  make lily58/rev1:via -e USER_NAME=holykeebs \
      -e POINTING_DEVICE=trackball_tps43 \
      -e SIDE=left \
      -e TRACKBALL_RGB_RAINBOW=yes \
      -e VIAL_ENABLE=yes
  ```
- Build artifacts are placed in `build_lily58/` by default.

## Testing and Linting
- Install dev requirements and init submodules first:
  ```bash
  scripts/init_submodules.sh
  pip install -r requirements-dev.txt
  ```
- Run tests and lint checks with `qmk pytest` (uses `nose2`, `flake8`, and `yapf`).
- Format Python code with `qmk format-python`.
- CI runs these checks in `.github/workflows/pr-checks.yml`.

## Call Graph Generation
- A helper script (`tools/callgraph.py`) can generate an SVG call graph for the Azoteq driver:
  ```bash
  python3 tools/callgraph.py
  ```
  Output is written to `docs/azoteq_callgraph.svg`.

## Pull Requests
- Follow conventional commits (`feat:`, `fix:`, `docs:`, etc.).
- Ensure PR descriptions are at least 50 characters (enforced by CI).
- GitHub Actions build firmware and run checks automatically.
- The PR assistant responds to `/ready` and `/build` comments.

## Commit Style
- Keep commits focused.
- Include tests or docs when modifying code.

## Further Reading
- Hardware guides and pointing device setup: [docs.holykeebs.com](https://docs.holykeebs.com)
- QMK firmware docs: [docs.qmk.fm](https://docs.qmk.fm)
- Vial usage and features: [docs.getvial.today](https://docs.getvial.today)
- Agent behavior guidelines: [agentsmd.net](https://agentsmd.net)


## Build/Flash Commands
- Use `make` rather than `qmk compile` for Vial and holykeebs configs:
  ```bash
  make <keyboard>:<keymap> -e VIAL_ENABLE=yes [other flags]
  make <keyboard>:<keymap>:flash        # compile and flash
  ```
- `qmk doctor` can still verify your environment.

## Vial Notes
- This fork integrates Vial for real-time configuration.
- Flash Vial-enabled firmware then open the Vial app to customize keys, macros, and lighting.
- `*.vil` files in `keyboards/<keyboard>` define Vial layouts.

## Holykeebs Specifics
- Supports Pimoroni trackball, Azoteq TPS43/TPS65 touchpads, and PS2 trackpoints.
- Dual pointing devices are possible (e.g., trackball on left, touchpad on right).
- Build matrix definitions live in `builddefs/` and pre-built firmware resides in `build_lily/`.

