dict_1 = {'name': 'Василь', 'age': 25, 'city': 'Київ', 'is_male': True, 'has_children': None, (1,2):1, 1:1, True:True}

print(dict_1['city'])

print(dict_1.get('city1', 'Цього значення в дікт нема'))


if dict_1.get('city1') is None:
    print('Цього значення в дікт нема')
# {"asd":1, "value": true, null}


if dict_1.get('age') > 18:
    print('Він вже повнолітній')


dict_1['age1'] = 15
print(dict_1.get('age1'))
print(dict_1)

dict_2 = {'name_1': 'Василь', 'age_1': [1, 2, 3]}

dict_1.update(dict_2)
print(dict_1)
print(dict_1.get('age_1')[-1])
list_1 = [
    {'name': 'Василь', 'age': 25, 'city': 'Київ', 'is_male': True, 'has_children': None, (1, 2): 1, 1: 1, True: True},
    {'name': 'Василь', 'age': 25, 'city': 'Київ', 'is_male': True, 'has_children': None, (1, 2): 1, 1: 1, True: True},
    {'name': 'Василь', 'age': 25, 'city': 'Київ', 'is_male': True, 'has_children': None, (1, 2): 1, 1: 1, True: True},
    {'name': 'Василь', 'age': 25, 'city': 'Київ', 'is_male': True, 'has_children': None, (1, 2): 1, 1: True,
     'age1': 15, 'name_1': 'Василь', 'age_1': [1, 2, 3]},
    {'name': 'Василь', 'age': 25, 'city': 'Київ', 'is_male': True, 'has_children': None, (1, 2): 1, 1: True, 'age1': 15}

    ]

print(list_1[-2].get('age_1')[1])

print(dict_2)
dict_2['age_1'].append('Hello')
dict_2.pop('age_1')
print(dict_2)
print(dict_1)
