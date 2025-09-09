# Задание №1
# Создайте функцию, которая принимает в качестве параметра - натуральное целое число. Данная 
# функция находит факториал полученного числа

def factorial(number):
    if number == 1:
        return 1
    
    return factorial(number - 1) * number


some_number = int(input("Введите число: "))
factorial_value = factorial(some_number)
factorials_list = list()

print(f"Факториал числа {some_number}: {factorial_value}")

for i in range(factorial_value, 0, -1):
    factorials_list.append(factorial(i))

print(factorials_list)