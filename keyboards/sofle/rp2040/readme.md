# Sofle RP2040

RP2040-based Sofle variant modeled after the Lily58 RP2040 build. Uses vendor split serial and WS2812 drivers and keeps the existing Sofle layout.

## Build

```sh
qmk compile -kb sofle/rp2040 -km vial
```

Enable pointing devices and sides via the same `POINTING_DEVICE`/`SIDE` options used for Lily58.
