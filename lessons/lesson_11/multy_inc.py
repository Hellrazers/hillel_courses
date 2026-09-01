class Animal:
    def __init__(self, name, age, alive):
        self.name = name
        self.age = age
        self.alive = alive

class Dog(Animal):
    def __init__(self, color, **kwargs):
        super().__init__(**kwargs)
        self.color = color

class Cat(Animal):
    def __init__(self, has_tail, **kwargs):
        super().__init__(**kwargs)
        self.has_tail = has_tail

class CatDog( Dog, Cat):
    def __init__(self, make_noise, **kwargs):
        super().__init__(**kwargs)
        self.make_noise = make_noise


# 2 поганий варіант наслідування
# class Animal:
#     def __init__(self, name, age, is_alive):
#         self.name = name
#         self.age = age
#         self.is_alive = is_alive
#
#
#
# class Dog(Animal):
#     def __init__(self, name, age, color, alive):
#         Animal.__init__(self, name, age, alive)
#         self.color = color
#
#
# class Cat(Animal):
#     def __init__(self, name, age, has_tail, alive):
#         Animal.__init__(self, name, age, alive)
#         self.has_tail = has_tail
#
#
#
#
# class CatDog( Dog, Cat):
#     def __init__(self, name, age, color,has_tail, make_noise, alive):
#         Cat.__init__(self, name, age,has_tail, alive)
#         Dog.__init__(self, name, age, color, alive)
#         self.make_noise = make_noise


cat_dog = CatDog(name='CatDog', age=30, has_tail=True,color='grey',make_noise='GauMau', alive=True)
print(cat_dog.__class__)
print(cat_dog.__class__)
print((CatDog.__mro__))


print(cat_dog.make_noise)
print(cat_dog.name)
dog_1 = Dog(name='Dog', age=30, alive=True, color='red')

print(dog_1.name)