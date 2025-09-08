# Задание №3
# На берегу реки стояли n рыбаков, все они хотели перебраться на другой берег. Одна лодка может 
# выдержать не более m килограмм, при этом в лодку помещается не более 2 человек. Определите, 
# какое минимальное число лодок нужно, чтобы перевезти на другой берег всех рыбаков В первую 
# строку вводится число m (1 ≤ m ≤ 10e6) - максимальная масса, которую может выдержать одна лодка. 
# Во вторую строку вводится число n (1 ≤ n ≤ 100) - количество рыбаков. В следующие N строк 
# вводится по одному числу Ai (1 ≤ Ai ≤ m) - вес каждого путешественника. Программа должна вывести 
# одно число - минимальное количество лодок, необходимое для переправки всех рыбаков на 
# противоположный берег.

# m
max_load_capacity = int(input("Укажите максимальную массу, которую может выдержать одна лодка: "))

if (max_load_capacity >= 1) and (max_load_capacity <= 10e6):
    # n
    number_of_fishermen = int(input("Укажите количество рыбаков: "))
    
    if (number_of_fishermen >= 1) and (number_of_fishermen <= 100):
        # Ai
        weight_of_fishermen = []
        for i in range(number_of_fishermen):
            weight = int(input(f"Укажите вес рыбака {i + 1}: "))

            if (weight >= 1) and (weight <= max_load_capacity):
                weight_of_fishermen.append(weight)
            else:
                print(f"Ошибка. Вес рыбака должен быть в диапазоне от 1 до {max_load_capacity}")
        weight_of_fishermen.sort()

        i = 0
        j = len(weight_of_fishermen) - 1
        count = 0

        while (i <= j):
            if (weight_of_fishermen[j] == max_load_capacity):
                count += 1
                j -= 1
            elif (weight_of_fishermen[i] == max_load_capacity):
                count += 1
                i += 1
            elif ((weight_of_fishermen[j] + weight_of_fishermen[i]) <= max_load_capacity):
                count += 1
                i += 1
                j -= 1
            else:
                count += 1
                j -= 1

        print(f"Необходимое количество лодок: {count}")
    else:
        print(f"Ошибка. Максимальное колиество рыбаков должно быть в диапазоне от 1 до 100. Текущее значение: {number_of_fishermen}")
else:
    print(f"Ошибка. Максимальная масса должна быть в диапазоне от 1 до 10e6. Текущее значение: {max_load_capacity}")