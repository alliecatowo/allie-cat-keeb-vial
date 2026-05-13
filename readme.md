<div align="center">

# 🐾 Allie Cat Keeb — Vial-Enabled QMK Firmware

*Real-time keyboard configuration for Holykeebs pointing-device builds*

[![GitHub Stars](https://img.shields.io/github/stars/alliecatowo/allie-cat-keeb-vial?style=for-the-badge&logo=github&color=ff69b4)](https://github.com/alliecatowo/allie-cat-keeb-vial/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/alliecatowo/allie-cat-keeb-vial?style=for-the-badge&logo=github&color=c792ea)](https://github.com/alliecatowo/allie-cat-keeb-vial/network/members)
[![Open Issues](https://img.shields.io/github/issues/alliecatowo/allie-cat-keeb-vial?style=for-the-badge&logo=github&color=f78c6c)](https://github.com/alliecatowo/allie-cat-keeb-vial/issues)
[![Last Commit](https://img.shields.io/github/last-commit/alliecatowo/allie-cat-keeb-vial?style=for-the-badge&logo=git&color=89ddff)](https://github.com/alliecatowo/allie-cat-keeb-vial/commits/main)

[![Build Status](https://img.shields.io/github/actions/workflow/status/alliecatowo/allie-cat-keeb-vial/build-firmware.yml?branch=main&style=for-the-badge&logo=githubactions&label=firmware%20build)](https://github.com/alliecatowo/allie-cat-keeb-vial/actions/workflows/build-firmware.yml)
[![Latest Release](https://img.shields.io/github/v/tag/alliecatowo/allie-cat-keeb-vial?style=for-the-badge&logo=github&label=release&color=addb67)](https://github.com/alliecatowo/allie-cat-keeb-vial/releases)
[![QMK](https://img.shields.io/badge/built%20on-QMK-blue?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PC9zdmc+)](https://qmk.fm)
[![Vial](https://img.shields.io/badge/Vial-enabled-green?style=for-the-badge)](https://get.vial.today)
[![License](https://img.shields.io/badge/license-GPL--2.0%2B-blue?style=for-the-badge)](https://github.com/alliecatowo/allie-cat-keeb-vial/blob/main/LICENSE)

---

**[⬇️ Download Firmware](https://github.com/alliecatowo/allie-cat-keeb-vial/releases)** &nbsp;•&nbsp;
**[🛍️ Buy Hardware](https://holykeebs.com)** &nbsp;•&nbsp;
**[📖 Docs](https://docs.holykeebs.com)** &nbsp;•&nbsp;
**[🐛 Report Bug](https://github.com/alliecatowo/allie-cat-keeb-vial/issues)**

</div>

---

A **Vial-enabled fork** of the [holykeebs QMK firmware](https://github.com/idank/qmk_firmware), bringing real-time keyboard configuration to holykeebs' amazing pointing-device builds — no reflashing required.

---

## ⚡ Quick Start

| Step | Action |
|------|--------|
| 1️⃣ | [Download](https://github.com/alliecatowo/allie-cat-keeb-vial/releases) the latest `.uf2` for your keyboard & side |
| 2️⃣ | Double-tap `RESET` to enter bootloader — a `RPI-RP2` drive appears |
| 3️⃣ | Drag-and-drop the `.uf2` onto the drive (repeat for both halves on splits) |
| 4️⃣ | Open [Vial](https://get.vial.today) and configure everything live! |

---

## 🎯 Why This Fork?

The upstream holykeebs firmware is excellent for pointing-device support but targets an older QMK version that predates Vial. This fork bridges the gap:

| Feature | Upstream holykeebs | **This fork** |
|---------|--------------------|---------------|
| Trackball / Touchpad / Trackpoint | ✅ | ✅ |
| VIA support | ✅ | ✅ |
| **Vial real-time config** | ❌ | ✅ |
| Pre-built `.uf2` releases | ❌ | ✅ |
| Automated CI builds | ❌ | ✅ |

---

## ⌨️ Supported Keyboards

| Keyboard | Layout | Pointing Devices | Status |
|----------|--------|-----------------|--------|
| **Lily58** | 6×4 split | Trackball, Touchpad (TPS43), Trackpoint | ✅ Supported |
| **Sofle** | 6×4 split | Trackball, Touchpad (TPS43) | ✅ Supported |
| **Holykeebs Aztec42** | 5×4 split | Trackball | ✅ Supported |
| **Holykeebs SpanKBD** | Columnar split | Trackball, Touchpad | ✅ Supported |
| **Holykeebs Sweeq** | 3×5 split | Trackball | ✅ Supported |

---

## 🚀 Key Features

- 🖱️ **Full Holykeebs Pointing Device Support**
  - Pimoroni Trackball with RGB
  - Azoteq IQS5xx TPS43 Touchpad
  - PS/2 Trackpoint modules
  - Dual pointing-device configurations
- ⚡ **Vial Real-Time Config** — remap keys, layers, macros, and pointing device settings without reflashing
- 🔌 **VIA Compatible** — works with both VIA and Vial configurators
- 🤖 **Automated GitHub Actions builds** — every tag produces a full suite of `.uf2` files
- 🔄 **Regularly synced** with upstream holykeebs changes

---

## 📦 Pre-Built Firmware

Find ready-to-flash firmware on the **[Releases page](https://github.com/alliecatowo/allie-cat-keeb-vial/releases)**.

Each release ships:
| Variant | Description |
|---------|-------------|
| Standard | Basic Vial-enabled firmware |
| Debug | Console output enabled for troubleshooting |
| Configuration variants | Different pointing-device combos |

### Naming convention

```
<keyboard>_<keymap>_<left-device>_<right-device>_<side>.uf2
```

Example: `lily58_rev1_via_trackball_tps43_left.uf2`

---

## 🛠️ Building From Source

### Prerequisites

```bash
# macOS
brew install qmk/qmk/qmk

# Linux / WSL
sudo apt-get install -y git python3-pip
pip3 install qmk && qmk setup -y
```

### Clone & Build

```bash
git clone --recurse-submodules https://github.com/alliecatowo/allie-cat-keeb-vial.git
cd allie-cat-keeb-vial

# Bootstrap the environment
export ORIG_CWD="$PWD" QMK_HOME="$PWD" QMK_FIRMWARE="$PWD"
export PYTHONPATH="$PWD/lib/python" PATH="$PWD/bin:$PATH"
python3 -m pip install -r requirements-dev.txt

# Build all variants
python build.py
```

### Common build flags

```bash
# Single target — e.g. Lily58 left half with trackball + touchpad
python build.py --build-single \
  --keyboard lily58/rev1 \
  --keymap via \
  --left-device trackball \
  --right-device tps43

# Or raw QMK make
make lily58/rev1:via \
  -e USER_NAME=holykeebs \
  -e POINTING_DEVICE=trackball_tps43 \
  -e SIDE=left \
  -e VIAL_ENABLE=yes
```

---

## 🤖 CI / GitHub Actions

Forking gives you free automated builds! Firmware is built and attached to every release tag.

```bash
# Tag a new release to trigger the full build matrix
git tag v1.2.0
git push origin v1.2.0
```

The workflow (`build-firmware.yml`) will:
1. Generate the build matrix from your keyboard configs
2. Build all firmware variants in parallel
3. Create a GitHub Release with all `.uf2` files attached

---

## 🔧 What We Changed

### Vial Core Integration
- Backported Vial's quantum-layer modifications from [vial-qmk](https://github.com/vial-kb/vial-qmk)
- Added Vial-specific keycodes, config structures, and communication protocol

### Build System
- Vial-specific build flags and configs
- Automated `build.py` script with a full build matrix

### Keymaps
- VIA keymaps updated with Vial's additional options
- Proper `.vil` keyboard definition files
- Backward-compatible with existing VIA configs

### Memory Optimizations
- Firmware size tuned to fit Vial extras within RP2040 flash constraints

---

## 🚨 Troubleshooting

| Symptom | Fix |
|---------|-----|
| Vial doesn't detect keyboard | Confirm you flashed the Vial build; try a different USB cable/port; check both halves are flashed |
| Pointing device not working | Verify firmware variant matches your hardware; see [docs.holykeebs.com](https://docs.holykeebs.com) |
| Build fails | Ensure you're building from **this** fork; run `qmk doctor`; init submodules: `git submodule update --init` |

---

## 📊 Azoteq IQS5xx Driver Call Graph

Generated automatically during CI:

![Azoteq driver call graph](docs/azoteq_callgraph.svg)

---

## 🤝 Contributing

All contributions welcome!

1. Fork → feature branch → PR
2. Build & test locally first
3. Document new features or configs

---

## 🙏 Acknowledgments

- **[idank](https://github.com/idank)** — holykeebs firmware & hardware
- **[Vial Contributors](https://github.com/vial-kb/vial-qmk)** — real-time configuration magic
- **[QMK Community](https://qmk.fm)** — the foundation everything is built on
- **All contributors** who keep this project improving!

---

## 📄 License

GPL-2.0+ — same terms as QMK firmware. See [`LICENSE`](LICENSE) for details.

---

<div align="center">

Made with ❤️ and 🐾 for the mechanical keyboard community

[![GitHub Stars](https://img.shields.io/github/stars/alliecatowo/allie-cat-keeb-vial?style=social)](https://github.com/alliecatowo/allie-cat-keeb-vial/stargazers)

</div>
