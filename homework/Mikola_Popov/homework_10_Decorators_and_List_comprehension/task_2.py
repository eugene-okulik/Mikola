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


example('prent me')
