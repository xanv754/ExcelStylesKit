import unittest

from exceltablekit.alphabet import Alphabet


class TestAlphabet(unittest.TestCase):
    def test_get_string_column_by_number(self) -> None:
        """Tests the conversion of a numeric index to its corresponding column letter."""
        self.assertEqual(Alphabet.get_string_column_by_number(1), "A")
        self.assertEqual(Alphabet.get_string_column_by_number(26), "Z")
        self.assertEqual(Alphabet.get_string_column_by_number(27), "AA")
        self.assertEqual(Alphabet.get_string_column_by_number(52), "AZ")
        self.assertEqual(Alphabet.get_string_column_by_number(53), "BA")
        self.assertEqual(Alphabet.get_string_column_by_number(78), "BZ")
        self.assertEqual(Alphabet.get_string_column_by_number(702), "ZZ")
        self.assertEqual(Alphabet.get_string_column_by_number(703), "AAA")
        self.assertEqual(Alphabet.get_string_column_by_number(704), "AAB")
        self.assertEqual(Alphabet.get_string_column_by_number(728), "AAZ")
        self.assertEqual(Alphabet.get_string_column_by_number(729), "ABA")
        self.assertEqual(Alphabet.get_string_column_by_number(1378), "AZZ")
        self.assertEqual(Alphabet.get_string_column_by_number(1379), "BAA")
        self.assertEqual(Alphabet.get_string_column_by_number(2304), "CJP")
        self.assertEqual(Alphabet.get_string_column_by_number(2913), "DHA")
        self.assertEqual(Alphabet.get_string_column_by_number(16384), "XFD")

    def test_get_number_column_by_string(self) -> None:
        """Tests the conversion of a column letter to its corresponding numeric index."""
        self.assertEqual(Alphabet.get_number_column_by_string("A"), 1)
        self.assertEqual(Alphabet.get_number_column_by_string("Z"), 26)
        self.assertEqual(Alphabet.get_number_column_by_string("AA"), 27)
        self.assertEqual(Alphabet.get_number_column_by_string("AZ"), 52)
        self.assertEqual(Alphabet.get_number_column_by_string("BA"), 53)
        self.assertEqual(Alphabet.get_number_column_by_string("BZ"), 78)
        self.assertEqual(Alphabet.get_number_column_by_string("ZZ"), 702)
        self.assertEqual(Alphabet.get_number_column_by_string("AAA"), 703)
        self.assertEqual(Alphabet.get_number_column_by_string("AAB"), 704)
        self.assertEqual(Alphabet.get_number_column_by_string("AAZ"), 728)
        self.assertEqual(Alphabet.get_number_column_by_string("ABA"), 729)
        self.assertEqual(Alphabet.get_number_column_by_string("AZZ"), 1378)
        self.assertEqual(Alphabet.get_number_column_by_string("BAA"), 1379)
        self.assertEqual(Alphabet.get_number_column_by_string("CJP"), 2304)
        self.assertEqual(Alphabet.get_number_column_by_string("DHA"), 2913)
        self.assertEqual(Alphabet.get_number_column_by_string("XFD"), 16384)


if __name__ == "__main__":
    unittest.main()
