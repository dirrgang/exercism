def square(number: int) -> int:
    if number <= 0 or number > 64:
        raise ValueError("Number must be 1 <= n <= 64")

    return 2**(number-1)


def total() -> int:
    return sum(square(n) for n in range(1, 65))
