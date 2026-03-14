"""Unit tests for build.py — runs quickly and validates the CI matrix."""

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
        self.assertEqual(idx, 1)  # ['-e', 'USER_NAME=holykeebs', '-e', 'SIDE=left']

    def test_add_argument_raw_no_flag(self):
        cmd = self._make()
        cmd.add_argument_raw('-j8')
        self.assertIn('-j8', cmd.arguments)
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
        cmd = Command('sofle/rp2040', 'vial')
        cmd.add_argument('POINTING_DEVICE=trackball')
        cmd.add_argument('SIDE=left')
        name = cmd.file_name()
        self.assertIn('sofle_rp2040', name)

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
    EXPECTED_KEYBOARDS = {'lily58/rev1', 'sofle/rp2040', 'crkbd/rev1'}
    EXPECTED_POINTING = {'trackball', 'trackpoint', 'tps43', 'None'}

    def _capture_matrix(self, matrix_type='release'):
        buf = StringIO()
        with patch('sys.stdout', buf):
            generate_matrix(matrix_type)
        return json.loads(buf.getvalue())

    def test_matrix_has_include_key(self):
        matrix = self._capture_matrix()
        self.assertIn('include', matrix)

    def test_matrix_entry_count(self):
        matrix = self._capture_matrix()
        self.assertEqual(len(matrix['include']), 132)

    def test_each_keyboard_has_expected_count(self):
        matrix = self._capture_matrix()
        counts = {kb: 0 for kb in self.EXPECTED_KEYBOARDS}
        for entry in matrix['include']:
            counts[entry['keyboard']] += 1
        self.assertEqual(set(counts.keys()), self.EXPECTED_KEYBOARDS)
        for kb, count in counts.items():
            self.assertEqual(count, 44, f'{kb} should have 44 entries')

    def test_keyboard_and_names_align(self):
        matrix = self._capture_matrix()
        for entry in matrix['include']:
            expected_name = entry['keyboard'].replace('/', '_')
            self.assertEqual(entry['keyboard_name'], expected_name)

    def test_matrix_keyboards_and_keymap(self):
        matrix = self._capture_matrix()
        keyboards = {e['keyboard'] for e in matrix['include']}
        self.assertEqual(keyboards, self.EXPECTED_KEYBOARDS)
        for entry in matrix['include']:
            self.assertEqual(entry['keymap'], 'vial')

    def test_matrix_debug_flags(self):
        release = self._capture_matrix()
        self.assertTrue(all(not e['debug'] for e in release['include']))
        debug = self._capture_matrix('debug')
        for entry in debug['include']:
            if entry['keyboard'] == 'crkbd/rev1':
                self.assertFalse(entry['debug'])
            else:
                self.assertTrue(entry['debug'])

    def test_matrix_contains_left_and_right_sides(self):
        matrix = self._capture_matrix()
        sides = {e['side'] for e in matrix['include']}
        self.assertIn('left', sides)
        self.assertIn('right', sides)

    def test_matrix_has_oled_variants(self):
        matrix = self._capture_matrix()
        oled_values = {e['oled'] for e in matrix['include']}
        self.assertEqual(oled_values, {True, False})

    def test_matrix_contains_single_and_dual_device_entries(self):
        matrix = self._capture_matrix()
        singles = [e for e in matrix['include'] if 'None' in (e['left_device'], e['right_device'])]
        duals = [e for e in matrix['include'] if e['left_device'] != 'None' and e['right_device'] != 'None']
        self.assertGreater(len(singles), 0)
        self.assertGreater(len(duals), 0)

    def test_matrix_includes_sofle_tps43_combo(self):
        matrix = self._capture_matrix()
        sofle_duals = [
            e for e in matrix['include']
            if e['keyboard'] == 'sofle/rp2040'
            and e['left_device'] in {'tps43', 'trackball'}
            and e['right_device'] in {'tps43', 'trackball'}
        ]
        self.assertGreater(len(sofle_duals), 0)

    def test_matrix_devices_are_expected(self):
        matrix = self._capture_matrix()
        for entry in matrix['include']:
            self.assertIn(entry['left_device'], self.EXPECTED_POINTING)
            self.assertIn(entry['right_device'], self.EXPECTED_POINTING)

    def test_matrix_valid_json(self):
        buf = StringIO()
        with patch('sys.stdout', buf):
            generate_matrix('release')
        obj = json.loads(buf.getvalue())
        self.assertIsInstance(obj, dict)


if __name__ == '__main__':
    unittest.main()
