


def tree(label, branches=[]):
    assert all([is_tree(b) for b in branches]), "branches must be trees"
    return [label] + branches

def branches(t):
    assert is_tree(t), "argument must be a tree"
    return t[1:]

def label(t):
    assert is_tree(t), "argument must be a tree"
    return t[0]

def is_tree(t):
    """

    is_tree function cannot use branches or label function;
    since these two functions use is_tree in assertion.
    >>> three = tree(3, [tree(2), tree(1), tree(0)])
    >>> is_tree(three)
    True
    """
    if type(t) != list or len(t) < 1:
        return False
    elif is_leaf(t):
        return True
    else:
        return all([is_tree(b) for b in t[1:]])

def is_leaf(t):
    if type(t) == list and len(t) == 1:
        return True 
    else:
        return False 

def partition_parts(n, m):
    if n == 0:
        return tree(True)
    if n < 0 or m == 0:
        return tree(False)
    else:
        left, right = partition_parts(n - m, m), partition_parts(n, m - 1)
        return tree(m, [left, right])

def print_partition(t, par=[]):
    if is_leaf(t):
        if label(t):
            print(' + '.join(par))
    else:
        m = str(label(t))
        left, right = branches(t)[0], branches(t)[1]
        print_partition(left, par + [m])
        print_partition(right, par)














