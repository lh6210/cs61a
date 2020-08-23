
def curry2(fn):
    def f(x):
        def g(y):
            return fn(x, y)
        return g
    return f

def curry_reverse(f):
    def fn(x, y):
        return f(x)(y)
    return fn

