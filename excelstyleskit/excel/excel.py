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

    def __init__(
        self, filepath: str, new_sheetname: bool = False, sheetname: str | None = None
    ) -> None:
        new_file: bool = False
        if Path(filepath).exists():
            self._workbook = load_workbook(filepath)
        else:
            new_file = True
            self._workbook = Workbook()
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
        """Returns true if a specific worksheet exists within the workbook.

        Parameters:
        -----------
        sheetname : str
            Sheet name of worksheet.
        """
        sheets = self._workbook.sheetnames
        return sheetname is sheets

    def _get_column(self, cell: str) -> str:
        """Gets the column part of a cell address."""
        return "".join([character for character in cell if character.isalpha()])

    def _get_row(self, cell: str) -> int:
        """Gets the row part of a cell address."""
        return int("".join([character for character in cell if character.isdigit()]))

    def set_table(self, start_cell: str, end_cell: str) -> None:
        """Defines the table area within the Excel worksheet.}

        Parameters:
        ----------
        start_cell : str
            Starting cell of the table.
        end_cell : str
            Ending cell of the table.

        Example:
        -------
        >> my_excel = ExcelManager("my_excel.xlsx")
        >> my_excel.set_table("A1", "D4")
        """
        start_cell = start_cell.upper()
        end_cell = end_cell.upper()
        if not validation.is_cell(start_cell) or not validation.is_cell(end_cell):
            raise ValueError(
                "Starting cell or ending cell not valid or out of bounds")
        start_column = self._get_column(start_cell)
        end_column = self._get_column(end_cell)
        start_row = self._get_row(start_cell)
        end_row = self._get_row(end_cell)
        self._table = Table(
            worksheet=self._worksheet,
            first_column=start_column,
            first_row=start_row,
            last_column=end_column,
            last_row=end_row,
        )

    def define_header(self, rows: int) -> None:
        """Defines trhe number of rows that the table will use as its header.

        Parameters:
        ----------
        rows : int
            Total count of rows designated as headers.
        """
        self._table.set_header(rows)

    def apply_style_header(self, property: str, value: any) -> None:
        """Applies a style to the header Excel table.

        Parameters:
        ----------
        property : str
            Property to define.
        value : any
            Value of the property to set.
        """
        if not self._table or not self._table.get_header():
            raise Exception("Table or header table not defined")
        self._table.set_style_header(property, value)
        self._workbook.save(self._filepath)

    def apply_style_body(self, property: str, value: any) -> None:
        """Applies a style to the body Excel table.

        Parameters:
        ----------
        property : str
            Property to define.
        value : any
            Value of the property to set.
        """
        if not self._table:
            raise Exception("Table not defined")
        self._table.set_style_body(property, value)
        self._workbook.save(self._filepath)

    def apply_style_table(self, property: str, value: any) -> None:
        """Applies a style to the Excel table.

        Parameters:
        ----------
        property : str
            Property to define.
        value : any
            Value of the property to set.
        """
        if not self._table:
            raise Exception("Table not defined")
        if self._table.get_header():
            self._table.set_style_header(property, value)
        self._table.set_style_body(property, value)
        self._workbook.save(self._filepath)
