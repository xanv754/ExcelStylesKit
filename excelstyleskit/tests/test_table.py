from excelstyleskit.table import Cell, Table
from openpyxl.styles import PatternFill
from openpyxl.styles.colors import Color
from excelstyleskit.tests import TestExcel
import unittest


class TestCell(unittest.TestCase):
    def test_create_object(self) -> None:
        """Tests the correct instantiation of a `Cell` object."""
        cell = Cell("A", 1)

        self.assertIsInstance(cell, Cell)

    def test_set_property(self) -> None:
        """Tests the definition of a cell property."""
        file = TestExcel()
        blue = Color(rgb="0000FF")
        format_fill = PatternFill(
            patternType="solid", start_color=blue, end_color=blue)
        cell = Cell("A", 1)
        cell.set_property(worksheet=file.worksheet,
                          property="fill", value=format_fill)
        file.save()
        file.delete()

        self.assertIsInstance(cell, Cell)


class TestTable(unittest.TestCase):
    def test_create_table(self) -> None:
        """Tests the correct instantiation of a `Table` object."""
        file = TestExcel()
        table = Table(
            worksheet=file.worksheet,
            first_column="A",
            first_row=1,
            last_column="D",
            last_row=3,
        )

        self.assertIsInstance(table, Table)
        self.assertEqual(len(table.get_body()), 12)

    def test_set_header(self) -> None:
        """Tests the retrieval of the list of table header cells."""
        file = TestExcel()
        table = Table(file.worksheet, "A", 1, "D", 3)
        table.set_header(total_row_header=1)

        self.assertIsInstance(table, Table)
        self.assertEqual(len(table.get_body()), 8)
        self.assertEqual(len(table.get_header()), 4)

    def test_get_all_row(self) -> None:
        """Test the complete retrieval of a table row."""
        file = TestExcel()
        table = Table(file.worksheet, "A", 1, "D", 3)
        second_row = table.get_cells_by_row(2)

        self.assertEqual(len(second_row), 4)

    def test_display_table(self) -> None:
        """Test the terminal rendering of the Excel table."""
        file = TestExcel()
        table = Table(file.worksheet, "A", 1, "D", 3)
        table.display_cells()

        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
