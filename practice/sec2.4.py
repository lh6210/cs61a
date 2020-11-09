

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

    @fullname.deleter
    #usage: del person.fullname"""
    def fullname(self):
        self.first ='' 
        self.last = ''
        
    @property
    def email(self):
            return '{}.{}@email.com'.format(self.first, self.last)


numerals = {'I':1, 'J':2, 'K':3, 'L':4, 'M':5}

# section 2.4.11
def mutable_link():
    """Return a functional implementation of a mutable linked list."""
    contents = [] 
    def dispatch(message, value=None):
        nonlocal contents;
        if message == 'len':
            return len_link(contents)
        elif message == 'getitem':
            return getitem_link(contents, value)
        elif message == 'push_first':
            contents = link(value, contents)
        elif message == 'pop_first':
            f = first(contents)
            contents = rest(contents)
            return f
        elif message == 'str':
            return join_link(contents, ", ")
    return dispatch

def to_mutable_link(source):
    """Return a functional list with the same contents as source."""
    s = mutable_link();
    for element in reversed(source):
        s('push_first', element)
    return s


















