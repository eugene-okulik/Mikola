def repeat_me(count):
    def dec(func):
        def wrapper(*args):
            for _ in range(count):
                print(func(*args))
        return wrapper
    return dec


@repeat_me(count=2)
def example(text):
    return text


example("prent me")


# У меня получилось только вот так реализовать, через костыли!!!
# Даже и не знаю как иначе сделать.
def repeat_me_2(func):
    def wrapper(*args, count=0):
        for _ in range(0, count):
            print(func(*args, count))

    return wrapper


@repeat_me_2
def example(text, count):
    return text


example("prent me", count=2)
