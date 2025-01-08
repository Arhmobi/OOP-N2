# задача один
cook_book = {}
ingredients = []
with open('recipies.txt', 'r', encoding='utf-8') as file:
    for k in file:
        name_ingred = k.strip()
        name_count = int(file.readline())
        for ind in range(name_count):
            recipie = file.readline().strip().split('|')
            ingredient_name, quantity, measure = recipie
            ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        file.readline()
        cook_book[name_ingred] = ingredients


# задача два
def get_shop_list_by_dishes(dishes: list, person_count: int):
    result = {}  # создаем список где будет вывод условия задачи
    for dish in dishes:   #  проходим циклом по каждому значению в списке
        if dish in cook_book:   # проверям есть ли значение в словаре
            for i in cook_book[dish]:   #(если есть) проходим циклом по всем встречающимся в словаре с этим значениям
                if i['ingredient_name'] in result:  # если есть в словаре result
                     result[i['ingredient_name']]['quantity'] += i['quantity'] * person_count
                else:
                    result[i['ingredient_name']] = {'measure': i['measure'],'quantity': (i['quantity'] * person_count)}   #
        else:
            print('нет такого блюда')
    print(result)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)