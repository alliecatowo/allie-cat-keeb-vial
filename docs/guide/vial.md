# Vial Integration

Vial is an open-source, community-driven keymap configurator that allows for real-time keymap editing without reflashing your keyboard. This document explains how Vial is integrated into this firmware and how to use it.

## What is Vial?

Vial is a powerful tool for keyboard enthusiasts. Unlike traditional QMK firmware, where you need to recompile and reflash your keyboard every time you make a change to your keymap, Vial allows you to make changes on the fly. This includes:

*   **Real-time Keymap Editing**: Change key assignments instantly.
*   **Macro Editing**: Create and modify macros without recompiling.
*   **Lighting Control**: Adjust RGB lighting effects and colors.
*   **Encoder Configuration**: Customize rotary encoder behavior.
*   **QMK Features**: Access most standard QMK features through the Vial client.

## Building Vial Firmware

To build a Vial-compatible firmware for your keyboard, you can use the `build.py` script with the `--vial-only` flag. This will compile a firmware with Vial support enabled.

```bash
.venv/bin/python3 build.py --vial-only
```

This command will generate `.uf2` files (or other appropriate firmware formats) in the `.build/` directory that are compatible with the Vial configurator application.

## Flashing Vial Firmware

Flashing a Vial firmware is similar to flashing any other QMK firmware. You will need to put your keyboard into bootloader mode and then use a flashing tool (like `qmk toolbox` or `uf2-util` for UF2 files) to flash the generated firmware. Once flashed, your keyboard should be recognized by the Vial client.

For detailed flashing instructions, please refer to the [QMK Firmware Flashing Guide](https://docs.qmk.fm/#/newbs_flashing).

## Using the Vial Client

Once your Vial-compatible firmware is flashed, you can download and run the Vial client application. The client will automatically detect your keyboard and allow you to configure its keymap, lighting, and other features in real-time.

*   **Download Vial Client**: [get.vial.today](https://get.vial.today/)

## Updating Vial (and QMK) Dependencies

This fork periodically updates its QMK and Vial dependencies to ensure compatibility and incorporate the latest features and bug fixes from upstream. This helps in maintaining a stable and feature-rich firmware for your keyboards. If you're experiencing issues, ensure you have the latest version of this repository and rebuild your firmware. 
