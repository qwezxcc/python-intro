# функції

# def function_name():
# ...
# function body
# ...


#   return # ? result


def hello():
    # 1...
    print('Привіт, це функція!')


hello()


# 2 функція з параметрами

def greet(name):
    print("Привіт ", name)


greet('Mike')


# функція з параметрами за замовчуванням
def greet_v2(name="User"):
    print(f"Привіт ", {name})

#
def user_info(name:str, age:int = 0, email:str = '') -> str:
    """
    ФУнкція отримання даних користувача
    :param name: Ім'я користувача
    :param age: Вік користувача
    :param email: Електрона пошта користувача
    :return: Статус користувача
    """
    result:str = ''

    # function code

    if age > 18:
        result += "Дорослий"
    else:
        result += "Неповнолійтній"

    return result

print(user_info("Петро", 20))
#
s = user_info(age = 20, name = "Петро")
print(s)



def sum_number(*args):
    suma = 0
    for s in args:
        suma += s
        
    return suma
print(sum_number(2, 4, 5, 4, 4, 4))