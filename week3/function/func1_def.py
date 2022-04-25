# # def <name_of_fucntion>(a,b # Параметры):
# #     ///
# #     <body> c / b == j
# #     ///
# #     return 'some text'

# # <name_of_function>(5,6 # Аргументы)
# # Аргументы функции это - переменная либо данные которые мы передаемдля параметров функции при вызове функции

# # Параметры функции это - это значения которые принимает функции, в теле функции мы работаем с этими данными или переменными


# # return нужно для того чтобы функция что-то возвращала,для того чтобы мы могли работать с результатом функции, return является не объязательным (возвращает None - по дефолту)




# # def isEven(num):
# #     if num % 2 == 0:
# #         return True
# #     else:
# #         return False



# # a = int(input())
# # b = int(input())

# # print(isEven(int(input())))
# # print(isEven(11))
# # print(isEven(8))
# # a = 10
# # print(isEven(a))
# # print(isEven(b))



# # def isEven(num: int) -> bool:
# #     '''
# #     Наша функция проверяет являеися ли число типа int, четным.
# #     '''
# #     if num % 2 == 0:
# #         return True
# #     else:
# #         return False

# # isEven()


def get_polindrom(words: list) -> list:
    '''Функция возвращает список из слов полиндромов.'''
    result = []
    for word in words:
        if word.lower() == word[::-1].lower():
            result.append(word)
            print('da')
        else:
            continue # пропускает операцию, ПРОПУСК
    return result

some_words = ['John', 'ono', 'Kazak','tenet']
print(get_polindrom(some_words))


# # ls = [] 
# # sword = str(input('Введите слово -> '))
# # ls.append(sword)
# # print(get_polindrom(ls))

# #==================================================================================

# # def func():
#     # print('Hello')
#     # return True
#     # print('world') # После return наша функция завершается и ниже он не будет читать!


# # func()
# # print(func)


# #==================================================================================
# # def welcome(name='user'): # по дефолту объявили струк "Юзер"
# #     print(f'Welcome, {name}!')


# # na = input('Vvedite imya > ')
# # welcome(na)
# # welcome('Kalash')




# # def get_pers(money: float, period: int) -> float:
# #     '''Retern finally amount of money.'''
# #     i = 0
# #     while i < period:
# #         money = money + (money * 0.10)
# #         i += i + 1
# #     return money

# # money = float(input('Введите сумму денег: '))
# # period = int(input('Введите срок вашего депозита: '))

# # print(get_pers(money, period))





# def get_revs(text: str) -> str:
#     '''Return reversed string'''
#     ls = []
#     spl = text.split(' ')
#     for i in spl[::-1]:
#         ls.append(i)
    
#     result_str = ' '.join(ls)

#     print(result_str)

#     return result_str

# # te = str(input())
# # get_revs(te)

# get_revs('Hello everyone, my name is Kalashovich !')




# def get_polindrom(words):
#     result = []
#     for word in words:
#         if word.lower() == word[::-1].lower():
#             result.append(word)
#         else:
#             continue # пропускает операцию, ПРОПУСК
#     return result

# some_words = ["кок", "топот", "комок"]
# print(get_polindrom(some_words))