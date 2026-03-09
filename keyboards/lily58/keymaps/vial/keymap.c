/* Copyright 2020 Naoki Katahira
  *
  * This program is free software: you can redistribute it and/or modify
  * it under the terms of the GNU General Public License as published by
  * the Free Software Foundation, either version 2 of the License, or
  * (at your option) any later version.
  *
  * This program is distributed in the hope that it will be useful,
  * but WITHOUT ANY WARRANTY; without even the implied warranty of
  * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
  * GNU General Public License for more details.
  *
  * You should have received a copy of the GNU General Public License
  * along with this program.  If not, see <http://www.gnu.org/licenses/>.
  */

#include QMK_KEYBOARD_H
#include <stdio.h>
#include "users/holykeebs/holykeebs.h"

#define QK_C_EEPROM QK_CLEAR_EEPROM

//extern uint8_t is_master;

// Layer names unified with ZMK Sofle: BASE / NAV / NUM / SYS
enum layer_number {
  _BASE = 0,  // was _QWERTY
  _NAV,       // was _LOWER  — symbols, mouse, vim arrows
  _NUM,       // was _RAISE  — F-keys, numpad
  _SYS,       // was _ADJUST — boot, HK_* settings
};

#define NAV MO(_NAV)
#define NUM MO(_NUM)

const uint16_t PROGMEM keymaps[][MATRIX_ROWS][MATRIX_COLS] = {

/* BASE (was QWERTY) — homerow mods: GUI/ALT/SFT/CTL on left, CTL/SFT/ALT/GUI on right
 * ,-----------------------------------------.                    ,-----------------------------------------.
 * | ESC  |   1  |   2  |   3  |   4  |   5  |                    |   6  |   7  |   8  |   9  |   0  |  `   |
 * |------+------+------+------+------+------|                    |------+------+------+------+------+------|
 * | Tab  |   Q  |   W  |   E  |   R  |   T  |                    |   Y  |   U  |   I  |   O  |   P  |  -   |
 * |------+------+------+------+------+------|                    |------+------+------+------+------+------|
 * |LCTRL |GUI(A)|ALT(S)|SFT(D)|CTL(F)|   G  |-------.    ,-------|   H  |CTL(J)|SFT(K)|ALT(L)|GUI(;)|  '   |
 * |------+------+------+------+------+------|   [   |    |    ]  |------+------+------+------+------+------|
 * |LShift|   Z  |   X  |   C  |   V  |   B  |-------|    |-------|   N  |   M  |   ,  |   .  |   /  |RShift|
 * `-----------------------------------------/       /     \      \-----------------------------------------'
 *                   | NAV  | LGUI | Alt  | /Space  /       \Enter \  |BackSP| RGUI | NUM  |
 *                   |      |      |      |/       /         \      \ |      |      |      |
 *                   `-------------------''-------'           '------''--------------------'
 */

 [_BASE] = LAYOUT(
  KC_ESC,   KC_1,          KC_2,          KC_3,          KC_4,          KC_5,                          KC_6,    KC_7,           KC_8,           KC_9,           KC_0,            KC_GRV,
  KC_TAB,   KC_Q,          KC_W,          KC_E,          KC_R,          KC_T,                          KC_Y,    KC_U,           KC_I,           KC_O,           KC_P,            KC_MINS,
  KC_LCTL,  LGUI_T(KC_A),  LALT_T(KC_S),  LSFT_T(KC_D),  LCTL_T(KC_F),  KC_G,                          KC_H,    RCTL_T(KC_J),   RSFT_T(KC_K),   RALT_T(KC_L),   RGUI_T(KC_SCLN), KC_QUOT,
  KC_LSFT,  KC_Z,          KC_X,          KC_C,          KC_V,          KC_B,  KC_LBRC,   KC_RBRC,     KC_N,    KC_M,           KC_COMM,        KC_DOT,         KC_SLSH,         KC_RSFT,
                              NAV, KC_LGUI,  KC_LALT, KC_SPC,   KC_ENT,   KC_BSPC,  KC_RGUI, NUM
),

/* NAV (was LOWER) — symbols, mouse controls, vim arrows at HJKL
 * ,-----------------------------------------.                    ,-----------------------------------------.
 * |      |      |      |      |      |      |                    |      |      |      |      |      |      |
 * |------+------+------+------+------+------|                    |------+------+------+------+------+------|
 * |      |   !  |   @  |   #  |   $  |   %  |                    |   ^  |   &  |   *  |   (  |   )  |      |
 * |------+------+------+------+------+------|                    |------+------+------+------+------+------|
 * |      |   1  |   2  |   3  |   4  |   5  |-------.    ,-------| LEFT | DOWN |  UP  |RIGHT |   0  |      |
 * |------+------+------+------+------+------|HK_SNIP|    |       |------+------+------+------+------+------|
 * |      |HK_DS |BTN4  |BTN5  |BTN1  |BTN2  |-------|    |-------|  |   |  `   |   +  |   {  |   }  |      |
 * `-----------------------------------------/       /     \      \-----------------------------------------'
 *                   | NAV  | LGUI | Alt  | /Space  /       \Enter \  |BackSP| RGUI | NUM  |
 *                   |      |      |      |/       /         \      \ |      |      |      |
 *                   `-------------------''-------'           '------''--------------------'
 */
[_NAV] = LAYOUT(
  _______, _______, _______, _______, _______, _______,                           _______, _______, _______, _______, _______, _______,
  _______, KC_EXLM, KC_AT,   KC_HASH, KC_DLR,  KC_PERC,                           KC_CIRC, KC_AMPR, KC_ASTR, KC_LPRN, KC_RPRN, _______,
  _______, KC_1,    KC_2,    KC_3,    KC_4,    KC_5,                              KC_LEFT, KC_DOWN, KC_UP,   KC_RGHT, KC_0,    _______,
  _______, HK_D_MODE, KC_BTN4, KC_BTN5, KC_BTN1, KC_BTN2, HK_S_MODE,   _______, KC_PIPE, KC_GRAVE, KC_PLUS, KC_LCBR, KC_RCBR, _______,
                               _______, _______, _______, _______,      _______, _______, _______, _______
),

/* NUM (was RAISE) — F-keys, numpad at HJKL (4-9)
 * ,-----------------------------------------.                    ,-----------------------------------------.
 * |      |      |      |      |      |      |                    |      |      |      |      |      |      |
 * |------+------+------+------+------+------|                    |------+------+------+------+------+------|
 * |  F1  |  F2  |  F3  |  F4  |  F5  |  F6  |                    |  F7  |  F8  |  F9  | F10  | F11  | F12  |
 * |------+------+------+------+------+------|                    |------+------+------+------+------+------|
 * |      |      |      |      |      |      |-------.    ,-------|   4  |   5  |   6  |   7  |   8  |   9  |
 * |------+------+------+------+------+------|   [   |    |    ]  |------+------+------+------+------+------|
 * |      |      |      |      |      |      |-------|    |-------|   +  |   =  |   [  |   ]  |   \  |      |
 * `-----------------------------------------/       /     \      \-----------------------------------------'
 *                   | NAV  | LGUI | Alt  | /Space  /       \Enter \  |BackSP| RGUI | NUM  |
 *                   |      |      |      |/       /         \      \ |      |      |      |
 *                   `-------------------''-------'           '------''--------------------'
 */
[_NUM] = LAYOUT(
  _______, _______, _______, _______, _______, _______,                      _______, _______, _______, _______, _______, _______,
  KC_F1,   KC_F2,   KC_F3,   KC_F4,   KC_F5,   KC_F6,                        KC_F7,   KC_F8,   KC_F9,   KC_F10,  KC_F11,  KC_F12,
  _______, _______, _______, _______, _______, _______,                       KC_4,    KC_5,    KC_6,    KC_7,    KC_8,    KC_9,
  _______, _______, _______, _______, _______, _______, _______, _______,     KC_PLUS, KC_EQL,  KC_LBRC, KC_RBRC, KC_BSLS, _______,
                             _______, _______, _______, _______, _______,     _______, _______, _______
),

/* SYS (was ADJUST) — boot, HK_* settings, EEPROM — PRESERVE ALL
 * ,-----------------------------------------.                    ,-----------------------------------------.
 * |      |      |      |      |      |      |                    |      |      |      |      |      |      |
 * |------+------+------+------+------+------|                    |------+------+------+------+------+------|
 * | BOOT |DUMP  |SAVE  |RESET |      |HK_C_S|                    |      |      |      |      |      | BOOT |
 * |------+------+------+------+------+------|                    |------+------+------+------+------+------|
 * |EEPROM|P_SET_D|P_ST_S|P_ST_B|     |S_MODE|-------.    ,-------|  UP  | DOWN |      |      |      |EEPROM|
 * |------+------+------+------+------+------|       |    |       |------+------+------+------+------+------|
 * |LShift|      |      |      |      |D_MODE|-------|    |-------|      |      |      |      |      |      |
 * `-----------------------------------------/       /     \      \-----------------------------------------'
 *                   | NAV  | LGUI | Alt  | /Space  /       \Enter \  |BackSP| RGUI | NUM  |
 *                   |      |      |      |/       /         \      \ |      |      |      |
 *                   `----------------------------'           '------''--------------------'
 */
  [_SYS] = LAYOUT(
    XXXXXXX,      XXXXXXX,    XXXXXXX,    XXXXXXX,      XXXXXXX, XXXXXXX,                           XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
    QK_BOOT,      HK_DUMP,    HK_SAVE,    HK_RESET,     XXXXXXX, HK_C_SCROLL,                       XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, QK_BOOT,
    QK_C_EEPROM,  HK_P_SET_D, HK_P_SET_S, HK_P_SET_BUF, XXXXXXX, HK_S_MODE_T,                       KC_UP,   KC_DOWN, XXXXXXX, XXXXXXX, XXXXXXX, QK_C_EEPROM,
    KC_LSFT,      XXXXXXX,    XXXXXXX,    XXXXXXX,      XXXXXXX, HK_D_MODE_T, XXXXXXX,   XXXXXXX,   XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
                                                   _______, _______, _______, _______,   _______, _______, _______, _______
  )
};

layer_state_t layer_state_set_user(layer_state_t state) {
  state = update_tri_layer_state(state, _NAV, _NUM, _SYS);
  return state;
}

#if defined(OLED_ENABLE) && !defined(HK_OLED_ENABLE)

oled_rotation_t oled_init_user(oled_rotation_t rotation) {
  if (!is_keyboard_master())
    return OLED_ROTATION_180;  // flips the display 180 degrees if offhand
  return rotation;
}

static void render_logo(void) {
    static const char PROGMEM logo[] = {
        0x80, 0x81, 0x82, 0x83, 0x84, 0x85, 0x86, 0x87, 0x88, 0x89, 0x8A, 0x8B, 0x8C, 0x8D, 0x8E, 0x8F, 0x90, 0x91, 0x92, 0x93, 0x94,
        0xA0, 0xA1, 0xA2, 0xA3, 0xA4, 0xA5, 0xA6, 0xA7, 0xA8, 0xA9, 0xAA, 0xAB, 0xAC, 0xAD, 0xAE, 0xAF, 0xB0, 0xB1, 0xB2, 0xB3, 0xB4,
        0xC0, 0xC1, 0xC2, 0xC3, 0xC4, 0xC5, 0xC6, 0xC7, 0xC8, 0xC9, 0xCA, 0xCB, 0xCC, 0xCD, 0xCE, 0xCF, 0xD0, 0xD1, 0xD2, 0xD3, 0xD4, 0x00
    };

    oled_write_P(logo, false);
}
char keylog_str[24] = {};
char keylogs_str[21] = {};
int keylogs_str_idx = 0;

const char code_to_name[60] = {
    ' ', ' ', ' ', ' ', 'a', 'b', 'c', 'd', 'e', 'f',
    'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
    'R', 'E', 'B', 'T', '_', '-', '=', '[', ']', '\\',
    '#', ';', '\'', '`', ',', '.', '/', ' ', ' ', ' '};

void set_keylog(uint16_t keycode, keyrecord_t *record) {
  char name = ' ';
  if (keycode < 60) {
    name = code_to_name[keycode];
  }

  // update keylog
  snprintf(keylog_str, sizeof(keylog_str), "%dx%d, k%2d : %c",
           record->event.key.row, record->event.key.col,
           keycode, name);

  // update keylogs
  if (keylogs_str_idx == sizeof(keylogs_str) - 1) {
    keylogs_str_idx = 0;
    for (int i = 0; i < sizeof(keylogs_str) - 1; i++) {
      keylogs_str[i] = ' ';
    }
  }

  keylogs_str[keylogs_str_idx] = name;
  keylogs_str_idx++;
}

const char *read_keylog(void) {
  return keylog_str;
}

const char *read_keylogs(void) {
  return keylogs_str;
}
//new

bool oled_task_user(void) {
  #ifdef OLED_FLIP
  bool condition = !is_keyboard_master();
  #else
  bool condition = is_keyboard_master();
  #endif
  if (condition) {
    // Host Keyboard Layer Status
    oled_write_P(PSTR("Layer: "), false);

    switch (get_highest_layer(layer_state)) {
    case _BASE:
        oled_write_ln_P(PSTR("BASE"), false);
        break;
    case _NUM:
        oled_write_ln_P(PSTR("NUM"), false);
        break;
    case _NAV:
        oled_write_ln_P(PSTR("NAV"), false);
        break;
    case _SYS:
        oled_write_ln_P(PSTR("SYS"), false);
        break;
    default:
        oled_write_ln_P(PSTR("Undefined"), false);
    }

    oled_write_ln(read_keylog(), false);
    oled_write_ln(read_keylogs(), false);

  } else {
      render_logo();
  }
    return false;
}

bool process_record_user(uint16_t keycode, keyrecord_t *record) {
  if (record->event.pressed) {
#ifdef OLED_ENABLE
    set_keylog(keycode, record);
#endif
    // set_timelog();
  }
  return true;
}

#endif // OLED_ENABLE
