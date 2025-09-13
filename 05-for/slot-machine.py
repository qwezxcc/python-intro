# --

import random
from secrets import choice

from cupshelpers import parseDeviceID

balance = 100
game_price = 10
game_win_3 = 50
game_win_2 = 10
print("\u2593" * 56)
print("\u2593" * 2, '                  Гральний автомат', ' ' * 15, "\u2593" * 2)
print("\u2593" * 2, f'             Стартовий баланс {balance} монет  ', ' ' * 8, "\u2593" * 2)
print("\u2593" * 2, f'                Вартість гри {game_price} монет ', ' ' * 11, "\u2593" * 2)
print("\u2593" * 2, f' Виграші: 3 однакових = {game_win_3} монет, 2 однакових = {game_win_2}', "\u2593" * 2)
print("\u2593" * 56)

games_played = 0
games_won = 0
games_lost = 0
biggest_win = 0
total_won = 0
total_lost = 0
total_spent = 0

for i in range(100):
    print(f"Ваш баланс: {balance}")
    print(f"1 - Грати ({game_price} монет)")
    print("2 - Переглянути статистику")
    print("3 - Вийти з гри")

    choice = input("Ваш вибір: ")

    if choice == "1":
        print("===== Гра =====")
        balance -= game_price
        games_played += 1
        total_spent += game_price

        symbol_1 = random.randint(1, 5)
        symbol_2 = random.randint(1, 5)
        symbol_3 = random.randint(1, 5)
        print(f"Результат: [{symbol_1}] [{symbol_2}] [{symbol_3}]")

        win_amount = 0

        if symbol_1 == symbol_2 == symbol_3:
            win_amount = random.randint(40, 60)
            print(f"🎰 Джекпот! Три однакових символи!")
        elif symbol_1 == symbol_2 or symbol_1 == symbol_3 or symbol_2 == symbol_3:
            win_amount = random.randint(10, 20)
            print('😋 Два однакових символи!')
        else:
            print('🙁 Нічого не виграно ')

        if win_amount > 0:
            balance += win_amount
            games_won += 1
            total_won += win_amount

        if win_amount > biggest_win:
            games_won += 1
            balance += win_amount
            total_won += win_amount
            biggest_win = win_amount
            print(f"Ви виграли {win_amount} монет 🥳")
        else:
            print(f"😥 Ви пограли і втратили {game_price} монет", end='\n\n')

        print('~'*30)

    elif choice == "2":
        print(" == Статистика 📊 == ")
        print("Зіграно ігор: ", games_played)
        print("Виграшів: ", games_won)
        print("Програшів: ", games_lost)

        if games_played > 0:
            win_rate = (games_won / games_played) * 100
            print(f'Відсоток виграшів: {win_rate:.1f}% 🏆')

        print("Найбільший виграш 💰️ : ", biggest_win, "монет")
        print("Всього виграно 📈 : ", total_won, "монет")
        print("Всього програно 📉 : ", total_lost, "монет")
        print("Всього витрачено 💸 : ", total_spent, "монет")

        net_result = total_won - total_lost
        if net_result > 0:
            print("Прибуток: ", net_result)
        else:
            print('Збитки: ', net_result, 'монет')
        print()

    elif choice == "3":
        print("\u2593" * 50)
        print("Дякуємо за гру!")
        print("\u2593" * 50)
        break

    else:
        print("\033[91m Немає такого варіанту \033[0m")

    if balance < 10:
        print("У вас недостатньо коштів")
        print("Кінець гри")
