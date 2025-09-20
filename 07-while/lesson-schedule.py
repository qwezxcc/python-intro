import json
import os

FILENAME = 'schedule.json'
schedule = {}

if os.path.exists(FILENAME):
    with open(FILENAME, 'r', encoding="utf-8") as f:
        schedule = json.load(f)


else:
    schedule = {
        'Понеділок': ['Алгебра', 'Фізика', 'Історія'],
        'Понеділок': ['Геометрія', 'Англійська', 'Хімія']
    }

while True:
    print('-' * 40)
    action = input('Введи: 1 - Перегляд, 2 - Додати 3 - Нічого: ')

    if action == '1' or action == 'Перегляд':
        for lesson in schedule:
            print('Урок: ', lesson)

    elif action == '2' or action == 'Додати':
        new_lesson = input('Введи назву уроку яку хочеш додати: ')

    while True:
        ing = input('Урок ')
        if ing == '1' or ing == 'стоп':
            break

    schedule[new_lesson] = lesson
    print("Страву додано")