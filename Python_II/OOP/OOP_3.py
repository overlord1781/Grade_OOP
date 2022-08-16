class Car:
    """Описание класса"""

    CURENT_SPEED = int

    def __init__(self, name, engine, color):
        self.name = name  # Название авто
        self.engine = engine  # Объем двигателя
        self.color = color  # Цвет авто
        self.nois = self.__get_nois()  # Приватный метод, результат работы которого записывается в атрибут nois

    @property
    def speed(self):
        return self.CURENT_SPEED

    @speed.setter
    def speed(self, speed):
        self.CURENT_SPEED = speed

    @staticmethod
    def start_the_engine():
        print('Вы завели двигатель')

    def __get_nois(self):
        if self.engine <= 1.6:
            return 'тыртыртыр'
        if 1.6 < self.engine <= 2.5:
            return 'брбрбрбрбр'
        if self.engine > 2.5:
            return 'врум врум'

    @classmethod
    def get_list_auto(cls, list_auto):
        name, engine, color = list_auto.split('/')
        car = cls(str(name), float(engine), str(color))
        return car


class Cargo_car(Car):  # Создали клас "Грузовой автомобиль" наследник класса "Авто"
    def __init__(self, name, engine, color, weight, max_weight):
        super().__init__(name, engine, color)
        self.weight = float(weight)
        self.max_weight = float(max_weight)

    def can_move(self):
        if self.weight > self.max_weight:
            return 'Не могу тронуться'

        else:
            return 'поехали'


man_medium_cargo = Cargo_car('MAN', 8, 'blue', 5, 10)
print(man_medium_cargo.can_move())
man_full_cargo = Cargo_car('MAN', 8, 'blue', 11, 10)
print(man_full_cargo.can_move())

man_full_cargo.start_the_engine()

man_full_cargo.speed = 200
print(man_full_cargo.speed)