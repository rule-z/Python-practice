# Задание №2
# Изза объемного описания задания 2. Смотри описание в прикрепляемом файле .docx

import collections

def get_suffix(age):
    age_ending = "лет"

    if (age % 10 == 1) and (age != 11):
        age_ending = "год"
    elif (age % 10 >= 2) and (age % 10 <= 4) and ((age < 5) or (age >= 22)):
        age_ending = "года"

    return age_ending

def get_pet(id):
    if (id in pets):
        return pets[id]

    return False

def pet_list():
    for pet_id in pets.keys():
        pet = get_pet(pet_id)
        pet_name = list(pet.keys())[0]
        pet_keys = list(pet[pet_name].keys())
        pet_values = list(pet[pet_name].values())

        some_string = f"[ {pet_id} ] Это"

        for i in range(len(pet_keys)):
            if i == 0:
                some_string += f" {pet_values[i]} по кличке {pet_name}."
            else:
                if pet_keys[i] == "Возраст питомца":
                    some_string += f" {pet_keys[i]}: {pet_values[i]} {get_suffix(pet_values[i])}."
                else:
                    some_string += f" {pet_keys[i]}: {pet_values[i]}."
        print(some_string)

def create():
    last = collections.deque(pets, maxlen=1)[0]
    pet = dict()
    pet_name = input("Укажите имя питомца: ")
    pet_type = input("Укажите тип питомца: ")
    pet_age = int(input("Укажите возраст питомца: "))
    pet_owner = input("Укажите имя владельца питомца: ")

    pet[pet_name] = dict()
    pet[pet_name]["Вид питомца"] = pet_type
    pet[pet_name]["Возраст питомца"] = pet_age
    pet[pet_name]["Имя владельца"] = pet_owner
    pets[last + 1] = dict(pet)
    print("Питомец добавлен в базу")

def read():
    pet_list()

def update():
    pet_id = int(input("Введите ID питомца, данные которого хотите изменить: "))

    pet = get_pet(pet_id)

    if (pet):
        pet_name = list(pet.keys())[0]
        pet_keys = list(pet[pet_name].keys())
        
        for pet_key in pet_keys:
            command = 0

            while (command != "N"):
                command = input(f"{pet_key}: {pet[pet_name][pet_key]} - Изменить эти данные? (Y/N): ")

                if command.upper() == "Y":
                    if (pet_key == "Возраст питомца"):
                        pet[pet_name][pet_key] = int(input(f"Введите новое значние для {pet_key}: "))
                    else:
                        pet[pet_name][pet_key] = input(f"Введите новое значние для {pet_key}: ")
                    break
                elif command.upper() == "N":
                    break
                else:
                    "Неизвестная команда"
        
        print("Данные питомца обновлены.")
    else:
        print("Ошибка. Питомец с таким ID не существует.")

def delete():
    count = collections.deque(pets, maxlen=1)[0]
    pet_id = int(input("Введите ID питомца, данные которого хотите удалить: "))

    pet = get_pet(pet_id)

    if (pet):
        pets.pop(pet_id)
        print("Питомец удален из базы")
    else:
        print("Ошибка. Питомец с таким ID не существует.")

pets = {
    1: {
        "Мухтар": {
            "Вид питомца": "cобака",
            "Возраст питомца": 1,
            "Имя владельца": "Павел"
        },
    },
    2: {
        "Каа": {
            "Вид питомца": "желторотый питон",
            "Возраст питомца": 2,
            "Имя владельца": "Саша"
        },
    },
    3: {
        "Симба": {
            "Вид питомца": "львенок",
            "Возраст питомца": 5,
            "Имя владельца": "лев"
        },
    },
    4: {
        "Яго": {
            "Вид питомца": "попугай",
            "Возраст питомца": 21,
            "Имя владельца": "Алладин"
        },
    },
    5: {
        "Лабубу": {
            "Вид питомца": "игрушка",
            "Возраст питомца": 23,
            "Имя владельца": "дети"
        },
    },
    6: {
        "Ститч": {
            "Вид питомца": "эксперимент 626",
            "Возраст питомца": 25,
            "Имя владельца": "Лило"
        },
    },
    7: {
        "Рататуй": {
            "Вид питомца": "уличная крыса",
            "Возраст питомца": 7,
            "Имя владельца": "повар"
        },
    },
    8: {
        "Хайзенберг": {
            "Вид питомца": "учитель химии",
            "Возраст питомца": 51,
            "Имя владельца": "нет"
        },
    },
    9: {
        "Фредди": {
            "Вид питомца": "кошмар из сна",
            "Возраст питомца": 60,
            "Имя владельца": "Кошмар на улице Вязов"
        },
    },
    10: {
        "Python": {
            "Вид питомца": "язык разработки программ",
            "Возраст питомца": 25,
            "Имя владельца": "Python Software Foundation"
        },
    },
    11: {
        "код задания № 2": {
            "Вид питомца": "функции",
            "Возраст питомца": 0,
            "Имя владельца": "Виталий"
        },
    },
}

command = 0

while (command != "stop"):
    print("Доступные комманды: create, read, update, delete, stop")
    command = input("Введите команду: ")

    if command == "create":
        create()
    elif command == "read":
        read()
    elif command == "update":
        update()
    elif command == "delete":
        delete()
    else:
        "Неизвестная команда"