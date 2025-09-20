# словник товарів: назва -- ціна
from secrets import choice

products: dict = {"Яблуко": 10, "Хліб": 25, "Молоко": 30, "Шоколад": 60}

cart: list = []
total: int = 0

print('Grocery:')
for name in products:
    print('-', name, ':', products[name], 'грн')


    print('-'*50)


while True: # ! безкінечний цикл !
    choice = input('Введіть повну назву товару який хочете придбати (або `Оплатити` для оплати та виходу):' )




    if choice == 'Оплатити':
        break


    if choice in products:
        price = products[choice]
        cart.append((choice, price))
        total += price
        print('У кошик додано: ', choice, '-', price, 'грн')
    else:
        print('Такого товару не існує')

print('Ваші покупки: ')
for item in cart:
    print(item[0], '-', item[1], 'грн')

print('Загальна сума: ', total)






