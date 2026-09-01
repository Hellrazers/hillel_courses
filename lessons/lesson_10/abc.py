from abc import ABC, abstractmethod

class Dog(ABC):
    @abstractmethod
    def make_sound(self):
        pass



class Spaniel(Dog):
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(self.name)

ssp= Spaniel('Spaniel')



