from typing import List


def classify(number: int) -> str:
    def calc_aliquot_sum(number: int) -> int:
        # In number theory, the aliquot sum s(n) of a positive integer n 
        # is the sum of all proper divisors of n, that is, all divisors 
        # of n other than n itself. It can be used to characterize the 
        # prime numbers, perfect numbers, deficient numbers, abundant 
        # numbers, and untouchable numbers, and to define the aliquot 
        # sequence of a number. 
        divisors: List[int] = []

        for num in range(number)[1:]:
            if number % num == 0:
                divisors.append(num)

        return sum(divisors)

    if number <= 0:
        raise ValueError("Number must be greater than 0")

    aliquot_sum = calc_aliquot_sum(number)

    if aliquot_sum == number:
        # n number theory, a perfect number is a positive integer that 
        # is equal to the sum of its positive divisors, excluding the 
        # number itself.
        return "perfect"
    elif aliquot_sum > number:
        # A number n for which the sum of divisors σ(n) > 2n, or, 
        # equivalently, the sum of proper divisors (or aliquot sum) 
        # s(n) > n.
        #
        # Abundance is the value σ(n) − 2n (or s(n) − n). 
        return "abundant"
    else:
        # In number theory, a deficient number or defective number is a 
        # number n for which the sum of divisors σ(n)<2n, or, 
        # equivalently, the sum of proper divisors (or aliquot sum) 
        # s(n)<n. The value 2n − σ(n) (or n − s(n)) is called the 
        # number's deficiency. 
        return "deficient"
