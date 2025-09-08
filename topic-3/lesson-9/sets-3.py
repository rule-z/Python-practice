# Задание №3
# Во входную строку водится последовательность чисел через пробел. Для каждого числа выведите слово
# ”YES” (в отдельной строке), если это число ранее встречалось в последовательности или ”NO”, если не встречалось.

some_numbers = list(map(int, input("Введите числа через пробел: ").split()))
set_of_numbers = set()

for i in range(len(some_numbers)):
    if (some_numbers[i] in set_of_numbers):
        print(f"{some_numbers[i]} - YES")
    else:
        print(f"{some_numbers[i]} - NO")
        set_of_numbers.add(some_numbers[i])