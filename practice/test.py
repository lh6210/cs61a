
def delay(arg):
    print('delayed')
    def g():
        return arg
    return g

delay(delay)()(6)()


def pirate(arggg):
    print('matey')
    def plunder(arggg):
        return arggg
    return plunder

from operator import add, mul

def square(x):
    return mul(x, x)


def horse(mask):
    horse = mask
    def mask(horse):
        return horse
    return horse(mask)

mask = lambda horse: horse(2)

horse(mask)

