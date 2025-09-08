# Задание №2
# Вводятся два списка чисел, которые могут содержать до 100000 чисел каждый. Все числа каждого 
# списка находятся на отдельной строке. Выведите, сколько чисел содержится одновременно как в 
# первом списке, так и во втором.

first_set = set()
second_set = set()
sets_numeration = ""

for i in range(2):
    if i == 0:
        sets_numeration = "первого"
    else:
        sets_numeration = "второго"

    set_size = int(input(f"Сколько элементов будет в множестве {i + 1}?: "))
    
    while (set_size > 0):
        number_in_set = int(input(f"Введите число для {sets_numeration} списка: "))

        if (i == 0):
            first_set.add(number_in_set)
        else:
            second_set.add(number_in_set)
        set_size -= 1

print(f"Множество 1: {first_set}")
print(f"Множество 2: {second_set}")
print(f"Одновременно как в первом так и во втором списке содержится количество чисел: {len(first_set.intersection(second_set))}")
print(f"Это числа: {first_set.intersection(second_set)}")