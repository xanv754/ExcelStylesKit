from excelstyleskit.excel import ExcelManager, ExcelStyle
from excelstyleskit.tests import TestExcel
import unittest


class TestExcelStyles(unittest.TestCase):
    def test_set_background(self) -> None:
        """Tests the style configuration for applying a background color to an Excel table."""
        file = TestExcel()
        blue = "0000FF"
        excel = ExcelManager(file.filepath)
        excel.set_table("A1", "D4")
        styles = ExcelStyle(excel)
        self.assertTrue(styles.set_background(blue))
        file.delete()

    def test_set_font(self) -> None:
        """Tests the style configuration for applying font settings to an Excel table."""
        file = TestExcel()
        excel = ExcelManager(file.filepath)
        excel.set_table("A1", "D4")
        styles = ExcelStyle(excel)
        self.assertTrue(styles.set_font(type="Arial", size="34"))
        file.delete()

    def test_set_alignment(self) -> None:
        """Tests the style configuration for applying alignment settings to an Excel table."""
        file = TestExcel()
        excel = ExcelManager(file.filepath)
        excel.set_table("A1", "D4")
        styles = ExcelStyle(excel)
        self.assertTrue(styles.set_alignment(horizontal="center"))
        file.delete()

    def test_set_border(self) -> None:
        """Tests the style configuration for applying border settings to an Excel table."""
        file = TestExcel()
        excel = ExcelManager(file.filepath)
        excel.set_table("A1", "D4")
        styles = ExcelStyle(excel)
        self.assertTrue(styles.set_border())
        file.delete()


if __name__ == "__main__":
    unittest.main()
