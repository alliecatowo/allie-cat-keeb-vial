ROOT_DIR := $(abspath $(dir $(lastword $(MAKEFILE_LIST)))..)
UNITY_DIR := $(ROOT_DIR)/test
BUILD_DIR ?= $(ROOT_DIR)/tests/BUILD

CC ?= clang
CFLAGS ?= -Wall -Wextra -I$(UNITY_DIR) -I$(ROOT_DIR)/tests/test_common -I$(ROOT_DIR) -DMATRIX_ROWS=5 -DMATRIX_COLS=15

TEST_BINS := $(addprefix $(BUILD_DIR)/,$(TESTS))

$(BUILD_DIR):
	mkdir -p $(BUILD_DIR)

$(BUILD_DIR)/%: $(ROOT_DIR)/tests/%.c $(UNITY_DIR)/unity.c | $(BUILD_DIR)
	$(CC) $(CFLAGS) $^ -o $@

all: $(TEST_BINS)

run: all
	for t in $(TEST_BINS); do $$t; done

clean:
	rm -rf $(BUILD_DIR)

.PHONY: all run clean
