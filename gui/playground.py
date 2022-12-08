def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


# print(add(3, 4, 3, 10, 70, 16))


def calculate(**kwargs):
    print(kwargs)


calculate(add=3, multiply=5)