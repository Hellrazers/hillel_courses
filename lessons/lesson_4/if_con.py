

true_value = False

if not true_value:
    print('True')


list_value = [1,2]
str_value = '1'

if list_value:
    print('My list')
elif 2 in list_value:
    print('2 in this list')
else:
    print('Nothing in this list')

if list_value:
    print('My list')
if 2 in list_value:
    print('2 in this list')
else:
    print('Nothing in this list')


#
# if 3 in list_value:
#     print('My list')
# else:
#     print('Nothing in this list')
# if 2 in list_value:
#     print('2 in this list')
# else:
#     print('Nothing in this list')