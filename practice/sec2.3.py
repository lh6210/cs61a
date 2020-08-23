from operator import mul, add

def find_divisors(num):
    return [x for x in range(1, num) if num % x == 0]


def is_perfect(n):
    l = find_divisors(n)
    if n == sum(l):
        return True
    return False

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



