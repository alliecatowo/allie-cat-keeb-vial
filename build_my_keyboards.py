#!/usr/bin/env python3
"""
Simplified build script for crkbd and lily58 with Vial and trackball support
"""

import sys
import subprocess
import os
from typing import List, Dict, Tuple, Optional

# Configuration for your keyboards
KEYBOARDS = {
    "crkbd": {
        "base": "crkbd/rev1",
        "keymap": "vial",
        "master_side": "left",  # TPS43 is on the left side
    },
    "lily58": {
        "base": "lily58/rev1",
        "keymap": "vial",
        "master_side": "left",  # Adjust if your master is on the right
    },
}

# Common build configurations
COMMON_ARGS = {
    "USER_NAME": "holykeebs",
    "TRACKBALL_RGB_RAINBOW": "yes",
}

# Pointing device configurations
POINTING_CONFIGS = {
    "trackball_tps43": {"device": "trackball_tps43", "description": "Trackball with TPS43"},
    "trackball": {"device": "trackball", "description": "Standard trackball"},
    "none": {"device": "", "description": "No pointing device"},
}


class BuildCommand:
    """Simple build command generator"""

    def __init__(self, keyboard: str, config: Dict, pointing: str, side: Optional[str] = None):
        self.keyboard = keyboard
        self.kb_path = config["base"]
        self.keymap = config["keymap"]
        self.pointing = pointing
        self.side = side
        self.args = dict(COMMON_ARGS)

        # Add pointing device args
        if pointing != "none" and POINTING_CONFIGS[pointing]["device"] is not None:
            self.args["POINTING_DEVICE"] = POINTING_CONFIGS[pointing]["device"]
            if side:
                self.args["SIDE"] = side

    def get_filename(self) -> str:
        """Generate output filename"""
        parts = [
            self.keyboard,
            self.keymap,
            self.pointing,
        ]
        if self.side:
            parts.append(self.side)
        return "_".join(parts) + ".uf2"

    def get_command(self) -> List[str]:
        """Get the make command as a list"""
        cmd = ["make", f"{self.kb_path}:{self.keymap}"]

        # Add all arguments
        for key, value in self.args.items():
            cmd.extend(["-e", f"{key}={value}"])

        # Add parallel build
        cmd.extend(["-j8"])

        return cmd

    def get_command_string(self) -> str:
        """Get the make command as a string for display"""
        return " ".join(self.get_command())


def build_keyboard(command: BuildCommand, output_dir: str = "build") -> bool:
    """Execute build command and move output file"""

    filename = command.get_filename()
    output_path = os.path.join(output_dir, filename)

    # Check if already built
    if os.path.exists(output_path):
        print(f"✓ {filename} already exists, skipping...")
        return True

    print(f"\n🔨 Building {filename}")
    print(f"   Command: {command.get_command_string()}")

    try:
        # Run the build
        result = subprocess.run(command.get_command(), capture_output=True, text=True)

        if result.returncode != 0:
            print(f"❌ Build failed!")
            print(f"   Error: {result.stderr}")
            return False

        # Find and move the output file
        # QMK usually names the file based on the keyboard and keymap
        original_name = f"{command.kb_path.replace('/', '_')}_{command.keymap}.uf2"

        if os.path.exists(original_name):
            os.rename(original_name, output_path)
            print(f"✅ Built successfully: {output_path}")
            return True
        else:
            print(f"⚠️  Warning: Could not find output file {original_name}")
            return False

    except subprocess.CalledProcessError as e:
        print(f"❌ Build failed with error: {e}")
        return False
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return False


def main():
    """Main build script"""

    print("🎹 Corne & Lily58 Vial Build Script")
    print("=" * 40)

    # Create output directory
    output_dir = "build"
    os.makedirs(output_dir, exist_ok=True)

    # Track results
    builds = []
    successful = 0
    failed = 0

    # Build configurations
    configs = []

    # For each keyboard
    for kb_name, kb_config in KEYBOARDS.items():
        print(f"\n📦 Configuring {kb_name}...")

        # Trackball with TPS43 - both sides
        for side in ["left", "right"]:
            cmd = BuildCommand(kb_name, kb_config, "trackball_tps43", side)
            configs.append(cmd)
            print(f"   - {cmd.get_filename()}")

        # Optional: Add more configurations here if needed
        # For example, a version without trackball:
        # cmd = BuildCommand(kb_name, kb_config, 'none')
        # configs.append(cmd)

    # Build all configurations
    print(f"\n🚀 Starting builds ({len(configs)} total)...")

    for i, cmd in enumerate(configs, 1):
        print(f"\n[{i}/{len(configs)}]", end="")
        if build_keyboard(cmd, output_dir):
            successful += 1
        else:
            failed += 1
        builds.append((cmd.get_filename(), cmd.get_command_string()))

    # Summary
    print("\n" + "=" * 40)
    print("📊 Build Summary:")
    print(f"   ✅ Successful: {successful}")
    print(f"   ❌ Failed: {failed}")
    print(f"   📁 Output directory: {output_dir}/")

    # Save build log
    log_file = os.path.join(output_dir, "build_log.txt")
    with open(log_file, "w") as f:
        f.write("Build Commands Log\n")
        f.write("=" * 40 + "\n\n")
        for filename, cmd in builds:
            f.write(f"{filename}:\n{cmd}\n\n")
    print(f"   📝 Build log saved to: {log_file}")

    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
