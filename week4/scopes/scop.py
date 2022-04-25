# Области видимости и пространство имен

# Built-ins(Встроенная) -print, len, max, int ...
# Global(глобальная область видимости)
# Enclosed(не локальная область видимости, nonlocal)
# local(локальная область видимости)



# a = 10 # global
# print() #built-ins
# def hello(): # global
#     # print(a)
#     a = 'Kalash' # local
#     print(a, 'local inside at func')
   
# hello()
# print(a, 'global')
# print(dir(__builtins__))

# x = 'global'
# print(x, '1')

# def enclosed():
#     x = 'enclosed'
#     print(x, '2')
#     def local():
#         x = 'local'
#         print(x, '3')
#     local()
#     print(x, '4')
# enclosed()
# print(x, '5')


# local -> enclosed -> global -> built-ins


# a = 10 # global
# def enclosed():
#     #Started enclosed scope

#     def local():
#         #Started local scope
#         #End local scope

#     #End enclosed scope
# print(a)

# global -> позволяет менять значения глобальной переменной находясь в локальной облати видимости. Нужен для незменяемых типов данных
# синтаксиз: global a

# nonlocal -> позволяет менять значения не локальной переменнной находясь в локальной 






# def my_func(a,b):
#     global c
#     a, b = b, a
#     # c = 'hello kalash' # так делать не рекомендуется. Нельзя изменять значения в переменной
#     d = 'Acosador'
#     print({
#         'a': a,
#         'b': b,
#         'c': c,
#         'd': d
#     }, 'Local scope!!')

# a = 1
# b = 10
# c = 'global c'
# d = 'Kalashovich'
# my_func(a,b)

# print({
#         'a': a,
#         'b': b,
#         'c': c,
#         'd': d
#     }, 'Global scope!!')




# def counter():
#     num = 0
#     def incr():
#         nonlocal num
#         num += 1
#         return num
#     return incr
# c = counter()
# print(c)
# print(c())
# print(c())


# print(globals())
# print(locals())



# ===========================================================================================================

# list_ = [[1,2,3], [3,3,5], [9,9,9]]
# print([sum(max(i for i in list_))])


# dict1 = {
#     'John': {'history': 99, 'fizik': 95, 'literature': 91}, 
#     'Jerry': {'history': 92, 'math': 96, 'literature': 81},
#     'Larry': {'history': 84, 'math': 85, 'literature': 87},
# }


# ndict = {inner_key: other_key for inner_key, inner_value in dict1.items() for other_key in inner_value.keys() if max(inner_value.values()) == inner_value[other_key]}
# print(ndict)

# new_dict = {key: max(value, key=value.get) for key, value in dict1.items()}
# print(new_dict)




# a = [13,15,99]
# b = [5,10,50]
# scores = []
# counter_a = 0
# counter_b = 0
# for i in a,b:
#     if a[i] < b[i]:
#         counter_b += 1
#         scores.append(counter_b)
#     else:
#         counter_a += 1
#         scores.append(counter_a)

# scores.reverse()
# print(scores)

# def comp(al,bo):
#     al = 0
#     bo = 0
#     for i in range(0,3):
#         if a[i] > b[i]:
#             al += 1
#         elif a[i] > b[i]:
#             bo += 1
#         else:
#             pass
#     return [al,bo]
# a = [13, 15, 99]
# b = [5, 10, 50]
# print(comp(a,b))

