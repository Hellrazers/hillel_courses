


# set_1.add()

# for item in set_1:
#     print(item)

#
# print(set_1.pop())
# # set_1.remove('hello')
# print(set_1)
set_1 = {'asd', 2342 ,32341,53453, 'hello', 'world' }
print(set_1)
print(set_1)
list_1 = ['hello', 'world', 1, 23 ]

set_1_1 = {'hello', 'world', 1, 23 }

# set_1.update(list_1)
print(set_1)

set_union =  set_1 | set_1_1
set_union_2 = set_1.union(list_1)
print(set_union_2)
set_intersection = set_1.intersection(set_1_1)
print(set_intersection)

set_difference = set_1.difference(set_1_1)
print(set_difference)
set_difference_2 = set_1_1.difference(set_1)
print(set_difference)
set_symmetric_difference = set_1.symmetric_difference(set_1_1)
print(set_symmetric_difference)