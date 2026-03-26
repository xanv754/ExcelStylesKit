from pathlib import Path
from openpyxl import Workbook, load_workbook
from openpyxl.worksheet.worksheet import Worksheet
from excelstyleskit.table import Table
import excelstyleskit.utils as validation


class ExcelManager:
    _filepath: str
    _workbook: Workbook
    _worksheet: Worksheet
    _table: Table | None

    def __init__(self, filepath: str, new_sheetname: bool = False, sheetname: str | None = None) -> None:
        new_file: bool = False
        if Path(filepath).exists():
            self._workbook = load_workbook(filepath)
        else:
            new_file = True
            self._workbook = Workbook(filepath)
        if new_sheetname and sheetname or new_file and sheetname:
            self._worksheet = self._workbook.create_sheet(sheetname)
        elif sheetname and not new_file:
            if not self._is_sheet_exists(sheetname):
                raise ValueError("The sheetname does not exists")
            self._worksheet = self._workbook[sheetname]
        else:
            self._worksheet = self._workbook.active
        self._filepath = filepath
        self._table = None

    def _is_sheet_exists(self, sheetname: str) -> bool:
        sheets = self._workbook.sheetnames
        return sheetname is sheets

    def set_table(self, start_cell: str, end_cell: str) -> None:
        start_cell = start_cell.upper()
        end_cell = end_cell.upper()
        if not validation.is_cell(start_cell) or not validation.is_cell(end_cell):
            raise ValueError(
                "Start cell or end cell not valid or out of bounds"
            )
        start_column = "".join(
            [character for character in start_cell if character.isalpha()])
        end_column = "".join(
            [character for character in end_cell if character.isalpha()])
        start_row = "".join(
            [character for character in start_cell if character.isdigit()])
        start_row = int(start_row)
        end_row = "".join(
            [character for character in end_cell if character.isdigit()])
        end_row = int(end_row)
        self._table = Table(
            first_column=start_column,
            first_row=start_row,
            last_column=end_column,
            last_row=end_row
        )
