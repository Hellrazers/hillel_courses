class Animal:

    HAS_NAME = True

    def __init__(self, name:str, age:int):
        self.name = name
        if age < 18:
           raise AttributeError(f'{age} is not a valid attribute')
        else:
            self.age = age
        self.has_trail = None
        self.has_children = []

    def is_tail(self, tail: bool):
        self.has_trail = tail
        self.make_sond(self.name)

    @staticmethod
    def make_sond(some_string:str):

        print(f'i make sound {some_string}')

    def __len__(self):
        return len(self.has_children)

    def __str__(self):
        return f'I make sound {self.name} and my age is {self.age}'

    def __repr__(self):
        return f'name:{self.name} age:{self.age} has_tail:{self.has_trail}'

    def __setattr__(self, key, value):
        if key == 'age' and value < 18:
            raise AttributeError(f'{key} is not a valid attribute')
        super().__setattr__(key, value)
    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        pass


animal = Animal(name='DOG', age=18)
with Animal('CAT', 546) as with_animal:
    print(with_animal)

# with open()
print(len(animal))
animal.has_children.append('cat')
print(len(animal))
print(len(animal.has_children))

# animal2 = Animal(name='CAT', age=20)
# print(animal.name)
# print(animal.age)
# print(animal.has_trail)
# animal.age = 15
# # animal.has_trail = True
# animal.is_tail(tail=True)
#
# print(animal.has_trail)
# # animal.make_sond()
# str_class = str(animal)
# print(str_class)
# list_ = []
# list_.append(animal)
# list_.append(animal2)
# print(list_)