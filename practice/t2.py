from math import sqrt

def sum_naturals(n):
    """Return the sum of the first n natural numbers.

    >>> sum_naturals(10)
    55
    >>> sum_naturals(100)
    5050
    """
    return sum_wt_func(identity, n)


def sum_wt_func(f, n):
    """this is a higher-order function which takes a function and a number as arguments

    >>> sum_wt_func(cube, 100)
    25502500
    >>> sum_wt_func(identity, 100)
    5050
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + f(k), k + 1
    return total

def identity(n):
    return n

def cube(n):
    return pow(n, 3)


def improve(update, close, guess = 1):
    """ improve function takes two function arguments here

    >>> temp = improve(golden_update, square_close_to_successor)
    >>> approx_eq(temp, 1/2 + sqrt(5)/2)
    True
    """

    while not close(guess):
        guess = update(guess)
    return guess

def golden_update(guess):
    return 1/guess + 1

def approx_eq(x, y, tol = 1e-15):
    return abs(x - y) < tol

def square_close_to_successor(x):
    return approx_eq(x*x, x+1)


def make_adder(n):
    """Return a function that takes a number k and returns k + n

    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def f(k):
        return k + n
    return f

def repeat(f, x):
    while f(x) != x:
        x = f(x)
    return x

def g(y):
    return (y + 5) // 3


def remove(n, digit):
    """ remove digits the same as digit

    >>> remove(2345, 2)
    345
    >>> remove(28567908, 8)
    256790
    >>> remove(120, 0)
    12
    """
    if n // 10 == 0:
        if n == digit:
            return 0
        else:
            return n

    left, unit = n // 10, n % 10
    if unit == digit:
        return remove(left, digit)
    else:
        return unit + 10*remove(left, digit)


def remove2(n, digit):
    """ description

    >>> remove2(123, 1)
    23
    >>> remove2(24874, 4)
    287
    """
    kept, digits = 0, 0
    while n != 0:
        n, last = n // 10, n % 10
        if last != digit:
            kept += last * pow(10, digits)
            digits += 1
    return kept




if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True) 
