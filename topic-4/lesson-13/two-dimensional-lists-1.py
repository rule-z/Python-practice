# Задание №1
# С помощью цикла создайте две матрицы вида 10x10.
# Сложить эти две матрицы в третью. Чтобы заполнить матрицы различными значениями - воспользуйтесь модулем random

import random

# Красивый вывод матрицы
def print_matrix(matrix, matrix_name):
    print(matrix_name)
    for rows in matrix:
        print(rows)

matrix_1 = [[random.randint(-500, 500) for i in range(10)] for i in range(10)]
matrix_2 = [[random.randint(-500, 500) for i in range(10)] for i in range(10)]
matrix_3 = []

# Флаг показывающий, что матрицы не равны по длине
not_the_same_length = False

# Проверка матриц на одинаковость в длинах
if (len(matrix_1) != len(matrix_2)): # Проверка что количество элементов одинаковое
    not_the_same_length = True
else:
    for i in range(len(matrix_1)):
        if len(matrix_1[i]) != len(matrix_2[i]): # Проверка что количество элементов внутри элементов одинаковое
          not_the_same_length = True  

if not not_the_same_length: # Если длины матриц равны, производим сложение матриц
    for i in range(len(matrix_1)):
        matrix_3_row = []
        for j in range(len(matrix_1[i])):
            matrix_3_row.append(matrix_1[i][j] + matrix_2[i][j])

        matrix_3.append(matrix_3_row)

    print_matrix(matrix_1, "Матрица 1")
    print_matrix(matrix_2, "Матрица 2")
    print_matrix(matrix_3, "Матрица 3")
else:
    print("Ошибка. Матрицы не равны между собой по длине")