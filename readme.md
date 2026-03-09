# allie-cat-keeb-vial

Allie's Vial-enabled QMK userspace for Lily58 and Sofle keyboards with holykeebs
pointing device support.

[![Build Status](https://github.com/alliecatowo/allie-cat-keeb-vial/actions/workflows/build.yml/badge.svg)](https://github.com/alliecatowo/allie-cat-keeb-vial/actions/workflows/build.yml)
[![License](https://img.shields.io/badge/license-GPL2+-blue.svg)](LICENSE)

---

## Supported Keyboards

| Board | Keymap | Layers | Notes |
|-------|--------|--------|-------|
| **Lily58 rev1** | `lily58/rev1:vial` | BASE / NAV / NUM / SYS | Pimoroni trackball via holykeebs |
| **Sofle rev1** | `sofle/rev1:vial` | BASE / NAV / NUM / SYS | Dual encoder support |

## Keymap Structure

All keymaps share a consistent 4-layer layout:

| Layer | Activation | Contents |
|-------|-----------|---------|
| **BASE** | default | QWERTY, modifiers, layer-tap on Space/Enter |
| **NAV** | hold Space | Arrows, Home/End/PgUp/PgDn, F-keys |
| **NUM** | hold Enter | Numbers row, symbols |
| **SYS** | NAV + NUM held | QMK Boot, RGB controls |

## Repository Layout

```
keyboards/
  lily58/keymaps/vial/    ← Lily58 keymap (keymap.c, rules.mk, vial.json)
  sofle/keymaps/vial/     ← Sofle keymap  (keymap.c, rules.mk, vial.json)
users/
  holykeebs/              ← Pointing device userspace (HK_* keycodes, drivers)
docs/
  CONTRIBUTING.md         ← How to build locally + add new keymaps
qmk.json                  ← Userspace build targets
.github/workflows/
  build.yml               ← CI: clones vial-qmk, compiles, uploads .hex/.uf2
```

## Quick Build

CI builds automatically on every push. Pre-built firmware is available in
[GitHub Actions artifacts](https://github.com/alliecatowo/allie-cat-keeb-vial/actions/workflows/build.yml).

To build locally, see [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md).

## Pointing Device Support

This repo uses [holykeebs](https://holykeebs.com)' QMK userspace for pointing devices.

Supported sensors: Pimoroni Trackball, Cirque Pinnacle (35/40mm), Azoteq IQS5xx,
PMW3320/PMW3360, TrackPoint.

See [POINTING_DEVICE_README.md](POINTING_DEVICE_README.md) for configuration details.

## Resources

- [Vial](https://get.vial.today) — real-time keymap editing without flashing
- [Vial-QMK](https://github.com/vial-kb/vial-qmk) — the upstream this builds against
- [holykeebs docs](https://docs.holykeebs.com) — hardware installation guides
