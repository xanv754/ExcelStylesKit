from typing import Any

from exceltablekit.errors.base import ExcelTableKitError


# ==========================================
# COLUMN ERRORS
# ==========================================
class InvalidColumnValueError(ExcelTableKitError):
    def __init__(self, value: Any, reason: str) -> None:
        self.value = value
        self.reason = reason

        super().__init__(f"The value '{value}' is not allowed as a column: {reason}")


class ColumnOutOfBoundsError(ExcelTableKitError):
    def __init__(self, value: int) -> None:
        self.value = value

        super().__init__(f"Column index '{value}' is out of bounds")


# ==========================================
# ROW ERRORS
# ==========================================
class InvalidRowValueError(ExcelTableKitError):
    def __init__(self, value: Any, reason: str) -> None:
        self.value = value
        self.reason = reason

        super().__init__(f"The value '{value}' is not allowed as a row: {reason}")


# ==========================================
# CELL ERRORS
# ==========================================
class InvalidCellError(ExcelTableKitError):
    def __init__(self, value: Any) -> None:
        self.value = value

        super().__init__(f"The cell {value} is not valid or out of bounds")
