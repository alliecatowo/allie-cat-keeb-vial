#include "unity.h"

#ifndef MATRIX_ROWS
#define MATRIX_ROWS 5
#endif
#ifndef MATRIX_COLS
#define MATRIX_COLS 15
#endif

void matrix_init(void) {}

void setUp(void) {
    matrix_init();
}

void tearDown(void) {}

void test_matrix_size(void) {
    TEST_ASSERT_EQUAL_INT(5, MATRIX_ROWS);
    TEST_ASSERT_EQUAL_INT(15, MATRIX_COLS);
}

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_matrix_size);
    return UNITY_END();
}
