# Задание №3
# Два инвестора - Майкл и Иван хотят вложиться в стартап. Фаундеры сказали, что минимальная сумма 
# инвестиций - X долларов, больше инвестировать можно сколько угодно. У Майкла A долларов, у Ивана 
# B долларов. Если оба могут вложиться - выведите 2, если только Майкл - Mike, если только Иван - 
# Ivan, если не могут по отдельности, но вместе им хватает - 1, если никто - 0.

# СПОРНЫЙ МОМЕНТ
# Существует вероятность, что у одного не будет денег вовсе, а у другого будет вся сумма или более.
# В такой ситуации они все равно могут вложиться либо один либо вместе

person_ivan = int(input("Укажите сколько долларов есть у Ivan: "))
person_mike = int(input("Укажите сколько долларов есть у Mike: "))
minimum_investment_threshold = int(input("Укажите минимально-необходимое для инвестирования количество денег: "))

group_sum = 0
ivan_sum = 0
mike_sum = 0


if (person_ivan >= minimum_investment_threshold):
    group_sum += 1
    ivan_sum = 1

if (person_mike >= minimum_investment_threshold):
    group_sum += 1
    mike_sum = 1

if ((person_ivan + person_mike) >= minimum_investment_threshold) and (group_sum == 0):
    group_sum += 1

if (group_sum == 2):
    print("2 - Могут вложиться оба")
elif (group_sum == 1) and (ivan_sum == 0) and (mike_sum == 0):
    print("1 - Не могут вложиться каждый по отдельности, но могут вложиться вместе")
elif (group_sum == 1) and (ivan_sum == 1) and (mike_sum == 0):
    print("Ivan, а так же могут вложиться вместе")
elif (group_sum == 1) and (ivan_sum == 0) and (mike_sum == 1):
    print("Mike, а так же могут вложиться вместе")
else:
    print("0 - Никто не может вложиться")
