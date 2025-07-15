# Holykeebs Driver Modifications

This section details the specific modifications and enhancements introduced by Holykeebs to various pointing device drivers within this QMK firmware fork. These modifications enable advanced functionality and support for a wider range of pointing devices.

## Azoteq IQS5xx (Touchpad)

The Azoteq IQS5xx driver (`drivers/sensors/azoteq_iqs5xx.c`) has been extended to support various configurations of Azoteq touchpads, including the TPS43 and TPS65. Key modifications include:

*   **Customizable Gestures**: Enhanced gesture recognition for single and multi-finger interactions (tap, press and hold, swipe, scroll, zoom).
*   **Report Rate Control**: Ability to configure the report rate for different power modes.
*   **Coordinate Flipping and Switching**: Options for flipping X/Y coordinates and switching X/Y axes to accommodate various physical orientations.
*   **Palm Rejection**: Implementation of palm rejection to prevent accidental inputs.

Here's the call graph for the Azoteq driver:
![Azoteq Call Graph](/azoteq_callgraph.svg)

## Pimoroni Trackball

The Pimoroni Trackball driver (`drivers/sensors/pimoroni_trackball.c`) includes Holykeebs modifications primarily for advanced control and configuration of the trackball's behavior.

*   **Customizable CPI (Counts Per Inch)**: Allows for runtime adjustment of trackball sensitivity, even though the sensor itself doesn't directly support CPI changes. This is achieved through software scaling.
*   **RGBW LED Control**: Direct control over the RGBW LEDs integrated into the Pimoroni trackball.
*   **Debounce and Error Handling**: Improved debouncing for button presses and robust error handling for I2C communication.

Here's the call graph for the Pimoroni Trackball driver:
![Pimoroni Call Graph](/pimoroni_callgraph.svg)

## Cirque Pinnacle (Trackpad)

The Cirque Pinnacle driver (`drivers/sensors/cirque_pinnacle.c`) has been adapted to support various Cirque trackpads, focusing on robust data handling and configuration.

*   **Logical Scaling**: Functions to clip and scale raw coordinates to a desired resolution.
*   **Extended Register Access (ERA)**: Provides mechanisms for reading and writing to extended registers, allowing for fine-grained control over sensor behavior.
*   **ADC Attenuation**: Configuration options for ADC attenuation to improve finger detection.
*   **Calibration and Smoothing**: Functions for sensor calibration and cursor smoothing.
*   **Cursor Glide**: Support for cursor glide functionality.

Here's the call graph for the Cirque Pinnacle driver:
![Cirque Call Graph](/cirque_callgraph.svg)

## PS2 Trackpoint

The PS2 Mouse driver (`drivers/ps2/ps2_mouse.c`) is used to interface with PS2 trackpoint modules. Holykeebs modifications enhance its integration within the QMK framework, particularly for dual-pointing device setups.

*   **Pimoroni Trackball Compatibility**: Includes a debounce mechanism to prevent conflicts when a Pimoroni trackball is also present.
*   **Register Read/Write**: Functions to read from and write to PS2 mouse registers, enabling advanced configuration of trackpoint behavior.
*   **HID Report Conversion**: Ensures seamless conversion of PS2 mouse reports to HID reports for host communication.

Here's the call graph for the PS2 Trackpoint driver:
![Trackpoint Call Graph](/trackpoint_callgraph.svg)

## Contributing to Driver Modifications

If you're interested in contributing to these driver modifications or adding support for new pointing devices, please refer to our [Contributing Guide](/guide/contributing.md).

# Holykeebs Custom Pointer Features

Beyond the base driver modifications, this firmware includes a set of custom features and keycodes, often referred to as "hk values," that enhance the functionality of pointing devices. These features are designed to provide a more tailored and flexible user experience, accessible without the need to reflash your keyboard for every adjustment. This information is derived from the [Holykeebs Documentation on Firmware](https://docs.holykeebs.com/firmware/).

## Core Pointer Features

These features streamline pointing device usage and are controlled via a collection of special keycodes. The default `hk` keymap often provides a pre-configured `POINTER` layer to utilize these functionalities.

*   **Scaled Movement**: Transforms the X/Y movement read from the pointing device. This is useful for adjusting sensitivity for large screens or when fine-grained movement is required. It supports two modes: a default scale and a secondary "sniping" scale.
*   **Sniping Mode**: A secondary scale profile that can be applied to a pointing device, typically using a smaller multiplier for finer, more precise movement (e.g., for pixel-perfect adjustments).
*   **Drag Scroll Mode**: Converts pointing device movements into scrolling actions, allowing you to "drag" the mouse to scroll through content.
*   **Buffered Scroll**: Slows down scrolling by buffering a specified amount of movement before sending a scroll event to the host, providing more controlled scrolling.
*   **Scroll Lock**: Constrains scrolling to either the horizontal or vertical axis.

## OLED Display Integration

For keyboards equipped with an OLED display and a pointing device, the screen can show dynamic information related to these features, including:

*   Last pressed key and any currently held keys.
*   Current pointing device type (or NONE) and recent X/Y/V/H movements.
*   Current pointing profile (D for default, S for sniping).
*   Current scaling multiplier, scroll buffer size, drag scroll mode status, and scroll lock status.
*   Active layers and whether automatic mouse layer is enabled.

## Custom Keycodes (HK Values)

The following keycodes allow direct control over the custom pointer features. These can be assigned to your keymap layers.

| Keycode         | VIA Code | Description                                                               |
| :-------------- | :------- | :------------------------------------------------------------------------ |
| `HK_RESET`      | `0x7e00` | Resets the configuration to its default state                             |
| `HK_SAVE`       | `0x7e01` | Saves the current configuration, making it persist across keyboard restarts |
| `HK_DUMP`       | `0x7e02` | Dumps the current configuration to the console (requires `CONSOLE_ENABLE=yes`) |
| `HK_P_SET_D`    | `0x7e03` | When held, tapping `Up`/`Down` increases/decreases the default profile's scale |
| `HK_P_SET_S`    | `0x7e04` | When held, tapping `Up`/`Down` increases/decreases the sniping profile's scale |
| `HK_P_SET_BUF`  | `0x7e05` | When held, pressing `Up`/`Down` increases/decreases the scroll buffer    |
| `HK_S_MODE`     | `0x7e06` | When held, enables sniping mode                                           |
| `HK_S_MODE_T`   | `0x7e07` | Toggles sniping mode                                                      |
| `HK_D_MODE`     | `0x7e08` | When held, enables drag scroll                                            |
| `HK_D_MODE_T`   | `0x7e09` | Toggles drag scroll                                                       |
| `HK_C_SCROLL`   | `0x7e0a` | Cycles the scroll lock between off, horizontal, and vertical            |

*Note: Holding `Shift` while using any config keycode that needs to be held will affect the peripheral pointing device.*

## Debugging Custom Features

To view the internal state of these custom features, especially without an OLED, you can enable debug mode. Set `CONSOLE_ENABLED=yes` in `users/holykeebs/rules.mk` (or your keyboard's `rules.mk`). Then, run `qmk console` and use the `HK_DUMP` keycode to print the current configuration to the console. This is invaluable for tuning and troubleshooting. 
