# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки, 
# одержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
# out

# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}

def make_list ():
    make_list = [str(i) for i in input("Input names ").split()]
    print (make_list)
    return make_list

def dictionary_new (make_list):
    make_dict = {}
    make_list.sort()
    for name in make_list:
        key = name[0]
        if key not in make_dict:
            make_dict[key] = []
        make_dict[key].append(name)
    print (make_dict)
    
dictionary_new(make_list())
