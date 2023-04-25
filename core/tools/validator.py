def validate_code(hex_code):
    try:
        if "#" in hex_code:
            code = hex_code.split("#")[1]

        else:
            code = hex_code

        if len(code) != 6:
            return False

        code = f"0x{code}"
        code = int(code, 16)

    except:
        return False

    return True


def validate_numbers(high, width):
    try:
        high = int(high)
        width = int(width)

    except:
        return False

    return True
