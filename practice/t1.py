
def delay(arg):
    print('delayed')
    def g():
        return arg
    return g


#delay(delay)()(6)()


def fib(n):
    """

    >>> assert fib(2) == 1, 'the second fib number should be 1'
    """
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

def fib_test():
    assert fib(2) == 1, 'the second Fib number should be 1'
    assert fib(3) == 1, 'the third fib number should be 1'
    assert fib(50) == 7778742049, 'Error at the 50th Fibonacci number'

