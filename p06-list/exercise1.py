import random

# список
color_list = ['red', 'green', 'white', 'black', 'gray']
print(color_list)
print(color_list[0], color_list[3])

# цикл зі списком (створення списук)
my_list = []
for k in range(random.randint(5, 10)):
    my_list.append(random.randint(0, 30))

k = 0
for a in my_list:
    print(k, ')', a, sep='', end='  ')
    k += 1

my_sum = 0
for i in my_list:
    my_sum += i
print()
print('1. Сума елементів списку: ', my_sum)
print('2. Сума елементів списку: ', sum(my_list))

# гістограма
print('Гістограма:')
for i in my_list:
    for h in range(i):
        print('\u2593', end='')
    print(':', i)

print('')
# реверс списук
print('1: ', my_list)
my_list_revers = my_list[::-1]  # [::-1]
print('2: ', my_list_revers)

# відсортувати масив
print('Сортування')
print(my_list)
n = len(my_list)
for i in range(n):
    for j in range(0, n - i - 1):
        if my_list[j] > my_list[j + 1]:
            temp = my_list[j]
            my_list[j] = my_list[j + 1]
            my_list[j + 1] = temp

print(my_list)
# print(my_list.sort())