<div align="center">

# 🐾 allie-cat-keeb-vial

### Vial-Enabled QMK Firmware for Holykeebs & Friends

[![Build Status](https://img.shields.io/github/actions/workflow/status/alliecatowo/allie-cat-keeb-vial/build-firmware.yml?logo=github&label=firmware%20build&style=for-the-badge)](https://github.com/alliecatowo/allie-cat-keeb-vial/actions/workflows/build-firmware.yml)
[![Latest Release](https://img.shields.io/github/v/release/alliecatowo/allie-cat-keeb-vial?include_prereleases&logo=github&style=for-the-badge&color=blueviolet)](https://github.com/alliecatowo/allie-cat-keeb-vial/releases/latest)
[![License](https://img.shields.io/badge/license-GPL--2.0%2B-blue?style=for-the-badge&logo=gnu)](https://github.com/alliecatowo/allie-cat-keeb-vial/blob/main/LICENSE)

[![Stars](https://img.shields.io/github/stars/alliecatowo/allie-cat-keeb-vial?style=flat-square&logo=github)](https://github.com/alliecatowo/allie-cat-keeb-vial/stargazers)
[![Forks](https://img.shields.io/github/forks/alliecatowo/allie-cat-keeb-vial?style=flat-square&logo=github)](https://github.com/alliecatowo/allie-cat-keeb-vial/network/members)
[![Issues](https://img.shields.io/github/issues/alliecatowo/allie-cat-keeb-vial?style=flat-square&logo=github)](https://github.com/alliecatowo/allie-cat-keeb-vial/issues)
[![Last Commit](https://img.shields.io/github/last-commit/alliecatowo/allie-cat-keeb-vial?style=flat-square&logo=github)](https://github.com/alliecatowo/allie-cat-keeb-vial/commits/main)
[![QMK](https://img.shields.io/badge/powered%20by-QMK-blue?style=flat-square&logo=qmk)](https://qmk.fm)
[![Vial](https://img.shields.io/badge/vial--enabled-%E2%9C%93-brightgreen?style=flat-square)](https://get.vial.today)
[![Discord](https://img.shields.io/discord/440868230475677696.svg?label=QMK%20Discord&style=flat-square&logo=discord)](https://discord.gg/qmk)

---

*A community-maintained **Vial-enabled** fork of [holykeebs/qmk_firmware](https://github.com/idank/qmk_firmware) — bringing real-time keyboard configuration to holykeebs' incredible pointing-device ecosystem.*

**[⬇️ Download Firmware](https://github.com/alliecatowo/allie-cat-keeb-vial/releases)** · **[🛍️ Get Hardware](https://holykeebs.com)** · **[📚 Documentation](https://docs.holykeebs.com)** · **[🐛 Report Bug](https://github.com/alliecatowo/allie-cat-keeb-vial/issues)**

</div>

---

## ✨ What Is This?

The [holykeebs](https://holykeebs.com) QMK repository delivers excellent support for trackballs, touchpads and trackpoints — but ships on an older QMK base that predates Vial. **This fork bridges that gap:**

- 🔁 Backports Vial-QMK's real-time configuration layer into the holykeebs codebase
- 🖱️ Keeps every holykeebs pointing-device driver fully intact
- 📦 Publishes pre-built `.uf2` files so you can flash without touching a compiler
- 🤖 Runs automated CI builds across all supported configurations on every release

---

## 🎹 Supported Keyboards

| Keyboard | MCU | Split | Pointing Devices | Vial |
|---|---|---|---|---|
| **Lily58** (rev1) | RP2040 | ✅ | Trackball, TPS43 Touchpad, Trackpoint, Dual | ✅ |
| **Sofle** (rev1) | — | ✅ | Trackball, Touchpad | ✅ |
| **holykeebs Aztec42** | RP2040 | ✅ | Trackball, Touchpad, Trackpoint | ✅ |
| **holykeebs Spankbd** | — | ✅ | Trackball, Touchpad, Trackpoint | ✅ |
| **holykeebs Sweeq** | — | ✅ | Trackball, Touchpad, Trackpoint | ✅ |

> Want your keyboard added? [Open an issue!](https://github.com/alliecatowo/allie-cat-keeb-vial/issues/new)

---

## 🚀 Key Features

| Feature | Details |
|---|---|
| 🎛️ **Full Vial Support** | Configure keymaps, layers, macros, tap-dance & more — live, without reflashing |
| 🖱️ **Holykeebs Pointing Devices** | Pimoroni Trackball (+ RGB), Azoteq IQS5xx TPS43 Touchpad, PS/2 Trackpoint, dual-device configs |
| 🔄 **VIA Compatible** | Works with both [VIA](https://usevia.app) and [Vial](https://get.vial.today) configurators |
| ⚡ **Automated Builds** | GitHub Actions matrix across every keyboard/pointing-device combo on each release tag |
| 💾 **Pre-built Firmware** | Download a ready-to-flash `.uf2` from [Releases](https://github.com/alliecatowo/allie-cat-keeb-vial/releases) |
| 🔮 **Regular Sync** | Kept up-to-date with upstream holykeebs changes |

---

## ⬇️ Flash Pre-built Firmware (Easiest)

> No compiler needed!

1. Grab the latest `.uf2` for your keyboard from **[Releases](https://github.com/alliecatowo/allie-cat-keeb-vial/releases)**
2. Double-tap **RESET** on your keyboard to enter bootloader mode — a drive called `RPI-RP2` will appear
3. Copy the `.uf2` file onto the drive — it flashes automatically and reboots
4. Repeat for the other half (split keyboards)
5. Open **[Vial](https://get.vial.today)** and start customizing!

### Firmware naming convention

```
lily58_rev1_via_<pointing-device-combo>_<side>.uf2
```

| Part | Examples |
|---|---|
| `<pointing-device-combo>` | `trackball_tps43`, `trackball_trackball`, `tps43_tps43` |
| `<side>` | `left`, `right` |

---

## 🛠️ Build From Source

### Prerequisites

```bash
# macOS
brew install qmk/qmk/qmk

# Linux / WSL
sudo apt-get update && sudo apt-get install -y git python3-pip
pip3 install qmk && qmk setup -y
```

### Quick Start

```bash
# 1. Clone the repo (with submodules!)
git clone --recurse-submodules https://github.com/alliecatowo/allie-cat-keeb-vial.git
cd allie-cat-keeb-vial

# 2. Install Python dependencies
pip install -r requirements-dev.txt

# 3. Build all firmware
python build.py --build-all
```

### Build Script Options

```bash
# Build one specific configuration
python build.py --build-single \
  --keyboard lily58/rev1 \
  --keymap via \
  --left-device trackball \
  --right-device tps43

# Build everything (all keyboards × all pointing-device combos)
python build.py --build-all

# Vial-only (no debug console)
python build.py --vial-only

# Full release build (all variants)
python build.py --release
```

### Manual QMK Command

```bash
make lily58/rev1:via \
  -e USER_NAME=holykeebs \
  -e POINTING_DEVICE=trackball_tps43 \
  -e SIDE=left \
  -e TRACKBALL_RGB_RAINBOW=yes \
  -e VIAL_ENABLE=yes
```

---

## 🔧 What This Fork Changes

<details>
<summary><strong>Click to expand technical details</strong></summary>

### 1. Vial Core Integration
- Backported Vial's quantum layer modifications from [vial-qmk](https://github.com/vial-kb/vial-qmk)
- Added Vial-specific keycodes and configuration structures
- Integrated the Vial communication protocol

### 2. Build System Updates
- Modified the build system to support Vial's additional features
- Added Vial-specific build flags and configurations
- Created an automated matrix build script (`build.py`) for common configurations

### 3. Keymap Modifications
- Updated VIA keymaps to include Vial's additional configuration options
- Added proper Vial keyboard definitions (`.vil` files)
- Maintained backward compatibility with existing VIA configurations

### 4. Memory Optimizations
- Tuned firmware size to accommodate Vial's additional overhead
- Carefully balanced features within RP2040 flash constraints

</details>

---

## 🤖 GitHub Actions / CI

When you fork this repo, automated firmware builds come for free.

| Workflow | Trigger | What it does |
|---|---|---|
| `build-firmware.yml` | Push a `v*` tag, manual dispatch | Builds all firmware variants, creates a GitHub release with `.uf2` attachments |
| `pr-checks.yml` | Pull requests | Quick build checks + linting |
| `quick-tests.yml` | Push / PR | Python unit tests (`nose2`) + flake8 |
| `sync-upstreams.yml` | Scheduled | Syncs with upstream holykeebs & Vial-QMK |

### Creating a Release

```bash
git tag v1.2.0
git push origin v1.2.0
# GitHub Actions builds everything and publishes the release automatically
```

---

## 📊 Driver Call Graph

The Azoteq IQS5xx touchpad driver call graph is generated automatically in CI:

![Azoteq driver call graph](docs/azoteq_callgraph.svg)

---

## 🤝 Contributing

Contributions are welcome! Whether it's:

- 🆕 Support for new pointing devices or keyboards
- 🐛 Bug fixes & optimizations
- 🔌 Better Vial integration
- 📖 Documentation improvements

### Contribution Steps

```bash
git checkout -b feature/my-awesome-feature
# hack hack hack
git commit -m "feat: add my awesome feature"
git push origin feature/my-awesome-feature
# open a Pull Request
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.

---

## 🚨 Troubleshooting

<details>
<summary><strong>Vial doesn't detect my keyboard</strong></summary>

- Make sure you flashed the **Vial-enabled** firmware (from this fork), not base holykeebs
- Try a different USB cable or port
- For split keyboards, ensure **both** halves are flashed
</details>

<details>
<summary><strong>Pointing device not working</strong></summary>

- Verify you chose the correct firmware variant for your hardware configuration
- Double-check wiring connections at [docs.holykeebs.com](https://docs.holykeebs.com)
- Flash the **debug** firmware build to get console output via Vial's CONSOLE tab
</details>

<details>
<summary><strong>Build fails</strong></summary>

- Make sure you're building from **this fork**, not base QMK or the original holykeebs repo
- Run `qmk doctor` to validate your local environment
- Ensure submodules are initialised: `git submodule update --init --recursive`
</details>

<details>
<summary><strong>Codex / automation bootstrap</strong></summary>

```bash
pip install -r requirements-dev.txt
export ORIG_CWD="$PWD" QMK_HOME="$PWD" QMK_FIRMWARE="$PWD"
export PYTHONPATH="$PWD/lib/python" PATH="$PWD/bin:$PATH"
flake8 lib/python          # lint Python helpers
python -m nose2 -v         # smoke tests
```

See [docs/codex.md](docs/codex.md) for more detail.
</details>

---

## 🙏 Acknowledgments

- **[idank](https://github.com/idank)** — creator of the holykeebs firmware & hardware ecosystem
- **[Vial Contributors](https://github.com/vial-kb/vial-qmk)** — for the incredible real-time configuration system
- **[QMK Community](https://qmk.fm)** — for the keyboard firmware framework that makes all of this possible
- **All contributors** — everyone who has opened issues, PRs, and helped test

---

## 📄 License

GPL-2.0+, the same as QMK firmware. See [LICENSE](LICENSE) for full text.

---

<div align="center">

Made with ❤️ and way too many mechanical keyboards

**[⬇️ Download Firmware](https://github.com/alliecatowo/allie-cat-keeb-vial/releases)** · **[🛍️ Get Hardware](https://holykeebs.com)** · **[📚 Documentation](https://docs.holykeebs.com)** · **[💬 QMK Discord](https://discord.gg/qmk)**

</div>
