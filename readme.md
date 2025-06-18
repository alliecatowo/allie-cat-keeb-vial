# 🐾 Allie Cat Keeb - Vial-Enabled QMK Firmware for Holykeebs

[![Current Version](https://img.shields.io/github/tag/alliecatowo/allie-cat-keeb.svg)](https://github.com/alliecatowo/allie-cat-keeb/tags)
[![Build Status](https://github.com/alliecatowo/allie-cat-keeb/actions/workflows/build.yml/badge.svg)](https://github.com/alliecatowo/allie-cat-keeb/actions)
[![Discord](https://img.shields.io/discord/440868230475677696.svg?label=QMK%20Discord)](https://discord.gg/qmk)
[![License](https://img.shields.io/badge/license-GPL2+-blue.svg)](https://github.com/alliecatowo/allie-cat-keeb/blob/main/LICENSE)

This repository is a **Vial-enabled fork** of the [holykeebs/qmk_firmware](https://github.com/idank/qmk_firmware) repository, bringing modern Vial support to holykeebs' amazing pointing device implementations for keyboards like the Lily58.

## 🛍️ Get Your Holykeebs Hardware

Visit the **[Holykeebs Store](https://holykeebs.com)** to purchase trackballs, touchpads, trackpoints, and other pointing device modules for your mechanical keyboard!

## 📚 Resources

- **[Holykeebs Documentation](https://docs.holykeebs.com)** - Complete guides for hardware installation and configuration
- **[Holykeebs Repository](https://github.com/idank/qmk_firmware)** - The original holykeebs QMK firmware (branch: `holykeebs-master`)
- **[Vial](https://get.vial.today)** - Real-time keyboard configuration without flashing
- **[Releases](https://github.com/alliecatowo/allie-cat-keeb/releases)** - Pre-built firmware with Vial support

## 🎯 Why This Fork Exists

The holykeebs QMK repository provides excellent support for various pointing devices (trackballs, touchpads, trackpoints) but is based on an older QMK version that lacks modern Vial support. This fork bridges that gap by:

1. **Backporting Vial Components** - We've carefully integrated Vial-QMK components into the holykeebs codebase
2. **Maintaining Compatibility** - All holykeebs pointing device drivers and features remain fully functional
3. **Enabling Real-time Configuration** - Use Vial to customize your keyboard without reflashing firmware
4. **Providing Pre-built Firmware** - Ready-to-use firmware files in our releases section

## 🚀 Key Features

- ✅ **Full Vial Support** - Configure your keyboard in real-time using the Vial GUI
- ✅ **Holykeebs Pointing Devices** - Complete support for:
  - Pimoroni Trackball with RGB
  - Azoteq IQS5xx TPS43 Touchpad
  - PS2 Trackpoint modules
  - Dual pointing device configurations
- ✅ **VIA Compatibility** - Works with both VIA and Vial configurators
- ✅ **Automated Builds** - GitHub Actions automatically build firmware for multiple configurations
- ✅ **Regular Updates** - Synced with upstream holykeebs changes

## 🔧 What We Changed

To enable Vial support on the holykeebs firmware, we made the following modifications:

### 1. **Vial Core Integration**
- Backported Vial's quantum layer modifications from [vial-qmk](https://github.com/vial-kb/vial-qmk)
- Added Vial-specific keycodes and configuration structures
- Integrated the Vial communication protocol

### 2. **Build System Updates**
- Modified the build system to support Vial's additional features
- Added Vial-specific build flags and configurations
- Created automated build scripts for common configurations

### 3. **Keymap Modifications**
- Updated VIA keymaps to include Vial's additional configuration options
- Added proper Vial keyboard definitions (`.vil` files)
- Maintained backward compatibility with existing VIA configurations

### 4. **Memory Optimizations**
- Optimized firmware size to accommodate Vial's additional features
- Carefully balanced features to fit within RP2040 constraints

## 📦 Pre-built Firmware

Don't want to build from source? No problem! Check our [Releases](https://github.com/alliecatowo/allie-cat-keeb/releases) page for pre-built firmware files.

Each release includes:
- **Standard builds** - Basic Vial-enabled firmware
- **Debug builds** - With console output for troubleshooting
- **Configuration variants** - Different pointing device combinations

### Firmware Naming Convention:
```
lily58_rev1_via_[configuration]_[side].uf2
```
- `configuration`: The pointing device setup (e.g., `trackball_tps43`)
- `side`: Either `left` or `right` for split keyboards

## 🛠️ Building Your Own Firmware

### Prerequisites

1. **Fork this repository** (not the base QMK or holykeebs repo)
2. Install QMK dependencies:
   ```bash
   # macOS
   brew install qmk/qmk/qmk
   
   # Linux/WSL
   sudo apt-get update
   sudo apt-get install -y git python3-pip
   pip3 install qmk
   qmk setup -y
   ```

### Quick Build

```bash
# Clone your fork
git clone --recurse-submodules https://github.com/YOUR_USERNAME/allie-cat-keeb.git
cd allie-cat-keeb

# Build firmware with our convenient build script
python build.py
```

### Build Options

The `build.py` script supports various configurations:

```bash
# Build specific configuration
python build.py --build-single \
  --keyboard lily58/rev1 \
  --keymap via \
  --left-device trackball \
  --right-device tps43

# Build all configurations
python build.py --build-all

# Build with Vial only (no debug)
python build.py --vial-only

# Build for release (all variants)
python build.py --release
```

### Manual Build Commands

For direct QMK commands:

```bash
# Dual pointing devices with Vial
make lily58/rev1:via -e USER_NAME=holykeebs \
  -e POINTING_DEVICE=trackball_tps43 \
  -e SIDE=left \
  -e TRACKBALL_RGB_RAINBOW=yes \
  -e VIAL_ENABLE=yes
```

## 🔄 Using GitHub Actions in Your Fork

When you fork this repository, you get automated firmware builds for free!

### Setting Up Actions:
1. Go to your fork's Settings → Actions
2. Enable GitHub Actions if not already enabled
3. The build workflow triggers on:
   - Pull requests to `main`
   - Tags matching `v*` pattern
   - Manual triggers via GitHub UI

### Creating a Release:
```bash
# Tag your version
git tag v1.0.0
git push origin v1.0.0
```

The workflow will automatically:
- Build all firmware variants
- Create a GitHub release
- Attach the firmware files

## 🤝 Contributing

We welcome contributions! Whether you want to:
- Add support for new pointing devices
- Improve Vial integration
- Fix bugs or optimize code
- Add new keyboard layouts

### How to Contribute:
1. Fork this repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to your branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Testing Your Changes:
- Build and test firmware locally first
- Include before/after comparisons for significant changes
- Document any new features or configurations

## 🎮 Getting Your Keyboard Working

### 1. Flash the Firmware
1. Download the appropriate `.uf2` file from [Releases](https://github.com/alliecatowo/allie-cat-keeb/releases)
2. Enter bootloader mode (double-tap RESET)
3. Copy the `.uf2` file to the `RPI-RP2` drive
4. Repeat for both halves (if split keyboard)

### 2. Configure with Vial
1. Download [Vial](https://get.vial.today)
2. Connect your keyboard
3. Customize everything in real-time:
   - Key mappings
   - Layers
   - Macros
   - Pointing device settings
   - RGB lighting

## 🚨 Troubleshooting

### Common Issues:

**"Vial doesn't detect my keyboard"**
- Ensure you flashed the Vial-enabled firmware (not base holykeebs)
- Try a different USB cable or port
- Check that both halves are flashed (for split keyboards)

**"Pointing device not working"**
- Verify the correct firmware variant for your hardware
- Check wiring connections (see [docs.holykeebs.com](https://docs.holykeebs.com))
- Try the debug firmware build for console output

**"Build fails"**
- Make sure you're building from this fork, not base QMK
- Run `qmk doctor` to check your environment
- Ensure submodules are initialized: `git submodule update --init`

## 📈 Project Status

This project is actively maintained and regularly synced with upstream holykeebs changes. We aim to:
- Keep Vial support up-to-date
- Maintain compatibility with all holykeebs hardware
- Provide timely firmware releases
- Support the community

## 🙏 Acknowledgments

- **[idank](https://github.com/idank)** - Creator of the holykeebs firmware and hardware
- **[Vial Contributors](https://github.com/vial-kb/vial-qmk)** - For the amazing real-time configuration system
- **[QMK Community](https://qmk.fm)** - For the incredible keyboard firmware framework
- **All Contributors** - Who help make this project better

## 📄 License

This firmware is based on QMK and includes modifications from holykeebs and Vial. Licensed under GPL-2.0+ with the same terms as QMK firmware.

---

<div align="center">
  
**[Get Hardware](https://holykeebs.com)** • **[Documentation](https://docs.holykeebs.com)** • **[Releases](https://github.com/alliecatowo/allie-cat-keeb/releases)** • **[Report Bug](https://github.com/alliecatowo/allie-cat-keeb/issues)**

Made with ❤️ for the mechanical keyboard community

</div>
