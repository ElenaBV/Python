# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# in 
# 6
# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071


number = int(input("Введите число "))
my_list = []
for i in range(1, number+1):
    my_list.append(f'{(1 + 1 / i) ** i}')
print(my_list)
sum = 0
for i in range(1, number + 1):
    sum += (1 + 1 / i) ** i
print(sum)
