"""
Montgomery for (base ^ exponent) mod n
"""


def exp_mode(base, exponent, n):
    bin_exponent = bin(exponent)[2:][::-1]
    bit = len(bin_exponent)
    base_array = [base]
    for _ in range(bit - 1):
        next_base = (base * base) % n
        base_array.append(next_base)
        base = next_base
    result = pi_mod(base_array, bin_exponent, n) % n
    return result


def pi_mod(base_array, bin_exponent, n):
    result = 1
    for i in range(len(base_array)):
        if not int(bin_exponent[i]):
            continue
        #     位零时直接不乘加速
        base = base_array[i]
        result = (result * base)
    return result
