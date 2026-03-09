# Contributing to allie-cat-keeb-vial

## Userspace Architecture

This repo is **not** a full QMK/Vial-QMK fork. It's a minimal userspace that gets
compiled *against* upstream [Vial-QMK](https://github.com/vial-kb/vial-qmk) in CI.

### What lives here

```
allie-cat-keeb-vial/
├── keyboards/
│   ├── lily58/keymaps/vial/    ← Lily58 Vial keymap (keymap.c, rules.mk, vial.json)
│   └── sofle/keymaps/vial/     ← Sofle Vial keymap  (keymap.c, rules.mk, vial.json)
├── users/holykeebs/            ← holykeebs pointing device userspace
├── docs/                       ← Documentation
├── qmk.json                    ← Userspace build targets
└── .github/workflows/build.yml ← CI: clones vial-qmk, copies files, compiles
```

### What does NOT live here

The full QMK/Vial-QMK source tree (quantum/, tmk_core/, lib/, platforms/, etc.)
is pulled fresh from upstream in CI. Do not add these directories.

### How to build locally

1. Clone [vial-qmk](https://github.com/vial-kb/vial-qmk) and follow its setup:
   ```bash
   git clone https://github.com/vial-kb/vial-qmk.git
   cd vial-qmk
   pip3 install -r requirements.txt
   qmk setup -H .
   ```

2. Copy this repo's files in:
   ```bash
   cp -r /path/to/allie-cat-keeb-vial/keyboards/lily58/keymaps/vial  keyboards/lily58/keymaps/
   cp -r /path/to/allie-cat-keeb-vial/keyboards/sofle/keymaps/vial   keyboards/sofle/keymaps/
   cp -r /path/to/allie-cat-keeb-vial/users/holykeebs                users/
   ```

3. Compile:
   ```bash
   qmk compile -kb lily58/rev1 -km vial
   qmk compile -kb sofle/rev1  -km vial
   ```

### Flashing

- **Lily58** (Pro Micro): `.hex` via QMK Toolbox or `avrdude`
- **Sofle rev1** (Pro Micro): `.hex` via QMK Toolbox or `avrdude`

### Adding a new keymap

1. Create `keyboards/<board>/keymaps/vial/`
2. Add `keymap.c`, `rules.mk` (with `VIAL_ENABLE = yes`), and `vial.json`
3. Add the build target to `qmk.json`
4. CI will pick it up automatically on next push

### Updating holykeebs userspace

The `users/holykeebs/` directory is sourced from
[holykeebs/qmk-userspace](https://github.com/holykeebs/qmk-userspace).
Update by copying the relevant files — do not include board-specific config
(that belongs in the keymap's own `config.h`).

See [POINTING_DEVICE_README.md](../POINTING_DEVICE_README.md) for sensor
configuration details.
