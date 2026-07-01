from typing import Any

from openpyxl.worksheet.worksheet import Worksheet

from exceltablekit.errors import InvalidColumnValueError, InvalidRowValueError
from exceltablekit.utils import Validation


class Cell:
    """Represents a single cell within an Excel file. This class defines the objects that compose a Table object."""

    _column: str
    _row: int

    def __init__(self, column: str, row: int) -> None:
        try:
            Validation.column(column)
            Validation.row(row)
        except (InvalidColumnValueError, InvalidRowValueError):
            raise
        else:
            self._column = column.upper()
            self._row = row

    def set_property(self, worksheet: Worksheet, property: str, value: Any) -> None:
        """Sets the values for an existing property of a cell.

        Parameters:
        -----------
        worksheet : Worksheet
            Active worksheet.
        property : str
            Property to define.
        value : Any
            Value of the property to set.
        """
        cell = worksheet[self.get_cell()]
        setattr(cell, property, value)

    def get_cell(self) -> str:
        """Returns the cell in the format <Column><Row>.

        Example
        -------
        >>> cell = Cell('A', 1)
        >>> cell.get_cell()
        'A1'
        """
        return f"{self._column}{self._row}"

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
