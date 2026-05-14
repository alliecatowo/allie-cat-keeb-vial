<div align="center">

# 🐾 Allie Cat Keeb

### Vial-Enabled QMK Firmware for Holykeebs Keyboards

*Real-time configuration. Trackballs, touchpads, and trackpoints — all in one place.*

---

[![Build Status](https://github.com/alliecatowo/allie-cat-keeb-vial/actions/workflows/build-firmware.yml/badge.svg)](https://github.com/alliecatowo/allie-cat-keeb-vial/actions)
[![Latest Release](https://img.shields.io/github/v/release/alliecatowo/allie-cat-keeb-vial?label=latest%20release&color=brightgreen)](https://github.com/alliecatowo/allie-cat-keeb-vial/releases/latest)
[![License](https://img.shields.io/badge/license-GPL--2.0+-blue.svg)](LICENSE)
[![Discord](https://img.shields.io/discord/440868230475677696.svg?label=QMK%20Discord&color=5865F2)](https://discord.gg/qmk)

**[⬇️ Download Firmware](https://github.com/alliecatowo/allie-cat-keeb-vial/releases)** · **[🛍️ Get Hardware](https://holykeebs.com)** · **[📖 Docs](https://docs.holykeebs.com)** · **[🐛 Report Bug](https://github.com/alliecatowo/allie-cat-keeb-vial/issues)**

</div>

---

## What Is This?

This repo is a **Vial-enabled fork** of [holykeebs/qmk_firmware](https://github.com/idank/qmk_firmware), the gold standard for split keyboards with integrated pointing devices. The upstream holykeebs firmware is fantastic — but it predates modern Vial support, meaning you had to reflash every time you tweaked a keymap.

This fork fixes that. You get everything holykeebs offers, plus live remapping in the Vial GUI without ever touching a compiler.

---

## ✨ Features

| Feature | Details |
|---|---|
| 🖱️ **Pointing Devices** | Pimoroni Trackball (RGB), Azoteq IQS5xx TPS43 Touchpad, PS/2 Trackpoint, dual-device combos |
| ⚡ **Vial Support** | Real-time key remapping, layers, macros, RGB — no reflashing required |
| 🔁 **VIA Compatible** | Works with both VIA and Vial configurators |
| 🏗️ **Automated Builds** | GitHub Actions builds firmware for all configurations on every release |
| 🔄 **Upstream Sync** | Regularly synced with holykeebs and QMK upstream changes |
| 🧠 **Memory Optimized** | Carefully tuned to fit all features within RP2040 constraints |

---

## 🎹 Supported Keyboards

| Keyboard | Variants | Pointing Devices |
|---|---|---|
| **Lily58** | `rev1`, `glow_enc`, `lite_rev3`, `r2g` | Trackball, TPS43 Touchpad, Trackpoint |
| **Sofle** | Standard | Trackball, TPS43 Touchpad |
| **Holykeebs** | `aztec42`, `spankbd`, `sweeq` | Varies by model |

---

## 🚀 Quick Start

### Option A — Just Flash It

1. **Download** the right `.uf2` from [**Releases**](https://github.com/alliecatowo/allie-cat-keeb-vial/releases)
2. **Enter bootloader** — double-tap the RESET button on your keyboard
3. **Copy the file** to the `RPI-RP2` drive that appears
4. **Repeat** for both halves if you have a split keyboard

> [!TIP]
> Not sure which firmware to pick? See the [Firmware Naming Convention](#-firmware-naming-convention) below.

### Option B — Configure with Vial

Once flashed, open [Vial](https://get.vial.today) and you can instantly customize:
- Key mappings & layers
- Macros & tap-dance
- Pointing device sensitivity & scrolling
- RGB lighting effects

---

## 📦 Firmware Naming Convention

```
lily58_rev1_vial_[left-device]_[right-device]_[side].uf2
```

| Token | Meaning | Examples |
|---|---|---|
| `left-device` | Pointing device on the left half | `trackball`, `tps43`, `none` |
| `right-device` | Pointing device on the right half | `trackball`, `tps43`, `none` |
| `side` | Which half to flash | `left`, `right` |

**Example:** `lily58_rev1_vial_trackball_tps43_left.uf2` → Lily58 rev1, trackball on left, touchpad on right, flash this to the left half.

Each release also ships **debug builds** (with USB console output) for troubleshooting.

---

## 🛠️ Building from Source

<details>
<summary><strong>Prerequisites</strong></summary>

Fork this repo (not base QMK or holykeebs), then install the toolchain:

```bash
# macOS
brew install qmk/qmk/qmk

# Linux / WSL
sudo apt-get update && sudo apt-get install -y git python3-pip
pip3 install qmk
qmk setup -y
```

</details>

### Clone & Build

```bash
git clone --recurse-submodules https://github.com/YOUR_USERNAME/allie-cat-keeb-vial.git
cd allie-cat-keeb-vial

# Build the default configuration (trackball left, TPS43 right)
python build.py
```

### Common Build Commands

```bash
# Build a specific configuration
python build.py --build-single \
  --keyboard lily58/rev1 \
  --keymap vial \
  --left-device trackball \
  --right-device tps43

# Build all configurations
python build.py --build-all

# Build for release (all variants, no debug)
python build.py --release
```

<details>
<summary><strong>Manual QMK make commands</strong></summary>

```bash
# Left half — trackball + TPS43 touchpad, Vial enabled
make lily58/rev1:via \
  -e USER_NAME=holykeebs \
  -e POINTING_DEVICE=trackball_tps43 \
  -e SIDE=left \
  -e TRACKBALL_RGB_RAINBOW=yes \
  -e VIAL_ENABLE=yes
```

</details>

---

## 🔄 GitHub Actions in Your Fork

Forking this repo gives you automated firmware builds for free. The workflows handle everything:

| Workflow | Trigger | What it Does |
|---|---|---|
| **Build Firmware** | Push a `v*` tag | Builds all variants, creates a GitHub Release |
| **PR Checks** | Pull requests | Validates build compiles for all configs |
| **Sync Upstreams** | Scheduled / manual | Merges latest holykeebs + QMK changes |
| **Changelog** | Push to `main` | Auto-generates `CHANGELOG.md` |

### Creating a Release

```bash
git tag v1.2.0
git push origin v1.2.0
# GitHub Actions builds firmware and attaches .uf2 files to the release automatically
```

---

## 🔍 Why This Fork Exists

The holykeebs firmware has exceptional pointing device support — but it's pinned to an older QMK version that predates Vial. This fork bridges the gap with four targeted changes:

1. **Vial Core Integration** — Backported Vial's quantum layer from [vial-qmk](https://github.com/vial-kb/vial-qmk), including keycodes and the communication protocol
2. **Build System Updates** — Added Vial build flags and automated multi-config build scripts
3. **Keymap Modifications** — Updated VIA keymaps with Vial extras; `.vil` definitions added; backward compat maintained
4. **Memory Optimizations** — Balanced feature set to fit within RP2040 flash constraints

---

## 📊 Azoteq Driver Call Graph

The IQS5xx touchpad driver call graph is auto-generated by CI and updated on each build:

![Azoteq driver call graph](docs/azoteq_callgraph.svg)

---

## 🚨 Troubleshooting

<details>
<summary><strong>"Vial doesn't detect my keyboard"</strong></summary>

- Make sure you flashed this fork's firmware, not the base holykeebs firmware
- Try a different USB cable or port
- For split keyboards, both halves need to be flashed
- On Linux, you may need udev rules — see [Vial docs](https://get.vial.today/manual/linux-udev.html)

</details>

<details>
<summary><strong>"Pointing device not responding"</strong></summary>

- Verify you flashed the correct variant (e.g., `trackball_tps43` if you have both devices)
- Check physical wiring against [docs.holykeebs.com](https://docs.holykeebs.com)
- Flash the debug build and open a serial console (115200 baud) to see driver output

</details>

<details>
<summary><strong>"Build fails"</strong></summary>

- Make sure you cloned **this fork**, not base QMK
- Run `qmk doctor` to validate your build environment
- Initialize submodules: `git submodule update --init --recursive`
- Check the [PR Checks workflow logs](https://github.com/alliecatowo/allie-cat-keeb-vial/actions) for the exact error

</details>

---

## 🤝 Contributing

Contributions are welcome — new pointing device support, Vial improvements, bug fixes, new layouts. See [**CONTRIBUTING.md**](CONTRIBUTING.md) for the full guide.

**Quick version:**

```bash
git checkout -b feature/your-feature
# make your changes, build & test locally
git commit -m "feat: describe your change"
# open a pull request
```

> [!NOTE]
> Run `python build.py --build-single --left-device trackball --right-device tps43` before opening a PR to make sure your changes compile.

---

## 🙏 Acknowledgments

- **[idank / holykeebs](https://github.com/idank)** — for the extraordinary pointing device firmware and hardware
- **[Vial Contributors](https://github.com/vial-kb/vial-qmk)** — for making real-time keyboard config a reality
- **[QMK Community](https://qmk.fm)** — the foundation everything is built on

---

## 📄 License

GPL-2.0+, the same terms as QMK firmware. See [LICENSE](LICENSE) for details.

---

<div align="center">

**[⬇️ Download Firmware](https://github.com/alliecatowo/allie-cat-keeb-vial/releases)** · **[🛍️ Get Hardware](https://holykeebs.com)** · **[📖 Holykeebs Docs](https://docs.holykeebs.com)** · **[💬 QMK Discord](https://discord.gg/qmk)**

<sub>Made with ❤️ for the mechanical keyboard community</sub>

</div>
