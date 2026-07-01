import unittest

from exceltablekit.errors import (
    InvalidCellError,
    InvalidColumnValueError,
    InvalidRowValueError,
)
from exceltablekit.utils import Validation


class TestValidation(unittest.TestCase):
    def test_valid_cell(self) -> None:
        """Tests whether the cell validation is correct."""
        valid_cells = [
            "A1",
            "A10",
            "A100",
            "A1000",
            "A10000",
            "A100000",
            "A1000000",
            "AA1",
            "AA10",
            "AA100",
            "AA1000",
            "AA10000",
            "AA100000",
            "AA1000000",
            "AAA1",
            "AAA10",
            "AAA100",
            "AAA1000",
            "AAA10000",
            "AAA100000",
            "AAA1000000",
            "XFD1048576",
        ]
        for cell in valid_cells:
            with self.subTest(cell=cell):
                Validation.cell(cell)

    def test_invalid_cell_format(self) -> None:
        """Tests that malformed cell references raise InvalidCellError."""
        with self.assertRaises(InvalidCellError):
            Validation.cell("!1")

    def test_invalid_column_value(self) -> None:
        """Tests that out-of-range column letters raise InvalidColumnValueError."""
        with self.assertRaises(InvalidColumnValueError):
            Validation.cell("XFE1")

    def test_invalid_row_value(self) -> None:
        """Tests that out-of-range row numbers raise InvalidRowValueError."""
        with self.assertRaises(InvalidRowValueError):
            Validation.cell("A1048577")


if __name__ == "__main__":
    unittest.main()
