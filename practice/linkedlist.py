

empty = 'empty'

def link(first, rest=empty):
    assert is_link(rest), 'rest must be a list'
    return [first, rest]

def is_link(s):
    return s == empty or (type(s) == list and len(s) == 2 and is_link(s[1]))

def first(s):
    assert is_link(s), 'first only applies to linked list'
    return s[0]

def rest(s):
    assert is_link(s), 'rest only applies to linked list'
    assert s != empty, 'rest only applies to linked list with more than one node'
    return s[1]

def len_link(s):
    if rest(s) == empty:
        return 1
    return 1 + len_link(rest(s))

def getitem_link(s, i):
    assert i <= len_link(s) - 1, 'the index is out of range'
    if i == 0:
        return first(s)
    return getitem_link(rest(s), i - 1)

def join_link(s, separator):
    """return linked list s as a readable string;
    s is not mutated."""
    if rest(s) ==  empty:
        return str(first(s))
    else:
        return str(first(s)) + separator + join_link(rest(s), separator)

def extend_link(s, t):
    """Return a list with the elements of s followed by those of t;
    s and t are not modified."""
    assert is_link(t), 't must be linked list'
    if s == empty:
        return t
    else:
        return link(first(s), extend_link(rest(s), t))

def insert_link(s, i, value):
    """linked list s is mutated"""
    if i == 0:
        return link(value, s) 
    assert i <= len_link(s) - 1, 'index is out of range'
    return link(first(s), insert_link(rest(s), i - 1, value))

def mutable_link():
    """Return a functional implementation of a mutable linked list."""
    contents = empty
    def dispatch(message, *args):
        nonlocal contents
        if message == 'len':
            # read-only 
            return len_link(contents)
        elif message == 'getitem':
            # read only
            return getitem_link(contents, index)
        elif message == 'push_first':
            # modify the linked list
            contents = insert_link(contents, 0, *args)
            return contents
        elif message == 'pop_first':
            # modify the linked list
            result = first(contents)
            contents = rest(contents)
            return result 
        elif message == 'str':
            # read-only
            return join_link(contents, ", ")
        elif message == 'insert':
            contents = insert_link(contents, *args)
        elif message == 'extend':
            contents = extend_link(contents, *args)
    return dispatch

a = mutable_link()
a('push_first', 1)
a('push_first', 2)
a('push_first', 3)
a('push_first', 4)

b = mutable_link()
b('push_first', 'one')
b('push_first', 'two')
b('push_first', 'three')

def to_mutable_link(source):
    """Return a functional linked list with the same contents as source."""
    s = mutable_link()
    for element in reversed(source):
        s('push_first', element)
    return s

four = link(1, link(2, link(3, link(4))))
suite = ['heart', 'diamond', 'spade', 'club']
"""
s = to_mutable_link(suite)
s2 = to_mutable_link(suite)
s3 = to_mutable_link(suite)
"""


def dictionary():
    """Return a functional implementation of a dictionary"""
    records = []
    def getitem(key):
        for elm in records:
            if elm[0] == key:
                return elm[1]
        return 'Not found'
    
    def setitem(key, value):
        nonlocal records
        non_match = [elm for elm in records if elm[0] != key]
        records = non_match + [[key, value]]

    def dispatch(message, key=None, value=None):
        if message == 'getitem':
            return getitem(key)
        elif message == 'setitem':
            setitem(key, value)
    return dispatch

def account(initial_balance):
    def deposit(amount):
        dispatch['balance'] += amount
        return dispatch['balance']
    def withdraw(amount):
        if amount > dispatch['balance']:
            return 'Insufficient funds'
        dispatch['balance'] -= amount
        return dispatch['balance']
    dispatch = {'deposit': deposit,
                'withdraw': withdraw,
                'balance': initial_balance}
    return dispatch

def withdraw(accountInstance, amount):
    return accountInstance['withdraw'](amount)

def deposit(accountInstance, amount):
    return accountInstance['deposit'](amount)

def check_balance(accountInstance):
    return accountInstance['balance']











d = dictionary()
d('setitem', 'color', 'black')
d('setitem', 'weather', 'shiny')
d('setitem', 'wind', 'tiny')





