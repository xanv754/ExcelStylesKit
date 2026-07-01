from __future__ import annotations

from pathlib import Path
from types import TracebackType

from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet


class TestExcel:
    __test__ = False

    path: Path
    workbook: Workbook
    worksheet: Worksheet

    def __init__(self, filepath: str | Path | None = None) -> None:
        if filepath is None:
            filepath = Path(__file__).parent / "example_excel.xlsx"
        self.path = Path(filepath)
        self.delete()
        self.workbook = Workbook()
        worksheet = self.workbook.active
        if worksheet is None:
            worksheet = self.workbook.create_sheet()
        self.worksheet = worksheet

    @property
    def filepath(self) -> str:
        return str(self.path.resolve())

    def save(self) -> None:
        self.workbook.save(self.path)

    def delete(self) -> None:
        self.path.unlink(missing_ok=True)

    def __enter__(self) -> TestExcel:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        self.delete()


if __name__ == "__main__":
    with TestExcel() as excel:
        excel.save()
