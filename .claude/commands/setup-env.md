Set up the development environment for working on this firmware:

1. Check if Python 3.11+ is installed: `python3 --version`
2. Install Python dependencies: `pip3 install -r requirements-dev.txt`
3. Initialize git submodules if not already done: `git submodule update --init --recursive`
4. Verify the fast tests pass: `python3 -m unittest tests.test_build_py -v`
5. Check if ARM build tools are available (optional, for firmware compiles):
   - `arm-none-eabi-gcc --version`
   - `make --version`
   - If missing, install `gcc-arm-none-eabi` via your package manager
6. If ARM tools are available, test a firmware build:
   `python3 build.py --build-single --keyboard lily58/rev1 --keymap vial --left-device trackball --right-device tps43 --side left`

Note: Python steps 1-4 always work. ARM toolchain (steps 5-6) is only needed for firmware compilation.
