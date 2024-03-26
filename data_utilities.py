"""Summary methods for data_frame objects.

data_utililties is a Pythonic implementation of the DataUtilities class in
JFreeChart. DataUtilities operates upon implementations of interfaces
specifying data-frame or tabular, two-dimensional data objects useful in
numerical computing.

This class specifies similar methods which operate upon a naive implementation
of a data frame, provided by data_frame.

"""
from numbers import Number


class DataUtilities:
    """Summary methods for data_frame objects."""

    @classmethod
    def calculate_column_total(cls, data: [[Number]], column: int):
        """Sum the values in a column of a 2D matrix.

        Summate the values in a given column of the supplied matrix (a list
        of lists, wherein interior lists are rows of the matrix).
        """
        total = 0
        for row in data:
            total += row[column]
        return total

    @classmethod
    def calculate_row_total(cls, data: [[Number]], row: int):
        """Sum the values in a row of a 2D matrix.

        Summate the values in a given row of the supplied matrix (a list
        of lists, wherein interior lists are rows of the matrix).
        """
        total = 0
        for column in data[row]:
            total += column
        return total

    # NOTE: there is no need to implement these methods because of Python's
    # duck-typing.
    # @classmethod
    # def create_number_array(cls, data: [float]) -> [Real]:
    #     """Coerce the float elements of a one-dimensional list to numbers."""

    # @classmethod
    # def create_number_array_2d(cls, data: [[float]]) -> [[Real]]:
    #     """Coerce the float elements of a two-dimensional list to numbers."""

    @classmethod
    def calculate_cumulative_percentages(cls, data: [Number]):
        """Calculate cumulative percentages of the sum of the data.

        Cumulative percentages are calculated with the sum of all values in the
        data being the divisor, and the cumulative sum at each index being the
        dividend; the quotient is the cumulative percentage.
        """
        s = sum(data)
        result = []
        for i, x in enumerate(data):
            z = float(x)
            for j, y in enumerate(data):
                if j < i:
                    z += y

            result.append(z / s)

        return result
