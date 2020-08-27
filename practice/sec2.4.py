

def make_withdraw(balance):
    """Return a withdraw function with a starting balance."""

    def withdraw(amount):
        if amount > balance:
            return 'Insufficient funds.'
        balance = balance - amount
        return balance
    return withdraw


def double_and_print(x):
    print('***', x, '=>', 2*x, '***')
    return 2*x

s = range(3, 7)
doubled = map(double_and_print, s)



d = {'one': 1, 'two':2, 'three': 3}
d['zero'] = 0


counts = [1, 2, 3]
for item in counts:
    print(item)


items = iter(counts)
try:
    while True:
        item = next(items)
        print(item)
except StopIteration:
    pass


def evens(start, end):
    even = start + (start % 2)
    while even < end:
        yield even 
        even += 2

