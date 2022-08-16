class Car:
    """Описание класса"""

    def __init__(self, name, engine, color):
        self.name = name  # Название авто
        self.engine = engine  # Объем двигателя
        self.color = color  # Цвет авто
        self.nois = self.__get_nois() # Приватный метод, результат работы которого записывается в атрибут nois

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



car1 = Car.get_list_auto('lada/1.2/red')
car1.start_the_engine()