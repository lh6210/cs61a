

def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n - 1)

def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n - 1)


def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n//10)
        print(n)

def game(n):
    return alice(n)

def alice(n):
    if n == 1:
        print('Alice wins.')
    else:
        return bob(n - 1)

def bob(n):
    if n == 1 or n == 2:
        print('Bob wins.')
    elif n % 2 == 0:
        return alice(n - 2)
    else:
        return alice(n - 1)

def cascade(n):
    if n // 10 == 0:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)

def inv_cascade(n):
    inc_disp(n // 10)
    print(n)
    dec_disp(n // 10)


def inc_disp(n):
    if n // 10 == 0:
        print(n)
    else:
        inc_disp(n // 10)
        print(n)

def dec_disp(n):
    if n // 10 == 0:
        print(n)
    else:
        print(n)
        dec_disp(n // 10)


def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

def grow(n):
    return f_then_g(grow, print, n// 10)






