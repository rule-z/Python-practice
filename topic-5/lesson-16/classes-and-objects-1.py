# Задание №1
# Создайте класс Касса, который хранит текущее количество денег в кассе, у него есть методы:
# top_up(X) - пополнить на X
# count_1000() - выводит сколько целых тысяч осталось в кассе
# take_away(X) - забрать X из кассы, либо выкинуть ошибку, что не достаточно денег

class Box_office(object):
    def __init__(self, cash = 0):
        self.cash = cash

    def top_up(self, quantity):
        self.cash += quantity
        print(f"Счет пополнен на сумму {quantity} единиц")

    def count_1000(self):
        print(f"В кассе осталось целых тысяч в количестве {self.cash // 1000} единиц")

    def take_away(self, x):
        if self.cash >= x:
            self.cash -= x
        else:
            print("Ошибка. Недостаточно денег в кассе")

my_box_office = Box_office(0)