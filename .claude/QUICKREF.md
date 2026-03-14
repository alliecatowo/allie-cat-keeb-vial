# Quick Reference Guide

## Quick Start

```bash
# Build default firmware (trackball_tps43)
python build.py

# Build custom configuration
python build.py --build-single \
  --keyboard lily58/rev1 \
  --keymap vial \
  --left-device trackball \
  --right-device tps43 \
  --side left

# Clean build artifacts
rm -rf build_lily58/ .build/ *.uf2
```

## Available Slash Commands

- `/build` - Build default firmware configuration
- `/build-custom` - Build with custom device selection
- `/check` - Run comprehensive repository checks
- `/clean` - Clean build artifacts
- `/build-info` - Show build system information
- `/info` - Show repository structure overview
- `/test` - Run QMK test suite
- `/release` - Prepare a new release
- `/setup-env` - Set up development environment

## Pointing Device Options

### Single Device
- `trackball` - Pimoroni trackball with RGB
- `tps43` - Azoteq IQS5xx TPS43 touchpad
- `trackpoint` - PS2 trackpoint module
- `oled` - OLED display only
- `None` - No device

### Dual Device Combinations
- `trackball_tps43` - Trackball on left, touchpad on right
- `trackball_trackpoint` - Trackball on left, trackpoint on right
- `tps43_trackball` - Touchpad on left, trackball on right
- And more combinations...

## Build Variables

```bash
# Essential
USER_NAME=holykeebs           # Holykeebs userspace
POINTING_DEVICE=<config>      # Device configuration
SIDE=left|right               # For dual device configs
VIAL_ENABLE=yes              # Enable Vial (required for vial keymap)

# Optional
TRACKBALL_RGB_RAINBOW=yes    # Enable trackball RGB effects
CONSOLE=yes                  # Enable debug console
OLED=yes                     # Enable OLED support
OLED_FLIP=yes               # Flip OLED orientation
```

## File Locations

### Source Code
- `keyboards/lily58/` - Lily58 keyboard files
- `users/holykeebs/` - Holykeebs userspace
- `drivers/sensors/` - Pointing device drivers
- `quantum/vial/` - Vial integration

### Configuration
- `keyboards/lily58/rev1/config.h` - Hardware config
- `keyboards/lily58/keymaps/via/` - Vial keymap
- `users/holykeebs/rules.mk` - Build rules

### Build System
- `build.py` - Main build script
- `Makefile` - QMK build system
- `paths.mk` - Path definitions

### Documentation
- `README.md` - Main documentation
- `CONTRIBUTING.md` - Contribution guide
- `docs/` - Additional documentation
- `.claude/` - Claude Code configuration

## Firmware Size Optimization

If firmware is too large (>1.5MB):

1. Disable console: `CONSOLE=no`
2. Reduce dynamic keymap layers
3. Disable RGB matrix effects
4. Enable LTO: `LTO_ENABLE=yes`
5. Remove unused features

Target sizes:
- Minimal: 600-800KB
- Standard: 900KB-1.2MB
- Full featured: 1.5MB+

## Common Issues

### Build Errors
- **"VIAL_ENABLE not set"**: Add `VIAL_ENABLE=yes` to make command
- **"undefined reference"**: Check pointing device is set correctly
- **"region FLASH overflowed"**: Firmware too large, optimize features
- **Missing submodules**: Run `git submodule update --init --recursive`

### Environment Issues
- **QMK not found**: Install with `pip3 install qmk`
- **ARM GCC missing**: Install `gcc-arm-none-eabi`
- **Python dependencies**: `pip3 install -r requirements.txt`

## Git Workflow

```bash
# Create feature branch
git checkout -b feat/your-feature

# Make changes and commit
git add .
git commit -m "feat: description"

# Push and create PR
git push origin feat/your-feature
```

## CI/CD

### Workflows
- **build-firmware.yml**: Triggered by tags (`v*`)
- **pr-checks.yml**: Validates PRs
- **sync-upstreams.yml**: Syncs with upstream repos

### Creating a Release
```bash
git tag v1.2.3
git push origin v1.2.3
# GitHub Actions builds and releases automatically
```

## Testing

```bash
# Run basic tests
make test:basic

# Run all tests
make test:all

# Test specific feature
make test:pointing

# Python linting
flake8 build.py

# Python formatting
yapf -d build.py
```

## Useful Commands

```bash
# Check firmware size
ls -lh build_lily58/*.uf2

# View build matrix
python build.py --generate-matrix-release

# Configure QMK
qmk config user.qmk_home=$PWD

# Check for debug code
grep -r "TODO\|FIXME\|console.log" --include="*.c" --include="*.h" .

# List recent commits
git log --oneline -10

# Check repository status
git status

# View git diff
git diff
```

## Memory Map (RP2040)

```
0x00000000 - 0x001FFFFF (2MB Flash)
├── 0x00000000 - Bootloader
├── 0x00004000 - Firmware start
└── 0x001FFFFF - Flash end

Warning: Keep firmware under 1.5MB
Critical: Must fit in 2MB with bootloader
```

## Resources

- **Holykeebs**: https://holykeebs.com
- **Holykeebs Docs**: https://docs.holykeebs.com
- **Vial**: https://get.vial.today
- **QMK Docs**: https://docs.qmk.fm
- **RP2040**: https://datasheets.raspberrypi.com/rp2040/

## Support

- GitHub Issues: Report bugs and request features
- QMK Discord: #firmware-help channel
- Holykeebs: Hardware support

## Emergency Fixes

### Firmware Won't Build
1. Clean everything: `rm -rf .build/ build_lily58/ *.uf2`
2. Update submodules: `git submodule update --init --recursive`
3. Reinstall dependencies: `pip3 install -r requirements.txt`
4. Try minimal build: Remove optional features

### Firmware Won't Flash
1. Enter bootloader: Double-tap RESET
2. Check USB cable and port
3. Verify `.uf2` file isn't corrupted
4. Try different computer if needed

### Keyboard Not Working
1. Check both halves are flashed (split keyboard)
2. Verify correct side flashed (left vs right)
3. Check TRRS cable connection
4. Try debug firmware for console output
5. Verify Vial GUI detects keyboard

## Development Tips

- Start with small, focused changes
- Test incrementally
- Check firmware size after each feature
- Use debug builds during development
- Flash release builds for production
- Document complex changes
- Ask for help when stuck
