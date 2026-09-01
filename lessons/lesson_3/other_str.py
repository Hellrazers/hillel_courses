#strat_swit
FIRST_CONSTANT = ' Oleksii'

hello_word = "Hello World"
print(hello_word)

print(hello_word.startswith('1Hello'))
print(hello_word.endswith('World'))

if hello_word.startswith('Hello'):
    hello_word += FIRST_CONSTANT

print(hello_word)
#find
hello_word = "Hello World"
print(hello_word.find('o'))
print(hello_word[hello_word.find('o')])
print(hello_word.find('o', hello_word.find('o') + 1))
print(hello_word[7])
print(hello_word.find('H'))
print(hello_word.find('!'))
if hello_word.find("!") == -1:
    print('Нема цього елемента')
#strip
hello_word = "     Hello World      "
print(hello_word)
print(hello_word.lstrip())
print(hello_word.rstrip())
print(hello_word.strip())
hello_word = "!Hello World"
print(hello_word)
print(hello_word.strip('!'))
