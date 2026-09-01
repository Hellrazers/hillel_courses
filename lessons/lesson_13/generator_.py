
def say_hello():
    return "Hello World"

def generator():
    yield "Hello World"
    yield "Hello World2"
    yield "Hello World3"
    yield "Hello World4"

print(say_hello())

generator_call = generator()
# print(next(generator_call))
# print(next(generator_call))
# print(next(generator_call))


for gen in generator_call:
    print(gen)

