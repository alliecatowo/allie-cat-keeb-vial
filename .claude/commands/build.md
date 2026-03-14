Build the default firmware configuration (trackball_tps43 for both left and right sides):

1. Run: `python3 build.py`
2. Show the build output and confirm the firmware files were generated in `build_lily58/`
3. Note: This requires the ARM cross-compiler (`gcc-arm-none-eabi`). If not available, say so and suggest running the fast Python tests instead: `python3 -m unittest tests.test_build_py -v`
