# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента. Use comprehension.
# in
# 9
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]
# in
# 10
# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

from random import choices


def make_list():
    num = int(input("Input number "))
    make_list = choices(range(num *2),k=num)
    print(make_list)
    return make_list

def new_list(make_list):
    sort_list = [(make_list[i]) for i in range (1, len(make_list)) if make_list[i] > make_list[i-1]]
    # for i in range(1, len(make_list)):
    #     if make_list[i] > make_list[i-1]:
    #         sort_list.append(make_list[i]) 
    #     else:
    #         i+=1
    return sort_list


print(new_list(make_list()))