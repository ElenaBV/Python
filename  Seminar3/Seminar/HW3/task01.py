# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

# from random import randint


# number = int(input('Введите нужный размер будущего списка '))
# my_list = []
# for i in range(number):
#     my_list.append(randint(0, 9))
# sum = 0
# for i in range(len(my_list)):
#     if (i+1) % 2 != 0:
#         sum = sum + my_list[i]
# print(f'Сумма введенного списка {my_list} = {sum}')


from random import sample


def list_rand_nums(count: int):
    if count < 0:
        print("Negative value of the number of numbers")
        return []

    list_nums = sample(range(1,count * 2), count)
    return list_nums

def sum_odd_pos(list_nums:list):
    sum_nums = 0
    for k in range(0,len(list_nums),2):
        sum_nums += list_nums[k]
    return sum_nums

all_list = list_rand_nums(int(input("Number of numbers:  ")))
print(all_list)
print (sum_odd_pos(all_list))
