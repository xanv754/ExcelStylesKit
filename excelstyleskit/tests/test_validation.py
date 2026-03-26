from excelstyleskit.utils import is_cell
import unittest


class TestValidation(unittest.TestCase):
    def test_valid_cell(self) -> None:
        """Tests whether the cell validation is correct."""
        self.assertTrue(is_cell("A1"))
        self.assertTrue(is_cell("A10"))
        self.assertTrue(is_cell("A100"))
        self.assertTrue(is_cell("A1000"))
        self.assertTrue(is_cell("A10000"))
        self.assertTrue(is_cell("A100000"))
        self.assertTrue(is_cell("A1000000"))
        self.assertTrue(is_cell("AA1"))
        self.assertTrue(is_cell("AA10"))
        self.assertTrue(is_cell("AA100"))
        self.assertTrue(is_cell("AA1000"))
        self.assertTrue(is_cell("AA10000"))
        self.assertTrue(is_cell("AA100000"))
        self.assertTrue(is_cell("AA1000000"))
        self.assertTrue(is_cell("AAA1"))
        self.assertTrue(is_cell("AAA10"))
        self.assertTrue(is_cell("AAA100"))
        self.assertTrue(is_cell("AAA1000"))
        self.assertTrue(is_cell("AAA10000"))
        self.assertTrue(is_cell("AAA100000"))
        self.assertTrue(is_cell("AAA1000000"))
        self.assertTrue(is_cell("XFD1048576"))
        self.assertFalse(is_cell("!1"))
        self.assertFalse(is_cell("XFE1"))
        self.assertFalse(is_cell("A1048577"))


if __name__ == "__main__":
    unittest.main()
