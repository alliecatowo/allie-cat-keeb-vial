<<<<<<< HEAD
=======
# Allie Cat Keeb - QMK Firmware

This repository contains QMK firmware for the Lily58 keyboard with support for various pointing devices including trackball, TPS43 touchpad, and trackpoint modules.

## Pre-built Firmware

The latest pre-built firmware for the trackball/TPS43 configuration is available in the [Releases](https://github.com/alliecatowo/allie-cat-keeb/releases) section. Download the appropriate `.uf2` file for your keyboard half (left or right).

## Building Your Own Firmware

### Important: Fork Requirements

**⚠️ You MUST build from a fork of this repository or the holykeebs repository, NOT from the base QMK firmware.**

The base QMK firmware does not include the necessary drivers and support for the holykeebs pointing devices (trackpoint, TPS43, etc.). This repository includes:
- Holykeebs userspace with pointing device support
- PS2 driver support for trackpoint
- Azoteq IQS5xx driver for TPS43 touchpad
- Pimoroni trackball support
- Custom configurations for dual pointing devices

### Prerequisites

1. Fork this repository to your GitHub account
2. Clone your fork locally:
   ```bash
   git clone --recurse-submodules git@github.com:YOUR_USERNAME/allie-cat-keeb.git
   cd allie-cat-keeb
   ```

3. Install QMK dependencies:
   ```bash
   # macOS
   brew install qmk/qmk/qmk
   
   # Linux/WSL
   sudo apt-get update
   sudo apt-get install -y build-essential avr-libc binutils-arm-none-eabi \
     binutils-avr dfu-programmer dfu-util gcc-arm-none-eabi gcc-avr git \
     libnewlib-arm-none-eabi unzip wget zip python3-pip
   pip3 install qmk
   ```

### Building Firmware

The repository includes a `build.py` script that simplifies building firmware with various configurations.

#### Build the default trackball/TPS43 configuration:
```bash
python build.py
```

This will build firmware for both halves of the keyboard with:
- Left side: Pimoroni trackball
- Right side: TPS43 touchpad

#### Build a specific configuration:
```bash
python build.py --build-single \
  --keyboard lily58/rev1 \
  --keymap via \
  --left-device trackball \
  --right-device tps43 \
  --side left
```

Available devices:
- `trackball` - Pimoroni trackball module
- `tps43` - Azoteq IQS5xx TPS43 touchpad
- `trackpoint` - PS2 trackpoint module
- `oled` - OLED display
- `None` - No device

### Manual Build Commands

If you prefer to use QMK make commands directly:

```bash
# Single pointing device (trackball on left)
make lily58/rev1:via -e USER_NAME=holykeebs \
  -e POINTING_DEVICE=trackball \
  -e POINTING_DEVICE_POSITION=left \
  -e TRACKBALL_RGB_RAINBOW=yes

# Dual pointing devices (trackball left, TPS43 right)
# Build left half:
make lily58/rev1:via -e USER_NAME=holykeebs \
  -e POINTING_DEVICE=trackball_tps43 \
  -e SIDE=left \
  -e TRACKBALL_RGB_RAINBOW=yes

# Build right half:
make lily58/rev1:via -e USER_NAME=holykeebs \
  -e POINTING_DEVICE=trackball_tps43 \
  -e SIDE=right
```

### Flashing

1. Connect the keyboard half to your computer
2. Enter bootloader mode:
   - Double-tap the reset button on the keyboard
   - Or hold BOOT and press RESET on the controller
3. A drive named `RPI-RP2` should appear
4. Copy the appropriate `.uf2` file to the drive
5. The drive will disappear and the keyboard will restart
6. Repeat for the other half

### Customizing Your Keymap

1. Copy an existing keymap:
   ```bash
   cp -r keyboards/lily58/keymaps/via keyboards/lily58/keymaps/YOUR_NAME
   ```

2. Edit `keyboards/lily58/keymaps/YOUR_NAME/keymap.c` to customize your layout

3. Build with your keymap:
   ```bash
   python build.py --keymap YOUR_NAME
   ```

### Troubleshooting

- **Build fails with "Invalid POINTING_DEVICE_DRIVER"**: Make sure you're building from this repository or holykeebs, not base QMK
- **Trackpoint not working**: Ensure PS2 support is enabled in the firmware
- **Rainbow effect errors**: The trackball RGB rainbow effect requires a Pimoroni trackball on either side

## License

This firmware is based on QMK and includes modifications from holykeebs. See the QMK license for details.

>>>>>>> c229afda3e
# alliecatowo/qmk_firmware Fork

This is my personal fork of QMK firmware for tinkering with my lily58 keyboard.

## Branch Structure

-   **main**: Kept in sync with upstream.
-   **develop**: Primary development branch for my custom lily58 keymaps and features. All work is done here.
-   **hk-master**: A mirror of the `holykeebs-master` branch for reference and easier rebasing.

## Automated Firmware Builds

This repository is configured with a GitHub Actions workflow to automatically build lily58 firmware.

### Workflow Triggers

The build process is automatically triggered on:

-   **Pull requests** targeting the `main` branch.
-   **Pushes of tags** matching the `v*` pattern (e.g., `v1.0`, `v1.1`).
-   **Manual triggers** from the GitHub Actions tab (`workflow_dispatch`).

This ensures that builds are only run when preparing a release, keeping resource usage to a minimum.

### Build Script

The builds are orchestrated by the `build_lily.py` script. You can also run this script locally to build firmware without relying on the GitHub Actions workflow.

`python3 build_lily.py`

This will generate the defined firmware variations and place them in the `build_lily/` directory.

## Upstream Documentation

-   [QMK official documentation](https://docs.qmk.fm)
-   [holykeebs/qmk_firmware](https://github.com/holykeebs/qmk_firmware#readme)

# Quantum Mechanical Keyboard Firmware

[![Current Version](https://img.shields.io/github/tag/qmk/qmk_firmware.svg)](https://github.com/qmk/qmk_firmware/tags)
[![Discord](https://img.shields.io/discord/440868230475677696.svg)](https://discord.gg/qmk)
[![Docs Status](https://img.shields.io/badge/docs-ready-orange.svg)](https://docs.qmk.fm)
[![GitHub contributors](https://img.shields.io/github/contributors/qmk/qmk_firmware.svg)](https://github.com/qmk/qmk_firmware/pulse/monthly)
[![GitHub forks](https://img.shields.io/github/forks/qmk/qmk_firmware.svg?style=social&label=Fork)](https://github.com/qmk/qmk_firmware/)

This is a keyboard firmware based on the [tmk\_keyboard firmware](https://github.com/tmk/tmk_keyboard) with some useful features for Atmel AVR and ARM controllers, and more specifically, the [OLKB product line](https://olkb.com), the [ErgoDox EZ](https://ergodox-ez.com) keyboard, and the Clueboard product line.

## Documentation

* [See the official documentation on docs.qmk.fm](https://docs.qmk.fm)

The docs are powered by [VitePress](https://vitepress.dev/). They are also viewable offline; see [Previewing the Documentation](https://docs.qmk.fm/#/contributing?id=previewing-the-documentation) for more details.

You can request changes by making a fork and opening a [pull request](https://github.com/qmk/qmk_firmware/pulls).

## Supported Keyboards

* [Planck](/keyboards/planck/)
* [Preonic](/keyboards/preonic/)
* [ErgoDox EZ](/keyboards/ergodox_ez/)
* [Clueboard](/keyboards/clueboard/)
* [Cluepad](/keyboards/clueboard/17/)
* [Atreus](/keyboards/atreus/)

The project also includes community support for [lots of other keyboards](/keyboards/).

## Maintainers

QMK is developed and maintained by Jack Humbert of OLKB with contributions from the community, and of course, [Hasu](https://github.com/tmk). The OLKB product firmwares are maintained by [Jack Humbert](https://github.com/jackhumbert), the Ergodox EZ by [ZSA Technology Labs](https://github.com/zsa), the Clueboard by [Zach White](https://github.com/skullydazed), and the Atreus by [Phil Hagelberg](https://github.com/technomancy).

## Official Website

[qmk.fm](https://qmk.fm) is the official website of QMK, where you can find links to this page, the documentation, and the keyboards supported by QMK.
