#include "armstrong_numbers.h"
#include <stdio.h>
#include <stddef.h>
#include <math.h>
#include <stdlib.h>

bool is_armstrong_number(int candidate)
{
    digitsOfNumber(1234);
    return candidate;
}

int *digitsOfNumber(int number)
{
    int digitLen = (int)floor(log10((float)number)) + 1;
    int *digits = malloc(digitLen * sizeof(int));

    for (int i = 0; i < (digitLen); i++)
    {
        digits[digitLen - i - 1] = number % 10;
        number /= 10;
    }

    return digits;
}