# Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве
# Пример:
# A (3,6); B (2,1) -> 5,09
# A (7,-5); B (1,-1) -> 7,21


import math

x1,x2 = float(input("Введите координаты точек ")),float(input("Введите координаты точек "))
y1,y2 = float(input("Введите координаты точек ")),float(input("Введите координаты точек "))
print(round((math.sqrt(((y1 - x1)**2) + ((y2 - x2)**2))),3))