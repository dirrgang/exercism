from __future__ import division

import math


class Rational:
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom

    def __eq__(self, other):
        self = self.get_reduced_term(self)
        other = self.get_reduced_term(other)

        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        self.numer = ((self.numer * other.denom) + (other.numer * self.denom))
        self.denom = self.denom * other.denom

        self = self.get_reduced_term(self)

        return self

    def __sub__(self, other):
        self.numer = ((self.numer * other.denom) - (other.numer * self.denom))
        self.denom = self.denom * other.denom

        self = self.get_reduced_term(self)

        return self

    def __mul__(self, other):
        self.numer = self.numer * other.numer
        self.denom = self.denom * other.denom

        self = self.get_reduced_term(self)

        return self

    def __truediv__(self, other):
        self.numer = (self.numer * other.denom)
        self.denom = (other.numer * self.denom)

        self = self.get_reduced_term(self)

        return self

    def __abs__(self):
        self.numer = abs(self.numer)
        self.denom = abs(self.denom)

        self = self.get_reduced_term(self)

        return self

    def __pow__(self, power):
        self.numer **= power
        self.denom **= power

        self = self.get_reduced_term(self)

        return self

    def __rpow__(self, base):
        base **= (self.numer / self.denom)

        return base

    def get_reduced_term(self, rational):
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
