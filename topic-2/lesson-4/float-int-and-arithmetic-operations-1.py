# Задание №1
# Пользователь вводит стороны прямоугольника, выведите его площадь и периметр. На вход программе 
# могут подаваться как целые числа, так и вещественные

side_a = int(input("Введите длину стороны А: "))
side_b = int(input("Введите длину стороны B: "))
rectangle_area = side_a * side_b
rectangle_perimeter = (side_a + side_b) * 2

print("Площать прямоугольника: ", rectangle_area, sep="")
print("Периметр прямоугольника: ", rectangle_perimeter, sep="")