import numpy as np


def arithmetic_mean(a: list) -> int:
    res = sum(a) // len(a)
    return res

print(arithmetic_mean([2, 4, 6]))


def geometric_mean(a: list) -> int:
    n = np.prod(np.array(a))
    if n < 0:
        n = abs(n)
        res = n ** (1 / len(a)) * -1
    else:
        res = n ** (1 / len(a))
    return round(res)

print(geometric_mean([2, 4, 8]))