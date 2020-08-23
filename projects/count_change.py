# HW3 Q3: Count change
# Once the machines take over, the denomination of every coin will be a power of two: 1-cent, 2-cent, 4-cent, 8-cent, 16-cent, etc. There will be no limit to how much a coin can be worth.
#
# Given a positive integer amount, a set of coins makes change for amount if the sum of the values of the coins is amount. For example, the following sets make change for 7:
#
# 7 1-cent coins
# 5 1-cent, 1 2-cent coins
# 3 1-cent, 2 2-cent coins
# 3 1-cent, 1 4-cent coins
# 1 1-cent, 3 2-cent coins
# 1 1-cent, 1 2-cent, 1 4-cent coins
# Thus, there are 6 ways to make change for 7. Write a recursive function count_change that takes a positive integer amount and returns the number of ways to make change for amount using these coins of the future.

# I want to not only compute the number of different combinations, but also show what those combinations are.
# I am going to use binary tree to make this happen.


from math import log, floor

def tree(label, branches=[]):
    assert all([is_tree(b) for b in branches]), "branches must be trees"
    return [label] +  branches

def is_tree(t):
    if type(t) != list or len(t) < 1:
        return False
    return all([is_tree(b) for b in t[1:]]) 

def branches(t):
    assert is_tree(t), "t must be a tree"
    return t[1:]

def label(t):
    assert is_tree(t), "t must be a tree"
    return t[0]

def is_leaf(t):
    assert is_tree(t), "t must be a tree"
    if len(t) == 1:
        return True
    return False

def change_partition(amount):
    """By assumption, we know we have change coins 1-cent, 2-cents, 4-cents, and so on. This function will build a binary tree for all possible combinations of the change coins. The leaves of this tree could be 'True' or 'False'.
    """

    def part_tree(n, m):
        if n == 0:
            return tree(True)
        if n < 0 or m == 0:
            return tree(False)
        else:
            left = part_tree(n - m, m)
            right = part_tree(n, m // 2)
            return tree(m, [left, right])


    k = floor(log(amount) / log(2))
    l = pow(2, k)
    return part_tree(amount, l)


def print_partition(t, par=[]):
    """print the partition tree
    >>> t = change_partition(7)
    >>> print_partition(t)
    1 + 2 + 4
    1 + 1 + 1 + 4
    1 + 2 + 2 + 2
    1 + 1 + 1 + 2 + 2
    1 + 1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 1 + 1 + 1 + 1
    """

    if is_leaf(t):
        if label(t) == True:
            print(' + '.join(par))
    else:
        left, right = branches(t)[0], branches(t)[1]
        print_partition(left, [str(label(t))] + par)
        print_partition(right, par)
        #print("total partitions: ", str(count_leaves(t)))


def print_total(t):
    """print total number of combinations
    >>> t = change_partition(7)
    >>> print_total(t)
    6
    """

    def count_leaves(t):
        if is_leaf(t):
            if label(t) == True:
                return 1
            return 0
        else:
            return count_leaves(branches(t)[0]) + count_leaves(branches(t)[1])
    print("total partitions: ", str(count_leaves(t)))
    


def print_tree(t):
    print_partition(t)
    print_total(t)















