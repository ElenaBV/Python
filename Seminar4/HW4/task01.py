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


# from decimal import Decimal
 
# def accuracy(num, acc):
#     number = Decimal(f"{num}")
#     return number.quantize(Decimal(f"{acc}"))

# print(accuracy(float(input ("Input number ")),
#                float(input("Enter the required accuracy"))))



num = float(input("Enter a number  "))

_, accu = input("Enter the accuracy  ").split(".") #_, безымянная переменная отбрпсвает то, что до сплита 
print(f"{num:.{len(accu)}f}") # способ форматирования строки для округления до количества после запятой