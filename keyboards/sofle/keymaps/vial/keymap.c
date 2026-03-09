// Copyright 2024 alliecatowo
// SPDX-License-Identifier: GPL-2.0-or-later

#include QMK_KEYBOARD_H

// Layer indices
enum sofle_layers {
    _BASE,
    _NAV,
    _NUM,
    _SYS,
};

// Transparent / no-op shorthands
#define _____ KC_TRNS
#define XXXXX KC_NO

// Layer-tap / mod-tap shorthands
#define LT_NAV  LT(_NAV, KC_SPC)   // Space  → hold for NAV
#define LT_NUM  LT(_NUM, KC_ENT)   // Enter  → hold for NUM
#define MO_SYS  MO(_SYS)

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {

/*
 * BASE — QWERTY
 * ┌─────┬─────┬─────┬─────┬─────┬─────┐                    ┌─────┬─────┬─────┬─────┬─────┬─────┐
 * │  `  │  1  │  2  │  3  │  4  │  5  │                    │  6  │  7  │  8  │  9  │  0  │  -  │
 * ├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
 * │ ESC │  Q  │  W  │  E  │  R  │  T  │                    │  Y  │  U  │  I  │  O  │  P  │BSPC │
 * ├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
 * │ TAB │  A  │  S  │  D  │  F  │  G  │                    │  H  │  J  │  K  │  L  │  ;  │  '  │
 * ├─────┼─────┼─────┼─────┼─────┼─────┼─────┐  ┌─────┬────┼─────┼─────┼─────┼─────┼─────┼─────┤
 * │LSFT │  Z  │  X  │  C  │  V  │  B  │MUTE │  │     │  N  │  M  │  ,  │  .  │  /  │RSFT │
 * └─────┴─────┴─────┼─────┼─────┼─────┼─────┤  ├─────┼─────┼─────┼─────┼─────┴─────┴─────┘
 *                   │LGUI │LALT │LCTL │ NUM │  │ NAV │RCTL │RALT │RGUI │
 *                   └─────┴─────┴─────┴─────┘  └─────┴─────┴─────┴─────┘
 */
[_BASE] = LAYOUT(
    KC_GRV,  KC_1,    KC_2,    KC_3,    KC_4,    KC_5,                        KC_6,    KC_7,    KC_8,    KC_9,    KC_0,    KC_MINS,
    KC_ESC,  KC_Q,    KC_W,    KC_E,    KC_R,    KC_T,                        KC_Y,    KC_U,    KC_I,    KC_O,    KC_P,    KC_BSPC,
    KC_TAB,  KC_A,    KC_S,    KC_D,    KC_F,    KC_G,                        KC_H,    KC_J,    KC_K,    KC_L,    KC_SCLN, KC_QUOT,
    KC_LSFT, KC_Z,    KC_X,    KC_C,    KC_V,    KC_B,    KC_MUTE,   XXXXX,   KC_N,    KC_M,    KC_COMM, KC_DOT,  KC_SLSH, KC_RSFT,
                      KC_LGUI, KC_LALT, KC_LCTL, LT_NUM,  KC_SPC,    KC_ENT,  LT_NAV,  KC_RCTL, KC_RALT, KC_RGUI
),

/*
 * NAV — Navigation
 * ┌─────┬─────┬─────┬─────┬─────┬─────┐                    ┌─────┬─────┬─────┬─────┬─────┬─────┐
 * │     │ F1  │ F2  │ F3  │ F4  │ F5  │                    │ F6  │ F7  │ F8  │ F9  │ F10 │ F11 │
 * ├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
 * │     │     │     │     │     │     │                    │HOME │PGDN │PGUP │ END │     │ DEL │
 * ├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
 * │     │     │     │     │     │     │                    │LEFT │DOWN │ UP  │RGHT │     │     │
 * ├─────┼─────┼─────┼─────┼─────┼─────┼─────┐  ┌─────┬────┼─────┼─────┼─────┼─────┼─────┼─────┤
 * │     │     │     │     │     │     │     │  │     │     │     │     │     │     │     │
 * └─────┴─────┴─────┼─────┼─────┼─────┼─────┤  ├─────┼─────┼─────┼─────┼─────┴─────┴─────┘
 *                   │     │     │     │ SYS │  │     │     │     │     │
 *                   └─────┴─────┴─────┴─────┘  └─────┴─────┴─────┴─────┘
 */
[_NAV] = LAYOUT(
    _____, KC_F1,   KC_F2,   KC_F3,   KC_F4,   KC_F5,                       KC_F6,   KC_F7,   KC_F8,   KC_F9,   KC_F10,  KC_F11,
    _____, XXXXX,   XXXXX,   XXXXX,   XXXXX,   XXXXX,                       KC_HOME, KC_PGDN, KC_PGUP, KC_END,  XXXXX,   KC_DEL,
    _____, XXXXX,   XXXXX,   XXXXX,   XXXXX,   XXXXX,                       KC_LEFT, KC_DOWN, KC_UP,   KC_RGHT, XXXXX,   XXXXX,
    _____, XXXXX,   XXXXX,   XXXXX,   XXXXX,   XXXXX,   _____,     _____,   XXXXX,   XXXXX,   XXXXX,   XXXXX,   XXXXX,   _____,
                    _____, _____, _____, MO_SYS,  _____,     _____,   _____, _____, _____, _____
),

/*
 * NUM — Numbers & Symbols
 * ┌─────┬─────┬─────┬─────┬─────┬─────┐                    ┌─────┬─────┬─────┬─────┬─────┬─────┐
 * │     │     │     │     │     │     │                    │     │     │     │     │     │     │
 * ├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
 * │     │  !  │  @  │  #  │  $  │  %  │                    │  ^  │  &  │  *  │  (  │  )  │     │
 * ├─────┼─────┼─────┼─────┼─────┼─────┤                    ├─────┼─────┼─────┼─────┼─────┼─────┤
 * │     │  1  │  2  │  3  │  4  │  5  │                    │  6  │  7  │  8  │  9  │  0  │  =  │
 * ├─────┼─────┼─────┼─────┼─────┼─────┼─────┐  ┌─────┬────┼─────┼─────┼─────┼─────┼─────┼─────┤
 * │     │  [  │  ]  │  {  │  }  │  \  │     │  │     │  |  │  -  │  +  │  _  │     │     │
 * └─────┴─────┴─────┼─────┼─────┼─────┼─────┤  ├─────┼─────┼─────┼─────┼─────┴─────┴─────┘
 *                   │     │     │     │     │  │ SYS │     │     │     │
 *                   └─────┴─────┴─────┴─────┘  └─────┴─────┴─────┴─────┘
 */
[_NUM] = LAYOUT(
    _____, XXXXX,   XXXXX,   XXXXX,   XXXXX,   XXXXX,                       XXXXX,   XXXXX,   XXXXX,   XXXXX,   XXXXX,   XXXXX,
    _____, KC_EXLM, KC_AT,   KC_HASH, KC_DLR,  KC_PERC,                     KC_CIRC, KC_AMPR, KC_ASTR, KC_LPRN, KC_RPRN, _____,
    _____, KC_1,    KC_2,    KC_3,    KC_4,    KC_5,                        KC_6,    KC_7,    KC_8,    KC_9,    KC_0,    KC_EQL,
    _____, KC_LBRC, KC_RBRC, KC_LCBR, KC_RCBR, KC_BSLS, _____,     _____,   KC_PIPE, KC_MINS, KC_PLUS, KC_UNDS, XXXXX,   _____,
                    _____, _____, _____, _____, _____,     _____,   MO_SYS,  _____, _____, _____
),

/*
 * SYS — System / RGB / QMK
 */
[_SYS] = LAYOUT(
    QK_BOOT, XXXXX,   XXXXX,   XXXXX,   XXXXX,   XXXXX,                     XXXXX,   XXXXX,   XXXXX,   XXXXX,   XXXXX,   XXXXX,
    XXXXX,   RGB_TOG, RGB_MOD, RGB_HUI, RGB_SAI, RGB_VAI,                   XXXXX,   XXXXX,   XXXXX,   XXXXX,   XXXXX,   XXXXX,
    XXXXX,   RGB_RMOD,XXXXX,   RGB_HUD, RGB_SAD, RGB_VAD,                   XXXXX,   XXXXX,   XXXXX,   XXXXX,   XXXXX,   XXXXX,
    XXXXX,   XXXXX,   XXXXX,   XXXXX,   XXXXX,   XXXXX,   _____,   _____,   XXXXX,   XXXXX,   XXXXX,   XXXXX,   XXXXX,   XXXXX,
                      _____, _____, _____, _____, _____,     _____,   _____,  _____, _____, _____
),

};

// Encoder mapping: rotate left encoder for volume, right encoder for scroll
#if defined(ENCODER_MAP_ENABLE)
const uint16_t PROGMEM encoder_map[][NUM_ENCODERS][NUM_DIRECTIONS] = {
    [_BASE] = { ENCODER_CCW_CW(KC_VOLD, KC_VOLU), ENCODER_CCW_CW(KC_WH_D, KC_WH_U) },
    [_NAV]  = { ENCODER_CCW_CW(KC_MPRV, KC_MNXT), ENCODER_CCW_CW(KC_PGDN, KC_PGUP) },
    [_NUM]  = { ENCODER_CCW_CW(KC_VOLD, KC_VOLU), ENCODER_CCW_CW(KC_WH_D, KC_WH_U) },
    [_SYS]  = { ENCODER_CCW_CW(RGB_VAD, RGB_VAI),  ENCODER_CCW_CW(RGB_SPD, RGB_SPI) },
};
#endif
