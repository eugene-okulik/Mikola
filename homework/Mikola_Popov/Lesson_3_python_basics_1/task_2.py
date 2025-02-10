def func(x: int, y: int) -> float:
    res = (x - y) / (1 + x * y)
    return res


print(func(5, 6))
