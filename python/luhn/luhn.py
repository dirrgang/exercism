from typing import List


class Luhn:
    card_num: List[int] = []
    input: str = ""
    length: int = 0

    def __init__(self, card_num: str) -> None:
        self.input = card_num.replace(" ", "")
        self.length = len(self.input)

    def valid(self) -> bool:
        try:
            # Turn input string into List[int]
            self.card_num = [int(elem) for elem in list(
                self.input)]
        except Exception:
            return False

        # LUHN FORMULA
        # 1. From the rightmost digit (excluding the check digit) and moving
        # left, double the value of every second digit. The check digit is neither
        # doubled nor included in this calculation; the first digit doubled is
        # the digit located immediately left of the check digit. If the result
        # of this doubling operation is greater than 9 (e.g., 8 × 2 = 16), then
        # add the digits of the result (e.g., 16: 1 + 6 = 7, 18: 1 + 8 = 9) or,
        # alternatively, the same final result can be found by subtracting 9
        # from that result (e.g., 16: 16 − 9 = 7, 18: 18 − 9 = 9).
        result = [((number*2) - 9 if number*2 > 9 else (number*2))
                  if (i+1) % 2 == 0 else number for i,
                  number in enumerate(reversed(self.card_num))]

        # 2. Take the sum of all the digits.
        result = sum(result)

        if result == 0 and self.length == 1:
            # Dealing with some edge-cases
            return False
        else:
            # If the total modulo 10 is equal to 0 (if the total ends in zero)
            # then the number is valid according to the Luhn formula; otherwise
            # it is not valid.
            return result % 10 == 0
