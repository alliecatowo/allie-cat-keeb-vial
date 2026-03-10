# users/alliecatowo

Primary QMK userspace for `allie-cat-keeb-vial`.

This directory now contains the full pointing-device userspace that was
previously built from `users/holykeebs/`. Builds should prefer
`USER_NAME=alliecatowo`.

---

## Files

| File | Purpose |
|------|---------|
| `config.h` / `rules.mk` | Main userspace entrypoints loaded by `USER_NAME=alliecatowo` |
| `holykeebs.h` | HK_* keycodes and userspace declarations |
| `pointing_device_config.h` | Unified standalone pointing-device selector header (ALLIE-202) |

---

## pointing_device_config.h — Multi-Device Abstraction

A single include file that translates a high-level sensor selector
(`HK_POINTING_*`) into the appropriate QMK `POINTING_DEVICE_DRIVER` and
gesture config defines.

### Quick Start

1. Add to your keyboard's `config.h`:

   ```c
   // Pick ONE sensor:
   #define HK_POINTING_CIRQUE_SPI   // or I2C, PIMORONI, PMW3320, PMW3360, AZOTEQ

   #include "users/alliecatowo/pointing_device_config.h"
   ```

2. Add to `rules.mk`:

   ```makefile
   POINTING_DEVICE_ENABLE = yes
   # driver is set automatically by the header, but must also appear in rules.mk:
   POINTING_DEVICE_DRIVER = cirque_pinnacle_spi  # match your selector
   ```

### Supported Selectors

| Define | Sensor | Interface | Gestures |
|--------|--------|-----------|----------|
| `HK_POINTING_PIMORONI` | Pimoroni Trackball (PMW3360) | I2C | — |
| `HK_POINTING_CIRQUE_SPI` | Cirque Pinnacle | SPI | tap-to-click, circular scroll |
| `HK_POINTING_CIRQUE_I2C` | Cirque Pinnacle | I2C | tap-to-click, circular scroll |
| `HK_POINTING_PMW3320` | PMW3320 optical | SPI | — |
| `HK_POINTING_PMW3360` | PMW3360 optical | SPI | — |
| `HK_POINTING_AZOTEQ` | Azoteq IQS5xx | I2C | tap, 2-finger tap, scroll, hold |

### Relationship with the main userspace

If you are using `USER_NAME=alliecatowo` with `POINTING_DEVICE=cirque40`
(or any other supported sensor variable) in `rules.mk`, the main userspace
already handles config for you — you do **not** need to include
`pointing_device_config.h`.

This header is for standalone builds or for quickly switching sensors
without modifying `rules.mk` at the make invocation level.

---

See [POINTING_DEVICE.md](../../POINTING_DEVICE.md) at the repo root for
the full sensor comparison and wiring guide.
