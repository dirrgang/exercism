"""
This exercise stub and the test suite contain several enumerated constants.

Since Python 2 does not have the enum module, the idiomatic way to write
enumerated constants has traditionally been a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""


# Score categories.
# Change the values as you see fit.

from enum import Enum, auto

YACHT = 0
ONES = 1
TWOS = 2
THREES = 3
FOURS = 4
FIVES = 5
SIXES = 6
FULL_HOUSE = 7
FOUR_OF_A_KIND = 8
LITTLE_STRAIGHT = 9
BIG_STRAIGHT = 10
CHOICE = 11


def score(dice, category):
    if category == ONES:
        return dice.count(1)

    elif category == TWOS:
        return dice.count(2) * 2

    elif category == THREES:
        return dice.count(3) * 3

    elif category == FOURS:
        return dice.count(4) * 4

    elif category == FIVES:
        return dice.count(5) * 5

    elif category == SIXES:
        return dice.count(6) * 6

    elif category == FULL_HOUSE:
        return sum(dice)

    elif category == FOUR_OF_A_KIND:
        for number in dice:
            if dice.count(number) == 4:
                return number * 4
    
    elif category == LITTLE_STRAIGHT:
        return 30

    elif category == BIG_STRAIGHT:
        return 30

    elif category == CHOICE:
        return sum(dice)

    elif category == YACHT:
        return 50
