# Создайте список из N натуральных чисел, упорядоченных
# по возрастанию. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1= A[i-1]. Найдите это число.


from random import choice


def make_list():
    num = int(input("Input number "))
    my_list = [i for i in range (num + 1)]
    my_list.remove(choice(my_list))
    print(my_list)
    return my_list

def find_num(my_list):
    for i in range(1,len(my_list)):
        if my_list[i] - 1 != my_list[i-1]:
            return (my_list[i]-1)
    return -1

print(find_num(make_list()))

