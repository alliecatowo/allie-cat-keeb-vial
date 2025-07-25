/*
Copyright 2011,2013 Jun Wako <wakojun@gmail.com>

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

#include <stdbool.h>
#include "keyboard.h"
#include "ps2_mouse.h"
#include "wait.h"
#include "gpio.h"
#include "host.h"
#include "timer.h"
#include "print.h"
#include "report.h"
#include "debug.h"
#include "ps2.h"

/* ============================= MACROS ============================ */

static uint8_t buttons_prev = 0;
static report_mouse_t local_mouse_report = {};

static inline void ps2_mouse_print_report(report_mouse_t *mouse_report);
static inline void ps2_mouse_convert_report_to_hid(report_mouse_t *mouse_report);
static inline void ps2_mouse_clear_report(report_mouse_t *mouse_report);
static inline void ps2_mouse_enable_scrolling(void);
static inline void ps2_mouse_scroll_button_task(report_mouse_t *mouse_report);

/* ============================= IMPLEMENTATION ============================ */

/* supports only 3 button mouse at this time */
void ps2_mouse_init(void) {
    if (!is_keyboard_master()) {
        return;
    }

    ps2_host_init();

    wait_ms(PS2_MOUSE_INIT_DELAY); // wait for powering up

    PS2_MOUSE_SEND(PS2_MOUSE_RESET, "ps2_mouse_init: sending reset");
    // Spec calls for 500ms sleep after reset.
    wait_ms(500);

    PS2_MOUSE_RECEIVE("ps2_mouse_init: read BAT");
    PS2_MOUSE_RECEIVE("ps2_mouse_init: read DevID");

#ifdef PS2_MOUSE_USE_REMOTE_MODE
    ps2_mouse_set_remote_mode();
#else
    ps2_mouse_enable_data_reporting();
    ps2_mouse_set_stream_mode();
#endif

#ifdef PS2_MOUSE_ENABLE_SCROLLING
    ps2_mouse_enable_scrolling();
#endif

#ifdef PS2_MOUSE_USE_2_1_SCALING
    ps2_mouse_set_scaling_2_1();
#endif

    ps2_mouse_init_user();

}

__attribute__((weak)) void ps2_mouse_init_user(void) {}

__attribute__((weak)) void ps2_mouse_moved_user(report_mouse_t *mouse_report) {}

void ps2_mouse_task(void) {
    if (!ps2_mouse_read(&local_mouse_report)) {
        return;
    }

    if (local_mouse_report.x || local_mouse_report.y || local_mouse_report.v || ((local_mouse_report.buttons ^ buttons_prev) & PS2_MOUSE_BTN_MASK)) {
        host_mouse_send(&local_mouse_report);
    }

    ps2_mouse_clear_report(&local_mouse_report);
}

bool ps2_mouse_read(report_mouse_t* mouse_report) {
    if (!is_keyboard_master()) {
        return false;
    }

#if defined(HK_POINTING_DEVICE_RIGHT_PIMORONI) || defined(HK_POINTING_DEVICE_LEFT_PIMORONI)
    // Reading the ps2 mouse too often can cause the Pimoroni on the other side to lock up.
    static uint32_t last_exec = 0;
    if (timer_elapsed32(last_exec) < 15) {
        return false;
    }
    last_exec = timer_read32();
#endif

    extern int     tp_buttons;

    /* receives packet from mouse */
#ifdef PS2_MOUSE_USE_REMOTE_MODE
    uint8_t rcv;
    rcv = ps2_host_send(PS2_MOUSE_READ_DATA);
    if (rcv == PS2_ACK) {
        mouse_report->buttons = ps2_host_recv_response();
        mouse_report->x       = ps2_host_recv_response();
        mouse_report->y       = ps2_host_recv_response();
#    ifdef PS2_MOUSE_ENABLE_SCROLLING
        mouse_report->v = -(ps2_host_recv_response() & PS2_MOUSE_SCROLL_MASK);
#    endif
    } else {
        if (debug_mouse) print("ps2_mouse: fail to get mouse packet\n");
        /* return here to avoid updating the mouse button state */
        return false;
    }
#else
    if (pbuf_has_data()) {
        mouse_report->buttons = ps2_host_recv_response();
        mouse_report->x       = ps2_host_recv_response();
        mouse_report->y       = ps2_host_recv_response();
#    ifdef PS2_MOUSE_ENABLE_SCROLLING
        mouse_report->v       = -(ps2_host_recv_response() & PS2_MOUSE_SCROLL_MASK);
#    endif
    } else {
        if (debug_mouse) print("ps2_mouse: fail to get mouse packet\n");
        /* return here to avoid updating the mouse button state */
        return false;
    }
#endif

    mouse_report->buttons |= tp_buttons;
    /* if mouse moves or buttons state changes */
    if (mouse_report->x || mouse_report->y || mouse_report->v || ((mouse_report->buttons ^ buttons_prev) & PS2_MOUSE_BTN_MASK)) {
#ifdef PS2_MOUSE_DEBUG_RAW
        // Used to debug raw ps2 bytes from mouse
        ps2_mouse_print_report(mouse_report);
#endif
        buttons_prev = mouse_report->buttons;
        ps2_mouse_convert_report_to_hid(mouse_report);
#if PS2_MOUSE_SCROLL_BTN_MASK
        ps2_mouse_scroll_button_task(mouse_report);
#endif
        if (mouse_report->x || mouse_report->y || mouse_report->v) {
            ps2_mouse_moved_user(mouse_report);
        }
#ifdef PS2_MOUSE_DEBUG_HID
        // Used to debug the bytes sent to the host
        ps2_mouse_print_report(mouse_report);
#endif

        return true;
    }

    return false;
}

void ps2_mouse_disable_data_reporting(void) {
    PS2_MOUSE_SEND(PS2_MOUSE_DISABLE_DATA_REPORTING, "ps2 mouse disable data reporting");
}

void ps2_mouse_enable_data_reporting(void) {
    PS2_MOUSE_SEND(PS2_MOUSE_ENABLE_DATA_REPORTING, "ps2 mouse enable data reporting");
}

void ps2_mouse_set_remote_mode(void) {
    PS2_MOUSE_SEND_SAFE(PS2_MOUSE_SET_REMOTE_MODE, "ps2 mouse set remote mode");
    ps2_mouse_mode = PS2_MOUSE_REMOTE_MODE;
}

void ps2_mouse_set_stream_mode(void) {
    PS2_MOUSE_SEND_SAFE(PS2_MOUSE_SET_STREAM_MODE, "ps2 mouse set stream mode");
    ps2_mouse_mode = PS2_MOUSE_STREAM_MODE;
}

void ps2_mouse_set_scaling_2_1(void) {
    PS2_MOUSE_SEND_SAFE(PS2_MOUSE_SET_SCALING_2_1, "ps2 mouse set scaling 2:1");
}

void ps2_mouse_set_scaling_1_1(void) {
    PS2_MOUSE_SEND_SAFE(PS2_MOUSE_SET_SCALING_1_1, "ps2 mouse set scaling 1:1");
}

void ps2_mouse_set_resolution(ps2_mouse_resolution_t resolution) {
    PS2_MOUSE_SET_SAFE(PS2_MOUSE_SET_RESOLUTION, resolution, "ps2 mouse set resolution");
}

void ps2_mouse_set_sample_rate(ps2_mouse_sample_rate_t sample_rate) {
    PS2_MOUSE_SET_SAFE(PS2_MOUSE_SET_SAMPLE_RATE, sample_rate, "ps2 mouse set sample rate");
}

const char* ps2_register_enum_to_string(ps2_mouse_register_e reg) {
    switch (reg) {
        case PS2_MOUSE_SENSITIVITY_FACTOR:
            return "sensitivity";
        case PS2_MOUSE_VALUE6:
            return "value6";
        case PS2_MOUSE_K1:
            return "K1";
        case PS2_MOUSE_C1:
            return "C1";
        case PS2_MOUSE_C2:
            return "C2";
        case PS2_MOUSE_C3:
            return "C3";
        default:
            return "unknown register";
    }
}

uint8_t ps2_mouse_read_register(ps2_mouse_register_e reg) {
    PS2_MOUSE_SEND(0xE2, "trackpoint command");
    PS2_MOUSE_SEND(0x80, "read byte");
    PS2_MOUSE_SEND(reg, ps2_register_enum_to_string(reg));
    uint8_t rcv = ps2_host_recv_response();
    if (debug_mouse) {
        xprintf("ps2 read register %s result: %X, error: %X [%ld] \n", ps2_register_enum_to_string(reg), rcv, ps2_error, timer_read32());
    }
    return rcv;
}


void ps2_mouse_write_register(ps2_mouse_register_e reg, uint8_t data) {
    PS2_MOUSE_SEND(0xE2, "trackpoint command");
    PS2_MOUSE_SEND(0x81, "write byte");
    PS2_MOUSE_SEND(reg, ps2_register_enum_to_string(reg));
    PS2_MOUSE_SEND(data, "data");
}

/* ============================= HELPERS ============================ */

#define X_IS_NEG (mouse_report->buttons & (1 << PS2_MOUSE_X_SIGN))
#define Y_IS_NEG (mouse_report->buttons & (1 << PS2_MOUSE_Y_SIGN))
#define X_IS_OVF (mouse_report->buttons & (1 << PS2_MOUSE_X_OVFLW))
#define Y_IS_OVF (mouse_report->buttons & (1 << PS2_MOUSE_Y_OVFLW))
static inline void ps2_mouse_convert_report_to_hid(report_mouse_t *mouse_report) {
#ifndef MOUSE_EXTENDED_REPORT
    // PS/2 mouse data is '9-bit integer'(-256 to 255) which is comprised of sign-bit and 8-bit value.
    // bit: 8    7 ... 0
    //      sign \8-bit/
    //
    // Meanwhile USB HID mouse indicates 8bit data(-127 to 127), note that -128 is not used.
    //
    // This converts PS/2 data into HID value. Use only -127-127 out of PS/2 9-bit.
    mouse_report->x *= PS2_MOUSE_X_MULTIPLIER;
    mouse_report->y *= PS2_MOUSE_Y_MULTIPLIER;
    mouse_report->x = X_IS_NEG ? ((!X_IS_OVF && -127 <= mouse_report->x && mouse_report->x <= -1) ? mouse_report->x : -127) : ((!X_IS_OVF && 0 <= mouse_report->x && mouse_report->x <= 127) ? mouse_report->x : 127);
    mouse_report->y = Y_IS_NEG ? ((!Y_IS_OVF && -127 <= mouse_report->y && mouse_report->y <= -1) ? mouse_report->y : -127) : ((!Y_IS_OVF && 0 <= mouse_report->y && mouse_report->y <= 127) ? mouse_report->y : 127);
#else
    // Sign extend if negative, otherwise leave positive 8-bits as-is
    mouse_report->x = X_IS_NEG ? (mouse_report->x | ~0xFF) : mouse_report->x;
    mouse_report->y = Y_IS_NEG ? (mouse_report->y | ~0xFF) : mouse_report->y;
    mouse_report->x *= PS2_MOUSE_X_MULTIPLIER;
    mouse_report->y *= PS2_MOUSE_Y_MULTIPLIER;
#endif
    mouse_report->v *= PS2_MOUSE_V_MULTIPLIER;

#ifdef PS2_MOUSE_INVERT_BUTTONS
    // swap left & right buttons
    bool needs_left       = mouse_report->buttons & (1 << PS2_MOUSE_BTN_RIGHT);
    bool needs_right      = mouse_report->buttons & (1 << PS2_MOUSE_BTN_LEFT);
    mouse_report->buttons = (mouse_report->buttons & ~((1 << PS2_MOUSE_BTN_LEFT) | (1 << PS2_MOUSE_BTN_RIGHT))) | (needs_left << PS2_MOUSE_BTN_LEFT) | (needs_right << PS2_MOUSE_BTN_RIGHT);
#endif
    // remove sign and overflow flags
    mouse_report->buttons &= PS2_MOUSE_BTN_MASK;

#ifdef PS2_MOUSE_INVERT_X
    mouse_report->x = -mouse_report->x;
#endif
#ifndef PS2_MOUSE_INVERT_Y // NOTE if not!
    // invert coordinate of y to conform to USB HID mouse
    mouse_report->y = -mouse_report->y;
#endif

#ifdef PS2_MOUSE_ROTATE
    mouse_xy_report_t x = mouse_report->x;
    mouse_xy_report_t y = mouse_report->y;
#    if PS2_MOUSE_ROTATE == 90
    mouse_report->x = y;
    mouse_report->y = -x;
#    elif PS2_MOUSE_ROTATE == 180
    mouse_report->x = -x;
    mouse_report->y = -y;
#    elif PS2_MOUSE_ROTATE == 270
    mouse_report->x = -y;
    mouse_report->y = x;
#    endif
#endif
}

static inline void ps2_mouse_clear_report(report_mouse_t *mouse_report) {
    mouse_report->x       = 0;
    mouse_report->y       = 0;
    mouse_report->v       = 0;
    mouse_report->h       = 0;
    mouse_report->buttons = 0;
}

static inline void ps2_mouse_print_report(report_mouse_t *mouse_report) {
    if (!debug_mouse) return;
    print("ps2_mouse: [");
    print_hex8(mouse_report->buttons);
    print("|");
    print_hex8((uint8_t)mouse_report->x);
    print(" ");
    print_hex8((uint8_t)mouse_report->y);
    print(" ");
    print_hex8((uint8_t)mouse_report->v);
    print(" ");
    print_hex8((uint8_t)mouse_report->h);
    print("]\n");
}

static inline void ps2_mouse_enable_scrolling(void) {
    PS2_MOUSE_SEND(PS2_MOUSE_SET_SAMPLE_RATE, "Initiaing scroll wheel enable: Set sample rate");
    PS2_MOUSE_SEND(200, "200");
    PS2_MOUSE_SEND(PS2_MOUSE_SET_SAMPLE_RATE, "Set sample rate");
    PS2_MOUSE_SEND(100, "100");
    PS2_MOUSE_SEND(PS2_MOUSE_SET_SAMPLE_RATE, "Set sample rate");
    PS2_MOUSE_SEND(80, "80");
    PS2_MOUSE_SEND(PS2_MOUSE_GET_DEVICE_ID, "Finished enabling scroll wheel");
    wait_ms(20);
}

#define PRESS_SCROLL_BUTTONS mouse_report->buttons |= (PS2_MOUSE_SCROLL_BTN_MASK)
#define RELEASE_SCROLL_BUTTONS mouse_report->buttons &= ~(PS2_MOUSE_SCROLL_BTN_MASK)
static inline void ps2_mouse_scroll_button_task(report_mouse_t *mouse_report) {
    static enum {
        SCROLL_NONE,
        SCROLL_BTN,
        SCROLL_SENT,
    } scroll_state                     = SCROLL_NONE;
    static uint16_t scroll_button_time = 0;
    static int16_t  scroll_x, scroll_y;

    if (PS2_MOUSE_SCROLL_BTN_MASK == (mouse_report->buttons & (PS2_MOUSE_SCROLL_BTN_MASK))) {
        // All scroll buttons are pressed

        if (scroll_state == SCROLL_NONE) {
            scroll_button_time = timer_read();
            scroll_state       = SCROLL_BTN;
            scroll_x           = 0;
            scroll_y           = 0;
        }

        // If the mouse has moved, update the report to scroll instead of move the mouse
        if (mouse_report->x || mouse_report->y) {
            scroll_state = SCROLL_SENT;
            scroll_y += mouse_report->y;
            scroll_x += mouse_report->x;
            mouse_report->v = -scroll_y / (PS2_MOUSE_SCROLL_DIVISOR_V);
            mouse_report->h = scroll_x / (PS2_MOUSE_SCROLL_DIVISOR_H);
            scroll_y += (mouse_report->v * (PS2_MOUSE_SCROLL_DIVISOR_V));
            scroll_x -= (mouse_report->h * (PS2_MOUSE_SCROLL_DIVISOR_H));
            mouse_report->x = 0;
            mouse_report->y = 0;
#ifdef PS2_MOUSE_INVERT_H
            mouse_report->h = -mouse_report->h;
#endif
#ifdef PS2_MOUSE_INVERT_V
            mouse_report->v = -mouse_report->v;
#endif
        }
    } else if (0 == (PS2_MOUSE_SCROLL_BTN_MASK & mouse_report->buttons)) {
        // None of the scroll buttons are pressed

#if PS2_MOUSE_SCROLL_BTN_SEND
        if (scroll_state == SCROLL_BTN && timer_elapsed(scroll_button_time) < PS2_MOUSE_SCROLL_BTN_SEND) {
            PRESS_SCROLL_BUTTONS;
            host_mouse_send(mouse_report);
            wait_ms(100);
            RELEASE_SCROLL_BUTTONS;
        }
#endif
        scroll_state = SCROLL_NONE;
    }

    RELEASE_SCROLL_BUTTONS;
}
