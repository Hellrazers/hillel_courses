from copy import deepcopy

list_1 = [1, 2, 3]
# print(list_1)
# list_1.append(4)
# print(list_1)
# list_1.insert(1, 'first_value')
# print(list_1)
#
# list_1.remove('first_value')
# print(list_1)
# list_1.pop()
# print(list_1)
# list_1.pop(0)
# print(list_1)
# list_2 = list(range(5))
# list_1.extend(list_2)
# print(list_1)


# str_1 = 'asd'
#
# str_2= str_1

list_2 = list_1[:]
list_4 = [2, 3, 0, 1, 2, 3, 4, [0, 1, 2, 3, 4]]
list_3 = deepcopy(list_4)
list_4[-1].append('new_Str')
print(list_4)
print(list_3)



list_1 = [1, 'value',2, 3, 1, 'value',2, 3, 1, ]
# print(list_1[::-1])


print(list_1.count('value'))
value_of_first_value = list_1.index('value')
print(list_1.index('value', value_of_first_value + 1))
