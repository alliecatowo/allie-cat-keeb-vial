"""Unit tests for build.py — runs in < 5 seconds without any C toolchain."""

import json
import unittest
from io import StringIO
from unittest.mock import patch

# ---------------------------------------------------------------------------
# Import build.py as a module without executing main()
# ---------------------------------------------------------------------------
import importlib.util
import os

_BUILD_PY = os.path.join(os.path.dirname(__file__), '..', 'build.py')
_spec = importlib.util.spec_from_file_location('build', _BUILD_PY)
_build = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_build)

Command = _build.Command
generate_matrix = _build.generate_matrix
_configure_device = _build._configure_device
_build_single = _build._build_single


# ---------------------------------------------------------------------------
# Command class tests
# ---------------------------------------------------------------------------

class TestCommand(unittest.TestCase):
    def _make(self, kb='lily58/rev1', km='vial'):
        return Command(kb, km)

    # --- build() / build_list() -------------------------------------------

    def test_build_list_minimal(self):
        cmd = self._make()
        self.assertEqual(cmd.build_list(), ['make', 'lily58/rev1:vial'])

    def test_build_returns_string(self):
        cmd = self._make()
        self.assertIsInstance(cmd.build(), str)
        self.assertIn('make', cmd.build())

    # --- add_argument / prepend_argument ------------------------------------

    def test_add_argument_appends_flag_and_value(self):
        cmd = self._make()
        cmd.add_argument('SIDE=left')
        self.assertIn('-e', cmd.arguments)
        self.assertIn('SIDE=left', cmd.arguments)

    def test_prepend_argument_inserts_at_front(self):
        cmd = self._make()
        cmd.add_argument('SIDE=left')
        cmd.prepend_argument('USER_NAME=holykeebs')
        idx = cmd.arguments.index('USER_NAME=holykeebs')
        # prepend should place it before 'SIDE=left'
        self.assertEqual(idx, 1)  # ['-e', 'USER_NAME=holykeebs', '-e', 'SIDE=left']

    def test_add_argument_raw_no_flag(self):
        cmd = self._make()
        cmd.add_argument_raw('-j8')
        self.assertIn('-j8', cmd.arguments)
        # raw argument must NOT be preceded by '-e'
        j8_idx = cmd.arguments.index('-j8')
        if j8_idx > 0:
            self.assertNotEqual(cmd.arguments[j8_idx - 1], '-e')

    # --- file_name() --------------------------------------------------------

    def test_file_name_dual_device_left(self):
        cmd = self._make()
        cmd.add_argument('POINTING_DEVICE=trackball_tps43')
        cmd.add_argument('SIDE=left')
        name = cmd.file_name()
        self.assertIn('lily58_rev1', name)
        self.assertIn('trackball_tps43', name)
        self.assertIn('left', name)

    def test_file_name_dual_device_right(self):
        cmd = self._make()
        cmd.add_argument('POINTING_DEVICE=trackball_tps43')
        cmd.add_argument('SIDE=right')
        self.assertIn('right', cmd.file_name())

    def test_file_name_single_device_position(self):
        cmd = self._make()
        cmd.add_argument('POINTING_DEVICE=trackball')
        cmd.add_argument('POINTING_DEVICE_POSITION=left')
        name = cmd.file_name()
        self.assertIn('trackball', name)
        self.assertIn('left', name)

    def test_file_name_with_oled(self):
        cmd = self._make()
        cmd.add_argument('OLED=yes')
        self.assertIn('oled', cmd.file_name())

    def test_file_name_no_duplicate_separators(self):
        cmd = self._make()
        cmd.add_argument('POINTING_DEVICE=tps43')
        cmd.add_argument('SIDE=right')
        name = cmd.file_name()
        self.assertNotIn('__', name)

    def test_file_name_different_keyboard(self):
        cmd = Command('sofle/rev1', 'vial')
        cmd.add_argument('POINTING_DEVICE=trackball')
        cmd.add_argument('SIDE=left')
        name = cmd.file_name()
        self.assertIn('sofle_rev1', name)

    # --- full build string integration -------------------------------------

    def test_full_build_string_contains_all_parts(self):
        cmd = self._make()
        cmd.prepend_argument('USER_NAME=holykeebs')
        cmd.add_argument('POINTING_DEVICE=trackball_tps43')
        cmd.add_argument('SIDE=left')
        cmd.add_argument('TRACKBALL_RGB_RAINBOW=yes')
        cmd.add_argument_raw('-j8')
        cmd.prepend_argument(f'TARGET={cmd.file_name()}')
        full = cmd.build()
        self.assertIn('make', full)
        self.assertIn('lily58/rev1:vial', full)
        self.assertIn('USER_NAME=holykeebs', full)
        self.assertIn('POINTING_DEVICE=trackball_tps43', full)
        self.assertIn('SIDE=left', full)
        self.assertIn('-j8', full)


# ---------------------------------------------------------------------------
# generate_matrix() tests
# ---------------------------------------------------------------------------

class TestGenerateMatrix(unittest.TestCase):
    def _capture_matrix(self):
        buf = StringIO()
        with patch('sys.stdout', buf):
            generate_matrix('release')
        return json.loads(buf.getvalue())

    def test_matrix_has_include_key(self):
        matrix = self._capture_matrix()
        self.assertIn('include', matrix)

    def test_matrix_has_two_entries(self):
        """Default matrix: left + right for trackball_tps43 on lily58/rev1."""
        matrix = self._capture_matrix()
        self.assertEqual(len(matrix['include']), 2)

    def test_matrix_entries_have_required_keys(self):
        required = {'keyboard', 'keyboard_name', 'keymap', 'left_device',
                    'right_device', 'side', 'debug'}
        matrix = self._capture_matrix()
        for entry in matrix['include']:
            self.assertTrue(required.issubset(entry.keys()),
                            f"Entry missing keys: {required - entry.keys()}")

    def test_matrix_contains_left_and_right_sides(self):
        matrix = self._capture_matrix()
        sides = {e['side'] for e in matrix['include']}
        self.assertIn('left', sides)
        self.assertIn('right', sides)

    def test_matrix_uses_lily58_keyboard(self):
        matrix = self._capture_matrix()
        for entry in matrix['include']:
            self.assertEqual(entry['keyboard'], 'lily58/rev1')

    def test_matrix_uses_vial_keymap(self):
        matrix = self._capture_matrix()
        for entry in matrix['include']:
            self.assertEqual(entry['keymap'], 'vial')

    def test_matrix_devices_trackball_tps43(self):
        matrix = self._capture_matrix()
        for entry in matrix['include']:
            self.assertEqual(entry['left_device'], 'trackball')
            self.assertEqual(entry['right_device'], 'tps43')

    def test_matrix_debug_is_false_by_default(self):
        matrix = self._capture_matrix()
        for entry in matrix['include']:
            self.assertFalse(entry['debug'])

    def test_matrix_valid_json(self):
        buf = StringIO()
        with patch('sys.stdout', buf):
            generate_matrix('release')
        # Must be parseable JSON with no trailing garbage
        obj = json.loads(buf.getvalue())
        self.assertIsInstance(obj, dict)


# ---------------------------------------------------------------------------
# _configure_device() / _build_single() tests
# ---------------------------------------------------------------------------

def _args(**over):
    from argparse import Namespace
    base = dict(keyboard='lily58/rev1', keymap='vial', user_name='alliecatowo',
                left_device='None', right_device='None', side=None, debug=False)
    base.update(over)
    return Namespace(**base)


def _flags(cmd):
    """The -e values of a Command, as a list."""
    return [a for a in cmd.arguments if a != '-e']


class TestConfigureDevice(unittest.TestCase):
    def _configured(self, **over):
        cmd = Command('lily58/rev1', 'vial')
        _configure_device(cmd, _args(**over))
        return _flags(cmd)

    def test_no_devices_adds_nothing(self):
        self.assertEqual(self._configured(), [])

    def test_dual_devices_set_pair_and_side(self):
        flags = self._configured(left_device='trackball', right_device='tps43', side='right')
        self.assertIn('POINTING_DEVICE=trackball_tps43', flags)
        self.assertIn('SIDE=right', flags)

    def test_trackball_rgb_only_on_the_trackball_side(self):
        left = self._configured(left_device='trackball', right_device='tps43', side='left')
        right = self._configured(left_device='trackball', right_device='tps43', side='right')
        self.assertIn('TRACKBALL_RGB_RAINBOW=yes', left)
        self.assertNotIn('TRACKBALL_RGB_RAINBOW=yes', right)

    def test_left_only_device(self):
        flags = self._configured(left_device='trackball')
        self.assertEqual(flags, ['POINTING_DEVICE=trackball', 'POINTING_DEVICE_POSITION=left',
                                 'TRACKBALL_RGB_RAINBOW=yes'])

    def test_right_only_device(self):
        flags = self._configured(right_device='tps43')
        self.assertEqual(flags, ['POINTING_DEVICE=tps43', 'POINTING_DEVICE_POSITION=right'])


class TestBuildSingle(unittest.TestCase):
    def _run(self, **over):
        """Run _build_single with subprocess/os stubbed; return the make argv."""
        calls = []
        with patch.object(_build, 'run_command_check_output', side_effect=calls.append), \
                patch.object(_build.os, 'makedirs'), \
                patch.object(_build.os, 'rename') as rename:
            _build_single(_args(**over))
        return calls[0], rename

    def test_builds_the_requested_keyboard_and_keymap(self):
        argv, _ = self._run(left_device='trackball', right_device='tps43', side='left')
        self.assertEqual(argv[:2], ['make', 'lily58/rev1:vial'])
        self.assertIn('USER_NAME=alliecatowo', argv)
        self.assertIn('POINTING_DEVICE=trackball_tps43', argv)
        self.assertEqual(argv[-1], '-j8')

    def test_firmware_is_moved_into_the_per_keyboard_build_dir(self):
        _, rename = self._run(left_device='trackball', right_device='tps43', side='right')
        src, dst = rename.call_args.args
        self.assertTrue(src.endswith('.uf2'))
        self.assertEqual(dst, f'build_lily58/{src}')

    def test_debug_flag_enables_console(self):
        argv, _ = self._run(debug=True)
        self.assertIn('CONSOLE=yes', argv)

    def test_oled_is_enabled_and_flipped_when_paired_with_another_device(self):
        argv, _ = self._run(left_device='oled', right_device='tps43', side='left')
        self.assertIn('OLED=yes', argv)
        self.assertIn('OLED_FLIP=yes', argv)

    def test_a_failed_make_exits_nonzero(self):
        import subprocess
        with patch.object(_build, 'run_command_check_output',
                          side_effect=subprocess.CalledProcessError(2, 'make')), \
                patch.object(_build.os, 'makedirs'), \
                self.assertRaises(SystemExit) as ctx:
            _build_single(_args())
        self.assertEqual(ctx.exception.code, 1)


if __name__ == '__main__':
    unittest.main()
