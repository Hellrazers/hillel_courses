class BankAccount(object):
    def __init__(self, name):
        self.name = name
        self.__balance = 0
        self._age = 0


    def deposit(self, value):
        self.__balance += value

    def get_balance(self):
        return self.__balance

class BankPrivate(BankAccount):
    def __init__(self, name):
        super().__init__(name)


    def deposit(self, value):
        print(f'Helo {self.name}!\nYour balance is {self.get_balance()}')
        print(f'You will add this {value} in your balance')
        self._BankAccount__balance += value

        print('DONE')
        print(f"Your balance is {self.get_balance()}")


print(BankPrivate.__mro__)
print(bool.__mro__)


# bank1 = BankAccount('BankAccount')
# print(bank1._age)
# bank1._age = 8
# print(bank1._age)
# print(bank1.get_balance())
# bank1.deposit(100)
# print(bank1.get_balance())
#
#
# bnk_1 = BankPrivate(name='Private Bank')
# print(bnk_1.name)
# bnk_1.deposit(123)
# bank1.deposit(100)
# bank1.get_balance()
#

class Dog(object):
    def make_sound(self):
        print('Dog')

class Cat(Dog):
    def make_sound(self):
        print('Cat')

