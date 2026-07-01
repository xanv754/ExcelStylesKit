from exceltablekit.errors.base import ExcelTableKitError


class ExcelSheetMissingError(ExcelTableKitError):
    def __init__(self, sheetname: str) -> None:
        self.value = sheetname

        super().__init__(f"Excel sheet name '{sheetname}' does not exist")
