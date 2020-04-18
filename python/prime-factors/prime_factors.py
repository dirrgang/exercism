from typing import List

def factors(value: int) -> List[int]:
    factors: List[int] = []

    while value % 2 == 0:
        factors.append(2)
        value = int(value/2)

    potential_factor = 3

    while potential_factor ** 2 <= value:
        if value % potential_factor == 0:
            factors.append(potential_factor)
            value = int(value/potential_factor)
        else:
            potential_factor += 2

    if value != 1:
        factors.append(value)

    return factors
