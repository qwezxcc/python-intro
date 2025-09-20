# Оператор - for
# функція - range() повертає послідовність чисел


# приклад 1
for i in range(5):  # від 0 до 4
    print("Number: ", i)
else: #
    print('Кінець циклу')

print('-'*30)

# приклад range(<параметр 1>, <параметр 2>, <параметр 3>)
k_start = 90
k_end = 20
k_step = -5
for k in range(k_start, k_end, k_step):
    print('Number: ', k)