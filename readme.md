<div align="center">

# 🐾 Allie Cat Keeb — Vial-Enabled QMK Firmware

### Holykeebs pointing devices + Vial real-time config, living in perfect harmony.

[![Build Status](https://github.com/alliecatowo/allie-cat-keeb-vial/actions/workflows/build-firmware.yml/badge.svg)](https://github.com/alliecatowo/allie-cat-keeb-vial/actions/workflows/build-firmware.yml)
[![Latest Release](https://img.shields.io/github/v/release/alliecatowo/allie-cat-keeb-vial?label=latest%20release&color=brightgreen)](https://github.com/alliecatowo/allie-cat-keeb-vial/releases/latest)
[![GitHub Stars](https://img.shields.io/github/stars/alliecatowo/allie-cat-keeb-vial?style=flat&color=yellow)](https://github.com/alliecatowo/allie-cat-keeb-vial/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/alliecatowo/allie-cat-keeb-vial?style=flat&color=blue)](https://github.com/alliecatowo/allie-cat-keeb-vial/network/members)
[![Issues](https://img.shields.io/github/issues/alliecatowo/allie-cat-keeb-vial?color=orange)](https://github.com/alliecatowo/allie-cat-keeb-vial/issues)
[![Last Commit](https://img.shields.io/github/last-commit/alliecatowo/allie-cat-keeb-vial?color=purple)](https://github.com/alliecatowo/allie-cat-keeb-vial/commits/main)
[![License](https://img.shields.io/badge/license-GPL2+-blue.svg)](https://github.com/alliecatowo/allie-cat-keeb-vial/blob/main/LICENSE)
[![Discord](https://img.shields.io/discord/440868230475677696.svg?label=QMK%20Discord&color=5865F2)](https://discord.gg/qmk)

</div>

---

This repository is a **Vial-enabled fork** of the [holykeebs QMK firmware](https://github.com/idank/qmk_firmware), bringing modern Vial real-time configuration to holykeebs' excellent pointing device implementations — no more reflashing just to tweak a layer!

## 🛍️ Get Your Holykeebs Hardware

Visit the **[Holykeebs Store](https://holykeebs.com)** to get trackballs, touchpads, trackpoints, and other pointing device modules for your mechanical keyboard build.

## 📚 Resources

- **[Holykeebs Documentation](https://docs.holykeebs.com)** — Complete guides for hardware installation and configuration
- **[Holykeebs Repository](https://github.com/idank/qmk_firmware)** — The original holykeebs QMK firmware (branch: `holykeebs-master`)
- **[Vial](https://get.vial.today)** — Real-time keyboard configuration without flashing
- **[Releases](https://github.com/alliecatowo/allie-cat-keeb-vial/releases)** — Pre-built firmware with Vial support

---

## 🎯 Why This Fork Exists

The holykeebs QMK repo provides great pointing device support but targets an older QMK version without Vial. This fork bridges that gap:

| Feature | Upstream holykeebs | This fork |
|---|---|---|
| Pointing device drivers | ✅ | ✅ |
| VIA support | ✅ | ✅ |
| **Vial real-time config** | ❌ | ✅ |
| **Pre-built firmware releases** | ❌ | ✅ |
| **Automated CI builds** | ❌ | ✅ |

---

## 🎹 Supported Keyboards

| Keyboard | MCU | Pointing Devices | Vial |
|---|---|---|---|
| **Lily58** (rev1) | RP2040 | Trackball, TPS43 touchpad, trackpoint | ✅ |
| **Sofle** | RP2040 | Pointing device modules | ✅ |
| **Aztec42** *(holykeebs)* | RP2040 | Trackball, touchpad | ✅ |
| **Spankbd** *(holykeebs)* | RP2040 | Pointing device modules | ✅ |
| **Sweeq** *(holykeebs)* | RP2040 | Pointing device modules | ✅ |

---

## 🚀 Key Features

- ✅ **Full Vial Support** — Configure your keyboard in real-time using the Vial GUI
- ✅ **Holykeebs Pointing Devices** — Complete support for:
  - Pimoroni Trackball with RGB
  - Azoteq IQS5xx TPS43 Touchpad
  - PS2 Trackpoint modules
  - Dual pointing device configurations
- ✅ **VIA Compatibility** — Works with both VIA and Vial configurators
- ✅ **Automated Builds** — GitHub Actions build firmware for every tagged release
- ✅ **Pre-built Releases** — Ready-to-flash `.uf2` files so you don't have to compile

---

## 📦 Pre-built Firmware

Don't want to build from source? Grab a release! Head to the [Releases page](https://github.com/alliecatowo/allie-cat-keeb-vial/releases) for pre-built `.uf2` files.

Each release includes:
- **Standard builds** — Basic Vial-enabled firmware
- **Debug builds** — With console output for troubleshooting
- **Configuration variants** — Different pointing device combos

### Firmware Naming Convention

```
<keyboard>_via_[configuration]_[side].uf2
```

- `keyboard`: e.g. `lily58_rev1`, `sofle`, `holykeebs_aztec42`
- `configuration`: The pointing device setup (e.g. `trackball_tps43`)
- `side`: Either `left` or `right` for split keyboards

---

## 🛠️ Building From Source

### Prerequisites

1. **Fork this repository** (not the base QMK or holykeebs repo)
2. Install QMK dependencies:

```bash
# macOS
brew install qmk/qmk/qmk

# Linux / WSL
sudo apt-get update && sudo apt-get install -y git python3-pip
pip3 install qmk && qmk setup -y
```

### Quick Build

```bash
# Clone this repo
git clone --recurse-submodules https://github.com/alliecatowo/allie-cat-keeb-vial.git
cd allie-cat-keeb-vial

# Build firmware with our build script
python build.py
```

### Build Options

```bash
# Build a specific config
python build.py --build-single \
  --keyboard lily58/rev1 \
  --keymap via \
  --left-device trackball \
  --right-device tps43

# Build everything
python build.py --build-all

# Vial only (no debug)
python build.py --vial-only

# Full release (all variants)
python build.py --release
```

### Manual QMK Commands

```bash
# Dual pointing devices with Vial
make lily58/rev1:via -e USER_NAME=holykeebs \
  -e LEFT_POINTING_DEVICE=TRACKBALL \
  -e RIGHT_POINTING_DEVICE=TPS43 \
  -e VIAL_ENABLE=yes
```

---

## 🔧 What We Changed

### 1. Vial Core Integration
- Backported Vial's quantum layer modifications from [vial-qmk](https://github.com/vial-kb/vial-qmk)
- Added Vial-specific keycodes and configuration structures
- Integrated the Vial communication protocol

### 2. Build System Updates
- Modified the build system to support Vial's additional features
- Added Vial-specific build flags and configurations
- Created automated build scripts for common configurations

### 3. Keymap Modifications
- Updated VIA keymaps to include Vial's additional config options
- Added proper Vial keyboard definitions (`.vil` files)
- Maintained backward compatibility with existing VIA configurations

### 4. Memory Optimizations
- Optimized firmware size to accommodate Vial's additional features
- Carefully balanced features to fit within RP2040 constraints

---

## 🎮 Getting Your Keyboard Working

### 1. Flash the Firmware

1. Download the right `.uf2` from [Releases](https://github.com/alliecatowo/allie-cat-keeb-vial/releases)
2. Enter bootloader mode (double-tap RESET)
3. Copy the `.uf2` to the `RPI-RP2` drive
4. Repeat for both halves (split keyboards)

### 2. Configure with Vial

1. Download [Vial](https://get.vial.today)
2. Connect your keyboard
3. Customize in real-time:
   - Key mappings & layers
   - Macros & tap-dance
   - Pointing device settings
   - RGB lighting

---

## 🔄 GitHub Actions in Your Fork

Fork this repo and get automated CI builds for free!

### Setup
1. Go to your fork's **Settings → Actions** and enable GitHub Actions
2. The build workflow triggers on:
   - Tags matching `v*`
   - Manual dispatch via the GitHub UI

### Create a Release

```bash
git tag v1.0.0
git push origin v1.0.0
```

The workflow will automatically build all variants, create a GitHub release, and attach firmware files.

---

## 🤖 Codex / Automation Setup

Bootstrapping a fresh machine or running in Codex? See [`docs/codex.md`](docs/codex.md) for a fast start:

```bash
# Install Python deps
python -m pip install -r requirements-dev.txt

# Set up environment
export ORIG_CWD="$PWD"
export QMK_HOME="$PWD"
export QMK_FIRMWARE="$PWD"
export PYTHONPATH="$PWD/lib/python"
export PATH="$PWD/bin:$PATH"

# Quick validation
flake8 lib/python
python -m nose2 -v
```

---

## 📊 Driver Call Graph

The Azoteq IQS5xx touchpad driver call graph is auto-generated during CI:

![Azoteq driver call graph](docs/azoteq_callgraph.svg)

---

## 🚨 Troubleshooting

**"Vial doesn't detect my keyboard"**
- Ensure you flashed the Vial-enabled firmware (not base holykeebs)
- Try a different USB cable or port
- Check both halves are flashed (split keyboards)

**"Pointing device not working"**
- Verify you have the correct firmware variant for your hardware
- Check wiring (see [docs.holykeebs.com](https://docs.holykeebs.com))
- Try the debug firmware build for console output

**"Build fails"**
- Build from this fork, not base QMK
- Run `qmk doctor` to check your environment
- Ensure submodules are initialized: `git submodule update --init`

---

## 🤝 Contributing

Contributions are welcome! Whether you want to add pointing device support, improve Vial integration, fix bugs, or add new keyboard layouts:

1. Fork this repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to your branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please build and test firmware locally first, and document any new features.

---

## 🙏 Acknowledgments

- **[idank](https://github.com/idank)** — Creator of the holykeebs firmware and hardware
- **[Vial Contributors](https://github.com/vial-kb/vial-qmk)** — For the amazing real-time config system
- **[QMK Community](https://qmk.fm)** — For the incredible keyboard firmware framework
- **All contributors** who help make this project better

---

## 📄 License

Based on QMK firmware and holykeebs modifications. Licensed under **GPL-2.0+** per QMK's terms.

---

<div align="center">

**[🛍️ Get Hardware](https://holykeebs.com)** • **[📚 Documentation](https://docs.holykeebs.com)** • **[📦 Releases](https://github.com/alliecatowo/allie-cat-keeb-vial/releases)** • **[🐛 Report Bug](https://github.com/alliecatowo/allie-cat-keeb-vial/issues)**

Made with ❤️ for the mechanical keyboard community 🐾

</div>
