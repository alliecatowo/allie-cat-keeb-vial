import sys
import subprocess
import os
import argparse
import json


class Command:
    def __init__(self, kb, km) -> None:
        self.kb = kb
        self.km = km
        self.arguments = []

    def prepend_argument(self, argument):
        self.arguments.insert(0, argument)
        self.arguments.insert(0, '-e')

    def add_argument(self, argument):
        self.arguments.append('-e')
        self.arguments.append(argument)

    def add_argument_raw(self, argument):
        self.arguments.append(argument)

    def build(self):
        return ' '.join(self.build_list())

    def build_list(self):
        return ['make', f'{self.kb}:{self.km}'] + self.arguments

    def file_name(self):
        parts = []
        parts.append(self.kb.replace('/', '_'))
        parts.append(self.km)
        for argument in self.arguments:
            if argument.startswith('POINTING_DEVICE='):
                pointing_device = argument[len('POINTING_DEVICE='):]
                parts.append(pointing_device)
            elif argument.startswith('SIDE='):
                side = argument[len('SIDE='):]
                parts.append(side)
            elif argument.startswith('POINTING_DEVICE_POSITION='):
                pointing_device_position = argument[len('POINTING_DEVICE_POSITION='):]
                parts.append(pointing_device_position)
            elif argument.startswith('OLED='):
                parts.append('oled')
            elif argument.startswith('CONSOLE='):
                parts.insert(-1, 'debug')  # Insert before the last part (side)
        return '_'.join(parts)


def generate_matrix(matrix_type='all'):
    """Generate CI matrix for trackball_tsp43 only"""
    matrix = {'include': [
        {
            "keyboard": "lily58/rev1",
            "keyboard_name": "lily58_rev1",
            "keymap": "vial",
            "left_device": "trackball",
            "right_device": "tps43",
            "side": "left",
            "debug": False,
        },
        {
            "keyboard": "lily58/rev1",
            "keyboard_name": "lily58_rev1",
            "keymap": "vial",
            "left_device": "trackball",
            "right_device": "tps43",
            "side": "right",
            "debug": False,
        }
    ]}
    print(json.dumps(matrix))


def run_command_check_output(command):
    print(f'Running: {command}')
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
    )

    if process.stdout:
        for line in iter(process.stdout.readline, ""):
            sys.stdout.write(line)
        process.stdout.close()
    return_code = process.wait()

    if return_code:
        raise subprocess.CalledProcessError(return_code, command)


def main():
    parser = argparse.ArgumentParser(description="Build lily58 firmware configurations.")

    actions = parser.add_argument_group('Actions')
    actions.add_argument('--generate-matrix-debug', action='store_true', help='Generate debug matrix for CI.')
    actions.add_argument('--generate-matrix-release', action='store_true', help='Generate release matrix for CI.')
    actions.add_argument('--build-personal', action='store_true', help='Build personal config.')
    actions.add_argument('--build-single', action='store_true', help='Build single variant.')
    actions.add_argument('--build-all', action='store_true', help='Build all configurations.')

    options = parser.add_argument_group('Build Options')
    options.add_argument('--keyboard', default='lily58/rev1', help='Keyboard to build.')
    options.add_argument('--keymap', default='vial', help='Keymap to build.')
    options.add_argument('--user-name', default='holykeebs', help='QMK user name.')
    options.add_argument('--left-device', default='None', help='Left device.')
    options.add_argument('--right-device', default='None', help='Right device.')
    options.add_argument('--side', choices=['left', 'right'], help='Side to build.')
    options.add_argument('--debug', action='store_true', help='Enable debug.')

    args = parser.parse_args()

    if args.generate_matrix_debug or args.generate_matrix_release:
        generate_matrix('release')
        return

    if args.build_single:
        # Build single configuration for CI
        command = Command(args.keyboard, args.keymap)
        command.prepend_argument(f'USER_NAME={args.user_name}')

        if args.debug:
            command.add_argument('CONSOLE=yes')

        # Handle device configuration
        if args.left_device != 'None' and args.right_device != 'None':
            command.add_argument(f'POINTING_DEVICE={args.left_device}_{args.right_device}')
            command.add_argument(f'SIDE={args.side}')
            current_device = args.left_device if args.side == 'left' else args.right_device
            if current_device == 'trackball':
                command.add_argument('TRACKBALL_RGB_RAINBOW=yes')
        elif args.left_device != 'None':
            command.add_argument(f'POINTING_DEVICE={args.left_device}')
            command.add_argument('POINTING_DEVICE_POSITION=left')
            if args.left_device == 'trackball':
                command.add_argument('TRACKBALL_RGB_RAINBOW=yes')
        elif args.right_device != 'None':
            command.add_argument(f'POINTING_DEVICE={args.right_device}')
            command.add_argument('POINTING_DEVICE_POSITION=right')
            if args.right_device == 'trackball':
                command.add_argument('TRACKBALL_RGB_RAINBOW=yes')

        # Handle OLED
        if args.left_device == 'oled' or args.right_device == 'oled':
            command.add_argument('OLED=yes')
            if args.left_device not in ['None', 'oled'] or args.right_device not in ['None', 'oled']:
                command.add_argument('OLED_FLIP=yes')

        build_dir = f"build_{args.keyboard.split('/')[0]}"
        os.makedirs(build_dir, exist_ok=True)

        command.add_argument_raw('-j8')
        command.prepend_argument(f'TARGET={command.file_name()}')

        try:
            print(f"Building {command.file_name()}...")
            run_command_check_output(command.build().split())
            os.rename(f'{command.file_name()}.uf2', f'{build_dir}/{command.file_name()}.uf2')
            print(f"✅ Success! Firmware moved to: {build_dir}/")
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            print(f"❌ Error during build: {e}")
            sys.exit(1)
        return

    # Default: build trackball_tsp43 only
    if args.build_personal or args.build_all or not any(vars(args).values()):
        kb = 'lily58/rev1'
        os.makedirs('build_lily58', exist_ok=True)

        # Build both sides of trackball_tsp43
        for side in ('left', 'right'):
            command = Command(kb, 'vial')
            command.prepend_argument('USER_NAME=holykeebs')
            command.add_argument('POINTING_DEVICE=trackball_tps43')
            command.add_argument(f'SIDE={side}')
            command.add_argument('TRACKBALL_RGB_RAINBOW=yes')
            command.add_argument_raw('-j8')
            command.prepend_argument(f'TARGET={command.file_name()}')

            try:
                print(f"Building {command.file_name()}...")
                run_command_check_output(command.build().split())
                os.rename(f'{command.file_name()}.uf2', f'build_lily58/{command.file_name()}.uf2')
                print(f"✅ Success!")
            except (subprocess.CalledProcessError, FileNotFoundError) as e:
                print(f"❌ Error building {command.file_name()}: {e}")
                sys.exit(1)


if __name__ == '__main__':
    main()
