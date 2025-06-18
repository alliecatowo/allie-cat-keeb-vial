# vial.mk
ifeq ($(strip $(VIAL_ENABLE)), yes)
    ifeq ($(strip $(VIA_ENABLE)), yes)
        # For VIA_ENABLE keyboards that want to opt-in to Vial features
        # Add vial subdirectory
        VPATH += $(QUANTUM_DIR)/vial
        # Add vial sources
        SRC += vial.c
        # Add vial flags
        OPT_DEFS += -DVIAL_ENABLE
        ifneq ($(strip $(VIAL_INSECURE)), no)
            OPT_DEFS += -DVIAL_INSECURE
        endif

        # Generate vial_generated_keyboard_definition.h
        VPATH += $(BUILD_DIR)
        VIAL_GEN_H = $(BUILD_DIR)/vial_generated_keyboard_definition.h
        $(VIAL_GEN_H): $(KEYBOARD_H)
	        @echo "Generating $(subst $(BUILD_DIR)/,,$@)"
	        @$(PYTHON) $(QUANTUM_DIR)/vial/vial_ctohex.py $< > $@
        DEPS_H += $(VIAL_GEN_H)
    endif
endif
