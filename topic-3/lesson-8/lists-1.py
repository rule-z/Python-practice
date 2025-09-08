# Задание №1
# В первой строке вводится число N. Далее в N строк вводится N чисел (1 ≤ N ≤ 10000), по одному 
# числу на строке. Все числа по модулю не превышают 10e5. Переверните массив чисел. Выведите N 
# чисел - перевернутый массив.

# N
list_size = int(input("Количество элементов в массиве: "))
array_of_items = []

if (list_size >= 1) and (list_size <= 10000):
    for i in range(1, list_size + 1):
        some_number = int(input("Введите число: "))

        if (some_number >= -10e5) and (some_number <= 10e5):
            array_of_items.append(some_number)
        else:
            print(f"Ошибка. Число должно быть не менее -10e5 и не более 10e5. Текущее значение: {some_number}")

    if (len(array_of_items) > 0):
        array_of_items.reverse()
        print(array_of_items)
else:
    print(f"Ошибка. N должно быть не менее 1 и не более 10000. Текущее значение: {list_size}")