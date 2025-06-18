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
