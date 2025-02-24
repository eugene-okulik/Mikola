import random


def discount(salary: int, bonus=(False, True)) -> str:
    bonus = random.choice(bonus)
    percent = random.randint(10, 50)
    if bonus:
        return f"{salary}, {bonus} - $'{(salary // 100) * percent + salary}'"
    else:
        return f"{salary}, {bonus}, $'{salary}'"


salary = int(input('Enter your number: '))
print(discount(salary))
