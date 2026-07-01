import re
from typing import Any

from exceltablekit.alphabet import Alphabet
from exceltablekit.constants import COLUMN_MAX, ROW_MAX
from exceltablekit.errors import (
    InvalidCellError,
    InvalidColumnValueError,
    InvalidRowValueError,
)


class Validation:
    _CELL_PATTERN = re.compile(r"^([A-Za-z]+)(\d+)$")

    @staticmethod
    def column(value: Any) -> None:
        if not isinstance(value, str):
            raise InvalidColumnValueError(value, "The value must be a string")
        if not value.isalpha():
            raise InvalidColumnValueError(value, "The value must be letters")
        if not Alphabet.get_number_column_by_string(value) <= COLUMN_MAX:
            raise InvalidColumnValueError(value, "The value exceeds the allowed limit")

    @staticmethod
    def row(value: Any) -> None:
        if not isinstance(value, int):
            raise InvalidRowValueError(value, "The value must be an integer")
        if value <= 0:
            raise InvalidRowValueError(value, "The value cannot be negative")
        if value > ROW_MAX:
            raise InvalidRowValueError(value, "The value exceeds the allowed limit")

    @staticmethod
    def cell(value: str) -> None:
        if len(value) > 10:
            raise InvalidCellError(value)

        match = Validation._CELL_PATTERN.match(value)
        if not match:
            raise InvalidCellError(value)

        column, row = match.groups()
        Validation.column(column)
        Validation.row(int(row))
