# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

# number = int(input('Введите число '))
# binaryNum = 0
# counter = 1
# while number > 0:
#     binaryNum = binaryNum + number % 2 * counter
#     counter = counter * 10
#     number = number // 2
# print(binaryNum)


def conv_bin(num: int):
    list_nums = []

    while num > 0:
        list_nums.insert(0, num%2) # функция, которая позволит записывать следующее число перед предыдущим
        num //=2
    print(*list_nums, sep = "") #* - оператор распаковки без него будет просто список , через sep = "" мы разбиваем отсутствующим пробелом 

conv_bin(int(input("Input number for converting:  ")))