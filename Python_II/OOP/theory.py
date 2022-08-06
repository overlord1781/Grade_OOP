class Car:
    """Описание класса"""
    name = 'car name' #Здесь мы объявили атрибут класса, который на данный момент хранит в себе строку
    def start_the_engine(self):
        print('Вы завели двигатель')


lada_priora = Car()
lada_priora.start_the_engine()