# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]

# from random import randint


# number = int(input('Введите нужный размер будущего списка '))
# my_list = []
# sum_list = []

# for i in range(number):
#     my_list.append(randint(0, 9))

# for i in range(len(my_list)):
#     while i < len(my_list)/2 and number > len(my_list)/2:
#         number = number - 1
#         sum = my_list[i] * my_list[number]
#         sum_list.append(sum)
#         i += 1
# print(my_list)
# print(sum_list)

from random import sample


def list_rand_nums(count: int):
    if count < 0:
        print("Negative value of the number of numbers")
        return []

    list_nums = sample(range(1, count * 2), count)
    return list_nums


def prod_pairs(list_nums: list):
    res_list = []
    len_list = len(list_nums)

    for k in range(len_list//2):
        res_list.append(list_nums[k] * list_nums[len_list - k - 1])

    if len_list % 2:
        res_list.append(list_nums[len_list // 2])
    return res_list


all_list = list_rand_nums(int(input("Number of numbers%  ")))
print(all_list)
print(prod_pairs(all_list))