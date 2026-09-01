# int, float
# 1, 2,5
first_int = 5
first_float = 5.5

print(type(first_int))
print(type(first_float))

first_str: str = 'hello world'
print(type(first_str))
first_str.startswith('hello')

first_true = True
first_false = False
first_none = None

second_str = ''
second_list = []

first_list = ['hello', 'world', 1, 2.4, ('hello', 'world', 1, 2.4)]
print(type(first_list))
first_tuple = ('hello', 'world', 1, 2.4)
print(type(first_tuple))
first_set = {'hello', 'world', 1, 2.4, 1, 1, }
print(type(first_set))
first_dict = {'id': 5}
print(type(first_dict))
print(first_set)
first_str: str = 'hello world'
second_str = ("Hello world\n"
              "new row")
third_str = '''Hello word
new row
'''
"""
Hello word
"""
print(second_str)
print(third_str)