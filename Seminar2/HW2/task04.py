# *Напишите программу, которая принимает на вход 2 числа. 
# Получите значение N, для пустого списка, заполните числами в диапазоне 
# [-N, N]. Найдите произведение элементов на указанных позициях(не индексах).

num1 = int(input("Введите 1 позицию  "))
num2 = int(input("Введите 2 позицию  "))
n = int(input("Введите число  "))
my_list = []
for i in range(- n, n +1 ):
    my_list.append(i)
print(my_list)
sum = 0
if num1 > len(my_list) or num2 > len(my_list):
    print("Позиции такой нет ")
else:
    for i in range (len(my_list)):
        sum = my_list[num1 - 1] * my_list[num2 - 1]
    print(sum)
