from typing import List


def classify(number: int) -> str:
    def calc_aliquot_sum(number: int) -> int:
        divisors: List[int] = []

        for num in range(number)[1:]:
            if number % num == 0:
                divisors.append(num)

        return sum(divisors)

    if number <= 0:
        raise ValueError("Number must be greater than 0")

    aliquot_sum = calc_aliquot_sum(number)

    if aliquot_sum == number:
        return "perfect"
    elif aliquot_sum > number:
        return "abundant"
    else:
        return "deficient"
