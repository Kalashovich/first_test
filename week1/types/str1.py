# string - Строки
# строки это набор последовательных символов, которые мы используем для хранения и представления текстовой информации.



# type - показывает какому типу относится та или иная переменная




# name = 'John'
# '\n'
# name2 = """John
# this 
# is 
# a
# power
# """
# '\n'
# name3 = str('Kalashovich Kalash')
# print(name, name2, name3)

# print(type(name), '\n', type(5), '\n', type('кто я?'), '\n', type('кто такой Калашович? - какой он человек?'))


# a = 5
# print(id(a))
# b = 5
# print(id(b))


# a = 'hello'
# b = 'Hello'
# print('',id(a), '\n', id(b))



# Экранирование - при помощи экранирования можно вставлять символы, которые сложно вести с клавиатуры.

# '\n' -> перенос строки
# '\f' -> перевод страницы
# '\r' -> возврат указателя
# '\t' -> горизонтальная табуляция
# '\v' -> вертикальная табуляция
# '\a' -> Звонок


# name = 'Kalashovich\nAcosador'
# print(name)




# lastname = input('Введите свою фамилию: ')
# print(lastname)


# Индексация символов в строке


# name = 'kalash'
#         # k = 0 = -6 
#         # a = 1 = -5
#         # l = 2 = -4
#         # a = 3 = -3
#         # s = 4 = -2
#         # h = 5 = -1
# print(name[0])
# print(name[-5])
# print(name[2])
# print(name[-3])        
# print(name[4])
# print(name[-1])



# a = 'birthday'
# print(len(a))



# Конкатенация строк

# import unittest


# hello = 'hello'
# world = 'world'
# result = hello + ' ' + world
# print(result)

# print(result.count('l', 3, 5))
# print(result.count('L'))
#                 # symbol, start, end


# Форматирование строк
# 1. С помощью %
# 2. С использованием .format()
# 3. Интерполяция строк (f - строки)

# 4. %

# name = input('Введите свое имя: ')
# last = input('last name: ')
# print('Hello, %s' %name, '%s' %last)
# print('Hello, %s %s' %(name, last))


#.format
# name = input('enter ur name: ')
# last_name = input('enter ur surname: ')
# print('Hello, {} {}'.format(name, last_name))





# name = input('ur name > ')
# last = input('ur last > ')
# print('hello,', name, last)
# print(f'Hello, {name}, {last}')



# from posixpath import split


# replace
# split



# Срезы по индексам
# [start:end:step]



# text = 'hello world! my name is kalashovich!'
# print(text[1:5])
# print(text[:-1])
# print(text[::-1])
# print(text[3::2])



