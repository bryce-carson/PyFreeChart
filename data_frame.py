"""Tabular data frame for COMP 3505, with a naive implementation."""
from numbers import Number
from re import sub


class data_frame:
    """A naive (tabular) data frame class."""

    def __init__(self, data: [Number], rows: int, columns: int):
        """Create a new data frame using a list of numbers, filling by row."""
        df = []

        # Fill by row
        for r in range(rows):
            df.append([x for x in data[r * columns: r * columns + columns]])

        self.df = df

    def get_column(self, column: int):
        """Retrieve a column from a data frame.

        This method, and its counterpart get_row, is not designed to be used
        with calculate_column_total.
        """
        assert 0 <= column <= len(self.df[0])
        return [x[column] for x in self.df]

    def get_row(self, row: int):
        """Retrieve a row from a data frame.

        This method, and its counterpart get_column, is not designed to be used
        with calculate_row_total.
        """
        assert 0 <= row <= len(self.df)
        return self.df[row]

    def get_dim(self):
        """Determine the magnitude of the two dimensions of this data_frame.

        The ording of the elements of the returned tuple is: columns, rows.
        """
        return (len(self.df[0]), len(self.df))

    def insert(self, index: int, data: [Number]):
        """Insert the given row in the given position.

        This method is simply `list.insert()`.
        """
        self.df.insert(index, data)

    def extend(self, data: 'data_frame'):
        """Extend the dataframe by appending the iterable as new rows.

        Identical to list.extend(), which it calls internally.
        """
        if isinstance(data, list):
            for e in data:
                if isinstance(e, list):
                    for n in e:
                        if isinstance(n, Number):
                            pass
                        else:
                            raise TypeError("data must be a data_frame object \
                            or a list of lists of Numbers.")
                    self.df.append(e)
                else:
                    raise TypeError("data must be a data_frame object or a \
                    list of lists of Numbers.")

    def append(self, data: [Number]):
        """Append a single row to the dataframe.

        This is identical to list.append(), which it calls internally.
        """
        self.df.append(data)

    def __len__(self):
        """Retrieve the number of rows in this data frame."""
        return len(self.df)

    # Ideally, Python should be able to iterate over instances of the
    # data_frame class, with "top-level" items being the rows of the data_frame
    def __getitem__(self, key: int):
        """Return slices of the data-frame, by row.

        A slice of the first, second, and fifth elements of the data-frame
        correspond to the first, second, and fifth rows of the data-frame.

        """
        return self.df[key]

    def __setitem__(self, key, value):
        """Set the value in a slice of df.

        If the index is beyond the current length of the dataframe, the element
        will be added to the end of the dataframe instead as a new row. For
        example, if a dataframe has four rows and a seventh row is added using
        slicing, the new row will be added as the fifth row per Python's
        standard implementation of insert/slicing operation fall-through cases.

        """
        self.df.insert(key, value)

    def __repr__(self):
        """Print a representation of the dataframe.

        This string representation of the object is used when the object is
        accessed with the interactive prompt, or other means, but is not
        printed or formatted in some special way. It is the string
        representation when accessed directly.

        """
        return f"({len(self.df[0])}, {len(self.df)}) dataframe @ {id(self):#x}"

    def __str__(self):
        r"""Return the string representation of the object for printing."""
        return sub(r"],\ ", r"],\n ", str(self.df))

    def calculate_column_total(self, column: int):
        """Sum the values in a column of this 2D matrix.

        Summate the values in a given column of the supplied matrix (a list
        of lists, wherein interior lists are rows of the matrix).
        """
        total = 0
        for row in self.df:
            total += row[column]
        return total

    def calculate_row_total(self, row: int):
        """Sum the values in a row of this 2D matrix.

        Summate the values in a given row of the supplied matrix (a list
        of lists, wherein interior lists are rows of the matrix).
        """
        total = 0
        for column in self.df[row]:
            total += column
        return total

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
