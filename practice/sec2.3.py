from operator import mul, add

def find_divisors(num):
    return [x for x in range(1, num) if num % x == 0]


def find_perfect(n):
    l1 = list(range(1, n + 1))
    return [x for x in l1 if is_perfect(x)]

def min_perimeter(area):
    """Given area, compute the minimum perimeter"""
    side_len = find_divisors(area) + [area]
    perimeter = [2*(x + area//x) for x in side_len ]
    return min(perimeter)

def reduce(fn, s, initial):
    reduced = initial
    for x in s:
	reduced = fn(x, reduced)
    return reduced


def is_perf2(n):
    l = find_divisors(n) 
    if n == reduce(add, l, 0):
	return True
    return False

def keep_if(cond_fn, s):
    return [x for x in s if cond_fn(x)]


def find_perf2(n):
    l = range(1, n+1)
    return keep_if(is_perf2, l)

def count(s, value):
    total = 0
    for elm in s:
	if elm == value:
	    total+=1
    print('by the end of the for loop, elm equals: ' + str(elm))
    return total

def tree(node, branches=[]):
    for b in branches:
	assert is_tree(b), 'branches must be trees'
    return [node] + branches

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(t):
    if type(t) != list or len(t) < 1:
	return False
    for b in branches(t):
	if not is_tree(b):
	    return False
    return True

def is_leaf(t):
    if not is_tree(t):
	return False
    return not branches(t)






