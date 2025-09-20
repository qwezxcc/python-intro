# Гральний автомат
import random

balance = 100
game_price = 10
game_win_3 = 50
game_win_2 = 10
games_played = 0
games_won = 0
games_lost = 0
biggest_win = 0
total_won = 0
total_lost = 0

print("\u2593" * 50)
print("\u2593" * 2, ' Гральний автомат ', ' ' * 25, "\u2593" * 2)
print("\u2593" * 2, f' Стартовий баланс {balance} монет', ' ' * 16, "\u2593" * 2)
print("\u2593" * 2, f' Вартість гри {game_price} монет', ' ' * 21, "\u2593" * 2)
print("\u2593" * 2, f' Виграші:'.ljust(44), '\u2593' * 2)
print("\u2593" * 2, f' 3 однакових {game_win_3} монет, 2 однакових {game_win_2} монет ', "\u2593" * 2)
print("\u2593" * 50)

for i in range(100):
    print(f"Ваш баланс: {balance}")
    print(f"1 - Грати ({game_price} монет)")
    print("2 - Переглянути статистику")
    print("3 - Вийти з гри")
    choice = input("Ваш вибір (1-3): ")

    if choice == "1":
        print("== ГРА ==")
        balance -= game_price
        games_played += 1
        total_lost += game_price

        symbol_1 = random.randint(1, 5)
        symbol_2 = random.randint(1, 5)
        symbol_3 = random.randint(1, 5)
        print(f"Результат: [{symbol_1}] [{symbol_2}] [{symbol_3}]")

        win_amount = 0
        if symbol_1 == symbol_2 == symbol_3:
            win_amount = random.randint(40, 60)
            print("🤓 ДЖЕКПОТ! Три однакових символи!")
        elif symbol_1 == symbol_2 or symbol_1 == symbol_3 or symbol_2 == symbol_3:
            win_amount = random.randint(10, 20)
            print("😄 Два однакових символи!")
        else:
            print('😪 Нічого не виграно ...')

        if win_amount > 0:
            balance += win_amount
            games_won += 1
            total_won += win_amount

            if win_amount > biggest_win:
                biggest_win = win_amount

            print(f"Ви виграли {win_amount} монет")
        else:
            games_lost += 1
            print(f"Ви програли, і втратили {game_price} монет")

        print("== Кінець спроби ==", end='\n\n')

    elif choice == "2":
        print("== СТАТИСТИКА 🦹🏼‍♀️ ==")
        print("Зіграно ігор: ", games_played)
        print("Виграшів: ", games_won)
        print("Програшів: ", games_lost)

        if games_played > 0:
            win_rate = (games_won / games_played) * 100
            print(f'Відсоток виграшів: {win_rate:.1f}% 💡')
        print('Найбільший виграш: ', biggest_win, 'монет')
        print('Всього виграно: ', total_won, 'монет')
        print('Всього втрачено: ', total_lost, 'монет')

        net_result = total_won - total_lost
        if net_result > 0:
            print("Прибуток: ", net_result, 'монет')
        else:
            print("Збитки: ", net_result, 'монет')

        print("=" * 20, end='\n\n')

    elif choice == "3":
        print("\u2593" * 50)
        print("Дякуємо за гру!")
        break
    else:
        print("\033[91m Неправельний вибір! \033[0m", end='\n\n')

    if balance < 10:
        print("У вас недостатньо коштів")
        print('Кінець гри!')
