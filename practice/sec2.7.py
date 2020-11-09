
from math import gcd, atan, cos, sin, sqrt


class Number:
    """This class requires the Number objects have a add and mul methods, but doesn't define them.
    Moreover, it does not have an __init__ method.
    The purpose of Number is to serve as a superclass of various specific number classes.

    """
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


class Account:
    interest = 0.01
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0
    def __bool__(self):
        return self.balance != 0
    def __str__(self):
        return self.holder + "\'s account"

class CheckingAccount(Account):
    def __init__(self, account_holder):
        self.holder = account_holder
        self.balance = 0

    @property
    def interest(self):
        return Account.interest * 2







def adder(n):
    def addN(k):
        return k + n
    return addN

class Adder:
    def __init__(self, n):
        self.n = n
    def __call__(self, k):
        return self.n + k


class Celsius:
    def __init__(self, degree = 0):
        self._degree = degree
    def to_fahrenheit(self):
        return (self._degree * 1.8) + 32
    def get_temperature(self):
        return self._degree
    def set_temperature(self, d):
        if d < -273.15:
            raise ValueError('Temperature below -273.15 is not possible.')
        self._degree = d

class Person:
    def __init__(self, firstname, lastname):
        self.first = firstname
        self.last = lastname

    @property
    def fullname(self):
        return self.first + ' ' + self.last

    @fullname.setter
    def fullname(self, name):
        firstname, lastname = name.split()
        self.first = firstname
        self.last = lastname

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)


class Complex(Number):
    def add(self, other):
        return ComplexRI(self.rel + other.rel, self.img + other.img)
    def mul(self, other):
        return ComplexMA(self.mag * other.mag, self.amp + other.amp)

class ComplexRI(Complex):
    def __init__(self, rel, img):
        self.rel = rel
        self.img = img
    def __repr__(self):
        return "ComplexRI(" + str(self.rel) + ", " + str(self.img) + ")"
    
    @property
    def mag(self):
        return sqrt(self.rel ** 2 + self.img ** 2)

    @property
    def amp(self):
        return atan2(self.img, self.rel)

class ComplexMA(Complex):
    def __init__(self, m, a):
        self.mag = m
        self.amp = a

    def __repr__(self):
        return "ComplexMA( " + str(self.mag) + ", " + str(self.amp) + ")" 

    @property
    def real(self):
        return self.mag * math.cos(self.amp)

    @property
    def img(self):
        return self.mag * math.sin(self.amp)




