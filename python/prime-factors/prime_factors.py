from typing import List

def factors(n: int) -> List[int]:

    factorization = []
    primes = sieve_of_eratosthenes(n)

    for d in primes:
        if (d*d > n):
            break
        while (n % d == 0):

            factorization.append(d)
            n /= d
    if n > 1:
        factorization.append(n)

    return factorization


def fermat(n: int)

# def sieve_of_eratosthenes(n: int) -> List[int]:

#     primes: List[bool] = [True for i in range(n + 1)]

#     primes[0] = primes[1] = False

#     i = 2
    # while (i*i <= n):
#         if (primes[i]):
#             j = i*i
#             while(j <= n):
#                 primes[j] = False
#                 j += i
#         i += 1

#     return [index for index in range(n) if primes[index] == True]
