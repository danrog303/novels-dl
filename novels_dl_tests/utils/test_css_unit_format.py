import unittest
from novels_dl.utils import css_unit_exists, css_unit_format


class TestCssUnitFormat(unittest.TestCase):

    def test_css_unit_exists_existing_unit(self):
        self.assertTrue(css_unit_exists("cm"))

    def test_css_unit_exists_not_existing_unit(self):
        self.assertFalse(css_unit_exists("abcdef"))

    def test_css_unit_format_correct_argument(self):
        self.assertEqual(css_unit_format("1 CM"), "1cm")

    def test_css_unit_format_incorrect_argument(self):
        self.assertIsNone(css_unit_format('1 abcdef'))
