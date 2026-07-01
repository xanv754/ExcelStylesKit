from exceltablekit.constants import COLUMN_MAX, NUMBER_ALPHABET, STRING_ALPHABET
from exceltablekit.errors import ColumnOutOfBoundsError, InvalidColumnValueError


class Alphabet:
    @staticmethod
    def get_string_column_by_number(number: int) -> str:
        """Returns the column letter for a given numeric index.

        Parameters:
        ----------
        number : int
            Reference number of column.
        """
        if number > COLUMN_MAX:
            raise ColumnOutOfBoundsError(number)

        column = ""
        while number > 0:
            number, remainder = divmod(number - 1, 26)
            column = NUMBER_ALPHABET[remainder + 1] + column
        return column

    @staticmethod
    def get_number_column_by_string(column: str) -> int:
        """Returns the numeric index for a given column letter.

        Parameters:
        ----------
        column : str
            Column letters.
        """
        number = 0
        for letter in column.upper():
            try:
                number = number * 26 + STRING_ALPHABET[letter]
            except KeyError:
                raise InvalidColumnValueError(letter, "Letter invalid")
        return number
