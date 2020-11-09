

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
    assert len(s) == 2, 'rest only applies to linked list with more than one node'
    return s[1]

def len_link(s):
    assert is_link(s), 'the argument must be a linked list'
    if rest(s) == empty:
        return 1
    return 1 + len_link(rest(s))

def getitem_link(s, i):
    assert i <= len_link(s) - 1, 'the index is out of range'
    assert is_link(s), 'the first argument must be a linked list'
    if i == 0:
        return first(s)
    return getitem_link(rest(s), i - 1)

def join_link(s, delimiter):
    if rest(s) ==  empty:
        return str(first(s))
    return str(first(s)) + delimiter + join_link(rest(s), delimiter)

def extend_link(s, t):
    """Return a list with the elements of s followed by those of t"""
    assert is_link(s) and is_link(t), 's and t must be linked list'
    if s == empty:
        return t
    else:
        return link(first(s), extend(rest(s), t))

def insert_link(s, i, value):
    assert i <= len_link(s) - 1, 'index is out of range'
    if i == 0:
        return link(value, s) 
    else:
        u = s
        for _ in range(i-1):
            u = rest(u) # go i - 1 times
        v = link(value, rest(u))
        u[1] = v
        return s 


            

    

def mutable_link():
    """Return a functional implementation of a mutable linked list."""
    contents = empty
    def dispatch(message, value=None):
        nonlocal contents
        if message == 'len':
            # read-only 
            return len_link(contents)
        elif message == 'getitem':
            # read only
            return getitem_link(contents, value)
        elif message == 'push_first':
            # modify the linked list
            contents = link(value, contents)
        elif message == 'pop_first':
            # modify the linked list
            result = first(contents)
            contents = rest(contents)
            return result 
        elif message == 'str':
            # read-only
            return join_link(contents, ", ")
    return dispatch

def to_mutable_link(source):
    """Return a functional linked list with the same contents as source."""
    s = mutable_link()
    for element in reversed(source):
        s('push_first', element)
    return s

four = link(1, link(2, link(3, link(4))))
suite = ['heart', 'diamond', 'spade', 'club']

s = to_mutable_link(suite)
s2 = to_mutable_link(suite)
s3 = to_mutable_link(suite)



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





