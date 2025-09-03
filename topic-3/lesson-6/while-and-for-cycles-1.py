# Задание №1
# Сначала вводится число N, затем вводится ровно N целых чисел. Подсчитайте, сколько из них равны 
# нулю, и выведите это количество.

nums_count = int(input("Сколько чисел будем проверять?: "))
zero_amount = 0

while nums_count > 0:
    some_number = int(input("Введите число: "))

    if (some_number == 0):
        zero_amount += 1
    
    nums_count -= 1
print("Количество чисел равных нулю:", zero_amount)