# Множества в python - 'контейнер', который содержит в себе уникальные элементы в случайном порядке. 
# Литералы явяются {}, но важную роль играют синтаксизы.
# {} - используются в словарях и в множествах

#{}
# a = {1: 'a', 2: 'b'} -> Словари
# a = {1,2,3,4,5,6} -> Множества

# Создавать множество так:
# a = set() 
# print(type(a)) # Множества
# b = {} # так создаются Словарь
# print(type(b))


 
# a =  set('hello') # уникальные элементы 
# print(a) # покажет только не повторяющиеся элементы в случайном порядке


# ls = [1,23,2,3,4,5,6,7,8,9,8,7,6,5,4,3,2]
# a = set(ls)
# ls = list(a)
# print(a)
# print(ls)

# FIFO
# a = {1, True,0, False, 1,2,3,4,5,6,7,8,2,3,4,4,5,6}
# print(a)

#SATTELITE-U945

# print(dir(set))


# a = {1,2,3,4,5,6,7}
# a.pop() # в множествах удаляет первый элемент (FIFO), а в списке (LIFO) удаляет последний элемент
# print(a)




# months = set(['Jan', 'Feb', 'March', 'Apr', 'May'])
# for i in months:
#     print(i)

# set_ = {1,2,3,4,5}
# set_.add('hello world')
# print(set_)



# remove/discard

# remove -> удаляет элемент, если элемента не будет в списке - то он выведет ошибку
# discard -> удаляет элемент, также как и remove, но если элемента не будет в списке - то он просто "промолчит"
# remove - > Error
# discard - > None # str.discard()



# set_ = {1,2,3,4,5,6,7,8}
# print('Before: ', set_)
# set_.discard(3)
# set_.discard(5)
# set_.discard(7)
# set_.discard(11)
# print('After: ', set_)

# set_ = {1,2,3,4,5,6,7,8}
# print('Before: ', set_)
# set_.remove(3)
# set_.remove(5)
# set_.remove(7)
# set_.remove(11)
# print('After: ', set_)


# set1 = {1,2,3,4,5,6,7}
# set2 = {11,22,33,44,55,66,77,88,99, 5,6,7,8}
# z = set1.intersection(set2)
# print(z)

# print(set1 & set2)



# set1 = {1,2,3,4,5,6,7}
# set2 = {11,22,33,44,55,66,77,88,99, 5,6,7,8}
# z = set1.difference(set2) # Разность множества (выведится те множества которые  не похожи на то или иное множество)
# print(z)
# print(set2 - set1) # то же самое что и Дифференс / - это ОПЕРАНД

# set1 = {1,2,3,4,5,6,7}
# set2 = {5,6,7,8}
# if set2.issubset(set1):
#     print('Подмножество!')

# set1 = {1,2,3,4,5,6,7,8,9}
# set2 = {1,2,3,4,5,6,7,8,9,11,12,213}
# if set1 <= set2:
#   print('Подмножество!')
# else:
#   print('Не является')

# if set2 <= set1:
#     print('Подмножество!')


# Метод Superset
# set1 = {1,2,3,4,5,6,7}
# set2 = {5,6,7}
# if set1.issuperset(set2):
#     print('Надмножество!')

# if set1 >= set2:
#     print('Надмножество!')



# set1 = {1,2,3,4,5,6,7,8,9,10}
# set2 = {11,22,33,5,6,7,12,13}
# z = set1.symmetric_difference(set2)
# print(z)
# print(set1 ^ set2)
# b = set1.difference(set2)
# print(b)


# set1 = {1,2,3,4}
# set2 = {3,4,5,7}

# print(set1.union(set2))
# print(set1 | set2)


# set1 = {1,2,3}
# set2 = {3,4,5}
# z = set1 | set2
# print(set1.union(set2))
# print(set1 | set2)


# print('before: ', set1)
# print(set1.update(set2))
# print('after: ', set1)

# set1 |= set2
# set1 -= set2

# a = set('qwerty')
# b = frozenset('qwerty')
# print(a == b)
# print(type(a))
# print(type(b))
# print(id(a))
# print(id(b))
# print(a)
# print(b)

# a.add(1)
# b.add(1)
# print(a)








# ls = []
# set1 = set()
# set2 = set()
# set3 = set()
# ls.append(set1)
# ls.append(set2)
# ls.append(set3)

# inp = input('Введите элементы через пробел: ').split(' ')
# ch = input('Выберите в какое множество добавить ваши элементы: (1 - set1, 2 - set2, 3- set3) ')
# if ch == '1':

#   set2.add('default value')
#   set3.add('default value')
#   for i in inp:
#     set1.add(i)
    
# elif ch == '2':
#   set1.add('default value')
#   set3.add('default value')
#   for i in inp:
#     set2.add(i)
    
# elif ch == '3':
#   set1.add('default value')
#   set2.add('default value')
#   for i in inp:
#     set3.add(i)

# print(ls)



set1 = {2,3,4}
set2 = {1,4,5,6,7}
if set2 >= set1:
  print('Над')