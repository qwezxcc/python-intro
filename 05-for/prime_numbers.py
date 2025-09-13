# Знайти прості числа з діапазону




a = int(input('Введіть початок діапазону: '))
b = int(input('Введіть кінець діапазону: '))

for n in range(a, b + 1):
    is_prime = True
    for i in range(2, n):
        if n % i == 0:
            is_prime = False

    if is_prime:
        print('%d ' % n, end='')