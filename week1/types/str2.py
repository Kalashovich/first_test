# # # from dataclasses import replace


# # # print(dir(str))

# # # raplace(old, newm [count])
# # # replace - меняет в строке значение old на new value, если вы укажите count, то он заменит count раз


# # # from audioop import reverse


# # # text = 'ha ha ha ha'

# # # # reverse = [::-1]
# # # result  = text.replace('a', 'i', 2)
# # # print(result)

# # # print(type('ha'))       #sattelite

# # # strip() -> убирает пробельные символы в начале и в конце строки

# rstrip() правое             lstrip() левое

# # # t = '    hello world   '
# # # res = t.strip()
# # # print(t)
# # # print(res)
# # from operator import truediv


# # # # startswith (string, [start], [end]) - Возвращает True если строка начинается с string,
# # # # в противном случаем возварашется False
# # # text = 'hello world'
# # # print(text.startswith('H'))
# # # print(text.startswith('W'))
# # # print(text.startswith('hello'))
# # # print(text.startswith('Hello'))

# # # print(text.startswith('ld', -2))
# # # -------------------------------------------
# # a = 'a'
# # print('a' is a)     'a' == a
# # # -------------------------------------------

# # from curses.ascii import isalpha, isdigit


# # isalpha() - проверяет состоит ли наша строка из символов
# # isdigit() - проверяет состоит ли наша сторока из числа, выводит True, если числа есть, в противном случае False.
# #isalnim() - состоит ли наша строка полностью из чисел

# # index(value, [start], [end]) - выводит индекс значения value в нашей строке


# text = 'hello world i am kalashovich'

# print(text.index('l', 2))
# # rindex(value, [start], [end]) такой же как и индекс просто с обратной стороны начинает подсчет индекса

# # find(value, [start], [end]) - выводит индекс значения value в нашей строке.
# # Разница файнда с индексом в том что, если value не найдено возвращается значение -1.
# # rfind - такой же как и файнд, просто ищет с конца


# text = 'hello world i am kalashovich'

# print(text.find('qq', 4))

# split(разделитель) - дробит строку по разделителю, которая находится в строке.
# Разделяет строку и возвращает тип данных list

# разделяет.join(iterable) -> соединяет строки, которые находятся в iterable, по разделителю



# text = 'Milk, Bread, Water'
# splited = text.split(',')
# # -> ['Milk', 'Bread', 'Water']
# print(splited)
# joined = '**'.join(splited)
# print(joined)
# # print('**'.join(splited))





# text = 'hello world this is Kalashovich Kalash'
# print(text.split(' '))
# print(type(text))

# count(string) - считает количество вхождений string в нашу строку

# swapcase - Возвращает строку, в которой каждая буква будет иметь противоположный регистр
# upper, lower


# text = 'Hello world! s  VAMI Kalash'

# res = text.swapcase()
# print(res)


