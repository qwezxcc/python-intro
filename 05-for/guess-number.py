# Вгадати число яке загадав комп'ютер

import random

import a

attempts = 1
rating = 0

print("\u2591"*35)
print("\u2591"*4, ' Вгадай число від 1 до 4 ', "\u2591"*4)
print("\u2591"*4, f' Ви маєте {attempts} спроби       ', "\u2591"*4)
print("\u2591"*35)

for i in range(1, attempts + 1):
    print("Спроба: \u21D2, [", i, ']')
    random_number = random.randint(1, 4)
    user_number = int(input("Введіть число: "))
    if random_number == user_number:
        rating += 1
        print(f"\033[92mВи вгадали! \033[92m")
    else:
        print(f"\033[91m Число = {random_number}, ви ввели = {user_number}")


print("\u2591"*35)
print("\u2591"*4, f'      Ваш рейтинг {rating}      ', "\u2591"*4)
print("\u2591"*35)

