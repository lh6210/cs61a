
from math import gcd

class Number:
    def __add__(self, other):
        return self.add(other)
    def __mul__(self, other):
        return self.mul(other)


class Rational(Number):
    def __init__(self, numer, denom):
        g = gcd(numer, denom)
        self.number = numer // g
        self.denom = denom // g
    def __repr__(self):
        return 'Rational({0}, {1})'.format(self.number, self.denom)
    def add(self, other):
        nx, dx = self.number, self.denom
        ny, dy = other.number, other.denom
        return Rational(nx * dy + ny * dx, dx * dy)
    def mul(self, other):
        numer = self.numer * other.numer
        denom = self.denom * other.denom
        return Raitonal(numer, denom)


class Ratio:
    def __init__(self, n, d):
        self.numer = n
        self.denom = d

    def __repr__(self):
        return 'Ratio({0}, {1})'.format(self.numer, self.denom)

    def __str__(self):
        return '{0}/{1}'.format(self.numer, self.denom)

    def __add__(self, other):
        if isinstance(other, int):
            n = self.numer + self.denom * other
            d = self.denom
        elif isinstance(other, Ratio):
            n = self.numer * other.denom + self.denom * other.numer
            d = self.denom * other.denom
        elif isinstance(other, float):
            return float(self) + other

        g = gcd(n, d)
        return Ratio(n // g, d // g)

    def __float__(self):
        return self.numer/self.denom

def gcd(n, d):
    while n != d:
        n, d = min(n, d), abs(n - d)
    return n
