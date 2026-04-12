from openpyxl.worksheet.worksheet import Worksheet
from excelstyleskit.table.cell import Cell
from excelstyleskit.alphabet import Alphabet
from excelstyleskit.constants.alphabet import STRING_ALPHABET
import excelstyleskit.utils as validation


class Table:
    _worksheet: Worksheet
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
        if not validation.is_column(first_column) or not validation.is_column(
            last_column
        ):
            raise ValueError("Invalid declaration column")
        if not validation.is_row(first_row) or not validation.is_row(last_row):
            raise ValueError("Invalid declaration row")
        self._worksheet = worksheet
        self._body = []
        self._headers = []
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
                self._body.append(
                    Cell(
                        column=Alphabet.get_string_column_by_number(col),
                        row=row
                    )
                )

    def _set_style_body(self, property: str, value: any, content: list[Cell]) -> None:
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
            for i in range(1, total_row_header + 1):
                self._headers += self.get_cells_by_row(i)
            new_body: list[Cell] = []
            for i in range(total_row_header + 1, STRING_ALPHABET[self._last_column]):
                new_body += self.get_cells_by_row(i)
            self._body = new_body

    def set_style_header(self, property: str, value: any) -> None:
        """Defines the style for all table header cells.

        Parameters:
        ----------
        property : str
            Property to define.
        value : any
            Value of the property to set.
        """
        self._set_style_body(
            property=property,
            value=value,
            content=self._headers
        )

    def set_style_body(self, property: str, value: any) -> None:
        """Defines the style for all table body cells.

        Parameters:
        ----------
        property : str
            Property to define.
        value : any
            Value of the property to set.
        """
        self._set_style_body(
            property=property,
            value=value,
            content=self._body
        )

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

    def display_cells(self) -> None:
        """Displays all cells (column and row coordinates) within the table to the console."""
        for cell in self._body:
            print(cell.get_cell())
