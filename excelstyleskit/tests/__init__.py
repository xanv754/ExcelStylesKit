from os import remove
from pathlib import Path
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet


class TestExcel:
    filepath: str
    workbook: Workbook
    worksheet: Worksheet

    def __init__(self, filepath: str | None = None) -> None:
        if filepath is None:
            home = Path.cwd()
            filepath = f'{home}/excelstyleskit/tests/example_excel.xlsx'
        self.filepath = filepath
        self.delete()
        self.workbook = Workbook()
        self.worksheet = self.workbook.active

    def save(self) -> None:
        self.workbook.save(self.filepath)

    def delete(self) -> None:
        if Path(self.filepath).exists():
            remove(self.filepath)


if __name__ == "__main__":
    excel_example = TestExcel()
    excel_example.save()
    excel_example.delete()
