# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

number = int(input('Введите число '))
binaryNum = 0
counter = 1
while number > 0:
    binaryNum = binaryNum + number % 2 * counter
    counter = counter * 10
    number = number // 2
print(binaryNum)