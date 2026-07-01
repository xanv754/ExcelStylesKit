import unittest

from exceltablekit.excel import ExcelManager, ExcelStyle
from tests import TestExcel


class TestExcelStyles(unittest.TestCase):
    def test_set_background(self) -> None:
        """Tests the style configuration for applying a background color to an Excel table."""
        with TestExcel() as file:
            blue = "0000FF"
            red = "FF0000"
            excel = ExcelManager(file.filepath)
            excel.set_table("A1", "D4")
            excel.define_header(rows=1)
            styles = ExcelStyle(excel)
            styles.set_background(blue)
            styles.set_header_background(red)

    def test_set_font(self) -> None:
        """Tests the style configuration for applying font settings to an Excel table."""
        with TestExcel() as file:
            file = TestExcel()
            excel = ExcelManager(file.filepath)
            excel.set_table("A1", "D4")
            styles = ExcelStyle(excel)
            styles.set_font(type="Arial", size=34)

    def test_set_alignment(self) -> None:
        """Tests the style configuration for applying alignment settings to an Excel table."""
        with TestExcel() as file:
            file = TestExcel()
            excel = ExcelManager(file.filepath)
            excel.set_table("A1", "D4")
            styles = ExcelStyle(excel)
            styles.set_alignment(horizontal="center")

    def test_set_border(self) -> None:
        """Tests the style configuration for applying border settings to an Excel table."""
        with TestExcel() as file:
            file = TestExcel()
            excel = ExcelManager(file.filepath)
            excel.set_table("A1", "D4")
            styles = ExcelStyle(excel)
            styles.set_border()

    def test_freeze_header(self) -> None:
        """Tests that freeze_header freezes the correct row in the worksheet."""
        with TestExcel() as file:
            file.save()
            excel = ExcelManager(file.filepath)
            excel.set_table("A1", "D10")
            excel.define_header(rows=2)
            styles = ExcelStyle(excel)
            styles.freeze_header()
            self.assertEqual(file.workbook["Sheet"].freeze_panes, None)
            from openpyxl import load_workbook
            wb = load_workbook(file.filepath)
            ws = wb.active
            self.assertEqual(ws.freeze_panes, "A3")

    def test_freeze_header_two_rows(self) -> None:
        """Tests that freeze_header freezes correctly with two header rows."""
        with TestExcel() as file:
            file.save()
            excel = ExcelManager(file.filepath)
            excel.set_table("A1", "D20")
            excel.define_header(rows=3)
            styles = ExcelStyle(excel)
            styles.freeze_header()
            from openpyxl import load_workbook
            wb = load_workbook(file.filepath)
            ws = wb.active
            self.assertEqual(ws.freeze_panes, "A4")

    def test_freeze_header_offset_start(self) -> None:
        """Tests that freeze_header accounts for tables not starting at row 1."""
        with TestExcel() as file:
            file.save()
            excel = ExcelManager(file.filepath)
            excel.set_table("B3", "F12")
            excel.define_header(rows=1)
            styles = ExcelStyle(excel)
            styles.freeze_header()
            from openpyxl import load_workbook
            wb = load_workbook(file.filepath)
            ws = wb.active
            self.assertEqual(ws.freeze_panes, "B4")

    def test_auto_fit_columns(self) -> None:
        """Tests that auto_fit_columns sets each column width to the longest cell content plus padding."""
        from openpyxl import load_workbook
        with TestExcel() as file:
            file.worksheet["A1"] = "Short"
            file.worksheet["A2"] = "A much longer value"
            file.worksheet["B1"] = "Hello"
            file.worksheet["B2"] = "Hi"
            file.save()
            excel = ExcelManager(file.filepath)
            excel.set_table("A1", "B2")
            styles = ExcelStyle(excel)
            styles.auto_fit_columns()
            wb = load_workbook(file.filepath)
            ws = wb.active
            self.assertEqual(ws.column_dimensions["A"].width, len("A much longer value") + 2)
            self.assertEqual(ws.column_dimensions["B"].width, len("Hello") + 2)


if __name__ == "__main__":
    unittest.main()
