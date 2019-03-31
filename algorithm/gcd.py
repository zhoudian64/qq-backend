def gcd(a, b):
    """
    欧几里得 最大公约数
    Greatest Common Divisor
    """
    return a if b == 0 else gcd(a, b)


def ext_gcd(a, b):
    """
    Extend Greatest Common Divisor
    """
    if a == 0:
        return b, 0, 1
    else:
        g, x, y = ext_gcd(b % a, a)
        return g, y - (b // a) * x, x
