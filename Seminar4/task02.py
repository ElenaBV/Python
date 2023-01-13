# 2. Найдите корни квадратного уравнения Ax² + Bx + C = 0,
#    с помощью дополнительных библиотек python. Запросите значения А, В, С 3 раза.
#    Уравнения и корни запишите в файл.

from math import sqrt


def roots_equ(a, b, c):
    D = b**2 - 4*a*c
    with open("roots.txt", "a", encoding="utf-8") as my_f:
        my_f.write(f"{a}x ** 2 + {b}x + {c} = 0\n")
        if D > 0 and a:
            my_f.write(f"The first root: {(-b + sqrt(D)) / (2 * a):.2f}\n")
            my_f.write(f"The first root: {(-b - sqrt(D)) / (2 * a):.2f}\n")

        elif D == 0 and a:
            my_f.write(f"The root: {-b / (2 * a):.2f}\n")
        else:
            my_f.write("There are no roots.\n")

# roots_equ(2, 3, 1)
for i in range(3):
    roots_equ(int(input("Enter the coefficient 'a': ")), int(input("Enter the coefficient 'b': ")),
              int(input("Enter the coefficient 'c': ")))