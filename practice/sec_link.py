
empty = 'empty'

def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair 
    
    >>> is_link(link(0))
    True

    >>> four = link(0, link(1, link(2, link(3, empty))))
    >>> is_link(four) 
    True
    """
    if type(s) != list or len(s) !=2:
        return False
    elif s[1] == empty:
        return True
    else:
        return is_link(s[1])

def link(first, rest=empty):
    """ linked list constructor
    
    >>> link(3)
    [3, 'empty']
    >>> three = link(0, link(1, link(2, link(3))))
    >>> three
    [0, [1, [2, [3, 'empty']]]]
    >>> is_link(three)
    True
    """
    assert rest == empty or is_link(rest), "rest must be empty or a linked list"
    return [first, rest]

def first(s):
    """ selector """
    assert is_link(s), "argument must be a linked list"
    return s[0]

def rest(s):
    """ selector """
    assert is_link(s), " argument must be a linked list"
    return s[1]


def len_link(s):
    """ the length of linked list s

    >>> three = link(0, link(1, link(2, link(3))))
    >>> len_link(three)
    4
    """
    if rest(s) == empty:
        return 1
    else:
        return 1 + len_link(rest(s))

def getitem_link(s, i):
    """
    
    >>> three = link(0, link(1, link(2, link(3))))
    >>> getitem_link(three, 2)
    2
    >>> getitem_link(three, 1)
    1
    """

    assert is_link(s), "argument must be a linked list"
    if i == 0:
        return first(s)
    else:
        return getitem_link(rest(s), i - 1)


def extend_link(s, t):
    """
    
    >>> l1 = link(2, link(1))
    >>> l2 = link(3, link(4, link(5)))
    >>> extend_link(l1, l2)
    [2, [1, [3, [4, [5, 'empty']]]]]
    >>> four = link(1, link(2, link(3, link(4))))
    >>> extend_link(four, four)
    [1, [2, [3, [4, [1, [2, [3, [4, 'empty']]]]]]]]
    >>> extend_link(l1, four)
    [2, [1, [1, [2, [3, [4, 'empty']]]]]]
    """
    assert is_link(s) and is_link(t), "s and t must be linked lists"
    if rest(s) == empty:
        return link(first(s), t)
    else:
        return link(first(s), extend_link(rest(s), t))
    

def apply_to_all(f, s):
    """f is a function with a number as its argument
    >>> s = link(1, link(2, link(3)))
    >>> apply_to_all(lambda x: x + 3, s)
    [4, [5, [6, 'empty']]]
    >>> apply_to_all(lambda x: x * 2, s)
    [2, [4, [6, 'empty']]]
    >>> apply_to_all(lambda x: x * x, s)
    [1, [4, [9, 'empty']]]
    """

    assert is_link(s), "s must be a link"
    if rest(s) == empty:
        return link(f(first(s)))
    else:
        return link(f(first(s)), apply_to_all(f, rest(s)))


def keep_if_link(f, s):
    """ the output could be 'empty', which is not a linked list anymore.
    That happens when s is a single-node linked list and f(first(s)) is false
    >>> four = link(1, link(2, link(3, link(4, empty))))
    >>> keep_if_link(lambda x: x%2 == 0, four)
    [2, [4, 'empty']]
    >>> nine = link(3, link(6, link(9)))
    >>> keep_if_link(lambda x: x % 3 != 0, nine)
    'empty'
    >>> nine = link(4, link(5, link(9)))
    >>> keep_if_link(lambda x: x % 3 != 0, nine)
    [4, [5, 'empty']]

    """

    assert is_link(s), "s must be a link"
    if rest(s) == empty:
        if f(first(s)) == True:
            return s
        else:
            return empty
    else:
        if f(first(s)) == True:
            return link(first(s), keep_if_link(f, rest(s)))
        else:
            return keep_if_link(f, rest(s))



def join_link(s, separator):
    """Return a string of all elements in s separated by separator.
    >>> four = link(1, link(2, link(3, link(4))))
    >>> join_link(four, ", ")
    '1, 2, 3, 4'
    >>> join_link(four, " + ") 
    '1 + 2 + 3 + 4'
    """

    if rest(s) == empty:
        return str(first(s))
    else:
        return(str(first(s)) + separator +  join_link(rest(s), separator))












    




