# Задание №1
# Изза объемного описания задания 1. Смотри описание в прикрепляемом файле .docx

class Transport(object):
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def print_info(self):
        print(f"Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}")

Autobus = Transport('Renault Logan', 180, 12)
Autobus.print_info()