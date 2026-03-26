from excelstyleskit.constants import ROW_MAX, COLUMN_MAX
from excelstyleskit.alphabet import Alphabet


def is_character(value: any) -> bool:
    try:
        if isinstance(value, str):
            return value.isalpha()
        return False
    except Exception as error:
        return False


def is_number(value: any) -> bool:
    try:
        if isinstance(value, int) and 0 < int(value) < ROW_MAX:
            return True
        return False
    except Exception as error:
        return False


def is_cell(cell: str) -> bool:
    if len(cell) > 10:
        return False
    characters: list[str] = list(cell)
    counter: int = 1
    column: str = ""
    row: str = ""
    for character in characters:
        if counter <= 3:
            if not character.isalpha() and not character.isdigit():
                return False
            elif character.isalpha():
                column += character.upper()
            else:
                row += character
        else:
            if not character.isdigit():
                return False
            else:
                row += character
        counter += 1
    num_row = int(row)
    if num_row > ROW_MAX:
        return False
    num_col = Alphabet.get_number_column_by_string(column)
    if num_col > COLUMN_MAX:
        return False
    return True
