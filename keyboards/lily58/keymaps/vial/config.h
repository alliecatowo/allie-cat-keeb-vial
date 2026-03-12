/*
This is the c configuration file for the keymap

Copyright 2012 Jun Wako <wakojun@gmail.com>
Copyright 2015 Jack Humbert

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

#pragma once

//#define USE_MATRIX_I2C

/* Select hand configuration */

// #define MASTER_LEFT
#define MASTER_RIGHT
// #define EE_HANDS

#define QUICK_TAP_TERM 0
#define TAPPING_TERM 100

// Vial configuration
#define VIAL_KEYBOARD_UID {0xA1, 0xB2, 0xC3, 0xD4, 0xE5, 0xF6, 0x01, 0x23}
#define VIAL_UNLOCK_COMBO_ROWS { 0, 2 }
#define VIAL_UNLOCK_COMBO_COLS { 0, 1 }

// Underglow
/*
#undef RGBLIGHT_LED_COUNT
#define RGBLIGHT_LED_COUNT 14    // Number of LEDs
#define RGBLIGHT_SLEEP
*/

// ---------------------------------------------------------------------------
// Pointing device — Cirque Pinnacle (ALLIE-201)
//
// Uncomment the block below if you have a Cirque Pinnacle trackpad wired to
// this keyboard.  Pointing device enable + driver selection lives in rules.mk
// (POINTING_DEVICE_ENABLE = yes / POINTING_DEVICE_DRIVER = cirque_pinnacle_spi
// or cirque_pinnacle_i2c).  These defines tune gesture behaviour.
//
// To use via holykeebs userspace, set POINTING_DEVICE=cirque40 (or cirque35)
// and POINTING_DEVICE_POSITION=right (or left) in rules.mk instead — holykeebs
// will set most of the defines below automatically.  This block is provided
// as a standalone reference for builds that bypass holykeebs.
// ---------------------------------------------------------------------------
/*
// Cirque Pinnacle — gesture configuration
// ----------------------------------------
// Physical trackpad diameter. Common sizes: 35 or 40 mm.
#define CIRQUE_PINNACLE_DIAMETER_MM 40

// 1-finger tap = left click.
#define CIRQUE_PINNACLE_TAP_ENABLE

// Drag a finger around the outer ring of the pad to scroll.
// Requires CIRQUE_PINNACLE_POSITION_MODE (absolute mode) — enabled by default
// in QMK when CIRQUE_PINNACLE_TAP_ENABLE is set.
#define CIRQUE_PINNACLE_CIRCULAR_SCROLL_ENABLE

// Uncomment if your trackpad is mounted at a non-standard angle.
// Increments of 90° CW: _90, _180, _270.
// #define POINTING_DEVICE_ROTATION_90

// Scroll sensitivity — higher divisor = slower scroll (default: 4).
#define POINTING_DEVICE_SCROLL_DIVISOR_H 8
#define POINTING_DEVICE_SCROLL_DIVISOR_V 8
*/
