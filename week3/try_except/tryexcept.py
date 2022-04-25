# a: int = input('')
# print(a / 0)
# print(type(a))




# try:
#     a: int = int(input(''))
#     print(a / 0)
# except ZeroDivisionError:
#     print('На ноль нельзя делить!')
# except TypeError:
#     print('Типы разные')
# except Exception as name:
#     print(name)

# print('eaeea')

# ------------------------------------------------------------------------------------------------

# str_ = 'Python'
# print(str_[1])
# print(str_[80])

# str_ = 'test'
# try:
#     print(str_[55])
# except:
#     print('нету такого индекса')

# list_ = [1,2,3,4,5,6]
# try:
#     index = int(input())
#     print(list_[index])
# except IndexError:
#     print('нету такого поймала')
# except Exception as e: #  Exception  вылавливают все исключения, и сохраняет его в переменную e
#     print('Мы поймали какую-то ошибку!')

# while True:
#     try:
#         x = int(input('Chislo > '))
#         break
#     except:
#         print('что-то пошло не так!')

# try:
#     n1 = int(input())
#     n2 = int(input())
#     # res = n1 / n2
#     # print(res)
#     print(n1 / n2) # краткая форма!
# except (ValueError, ZeroDivisionError):
#     print('Вы ввели неправильные данные')
#     print('Или на ноль делить нельзя')

# dict_ = {'a': 5, 'b': 10, 'c': 15, 'd': 20} # что-то тут не работает!
# try:
#     n1 = input('Enter > ')
#     res = dict_[n1]
#     print(res)
    
# except KeyError:
#     print('Нет такого ключа!')
# else: # сработает только тогда, когда try заработает! (не выдаст исключений!)
#     res *= 2
#     print(res)

# try:
#     a = int(input('Enter > '))
#     res = 5 + a
#     print(res)

# except Exception as e:
#     print(f'Возникла ошибка {e}')

# finally: # сработает в любом случае
#     res = 4
#     print(res)















# n = int(input("Enter: ")) # -5
# if n <= 0:
#     raise ValueError("Значение не может быть равным или меньше нуля")
# print(n)


# try:
#     num = int(input("enter: ")) # fafaohof
# except TypeError:
#     num = 45
# finally:
#     print(num)
#     print("all okay!!!")




# x = 99
# if not type(x) is int:
#     raise TypeError("только цифры")




# info_user = dict()

# email = input("enter email: ")
# if not email.endswith("@gmail.com"):
#     raise ValueError("email должен окончаться на @gmail.com")
# print(email)

# password = input("enter password: ")
# password_confirm = input("enter password_confirm: ")

# if len(password) <= 8 and len(password_confirm) <= 8:
#     raise ValueError("пароль должен быть не меньше 8 символов")
# if password != password_confirm:
#     raise ValueError("пароли не совпадают ты писать чтоли не умеешь!")

# info_user["email"] = email
# info_user["password"] = password

# print(info_user)

# try:
#     <expresion>
# except <Exception>:
#     <body>
# else: # если все окей!
#     <body>
# finally: # В любом случае
#     <body>

# 2 вида ошибок; Синтаксиз и 


# print(dir(__builtins__))

# try:
#     100/0
# except ZeroDivisionError:
#     print('На ноль делить нельзя!')
# except Exception as e:
#     print(e)




# moydic ={
#     'key': 1,
#     'key2': 2,
#     'key3': 3
# }
# ls = [1,2,3,4,5,6,7]
# try:
#     key = input('Введите ключ ')
#     index = int(input('Введите индекс '))
#     print(moydic[key])
#     print(ls[index])
# except IndexError:
#     print('Этот индекс не выходит')
# except KeyError:
#     print('Не найдено')
# except:
#     print('Что-то пошло не так')

# print('Наша программа жива!')

# a = 5
# def func():
#     global a
#     if a < 10: # UnboundLocalError
#         a = 'Stroka'
#         return a
# print(func())

# a = b # NameError