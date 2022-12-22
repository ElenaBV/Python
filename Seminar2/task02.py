# создать список длины n, значение формируется по формуле 3k+1, где k принимает значение от 1 до n

my_list = []
n = (int(input("Введите длину списка")))
for i in range (1, n+ 1):
    my_list.append(3*i + 1)
    
print(my_list)
