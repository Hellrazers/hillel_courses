# Поїзд складається з вагонів, перший вагон — локомотив.
#
# У поїзді може бути тільки один локомотив.
#
# Локомотив не може перевозити пасажирів.
#
# Кожен звичайний вагон може перевозити не більше 10 пасажирів.


class Wagon:
    MAX_PASSANGERS = 10

    def __init__(self, is_head_wagon: bool = False):
        self.is_head_wagon = is_head_wagon
        self.passangers = []

    def add_passanger(self, passanger: list):
        if self.is_head_wagon:
            raise ValueError('Локомотив не може перевозити пасажирів.')
        else:
            for i in passanger:
                self.passangers = self.passangers + [i]

    def __setattr__(self, key, value):
        if key == 'passangers':
            is_head = getattr(self, 'is_head_wagon', False)
            if not is_head and len(value) > self.MAX_PASSANGERS:
                raise ArithmeticError('Кожен звичайний вагон може перевозити не більше 10 пасажирів.')
            if is_head and len(value) > 0:
                raise ValueError('Локомотив не може перевозити пасажирів.')

        super().__setattr__(key, value)

    def __repr__(self):
        if self.is_head_wagon:
            return 'LOKOMOTIVE'
        else:
            return f'Wagon({self.passangers})'


class Train:
    COUNTER_OF_HEAD_WAGON = 1

    def __init__(self):
        self.train = [Wagon(is_head_wagon=True), ]

    def add_wagon(self, wagon: Wagon):
        self.train = self.train + [wagon]

    def __setattr__(self, key, value):
        if key == 'train':
            counter = 0
            for item in value:
                if getattr(item, 'is_head_wagon', True):
                    counter += 1
            if counter != self.COUNTER_OF_HEAD_WAGON:
                raise ValueError('У поїзді може бути тільки один локомотив.')
            if counter == 0:
                raise ArithmeticError('У поїзді може бути тільки один локомотив.')
        super().__setattr__(key, value)

