"""data_utilities.py is a Pythonic implementation of the DataUtilities class in
JFreeChart.

In JFreeChart, the Number abstract base class is used to retrieve numeric
values from data arguments provided to the methods of DataUtilties. The
retrieved value is always converted to a double before operating upon it. In
this Python translation there is no need to use the Number ABC because Python
is duck-typed, so any value returned by methods which would in principle
operate upon rows and columns of a two-dimensional data structure would not
need to be cast to a higher type in the Numeric hierarchy.

"""
from numbers import Real  # NOTE: not needed; see the above explanation.


class DataUtilities:
    """See the module documentation; the module only contains this class."""

    @classmethod
    def calcualte_column_total(cls, data, column):
        """Summate the values in a given column of the supplied matrix."""
        total = 0
        for row in data:
            total += row[column]
        return total

    @classmethod
    def calculate_row_total(cls, data, row):
        """Summate the values in a given row of the supplied matrix."""
        total = 0
        for column in data[row]:
            total += column
        return total

    # NOTE: there is no need to implement these methods because of Python's
    # duck-typing.
    @classmethod
    def create_number_array(cls, data: [float]) -> [Real]:
        """Coerce the float elements of a one-dimensional list to numbers."""

    @classmethod
    def create_number_array_2d(cls, data: [[float]]) -> [[Real]]:
        """Coerce the float elements of a two-dimensional list to numbers."""

    @classmethod
    def calculate_cumulative_percentages(cls, data: [float]):
        """Calculate cumulative percentages of the sum of the data.

        Cumulative percentages are calculated with the sum of all values in the
        data being the divisor, and the cumulative sum at each index being the
        dividend; the quotient is the cumulative percentage.

        TODO: ensure the values that come out of the function are correct.
        """
        s = sum(data)
        result = []
        for x, i in enumerate(data):
            z = float(x)
            for y, j in enumerate(data):
                if j < i:
                    z += y

            result.append(z / s)

        return result
