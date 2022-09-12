def get_consecutive_number(string, start, stop=-1):
    """
    from a given start point, start going backwards recollecting
    decimal integers until stop index, stop recollecting if decimal
    integer is not found, then return the number backwards
    """

    number = ""
    for idx in range(start - 1, stop, -1): # Going  backwards
        if not string[idx].isdecimal(): # Not decimal integer
            break
        number += string[idx]
    return 1 if not number else int(number[::-1])
