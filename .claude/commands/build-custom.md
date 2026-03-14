Build a custom firmware configuration. Ask the user for:
1. Which keyboard (default: lily58/rev1)
2. Which keymap (default: vial)
3. Left pointing device (options: trackball, tps43, trackpoint, oled, None)
4. Right pointing device (options: trackball, tps43, trackpoint, oled, None)
5. Which side to build (left or right)
6. Whether to enable debug output

Then build the firmware using these parameters with build.py --build-single.
