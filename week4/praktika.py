"""
7. Даны списки из чисел. Проверьте,есть ли в нем отрицательные числа.
"""


# list_ = [1, 2, 3, 0, 5, -3, -7,]
# nlist = list(filter(lambda x: x<0,list_))
# # if nlist:
# #   print(f'да, есть {len(nlist)}')
# # else:
# #   print('нет отрицательных чисел!')
# print(bool(nlist))


"""
2.Даны три числа x, y, z представляющие плоскости куба, также дано число n. Напишите функцию
выдающую все возможные комбинации координат данных трех чисел, при условии что сумма x + y + z не должна равняться числу ограничению n. Для решения использовать list comprehensions. 
Например: x, y, z = 1, 1, 2 
                n = 4 
правильный вывод: [[2, 1, 2], [1, 2, 2], [2, 2, 1]]
"""

# x,y,z = 1,2,2
# n = 4

# def cube(x,y,z,n):
#     from itertools import permutations
#     ls = [x,y,z]
#     res = [i if sum(i) != n else None for i in list(permutations(ls,3))]
#     return list(set(res))
# print(cube(x,y,z,n))




# strs = ["flo","flo","flo"]
# def longestCommonPrefix(strs) -> str:
    
#     short = min(strs, key=len)
#     for i,x in enumerate(short):
#         for other_str in strs:
#             # print(x)
#             if other_str[i] != x:
#                 return short[:i]
#     return short

# print(longestCommonPrefix(strs))





# def valid_email(email):
#     domains = ['gmail.com','mail.ru','yandex.ru']
#     index = email.find('@')
#     if '@' not in email:
#         raise Exception('Invalid email')
#     elif not email[:index]:
#         raise Exception('Incorrect email!')
#     elif email[index+1:] not in domains:
#         raise Exception(f'Такого домена не существует ({domains})!')
#     print('Your email is valid and successfully saved!')
#     return True



# def register(email,password, password2):
#     db_email = None
#     db_password = None
#     if valid_email(email):
#         db_email = email
#     if password != password2:
#         raise Exception('Passwords is didnt match')
#     db_password = password
#     msg = 'You have successfully registered, Welcome!'
#     return {
#         'email': db_email,
#         'password': db_password[::-1],
#         'msg': msg
#     }


# email = input('Введите свою почту: ')
# password = input('Введите свой пароль: ')
# password2 = input('Повторите свой пароль: ')
# # valid_email(email)
# print(register(email,password, password2))
