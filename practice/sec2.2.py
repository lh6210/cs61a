from math import gcd

def rational(n, d):
    g = gcd(n, d)
    return [n // g, d // g]

def numer(x):
    return x[0]

def denom(x):
    return x[1]

def add_rationals(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * dy + dx * ny, dx * dy)

def print_rational(x):
    nx, dx = numer(x), denom(x)
    print(nx, '/', dx)

def mul_rationals(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    return rational(nx * ny, dx * dy)


def pair(x, y):
    def get(index):
        if index == 0:
            return x
        elif index == 1:
            return y
    return get

def select(p, i):
    """Return the element at index i of pair p"""
    return p(i)

