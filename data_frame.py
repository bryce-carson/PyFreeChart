"""Tabular data frame for COMP 3505, with a naive implementation."""
from numbers import Number


class data_frame:
    """A naive (tabular) data frame class."""

    df = []

    def __init__(self, data: [Number],
                 rows: int,
                 columns: int,
                 by_row: bool = True):
        """Create a new data frame using a list of numbers, filling by row.

        TODO: handle by_row = False.
        """
        # Fill by row
        for r in range(rows):
            self.df[r] = [x for x in data[r*columns:columns]]

        return self.df

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

    def __len__(self):
        """Retrieve the number of rows in this data frame."""
        return len(self.df)

    def __getitem__(self, key: int):
        """Return slices of df."""
        return self.df[key]

    def __setitem__(self, key, value):
        """Set the value in a slice of df."""
        self.df[key] = value
