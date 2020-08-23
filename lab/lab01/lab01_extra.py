"""Optional questions for Lab 1"""

# While Loops

def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    pd = 1
    if k == 0:
        return 1
    while k > 0:
        pd = pd * n
        n = n - 1
        k = k - 1

    return pd


def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    def last_digit_check(n):
        last_digit = n % 10
        if last_digit == 8:
            return True
        else:
            return False

    anchor = False 
    if n // 10 == 0:    # check single digit
        return False 
    elif last_digit_check(n) == False: # if last digit is not 8   
        return double_eights(n // 10)
    else:  # last digit is 8
        n = n // 10    # check left neighboring digit, a modified n without the last digit
        anchor = last_digit_check(n)
        if anchor == False:
            return double_eights(n // 10)
        else:
            return True



