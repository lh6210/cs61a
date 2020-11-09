

def tree(node, branches=[]):
    for b in branches:
        assert is_tree(b), 'branches must be trees'
    return [node] + branches

def is_tree(t):
    if type(t) != list or len(t) < 1:
        return False
    for b in branches(t):
        if not is_tree(b):
            return False
    return True

def branches(t):
    return t[1:]

def label(t):
    return t[0]

def is_leaf(t):
    return not branches(t)

def fib_tree(n):
    if n == 0 or n == 1:
        return tree(n)
    left, right = fib_tree(n - 2), fib_tree(n - 1)
    node = label(left) + label(right)
    return tree(node, [left, right])

def count_leaves(t):
    if is_leaf(t):
        return 1
    cnt = [count_leaves(b) for b in branches(t)]
    return sum(cnt)



