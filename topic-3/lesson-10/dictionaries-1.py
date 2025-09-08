# Задание №1
# Описание слишком длинное. Смотри приложенный файл .docx

pets = dict()
pet_name = input("Укажите имя питомца: ")
age_ending = "лет"

if pet_name not in pets.keys():
    pet_type = input("Укажите тип питомца: ")
    pet_age = int(input("Укажите возраст питомца: "))

    if (pet_age % 10 == 1) and (pet_age != 11):
        age_ending = "год"
    elif (pet_age % 10 >= 2) and (pet_age % 10 <= 4) and ((pet_age < 5) or (pet_age >= 22)):
        age_ending = "года"

    pet_owner = input("Укажите имя владельца питомца: ")
    pets[pet_name] = {"Вид питомца": pet_type, "Возраст питомца": pet_age, "Имя владельца": pet_owner}
else:
    print(f"Ошибка. Питомец с именем {pet_name} уже есть в словаре")

for pet in pets:
    pet_keys = list(pets[pet].keys())
    pet_values = list(pets[pet].values())

    some_string = "Это"

    for i in range(len(pet_keys)):
        if i == 0:
            some_string += f" {pet_values[i]} по кличке {pet}."
        else:
            if pet_keys[i] == "Возраст питомца":
                some_string += f" {pet_keys[i]}: {pet_values[i]} {age_ending}."
            else:
                some_string += f" {pet_keys[i]}: {pet_values[i]}."

print(some_string)