str_1 = 'hello'
str_2 = 'world'

str_3 = str_1 + str_2
print(id(str_1))
print(id(str_2))
print(id(str_3))
print(str_3)
str_1 = str_1 + ' word' # str_1 += ' word'
print(str_1)
print(id(str_1))
int_1 = 5
print(id(int_1))
int_1 += 1
print(id(int_1))

tuple_1 = (1, 2, 3)
print(id(tuple_1))

list_1 = [1, 2, 3]
print(id(list_1))
list_1.append(4)
print(id(list_1))
set_1 = {1, 2, 3}
print(id(set_1))
set_1.add(4)
print(id(set_1))
list_2 = list_1
list_2.append(5)
print(id(list_2))