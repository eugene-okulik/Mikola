def decorator(calc):
    def inner(*args):
        num_1, num_2, operator = (args)
        if num_1 < 0 or num_2 < 0:
            return calc(num_1, num_2, '*')
        elif num_1 > num_2:
            return calc(num_1, num_2, '-')
        elif num_2 > num_1:
            return calc(num_2, num_1, '//')
        elif num_1 == num_2:
            return calc(num_1, num_2, '+')

    return inner


@decorator
def calc(first: int, second: int, operator: str) -> int:
    if operator == '+':
        return first + second
    elif operator == '-':
        return first - second
    elif operator == '*':
        return first * second
    elif operator == '//':
        return first // second


first_num = int(input('Enter first number: '))
second_num = int(input('Enter second number: '))
print(20 * '*')
print(f"Output: {calc(first_num, second_num, '+')}")
