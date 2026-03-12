# Pointing Device Support

This repo's keymaps use the [holykeebs](users/holykeebs/) QMK userspace for
advanced pointing device management. Below is a reference for supported hardware
and configuration options.

## Supported Sensors

| Sensor | Driver | Notes |
|--------|--------|-------|
| **Pimoroni Trackball** | `pimoroni_trackball` | I2C, RGB ball. Most tested with Lily58+holykeebs setups. |
| **Cirque Pinnacle 35mm** | `cirque_pinnacle_spi` / `_i2c` | Circular touchpad. Supports tap + gesture. |
| **Cirque Pinnacle 40mm** | `cirque_pinnacle_spi` / `_i2c` | Larger circular touchpad. Same driver. |
| **Azoteq IQS5xx** | `azoteq_iqs5xx` | Capacitive multi-touch (2-finger). Advanced gesture support. |
| **PMW3320** | `pmw3320` | Optical sensor, low-profile builds. |
| **PMW3360 / PMW33xx** | `pmw3360` | High-DPI optical, popular in gaming mice. |
| **TrackPoint** | `ps2mouse` (custom) | IBM-style isometric stick. |

---

## Configuration Quick Reference

### Step 1 — Enable in `rules.mk`

```makefile
POINTING_DEVICE_ENABLE = yes
POINTING_DEVICE_DRIVER = pimoroni_trackball   # swap to your driver

# For two sensors (one per half):
POINTING_DEVICE_COMBINED = yes
```

### Step 2 — `config.h`

```c
// Required: which half has the master controller
#define HK_MASTER_LEFT   // or HK_MASTER_RIGHT

// Tell holykeebs which sensor type(s)
#define HK_POINTING_DEVICE_RIGHT_PIMORONI   // right-side Pimoroni
// or HK_POINTING_DEVICE_LEFT_CIRQUE35, HK_POINTING_DEVICE_LEFT_CIRQUE40, etc.
```

---

## Cirque Pinnacle — Tap & Gesture

```c
// config.h
#define CIRQUE_PINNACLE_TAP_ENABLE              // 1-finger tap = left click
#define CIRQUE_PINNACLE_CIRCULAR_SCROLL_ENABLE  // 1-finger circle = scroll
#define CIRQUE_PINNACLE_SECONDARY_TAP_ENABLE    // 2-finger tap = right click (if supported)
```

> **Note:** `CIRQUE_PINNACLE_CIRCULAR_SCROLL_ENABLE` and per-axis scroll lock
> (`HK_C_SCROLL`) do not conflict — scroll lock acts as an output filter after
> the gesture is detected.

---

## POINTING_DEVICE_COMBINED — Dual Sensor Setup

Enables independent processing of left and right trackballs/pads.

```c
// config.h
#define POINTING_DEVICE_COMBINED
#define POINTING_DEVICE_TASK_THROTTLE_MS 1  // keep fast for Pimoroni
```

```makefile
# rules.mk
POINTING_DEVICE_COMBINED = yes
```

The holykeebs userspace tracks both `g_hk_state.main` and `g_hk_state.peripheral`
states separately. The split sync (`HK_SPLIT_SYNC_STATE`) mirrors peripheral state
over the USART link so both sides can be controlled from the master.

To apply an HK_* keycode to the peripheral side, hold `Shift` while pressing it.

---

## Default Scalers

Scaling is stored in EEPROM (persisted with `HK_SAVE`).

| Setting | Default | Notes |
|---------|---------|-------|
| Default speed | 1.0× | Adjusted with `HK_P_SET_D` + `+`/`-` |
| Sniping speed | 0.25× | Adjusted with `HK_P_SET_S` + `+`/`-` |
| Scroll buffer | 8 | Adjusted with `HK_P_SET_BUF` + `+`/`-`. Higher = less sensitive scroll. |

---

## Recommended Keymap Placement

Put pointing device controls on the `_NAV` or `_SYS` layer:

```c
// In your _NAV or _SYS layer:
HK_S_MODE_T,     // toggle sniping
HK_D_MODE_T,     // toggle drag-scroll
HK_C_SCROLL,     // cycle scroll lock axis
HK_SAVE,         // persist settings
```

---

See [users/holykeebs/README.md](users/holykeebs/README.md) for full HK_* keycode
documentation.
