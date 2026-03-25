from excelstyleskit.constants import NUMBER_ALPHABET, STRING_ALPHABET


class Alphabet:
    @staticmethod
    def get_total_letters_by_number(number: int) -> int:
        """Returns the total character count of the column name for a given reference number.

        Parameters:
        -----------
        number : int
            Reference number of column.
        """
        if number > 16384:
            raise ValueError("Column number out of bounds")
        if number <= 26:
            return 1
        if number <= 702:
            return 2
        return 3

    @staticmethod
    def get_string_column_by_number(number: int) -> str:
        """Returns the column letter for a given numeric index.

        Parameters:
        ----------
        number : int
            Reference number of column.
        """
        column = ""
        total_letters = Alphabet.get_total_letters_by_number(number)
        for i in range(0, total_letters):
            num_letter = number % 26
            if num_letter == 0:
                num_letter = 26
            column += NUMBER_ALPHABET[num_letter]
            number = int(number / 26)
            if (_next_round := i + 1) < total_letters and column == "Z" or column == "ZZ":
                number -= 1
        return column[::-1]

    @staticmethod
    def get_number_column_by_string(column: str) -> int:
        """Returns the numeric index for a given column letter.

        Parameters:
        ----------
        column : str
            Column letters.
        """
        column = column.upper()
        number = 0
        letters = list(column)
        total_letters = len(letters)
        for letter in letters:
            num_letter = STRING_ALPHABET[letter]
            number += num_letter
            total_letters -= 1
            if total_letters > 0:
                number *= 26
        return number
