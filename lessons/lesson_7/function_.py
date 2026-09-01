def func_1(list_value: list, value_for_validate: int = 0) -> list:
    '''

    :param list_value:  list onj
    :param value_for_validate: we want to validate the value 0 or 1
    :return: list_new: list of pairs obj
    '''
    list_new = []
    for item in list_value:
        if item % 2 == value_for_validate:
            list_new.append(item)
    return list_new


#
list_2 = [1, 2, 3]
#
# for item in list_2:
#     if item % 2 == 0:
#         print(item)

list_1 = [1, 2, 3]

func_1(list_1)

print(func_1(value_for_validate=1, list_value=list_1))
print(func_1(list_2, 1))

def kwargs_func(some_string, **kwargs):
    print(some_string, kwargs)


dict_ = {'id' : 5, 'name': 'Oleskii'}

kwargs_func(some_string='asdasdasd', id=5, int_value=1, list_value=[1, 2, 3])

kwargs_func(some_string='asdasdasd', **dict_)


def arg_func(some_string, *args):
    print(some_string, args)

arg_func('asdasdasd', *list_2)