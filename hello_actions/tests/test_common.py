from unittest import TestCase
from .. import common


class TestCommon(TestCase):
    def test_square(self):
        self.assertEqual(common.square(2), 4)

    def test_batman(self):
        self.assertEqual(common.batman(), "NaNaNaNa")

    def test_discontinuity(self):
        self.assertRaises(ZeroDivisionError, common.discontinuity, 4)
