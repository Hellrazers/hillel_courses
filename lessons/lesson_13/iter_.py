list_1 = [1, 2, 3]

iter_1 = iter(list_1)

# for i in list_1:
#     print(i)

print('-'*80)
# for i in iter_1:
#     print(i)

next(iter_1)
next(iter_1)
asd = next(iter_1)
# next(iter_1)
print(asd)
asd += 5000

list_1.append(asd)
print(list_1)


class Person:
    def __init__(self):
        self.__list_person = []
        self.__len_person = 0

    def add_persons(self, name, age):
        person_to_add = {
            'name' : name,
            'age' : age
        }
        self.__list_person.append(person_to_add)

    def __repr__(self):

        return f'Person len {self.__len_person}: {self.__list_person}'

    def __iter__(self):
        return self

    def __next__(self):
        if self.__len_person >= len(self.__list_person):
            raise StopIteration
        else:
            # smth_to_return = self.__list_person[self.__len_person]
            self.__len_person += 1
            return self.__list_person[self.__len_person - 1]


person = Person()
person.add_persons(name='111', age=21)
print(person)
person.add_persons(name='222', age=21)
person.add_persons(name='333', age=21)
person.add_persons(name='444', age=21)

for person in person:
    print(person)