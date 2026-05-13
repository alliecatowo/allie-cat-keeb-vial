<div align="center">

# 🐾 Allie Cat Keeb — Vial-Enabled QMK Firmware

### _Holykeebs pointing devices + Vial real-time config, living together in harmony_ 🎹

[![Current Version](https://img.shields.io/github/tag/alliecatowo/allie-cat-keeb-vial.svg?label=version&color=ff69b4)](https://github.com/alliecatowo/allie-cat-keeb-vial/tags)
[![Build Status](https://github.com/alliecatowo/allie-cat-keeb-vial/actions/workflows/build-firmware.yml/badge.svg)](https://github.com/alliecatowo/allie-cat-keeb-vial/actions)
[![License](https://img.shields.io/badge/license-GPL2+-blue.svg)](https://github.com/alliecatowo/allie-cat-keeb-vial/blob/main/LICENSE)
[![Discord](https://img.shields.io/discord/440868230475677696.svg?label=QMK%20Discord&color=5865F2&logo=discord&logoColor=white)](https://discord.gg/qmk)

[![GitHub Stars](https://img.shields.io/github/stars/alliecatowo/allie-cat-keeb-vial?style=flat&color=yellow&logo=github)](https://github.com/alliecatowo/allie-cat-keeb-vial/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/alliecatowo/allie-cat-keeb-vial?style=flat&color=orange&logo=github)](https://github.com/alliecatowo/allie-cat-keeb-vial/network/members)
[![Open Issues](https://img.shields.io/github/issues/alliecatowo/allie-cat-keeb-vial?style=flat&color=red&logo=github)](https://github.com/alliecatowo/allie-cat-keeb-vial/issues)
[![Last Commit](https://img.shields.io/github/last-commit/alliecatowo/allie-cat-keeb-vial?style=flat&color=brightgreen&logo=git)](https://github.com/alliecatowo/allie-cat-keeb-vial/commits/main)
[![Contributors](https://img.shields.io/github/contributors/alliecatowo/allie-cat-keeb-vial?style=flat&color=blueviolet&logo=github)](https://github.com/alliecatowo/allie-cat-keeb-vial/graphs/contributors)

[![QMK](https://img.shields.io/badge/powered%20by-QMK-blue?logo=qmk&logoColor=white)](https://qmk.fm)
[![Vial](https://img.shields.io/badge/Vial-enabled-success?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMiAxNWwtNS01IDEuNDEtMS40MUwxMCAxNC4xN2w3LjU5LTcuNTlMMTkgOGwtOSA5eiIvPjwvc3ZnPg==)](https://get.vial.today)
[![Holykeebs](https://img.shields.io/badge/hardware-holykeebs-ff6b6b)](https://holykeebs.com)

</div>

---

This repository is a **Vial-enabled fork** of the [holykeebs/qmk_firmware](https://github.com/idank/qmk_firmware) repository, bringing modern Vial support to holykeebs' excellent pointing device implementations. Flash once, configure forever — no re-flashing needed when you change your layout.

## 📋 Table of Contents

- [🛍️ Get Hardware](#️-get-your-holykeebs-hardware)
- [🎯 Why This Fork Exists](#-why-this-fork-exists)
- [🚀 Key Features](#-key-features)
- [🎹 Supported Keyboards](#-supported-keyboards)
- [🖱️ Supported Pointing Devices](#️-supported-pointing-devices)
- [📚 Resources](#-resources)
- [🔧 What We Changed](#-what-we-changed)
- [📦 Pre-built Firmware](#-pre-built-firmware)
- [🛠️ Building Your Own Firmware](#️-building-your-own-firmware)
- [🤖 Codex Setup](#-codex-setup)
- [🔄 GitHub Actions in Your Fork](#-using-github-actions-in-your-fork)
- [🤝 Contributing](#-contributing)
- [🎮 Getting Your Keyboard Working](#-getting-your-keyboard-working)
- [🚨 Troubleshooting](#-troubleshooting)
- [📊 Driver Call Graph](#-driver-call-graph)
- [🙏 Acknowledgments](#-acknowledgments)
- [📄 License](#-license)

---

## 🛍️ Get Your Holykeebs Hardware

Visit the **[Holykeebs Store](https://holykeebs.com)** to purchase trackballs, touchpads, trackpoints, and other pointing device modules for your mechanical keyboard!

---

## 🎯 Why This Fork Exists

The holykeebs QMK repository provides excellent support for various pointing devices (trackballs, touchpads, trackpoints) but is based on an older QMK version that lacks modern Vial support. This fork bridges that gap by:

1. **Backporting Vial Components** — carefully integrating Vial-QMK components into the holykeebs codebase
2. **Maintaining Compatibility** — all holykeebs pointing device drivers and features remain fully functional
3. **Enabling Real-time Configuration** — use Vial to customize your keyboard without reflashing firmware
4. **Providing Pre-built Firmware** — ready-to-use firmware files in the releases section

---

## 🚀 Key Features

| Feature | Status |
|---|---|
| Full Vial real-time configuration | ✅ |
| VIA compatibility | ✅ |
| Pimoroni Trackball with RGB | ✅ |
| Azoteq IQS5xx TPS43 Touchpad | ✅ |
| PS2 Trackpoint modules | ✅ |
| Dual pointing device configurations | ✅ |
| Automated GitHub Actions builds | ✅ |
| Daily upstream sync (holykeebs + vial-qmk + QMK) | ✅ |

---

## 🎹 Supported Keyboards

| Keyboard | Type | MCU | Notes |
|---|---|---|---|
| **Lily58** `rev1` | 6×4+5 split | RP2040 | Primary build target; `via` and `vial` keymaps included |
| **Aztec42** | 42-key column-stagger split | RP2040 | Holykeebs variant |
| **SpanKBD** | Split | RP2040 | Holykeebs variant |
| **Sweeq** | 34-key sweep variant | RP2040 | Holykeebs variant |

> 💡 More keyboards may be added — check the [`keyboards/holykeebs/`](keyboards/holykeebs/) directory for the full list.

---

## 🖱️ Supported Pointing Devices

- 🔵 **Pimoroni Trackball** — with RGB underglow support
- 🟤 **Azoteq IQS5xx TPS43 Touchpad** — capacitive touchpad
- ⚪ **PS2 Trackpoint** — classic nub-style pointer
- ⚡ **Dual device configs** — mix and match (e.g. trackball left + touchpad right)

---

## 📚 Resources

- **[Holykeebs Documentation](https://docs.holykeebs.com)** — complete guides for hardware installation and configuration
- **[Holykeebs Repository](https://github.com/idank/qmk_firmware)** — the original holykeebs QMK firmware (`holykeebs-master` branch)
- **[Vial](https://get.vial.today)** — real-time keyboard configuration without flashing
- **[Releases](https://github.com/alliecatowo/allie-cat-keeb-vial/releases)** — pre-built firmware with Vial support
- **[QMK Docs](https://docs.qmk.fm)** — QMK firmware documentation

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
- Updated VIA keymaps to include Vial's additional configuration options
- Added proper Vial keyboard definitions (`.vil` files)
- Maintained backward compatibility with existing VIA configurations

### 4. Memory Optimizations
- Optimized firmware size to accommodate Vial's additional features
- Carefully balanced features to fit within RP2040 constraints

---

## 📦 Pre-built Firmware

Don't want to build from source? Check the [Releases](https://github.com/alliecatowo/allie-cat-keeb-vial/releases) page for pre-built firmware files.

Each release includes:
- **Standard builds** — basic Vial-enabled firmware
- **Debug builds** — with console output for troubleshooting
- **Configuration variants** — different pointing device combinations

### Firmware Naming Convention

```
lily58_rev1_via_[configuration]_[side].uf2
```

| Token | Description |
|---|---|
| `configuration` | pointing device setup, e.g. `trackball_tps43` |
| `side` | `left` or `right` for split keyboards |

---

## 🛠️ Building Your Own Firmware

### Prerequisites

1. **Fork this repository** (not the base QMK or holykeebs repo)
2. Install QMK dependencies:

```bash
# macOS
brew install qmk/qmk/qmk

# Linux / WSL
sudo apt-get update && sudo apt-get install -y git python3-pip
pip3 install qmk
qmk setup -y
```

### Quick Build

```bash
# Clone your fork
git clone --recurse-submodules https://github.com/YOUR_USERNAME/allie-cat-keeb-vial.git
cd allie-cat-keeb-vial

# Build firmware with our convenient build script
python build.py
```

### Build Options

```bash
# Build a specific configuration
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

### Manual QMK Commands

```bash
# Dual pointing devices with Vial
make lily58/rev1:via -e USER_NAME=holykeebs \
  -e POINTING_DEVICE=trackball_tps43 \
  -e SIDE=left \
  -e TRACKBALL_RGB_RAINBOW=yes \
  -e VIAL_ENABLE=yes
```

---

## 🤖 Codex Setup

Automating with Codex (or bootstrapping a fresh machine)? Follow [`docs/codex.md`](docs/codex.md) for a fast start:

```bash
# Install Python deps
python -m pip install -r requirements-dev.txt

# Bootstrap local CLI
export PATH="$PWD/bin:$PATH"
export ORIG_CWD="$PWD"
export PYTHONPATH="$PWD/lib/python"

# Quick validation
flake8 lib/python
python -m nose2 -v
```

---

## 🔄 Using GitHub Actions in Your Fork

When you fork this repository, you get automated firmware builds for free! Workflows run on:

| Trigger | What happens |
|---|---|
| Push to `main` | Quick tests & lint |
| PR opened/updated | PR checks + firmware build matrix |
| Tag matching `v*` | Full release build + GitHub release created |
| Daily schedule (2 AM UTC) | Upstream sync (holykeebs + vial-qmk + QMK) |
| Manual dispatch | Any workflow, on demand |

### Creating a Release

```bash
git tag v1.0.0
git push origin v1.0.0
```

The workflow automatically builds all variants, creates a GitHub release, and attaches the firmware files. 🎉

---

## 🤝 Contributing

We welcome contributions! Whether you want to add support for new pointing devices, improve Vial integration, fix bugs, or add new keyboard layouts — PRs are open.

```bash
# 1. Fork & clone
git clone https://github.com/YOUR_USERNAME/allie-cat-keeb-vial.git

# 2. Branch
git checkout -b feature/amazing-feature

# 3. Commit
git commit -m 'feat: add amazing feature'

# 4. Push & open a PR
git push origin feature/amazing-feature
```

> Before submitting: build locally, test on hardware, and document any new features or config options.

See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.

---

## 🎮 Getting Your Keyboard Working

### Step 1 — Flash the Firmware

1. Download the appropriate `.uf2` file from [Releases](https://github.com/alliecatowo/allie-cat-keeb-vial/releases)
2. Enter bootloader mode: **double-tap the RESET button**
3. Copy the `.uf2` file to the `RPI-RP2` drive that appears
4. Repeat for both halves (split keyboards)

### Step 2 — Configure with Vial

1. Download and open [Vial](https://get.vial.today)
2. Connect your keyboard via USB
3. Customize in real-time — no reflashing needed:
   - Key mappings & layers
   - Macros & tap-dance
   - Pointing device sensitivity & scrolling
   - RGB lighting effects

---

## 🚨 Troubleshooting

<details>
<summary><b>"Vial doesn't detect my keyboard"</b></summary>

- Ensure you flashed the **Vial-enabled** firmware (not base holykeebs)
- Try a different USB cable or port
- Check that **both halves** are flashed for split keyboards
</details>

<details>
<summary><b>"Pointing device not working"</b></summary>

- Verify the correct firmware variant matches your hardware (e.g. `trackball_tps43`)
- Check wiring connections at [docs.holykeebs.com](https://docs.holykeebs.com)
- Flash a **debug build** and open the Vial console for output
</details>

<details>
<summary><b>"Build fails"</b></summary>

- Make sure you're building from **this fork**, not base QMK
- Run `qmk doctor` to check your environment
- Initialize submodules: `git submodule update --init --recursive`
</details>

---

## 📊 Driver Call Graph

The Azoteq IQS5xx touchpad driver call graph is generated automatically during CI. View the latest below:

![Azoteq driver call graph](docs/azoteq_callgraph.svg)

---

## 🙏 Acknowledgments

- **[idank](https://github.com/idank)** — creator of the holykeebs firmware and hardware
- **[Vial Contributors](https://github.com/vial-kb/vial-qmk)** — for the amazing real-time configuration system
- **[QMK Community](https://qmk.fm)** — for the incredible keyboard firmware framework
- **All Contributors** — who help make this project better 🐾

---

## 📄 License

This firmware is based on QMK and includes modifications from holykeebs and Vial. Licensed under **GPL-2.0+** with the same terms as QMK firmware.

---

<div align="center">

**[🛒 Get Hardware](https://holykeebs.com)** • **[📖 Documentation](https://docs.holykeebs.com)** • **[📦 Releases](https://github.com/alliecatowo/allie-cat-keeb-vial/releases)** • **[🐛 Report a Bug](https://github.com/alliecatowo/allie-cat-keeb-vial/issues)**

<br/>

_Made with ❤️ and way too many keycaps for the mechanical keyboard community_ 🐾

</div>
