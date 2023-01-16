# 3. Задайте последовательность чисел. 
# Напишите программу, которая выведет список неповторяющихся элементов исходной 
# последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
# in
# -1
# out
# Negative value of the number of numbers!
# []

# choicec метод и остается те, котрые были в ед экземпляре 
# модуль collections


# from random import randrange


# def list_rand_nums(count:int):
#     if count <0:
#         print("Negative value of the number of numbers")
#         return []

#     list_nums = []
#     for i in range(count):
#         list_nums.append(randrange(count))

#     return list_nums

# def uniq_el(list_nums: list):
#     result = []
#     my_dict = {}.fromkeys(list_nums,0) #ключами словаря могут быть только уникальные значения, поэтому повторяющиеся значения уйдут

#     for i in list_nums:
#         my_dict[i]+=1 # увеличит счетчик, если есть повтор 
#     for k in my_dict:
#         if my_dict[k] == 1:
#             result.append(k)
#     return result

# all_list = list_rand_nums(int(input("Nmber ")))
# print(all_list)
# print (uniq_el(all_list))

from collections import Counter

my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
counter = Counter(my_list)

single = [x for x, n in counter.items() if n == 1]
print(single)