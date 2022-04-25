# # list()(Массив, список) - изменяемый, последовательный тип данных, который из себя представляет коллекцию каких-либо объектов


# # my_list = [1, 'string', False, None, [1,2,3]]
# # print(my_list)
# # print(type(my_list))

# # 1. -> list(iterable)


# # my_list = list('Hello') #все разбивает на символы
# # print(my_list)
# # print(type(my_list))



# # 2. -> range() - возвращает последовательность элементов

# # my_list = list(range(0,100, 2))

# # print(my_list, type(my_list), sep='\n')



# # 3. -> []
# # my_list = []
# # print(type(my_list))

# # print(dir(list))








# # append(Element)
# list_ = [1,2,3]
# list_.append([4,5,6])
# print(list_)
# list_.extend([7,8,9])
# print(list_)


# # a = [1,2,3,4]
# # a.extend([1,2,3,4])
# # print(a)
# # print(type(a))

# # list_ = ['string', 2, 3]

# # list_.insert(-8, -1) #.insert(element, step)
# # print(list_)

# # len
# # list_ = [1,2,3,4,1,2,3,42,4,21,214,2]
# # print(len(list_))

# # remove(значение)
# # list_ = [1,2,3,4,5,6,5]
# # list_.remove(5) # Удаляет одно значение
# # list_.remove(5)
# # print(list_)

# # pop([index])

# # list_ = [1,2,3,4,5,6,7]
# # list_.pop() # если не задать индекс - то удалит последнее
# # list_.pop(1) # удаляет элемент под данным индексом 
# # print(list_)
# # a = list_.pop() # возвращает удаленный элемент и присваивает переменную "а"
# # print(a) # выводит то что хранится в переменной "а"


# # clear()
# # lis = [1,2,3,4,5,6]
# # lis.clear() # очищает все, аргумент не дается
# # print(lis)





# # WARNING!!

# # a = [1,2,3,4,5,6]
# # b = a
# # print(a)
# # print(b)
# # b.pop() # "b" хранит ссылку на лист, и после того как в "б" удалили последний элемент, он и в "а" удалился!
# # print(a)
# # print(id(a))
# # print(id(b))


# copy() - поверхностное копирование
# a = [1,2,3,4,5]
# b = a.copy()
# print(a)
# print(b)
# a.pop() # удаляем последний элемент в "а", но в "б" она будет, потому что перед этим мы скопировали.
# print(b)
# print(a)
# print(id(a))
# print(id(b))




# # sort([reverse=True/False, key=])
# # lis = [12,214124,312,1,231,-1]
# # lis.sort()
# # print(lis)




# # lis = [12,214124,312,1,231,-1]
# # lis.sort(reverse=True) #обратно
# # print(lis)


# # lis = ['award', 'war22', 'hello', 'beta', 'war', '@$@']
# # lis.sort(reverse=False) # элементы по ascii сортируется, обратно
# # print(lis)





# # lis = ['award', 'war22', 'hello', 'beta', 'war', '@$@']
# # lis.sort(key=len) 
# # print(lis)


# from copy import copy, deepcopy


# a = [1,2,3,4,5,6, [1,2]]
# b = copy(a) #теория токова, копи из библеотеки работает так же как и встроенном в питоне
# c = deepcopy(a)
# d = a.copy()
# print(a.index(6))



# a.clear()
# print('a: ', a)
# print('b: ', b)
# print('c: ', c)
# a[-1][0] = 'A'
# print('a after changes: ', a)
# print('b copy func: ', b)
# print('c deepcopy: ', c)
# print('d: ', d)

# print(id(a))
# print(id(b))



















