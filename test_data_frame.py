"""Documentation for this module of unit testing."""
import unittest
from data_frame import data_frame


class DataFrameTestCase(unittest.TestCase):
    """Test the methods in data_frame for proper implementation."""

    # E.g. data_frame for testing.
    egdataframe = data_frame([*range(1, 10)], rows=3, columns=3)

    data_row_one_sum = dr1s = sum([1, 2, 3])
    data_row_one_cumpercentage = [(1) / dr1s,
                                  (1 + 2) / dr1s,
                                  (1 + 2 + 3) / dr1s]

    data_row_two_sum = dr2s = sum([4, 5, 6])
    data_row_two_cumpercentage = [(4) / dr2s,
                                  (4 + 5) / dr2s,
                                  (4 + 5 + 6) / dr2s]

    data_row_three_sum = dr3s = sum([7, 8, 9])
    data_row_three_cumpercentage = [(7) / dr3s,
                                    (7 + 8) / dr3s,
                                    (7 + 8 + 9) / dr3s]

    data_column_one_sum = dc1s = sum([1, 4, 7])
    data_column_one_cumpercentage = [(1) / dc1s,
                                     (1 + 4) / dc1s,
                                     (1 + 4 + 7) / dc1s]

    data_column_two_sum = dc2s = sum([2, 5, 8])
    data_column_two_cumpercentage = [(2) / dc2s,
                                     (2 + 5) / dc2s,
                                     (2 + 5 + 8) / dc2s]

    data_column_three_sum = dc3s = sum([3, 6, 9])
    data_column_three_cumpercentage = [(3) / dc3s,
                                       (3 + 6) / dc3s,
                                       (3 + 6 + 9) / dc3s]

    data_row_or_column_cumulative_percentages = [
        data_row_one_cumpercentage,
        data_row_two_cumpercentage,
        data_row_three_cumpercentage,
        data_column_one_cumpercentage,
        data_column_two_cumpercentage,
        data_column_three_cumpercentage
    ]

    def test_calcualte_column_total(self):
        """Test that the sum returned by the method is correct for a variety of
        numeric data types."""
        self.assertEqual(self.egdataframe.calculate_column_total(0), 12)

    def test_calcualte_row_total(self):
        """pass"""
        self.assertEqual(self.egdataframe.calculate_row_total(0), 6)

    def test_calculate_cumulative_percentages_rows(self):
        """Assert that every row has the expected cumulative percentage."""
        for i in range(3):
            with self.subTest(i):
                self.assertEqual(
                    data_frame
                    .calculate_cumulative_percentages(self
                                                      .egdataframe.get_row(i)),
                    self.data_row_or_column_cumulative_percentages[i])

    def test_calculate_cumulative_percentages_columns(self):
        """Assert that every column has the expected cumulative percentage."""
        for i in range(3):
            with self.subTest(i):
                self.assertEqual(
                    data_frame
                    .calculate_cumulative_percentages(self
                                                      .egdataframe
                                                      .get_column(i)),
                    self.data_row_or_column_cumulative_percentages[i + 3])


if __name__ == '__main__':
    unittest.main()
