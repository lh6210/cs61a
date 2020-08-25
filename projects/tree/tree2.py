

def right_binarize(tree):
    m = label(tree)
    b_list = branches(tree)

    #if current level of branches is ok, go down to nest level
    if len(branches(tree)) <= 2:   
        return tree(m, [right_binarize(b) for b in b_list])
    else:
        first, rest = b_list[0], b_list[1:]
        left = first
        right = tree(rest[0], rest[1:])
        return tree(m, [left, right_binarize(right)])


