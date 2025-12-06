# всутп - повторення

name: str = "Michael"
is_student: bool = False
age: int = 21
grade: float = 76.54

print('Інформація по користувачу')

# 1 просте вивід
print(name, is_student, age, grade)

# 2 з тексом пояснення
print('Імя:', name, '  Студент:', is_student, '  Вік:', age, "  Середня оцінка:", grade, sep="")

# 3 форматований текст
print(f"Імя:{name}  Студент:{is_student}  Вік:{age}  Середня оцінка:{grade}")

# 4 форматуючий символ
print("Імя:%s  Студент:%s  Вік:%d  Середня оцінка:%f" % (name, is_student, age, grade))

# -----------------------------------------------------
# введення значень
number_1 = int(input('Веведіть число 1: '))
number_2 = int(input('Веведіть число 1: '))

print(f"Сума чисел {number_1}+{number_2}=", number_1 + number_2)
