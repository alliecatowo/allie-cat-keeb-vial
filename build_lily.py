import subprocess
import os
import sys


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


def main():
    """
    Builds the firmware for the Lily58 with a left trackball and right tps43.
    """
    # Configuration
    keyboard = "lily58/rev1"
    keymap = "vial"
    user_name = "holykeebs"
    left_device = "trackball"
    right_device = "tps43"
    pointing_device_arg = f"{left_device}_{right_device}"
    build_dir = "build_lily"
    firmware_path = "" # Initialize to empty string

    os.makedirs(build_dir, exist_ok=True)

    # --- Build for LEFT side (with the trackball) ---
    left_target_name = (
        f"lily58_rev1_{keymap}_{left_device}_{right_device}_flash_on_left"
    )
    left_command = [
        "make",
        f"{keyboard}:{keymap}",
        f"-e",
        f"USER_NAME={user_name}",
        f"-e",
        f"POINTING_DEVICE={pointing_device_arg}",
        f"-e",
        "SIDE=left",
        f"-e",
        "TRACKBALL_RGB_RAINBOW=yes",
        f"-e",
        f"TARGET={left_target_name}",
        "-j8",
    ]

    # --- Build for RIGHT side (with the tps43) ---
    right_target_name = (
        f"lily58_rev1_{keymap}_{left_device}_{right_device}_flash_on_right"
    )
    right_command = [
        "make",
        f"{keyboard}:{keymap}",
        f"-e",
        f"USER_NAME={user_name}",
        f"-e",
        f"POINTING_DEVICE={pointing_device_arg}",
        f"-e",
        "SIDE=right",
        f"-e",
        f"TARGET={right_target_name}",
        "-j8",
    ]

    try:
        print(f"\\n{'='*20}\\nBuilding LEFT side firmware...\\n{'='*20}")
        run_command(left_command)
        firmware_path = f"{left_target_name}.uf2"
        os.rename(firmware_path, os.path.join(build_dir, firmware_path))
        print(f"✅ Success! Left side firmware moved to: {build_dir}/")

        print(f"\\n{'='*20}\\nBuilding RIGHT side firmware...\\n{'='*20}")
        run_command(right_command)
        firmware_path = f"{right_target_name}.uf2"
        os.rename(firmware_path, os.path.join(build_dir, firmware_path))
        print(f"✅ Success! Right side firmware moved to: {build_dir}/")

        print("\\nAll builds complete!")

    except subprocess.CalledProcessError:
        print(
            "\\n❌ Error: A build command failed. Please check the output above for details."
        )
        sys.exit(1)
    except FileNotFoundError:
        print(
            f"\\n❌ Error: Could not find the compiled firmware file '{firmware_path}'."
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
