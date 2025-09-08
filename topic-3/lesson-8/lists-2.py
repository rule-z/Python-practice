# Задание №2
# В первую строчку вводится число N (1 ≤ N ≤ 100 000). В следующую строку через пробел вводятся N 
# чисел (1 ≤ Ai ≤ 10e9). Вам требуется написать метод, который получает на вход массив и изменяет 
# его таким образом, чтобы на первом месте стоял последний элемент, на втором - первый, на третьем 
# - второй и т. д. Выведите N чисел - измененный массив.

# Замечание. При вооде чисел подряд через пробел, невозможно запретить пользователю ввести больше 
# чисел чем требуется в переменной items_count, но мы можем отсечь лишние введенные числа уже после ввода

# N
items_count = int(input("Введите количество элементов в массиве: "))
array_of_numbers = []
modified_array = []

if (items_count >= 1) and (items_count <= 100000):
    # Ai
    some_numbers = list(map(int, input("Введите числа через пробел: ").split()))

    for i in range(items_count):
        if (some_numbers[i] >= 1) and (some_numbers[i] <= 10e9):
            array_of_numbers.append(some_numbers[i])
        else:
            print(f"Ошибка. Число должно быть больше или равно 1 и меньше или равно 10 000 000 000. Текущее значение: {some_numbers[i]}")
else:
    print(f"Ошибка. Количество элементов должно быть больше или равно 1 и меньше или равно 100 000. Текущее значение: {items_count}")

modified_array.append(array_of_numbers[len(array_of_numbers) - 1])

for i in range(len(array_of_numbers) - 1):
    modified_array.append(array_of_numbers[i])

print(modified_array)