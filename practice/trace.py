
def trace1(fn):
    def wrapped(x):
        print('->', fn, '(', x, ')')
        return fn(x)
    return wrapped


@trace1 
def triple(x):
    return 3*x

def trace2(fn):
    def wrapped(x, y):
        print('->', fn)
        return fn(x, y)
    return wrapped



@trace2
def sum(a, b):
    return a + b


