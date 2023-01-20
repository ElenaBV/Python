# Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

import random



def make_list():
    num = int(input("Input number of words "))
    word = input("Input letter :\n")
    my_list = []
    for i in range(num):
        text = random.sample(word, 3)
        my_list.append("".join(text))
    print(my_list)
    return my_list

def search_letter (my_list):
    find_txt = input("Input 3 Letters  ")
    new_list = []
    for i in range (len(my_list)):
        temp = my_list[i]
        if find_txt not in my_list[i]:
           new_list.append(temp)
        
    print(new_list)
  
search_letter(make_list())