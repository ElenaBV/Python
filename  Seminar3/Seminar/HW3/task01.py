# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

from random import randint


number = int(input('Введите нужный размер будущего списка '))
my_list = []
for i in range(number):
    my_list.append(randint(0, 9))
sum = 0
for i in range(len(my_list)):
    if (i+1) % 2 != 0:
        sum = sum + my_list[i]
print(f'Сумма введенного списка {my_list} = {sum}')
