#include <stddef.h>
#include <stdint.h>
#include <string.h>

#include "qmk_settings.h"
#include "holykeebs.h"
#include "pointing.h"

static int hk_settings_write_u16(void *setting, size_t maxsz, uint16_t value) {
    if (maxsz < sizeof(uint16_t)) {
        return -1;
    }
    memcpy(setting, &value, sizeof(uint16_t));
    return 0;
}

static uint16_t hk_multiplier_to_setting(float multiplier) {
    if (multiplier < 0) {
        multiplier = 0;
    }
    return (uint16_t)(multiplier * 100);
}

static float hk_multiplier_from_setting(uint16_t value) {
    if (value == 0) {
        value = 1;
    }
    return value / 100.0f;
}

static uint16_t hk_scroll_buffer_to_setting(uint8_t size) {
    return size;
}

static uint8_t hk_scroll_buffer_from_setting(uint16_t value) {
    return value > UINT8_MAX ? UINT8_MAX : (uint8_t)value;
}

static uint16_t hk_bool_to_setting(bool value) {
    return value ? 1 : 0;
}

static bool hk_bool_from_setting(uint16_t value) {
    return value != 0;
}

int qmk_settings_user_get(uint16_t qsid, void *setting, size_t maxsz) {
    switch (qsid) {
        case 9:
            return hk_settings_write_u16(setting, maxsz, hk_bool_to_setting(g_hk_state.main.drag_scroll));
        case 10:
            return hk_settings_write_u16(setting, maxsz, g_hk_state.main.scroll_lock);
        case 11:
            return hk_settings_write_u16(setting, maxsz, hk_multiplier_to_setting(g_hk_state.main.pointer_default_multiplier));
        case 12:
            return hk_settings_write_u16(setting, maxsz, hk_multiplier_to_setting(g_hk_state.main.pointer_sniping_multiplier));
        case 13:
            return hk_settings_write_u16(setting, maxsz, hk_scroll_buffer_to_setting(g_hk_state.main.pointer_scroll_buffer_size));
        case 14:
            return hk_settings_write_u16(setting, maxsz, hk_multiplier_to_setting(g_hk_state.peripheral.pointer_default_multiplier));
        case 15:
            return hk_settings_write_u16(setting, maxsz, hk_multiplier_to_setting(g_hk_state.peripheral.pointer_sniping_multiplier));
        case 16:
            return hk_settings_write_u16(setting, maxsz, hk_bool_to_setting(g_hk_state.peripheral.drag_scroll));
        case 17:
            return hk_settings_write_u16(setting, maxsz, hk_scroll_buffer_to_setting(g_hk_state.peripheral.pointer_scroll_buffer_size));
        default:
            return QMK_SETTINGS_USER_NOT_HANDLED;
    }
}

int qmk_settings_user_set(uint16_t qsid, const void *setting, size_t maxsz) {
    if (maxsz < sizeof(uint16_t)) {
        return -1;
    }

    const uint8_t *bytes = (const uint8_t *)setting;
    uint16_t value = (uint16_t)(bytes[0] | (bytes[1] << 8));

    switch (qsid) {
        case 9:
            g_hk_state.main.drag_scroll = hk_bool_from_setting(value);
            break;
        case 10:
            if (value > SCROLL_LOCK_VERTICAL) {
                value = SCROLL_LOCK_OFF;
            }
            g_hk_state.main.scroll_lock = (hk_scroll_lock)value;
            g_hk_state.peripheral.scroll_lock = (hk_scroll_lock)value;
            break;
        case 11:
            g_hk_state.main.pointer_default_multiplier = hk_multiplier_from_setting(value);
            break;
        case 12:
            g_hk_state.main.pointer_sniping_multiplier = hk_multiplier_from_setting(value);
            break;
        case 13:
            g_hk_state.main.pointer_scroll_buffer_size = hk_scroll_buffer_from_setting(value);
            g_hk_state.peripheral.pointer_scroll_buffer_size = hk_scroll_buffer_from_setting(value);
            break;
        case 14:
            g_hk_state.peripheral.pointer_default_multiplier = hk_multiplier_from_setting(value);
            break;
        case 15:
            g_hk_state.peripheral.pointer_sniping_multiplier = hk_multiplier_from_setting(value);
            break;
        case 16:
            g_hk_state.peripheral.drag_scroll = hk_bool_from_setting(value);
            break;
        case 17:
            g_hk_state.peripheral.pointer_scroll_buffer_size = hk_scroll_buffer_from_setting(value);
            break;
        default:
            return QMK_SETTINGS_USER_NOT_HANDLED;
    }

    g_hk_state.dirty = true;
    hk_write_eeconfig();
    return 0;
}
