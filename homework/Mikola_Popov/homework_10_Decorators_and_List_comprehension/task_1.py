import datetime

"""Немного боловства. Я добавил время работы любой декорированной функции"""


def add_decorator(func_action):
    def inner_func(*args):
        start_time = datetime.datetime.now()
        func_action(*args)
        finish_time = datetime.datetime.now()
        t = finish_time - start_time
        print('finished')
        print(f'Time execute {t} second')

    return inner_func


@add_decorator
def func_1():
    print("text")


@add_decorator
def func_2(a):
    lst_comp = [x for x in range(0, a)]
    print("speed list comprehension")
    return lst_comp


lst_2 = [x for x in range(0, 1000)]


@add_decorator
def func_3():
    lst = list(map(lambda x: x, lst_2))
    print("speed function map")
    return lst


func_1()
print(20 * '*')
func_2(1000)
print(20 * '*')
func_3()
