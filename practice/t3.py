
from math import sqrt

def make_adder(n):
    def adder(k):
        return n + k
    return adder

def square(x):
    return x * x

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h


def improve(update, close, guess = 1):
    while not close(guess):
        guess = update(guess)
    return guess

def sq_root(a):
    """ find the principle square root of argument a;
    the accuracy depends on the global function approx_eq

    >>> b = sq_root(2)
    >>> approx_eq(b, sqrt(2))
    True
    >>> approx_eq(sq_root(5), sqrt(5))
    True
    """
    def f(x):
        return pow(x, 2) - a
    def df(x):
        return 2*x
    return find_zero(f, df)

def approx_eq(x, y, tol = 1e-3):
    return abs(x - y) < tol

def find_zero(f, df):
    def newton_update(x):
        return x - f(x)/df(x)
    def close_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update, close_zero)





