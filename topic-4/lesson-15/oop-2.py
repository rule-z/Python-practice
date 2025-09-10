# Задание №1
# Изза объемного описания задания 2. Смотри описание в прикрепляемом файле .docx

class Transport(object):
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def print_info(self):
        print(f"Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}")

    def seating_capacity(self, capacity):
        return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"
    
class Autobus(Transport):
    def seating_capacity(self, capacity = 50):
        return f"Вместимость одного автобуса {self.name} {capacity} пассажиров"

MyAutobus = Autobus('Renault Logan', 180, 12)
MyAutobus.print_info()
print(MyAutobus.seating_capacity())