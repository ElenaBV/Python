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



my_list =list(map(int, input("Введите числа: ").split()))
print(my_list)
new_list = []
for item in my_list:
    if item not in new_list:
        new_list.append(item)
print(new_list)

