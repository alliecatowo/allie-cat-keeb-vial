<div align="center">

# 🐾 Allie Cat Keeb — Vial-Enabled QMK Firmware

### Bringing real-time keyboard configurability to [Holykeebs](https://holykeebs.com) pointing-device builds

[![Build Firmware](https://github.com/alliecatowo/allie-cat-keeb-vial/actions/workflows/build-firmware.yml/badge.svg)](https://github.com/alliecatowo/allie-cat-keeb-vial/actions/workflows/build-firmware.yml)
[![Quick Tests](https://github.com/alliecatowo/allie-cat-keeb-vial/actions/workflows/quick-tests.yml/badge.svg)](https://github.com/alliecatowo/allie-cat-keeb-vial/actions/workflows/quick-tests.yml)
[![Latest Release](https://img.shields.io/github/v/release/alliecatowo/allie-cat-keeb-vial?label=latest%20release&color=violet)](https://github.com/alliecatowo/allie-cat-keeb-vial/releases/latest)
[![Last Commit](https://img.shields.io/github/last-commit/alliecatowo/allie-cat-keeb-vial)](https://github.com/alliecatowo/allie-cat-keeb-vial/commits/main)
[![GitHub Stars](https://img.shields.io/github/stars/alliecatowo/allie-cat-keeb-vial?style=flat)](https://github.com/alliecatowo/allie-cat-keeb-vial/stargazers)
[![License](https://img.shields.io/badge/license-GPL--2.0%2B-blue)](https://github.com/alliecatowo/allie-cat-keeb-vial/blob/main/LICENSE)
[![Discord](https://img.shields.io/discord/440868230475677696.svg?label=QMK%20Discord&color=5865F2)](https://discord.gg/qmk)

</div>

---

This repository is a **Vial-enabled fork** of the [holykeebs/qmk_firmware](https://github.com/idank/qmk_firmware) project, giving you real-time keyboard configuration (no reflashing!) on holykeebs' excellent pointing-device builds for split keyboards like the **Lily58** and **Sofle**.

## 🛍️ Get Your Holykeebs Hardware

Visit the **[Holykeebs Store](https://holykeebs.com)** to pick up trackballs, touchpads, trackpoints, and other pointing-device modules for your mechanical keyboard!

---

## 🎯 Why This Fork Exists

The holykeebs QMK repo has top-tier pointing-device support, but it's based on an older QMK version that predates Vial. This fork bridges the gap:

| What we added | Why it matters |
|---|---|
| **Vial core backport** | Configure keymaps, macros, and layers live — no reflash needed |
| **VIA + Vial dual compatibility** | Works with both configurators |
| **Automated firmware builds** | Pre-built `.uf2` files for every supported config in every release |
| **Upstream sync workflow** | Stays current with holykeebs, QMK, and Vial-QMK |
| **Call-graph CI artifact** | Azoteq IQS5xx driver diagram generated automatically |

---

## 🚀 Key Features

- ✅ **Full Vial support** — real-time key mapping, layers, macros, and tap-dance in [Vial GUI](https://get.vial.today)
- ✅ **Holykeebs pointing devices** — Pimoroni Trackball (RGB), Azoteq IQS5xx TPS43 Touchpad, PS/2 Trackpoint, dual-device configs
- ✅ **Supported keyboards** — Lily58 (rev1, lite, glow, r2g) and Sofle
- ✅ **RP2040 optimised** — memory budget carefully balanced to fit Vial's extras
- ✅ **Pre-built releases** — grab a `.uf2` and go; no toolchain required

---

## 📦 Pre-built Firmware

Don't want to build from source? Head straight to [**Releases**](https://github.com/alliecatowo/allie-cat-keeb-vial/releases) — every tagged release attaches pre-built firmware for all supported configurations.

### Firmware naming convention

```
lily58_rev1_via_<left-device>_<right-device>_<side>.uf2
```

**Examples:**

| File | Config |
|---|---|
| `lily58_rev1_via_trackball_tps43_left.uf2` | Lily58, trackball left, TPS43 right |
| `lily58_rev1_via_trackball_tps43_right.uf2` | Same config, right half |
| `lily58_rev1_via_trackball_trackball_left.uf2` | Dual trackball |

---

## 🎮 Flashing & Configuring

### 1. Flash the firmware

1. Download the right `.uf2` from [Releases](https://github.com/alliecatowo/allie-cat-keeb-vial/releases)
2. Enter bootloader mode on your keyboard (double-tap the RESET button)
3. Drag-and-drop the `.uf2` onto the `RPI-RP2` USB drive that appears
4. Repeat for the other half of your split keyboard

### 2. Configure with Vial

1. Download [Vial](https://get.vial.today) (desktop app)
2. Plug in your keyboard — it should be detected automatically
3. Customise in real-time:
   - Key mappings & layers
   - Macros & tap-dance
   - Pointing-device sensitivity
   - RGB lighting

---

## 🛠️ Building from Source

### Prerequisites

```bash
# macOS
brew install qmk/qmk/qmk

# Linux / WSL
sudo apt-get update && sudo apt-get install -y git python3-pip
pip3 install qmk && qmk setup -y
```

### Quick build

```bash
git clone --recurse-submodules https://github.com/alliecatowo/allie-cat-keeb-vial.git
cd allie-cat-keeb-vial

python3 build.py          # builds the default config (trackball left, TPS43 right, both sides)
```

### `build.py` options

```bash
# Single variant
python3 build.py --build-single \
  --keyboard lily58/rev1 \
  --keymap vial \
  --left-device trackball \
  --right-device tps43 \
  --side left

# All variants
python3 build.py --build-all

# Release build (all variants, both sides)
python3 build.py --release

# Validate CI matrix (no ARM toolchain needed)
python3 build.py --generate-matrix-release
```

### Direct `make` command

```bash
make lily58/rev1:via -e USER_NAME=holykeebs \
  -e POINTING_DEVICE=trackball_tps43 \
  -e SIDE=left \
  -e TRACKBALL_RGB_RAINBOW=yes \
  -e VIAL_ENABLE=yes
```

---

## 🔄 CI / GitHub Actions

| Workflow | Triggers | What it does |
|---|---|---|
| **Quick Tests** | Every PR, push to `main` | Python unit tests, linting, matrix validation |
| **Build Firmware** | Version tags (`v*`), manual dispatch | Full ARM firmware build across all configs |
| **Release Drafter** | Push to `main`, PRs | Drafts the next release notes |
| **Sync Upstreams** | Scheduled | Pulls in upstream holykeebs / QMK / Vial-QMK changes |

### Creating a release

```bash
git tag v1.2.0
git push origin v1.2.0
```

The **Build Firmware** workflow fires automatically, cross-compiles every config, and attaches all `.uf2` files to a new GitHub Release.

### Using Actions in your own fork

1. Fork this repository
2. Go to **Settings → Actions** and enable GitHub Actions
3. PRs get automatic test coverage; tag a version to trigger a firmware release build

---

## 🔧 What We Changed

### Vial core integration
- Backported Vial's quantum-layer patches from [vial-qmk](https://github.com/vial-kb/vial-qmk)
- Added Vial-specific keycodes, config structures, and the Vial USB communication protocol

### Build system
- Extended the build system with Vial flags and a Python orchestration script (`build.py`)
- CI matrix generation — `build.py --generate-matrix-release` outputs a JSON matrix consumed directly by GitHub Actions

### Keymap updates
- Updated VIA keymaps to expose Vial's extra configuration options
- Added `.vil` keyboard-definition files for each supported board
- Backwards-compatible with existing VIA layouts

### Memory optimisations
- Trimmed firmware features to keep the image within RP2040 flash constraints while keeping Vial enabled

---

## 📊 Azoteq IQS5xx Driver Call Graph

The touchpad driver dependency graph is generated automatically during CI and committed to the repo:

![Azoteq driver call graph](docs/azoteq_callgraph.svg)

---

## 🚨 Troubleshooting

<details>
<summary><strong>Vial doesn't detect my keyboard</strong></summary>

- Confirm you flashed the Vial-enabled firmware (not the base holykeebs build)
- Try a different USB cable or port
- Make sure **both** halves are flashed for split keyboards
</details>

<details>
<summary><strong>Pointing device not responding</strong></summary>

- Verify you flashed the correct device variant (e.g. `trackball_tps43`, not `trackball_trackball`)
- Check wiring — see [docs.holykeebs.com](https://docs.holykeebs.com)
- Flash the debug build and connect via the QMK console for verbose output
</details>

<details>
<summary><strong>Build fails</strong></summary>

- Make sure you're building from **this fork**, not upstream QMK or holykeebs
- Run `qmk doctor` to validate your environment
- Ensure submodules are initialised: `git submodule update --init --recursive`
</details>

---

## 🤝 Contributing

Contributions are welcome! Adding a new pointing device, improving Vial integration, fixing bugs — all great. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full guide.

Quick steps:

```bash
git checkout -b feat/my-cool-thing
# make changes
git commit -m "feat: describe what you did"
git push origin feat/my-cool-thing
# open a Pull Request
```

We use **conventional commits** (`feat:`, `fix:`, `docs:`, `ci:`, `chore:`, …).

---

## 🤖 Agent / Codex Setup

Automating or running in a CI-like shell? See [AGENTS.md](AGENTS.md) for environment bootstrap steps. Quick version:

```bash
export ORIG_CWD="$PWD" QMK_HOME="$PWD" QMK_FIRMWARE="$PWD" PYTHONPATH="$PWD/lib/python"
export PATH="$PWD/bin:$PATH"
python3 -m pip install -r requirements-dev.txt

# Smoke test (no ARM toolchain needed)
python3 -m unittest tests.test_build_py -v
```

---

## 📚 Resources

| Link | Description |
|---|---|
| [Holykeebs Store](https://holykeebs.com) | Hardware — trackballs, touchpads, trackpoints |
| [Holykeebs Docs](https://docs.holykeebs.com) | Installation and wiring guides |
| [Holykeebs QMK repo](https://github.com/idank/qmk_firmware) | Upstream source (branch: `holykeebs-master`) |
| [Vial](https://get.vial.today) | Real-time keyboard configurator |
| [QMK Docs](https://docs.qmk.fm) | Full QMK firmware reference |
| [Releases](https://github.com/alliecatowo/allie-cat-keeb-vial/releases) | Pre-built `.uf2` firmware files |

---

## 🙏 Acknowledgments

- **[idank](https://github.com/idank)** — Creator of the holykeebs firmware and hardware ecosystem
- **[Vial contributors](https://github.com/vial-kb/vial-qmk)** — For the real-time configuration magic
- **[QMK community](https://qmk.fm)** — For the incredible open-source firmware foundation
- **All contributors** — Everyone who opens PRs, files issues, and tests firmware 🐾

---

## 📄 License

GPL-2.0-or-later — same terms as QMK firmware. See [LICENSE](LICENSE) for details.

---

<div align="center">

**[Get Hardware](https://holykeebs.com)** • **[Documentation](https://docs.holykeebs.com)** • **[Releases](https://github.com/alliecatowo/allie-cat-keeb-vial/releases)** • **[Report a Bug](https://github.com/alliecatowo/allie-cat-keeb-vial/issues)**

Made with ❤️ for the mechanical keyboard community 🐾

</div>
