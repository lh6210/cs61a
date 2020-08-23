
empty = 'empty'

def is_link(s):
    """s is a linked list if it is empty or a (first, rest) pair 
    
    >>> is_link(link(0))
    True

    >>> four = link(0, link(1, link(2, link(3, empty))))
    >>> is_link(four) 
    True
    """
    if type(s) != list:
        return False
    if len(s) != 2:
        return False
    if s[1] == empty:
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
    """
    #assert is_link(s) and is_link(t), "s and t must be linked lists"
    if rest(s) == empty:
        s[1] = t
        return s
    else:
        return link(first(s), extend_link(rest(s), t))
    







