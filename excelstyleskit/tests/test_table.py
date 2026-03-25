import unittest
from excelstyleskit.table import Cell, Table


class TestCell(unittest.TestCase):
    def test_create_object(self) -> None:
        """Tests the correct instantiation of a `Cell` object."""
        cell = Cell("A", 1)

        self.assertIsInstance(cell, Cell)


class TestTable(unittest.TestCase):
    def test_create_table(self) -> None:
        """Tests the correct instantiation of a `Table` object."""
        table = Table(
            first_column="A",
            first_row=1,
            last_column="D",
            last_row=3
        )

        self.assertIsInstance(table, Table)
        self.assertEqual(len(table.get_content()), 12)

    def test_set_header(self) -> None:
        """Tests the retrieval of the list of table header cells."""
        table = Table(
            first_column="A",
            first_row=1,
            last_column="D",
            last_row=3,
            total_headers=1
        )

        self.assertIsInstance(table, Table)
        self.assertEqual(len(table.get_content()), 12)
        self.assertEqual(len(table.get_header()), 4)

    def test_get_all_row(self) -> None:
        table = Table("A", 1, "D", 3)
        second_row = table.get_cells_by_row(2)

        self.assertEqual(len(second_row), 4)


if __name__ == '__main__':
    unittest.main()
