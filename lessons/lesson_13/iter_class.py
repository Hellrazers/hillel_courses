class Person:
    def __init__(self):
        self.list_person = []
        self.__iter_person = 0


    def add_person(self, name):
        self.list_person.append(name)

    def __iter__(self):
        return self


    def __next__(self):
        if self.__iter_person < len(self.list_person):
            val = self.list_person[self.__iter_person]
            self.__iter_person += 1
            return val
        raise StopIteration

persons = Person()

persons.add_person("John")
persons.add_person("Jane")
persons.add_person("Bob")

print(persons.list_person)
# for person in persons.list_person:
#     print(person)

# for person in persons:
#     print(person)

print(next(persons))
print(next(persons))
print(next(persons))
print(next(persons))