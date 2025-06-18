# builddefs/vial.mk
ifeq ($(strip $(VIAL_ENABLE)), yes)
    include $(QUANTUM_DIR)/vial/vial.mk
endif

