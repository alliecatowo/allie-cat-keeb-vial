Run tests to verify firmware correctness:

1. **Fast Python tests (no ARM toolchain needed):**
   - Run: `python3 -m unittest tests.test_build_py -v`
   - These cover all `build.py` logic and complete in < 5 seconds
   - Should always pass; fix any failures before proceeding

2. **Validate CI matrix:**
   - Run: `python3 build.py --generate-matrix-release`
   - Confirms the matrix JSON is valid and outputs correctly

3. **Lint Python files:**
   - Run: `flake8 build.py tools/callgraph.py tests/test_build_py.py`

4. **Full QMK C unit tests (requires ARM toolchain):**
   - Check if `gcc-arm-none-eabi` is available: `arm-none-eabi-gcc --version`
   - If available, run: `make test:all`
   - If not available, skip and note that C tests require the cross-compiler

Report any test failures with details and suggest fixes.
