# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]

from random import randint


number = int(input('Введите нужный размер будущего списка '))
my_list = []
sum_list = []

for i in range(number):
    my_list.append(randint(0, 9))

for i in range(len(my_list)):
    while i < len(my_list)/2 and number > len(my_list)/2:
        number = number - 1
        sum = my_list[i] * my_list[number]
        sum_list.append(sum)
        i += 1
print(my_list)
print(sum_list)