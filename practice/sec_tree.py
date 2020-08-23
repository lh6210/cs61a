
def tree(root_label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [root_label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]


def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
#    for branch in branches(tree):
#        if not is_tree(branch):
#            return False
    return all([is_tree(b) for b in branches(tree)])
#    return True

def is_leaf(tree):
    if not is_tree(tree):
        return False
    return not branches(tree)


def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

#def fib_tree(n):
#    if n == 1: 
#        return tree(1)
#    elif n == 2:
#        return tree(1)
#    else:
#        rt_label = fib(n)
#        return tree(rt_label, [fib_tree(n - 2), fib_tree(n - 1)])
#


def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    else:
        left_subT = fib_tree(n - 2)
        right_subT = fib_tree(n - 1)
        rt_label = label(left_subT) + label(right_subT)
        return tree(rt_label, [left_subT, right_subT])


def count_leaves(tree):
    if is_leaf(tree):   # base case
        return 1
    else:
        total = 0
        for b in branches(tree):
            total += count_leaves(b)
        return total 


#def partition_tree(n, m):
#    """Return a partition tree of n using parts of up to m."""
#    if n == 0:
#        return tree(True)
#    elif n < 0 or m == 0:
#        return tree(False)
#    else:
#        left = partition_tree(n-m, m)
#        right = partition_tree(n, m-1)
#        return tree(m, [left, right])
#
#
#def print_parts(tree, partition=[]):
#    if is_leaf(tree):
#        if label(tree):
#            print(' + '.join(partition))
#    else:
#        left, right = branches(tree)
#        m = str(label(tree))
#        print_parts(left, partition + [m])
#        print_parts(right, partition)
#
def decorate(fn):
    def fn(x):
        print(fn, '->', x)
        return fn(x)
    return fn



def leaves(tree):
    if is_leaf(tree):
        return [label(tree)]
    else:
        lf = [leaves(b) for b in branches(tree)]
        return  sum(lf, [])

#def increment_leaves(t):
#    if is_leaf(t):
#        label(t) = label(t) + 1
#    else:
#        for b in branches(t):
#            increment_leaves(b)
#        return t
#

def right_binarize(t):  # argument is a tree
    """ Construct a right-branching binary tree. 
    >>> s1 = tree(3, [tree(1), tree(2, [tree(4)])])
    >>> right_binarize(s1)
    [3, [1], [2, [4]]]
    >>> s2 = tree(0, [tree(1), tree(2), tree(3)])
    >>> right_binarize(s2)
    [0, [1], [[2], [3]]]
    >>> right_binarize(tree(0, [tree(x) for x in range(1, 8)]))
    [0, [1], [[2], [[3], [[4], [[5], [[6], [7]]]]]]]
    """

    return tree(label(t), binarize_branches(branches(t)))

def binarize_branches(bs):  # argument is a list of branches
    """ Binarize a list of branches. """
    if len(bs) > 2:
        first, rest = bs[0], bs[1:]
        return [first, binarize_branches(rest)]
    else:  # len(bs) = 2 or len(bs) = 1
        return [right_binarize(b) for b in bs]  # every b is a tree


def right_binarize2(t):
    """

    argument t is a tree
    >>> three = tree(3, [tree(2), tree(1)])
    >>> right_binarize2(three)
    [3, [2], [1]]
    >>> four = tree(4, [tree(3), tree(2), tree(1), tree(0)])
    >>> right_binarize2(four)
    [4, [3], [[2], [[1], [0]]]]
    """
    m = label(t)
    b_list = branches(t)

    #if current level of branches is ok, go down to nest level
    if is_leaf(t):
        return t
    if len(branches(t)) <= 2:   
        return tree(m, [right_binarize2(b) for b in b_list])
    else:
        first, rest = b_list[0], b_list[1:]
        left = first
        right = tree(rest[0], [rest[1:]])
        return tree(m, [left, right_binarize2(right)])




def right_binarize3(t):
    """
    this function makes a tree a binary tree;
    in another word, conbine branches if necessary
    argument t is a tree
    check condition is whether the number of branches is greater than 2 or not

    >>> three = tree(3, [tree(2), tree(1)])
    >>> right_binarize3(three)
    [3, [2], [1]]
    >>> four = tree(4, [tree(3), tree(2), tree(1), tree(0)])
    >>> right_binarize3(four)
    [4, [3], [2, [1], [0]]]
    >>> five = tree(5, [tree(4), tree(3), tree(2), tree(1), tree(0)])
    >>> right_binarize3(five)
    [5, [4], [3, [2], [1, [0]]]]
    >>> seven = tree(7, [tree(6), tree(5, [tree(1), tree(2), tree(3)])])
    >>> right_binarize3(seven)
    [7, [6], [5, [1], [2, [3]]]]
    >>> seven2 = tree(7, [tree(6), tree(5, [tree(1), tree(2), tree(3), tree(4)])])
    >>> right_binarize3(seven2)
    [7, [6], [5, [1], [2, [3], [4]]]]
    >>> nine = tree(9, [tree(4, [tree(1), tree(2), tree(3)]), tree(8, [tree(5), tree(6), tree(7)])])
    >>> right_binarize3(nine)
    [9, [4, [1], [2, [3]]], [8, [5], [6, [7]]]]
    >>> seven3 = tree(7, [tree(6), tree(1), tree(2, [tree(3), tree(4), tree(5)])])
    >>> right_binarize3(seven3)
    [7, [6], [1, [2, [3], [4, [5]]]]]
    >>> eight = tree(8, [tree(0), tree(1), tree(2, [tree(5), tree(6), tree(7)]), tree(3), tree(4)])
    >>> right_binarize3(eight)
    [8, [0], [1, [2, [5], [6, [7]]], [3, [4]]]]
    >>> eight2 = tree(8, [tree(0), tree(1, [tree(2), tree(3)]), tree(4, [tree(5), tree(6)])])
    >>> right_binarize3(eight2)
    [8, [0], [1, [2], [3, [4, [5], [6]]]]]
    """
    m = label(t)
    bl = branches(t)
    if is_leaf(t):
        return t
    if len(bl) <= 2:
        # if the current level of branches is ok
        # do recursive check for these branches 
        return tree(m, [right_binarize3(b) for b in bl]) 
    else:
        # combine the branches, when number of branches > 2
        br1, br2, rest = bl[0], bl[1], bl[2:]
        br2_blist = branches(br2) + rest
        combined_br = tree(label(br2), br2_blist)  # rest should be a tree
        # binarize3 makes a bunch of branches into a binary tree
        return tree(m, [right_binarize3(br1), right_binarize3(combined_br)]) # output is a binary tree 
 
def leaves2(t):
     """
 
     >>> five = fib_tree(5)
     >>> leaves2(five)
     [1, 0, 1, 0, 1, 1, 0, 1]
     """
     if is_leaf(t):
         return t
     else:
         s = [leaves(b) for b in branches(t)]
         return sum(s, []) 
 
def increment_leaves(t):
    
    """
 
    >>> five = fib_tree(5)
    >>> six = increment_leaves(five)
    >>> six
    [5, [2, [2], [1, [1], [2]]], [3, [1, [1], [2]], [2, [2], [1, [1], [2]]]]]
    >>> leaves(six)
    [2, 1, 2, 1, 2, 2, 1, 2]
    """
    if is_leaf(t):
        t = tree(label(t) + 1)
        return t
    else:
        return tree(label(t), [increment_leaves(b) for b in branches(t)])

def increment(t):
    """

    >>> two = tree(0, [tree(1), tree(2)])
    >>> three = increment(two)
    >>> three
    [1, [2], [3]]
    >>> four = fib_tree(4)
    >>> four_inc = increment(four)
    >>> four_inc
    [4, [2, [1], [2]], [3, [2], [2, [1], [2]]]]
    """
    if is_leaf(t):
        return tree(label(t)+1)
    else:  # increment label of the tree, and then increment the branches
        return tree(label(t) + 1, [increment(b) for b in branches(t)])


def print_tree(t, indent=0):
    print(' '*indent  + str(label(t)))
    indent += 2
    for b in branches(t):
        print_tree(b, indent)


def partition(n, m):
    if n == 0:
        return tree(True)
    if m == 0:
        return tree(False)
    if n < 0:
        return tree(False)
    left, right = partition(n - m, m), partition(n, m - 1)
    return tree(m, [left, right])

def print_parts(tree, part=[]):
    if is_leaf(tree):
        if label(tree):
            print(' + '.join(part))
    else:
        m = str(label(tree))
        left, right = branches(tree)[0], branches(tree)[1]
        print_parts(left, part + [m])
        print_parts(right, part)




