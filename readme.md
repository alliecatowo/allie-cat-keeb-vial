<div align="center">

# 🐾 allie-cat-keeb-vial

### Vial-enabled QMK firmware for Holykeebs pointing-device keyboards

[![Build Firmware](https://github.com/alliecatowo/allie-cat-keeb-vial/actions/workflows/build-firmware.yml/badge.svg)](https://github.com/alliecatowo/allie-cat-keeb-vial/actions/workflows/build-firmware.yml)
[![Latest Release](https://img.shields.io/github/v/release/alliecatowo/allie-cat-keeb-vial?style=flat&logo=github&label=release&color=a78bfa)](https://github.com/alliecatowo/allie-cat-keeb-vial/releases/latest)
[![License: GPL v2+](https://img.shields.io/badge/license-GPL--2.0%2B-blue?logo=gnu)](https://github.com/alliecatowo/allie-cat-keeb-vial/blob/main/LICENSE)

[![RP2040](https://img.shields.io/badge/MCU-RP2040-e7000b?logo=raspberrypi&logoColor=white)](https://www.raspberrypi.com/products/rp2040/)
[![Vial Compatible](https://img.shields.io/badge/Vial-compatible-brightgreen?logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCI+PHBhdGggZmlsbD0id2hpdGUiIGQ9Ik0xMiAyQzYuNDggMiAyIDYuNDggMiAxMnM0LjQ4IDEwIDEwIDEwIDEwLTQuNDggMTAtMTBTMTcuNTIgMiAxMiAyem0tMiAxNWwtNS01IDEuNDEtMS40MUwxMCAxNC4xN2w3LjU5LTcuNTlMMTkgOGwtOSA5eiIvPjwvc3ZnPg==)](https://get.vial.today)
[![QMK Firmware](https://img.shields.io/badge/powered%20by-QMK-1e88e5?logo=qmk)](https://qmk.fm)
[![Discord](https://img.shields.io/discord/440868230475677696.svg?label=QMK%20Discord&logo=discord&logoColor=white&color=5865f2)](https://discord.gg/qmk)

[![GitHub Stars](https://img.shields.io/github/stars/alliecatowo/allie-cat-keeb-vial?style=flat&logo=github&color=f59e0b)](https://github.com/alliecatowo/allie-cat-keeb-vial/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/alliecatowo/allie-cat-keeb-vial?style=flat&logo=github&color=6366f1)](https://github.com/alliecatowo/allie-cat-keeb-vial/network)
[![GitHub Issues](https://img.shields.io/github/issues/alliecatowo/allie-cat-keeb-vial?style=flat&logo=github&color=ef4444)](https://github.com/alliecatowo/allie-cat-keeb-vial/issues)
[![Last Commit](https://img.shields.io/github/last-commit/alliecatowo/allie-cat-keeb-vial?style=flat&logo=github&color=22c55e)](https://github.com/alliecatowo/allie-cat-keeb-vial/commits/main)

---

> **A Vial-enabled fork of [holykeebs/qmk\_firmware](https://github.com/idank/qmk_firmware)** — bringing real-time keyboard configuration to Holykeebs' outstanding pointing-device ecosystem.

</div>

---

## 🛍️ Get Your Holykeebs Hardware

Visit the **[Holykeebs Store](https://holykeebs.com)** to grab trackballs, touchpads, trackpoints, and other pointing-device modules for your split keyboard build!

---

## ✨ Why This Fork?

Holykeebs' QMK fork provides best-in-class pointing-device support but is based on an older QMK codebase without [Vial](https://get.vial.today) integration. This fork bridges that gap:

| Feature | Holykeebs upstream | allie-cat-keeb-vial |
|---|:---:|:---:|
| Trackball / Touchpad / Trackpoint drivers | ✅ | ✅ |
| Dual pointing-device configs | ✅ | ✅ |
| VIA support | ✅ | ✅ |
| **Real-time Vial configurator** | ❌ | ✅ |
| **Pre-built `.uf2` firmware** | ❌ | ✅ |
| **Automated CI builds** | ❌ | ✅ |

---

## 🚀 Key Features

- 🎛️ **Full Vial Support** — configure keymaps, layers, macros, and pointing device settings live, no reflashing needed
- 🖱️ **Holykeebs Pointing Device Drivers** — complete support for:
  - 🔵 Pimoroni Trackball with RGB
  - 🟣 Azoteq IQS5xx TPS43 Touchpad
  - 🔴 PS/2 Trackpoint modules
  - Dual pointing-device combinations
- 🤖 **Automated GitHub Actions CI** — firmware built and released automatically on every version tag
- 📦 **Pre-built Releases** — grab a `.uf2` straight from the [Releases](https://github.com/alliecatowo/allie-cat-keeb-vial/releases) page

---

## 🎮 Supported Keyboards

| Keyboard | Variants |
|---|---|
| **Lily58** | `rev1`, `glow_enc`, `light`, `lite_rev3`, `r2g` |
| **Sofle** | `rev1`, `keyhive`, `aztec42`, `spankbd`, `sweeq` |
| **Holykeebs** variants | see `keyboards/holykeebs/` |

> All builds target the **RP2040** microcontroller (Raspberry Pi).

---

## 📦 Pre-built Firmware

Don't want to build from source? Download straight from the [**Releases page**](https://github.com/alliecatowo/allie-cat-keeb-vial/releases).

### Firmware Naming Convention

```
lily58_rev1_vial_<left-device>_<right-device>_<side>.uf2
```

**Example:** `lily58_rev1_vial_trackball_tps43_left.uf2`

| Part | Meaning |
|---|---|
| `trackball` | Pimoroni Trackball on the left half |
| `tps43` | Azoteq TPS43 Touchpad on the right half |
| `left` / `right` | Which keyboard half this file flashes |

---

## 🛠️ Build From Source

### Prerequisites

1. **Fork & clone this repository** (not the base QMK or Holykeebs repo):

   ```bash
   git clone --recurse-submodules https://github.com/YOUR_USERNAME/allie-cat-keeb-vial.git
   cd allie-cat-keeb-vial
   ```

2. Set up the environment:

   ```bash
   export ORIG_CWD="$PWD"
   export QMK_HOME="$PWD"
   export QMK_FIRMWARE="$PWD"
   export PYTHONPATH="$PWD/lib/python"
   export PATH="$PWD/bin:$PATH"
   python3 -m pip install -r requirements-dev.txt
   ```

### Quick Build (with ARM toolchain)

```bash
# Build the default config (Lily58 rev1, Vial, trackball left + TPS43 right, both sides)
python3 build.py

# Build a single variant
python3 build.py --build-single \
  --keyboard lily58/rev1 \
  --keymap vial \
  --left-device trackball \
  --right-device tps43 \
  --side left

# Build all release configurations
python3 build.py --build-all
```

### Manual QMK Command

```bash
make lily58/rev1:vial \
  -e USER_NAME=holykeebs \
  -e POINTING_DEVICE=trackball_tps43 \
  -e SIDE=left
```

---

## ⚡ Flashing Your Keyboard

1. Download the appropriate `.uf2` from [Releases](https://github.com/alliecatowo/allie-cat-keeb-vial/releases)
2. Enter bootloader mode — double-tap the **RESET** button on the PCB
3. A `RPI-RP2` USB drive appears; drag-and-drop the `.uf2` onto it
4. Repeat for the other half (split keyboards require flashing both sides)

---

## 🎨 Configure with Vial

1. Download [**Vial**](https://get.vial.today) for your OS
2. Plug in your keyboard
3. Open Vial and configure in real-time:
   - Key mappings & layers
   - Macros & tap-dance
   - Pointing device sensitivity & scroll
   - RGB lighting

---

## 🔄 GitHub Actions in Your Fork

Fork this repo and get automated firmware CI for free!

**Triggers:**
- Tags matching `v*` → full release build + GitHub Release with `.uf2` artifacts
- `workflow_dispatch` → manual trigger from the Actions tab

**Creating a release:**
```bash
git tag v1.2.0
git push origin v1.2.0
```

The workflow will build all firmware variants and publish them as a GitHub Release automatically.

---

## 🔬 What Was Changed

### Vial Core Integration
- Backported Vial's quantum-layer modifications from [vial-qmk](https://github.com/vial-kb/vial-qmk)
- Added Vial keycodes, keyboard-definition structures, and the Vial USB communication protocol

### Build System
- Extended build tooling via `build.py` for multi-variant CI matrix generation
- Added Vial-specific build flags; CI generates and uploads `.uf2` artifacts automatically

### Keymaps
- Replaced VIA keymaps with Vial-compatible variants (`.vil` definitions included)
- Backward-compatible with existing VIA configurations

### Memory Optimizations
- Tuned feature flags to fit Vial's additional footprint within RP2040 constraints

---

## 📊 Driver Call Graph

The Azoteq IQS5xx touchpad driver call graph is generated automatically by CI:

![Azoteq IQS5xx driver call graph](docs/azoteq_callgraph.svg)

---

## 🤝 Contributing

Contributions are welcome! Bug fixes, new pointing-device support, keymap improvements — all appreciated.

1. Fork the repo & create a feature branch
2. Commit with [Conventional Commits](https://www.conventionalcommits.org/): `feat:`, `fix:`, `docs:`, `ci:`, etc.
3. Open a Pull Request — CI will build and validate your changes automatically

See [CONTRIBUTING.md](CONTRIBUTING.md) for full guidelines.

---

## 🚨 Troubleshooting

<details>
<summary><b>Vial doesn't detect my keyboard</b></summary>

- Confirm you flashed the Vial-enabled firmware (`.uf2` from this repo, not base Holykeebs)
- Try a different USB cable or port
- Make sure **both halves** are flashed for split keyboards

</details>

<details>
<summary><b>Pointing device not working</b></summary>

- Verify you flashed the correct variant for your hardware combination
- Double-check wiring against [docs.holykeebs.com](https://docs.holykeebs.com)
- Flash the debug build variant for console output

</details>

<details>
<summary><b>Build fails</b></summary>

- Make sure you cloned **this fork**, not base QMK
- Run `qmk doctor` to check your toolchain
- Ensure submodules are initialized: `git submodule update --init --recursive`

</details>

---

## 📚 Resources

| Link | Description |
|---|---|
| [Holykeebs Store](https://holykeebs.com) | Buy hardware |
| [Holykeebs Docs](https://docs.holykeebs.com) | Wiring & hardware guides |
| [Holykeebs QMK repo](https://github.com/idank/qmk_firmware) | Upstream firmware |
| [Vial](https://get.vial.today) | Real-time configurator |
| [QMK Firmware](https://qmk.fm) | Base firmware framework |
| [Releases](https://github.com/alliecatowo/allie-cat-keeb-vial/releases) | Pre-built `.uf2` files |

---

## 🙏 Acknowledgments

- **[idank](https://github.com/idank)** — Creator of Holykeebs firmware and hardware
- **[Vial contributors](https://github.com/vial-kb/vial-qmk)** — For the incredible real-time config system
- **[QMK community](https://qmk.fm)** — For the foundation everything is built on

---

## 📄 License

GPL-2.0+ — same as QMK firmware. See [LICENSE](LICENSE) for details.

---

<div align="center">

**[🛍️ Get Hardware](https://holykeebs.com)** &nbsp;•&nbsp; **[📖 Documentation](https://docs.holykeebs.com)** &nbsp;•&nbsp; **[📦 Releases](https://github.com/alliecatowo/allie-cat-keeb-vial/releases)** &nbsp;•&nbsp; **[🐛 Report a Bug](https://github.com/alliecatowo/allie-cat-keeb-vial/issues)**

Made with ❤️ for the mechanical keyboard community 🐾

</div>
