/**
 * pointing_device_config.h — Unified pointing device configuration
 * for alliecatowo builds.  (ALLIE-202)
 *
 * Usage
 * -----
 * Include this file from your keyboard's config.h:
 *
 *   #include "users/alliecatowo/pointing_device_config.h"
 *
 * Then define EXACTLY ONE of the selector macros BEFORE including, either in
 * your keyboard's config.h or by passing it via rules.mk OPT_DEFS:
 *
 *   OPT_DEFS += -DHK_POINTING_PIMORONI
 *
 * Selectors
 * ---------
 *   HK_POINTING_PIMORONI      — Pimoroni Trackball (PMW3360, I2C, RGB)
 *   HK_POINTING_CIRQUE_SPI    — Cirque Pinnacle via SPI (MOSI/MISO/SCK/CS)
 *   HK_POINTING_CIRQUE_I2C    — Cirque Pinnacle via I2C (SDA/SCL)
 *   HK_POINTING_PMW3320       — PMW3320 optical sensor (SPI)
 *   HK_POINTING_PMW3360       — PMW3360 high-DPI optical sensor (SPI)
 *   HK_POINTING_AZOTEQ        — Azoteq IQS5xx capacitive multi-touch pad
 *
 * Note: if you are using the holykeebs userspace (users/holykeebs) you
 * normally do NOT need this file — holykeebs manages pointing device
 * configuration through its own rules.mk POINTING_DEVICE variable.
 * This header exists for custom/standalone alliecatowo builds that want a
 * single authoritative pointing device config.
 */

#pragma once

/* ------------------------------------------------------------------ */
/*  Pimoroni Trackball — PMW3360, RGB, I2C                            */
/* ------------------------------------------------------------------ */
#if defined(HK_POINTING_PIMORONI)
#    define POINTING_DEVICE_ENABLE
#    define POINTING_DEVICE_DRIVER pimoroni_trackball

// Non-linear adaptive motion scaling is implemented in users/holykeebs/pimoroni.c
// and guarded by ENABLE_PIMORONI_ADAPTIVE_MOTION.  Enable here if not using
// holykeebs and you've copied that scaling code into your own userspace.
// #define ENABLE_PIMORONI_ADAPTIVE_MOTION

/* ------------------------------------------------------------------ */
/*  Cirque Pinnacle — SPI wiring                                      */
/* ------------------------------------------------------------------ */
#elif defined(HK_POINTING_CIRQUE_SPI)
#    define POINTING_DEVICE_ENABLE
#    define POINTING_DEVICE_DRIVER cirque_pinnacle_spi

// 1-finger tap = left click.
#    define CIRQUE_PINNACLE_TAP_ENABLE

// Drag along the outer ring to scroll.  Requires absolute (position) mode,
// which is automatically selected when TAP_ENABLE is set.
#    define CIRQUE_PINNACLE_CIRCULAR_SCROLL_ENABLE

// Physical diameter of your trackpad.  Common: 35 or 40 mm.
#    define CIRQUE_PINNACLE_DIAMETER_MM 40

// Scroll sensitivity — 8 is conservative; lower = faster.
#    define POINTING_DEVICE_SCROLL_DIVISOR_H 8
#    define POINTING_DEVICE_SCROLL_DIVISOR_V 8

/* ------------------------------------------------------------------ */
/*  Cirque Pinnacle — I2C wiring                                      */
/* ------------------------------------------------------------------ */
#elif defined(HK_POINTING_CIRQUE_I2C)
#    define POINTING_DEVICE_ENABLE
#    define POINTING_DEVICE_DRIVER cirque_pinnacle_i2c

#    define CIRQUE_PINNACLE_TAP_ENABLE
#    define CIRQUE_PINNACLE_CIRCULAR_SCROLL_ENABLE
#    define CIRQUE_PINNACLE_DIAMETER_MM 40

#    define POINTING_DEVICE_SCROLL_DIVISOR_H 8
#    define POINTING_DEVICE_SCROLL_DIVISOR_V 8

// I2C Cirque pads need their poll rate throttled to avoid saturating the bus.
// 10 ms is the official recommended minimum between reads.
#    ifndef POINTING_DEVICE_TASK_THROTTLE_MS
#        define POINTING_DEVICE_TASK_THROTTLE_MS 10
#    endif

/* ------------------------------------------------------------------ */
/*  PMW3320 — optical sensor, SPI                                     */
/* ------------------------------------------------------------------ */
#elif defined(HK_POINTING_PMW3320)
#    define POINTING_DEVICE_ENABLE
#    define POINTING_DEVICE_DRIVER pmw3320

/* ------------------------------------------------------------------ */
/*  PMW3360 — high-DPI optical sensor, SPI                            */
/* ------------------------------------------------------------------ */
#elif defined(HK_POINTING_PMW3360)
#    define POINTING_DEVICE_ENABLE
#    define POINTING_DEVICE_DRIVER pmw3360

/* ------------------------------------------------------------------ */
/*  Azoteq IQS5xx — capacitive multi-touch (up to 5 fingers), I2C    */
/* ------------------------------------------------------------------ */
#elif defined(HK_POINTING_AZOTEQ)
#    define POINTING_DEVICE_ENABLE
#    define POINTING_DEVICE_DRIVER azoteq_iqs5xx

// Gesture support.  These are already enabled by default in the QMK
// azoteq driver, but listed here explicitly for documentation.
#    define AZOTEQ_IQS5XX_TAP_ENABLE           true  // 1-finger tap
#    define AZOTEQ_IQS5XX_TWO_FINGER_TAP_ENABLE true  // 2-finger tap = right-click
#    define AZOTEQ_IQS5XX_SCROLL_ENABLE         true  // 2-finger scroll
#    define AZOTEQ_IQS5XX_PRESS_AND_HOLD_ENABLE true  // press-and-hold

#endif /* pointing device selector */
