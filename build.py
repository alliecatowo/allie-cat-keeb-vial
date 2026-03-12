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
    'trackball', 'tps43', 'cirque40', 'cirque35', 'trackpoint',
]
DUAL_DEVICE_CONFIGS = [
    'tps43_tps43', 'cirque35_cirque35', 'cirque40_cirque40', 'trackball_trackball',
    'trackball_tps43', 'tps43_trackball',
    'trackball_cirque35', 'cirque35_trackball',
    'trackball_cirque40', 'cirque40_trackball',
    'trackpoint_tps43', 'tps43_trackpoint',
    'trackpoint_trackball', 'trackball_trackpoint',
    'trackpoint_cirque35', 'cirque35_trackpoint',
    'trackpoint_cirque40', 'cirque40_trackpoint',
    'cirque40_tps43', 'tps43_cirque40',
    'cirque35_tps43', 'tps43_cirque35',
]


def generate_matrix():
    """Generate CI matrix for all valid pointing device configs (lily58) and plain vial (sofle)."""
    matrix = {'include': []}

    # lily58/rev1 — holykeebs userspace, full pointing device matrix
    for device in SINGLE_DEVICE_CONFIGS:
        for position in ['left', 'right']:
            matrix['include'].append({
                'keyboard': 'lily58/rev1',
                'keyboard_safe': 'lily58_rev1',
                'keymap': 'vial',
                'pointing_device': device,
                'side': position,
            })

    for device in DUAL_DEVICE_CONFIGS:
        for side in ['left', 'right']:
            matrix['include'].append({
                'keyboard': 'lily58/rev1',
                'keyboard_safe': 'lily58_rev1',
                'keymap': 'vial',
                'pointing_device': device,
                'side': side,
            })

    # sofle/rev1 — plain vial, no pointing device
    matrix['include'].append({
        'keyboard': 'sofle/rev1',
        'keyboard_safe': 'sofle_rev1',
        'keymap': 'vial',
        'pointing_device': '',
        'side': '',
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


def build_single(keyboard, keymap, pointing_device, side, user_name='holykeebs'):
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
    options.add_argument('--side', choices=['left', 'right'], default='', help='Side to build (left/right).')

    args = parser.parse_args()

    if args.generate_matrix_debug or args.generate_matrix_release:
        generate_matrix()
        return

    if args.build_single:
        try:
            build_single(args.keyboard, args.keymap, args.pointing_device, args.side, args.user_name)
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            print(f'❌ Build error: {e}')
            sys.exit(1)
        return

    if args.build_all:
        errors = []
        # lily58: all pointing device configs
        for device in SINGLE_DEVICE_CONFIGS:
            for position in ['left', 'right']:
                try:
                    build_single('lily58/rev1', 'vial', device, position, args.user_name)
                except (subprocess.CalledProcessError, FileNotFoundError) as e:
                    errors.append(str(e))
        for device in DUAL_DEVICE_CONFIGS:
            for side in ['left', 'right']:
                try:
                    build_single('lily58/rev1', 'vial', device, side, args.user_name)
                except (subprocess.CalledProcessError, FileNotFoundError) as e:
                    errors.append(str(e))
        # sofle: plain vial
        try:
            build_single('sofle/rev1', 'vial', '', '')
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            errors.append(str(e))
        if errors:
            print(f'\n❌ {len(errors)} build(s) failed.')
            sys.exit(1)
        print('\n✅ All builds complete!')
        return

    # Default / --build-personal: personal config (trackball_tps43, both sides)
    os.makedirs('build_lily58', exist_ok=True)
    for side in ('left', 'right'):
        try:
            build_single('lily58/rev1', 'vial', 'trackball_tps43', side, args.user_name)
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            print(f'❌ Error: {e}')
            sys.exit(1)
    print('\n✅ Personal build complete!')


if __name__ == '__main__':
    main()
