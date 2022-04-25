# def a(a: int,b: int,c: int,d: int) -> int: # это параметры
#     """Функция возвращает сумму всех парамтеров!"""
#     return a + b + c+ d

# res = a(1,2,3,4) # аргументы 
# print(res)
# print(type(res))

# =============================================================================================

# Позиционные и именованные аргументы

# def test(a=None,b=None,c=None):
#     print(a, ' is on a')
#     print(b, ' is on b')
#     print(c, ' is on c')

# # test(b=2,c=3) # именованные аргументы (keyword arguments)
# # test(1,2,3) # позиционные аргументы (arguments)

# ls = ['123','1233','1','12','12344555']
# ls.sort(key=len)
# print(ls)

# оператор *args (распаковщик) 
# a = [1,2,3]
# b = [*a,4,5,6]
# c = [*a, *b]
# print(b)
# print(c)

# =================================================================================

# *args, **kwargs в функциях

# def printScores(studen, *args):
#     print(f'Student name: {studen}')
#     print(args)
#     print(type(args))
#     for i in args:
#         print(i)

# printScores('kalash', 100,90,89,80,99)

# (100,90,89,80,99) -> args



# def printPetnames(owner, **kwargs):
#     print(f'owner name {owner}')
#     print(kwargs)
#     print(type(kwargs))

#     # for pet,name in kwargs.items():
#     #     print(f'{pet}`s name: {name}')

# printPetnames('Kalashovich', dog='Arstan', fishes=['nemo', 'dori','lari'], turtle='Leonardo' )


# ⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀ ⣀⣀⣤⣤⣤⣀⡀
# ⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀
# ⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆
# ⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆
# ⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆
# ⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠸⣼⡿
# ⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉
# ⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇
# ⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇
# ⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇
# ⠀⠀ ⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠇
# ⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇
# ⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿




# def get_some_data(*args, **kwargs):
#     print(args[0])
#     print(args[1])
#     print(kwargs['lang'])
#     print('arguments', kwargs)
#     print('Именнованые Аргументы: ', kwargs)

# get_some_data(1,2,3,4,5,6, lang='python', name='Kalash')


# ===================================================================================
# Калькулятор на функциях



# def add(num1: float,num2: float) -> float:
#     '''Функция возвращает нам сложение'''
#     return num1 + num2

# def subt(num1: float,num2: float) -> float:
#     '''Функция возвращает нам разность'''
#     return num1 - num2

# def divide(num1: float,num2: float) -> float:
#     '''Функция возвращает нам деление'''
#     try:
#         return num1 / num2
#     except ZeroDivisionError:
#         print('На ноль нельзя делить!')
    
# def mult(num1: float,num2: float) -> float:
#     '''Функция возвращает нам произведение'''
#     return num1 * num2


# def main():
#     try:
#         num1 = float(input('Введите первое число > '))
#         num2 = float(input('Введите второе число > '))
#     except TypeError:
#         print('Вы ввели не правильный формат, нам нужны именно цифры!')
#     operator = input('Введите операцию (+, -, /, *):\n> ')
#     result = None

#     if operator == '+':result=add(num1, num2)
#     elif operator == '-':result=subt(num1,num2)
#     elif operator == '*':result=mult(num1,num2)
#     elif operator == '/':result=divide(num1,num2)
#     else:
#         print('Вы ввели неправильный оператор')
#     print(result)
#     q = input('Хотите продолжить? (Y/N): \n> ')
#     if q.lower() == 'y':
#         main()
#     else:
#         print('Спасибо, пока')

# main()



# ==========================================================================================
# Короткий вариант:

# def add(a, b):return a + b 
# def substract(a, b):return a - b
# def multiply(a, b):return a*b 
# def division(a, b):return a/b 

# def result(param):return param 

# def get_data(action):
#     num1 = int(input('Enter number1:'))
#     num2 = int(input('Enter number2:'))

#     dictionary = {'+': add(num1, num2), '-': substract(num1, num2), '*':multiply(num1, num2), '/':division(num1, num2)}
#     some_result = dictionary[action]
#     return result(some_result)


# action = input('Choose action:')
# print(get_data(action))



