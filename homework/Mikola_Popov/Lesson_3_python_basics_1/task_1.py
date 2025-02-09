def plus(a: int, b: int) -> int:
    res_1 = a + b
    return res_1

print(plus(4, 5))


def minus(a: int, b: int) -> int:
    if a > b:
        res_2 = a - b
    elif a < b:
        res_2 = b - a
    return res_2

print(minus(6, 10))


def mult(a: int, b:int) -> int:
    res_3 = a * b
    return res_3

print(mult(5, 7))