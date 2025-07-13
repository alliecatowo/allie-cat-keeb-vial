#!/usr/bin/env bash

_qmk_install_prepare() {
    sudo pkg update $SKIP_PROMPT
}

_qmk_install() {
    echo "Installing dependencies"

    sudo pkg install -y \
        git wget gmake gcc zip unzip diffutils \
        python3 \
        avr-binutils avr-gcc avr-libc \
        arm-none-eabi-binutils arm-none-eabi-gcc arm-none-eabi-newlib \
        avrdude dfu-programmer dfu-util

    curl -Ls https://astral.sh/uv/install.sh | bash
    sudo uv pip install -r $QMK_FIRMWARE_DIR/requirements.txt
}
