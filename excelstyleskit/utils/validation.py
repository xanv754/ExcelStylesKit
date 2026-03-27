from excelstyleskit.constants import ROW_MAX, COLUMN_MAX
from excelstyleskit.alphabet import Alphabet


def is_column(value: any) -> bool:
    try:
        return (
            isinstance(value, str)
            and value.isalpha()
            and Alphabet.get_number_column_by_string(value) <= COLUMN_MAX
        )
    except Exception as error:
        return False


def is_row(value: any) -> bool:
    try:
        return isinstance(value, int) and 0 < int(value) <= ROW_MAX
    except Exception as error:
        return False


def is_cell(cell: str) -> bool:
    if len(cell) > 10:
        return False
    characters: list[str] = list(cell)
    column: str = ""
    row: str = ""
    for character in characters:
        if character.isalpha():
            column += character
        elif character.isdigit():
            row += character
        else:
            return False
    return is_column(column) and is_row(int(row))
