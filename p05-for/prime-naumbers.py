# Знайти прості числа з діапазону
a = int(input('Введіть початок діапазону: '))
b = int(input('Введіть кінець діапазону: '))

print(f'Прості числа з діапазону: ({a},{b})')
for n in range(a, b + 1):
    is_prime = True
    for i in range(2, int(n/2) + 1):
        if n % i == 0:
            is_prime = False

    if is_prime:
        print(' %d ' % n, end='')
