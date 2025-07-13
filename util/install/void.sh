#!/usr/bin/env bash

_qmk_install() {
    echo "Installing dependencies"

    sudo xbps-install $SKIP_PROMPT \
        gcc git make wget unzip zip \
        curl \
        avr-binutils avr-gcc avr-libc \
        cross-arm-none-eabi-binutils cross-arm-none-eabi-gcc cross-arm-none-eabi-newlib \
        avrdude dfu-programmer dfu-util teensy_loader_cli \
        libusb-compat-devel

    curl -Ls https://astral.sh/uv/install.sh | bash
    uv pip install --user -r $QMK_FIRMWARE_DIR/requirements.txt
}
