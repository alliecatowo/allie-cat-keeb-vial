#!/usr/bin/env bash

_qmk_install_prepare() {
    sudo eopkg -y update-repo
    sudo eopkg -y upgrade
}

_qmk_install() {
    echo "Installing dependencies"

    sudo eopkg -y install \
        -c system.devel git wget zip unzip \
        python3 \
        avr-binutils avr-gcc avr-libc \
        arm-none-eabi-binutils arm-none-eabi-gcc arm-none-eabi-newlib \
        avrdude dfu-programmer dfu-util

    uv venv "$QMK_FIRMWARE_DIR/.venv"
    source "$QMK_FIRMWARE_DIR/.venv/bin/activate"
    uv pip install -r $QMK_FIRMWARE_DIR/requirements.txt
}
