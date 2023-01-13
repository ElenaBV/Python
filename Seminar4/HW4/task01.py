# 1. Вычислить число c заданной точностью d
# in
# Enter a real number: 9
# Enter the required accuracy '0.0001': 0.000001
# out
# 9.000000
# in
# Enter a real number: 8.98785
# Enter the required accuracy '0.0001': 0.001
# out
# 8.988

# decimal python  - посомтреть модуль и через него искать само решение 


from decimal import Decimal
 
number = Decimal(input("Input number"))
number = number.quantize(Decimal(input("Enter the required accuracy")))
print(number)


