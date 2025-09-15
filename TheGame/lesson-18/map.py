# 0 - поле
# 1 - дерево
# 2 - река
# 3 - больница
# 4 - магазин

CELL_TYPES = "🟩🌳🟦🏥🏪"

class Map(object):
    def generate_rivers(self):
        pass

    def generate_forest(self):
        pass

    def print_map(self):
        print("⬛️" * (self.w + 2))
        for row in self.cells:
            print("⬛️", end="")
            for cell in row:
                if (cell >= 0 and cell < len(CELL_TYPES)):
                    print(CELL_TYPES[cell], end="")
            print("⬛️")
        print("⬛️" * (self.w + 2))

    def check_bounds(self, x, y):
        if (x < 0 or y < 0 or x >= self.h or y >= self.w):
            return False
        return True

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.cells = [[0 for i in range(w)] for j in range(h)]

my_map = Map(20, 10)
my_map.cells[1][1] = 1
my_map.cells[2][2] = 2
my_map.cells[3][3] = 3
my_map.cells[4][4] = 4

if (my_map.check_bounds(10, 10)):
    print("Yes")

my_map.print_map()