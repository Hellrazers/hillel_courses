

def new_func():
    return 42


def new_func2(argument):
    argument = argument + 1
    yield argument
    yield argument // 2
    yield 2
    yield 3


value = new_func2(54)
value_int = next(value)
value_2 = value_int + 32
print(value_2)

value_int = next(value)
value_2 = value_int +value_2
print(value_2)
print(next(value))
print(next(value))
