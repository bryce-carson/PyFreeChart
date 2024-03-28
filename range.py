"""Immutable ranges of values, wouldst x = [1,10] be helpful.

range.py is a Python(ic) implemention of the Range class from JFreeChart.
Effort is made to ensure that where a Pythonic implementation can be made, one
is made. For instance, Properites are used rather than getters and setters,
because the privacy pattern commonly used in Java objects is not appropriate
for this class.
"""
from numbers import Number
from sys import maxsize


class Range:
    """Immutable ranges of values, wouldst x = [1,10] be helpful."""

    # The boundaries of the range, both are inclusive such that any Range
    # x = [lower, upper].
    lower: float
    upper: float

    @classmethod
    def combine(cls, range1: 'Range', range2: 'Range'):
        """Combine two Range objects into a new object.

        The minimum of the two lower bounds and the maximum of the two upper
        bounds is used to determine the lower and upper bound of the new Range
        object.
        """
        if range1 is None:
            return range2
        if range2 is None:
            return range2

        return Range(min(range1.lower, range2.lower),
                     max(range1.upper, range2.upper))

    def constrain(self, value: float):
        """Return the value in this Range closest to the given value."""
        if self.lower <= value <= self.upper:
            return value

        if (self.lower - value) < (self.upper - value):
            return self.lower

        return self.upper

    def contains(self, value: float):
        """Return whether the range contains the specified value."""
        return self.lower <= value <= self.upper

    @classmethod
    def expand(cls, rng: 'Range', lower_margin: float, upper_margin: float):
        """Create a new range by adding margins to an existing range."""
        return Range(rng.lower - len(rng) * lower_margin,
                     rng.upper + len(rng) * upper_margin)

    @classmethod
    def expand_to_include(cls, rng: 'Range', value: float):
        """Return a new Range, with the specified value within bounds.

        Given a Range with bounds not include the given value, the appropriate
        bound is expanded, while the other is left unchanged.

        If the value is within the range, the same range object is returned (no
        copying is performed).

        """
        if range is None:
            return Range(value, value)

        if value < rng.lower:
            return Range(value, rng.upper)

        if value > rng.upper:
            return Range(value, rng.lower)

        return range

    # If this is converted to a Python property, then reasonably, there would
    # need to be calls to expand such that the central value given would become
    # the actual central value; this should be achieved with the minimal amount
    # of padding in either direction.
    def central_value(self):
        """Return the central value for the range."""
        return (self.lower / 2.0) + (self.upper / 2.0)

    @property
    def lower(self):
        """Returns the lower bound for the range."""
        return self._lower

    @lower.setter
    def lower(self, value):
        self._lower = value

    @property
    def upper(self):
        """Returns the upper bound for the range."""
        return self._upper

    @upper.setter
    def upper(self, value):
        self._upper = value

    def intersects(self, rng: 'Range') -> bool:
        """Test if this and another range object intersect."""
        if rng.lower <= self.lower:
            return rng.upper > self.lower

        return rng.lower >= self.upper and rng.upper >= self.lower

    @classmethod
    def shift(cls, base: 'Range', delta: float,
              allow_zero_crossing: [bool | None]):
        """Shifts the range to the right by the specified amount."""
        if allow_zero_crossing:
            return Range(base.lower + delta, base.upper + delta)
        return Range(cls._shift_with_no_zero_crossing(base.lower, delta),
                     cls._shift_with_no_zero_crossing(base.upper, delta))

    @classmethod
    def _shift_with_no_zero_crossing(cls, value: float, delta: float):
        """Shift the given value to the right, without crossing zero.

        This is a protected helper method.
        """
        if value > 0.0:
            return max(value + delta, 0.0)
        return min(value + delta, 0.0)

    def __init__(self, lower: Number, upper: Number):
        """Initialize a new object of this type."""
        self.lower = lower
        self.upper = upper

    def __str__(self):
        """Return a string representation of this Range."""
        return f"Range[{self.lower},{self.upper}]"

    def __repr__(self):
        """Return a string representation of this Range."""
        return self.__str__()

    def __hash__(self):
        """Return a hash code."""
        temp = int(bytes(f"{self.lower:064b}", "utf8"))
        result = int(temp ^ temp >> 32)
        temp = int(bytes(f"{self.upper:064b}", "utf8"))
        return 29 * result + int(temp ^ temp >> 32)

    def __len__(self):
        """Return the difference between the upper and lower boundaries.

        The differnece is rounded to the nearest integer value if necessary.
        """
        if self.upper - self.lower <= maxsize:
            return int(self.upper - self.lower)
        raise ArithmeticError

    def __eq__(self, other):
        """Test if this object is equal to another."""
        return (isinstance(other, self.__class__) and
                self.lower == other.lower and
                self.upper == other.upper)

    def __ne__(self, other):
        """Test if this object is inequal to another."""
        return not self.__eq__(other)
