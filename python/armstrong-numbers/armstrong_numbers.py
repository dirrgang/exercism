def is_armstrong_number(number):

    digits = [int(x) for x in str(number)]

    sum = 0

    for digit in digits:
        sum += digit ** len(digits)

    return sum == number
