


def improve(update, close, guess = 1):
    while not close(guess):
        guess = update(guess)
    return guess

def find_root(n, a):
    """ find nth root of function pow(x, n) = a

    >>> approx_eq(find_root(2, 64), 8.0)
    True
    >>> approx_eq(find_root(3, 64), 4.0)
    True
    >>> approx_eq(find_root(6, 64), 2.0)
    True
    """
    def f(x):
        return pow(x, n) - a
    def df(x):
        return n * pow(x, n-1)
    def newton_update(x):
        return x - f(x)/df(x)
    def near_zero(x):
        return approx_eq(f(x), 0)
    return improve(newton_update, near_zero)




def approx_eq(x, y, tol = 1e-3):
    return abs(x-y) < tol





