import random


def generator_function(limit=100):
    n = 2
    num = 1
    count = 0
    while count < limit:
        yield num
        num += n
        count += 1


# print(list(generator_function(10)))
count = 1
for number in generator_function(1000000):
    if count == 1000000:
        print(number)
        break
    count += 1


def discount(salary: int, bonus=(False, True)) -> str:
    bonus = random.choice(bonus)
    percent = random.randint(10, 50)
    if bonus:
        return f"{salary}, {bonus} - $'{(salary // 100) * percent + salary}'"
    else:
        return f"{salary}, {bonus}, $'{salary}'"


salary = int(input('Enter your number: '))
print(discount(salary))
