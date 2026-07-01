from exceltablekit.errors.base import ExcelTableKitError


class TableNotDefinedError(ExcelTableKitError):
    def __init__(self) -> None:
        super().__init__("The excel table is not defined")


class HeaderTableNotDefinedError(ExcelTableKitError):
    def __init__(self) -> None:
        super().__init__("The header of the excel table is not defined")
