from collections import defaultdict
from typing import Any

from openpyxl.worksheet.worksheet import Worksheet
from tabulate import tabulate

from exceltablekit.alphabet import Alphabet
from exceltablekit.errors import InvalidColumnValueError, InvalidRowValueError
from exceltablekit.table.cell import Cell
from exceltablekit.utils import Validation


class Table:
    _worksheet: Worksheet
    _total_row_headers: int
    _first_column: str
    _first_row: int
    _last_column: str
    _last_row: int
    _num_first_column: int
    _num_last_column: int
    _body: list[Cell]
    _headers: list[Cell]

    def __init__(
        self,
        worksheet: Worksheet,
        first_column: str,
        first_row: int,
        last_column: str,
        last_row: int,
    ) -> None:
        try:
            Validation.column(first_column)
            Validation.column(last_column)
            Validation.row(first_row)
            Validation.row(last_row)
        except (InvalidColumnValueError, InvalidRowValueError):
            raise

        self._worksheet = worksheet
        self._total_row_headers = 0
        self._body = []
        self._headers = []
        self._first_column = first_column
        self._first_row = first_row
        self._last_column = last_column
        self._last_row = last_row
        self._num_first_column = Alphabet.get_number_column_by_string(first_column)
        self._num_last_column = Alphabet.get_number_column_by_string(last_column)
        for col in range(self._num_first_column, self._num_last_column + 1):
            for row in range(first_row, last_row + 1):
                self._body.append(
                    Cell(column=Alphabet.get_string_column_by_number(col), row=row)
                )

    def _set_style(self, property: str, value: Any, content: list[Cell]) -> None:
        """Defines the style for all table body cells.

        Parameters:
        ----------
        property : str
            Property to define.
        value : any
            Value of the property to set.
        content : list[Cell]
            Header o body.
        """
        for cell in content:
            cell.set_property(self._worksheet, property, value)

    def set_header(self, total_row_header: int) -> None:
        """Sets the row count for the table headers."""
        if total_row_header > 0:
            self._headers = []
            header_end = self._first_row + total_row_header
            for i in range(self._first_row, header_end):
                self._headers += self.get_cells_by_row(i)
            new_body: list[Cell] = []
            for i in range(header_end, self._last_row + 1):
                new_body += self.get_cells_by_row(i)
            self._body = new_body
            self._total_row_headers = total_row_header

    def set_style_header(self, property: str, value: Any) -> None:
        """Defines the style for all table header cells.

        Parameters:
        ----------
        property : str
            Property to define.
        value : any
            Value of the property to set.
        """
        self._set_style(property=property, value=value, content=self._headers)

    def set_style_body(self, property: str, value: Any) -> None:
        """Defines the style for all table body cells.

        Parameters:
        ----------
        property : str
            Property to define.
        value : any
            Value of the property to set.
        """
        self._set_style(property=property, value=value, content=self._body)

    def get_cells_by_row(self, num_row: int) -> list[Cell]:
        """Returns all cells within a row for a given row number.

        Parameters:
        ----------
        num_row : int
            The row index or identifier.
        """
        cells: list[Cell] = []
        if num_row > self._last_row:
            raise ValueError("Row number out of bounds.")
        for cell in self._body:
            if cell.get_row() == num_row:
                cells.append(cell)
        return cells

    def get_body(self) -> list[Cell]:
        """Returns the list of cells contained within a table."""
        return self._body

    def get_header(self) -> list[Cell]:
        """Returns the list of cells that form the defined table header."""
        return self._headers

    def get_first_column(self) -> str:
        """Returns the first column letter of the table."""
        return self._first_column

    def get_first_row(self) -> int:
        """Returns the first row number of the table."""
        return self._first_row

    def get_total_row_headers(self) -> int:
        """Returns the number of rows designated as headers."""
        return self._total_row_headers

    def display_cells(self) -> None:
        """Displays all cells (column and row coordinates) within the table to the console."""
        content = self._headers + self._body
        text_content = [cell.get_cell() for cell in content]
        rows_dict: dict[int, list[str]] = defaultdict(list)
        for cell_str in text_content:
            row_num = int("".join(ch for ch in cell_str if ch.isdigit()))
            rows_dict[row_num].append(cell_str)
        table = [rows_dict[key] for key in sorted(rows_dict.keys())]
        print(tabulate(table, tablefmt="simple_grid"))
