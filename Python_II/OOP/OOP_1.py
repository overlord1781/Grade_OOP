class Car:
    """Описание класса"""

    def __init__(self, name, engine, color):
        self.name = name            # Название авто
        self.engine = engine        # Объем двигателя
        self.color = color          # Цвет авто

    def start_the_engine(self):
        print('Вы завели двигатель')




KiaRio = Car(name='Kia rio', engine=1.6, color='red')

print(KiaRio.name)
print(KiaRio.engine)
print(KiaRio.color)