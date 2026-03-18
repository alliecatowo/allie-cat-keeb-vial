# Pointing Device Guide

Comprehensive reference for all supported pointing devices in `allie-cat-keeb-vial`.

> **TL;DR** — Use the alliecatowo userspace (`users/alliecatowo`) for the easiest
> setup.  Set `POINTING_DEVICE=<type>` and `POINTING_DEVICE_POSITION=<side>`
> in `rules.mk` and everything else is handled automatically.

---

## Sensor Comparison

| Sensor | Driver | Interface | Gestures | Form factor |
|--------|--------|-----------|----------|-------------|
| **Pimoroni Trackball** | `pimoroni_trackball` | I2C | — (scroll via drag-scroll key) | Ball, RGB |
| **Cirque Pinnacle 35mm** | `cirque_pinnacle_i2c` / `_spi` | I2C or SPI | tap, circular scroll | Circular pad |
| **Cirque Pinnacle 40mm** | `cirque_pinnacle_i2c` / `_spi` | I2C or SPI | tap, circular scroll | Circular pad |
| **Azoteq IQS5xx (TPS43)** | `azoteq_iqs5xx` | I2C | tap, 2-finger tap, scroll, press+hold | Rectangular pad |
| **PMW3320** | `pmw3320` | SPI | — | Optical chip |
| **PMW3360** | `pmw3360` | SPI | — | Optical chip, high-DPI |
| **TrackPoint** | `ps2` (PS/2 via PIO) | PS/2 | — | Isometric stick |

---

## Quick Setup — alliecatowo Userspace (Recommended)

### 1. Set sensor in `rules.mk`

```makefile
# Single sensor
POINTING_DEVICE          = cirque40          # or: cirque35, trackball, tps43, trackpoint, pmw3320
POINTING_DEVICE_POSITION = right             # or: left, thumb, thumb_inner, thumb_outer, middle
```

Valid `POINTING_DEVICE` values:

| Value | Sensor |
|-------|--------|
| `trackball` | Pimoroni Trackball |
| `cirque35` | Cirque Pinnacle 35mm |
| `cirque40` | Cirque Pinnacle 40mm |
| `tps43` | Azoteq IQS5xx (TPS43) |
| `trackpoint` | TrackPoint (PS/2) |

**Dual sensor** (one per half — `POINTING_DEVICE_COMBINED`):

```makefile
POINTING_DEVICE = trackball_cirque40   # left=trackball, right=Cirque40
SIDE            = right                # which half you are flashing
```

See `users/alliecatowo/rules.mk` for all 28 valid dual-sensor combinations.

### 2. No config.h changes needed

The alliecatowo `config.h` automatically sets `CIRQUE_PINNACLE_TAP_ENABLE`,
`POINTING_DEVICE_GESTURES_SCROLL_ENABLE`, diameter, rotation, and throttle
based on the `POINTING_DEVICE` variable you set.

---

## Standalone Setup (no alliecatowo userspace)

### Option A — using `users/alliecatowo/pointing_device_config.h`

```c
// In your keyboard's config.h:
#define HK_POINTING_CIRQUE_SPI   // see below for all selectors

#include "users/alliecatowo/pointing_device_config.h"
```

```makefile
# In rules.mk:
POINTING_DEVICE_ENABLE = yes
POINTING_DEVICE_DRIVER = cirque_pinnacle_spi
```

Available selectors:

| Define | Sensor |
|--------|--------|
| `HK_POINTING_PIMORONI` | Pimoroni Trackball |
| `HK_POINTING_CIRQUE_SPI` | Cirque Pinnacle (SPI) |
| `HK_POINTING_CIRQUE_I2C` | Cirque Pinnacle (I2C) |
| `HK_POINTING_PMW3320` | PMW3320 optical |
| `HK_POINTING_PMW3360` | PMW3360 optical |
| `HK_POINTING_AZOTEQ` | Azoteq IQS5xx |

### Option B — manual config

```makefile
# rules.mk
POINTING_DEVICE_ENABLE = yes
POINTING_DEVICE_DRIVER = cirque_pinnacle_spi
```

```c
// config.h
#define CIRQUE_PINNACLE_DIAMETER_MM     40   // 35 or 40 mm
#define CIRQUE_PINNACLE_TAP_ENABLE           // 1-finger tap = left click
#define CIRQUE_PINNACLE_CIRCULAR_SCROLL_ENABLE  // ring drag = scroll
#define POINTING_DEVICE_SCROLL_DIVISOR_H 8
#define POINTING_DEVICE_SCROLL_DIVISOR_V 8
```

---

## Cirque Pinnacle — Gesture Reference (ALLIE-201)

### Tap-to-Click

Enabled by `CIRQUE_PINNACLE_TAP_ENABLE`.

| Gesture | Action |
|---------|--------|
| 1-finger tap | Left click |
| Corner tap (if `CIRQUE_PINNACLE_SECONDARY_TAP_ENABLE`) | Right click |

Tap timing is tuned with:

```c
#define CIRQUE_PINNACLE_TAPPING_TERM   200  // ms, default
#define CIRQUE_PINNACLE_TOUCH_DEBOUNCE 25   // ms, default
```

### Circular Scroll

Enabled by `CIRQUE_PINNACLE_CIRCULAR_SCROLL_ENABLE`.

Draw a circle near the edge of the pad to generate scroll events.
Clockwise = scroll down / right.  Counter-clockwise = scroll up / left.

> Requires absolute (position) mode — automatically enabled when
> `CIRQUE_PINNACLE_TAP_ENABLE` is defined.

Tune the scroll zone with:

```c
// Percentage of the radius that counts as the scroll ring (default: 30)
// #define CIRQUE_PINNACLE_CIRCULAR_SCROLL_OUTER_RING_PCT 30
```

### Scroll axis lock

`HK_C_SCROLL` (from `users/alliecatowo`) cycles through: off → horizontal only →
vertical only.  Works as an output filter on top of circular scroll — they
don't conflict.

---

## Azoteq IQS5xx — Gesture Reference

The IQS5xx driver supports true multi-touch (up to 5 simultaneous contacts).

| Gesture | Default | Config define |
|---------|---------|---------------|
| 1-finger tap | enabled | `AZOTEQ_IQS5XX_TAP_ENABLE` |
| 2-finger tap (right-click) | enabled | `AZOTEQ_IQS5XX_TWO_FINGER_TAP_ENABLE` |
| 2-finger scroll | enabled | `AZOTEQ_IQS5XX_SCROLL_ENABLE` |
| Press and hold | enabled* | `AZOTEQ_IQS5XX_PRESS_AND_HOLD_ENABLE` |

*Press-and-hold is disabled in the QMK default but enabled in the alliecatowo userspace.

---

## Pimoroni Trackball — Non-Linear Scaling

The Pimoroni trackball supports adaptive non-linear scaling implemented in
`users/alliecatowo/pimoroni.c`.  Enable it with:

```c
// In users/alliecatowo/holykeebs.h (or your own userspace):
#define ENABLE_PIMORONI_ADAPTIVE_MOTION
```

The scaler uses an exponential moving average so slow movements stay precise
and fast flicks accelerate.  Tune the constants in `pimoroni.c`:

```c
#define MAX_SCALE     32    // maximum multiplier
#define MIN_SCALE      1    // minimum multiplier
#define GROWTH_FACTOR 64    // how steeply the curve rises
#define MOMENTUM    0.01f   // EMA smoothing (smaller = smoother but slower)
```

---

## HK_* Keycodes (Runtime Tuning)

Place these on your `_NAV` or `_SYS` layer:

| Keycode | Action |
|---------|--------|
| `HK_S_MODE_T` | Toggle sniping mode (slow, precise) |
| `HK_D_MODE_T` | Toggle drag-scroll (move → scroll) |
| `HK_C_SCROLL` | Cycle scroll axis lock: off / H / V |
| `HK_P_SET_D` + `+`/`-` | Increase/decrease default speed scaler |
| `HK_P_SET_S` + `+`/`-` | Increase/decrease sniping speed scaler |
| `HK_P_SET_BUF` + `+`/`-` | Increase/decrease scroll buffer |
| `HK_SAVE` | Persist current settings to EEPROM |
| `HK_RESET` | Reset HK settings to defaults |

Hold `Shift` while pressing any `HK_*` key to target the peripheral half
(in `POINTING_DEVICE_COMBINED` setups).

---

## Dual Sensor (`POINTING_DEVICE_COMBINED`)

When using two sensors (one per half) you must build each side separately:

```bash
make lily58/rev1:vial POINTING_DEVICE=trackball_cirque40 SIDE=left
make lily58/rev1:vial POINTING_DEVICE=trackball_cirque40 SIDE=right
```

The alliecatowo RPC layer (`users/alliecatowo/rpc.c`) syncs the peripheral side's
state to the master over USART so both sides can be tuned from the master.

---

## Rotation

| Define | Rotation |
|--------|---------|
| `POINTING_DEVICE_ROTATION_90` | 90° CW |
| `POINTING_DEVICE_ROTATION_180` | 180° |
| `POINTING_DEVICE_ROTATION_270` | 270° CW (= 90° CCW) |

For `POINTING_DEVICE_COMBINED`, suffix with `_RIGHT` or `_LEFT`:

```c
#define POINTING_DEVICE_ROTATION_90_RIGHT
```

---

## Related Files

| File | Purpose |
|------|---------|
| `users/alliecatowo/config.h` | Main pointing device config |
| `users/alliecatowo/rules.mk` | POINTING_DEVICE build system |
| `users/alliecatowo/holykeebs.h` | HK_* keycode enum |
| `users/alliecatowo/pimoroni.c` | Non-linear Pimoroni scaling |
| `users/alliecatowo/pointing_device_config.h` | Standalone multi-sensor abstraction (ALLIE-202) |
| `keyboards/lily58/keymaps/vial/config.h` | Vial keymap — Cirque gesture config reference (ALLIE-201) |
| `drivers/sensors/cirque_pinnacle_gestures.c` | Tap + circular scroll implementation |
| `drivers/sensors/azoteq_iqs5xx.c` | IQS5xx multi-touch implementation |
| `POINTING_DEVICE_README.md` | Legacy README (still valid) |
