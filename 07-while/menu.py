import json
import os

FILENAME = 'menu.json'
menu = {}

if os.path.exists(FILENAME):
    with open(FILENAME, 'r', encoding="utf-8") as f:
        menu = json.load(f)

else:
    menu = {
        'Піца': ['Тісто', 'Сир', 'Помідори'],
        'Салат': ['Огірок', 'Помідор', 'Олія'],
    }

print('Вітаємо в ресторані')

while True:
    print('-' * 40)
    action = input('Введи 1 - Перегляд, 2 - Додати 3 - Нічого: ')

    if action == '3' or action == 'Нічого':
        with open(FILENAME, 'w', encoding="utf-8") as f:
            json.dump(menu, f, ensure_ascii=False, indent=4)
        print('Меню збережено')
        break

    if action == '1' or action == 'Перегляд':
        for dish in menu:
            print('Страва: ', dish)
            print('Інгредієнти: ')
            for ing in menu[dish]:
                print('-', ing)

    elif action == '2' or action == 'Додати':
        new_dish = input('Введи назву страви яку хочеш додати: ')
        ingredients = []
        print('Введи інгредієнти до цієї страви (1/стоп щоб закінчити): ')

        while True:
            ing = input('Інгредієнт: ')
            if ing == '1' or ing == 'стоп':
                break
            ingredients.append(ing)

        menu[new_dish] = ingredients
        print("Страву додано")
