print('----------------')
print("Початок програми")
a = 300
b = 1000
c = False

# if 1 ----
if a > b or c:
    print(f'1. Число a={a} ')
if b > a or c:
    print(f'1. Число b={b} ')

# if 2 ----
if b == 1000:
    print(f'2. Число b={b} - (1000)')
elif a > b or c:
    print(f'2. Число a={a} ')
elif b > a or c:
    print(f'2. Число b={b} ')


print("Кінець програми")
print('----------------')


# Вкладені умови
temperature = 28
is_raining = True

if temperature > 30:
    if is_raining:
        print('Жарко і дощ')
    else:
        print('Жарко')
elif temperature > 20:
    if is_raining:
        print('Тепло і дощ')
    else:
        print('Тепло')
else:
    print('Холодно')


# Оператор match
day: str = input('Введіть день: ')
day = day.capitalize()

match day:
    case 'Понеділок':
        print(f'{day}: Початок робочого тижня')
    case 'Вівторок':
        pass # оператор заповнення
    case 'Середа':
        print(f"{day}: Середина робочоо тижня")
    case 'Пятниця':
        print(f"{day}: Кінець робочого тижня")
    case _ :
        print('Інший день')