# 1. Задайте строку из набора чисел. Напишите программу,
#    которая покажет большее и меньшее число.
#    В качестве символа-разделителя используйте пробел.


def user_input(user_str):
    new_str = user_str.split()
    new_list = []

    for i in range(len(new_str)):
        new_str[i] =  new_str[i].strip(".,:;!")
        if new_str[i].replace("-","",1).isdigit():
            new_list.append(new_str[i])
    print(new_list)
    
def user_output(new_list):
    if new_list:
        return max(new_list,key = int), min(new_list,key = int)
    return"Something strange"
print(user_output(user_input(input("..."))))

