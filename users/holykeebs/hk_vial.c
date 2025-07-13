#include "vial.h"
#include "holykeebs.h"
#include "pointing.h"

// FEATURE IDs – keep enum order in sync with vial.json
enum {
    FEAT_MAIN_DPI = 0,
    FEAT_MAIN_SNIPE,
    FEAT_MAIN_SCROLL_BUF,
    FEAT_MAIN_DRAG,
    FEAT_MAIN_SCROLL_LOCK,
    FEAT_PERI_DPI,
    FEAT_PERI_SNIPE,
    FEAT_PERI_SCROLL_BUF,
    FEAT_PERI_DRAG,
    FEAT_PERI_SCROLL_LOCK,
    FEAT_COUNT      // must be last
};

bool vial_user_feature_get(uint8_t id, void *data, uint8_t *sz) {
    switch (id) {
        case FEAT_MAIN_DPI:         *((uint8_t*)data)=g_hk_state.main.pointer_default_multiplier*100; *sz=1; return true;
        case FEAT_MAIN_SNIPE:       *((uint8_t*)data)=g_hk_state.main.pointer_sniping_multiplier*100;  *sz=1; return true;
        case FEAT_MAIN_SCROLL_BUF:  *((uint8_t*)data)=g_hk_state.main.pointer_scroll_buffer_size;      *sz=1; return true;
        case FEAT_MAIN_DRAG:        *((bool  *)data)=g_hk_state.main.drag_scroll;                      *sz=1; return true;
        case FEAT_MAIN_SCROLL_LOCK: *((uint8_t*)data)=g_hk_state.main.scroll_lock;                     *sz=1; return true;
        case FEAT_PERI_DPI:         *((uint8_t*)data)=g_hk_state.peripheral.pointer_default_multiplier*100; *sz=1; return true;
        case FEAT_PERI_SNIPE:       *((uint8_t*)data)=g_hk_state.peripheral.pointer_sniping_multiplier*100;  *sz=1; return true;
        case FEAT_PERI_SCROLL_BUF:  *((uint8_t*)data)=g_hk_state.peripheral.pointer_scroll_buffer_size;      *sz=1; return true;
        case FEAT_PERI_DRAG:        *((bool  *)data)=g_hk_state.peripheral.drag_scroll;                      *sz=1; return true;
        case FEAT_PERI_SCROLL_LOCK: *((uint8_t*)data)=g_hk_state.peripheral.scroll_lock;                     *sz=1; return true;
    }
    return false;
}

bool vial_user_feature_set(uint8_t id, const void *data, uint8_t sz) {
    if (sz!=1) return false;
    switch (id) {
        case FEAT_MAIN_DPI:         g_hk_state.main.pointer_default_multiplier      = *((uint8_t*)data)/100.0; break;
        case FEAT_MAIN_SNIPE:       g_hk_state.main.pointer_sniping_multiplier      = *((uint8_t*)data)/100.0; break;
        case FEAT_MAIN_SCROLL_BUF:  g_hk_state.main.pointer_scroll_buffer_size      = *((uint8_t*)data);       break;
        case FEAT_MAIN_DRAG:        g_hk_state.main.drag_scroll                     = *((bool  *)data);        break;
        case FEAT_MAIN_SCROLL_LOCK: g_hk_state.main.scroll_lock                     = *((uint8_t*)data);       break;
        case FEAT_PERI_DPI:         g_hk_state.peripheral.pointer_default_multiplier= *((uint8_t*)data)/100.0; break;
        case FEAT_PERI_SNIPE:       g_hk_state.peripheral.pointer_sniping_multiplier= *((uint8_t*)data)/100.0; break;
        case FEAT_PERI_SCROLL_BUF:  g_hk_state.peripheral.pointer_scroll_buffer_size= *((uint8_t*)data);       break;
        case FEAT_PERI_DRAG:        g_hk_state.peripheral.drag_scroll               = *((bool  *)data);        break;
        case FEAT_PERI_SCROLL_LOCK: g_hk_state.peripheral.scroll_lock               = *((uint8_t*)data);       break;
        default: return false;
    }
    g_hk_state.dirty = true;
    return true;
}
