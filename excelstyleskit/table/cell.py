import excelstyleskit.utils as validation


class Cell:
    """Represents a single cell within an Excel file. This class defines the objects that compose a Table object."""
    _column: str
    _row: int

    def __init__(self, column: str, row: int) -> None:
        if not validation.is_character(column):
            raise ValueError("Invalid value column")
        if not validation.is_number(row):
            raise ValueError("Invalid value row")
        self._column = column.upper()
        self._row = row

    def get_cell(self) -> str:
        """Returns the cell in the format <Column><Row>.

        Example
        -------
        >>> cell = Cell('A', 1)
        >>> cell.get_cell()
        'A1'
        """
        return f'{self._column}{self._row}'

    def get_column(self) -> str:
        """Returns the column of the cell.

        Example
        -------
        >>> cell = Cell('A', 1)
        >>> cell.get_column()
        'A'
        """
        return self._column

    def get_row(self) -> int:
        """Returns the row of the cell.

        Example
        -------
        >>> cell = Cell('A', 1)
        >>> cell.get_row()
        1
        """
        return self._row
