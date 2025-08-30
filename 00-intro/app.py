# вступ - повторення

name: str = "Michael"
is_student: bool = False
age: int = 21
grade: float = 76.54

print('Інформація про користувача')


# 1 просто вивід
print(name , is_student, age, grade)


# 2 з текстом пояснення
print('Імя:', name, '  Студент:', is_student, '  Вік:', age, "  Середня оцінка:", grade)


# 3 форматований текст
print(f"Імя: {name}   Студент: {is_student}   Вік: {age}   Середня оцінка: {grade}")


# 4 форматуючий символ
print("Імя: %s   Студент: %s   Вік: %s   Середня оцінка: %s" % (name, is_student, age, grade) )



# --------------------------------------------------------------------------------------------------------------
# введення значень
number_1 = int(input('Введіть число 1:'))
number_2 = int(input('Введіть число 2:'))

print(F"Сума чисел {number_1}+{number_2} =", number_1 + number_2)