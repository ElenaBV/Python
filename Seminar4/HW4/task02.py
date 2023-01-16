# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# in
# 54
# out
# [2, 3, 3, 3]
# in
# 9990
# out
# [2, 3, 3, 3, 5, 37]

# n = int(input("Input number N  "))
# i = 2 
# my_list = []

# while i <= n:
#     if n % i == 0:
#         my_list.append(i)
#         n //= i
#     else:
#         i += 1
# print(f"список простых множителей числа N -  {my_list}")

def find_prime_nums(num):
    pr_fact = []
    di = 2
    while num > 1:
        if num % di == 0:
            pr_fact.append(di)
            num/= di
        else:
            di+=1
    return pr_fact