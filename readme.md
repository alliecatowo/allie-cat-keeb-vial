<div align="center">

# 🐾 Allie Cat Keeb — Vial-Enabled QMK Firmware

*Holykeebs firmware with real-time Vial configuration for split keyboards with pointing devices*

<!-- Build & Release -->
[![Build Firmware](https://github.com/alliecatowo/allie-cat-keeb-vial/actions/workflows/build-firmware.yml/badge.svg)](https://github.com/alliecatowo/allie-cat-keeb-vial/actions/workflows/build-firmware.yml)
[![Latest Release](https://img.shields.io/github/v/release/alliecatowo/allie-cat-keeb-vial?include_prereleases&label=latest%20release&color=brightgreen)](https://github.com/alliecatowo/allie-cat-keeb-vial/releases)
[![License](https://img.shields.io/badge/license-GPL--2.0%2B-blue)](https://github.com/alliecatowo/allie-cat-keeb-vial/blob/main/LICENSE)

<!-- Repo Stats -->
[![GitHub Stars](https://img.shields.io/github/stars/alliecatowo/allie-cat-keeb-vial?style=flat&color=yellow)](https://github.com/alliecatowo/allie-cat-keeb-vial/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/alliecatowo/allie-cat-keeb-vial?style=flat&color=orange)](https://github.com/alliecatowo/allie-cat-keeb-vial/network/members)
[![Last Commit](https://img.shields.io/github/last-commit/alliecatowo/allie-cat-keeb-vial?color=8b5cf6)](https://github.com/alliecatowo/allie-cat-keeb-vial/commits/main)
[![Open Issues](https://img.shields.io/github/issues/alliecatowo/allie-cat-keeb-vial)](https://github.com/alliecatowo/allie-cat-keeb-vial/issues)

<!-- Community & Stack -->
[![Powered by QMK](https://img.shields.io/badge/Powered%20by-QMK-eb0000?logo=qmk&logoColor=white)](https://qmk.fm)
[![Vial Enabled](https://img.shields.io/badge/Vial-enabled-7c3aed?logoColor=white)](https://get.vial.today)
[![Discord](https://img.shields.io/discord/440868230475677696?label=QMK%20Discord&logo=discord&logoColor=white&color=5865F2)](https://discord.gg/qmk)

---

**[📦 Releases](https://github.com/alliecatowo/allie-cat-keeb-vial/releases)** · **[🛍️ Get Hardware](https://holykeebs.com)** · **[📚 Docs](https://docs.holykeebs.com)** · **[🐛 Report Bug](https://github.com/alliecatowo/allie-cat-keeb-vial/issues)**

</div>

---

A **Vial-enabled fork** of [holykeebs/qmk_firmware](https://github.com/idank/qmk_firmware), bringing real-time keyboard configuration to holykeebs' excellent pointing device ecosystem — trackballs, touchpads, trackpoints, and more. 🐱⌨️

## 📋 Table of Contents

- [Why This Fork](#-why-this-fork-exists)
- [Supported Keyboards](#-supported-keyboards)
- [Key Features](#-key-features)
- [Pre-built Firmware](#-pre-built-firmware)
- [Building Your Own Firmware](#-building-your-own-firmware)
- [Getting Your Keyboard Working](#-getting-your-keyboard-working)
- [GitHub Actions](#-using-github-actions-in-your-fork)
- [Contributing](#-contributing)
- [Troubleshooting](#-troubleshooting)
- [Acknowledgments](#-acknowledgments)

---

## 🎯 Why This Fork Exists

The holykeebs QMK repository provides excellent support for various pointing devices (trackballs, touchpads, trackpoints) but is based on an older QMK version that lacks modern Vial support. This fork bridges that gap by:

1. **Backporting Vial Components** — Carefully integrated Vial-QMK components into the holykeebs codebase
2. **Maintaining Compatibility** — All holykeebs pointing device drivers and features remain fully functional
3. **Enabling Real-time Configuration** — Use Vial to customize your keyboard without reflashing firmware
4. **Providing Pre-built Firmware** — Ready-to-use firmware files in the [Releases](https://github.com/alliecatowo/allie-cat-keeb-vial/releases) section

## ⌨️ Supported Keyboards

All keyboards below are available from the **[Holykeebs Store](https://holykeebs.com)**:

| Keyboard | Layout | MCU | Notes |
|----------|--------|-----|-------|
| **Lily58** | 6×4+5 split | RP2040 | Multiple rev builds; primary supported board |
| **Aztec42** | 4×5+2 split | RP2040 | Compact columnar stagger with pointing device |
| **Spankbd** (Span) | 3×5+3 split | RP2040 | GergoPlex-derived layout; trackball-friendly |
| **Sweeq** | 3×5+2 split | RP2040 | Ultra-compact with Vial keymap support |

## 🚀 Key Features

- ✅ **Full Vial Support** — Configure your keyboard in real-time using the Vial GUI
- ✅ **Holykeebs Pointing Devices** — Complete support for:
  - Pimoroni Trackball with RGB
  - Azoteq IQS5xx TPS43 Touchpad
  - PS2 Trackpoint modules
  - Dual pointing device configurations
- ✅ **VIA Compatibility** — Works with both VIA and Vial configurators
- ✅ **Automated Builds** — GitHub Actions automatically build firmware for multiple configurations
- ✅ **Regular Updates** — Synced with upstream holykeebs changes via automated sync workflow

## 📦 Pre-built Firmware

Don't want to build from source? Download pre-built firmware straight from our **[Releases](https://github.com/alliecatowo/allie-cat-keeb-vial/releases)** page!

Each release includes:
- **Standard builds** — Vial-enabled firmware ready to flash
- **Debug builds** — Console output enabled for troubleshooting
- **Configuration variants** — Different pointing device combinations

### Firmware Naming Convention

```
lily58_rev1_vial_[configuration]_[side].uf2
```

| Part | Description |
|------|-------------|
| `configuration` | Pointing device setup (e.g. `trackball_tps43`) |
| `side` | `left` or `right` for split keyboards |

## 🛠️ Building Your Own Firmware

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
# Clone your fork (with submodules)
git clone --recurse-submodules https://github.com/YOUR_USERNAME/allie-cat-keeb-vial.git
cd allie-cat-keeb-vial

# Install Python deps
python3 -m pip install -r requirements-dev.txt

# Build default config
python3 build.py
```

### Build Options

The `build.py` script supports a variety of configurations:

```bash
# Build a single variant
python3 build.py --build-single \
  --keyboard lily58/rev1 \
  --keymap vial \
  --left-device trackball \
  --right-device tps43 \
  --side left

# Build all configurations
python3 build.py --build-all

# Build for release (all variants)
python3 build.py --release

# Generate CI build matrix (JSON)
python3 build.py --generate-matrix-release
```

### Manual Build Command

```bash
make lily58/rev1:via \
  -e USER_NAME=holykeebs \
  -e POINTING_DEVICE=trackball_tps43 \
  -e SIDE=left \
  -e TRACKBALL_RGB_RAINBOW=yes \
  -e VIAL_ENABLE=yes
```

### Agent / Codex Setup

Bootstrapping a fresh machine or automating with an AI coding agent? Set these env vars first:

```bash
export ORIG_CWD="$PWD"
export QMK_HOME="$PWD"
export QMK_FIRMWARE="$PWD"
export PYTHONPATH="$PWD/lib/python"
export PATH="$PWD/bin:$PATH"
```

Then run quick validation (no ARM toolchain required):

```bash
python3 -m unittest tests.test_build_py -v   # unit tests
python3 build.py --generate-matrix-release    # validate CI matrix
flake8 build.py tools/callgraph.py tests/test_build_py.py --max-line-length=120
```

See [`docs/codex.md`](docs/codex.md) for the full bootstrap guide.

## 🎮 Getting Your Keyboard Working

### 1. Flash the Firmware

1. Download the appropriate `.uf2` file from [Releases](https://github.com/alliecatowo/allie-cat-keeb-vial/releases)
2. Enter bootloader mode (double-tap the RESET button)
3. Drag-and-drop the `.uf2` file onto the `RPI-RP2` drive that appears
4. Repeat for both halves of a split keyboard

### 2. Configure with Vial

1. Download [Vial](https://get.vial.today)
2. Connect your keyboard via USB
3. Customize everything in real-time:
   - Key mappings & layers
   - Macros & tap-dance
   - Pointing device sensitivity & scroll settings
   - RGB lighting effects

## 🔄 Using GitHub Actions in Your Fork

When you fork this repository you get automated firmware builds for free!

### Enabling Actions

1. Go to your fork → **Settings → Actions**
2. Enable GitHub Actions (if not already on)
3. The build workflow triggers on:
   - Tags matching `v*`
   - Manual triggers via the **Actions** tab

### Creating a Release

```bash
git tag v1.0.0
git push origin v1.0.0
```

The workflow will automatically:
- Build all firmware variants in parallel
- Create a GitHub Release
- Attach all `.uf2` firmware files

## 📊 Driver Call Graph

The Azoteq IQS5xx touchpad driver call graph is auto-generated by CI and committed to the repo:

![Azoteq driver call graph](docs/azoteq_callgraph.svg)

## 🤝 Contributing

Contributions are welcome! Whether you want to add support for a new pointing device, improve Vial integration, fix bugs, or add keyboard layouts — open a PR!

1. Fork this repository
2. Create a feature branch: `git checkout -b feat/my-cool-feature`
3. Commit with [conventional commits](https://www.conventionalcommits.org/): `git commit -m "feat: add amazing feature"`
4. Push and open a Pull Request

Please run the quick checks before submitting:

```bash
python3 -m unittest tests.test_build_py -v
flake8 build.py tools/callgraph.py tests/test_build_py.py --max-line-length=120
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for full details.

## 🚨 Troubleshooting

**"Vial doesn't detect my keyboard"**
→ Make sure you flashed the Vial-enabled firmware (not base holykeebs).  
→ Try a different USB cable or port.  
→ Both halves of a split keyboard must be flashed.

**"Pointing device not working"**
→ Verify you flashed the correct firmware variant for your hardware combination.  
→ Check wiring with [docs.holykeebs.com](https://docs.holykeebs.com).  
→ Try a debug build and open the Vial console for log output.

**"Build fails"**
→ Make sure you're building from **this fork**, not base QMK or holykeebs.  
→ Run `qmk doctor` to check your environment.  
→ Ensure submodules are initialized: `git submodule update --init --recursive`

## 📈 Project Status

This project is actively maintained and regularly synced with upstream holykeebs changes via the automated [`sync-upstreams`](.github/workflows/sync-upstreams.yml) workflow. Goals:

- Keep Vial support up-to-date with upstream Vial-QMK
- Maintain compatibility with all holykeebs hardware
- Provide timely firmware releases
- Support the split-keyboard community 🐱

## 🙏 Acknowledgments

- **[idank](https://github.com/idank)** — Creator of the holykeebs firmware and hardware
- **[Vial Contributors](https://github.com/vial-kb/vial-qmk)** — For the incredible real-time configuration system
- **[QMK Community](https://qmk.fm)** — For the amazing keyboard firmware framework
- **All Contributors** — Who help make this project better ✨

## 📄 License

This firmware is based on QMK and includes modifications from holykeebs and Vial. Licensed under **GPL-2.0+** — the same terms as QMK firmware.

---

<div align="center">

**[📦 Releases](https://github.com/alliecatowo/allie-cat-keeb-vial/releases)** · **[🛍️ Get Hardware](https://holykeebs.com)** · **[📚 Docs](https://docs.holykeebs.com)** · **[🐛 Report Bug](https://github.com/alliecatowo/allie-cat-keeb-vial/issues)**

Made with ❤️ for the mechanical keyboard community 🐾

</div>
