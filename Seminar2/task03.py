

string1 = input("Input string")
string2 = input("Input string")

count = 0
for i in range(len(string1)):
    if string2 == string1[i:i+len(string2)]:
        count+=1

print(count)
# реализация через методы 
n1 = input("Введите 1 строку  ")
n2 = input ("Введите искомую строку  ")

print(n1.count(n2))