# Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10
# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

import random



def make_list(num:int , word:str):
    my_list = []
    for i in range(num):
        text = random.sample(word, k=3)
        my_list.append("".join(text))
    print(my_list)
    return my_list

# def make_list(num:int,word:str):
#   return " ".join("".join(sample(word,3))for _ in range(num))
# запись с помощью comprehencion для увеличения скорости работы 
def search_letter (my_list):
    find_txt = input("Input 3 Letters  ")
    new_list = []
    for i in range (len(my_list)):
        temp = my_list[i]
        if find_txt not in my_list[i]:
           new_list.append(temp)
        
    print(new_list)
  
search_letter(make_list())