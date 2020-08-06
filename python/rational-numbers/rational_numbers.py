from __future__ import division, annotations

import math


class Rational:
    def __init__(self, numer: int, denom: int):
        self.numer: int = numer
        self.denom: int = denom

    def __eq__(self, other: Rational) -> bool:
        self = self.get_reduced_term(self)
        other = self.get_reduced_term(other)

        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self) -> str:
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other: Rational) -> Rational:
        self.numer = ((self.numer * other.denom) + (other.numer * self.denom))
        self.denom = self.denom * other.denom

        self = self.get_reduced_term(self)

        return self

    def __sub__(self, other: Rational) -> Rational:
        self.numer = ((self.numer * other.denom) - (other.numer * self.denom))
        self.denom = self.denom * other.denom

        self = self.get_reduced_term(self)

        return self

    def __mul__(self, other: Rational) -> Rational:
        self.numer = self.numer * other.numer
        self.denom = self.denom * other.denom

        self = self.get_reduced_term(self)

        return self

    def __truediv__(self, other: Rational) -> Rational:
        self.numer = (self.numer * other.denom)
        self.denom = (other.numer * self.denom)

        self = self.get_reduced_term(self)

        return self

    def __abs__(self) -> Rational:
        self.numer = abs(self.numer)
        self.denom = abs(self.denom)

        self = self.get_reduced_term(self)

        return self

    def __pow__(self, power: int) -> Rational:
        self.numer **= power
        self.denom **= power

        self = self.get_reduced_term(self)

        return self

    def __rpow__(self, base: int) -> int:
        base **= int(self.numer / self.denom)

        return base

    def get_reduced_term(self, rational: Rational) -> Rational:
        gcd = math.gcd(rational.numer, rational.denom)

        rational.numer = round(rational.numer / gcd)
        rational.denom = round(rational.denom / gcd)

        if rational.denom < 0:
            if rational.numer < 0:
                rational.denom = abs(rational.denom)
                rational.numer = abs(rational.numer)
            else:
                rational.denom = abs(rational.denom)
                rational.numer *= -1

        return rational
