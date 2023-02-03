
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

# Создайте список, в который попадают числа, описывающие возрастающую последовательность. Порядок элементов менять нельзя.

from random import choices


def make_list():
     num = int(input("Input number "))
     make_list = choices(range(num *2),k=num)
     return make_list

def sort_nums(sort_list):
     new_list = []
     for i in range(len(sort_list)):
         temp = sort_list[i]
         d_list = [temp]
         for j in range(i +1,len(sort_list)):
             if sort_list[j]> temp:
                 temp = sort_list[j]
                 d_list.append(temp)
         if len(d_list) > 1:
             new_list.append(d_list)
     return new_list

list1 = make_list()
print(f"First list {list1}")
print()
print(f"New lists: {sort_nums(list1)}")