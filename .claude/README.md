# Claude Code Configuration for Allie Cat Keeb Vial

This directory contains configuration and guidance for Claude Code when working on this repository.

## Repository Overview

This is a **Vial-enabled QMK firmware** fork specifically designed for holykeebs keyboards with pointing devices. The repository:

- Backports Vial support to holykeebs' QMK firmware (based on older QMK)
- Supports various pointing devices (trackballs, touchpads, trackpoints)
- Targets the Lily58 Rev1 keyboard with RP2040 controller
- Uses a custom build system (`build.py`) for generating firmware variants
- Maintains automated CI/CD through GitHub Actions

## Key Technical Constraints

### Memory Limitations
- **Target MCU**: RP2040 (2MB flash)
- **Firmware size**: Warn if over 1.5MB
- Vial support adds significant overhead, requiring careful feature selection

### Build System
- **Primary build script**: `build.py` (Python)
- **Build command**: `make lily58/rev1:via -e USER_NAME=holykeebs -e POINTING_DEVICE=<config> -e VIAL_ENABLE=yes`
- **Build outputs**: `.uf2` files in `build_lily58/` directory
- **Configuration variables**:
  - `POINTING_DEVICE`: Device configuration (e.g., `trackball_tps43`)
  - `SIDE`: `left` or `right` for split keyboards
  - `TRACKBALL_RGB_RAINBOW`: Enable trackball RGB effects
  - `CONSOLE`: Enable debug console output
  - `OLED`: Enable OLED support

### Critical Build Requirements
- When building `keymap=vial`, **MUST** pass `VIAL_ENABLE=yes` to avoid build errors
- Holykeebs userspace only builds when `POINTING_DEVICE` is set
- Build generates 55 matrix entries for all device combinations

## Project Structure

```
.
├── build.py                    # Main build script
├── keyboards/lily58/           # Keyboard definitions
├── users/holykeebs/            # Holykeebs userspace code
│   └── rules.mk               # Conditional build rules for pointing devices
├── quantum/                    # QMK core with Vial modifications
├── drivers/                    # Pointing device drivers
├── .github/workflows/          # CI/CD workflows
│   ├── build-firmware.yml     # Release builds
│   ├── pr-checks.yml          # PR validation
│   └── sync-upstreams.yml     # Upstream sync automation
└── docs/                       # Documentation
```

## Common Tasks

### Building Firmware

```bash
# Build default trackball_tps43 configuration (both sides)
python build.py

# Build specific configuration
python build.py --build-single \
  --keyboard lily58/rev1 \
  --keymap vial \
  --left-device trackball \
  --right-device tps43 \
  --side left

# Build with debug output
python build.py --build-single \
  --left-device trackball \
  --right-device tps43 \
  --side left \
  --debug
```

### Testing Changes

```bash
# Run QMK tests
make test:all

# Build specific test
make test:basic

# Lint Python code
flake8 build.py

# Format Python code
yapf -i build.py
```

### Firmware Flashing

1. Enter bootloader mode (double-tap RESET)
2. Copy `.uf2` file to `RPI-RP2` drive
3. Firmware automatically loads

## Code Conventions

### C/C++ Code
- Follow QMK coding style
- Use existing patterns from `quantum/` and `keyboards/`
- Keep memory usage minimal (RP2040 constraints)
- Document complex pointing device logic

### Python Code
- Follow PEP 8 style guide
- Use type hints where applicable
- Keep `build.py` maintainable and well-documented

### Commit Messages
- Use conventional commits: `feat:`, `fix:`, `docs:`, `chore:`
- Reference issues when applicable
- Be descriptive about firmware changes

## Important Files to Understand

### Build System
- `build.py`: Main build orchestration
- `Makefile`: QMK build system entry point
- `users/holykeebs/rules.mk`: Conditional compilation rules

### Pointing Device Support
- `drivers/sensors/pimoroni_trackball.c`: Trackball driver
- `drivers/sensors/azoteq_iqs5xx.c`: Touchpad driver
- `users/holykeebs/*.c`: Pointing device integration

### Vial Integration
- `quantum/vial/`: Vial core implementation
- `keyboards/lily58/keymaps/via/`: Vial-enabled keymap
- `keyboards/lily58/keymaps/via/vial.json`: Vial configuration

## Working with GitHub Actions

### Workflows
- **build-firmware.yml**: Triggers on tags (`v*`), builds all firmware variants
- **pr-checks.yml**: Validates PRs with build tests and code quality checks
- **sync-upstreams.yml**: Syncs with upstream holykeebs repository

### Testing PRs Locally
Before pushing, ensure:
1. Firmware builds successfully
2. No debug code left in commits
3. Firmware size is reasonable (<1.5MB)
4. PR description is meaningful (>50 chars)

## Common Pitfalls

1. **Missing VIAL_ENABLE**: Always pass `VIAL_ENABLE=yes` when building vial keymap
2. **Memory overflow**: Watch firmware size, optimize features if needed
3. **Submodules**: Use `git clone --recurse-submodules` or `git submodule update --init`
4. **Build artifacts**: Don't commit `.uf2`, `.hex`, or build directory files
5. **QMK home**: CI sets `qmk config user.qmk_home=$GITHUB_WORKSPACE`

## Repository Relationships

- **Upstream holykeebs**: `github.com/idank/qmk_firmware` (branch: `holykeebs-master`)
- **Vial QMK**: `github.com/vial-kb/vial-qmk` (backported components)
- **Base QMK**: Old QMK version with holykeebs modifications

## Resources

- [Holykeebs Documentation](https://docs.holykeebs.com)
- [QMK Documentation](https://docs.qmk.fm)
- [Vial Documentation](https://get.vial.today/docs/)
- [RP2040 Datasheet](https://datasheets.raspberrypi.com/rp2040/rp2040-datasheet.pdf)

## Notes for Claude

- This is a specialized QMK fork with custom build system
- Not a standard QMK repository - don't assume standard QMK commands work
- Memory constraints are critical - always check firmware size
- Dual pointing device configurations are complex - refer to `build.py` matrix
- CI/CD is well-established - don't break existing workflows
- The community relies on pre-built firmware - ensure releases are stable
