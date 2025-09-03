# Задание №2
# Дана строка, длина которой не превосходит 1000. Вам требуется преобразовать все идущие подряд 
# пробелы в один. Выведите измененную строку.

# some_string = "Какая-нибудь     строка  которую можно      обработать  нормализовав      пробелы"
some_string = input()
formatted_string = ""
last_is_space = 0

for i in some_string:
    if i == " ":
        if last_is_space == 0:
            formatted_string += i
            last_is_space = 1
    else:
        formatted_string += i
        last_is_space = 0

print(formatted_string)