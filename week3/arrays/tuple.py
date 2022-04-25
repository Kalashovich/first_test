# tuple() -> Это кортеж, неизменяемый тип данных



# a = [1,2,3,4,5,6,7]
# b = (1,2,3,4,5,6,7)

# print('List: ', a.__sizeof__()) # __sizeof__ - показывает сколько занимает память
# print('Tuple:', b.__sizeof__()) # можно использовать вместо списков


# WARNING!!
# tuple_ = 'string',
# print(type(tuple_)) # Кортежами являются ",", а не ()

# tuple_ = tuple('Hello my voss')
# print(tuple_)






# a = 1
# b = 2
# c = 3
# res = a, b, c
# print('Res:', res)
# print(type(res))


# new1, new2, new3 = res
# print(new1, new2, new3)


# Неизменяемый 
# tuple1 = (1,2,3,4,5)
# del tuple1[0] # -> Нельзя удалить из-за того что оно не изменяемое




# tuple1 = tuple(range(1,100))
# print(tuple1)


# print(dir(tuple)) # показывает методы

# index(element, [start], [end])
# tuple_ = (1,2,3,4)
# res = tuple_.index(3)
# print(res)

# count(element)
# tuple_ = (1,2,3,2,2,33)
# print(tuple_.count(10))

# + -> соединяет наши тюплы, * -> умнажает наши значения
# a = (1,2,3)
# b = (4,5,6)
# print(a + b)
# print(a * 3)



























































