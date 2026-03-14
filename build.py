import sys
import subprocess
import os
import argparse
import json


# All valid pointing device configurations from users/holykeebs/rules.mk.
# Single-device configs are built twice: once with POINTING_DEVICE_POSITION=left,
# once with POINTING_DEVICE_POSITION=right.
# Dual-device configs are built twice: once with SIDE=left, once with SIDE=right.
SINGLE_DEVICE_CONFIGS = [
    'trackball', 'tps43', 'trackpoint',
]
DUAL_DEVICE_CONFIGS = [
    'tps43_tps43', 'trackball_trackball',
    'trackball_tps43', 'tps43_trackball',
    'trackpoint_tps43', 'tps43_trackpoint',
    'trackpoint_trackball', 'trackball_trackpoint',
]


def generate_matrix():
    """Generate CI matrix for all valid pointing device configs (lily58) and plain vial (sofle)."""
    matrix = {'include': []}

    # lily58/rev1 — holykeebs userspace, full pointing device matrix × OLED on/off
    for device in SINGLE_DEVICE_CONFIGS:
        for position in ['left', 'right']:
            for oled in ['yes', 'no']:
                matrix['include'].append({
                    'keyboard': 'lily58/rev1',
                    'keyboard_safe': 'lily58_rev1',
                    'keymap': 'vial',
                    'pointing_device': device,
                    'side': position,
                    'oled': oled,
                })

    for device in DUAL_DEVICE_CONFIGS:
        for side in ['left', 'right']:
            for oled in ['yes', 'no']:
                matrix['include'].append({
                    'keyboard': 'lily58/rev1',
                    'keyboard_safe': 'lily58_rev1',
                    'keymap': 'vial',
                    'pointing_device': device,
                    'side': side,
                    'oled': oled,
                })

    # sofle/rev1 — plain vial, no pointing device, no oled toggle (OLED handled by keymap)
    matrix['include'].append({
        'keyboard': 'sofle/rev1',
        'keyboard_safe': 'sofle_rev1',
        'keymap': 'vial',
        'pointing_device': '',
        'side': '',
        'oled': '',
    })

    print(json.dumps(matrix))


def run_command_check_output(command):
    print(f'Running: {" ".join(command)}')
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True
    )

    if process.stdout:
        for line in iter(process.stdout.readline, ''):
            sys.stdout.write(line)
        process.stdout.close()
    return_code = process.wait()

    if return_code:
        raise subprocess.CalledProcessError(return_code, command)


def build_single(keyboard, keymap, pointing_device, side, oled='', user_name='holykeebs'):
    """Build a single firmware variant."""
    kb_safe = keyboard.replace('/', '_')
    name_parts = [kb_safe, keymap]

    command = ['make', f'{keyboard}:{keymap}']

    if pointing_device:
        command += ['-e', f'USER_NAME={user_name}']
        command += ['-e', f'POINTING_DEVICE={pointing_device}']

        if '_' in pointing_device:
            # Dual-device config: SIDE selects which physical device this half uses
            command += ['-e', f'SIDE={side}']
        else:
            # Single-device config: POINTING_DEVICE_POSITION selects which half carries it
            command += ['-e', f'POINTING_DEVICE_POSITION={side}']

        if 'trackball' in pointing_device:
            command += ['-e', 'TRACKBALL_RGB_RAINBOW=yes']

        name_parts += [pointing_device, side]

    if oled == 'yes':
        command += ['-e', 'OLED=yes']
        name_parts.append('oled')

    target = '_'.join(name_parts)
    command += ['-e', f'TARGET={target}', '-j8']

    build_dir = f"build_{keyboard.split('/')[0]}"
    os.makedirs(build_dir, exist_ok=True)

    print(f'Building {target}...')
    run_command_check_output(command)

    ext = 'uf2' if 'lily' in keyboard else 'hex'
    src = f'{target}.{ext}'
    dst = os.path.join(build_dir, f'{target}.{ext}')
    os.rename(src, dst)
    print(f'✅ Success! Firmware at: {dst}')


def main():
    parser = argparse.ArgumentParser(description='Build QMK firmware for lily58 and sofle keyboards.')

    actions = parser.add_argument_group('Actions')
    actions.add_argument('--generate-matrix-debug', action='store_true', help='Generate CI build matrix.')
    actions.add_argument('--generate-matrix-release', action='store_true', help='Generate CI build matrix.')
    actions.add_argument('--build-personal', action='store_true', help='Build personal config (trackball_tps43, both sides).')
    actions.add_argument('--build-single', action='store_true', help='Build a single variant (used by CI).')
    actions.add_argument('--build-all', action='store_true', help='Build all configurations locally.')

    options = parser.add_argument_group('Build Options')
    options.add_argument('--keyboard', default='lily58/rev1', help='Keyboard to build.')
    options.add_argument('--keymap', default='vial', help='Keymap to build.')
    options.add_argument('--user-name', default='holykeebs', help='QMK user name for holykeebs userspace.')
    options.add_argument('--pointing-device', default='', help='POINTING_DEVICE value (e.g. trackball, trackball_tps43).')
    options.add_argument('--side', choices=['left', 'right', ''], default='', help='Side to build (left/right).')
    options.add_argument('--oled', choices=['yes', 'no', ''], default='', help='Build with OLED support (yes/no).')

    args = parser.parse_args()

    if args.generate_matrix_debug or args.generate_matrix_release:
        generate_matrix()
        return

    if args.build_single:
        # Build single configuration for CI
        command = Command(args.keyboard, args.keymap)
        command.prepend_argument(f'USER_NAME={args.user_name}')
        if args.keymap == 'vial':
            command.add_argument('VIAL_ENABLE=yes')

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

    if args.build_all:
        errors = []
        # lily58: all pointing device configs × OLED on/off
        for device in SINGLE_DEVICE_CONFIGS:
            for position in ['left', 'right']:
                for oled in ['yes', 'no']:
                    try:
                        build_single('lily58/rev1', 'vial', device, position, oled, args.user_name)
                    except (subprocess.CalledProcessError, FileNotFoundError) as e:
                        errors.append(str(e))
        for device in DUAL_DEVICE_CONFIGS:
            for side in ['left', 'right']:
                for oled in ['yes', 'no']:
                    try:
                        build_single('lily58/rev1', 'vial', device, side, oled, args.user_name)
                    except (subprocess.CalledProcessError, FileNotFoundError) as e:
                        errors.append(str(e))
        # sofle: plain vial
        try:
            build_single('sofle/rev1', 'vial', '', '', '')
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            errors.append(str(e))
        if errors:
            print(f'\n❌ {len(errors)} build(s) failed.')
            sys.exit(1)
        print('\n✅ All builds complete!')
        return

    # Default: build trackball_tsp43 only
    if args.build_personal or args.build_all or not any(vars(args).values()):
        kb = 'lily58/rev1'
        os.makedirs('build_lily58', exist_ok=True)

        # Build both sides of trackball_tsp43
        for side in ('left', 'right'):
            command = Command(kb, 'vial')
            command.prepend_argument('USER_NAME=holykeebs')
            command.add_argument('VIAL_ENABLE=yes')
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
