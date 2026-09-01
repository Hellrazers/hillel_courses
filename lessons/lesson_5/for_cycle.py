# list_10 = list(range(10))
# print(list_10)
#
# # for num in list_10:
# #     if num % 2 == 0 and num != 0:
# #         print(num)
# #
# # else:
# #     print('I finish cycle FOR')
#
#
# list_1 = list(range(1, 5))
# list_2 = list(range(5,10))
#
# for number_1 in list_1:
#     if number_1 == 2:
#         continue
#
#     for number_2 in list_2:
#         if number_2 == 6:
#             continue
#         if number_2 == 8:
#             break
#         print(f'{number_1} * {number_2} = {number_1 * number_2}')
#
# else:
#     print('I finish cycle FOR')
#
#
# for index, number in enumerate(list_1[::-1]):
#     print(f'index: {index} value: {number}')
#
# str_value = 'Hello word'
# for char in str_value:
#     print(char)
#


# list_value = range(100)
# list_2  = []
# for value in list_value:
#     if value % 2 == 0:
#         list_2.append(value)
#     else:
#         list_2.append(value - 1)
#
# print(list_2)

list_value = range(100)

# list_2 = [value for value in list_value if value % 2 == 0]

#[значення_яке_будем_записувати for значення_яке_будем_записувати(кожне значення з ітерабельного об'єкта) in ітерабельний_об'єкт if якась_умова]


list_2 = [value if value % 2 == 0 else value - 1 for value in list_value ]
#[значення_яке_будем_записувати  if якась_умова else якийсь_ваш_код for значення_яке_будем_записувати(кожне значення з ітерабельного об'єкта) in ітерабельний_об'єкт]

print(list_2)