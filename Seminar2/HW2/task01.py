# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

# num = float(input('Input number: '))
# m = len(str(num))
# num = num * 10 ** (m - 2)
# print(num)

number = float(input("Введите число "))
sum = 0 
m = len(str(number))
number = number* 10 ** (m - 2)
while number != 0:
    sum = sum + number % 10 
    number = number // 10
print( sum )