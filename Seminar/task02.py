# На вход принимает 5 чисел и находит максимальное



num = int(input('Введите количество чисел '))
my_list = []
for i in range(num):
    my_list.append(int(input('Введите числа ')))

max = 0
for i in range(len(my_list)):
    if my_list[i] > max:
        max = my_list[i]
        i+=1
print(f'Максимальное число в {my_list} = {max}')
