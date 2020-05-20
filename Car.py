from Battery import Battery

class Car:
    """ Базовый Класс автомобиля"""

    def __init__(self, marka, speed):
        """ Инициализирует атрибуты марки и скорость автомобиля"""
        self.marka = marka
        self.speed = speed
        self.odometr = 0

    def car_ride(self):
        return "Машинка " + self.marka + " едет со скоростью " + str(self.speed)

    def read_odometr(self):
        """ Выведет нам пробег автомобиля"""
        print("У этого автомобиля пробег " + str(self.odometr))
    def update_odometr(self, kilometrs):
        self.odometr += kilometrs

class Tesla(Car):
    """ Тут у нас гордо выкатывается Тесла"""
    def __init__(self, marka, speed):
        """Хотим иницализировать свойства класса-родителя """
        super().__init__(marka, speed)
        self.battery = Battery(2400)
    @staticmethod
    def get_name_son():
        print("X-AF-12")














# my_bmw = Car("bmw", 120)
# jigul = Car("jigul", 60)
# audi = Car("audi", 180)
# print(getattr(jigul, 'speed'))
# if (hasattr(jigul, 'speed')):
#     print(" Оно едет")
# setattr(jigul, 'speed', 210)
# print(jigul.speed)