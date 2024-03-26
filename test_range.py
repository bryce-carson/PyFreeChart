"""Tests for the class in Freepy: translated classes from JFreeChart."""
import unittest
from range import Range
import math


class test_range(unittest.TestCase):
    """Test case for the range class in Freepy."""

    _ONE = 1
    _avogadros_number = 6.02214076e23

    ordinal_range = Range(_ONE, _avogadros_number)
    integer_range = Range(math.pi, _avogadros_number)
    irrational_range = Range(-math.pi, _avogadros_number)

    def test_equal(self):
        """__eq__ should report correctly."""
        for i in [self.ordinal_range,
                  self.integer_range,
                  self.irrational_range]:
            with self.subTest(i):
                self.assertEqual(i, Range(i.lower, i.upper))

    def test_not_equal(self):
        """__ne__ should report correctly."""
        for i in [self.ordinal_range,
                  self.integer_range,
                  self.irrational_range]:
            with self.subTest(i):
                self.assertNotEqual(i, Range(i.upper, i.lower))

    def test_len_with_integer(self):
        """__len__ should report correctly with integer values."""
        self.assertEqual(len(Range(1, 10)), 10 - 1)

    def test_len_with_float(self):
        """__len__ should report correctly with float values."""
        self.assertAlmostEqual(len(Range(0.1, 9.9)), 9.9 - 0.1)

    def test_central_value(self):
        """Expect that the central value for any given range is correct.

        TODO: assertions for other inputs.
        """
        ordrnge = self.ordinal_range
        self.assertAlmostEqual((ordrnge.lower / 2) + (ordrnge.upper / 2),
                               3.01107038e+23)

    def test_constrain_returns_given_value(self):
        """Constrain must return the given value if it is within the range.

        TODO: assertions for other inputs.
        """
        self.assertEqual(Range(1, math.pi).constrain(math.pi), math.pi)

    def test_constrain_returns_closest_value(self):
        """Constrain should return the closest value if the given value is not
        within its range.

        TODO: assertions for other inputs.
        """
        self.assertEqual(Range(1, math.pi).constrain(self._avogadros_number),
                         math.pi)

    def test_contains(self):
        """Range.contains should report sane values.

        TODO: assertions for other inputs.
        """
        self.assertTrue(self.ordinal_range.contains(3))

    def test_intersects(self):
        """Reasonable return values should be obtained.

        TODO: assertions for other inputs.
        """
        self.assertTrue(self.integer_range.intersects(self.irrational_range))

    def test_lower(self):
        """The correct attribute is returned."""
        self.assertEqual(self.ordinal_range.lower, self._ONE)

    def test_upper(self):
        """The correct attribute is returned."""
        self.assertEqual(self.ordinal_range.upper, self._avogadros_number)

    def test_shift(self):
        """Expect the correct amount of frameshifting."""

    def test_expand_to_include(self):
        """Assure that the method is operable."""

    def test_expand(self):
        """Range objects should work good?"""

    def test_combine(self):
        """Range objects should work great!"""


if __name__ == '__main__':
    unittest.main()
