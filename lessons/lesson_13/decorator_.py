#
def first_function():
    print('Hello')
def second_function(fn):
    fn()
    print('Word')

#
# second_function(first_function)



asd = first_function

print(second_function(asd))


def first_decorator(func):
    def wrapper(*args, **kwargs):
        print('Before call')
        value = func(*args, **kwargs)
        print('After call')
        return value
    return wrapper


@first_decorator
def say_hello():
    print('Hello, ' )


say_hello()


@first_decorator
def counter(value_1, value_2):
    sum_values = value_1 + value_2
    print(f'Sum of {value_1} and {value_2} is {sum_values}')
    return sum_values


# print(counter(value_1=4, value_2=5))