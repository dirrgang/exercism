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

from enum import auto

YACHT = auto()
ONES = auto()
TWOS = auto()
THREES = auto()
FOURS = auto()
FIVES = auto()
SIXES = auto()
FULL_HOUSE = auto()
FOUR_OF_A_KIND = auto()
LITTLE_STRAIGHT = auto()
BIG_STRAIGHT = auto()
CHOICE = auto()


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
        for number in dice:
            if dice.count(number) == 3:
                for number in dice:
                    if dice.count(number) == 2:
                        return sum(dice)

        return 0

    elif category == FOUR_OF_A_KIND:
        for number in dice:
            if dice.count(number) >= 4:
                return number * 4
        return 0

    elif category == LITTLE_STRAIGHT:
        if sorted(dice) == [1, 2, 3, 4, 5]:
            return 30
        else:
            return 0

    elif category == BIG_STRAIGHT:
        if sorted(dice) == [2, 3, 4, 5, 6]:
            return 30
        else:
            return 0

    elif category == CHOICE:
        return sum(dice)

    elif category == YACHT:
        last = dice[0]
        for die in dice:
            if die != last:
                return 0
        return 50
