from typing import List


def is_armstrong_number(number: int) -> bool:

    # Convert string to number to make it iterable
    digits: List[int] = [int(x) for x in str(number)]

    # An Armstrong number is a number that is the sum of its own digits
    # each raised to the power of the number of digits.
    return sum([digit ** len(digits) for digit in digits]) == number
