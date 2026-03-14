Run the QMK test suite to verify firmware correctness:

1. Check if there are any specific tests for lily58 or holykeebs
2. Run basic QMK tests: make test:all
3. If that's too extensive, run: make test:basic
4. Report any test failures with details
5. Check if pointing device tests exist and run them

This ensures code changes don't break existing functionality.
