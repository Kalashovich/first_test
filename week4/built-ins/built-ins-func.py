# Встроенные функции 
# print()
# list()
# len()
# max()
# sum()
# min()
# divmod()
# globals()
# locals()
# etc.
# import functools


# map()
# filter()
# zip()
# enumerate()
# functools.reduce()


# Анонимные функции - lambda(такие же функции только без названия)

# Pythonic way
# sum_ = lambda number: number**number
# res = sum_(5)
# print(res)


# sum 10-1000

# int a, b;
# int total_sum;
# a = 10;
# b = 1000;
# total_sum = 0
# while (a<=b){
#     total_sum += a
#     a ++
# }

# a, b = 10, 1000
# total_sum = 0
# while a <= b:
#     total_sum += a
#     a += 1

# res = sum(range(10,10001))
# print(res)
# -----------------------------------------------------------------------------------



# map(function, Iterable) -> она применяеи функцию каждый элемент из iterable. Возвращает mapobject.
# nums = [1,2,3,4,5]
# second = [1,2,3,4,5]

# # 3 способ
# result = list(map(
#     lambda *nums: sum(nums),
#     nums ,second
#     ))
# print(result)


# # 2 способ
# def func(*nums):
#     return sum(nums)
# res2 = list(map(func, nums, second))
# print(res2)

# # 1 способ
# def func1(num1, num2):
#     nlist = []
#     for i in range(0,5):
#         nlist.append(num1[i] + num2[i])
#     return nlist
# res1 = func1(nums, second)
# print(res1)


# names = ['Kalash', 'Khasan', 'Mas']
# def func(name):
#     return f'Hello mr/mrs {name}'
# result = list(map(func, names))
# print(result)

# dict_ = {1: 2, 3: 4, 5: 6}
# print(dict_)
# list_str = list(map(lambda value: str(value), dict_.values()))
# print(list_str)
# def update(v):
#     i = 0
#     for key in dict_:
#         dict_[key] = v[i]
#         # print(v[i], f'Индекс: {i}')
#         i += 1
# update(list_str)
# print(dict_)

#==================================================================================


# filter(function, iterable) - Фильтрует по принципу того, что функция должна возвращать True.



# numbers = list(range(1,16))
#         #[2,4,6,8,10]

# # 2 способ
# result = list(filter(lambda num: num % 2 == 0, numbers))
# print(result)

# 1 способ
# def filter_num(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
# result = list(filter(filter_num, numbers))
# print(result)



# symbols = ['a', 'b', 'c', 'd', 'e', 'f', 'j', 'i', 'o', 'z']
# vowels = ['a', 'e', 'i', 'o', 'u', 'y']
# result = list(map(lambda x: x in vowels, symbols))
# print(result)

#---------------------------------------------------------------------------------

# zip(iterable, iterable, *) -> Он сопоставляет каждый элемент из итерейблс (соединяет)


# a = [1,2,3,4,5,6,7]
# b = [66,77,88,99,11,22,34,35,36]
# result = list(zip(a,b)) # -> [(1, 66), (2, 77), (3, 88), (4, 99), (5, 11), (6, 22), (7, 34)]
# print(result)

#-----------------------------------------------------------------------------------------------

# reduce(function, iterable) -> над каждым элементом из итерейбл приминяет функцию, при этом сохраняя результат после возвращает одно значение

# from functools import reduce



# # numbers = [1,2,3,4,5,6,7,8,9,10]
# # result = reduce(lambda x,y: x*y, numbers)
# # print(result)

# list_ = ['ccc', 'aaaa', 'bb', 's']
# result = reduce(lambda x, y: x if len(x) > len(y) else y, list_)
# print(result)

#---------------------------------------------------------------------------------------


# enumerate()
# ls = [12,33,445,55,66,77,88,22]
# for i,x in enumerate(ls):
#     print(f'Id: {i+1}, element: {x}')

#===============================================================

# names = ['Raychel', 'kalash', 'Sandy', 'Fin', 'Kira', 'Sooronbay', 'Bayden']

# # Your name os {len > 4}
# result = list(map(lambda x: f'Your name is {x}',(filter(lambda x: len(x)> 4, names))))
# print(result)


# from string import ascii_letters, digits
# from random import choices
# from itertools import repeat

# print({
#     f(choices(ascii_letters,k=5),
#     choices(digits, k=8)) for f in repeat(lambda x,y: ''.join(set((x+y))),int(input('Введите количество паролей: ')))})



# import string
# import random
# def generate_rand_names():
#     random_name =''.join(
#         random.choice(string.ascii_lowercase + string.digits + string.ascii_uppercase)
#         for i in range(1, 9) )
#     return random_name

# print(generate_rand_names())

# random_name1 = str()
