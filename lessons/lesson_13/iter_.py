
list_1 = [1, 2, 3]

#
# for item in list_1:
#     print(item)


iter_1 = iter(list_1)
# for item in iter_1:
#     print(item)

value = next(iter_1)
value += 5
print(value)
print(next(iter_1))
print(next(iter_1))
list_2 = [[1], [2], [3]]

iter_2 = iter(list_2)

value_list_1 = next(iter_2)
value_list_1.append(4)


print(list_2)