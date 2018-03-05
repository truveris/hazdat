from unittest import TestCase

from hazdat import Shielding
from hazdat.shielding import StrGuarded


class TestStrGuarded(TestCase):

    def test_wrapped_object_access_denied(self):
        wrap = StrGuarded('a')
        with self.assertRaises(AttributeError) as error:
            wrap.__wrapped__
        expected = "'str' object has no attribute '__wrapped__'"
        self.assertEqual(str(error.exception), expected)

    def test_wrapped_object_str_denied(self):
        wrap = StrGuarded('a')
        with self.assertRaises(AttributeError) as error:
            str(wrap)
        expected = "Can't access StrGuarded __str__"
        self.assertEqual(str(error.exception), expected)

    def test_private_str_once(self):
        wrap = StrGuarded(1)
        with self.assertRaises(AttributeError) as error:
            wrap._self_str_once
        expected = "'int' object has no attribute '_self_str_once'"
        self.assertEqual(str(error.exception), expected)

    def test_str_once(self):
        wrap = StrGuarded(1)
        self.assertEqual(wrap.str_once, '1')
        with self.assertRaises(AttributeError) as error:
            wrap.str_once
        expected = "'int' object has no attribute 'str_once'"
        self.assertEqual(str(error.exception), expected)

    def test_dir(self):
        wrap = StrGuarded(1)
        expected = sorted(dir(1) + ['str_once'])
        self.assertEqual(dir(wrap), expected)


class TestShielding(TestCase):

    def test_get_once(self):
        hazard = Shielding(1)
        success = hazard.hazdat
        self.assertIsInstance(success, StrGuarded)
        self.assertEqual(success, 1)

        with self.assertRaises(AttributeError) as error:
            hazard.hazdat
        expected = "Attribute 'hazdat' accessed more than once"
        self.assertEqual(str(error.exception), expected)

    def test_get_private_hazdat(self):
        hazard = Shielding(1)
        with self.assertRaises(AttributeError) as error:
            hazard._hazdat
        expected = '_hazdat'
        self.assertEqual(str(error.exception), expected)

    def test_cannot_set_hazdat(self):
        hazard = Shielding(1)
        with self.assertRaises(AttributeError) as error:
            hazard.hazdat = 2
        expected = "'Shielding' object attributes are read-only"
        self.assertEqual(str(error.exception), expected)

    def test_cannot_set_private_hazdat(self):
        hazard = Shielding(1)
        with self.assertRaises(AttributeError) as error:
            hazard._hazdat = 2
        expected = "'Shielding' object attributes are read-only"
        self.assertEqual(str(error.exception), expected)

    def test_cannot_set_attribute_does_not_exist(self):
        hazard = Shielding(1)
        with self.assertRaises(AttributeError) as error:
            hazard.nope = 2
        expected = "'Shielding' object attributes are read-only"
        self.assertEqual(str(error.exception), expected)
