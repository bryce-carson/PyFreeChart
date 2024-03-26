"""Documentation for this module of unit testing."""
import unittest
from data_utilities import DataUtilities


class DataUtilitiesTestCase(unittest.TestCase):
    """Test the methods in data_utilities for proper implementation."""

    _data = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]

    _data_row_one_sum = _dr1s = sum([1, 2, 3])
    _data_row_one_cumpercentage = [(1) / _dr1s,
                                   (1 + 2) / _dr1s,
                                   (1 + 2 + 3) / _dr1s]

    _data_row_two_sum = _dr2s = sum([4, 5, 6])
    _data_row_two_cumpercentage = [(4) / _dr2s,
                                   (4 + 5) / _dr2s,
                                   (4 + 5 + 6) / _dr2s]

    _data_row_three_sum = _dr3s = sum([7, 8, 9])
    _data_row_three_cumpercentage = [(7) / _dr3s,
                                     (7 + 8) / _dr3s,
                                     (7 + 8 + 9) / _dr3s]

    _data_column_one_sum = _dc1s = sum([1, 4, 7])
    _data_column_one_cumpercentage = [(1) / _dc1s,
                                      (1 + 4) / _dc1s,
                                      (1 + 4 + 7) / _dc1s]

    _data_column_two_sum = _dc2s = sum([2, 5, 8])
    _data_column_two_cumpercentage = [(2) / _dc2s,
                                      (2 + 5) / _dc2s,
                                      (2 + 5 + 8) / _dc2s]

    _data_column_three_sum = _dc3s = sum([3, 6, 9])
    _data_column_three_cumpercentage = [(3) / _dc3s,
                                        (3 + 6) / _dc3s,
                                        (3 + 6 + 9) / _dc3s]

    _data_row_or_column_cumulative_percentages =\
        [_data_row_one_cumpercentage,
         _data_row_two_cumpercentage,
         _data_row_three_cumpercentage,
         _data_column_one_cumpercentage,
         _data_column_two_cumpercentage,
         _data_column_three_cumpercentage]

    def test_calcualte_column_total(self):
        """Test that the sum returned by the method is correct for a variety of
        numeric data types."""
        self.assertEqual(DataUtilities.calculate_column_total(self._data, 0),
                         12)

    def test_calcualte_row_total(self):
        """pass"""
        self.assertEqual(DataUtilities.calculate_row_total(self._data, 0), 6)

    def test_calculate_cumulative_percentages_rows(self):
        """Assert that every row has the expected cumulative percentage."""
        for i in range(3):
            with self.subTest(i):
                self.assertEqual(
                    DataUtilities.calculate_cumulative_percentages(
                        DataUtilities.get_row(self._data, i)),
                    self._data_row_or_column_cumulative_percentages[i])

    def test_calculate_cumulative_percentages_columns(self):
        """Assert that every row has the expected cumulative percentage."""
        for i in range(3):
            with self.subTest(i):
                self.assertEqual(
                    DataUtilities.calculate_cumulative_percentages(
                        DataUtilities.get_column(self._data, i)),
                    self._data_row_or_column_cumulative_percentages[i + 3])


if __name__ == '__main__':
    unittest.main()
