import subprocess
import os
import sys
import argparse
import json
from itertools import product


def run_command(command_list):
    """Runs a command, streams its output, and checks for errors."""
    print(f"--- Running command: {' '.join(command_list)} ---")
    process = subprocess.Popen(
        command_list, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
    )

    if process.stdout:
        # Stream the output
        for line in iter(process.stdout.readline, ""):
            sys.stdout.write(line)

        process.stdout.close()
    return_code = process.wait()

    if return_code:
        raise subprocess.CalledProcessError(return_code, command_list)


def build_firmware(left_device, right_device, side, oled=False, debug=False):
    """Builds the firmware for a given left and right pointing device configuration and a specific side."""
    keyboard = "lily58/rev1"
    keymap = "vial"
    user_name = "holykeebs"
    build_dir = "build_lily"

    left = None if left_device == 'None' else left_device
    right = None if right_device == 'None' else right_device

    pointing_device_arg = f"{left}_{right}" if left and right else left or right
    if not pointing_device_arg:
        pointing_device_arg = "default"

    os.makedirs(build_dir, exist_ok=True)

    variant_suffix = ""
    if oled:
        variant_suffix += "_oled"
    if debug:
        variant_suffix += "_debug"

    target_name = f"lily58_rev1_{keymap}_{pointing_device_arg}{variant_suffix}_flash_on_{side}"
    command = [
        "make", f"{keyboard}:{keymap}", f"-e", f"USER_NAME={user_name}",
        f"-e", f"POINTING_DEVICE={pointing_device_arg}", f"-e", f"SIDE={side}",
        f"-e", f"TARGET={target_name}", "-j8"
    ]

    current_device = left if side == 'left' else right
    if current_device == "trackball":
        command.extend(["-e", "TRACKBALL_RGB_RAINBOW=yes"])

    if oled:
        command.extend(["-e", "OLED_ENABLE=yes"])
    if debug:
        command.extend(["-e", "CONSOLE_ENABLE=yes"])

    try:
        print(f"\\n{'='*20}\\nBuilding {side.upper()} side for {pointing_device_arg}{variant_suffix}...\\n{'='*20}")
        run_command(command)
        firmware_path = f"{target_name}.uf2"
        os.rename(firmware_path, os.path.join(build_dir, firmware_path))
        print(f"✅ Success! {side.upper()} side firmware moved to: {build_dir}/")
        return True
    except (subprocess.CalledProcessError, FileNotFoundError) as e:
        print(f"\\n❌ Error during build for {side.upper()} side of {pointing_device_arg}: {e}")
        return False


def generate_matrix(matrix_type='all'):
    """Generates a JSON matrix for all build variants."""
    devices = ["trackball", "tps43", "trackpoint", "cirque35", "cirque40", "None"]
    sides = ["left", "right"]
    oled_options = [True, False]
    matrix = {'include': []}

    if matrix_type == 'debug':
        debug_options = [True]
    elif matrix_type == 'release':
        debug_options = [False]
    else: # 'all'
        debug_options = [True, False]

    device_pairs = list(product(devices, repeat=2))

    for (left, right), oled, debug in product(device_pairs, oled_options, debug_options):
        # Skip 'None-None' for release builds to reduce clutter, but keep for debug
        if not debug and left == 'None' and right == 'None':
            continue

        for side in sides:
            matrix['include'].append({
                "keymap": "vial",
                "left_device": left,
                "right_device": right,
                "side": side,
                "oled": oled,
                "debug": debug,
            })
    print(json.dumps(matrix))


def main():
    """Builds firmware for specific or all configurations."""
    parser = argparse.ArgumentParser(description="Build Lily58 firmware for various pointing device configurations.")
    parser.add_argument('--generate-matrix', action='store_true', help='Generate a build matrix for CI.')
    parser.add_argument('--matrix-type', choices=['all', 'debug', 'release'], default='all', help='Specify the type of matrix to generate.')
    parser.add_argument('--build-personal', action='store_true', help='Build personal (trackball/tps43) firmware, debug and release.')
    parser.add_argument('--build-single', action='store_true', help='Build a single firmware variant with specific options.')
    parser.add_argument('--left-device', default='None', help='Left pointing device.')
    parser.add_argument('--right-device', default='None', help='Right pointing device.')
    parser.add_argument('--side', choices=['left', 'right'], help='The side to build for.')
    parser.add_argument('--oled', action='store_true', help='Enable OLED screen support.')
    parser.add_argument('--debug', action='store_true', help='Enable console debug output.')

    args = parser.parse_args()

    if args.generate_matrix:
        generate_matrix(args.matrix_type)
        return

    if args.build_single:
        if not args.side:
            print("Error: --side is required for a single build.")
            sys.exit(1)
        print(f"Starting single build for left:{args.left_device}, right:{args.right_device}, side:{args.side}, oled:{args.oled}, debug:{args.debug}...")
        if not build_firmware(args.left_device, args.right_device, args.side, args.oled, args.debug):
            sys.exit(1)
        print("\\nBuild complete!")
        return

    # Default action is to build personal versions
    if args.build_personal or not (args.generate_matrix or args.build_single):
        print("Starting build for personal configuration (trackball/tps43), both normal and debug...")

        # Normal build
        print("\\n--- Building Personal Config: Normal ---")
        if not build_firmware("trackball", "tps43", "left", oled=True): sys.exit(1)
        if not build_firmware("trackball", "tps43", "right", oled=True): sys.exit(1)

        # Debug build
        print("\\n--- Building Personal Config: Debug ---")
        if not build_firmware("trackball", "tps43", "left", oled=True, debug=True): sys.exit(1)
        if not build_firmware("trackball", "tps43", "right", oled=True, debug=True): sys.exit(1)

        print("\\nAll personal builds complete!")


if __name__ == "__main__":
    main()
