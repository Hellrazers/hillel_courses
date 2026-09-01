str_1 = 'Hello World'
print(len(str_1))
print(str_1[4])


list_str = str_1.split()
print(str_1)
print(list_str)
print(type(list_str))


str_2 = 'Hello, World, I\'m okay'
list_2 = str_2.split(sep=',')
list_3 = str_2.split()
print(list_2)
print(list_3)
list_4 = str_2.split(sep=',', maxsplit=2)
print(list_4)
