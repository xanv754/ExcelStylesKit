from excelstyleskit.table.cell import Cell
from excelstyleskit.alphabet import Alphabet
import excelstyleskit.utils as validation


class Table:
    _first_column: str
    _first_row: int
    _last_column: str
    _last_row: int
    _num_first_column: int
    _num_last_column: int
    _content: list[Cell]
    _headers: list[Cell]

    def __init__(self, first_column: str, first_row: int, last_column: str, last_row: int, total_headers: int = 0) -> None:
        if not validation.is_character(first_column) or not validation.is_character(last_column):
            raise ValueError("Invalid declaration column")
        if not validation.is_number(first_row) or not validation.is_number(last_row):
            raise ValueError("Invalid declaration row")
        self._content = []
        self._first_column = first_column
        self._first_row = first_row
        self._last_column = last_column
        self._last_row = last_row
        self._num_first_column = Alphabet.get_number_column_by_string(
            first_column)
        self._num_last_column = Alphabet.get_number_column_by_string(
            last_column)
        for col in range(self._num_first_column, self._num_last_column + 1):
            for row in range(first_row, last_row + 1):
                self._content.append(
                    Cell(
                        column=Alphabet.get_string_column_by_number(col),
                        row=row
                    )
                )
        if total_headers > 0:
            self._headers = []
            for i in range(1, total_headers + 1):
                self._headers += self.get_cells_by_row(i)

    def get_cells_by_row(self, num_row: int) -> list[Cell]:
        """Returns all cells within a row for a given row number.

        Parameters:
        ----------
        num_row : int
            The row index or identifier.
        """
        cells: list[Cell] = []
        if num_row > self._last_row:
            return ValueError("Row number out of bounds.")
        for cell in self._content:
            if cell.get_row() == num_row:
                cells.append(cell)
        return cells

    def get_content(self) -> list[Cell]:
        """Returns the list of cells contained within a table."""
        return self._content

    def get_header(self) -> list[Cell]:
        """Returns the list of cells that form the defined table header."""
        return self._headers

    def display_cells(self) -> None:
        """Displays all cells (column and row coordinates) within the table to the console."""
        for cell in self._content:
            print(cell.get_cell())
