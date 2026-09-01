
def my_func(value_1, value_2):
    return value_1 / value_2


try:
    value = my_func(1, 1)
    # my_func(1, '1')
    raise AssertionError

    [1,2][433]

except ZeroDivisionError:
    print('Помилка при діленні на 0')
except TypeError as e:
    print(my_func(1, int('1')))
except Exception as e:
    print(e)
else:
    print('Я впав без помилки')
finally:
    print('Я БУДУ ВИКОНОВАТИСЬ ЗАВЖДИ')




print(my_func(1, 2))