# # # dict() -> это словари - упорядоченная (python 3.7) коллекция элементов. До Пайтона 3.7 был как и сет = неупорядоченная
# # # Каждый элемент в словаре хранится в виде пары ключ:значение (key: value) уникальные значит не дублированные 

# # # Ключи должны быть уникальными и быть неизменяемыми типом данных (str, int, tuple, и т.д). Тогда как значениями могут выступать любой тип данных.

# # # thisdict = {
# # #     'brand': 'Ford',
# # #     'model': 'Mustang',
# # #     'year' : 1964   
# # # }
# # # print(thisdict)
# # # print(thisdict['model'])




# user_info = {
#     'first_name': 'John',
#     'last_name': 'snow',
#     'age': 28,
#     'email':'johnsnow',
#     'role': 'moderator',
#     # 1,2,3,
#     'number': 24_4242_777
# }
# # # print(user_info)
# # # print(user_info['first_name'])
# # # print(user_info['number'])
# # # user_info['role'] = 'admin'
# # # print(user_info['role'])
# # # print(user_info.keys())
# # # for k,v in user_info.items():
# #     # print(k,v)


# # # clear() -> очищает словарь полностью

# # # copy() -> копирует

# # for k,v in user_info.items():
# #     print(f'Ключи: {k}, значение: {v}')

# # dict_.get(key, [default == None]) == dict_[key]
# # print(user_info.get('first_name', 'Такого ключа нет!!!'))

# # dict_.pop(key, [defult == None])

# # user_info.pop('first_name', 'нет ключа!')


# # print(user_info.pop('first_nam', 'нет ключа!'))

# # update([other]) - обновляет словарь, добавляя пары(ключ : значение) из other

# # a = {'hobby':'убивать белых ходоков', 'цвет волос': 'черный'}
# # user_info.update(a)
# # print(user_info)

# # print(dir(dict))

# # setdefault(key, [value == None]) -> Работает так же как и get, но если нет такого ключа он создаст новую пару. 
# dict_ = {
#     'name': 'tirion',
#     'age': 20
# }
# res = dict_.setdefault('name')
# print(res)

# # 2. Второе способ применения, добавление пары

# dict_.setdefault('last_name', 'lanister')
# print(dict_)

# dict_.fromkeys(keys, [values] = создает новый словарь)




# tuple_ = (1,2,3,4,5,6,7,8,9)
# thisdict = dict.fromkeys(tuple_) # {1: None, 2: None, 3: None, 4: None, 5: None, 6: None, 7: None, 8: None, 9: None}
# print(thisdict)


# user_0 = {
#     'username': 'efermi',
#     'first': 'enrico',
#     'last': 'fermi',
#     }

# for key, value in user_0.items():
#     print("\nKey: " + key)
#     print("Value: " + value)



# dict_ = {
#   'banan': 155,
#   'apple': 120,
#   'orange': 100,
#   'lemon': 101
# }
# nw = dict()

# for k,v in dict_.items():
#   if v % 2 == 0:
#     dict_.pop(k)
#     nw.update()



dict2 = dict(("move", "ground"),("eat", "grass"),("say", "moo"))
print(dict2)