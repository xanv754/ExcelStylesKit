from exceltablekit.errors.base import ExcelTableKitError


class TableBackgroundError(ExcelTableKitError):
    def __init__(self, error: Exception) -> None:
        super().__init__(f"Failed to apply background color to the table: {error}")


class TableFontError(ExcelTableKitError):
    def __init__(self, error: Exception) -> None:
        super().__init__(f"Failed to apply font style to the table: {error}")


class TableAlignmentError(ExcelTableKitError):
    def __init__(self, error: Exception) -> None:
        super().__init__(f"Failed to apply text alignment to the table: {error}")


class TableBorderError(ExcelTableKitError):
    def __init__(self, error: Exception) -> None:
        super().__init__(f"Failed to apply borders to the table: {error}")


class HeaderTableBackgroundError(ExcelTableKitError):
    def __init__(self, error: Exception) -> None:
        super().__init__(
            f"Failed to apply background color to the table header: {error}"
        )


class HeaderTableFontError(ExcelTableKitError):
    def __init__(self, error: Exception) -> None:
        super().__init__(f"Failed to apply font style to the table header: {error}")


class HeaderTableAlignmentError(ExcelTableKitError):
    def __init__(self, error: Exception) -> None:
        super().__init__(f"Failed to apply text alignment to the table header: {error}")


class HeaderTableBorderError(ExcelTableKitError):
    def __init__(self, error: Exception) -> None:
        super().__init__(f"Failed to apply borders to the table header: {error}")


class HeaderTableFreezeError(ExcelTableKitError):
    def __init__(self, error: Exception) -> None:
        super().__init__(f"Failed to freeze the table header rows: {error}")


class TableColumnWidthError(ExcelTableKitError):
    def __init__(self, error: Exception) -> None:
        super().__init__(f"Failed to auto-fit column widths: {error}")
