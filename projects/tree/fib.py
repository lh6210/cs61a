
import tree_mod as tr


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
        return tr.tree(n)
    else:
        left_subT = fib_tree(n - 2)
        right_subT = fib_tree(n - 1)
        rt_label = tr.label(left_subT) + tr.label(right_subT)
        return tr.tree(rt_label, [left_subT, right_subT])


def print_fib_tree(t):
    assert tr.is_tree(t), "t must be a tree"
    return tr.print_tree(t)
