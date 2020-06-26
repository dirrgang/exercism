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
            self.card_num = [int(elem) for elem in list(
                self.input)]
        except Exception:
            return False

        result = [((number*2) - 9 if number*2 > 9 else (number*2))
                  if (i+1) % 2 == 0 else number for i,
                  number in enumerate(reversed(self.card_num))]
        result = sum(result)

        if result == 0 and self.length == 1:
            return False
        else:
            return result % 10 == 0
