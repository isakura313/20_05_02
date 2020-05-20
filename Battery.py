class Battery():
    """ инициализирует атрибуты и методы аккумулятора для нашей Теслы"""
    def __init__(self, battery_size):
        self.battery_size = battery_size
    def show_akk(self):
        print("аккумулятор емкостью " + str(self.battery_size))