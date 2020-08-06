from typing import List


def is_valid(isbn: str) -> bool:
    # Strip dashes
    isbn_list: List[str] = list(isbn.replace("-", ""))

    # The ISBN-10 format is 9 digits (0 to 9) plus one check character (either a digit or an X only)
    if len(isbn_list) != 10:
        return False

    # Convert string to List[int].  In the case the check character is an X,
    # this represents the value '10'.
    try:
        # Because we use static typing, we can't just replace the 'X' with a 10
        # and call it a day. That's why we skip it if it exists and append it after
        if isbn_list[-1] == "X":
            isbn_list_int: List[int] = [int(digit) for digit in isbn_list[:-1]]
            isbn_list_int.append(10)
        else:
            isbn_list_int: List[int] = [int(digit) for digit in isbn_list]

    except ValueError:
        return False

    # Check-Formula: (x1 * 10 + x2 * 9 + x3 * 8 + x4 * 7 + x5 * 6 + 
    # x6 * 5 + x7 * 4 + x8 * 3 + x9 * 2 + x10 * 1) mod 11 == 0
    return sum([isbn_list_int[i] * (10 - i) for i in range(10)]) % 11 == 0
