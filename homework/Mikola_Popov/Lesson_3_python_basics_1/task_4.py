def rectangular_triangle(a: int, b: int) -> int | float:
    hipotenuse = (a ** 2 + b ** 2) ** 0.5
    return hipotenuse


print(rectangular_triangle(8, 15))


def area_rectangle(a: int, b: int) -> int | float:
    S = (a * b) / 2
    return S


print(area_rectangle(8, 15))
