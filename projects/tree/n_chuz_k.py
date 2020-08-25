
import tree_mod as tr

def cnt_n_choose_k(n, k):
    assert n >= k, "n must be greater than or equal to k"
    if n == k or k == 0:
        return 1
    if k == 1:
        return n
    else:
        return cnt_n_choose_k(n - 1, k - 1) + cnt_n_choose_k(n - 1, k)


def tree_n_choose_k(lst, k):
    #assert len(lst) >= k, "length of the list must be greater than or equal to k"

    if k == 0: 
        return tr.tree(True)
    if k == 1 and len(lst) == 1:
        return tr.tree(str(tr.label(lst)), [tr.tree(True), tr.tree(False)])
    if len(lst) < k:
        return tr.tree(False)
    else:
        m = str(lst[0])
        left, right = tree_n_choose_k(lst[1:], k - 1), tree_n_choose_k(lst[1:], k)
        return tr.tree(m, [left, right])


def print_n_chuz_k(symb, t):
    """
    >>> tp = tree_n_choose_k(['a', 'b', 'c', 'd'], 3)
    >>> print_n_chuz_k(' ~ ', tp)
    a ~ b ~ c
    a ~ b ~ d
    a ~ c ~ d
    b ~ c ~ d
    >>> t = ['a', 'b', 'c', 'd', 'e']
    >>> tp = tree_n_choose_k(t, 3)
    >>> print_n_chuz_k(' # ', tp)
    a # b # c
    a # b # d
    a # b # e
    a # c # d
    a # c # e
    a # d # e
    b # c # d
    b # c # e
    b # d # e
    c # d # e
    >>> t = ['a', 'b', 'c', 'd', 'e', 'f']
    >>> tp = tree_n_choose_k(t, 4)
    >>> print_n_chuz_k(' / ', tp)
    a / b / c / d
    a / b / c / e
    a / b / c / f
    a / b / d / e
    a / b / d / f
    a / b / e / f
    a / c / d / e
    a / c / d / f
    a / c / e / f
    a / d / e / f
    b / c / d / e
    b / c / d / f
    b / c / e / f
    b / d / e / f
    c / d / e / f
    """

    assert tr.is_tree(t), "t must be a tree"
    return tr.sym_print_tree(symb)(t)
