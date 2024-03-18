"""data_utilities.py is a Pythonic implementation of the DataUtilities class in
JFreeChart."""


class DataUtilities:
    """See the module documentation; the module only contains this class."""

    @classmethod
    def calcualte_column_total(cls, data, column):
        """Summate the values in a given column of the supplied matrix.

        TODO: write the function body.
        """

    @classmethod
    def calculate_row_total(cls, data, row):
        """Summate the values in a given row of the supplied matrix.

        TODO: write the function body.
        """

    @classmethod
    def create_number_array(cls, data: [float]):
        """Coerce the float elements of a one-dimensional list to numbers.

        TODO: write the function body.
        """

    @classmethod
    def create_number_array_2d(cls, data: [[float]]):
        """Coerce the float elements of a two-dimensional list to numbers.

        TODO: write the function body.
        """

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
