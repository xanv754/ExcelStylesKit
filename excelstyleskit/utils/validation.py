def is_character(value: any) -> boolean:
    try:
        if isinstance(value, str):
            return value.isalpha()
        return False
    except:
        return False

def is_number(value: any) -> boolean:
    try:
        if isinstance(value, int) and 0 < int(value) < 1000:
            return True
        return False
    except:
        return False
