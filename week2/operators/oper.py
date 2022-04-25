# Nontype
# Условные операторы
# Операторы сравнения
# Логические операторы

# Nontype
# a = None
# db_connection = db.connect(...)
# db_connection == None
# if db_connection == None:
#     print('Что-то пошло не так')

# Операторы сравнения
# == (равно), != (не равно)
# <, >, >=, <=


# Возвращает True/False

# a = 10
# b = 8
# print(a == b) #False
# print(a != b) #True
# print(a > b) #True
# str1 = 'Hello'
# str2 = 'World'
# print(str1 > str2) #False (Ascii числа : 72 < 87)
# print(str1 < str2) #True 
# print(ord('H')) #72 (По ascii Числа)
# ord('<word>') выводит число по таблице Ascii - числам

# a = 'hello world'
# b = 'khasan'
# len() -> возвращает длинну объекта
# print(len(a), len(b))
# print(len(a) > len(b))

#chr
# print(chr(1100)) - ь
            # chr() -> Антоним ord() - Вводим ascii код и оно выдаст буквы
# bool(x) - возвращает True  если х == True, в противном случае False




# 1 - True
# 0 - False
# 'a' - True
# '' - False




# a = 5 
# b = 'abs'
# c = ''
# d = [1,2,3]
# res = f'a is : {bool(a)}\n'   
# res1 = f'b is : {bool(b)}\n'
# res2 = f'c is : {bool(c)}\n'
# res3 = f'd is : {bool(d)}\n'
# print(res, res1, res2, res3)


# Условные операторы
# if <conditional>:
#     <body>
#     <body>
# elif <conditional>:
#     <body>
# else:
#     <body>




# str = input('Enter sm   ')

# if str == 'Hello':
#     print('Hello World')
# elif str == 'Mercedes':
#     print('Merc-Benz S classic') 
# else:
#     print('Совпадение не найдено')


# Логические операторы:
# and -> логическое и
# or  -> логическое или
# not -> логическое отрицание

# Операторы идентификации:

# in      -> Проверяет наличие элемента
# is      -> Сравнивает ячейки памяти
# ==      -> Сравнивает по значению 
# is not  -> Отрицательное сравнение ячеек памяти










# str = 'Hello world'
# choice = input('vvedite = ')
# if choice in str:
#     print(f'Символ {choice} есть в строке:"{str}"')
# else:
#     print(f'Символ {choice} нет в нашей строке "{str}"')

# for number in range(1, 100):
#     if number % 2 != 0:
#         print(f'{number} - это число нечетное')
#     else:
#         print(f'{number} - четное')


# Дано числа [1 -- 100]
# если наши числа делятся на 3 без остатка: принтят фу
# 5 без остатка принт ба
# и на 3 и на 5 принт фуба

# for i in range(1, 100):
#     if i % 3 == 0 and i % 5 == 0:
#         print(f'{i} - fuba')
#     elif i % 5 == 0:
#         print(f'{i} - ba')
#     elif i % 3 == 0:
#         print(f'{i} - fu')
    
# for i in range(1, 100):
#     if i % 3 == 0 and i % 5 == 0:
#         print(f'{i} - fuba')
#     elif i % 5 == 0 or i % 3 == 0:
#         print(f'{i} - ba или fu')

#               import math
#               a, b, x = float(input()), float(input()), float(input())
#               print(math.sqrt((x * b) / a) + math.cos((x + b) ** 3) ** 2)

    


# import math



# a = int(input("write a first num- "))
# b = int(input("write a second num- "))
# c = input("choose one of them (*, -, +, /, ^,) - ")

# if c == "+":
#   print(a, c, b, '=', a + b)
# elif c == "-":
#   print(a, c, b, '=', a - b)
# elif c == '/':
#     if c == '/':
#         print('Деление па 0!')
#     else:
#         print(a, c, b, '=', a / b)
# elif c == '*':
#   print(a, c, b, '=', a * b)
# elif c == '^':
#     print(a, c, b, '=', a ** b)
# else:
#   print('You are have a mistake, try again')


