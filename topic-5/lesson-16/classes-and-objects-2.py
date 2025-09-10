# Задание №2
# Создайте класс Черепашка, который хранит позиции x и y черепашки, а также s - количество клеточек, на которое она перемещается за ход
# у этого класс есть методы:
# go_up() - увеличивает y на s
# go_down() - уменьшает y на s
# go_left() - уменьшает x на s
# go_right() - увеличивает y на s
# evolve() - увеличивает s на 1
# degrade() - уменьшает s на 1 или выкидывает ошибку, когда s может стать ≤ 0
# count_moves(x2, y2) - возвращает минимальное количество действий, за которое черепашка сможет добраться до x2 y2 от текущей позиции

import math
import random

class Turtle(object):
    def __init__(self, x = 10, y = 10, s = 1):
        self.x = x
        self.y = y
        self.s = s

    def go_up(self):
        self.y += self.s

    def go_down(self):
        self.y -= self.s

    def go_left(self):
        self.x -= self.s

    def go_right(self):
        self.x += self.s

    def evolve(self):
        self.s += 1

    def degrade(self):
        if self.s > 1:
            self.s -= 1
        else:
            print(f"Ошибка. Минимальное количество клеток перемещений: 1")

    def count_moves(self, x2, y2):
        print(f"X2: {x2}, Y2: {y2}")
        move_x = abs(x2 - self.x)
        move_y = abs(y2 - self.y)

        return math.ceil(move_x / self.s) + math.ceil(move_y / self.s)

my_turtle = Turtle(random.randint(-50, 50), random.randint(-50, 50), random.randint(1, 50))
print(my_turtle.x, my_turtle.y, my_turtle.s)
print(my_turtle.count_moves(random.randint(-50, 50), random.randint(-50, 50)))
