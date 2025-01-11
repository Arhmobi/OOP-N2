with open('recipies.txt', encoding='utf-8') as file:
    cook_book = {}
    for i in file:
        name_in = i.strip()
        name_count = file.readline()
        ingredients = []
        for ind_ in range(int(name_count)):
            i1, i2, i3 = file.readline().strip().split('|')
            ingredients.append({'ingredient_name': i1, 'quantity': i2, 'measure': i3})
        file.readline()
        cook_book[name_in] = ingredients

# print(cook_book)


# ЗАДАЧА 2

def get_shop_list_by_dishes(dishes: list, person_count: int):
    result_dict = {}
    for dish in dishes:
        if dish in cook_book:
            for i in cook_book[dish]:
                if i['ingredient_name'] in result_dict:
                   result_dict[i['ingredient_name']]['quantity'] += int(i['quantity']) * person_count
                else:
                    result_dict[i['ingredient_name']] = {'measure': i['measure'], 'quantity': int(i['quantity']) * person_count}
        else:
            print('такого блюда нет:')
    # print(result_dict)



get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)


# ЗАДАЧА ТРИ

name_dict = {}

with open('1.txt', encoding='utf-8') as f1:
    name_1 = '1.txt'
    count_1 = len(f1.readlines())
    with open('2.txt', encoding='utf-8') as f2:
        name_2 = '2.txt'
        count_2 = len(f2.readlines())
        with open('3.txt', encoding='utf-8') as f3:
            name_3 = '3.txt'
            count_3 = len(f3.readlines())
            name_dict = {count_1: [name_1, count_1], count_2: [name_2, count_2], count_3: [name_3, count_3]}

sorted_dict = dict(sorted(name_dict.items()))
with open('result.txt', 'a', encoding='utf-8') as file:
    for value in sorted_dict.values():
        for i in value:
           file.write(f'{i}\n')
with open('result.txt', encoding='utf-8') as result_file:
    print(result_file.read())



