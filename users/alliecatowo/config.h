#pragma once

/* Reset. */
#define RP2040_BOOTLOADER_DOUBLE_TAP_RESET
#define RP2040_BOOTLOADER_DOUBLE_TAP_RESET_TIMEOUT 1000U

#define MOUSE_EXTENDED_REPORT
#define WHEEL_EXTENDED_REPORT

// #define POINTING_DEVICE_AUTO_MOUSE_ENABLE
// #define AUTO_MOUSE_DEFAULT_LAYER 4

#undef PRINTF_SUPPORT_DECIMAL_SPECIFIERS
#define PRINTF_SUPPORT_DECIMAL_SPECIFIERS 1

#define EECONFIG_USER_DATA_SIZE 64

#undef MASTER_LEFT
#undef EE_HANDS
#undef MASTER_RIGHT

#if defined(HK_MASTER_LEFT)
    #define MASTER_LEFT
#elif defined(HK_MASTER_RIGHT)
    #define MASTER_RIGHT
#else
    #error "HK_MASTER_LEFT or HK_MASTER_RIGHT not defined in rules.mk"
#endif

#ifdef SPLIT_KEYBOARD
    #define SERIAL_USART_TX_PIN GP1

    // This helps in setups where the keyboard isn't recognized on boot if it's already plugged in.
    #define SPLIT_WATCHDOG_ENABLE
    #define SPLIT_WATCHDOG_TIMEOUT 3000
#endif

#ifdef HK_POINTING_DEVICE_RIGHT_PIMORONI
    #ifdef POINTING_DEVICE_COMBINED
        #define POINTING_DEVICE_ROTATION_90_RIGHT
    #else
        #define POINTING_DEVICE_ROTATION_90
    #endif
#endif
#ifdef HK_POINTING_DEVICE_LEFT_PIMORONI
    #define POINTING_DEVICE_ROTATION_270
#endif

#if defined(HK_POINTING_DEVICE_RIGHT_PIMORONI) || defined(HK_POINTING_DEVICE_LEFT_PIMORONI)
    // When mixing Azoteq and Pimoroni we need to throttle the driver instead of the task.
    #if defined(POINTING_DEVICE_DRIVER_azoteq_iqs5xx)
        #define POINTING_DEVICE_TASK_THROTTLE_MS 1
    #endif
#endif

#ifdef POINTING_DEVICE_DRIVER_azoteq_iqs5xx
    #if defined(HK_POINTING_DEVICE_RIGHT_TPS43) || defined(HK_POINTING_DEVICE_LEFT_TPS43)
        #define AZOTEQ_IQS5XX_TPS43
    #endif

    #if defined(HK_POINTING_DEVICE_RIGHT_TPS43)
        // We define the rotation in rules.mk in case we have a TPS43 on both sides. This is because we need to know
        // which side we're flashing for, and that information is lost outside of rules.mk.
        #if !defined(HK_POINTING_DEVICE_LEFT_TPS43)
            #define AZOTEQ_IQS5XX_ROTATION_180
        #endif
    #endif

    // These are enabled by default.
    // #define AZOTEQ_IQS5XX_TAP_ENABLE true
    // #define AZOTEQ_IQS5XX_TWO_FINGER_TAP_ENABLE true
    // #define AZOTEQ_IQS5XX_SCROLL_ENABLE true
    #define AZOTEQ_IQS5XX_PRESS_AND_HOLD_ENABLE true
#endif

#if defined(OLED_ENABLE) && defined(SPLIT_KEYBOARD)
    #define HK_SPLIT_SYNC_STATE
#endif

#ifdef HK_OLED_ENABLE
#    define OLED_FONT_H "users/alliecatowo/logofont/logofont.c"
#    define OLED_FONT_START 32
#    define OLED_FONT_END 195
#endif

#ifdef HK_SPLIT_SYNC_STATE
    #define SPLIT_LAYER_STATE_ENABLE
    #define SPLIT_TRANSACTION_IDS_USER HK_SYNC_STATE
    #define RPC_M2S_BUFFER_SIZE 64
#endif
