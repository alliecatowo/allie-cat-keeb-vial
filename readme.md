<div align="center">

```
 ██████╗ █████╗ ████████╗    ██╗  ██╗███████╗███████╗██████╗
██╔════╝██╔══██╗╚══██╔══╝    ██║ ██╔╝██╔════╝██╔════╝██╔══██╗
██║     ███████║   ██║       █████╔╝ █████╗  █████╗  ██████╔╝
██║     ██╔══██║   ██║       ██╔═██╗ ██╔══╝  ██╔══╝  ██╔══██╗
╚██████╗██║  ██║   ██║       ██║  ██╗███████╗███████╗██████╔╝
 ╚═════╝╚═╝  ╚═╝   ╚═╝       ╚═╝  ╚═╝╚══════╝╚══════╝╚═════╝
```

# 🐾 Allie Cat Keeb — Vial-Enabled QMK for Holykeebs

*Bringing modern real-time configurability to holykeebs pointing-device keyboards*

[![Build Status](https://github.com/alliecatowo/allie-cat-keeb-vial/actions/workflows/build-firmware.yml/badge.svg)](https://github.com/alliecatowo/allie-cat-keeb-vial/actions)
[![GitHub Release](https://img.shields.io/github/v/release/alliecatowo/allie-cat-keeb-vial?include_prereleases&label=latest)](https://github.com/alliecatowo/allie-cat-keeb-vial/releases)
[![GitHub Stars](https://img.shields.io/github/stars/alliecatowo/allie-cat-keeb-vial?style=flat&color=yellow)](https://github.com/alliecatowo/allie-cat-keeb-vial/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/alliecatowo/allie-cat-keeb-vial?style=flat)](https://github.com/alliecatowo/allie-cat-keeb-vial/network/members)
[![GitHub Issues](https://img.shields.io/github/issues/alliecatowo/allie-cat-keeb-vial)](https://github.com/alliecatowo/allie-cat-keeb-vial/issues)
[![Last Commit](https://img.shields.io/github/last-commit/alliecatowo/allie-cat-keeb-vial)](https://github.com/alliecatowo/allie-cat-keeb-vial/commits/main)
[![Discord](https://img.shields.io/discord/440868230475677696.svg?label=QMK%20Discord&color=5865F2&logo=discord&logoColor=white)](https://discord.gg/qmk)
[![License](https://img.shields.io/badge/license-GPL--2.0%2B-blue.svg?logo=gnu)](https://github.com/alliecatowo/allie-cat-keeb-vial/blob/main/LICENSE)

---

**[📦 Releases](https://github.com/alliecatowo/allie-cat-keeb-vial/releases)** • **[🛍️ Get Hardware](https://holykeebs.com)** • **[📖 Docs](https://docs.holykeebs.com)** • **[🐛 Report Bug](https://github.com/alliecatowo/allie-cat-keeb-vial/issues)**

</div>

---

## 📖 Table of Contents

- [What Is This?](#-what-is-this)
- [Supported Keyboards](#-supported-keyboards)
- [Key Features](#-key-features)
- [Getting Started — Flash Pre-built Firmware](#-getting-started--flash-pre-built-firmware)
- [Configure with Vial](#-configure-with-vial)
- [Build From Source](#-build-from-source)
- [GitHub Actions in Your Fork](#-github-actions-in-your-fork)
- [What We Changed](#-what-we-changed)
- [Troubleshooting](#-troubleshooting)
- [Driver Call Graph](#-driver-call-graph)
- [Contributing](#-contributing)
- [Acknowledgments](#-acknowledgments)
- [License](#-license)

---

## 🐱 What Is This?

This repository is a **Vial-enabled fork** of the [holykeebs/qmk_firmware](https://github.com/idank/qmk_firmware) repository. The upstream holykeebs repo is an older QMK version that offers stellar pointing-device support (trackballs, touchpads, trackpoints) but lacks modern [Vial](https://get.vial.today) integration.

This fork bridges that gap:

| Upstream holykeebs | **This fork (allie-cat-keeb-vial)** |
|---|---|
| Excellent pointing-device drivers | ✅ All drivers kept intact |
| No Vial support | ✅ Full Vial real-time config |
| No automated builds | ✅ GitHub Actions CI for `.uf2` artifacts |
| Older QMK base | ✅ Backported Vial-QMK components |

---

## 🎹 Supported Keyboards

| Keyboard | Layout | Pointing Device Support |
|---|---|---|
| **Lily58** `rev1` | 58-key split | Trackball, TPS43 touchpad, trackpoint, dual combos |
| **Sofle** `rev1` | 58-key split | Pointing device variants |
| **Holykeebs Sweeq** | Sweep-style | Trackball |
| **Holykeebs Aztec42** | 42-key | Trackball |
| **Holykeebs SpanKBD** | Custom | Trackball |

> **Note:** Pre-built firmware in [Releases](https://github.com/alliecatowo/allie-cat-keeb-vial/releases) covers the most popular `lily58/rev1` configurations. Other keyboards can be built from source.

---

## 🚀 Key Features

| Feature | Details |
|---|---|
| 🔴 **Full Vial Support** | Configure keys, layers, macros, and RGB in real-time — no reflashing |
| 🖱️ **Holykeebs Pointing Devices** | Pimoroni Trackball (RGB), Azoteq IQS5xx TPS43 Touchpad, PS2 Trackpoint, dual-device configs |
| ⚡ **VIA + Vial Compatibility** | Works with both VIA and Vial configurators |
| 🤖 **Automated CI Builds** | GitHub Actions builds `.uf2` firmware on every tagged release |
| 🔄 **Regular Upstream Sync** | Auto-merges from holykeebs and vial-qmk when CI is green |
| 📊 **Driver Call Graph** | Azoteq IQS5xx call graph generated automatically in CI |

---

## 📦 Getting Started — Flash Pre-built Firmware

No build environment needed — just grab a `.uf2` from Releases!

1. **Download** the right `.uf2` from [Releases](https://github.com/alliecatowo/allie-cat-keeb-vial/releases):

   ```
   lily58_rev1_vial_<pointing_config>_<side>.uf2
   ```

   | Part | Meaning |
   |---|---|
   | `pointing_config` | e.g. `trackball_tps43` |
   | `side` | `left` or `right` |

2. **Enter bootloader** — double-tap the RESET button on your controller; a `RPI-RP2` drive appears.
3. **Copy the `.uf2`** onto the drive — it flashes and reboots automatically.
4. **Repeat for the other half** of your split keyboard.

---

## 🎛️ Configure with Vial

Once flashed, open [Vial](https://get.vial.today) and start customising in real-time:

- 🗺️ Key mappings & layers
- ⌨️ Macros & tap-dance
- 🖱️ Pointing device sensitivity & scroll speed
- 🌈 RGB lighting & effects

No reflashing needed — all changes apply instantly over USB.

---

## 🛠️ Build From Source

### Prerequisites

```bash
# macOS
brew install qmk/qmk/qmk

# Linux / WSL
sudo apt-get update && sudo apt-get install -y git python3-pip
pip3 install qmk
qmk setup -y
```

### Clone & Quick Build

```bash
# Clone THIS fork (not base QMK or holykeebs)
git clone --recurse-submodules https://github.com/alliecatowo/allie-cat-keeb-vial.git
cd allie-cat-keeb-vial

# Install Python helpers
pip install -r requirements-dev.txt

# Build the default trackball + TPS43 Vial firmware
python build.py
```

### build.py Options

```bash
# Build a specific single configuration
python build.py --build-single \
  --keyboard lily58/rev1 \
  --keymap vial \
  --left-device trackball \
  --right-device tps43

# Build all supported configurations
python build.py --build-all

# Build for release (all variants, optimised)
python build.py --release
```

### Manual QMK Command

```bash
make lily58/rev1:vial \
  -e USER_NAME=holykeebs \
  -e POINTING_DEVICE=trackball_tps43 \
  -e SIDE=left \
  -e TRACKBALL_RGB_RAINBOW=yes \
  -e VIAL_ENABLE=yes \
  -j8
```

### Codex / Copilot Setup

See `docs/codex.md` for a fast machine-bootstrap. Quick summary:

```bash
python -m pip install -r requirements-dev.txt
export PATH="$PWD/bin:$PATH"
export ORIG_CWD="$PWD"
export PYTHONPATH="$PWD/lib/python"

# Quick validation
flake8 lib/python
python -m nose2 -v
```

---

## 🤖 GitHub Actions in Your Fork

Fork this repo and you get automated firmware builds for free!

### Setup

1. Go to **Settings → Actions** in your fork and enable GitHub Actions.
2. The build workflow triggers on:
   - Tags matching `v*` (creates a Release with `.uf2` attachments)
   - `workflow_dispatch` (manual run from the Actions tab)

### Creating a Release

```bash
git tag v1.2.0
git push origin v1.2.0
```

The workflow will:
- Build all configured firmware variants in parallel
- Create a GitHub Release
- Attach all `.uf2` files automatically

---

## 🔧 What We Changed

<details>
<summary>Click to expand technical details</summary>

### 1. Vial Core Integration
- Backported Vial's quantum-layer modifications from [vial-qmk](https://github.com/vial-kb/vial-qmk)
- Added Vial-specific keycodes, configuration structures, and the Vial USB communication protocol

### 2. Build System Updates
- Modified the build system to support Vial's extra features and flags
- Added `build.py` — a convenient wrapper for common configurations and CI matrix generation

### 3. Keymap Modifications
- Updated keymaps to expose Vial's extended configuration surface
- Added proper Vial keyboard definition (`.vil`) files
- Maintained backward compatibility with existing VIA configurations

### 4. Memory Optimisations
- Carefully balanced features to keep firmware within RP2040 flash constraints while including Vial overhead

### 5. CI / Automation
- GitHub Actions workflow for matrix builds, releases, upstream syncing, and call-graph generation
- Auto-merge from holykeebs and vial-qmk upstreams when CI passes

</details>

---

## 🚨 Troubleshooting

<details>
<summary><strong>"Vial doesn't detect my keyboard"</strong></summary>

- Make sure you flashed the **Vial-enabled** firmware from this repo (not the base holykeebs build)
- Try a different USB cable or port
- Ensure **both halves** are flashed for split keyboards

</details>

<details>
<summary><strong>"Pointing device not working"</strong></summary>

- Verify you flashed the right `pointing_config` variant for your hardware
- Double-check wiring — see [docs.holykeebs.com](https://docs.holykeebs.com) for pinouts
- Flash a debug build (`--debug` flag in `build.py`) and open a serial console for logs

</details>

<details>
<summary><strong>"Build fails"</strong></summary>

- Make sure you're building **from this fork**, not base QMK or holykeebs
- Run `qmk doctor` to validate your environment
- Initialise submodules: `git submodule update --init --recursive`

</details>

---

## 📊 Driver Call Graph

The Azoteq IQS5xx touchpad driver call graph is regenerated automatically in CI:

![Azoteq driver call graph](docs/azoteq_callgraph.svg)

---

## 🤝 Contributing

Contributions are welcome! Whether it's new pointing-device support, Vial improvements, bug fixes, or new keyboard layouts — open a PR.

1. Fork → branch → commit (use [Conventional Commits](https://www.conventionalcommits.org))
2. Build and test locally: `python build.py --build-single ...`
3. Push and open a Pull Request against `main`

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide.

---

## 🙏 Acknowledgments

- **[idank](https://github.com/idank)** — Creator of holykeebs firmware and hardware
- **[Vial Contributors](https://github.com/vial-kb/vial-qmk)** — For the amazing real-time configuration system
- **[QMK Community](https://qmk.fm)** — For the incredible keyboard firmware framework
- **All Contributors** — Everyone who opens issues, PRs, and helps the community

---

## 📄 License

GPL-2.0+ — same terms as QMK firmware. See [LICENSE](LICENSE) for details.

---

<div align="center">

Made with ❤️ and 🐾 for the mechanical keyboard community

**[📦 Releases](https://github.com/alliecatowo/allie-cat-keeb-vial/releases)** • **[🛍️ Hardware](https://holykeebs.com)** • **[📖 Docs](https://docs.holykeebs.com)** • **[🐛 Issues](https://github.com/alliecatowo/allie-cat-keeb-vial/issues)**

</div>
