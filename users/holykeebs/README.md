# holykeebs QMK Userspace

Pointing device abstraction layer for QMK keyboards. Supports multiple sensor types,
dual-device configurations, sniping, drag-scroll, and configurable scaling.

## HK_* Keycodes

| Keycode | Alias | Description |
|---------|-------|-------------|
| `HK_SAVE_SETTINGS` | `HK_SAVE` | Persist current config to EEPROM |
| `HK_RESET_SETTINGS` | `HK_RESET` | Reset config to firmware defaults (not full EEPROM clear) |
| `HK_DUMP_SETTINGS` | `HK_DUMP` | Print config to console (requires `CONSOLE_ENABLE`) |
| `HK_POINTER_SET_DEFAULT_SCALER` | `HK_P_SET_D` | Hold + press `+`/`-` to adjust default movement speed |
| `HK_POINTER_SET_SNIPING_SCALER` | `HK_P_SET_S` | Hold + press `+`/`-` to adjust sniping speed |
| `HK_POINTER_SET_SCROLL_BUFFER` | `HK_P_SET_BUF` | Hold + press `+`/`-` to adjust scroll threshold |
| `HK_SNIPING_MODE` | `HK_S_MODE` | Hold to enter sniping (precision) mode |
| `HK_SNIPING_MODE_TOGGLE` | `HK_S_MODE_T` | Toggle sniping mode |
| `HK_DRAGSCROLL_MODE` | `HK_D_MODE` | Hold to translate pointer movement into scroll |
| `HK_DRAGSCROLL_MODE_TOGGLE` | `HK_D_MODE_T` | Toggle drag-scroll mode |
| `HK_CYCLE_SCROLL_LOCK` | `HK_C_SCROLL` | Cycle scroll axis lock: off → horizontal → vertical |

### Notes on dual-device (POINTING_DEVICE_COMBINED)

All HK_* keycodes above apply to the **main side** by default.
Hold `Shift` while pressing them to apply the action to the **peripheral side**.

## Sensor Configuration

Set sensor type in your keymap's `rules.mk`:

```makefile
# Pick one for right side (or left, depending on HK_MASTER_LEFT/RIGHT):
POINTING_DEVICE_DRIVER = pimoroni_trackball   # Pimoroni trackball
POINTING_DEVICE_DRIVER = cirque_pinnacle_spi  # Cirque Pinnacle (SPI)
POINTING_DEVICE_DRIVER = cirque_pinnacle_i2c  # Cirque Pinnacle (I2C)
POINTING_DEVICE_DRIVER = pmw3360              # PMW3360 optical
POINTING_DEVICE_DRIVER = pmw3320              # PMW3320 optical
```

And in your keymap's `config.h`:

```c
// Required: declare which side has the master controller
#define HK_MASTER_LEFT   // or HK_MASTER_RIGHT

// Optional: adjust default scaling (percentage, 100 = 1.0x)
// #define HK_DEFAULT_SCALER 100
// #define HK_SNIPING_SCALER 25
```

### Cirque Pinnacle specific

Enable tap and circular scroll in `config.h`:

```c
#define CIRQUE_PINNACLE_TAP_ENABLE           // tap-to-click
#define CIRQUE_PINNACLE_CIRCULAR_SCROLL_ENABLE  // two-finger circular scroll
```

### Dual sensor (POINTING_DEVICE_COMBINED)

Add to `rules.mk`:

```makefile
POINTING_DEVICE_COMBINED = yes
```

This enables independent left+right sensor handling. The peripheral side
state is synced over the split transport using `HK_SPLIT_SYNC_STATE`.

## Files

| File | Purpose |
|------|---------|
| `holykeebs.h` | Public API: keycodes, state types, `g_hk_state` |
| `holykeebs.c` | Core logic: EEPROM, mouse report processing, keycode handlers |
| `pointing.h` | `hk_pointer_kind` enum, pointer/scroll state structs |
| `pimoroni.h/.c` | Pimoroni trackball driver integration |
| `trackpoint.h/.c` | TrackPoint driver integration |
| `eeprom_config.h` | EEPROM layout for persistent settings |
| `rpc.h/.c` | Split-sync RPC for peripheral state |
| `oled.c` | OLED display helpers |
| `hk_debug.h/.c` | Console debug helpers |
| `config.h` | Default compile-time config (overridable per keymap) |
| `rules.mk` | Required QMK feature flags |

## Source

Based on [holykeebs/qmk-userspace](https://github.com/holykeebs/qmk-userspace).
