from random import sample


def num_find(len_list, number):

    new_list = sample(range(1, len_list * 2), k=len_list)
    print(new_list)
    if number in new_list:
        return "Yes"
    return "No"

print(num_find(int(input("Введите длину списка   ")), int(input("Введите искомое число  "))))

