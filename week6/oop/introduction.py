# # # ООП (Объектно-ориентированное програмирование) - цель создать была связать поведение объекта с ее данными

# # # Класс - это описание того, какими свойствами и поведением должен обладать обхект (экземпляр) - А объект - это экземпляр с собствнным собсвенным состонием этих свойств.

# # # Свойствами называют обычные переменные (body = 'Человеческое тело', name = 'Калаш')

# # # Поведние - это обычные функции(def eat - методы)

# # # --------------------------------------




# # # class Dog:
# # #     # аттрибуты класса
# # #     name = 'Bobik'
# # #     age = 7

# # # bobik = Dog() # здесь определяется объект класса присвоенный в переменную bobik
# # # belka = Dog()
# # # print(bobik.name)
# # # print(bobik.age)

# # # print(belka.name)
# # # print(belka.age)


# # # class Dog():
# # #     ushi = 'Есть уши'
     
# # #     # в self хранится сам объект

# # #     def __init__(self, name, age, color) -> None:
# # #         '''
# # #         Инициализатор
# # #         Именно здесь определяются аттрибуты объекта классы
# # #         '''
# # #         self.name = name
# # #         self.age = age
# # #         self.color = color

# # # bobik = Dog('Bobik', '7', 'Brown')
# # # strelka = Dog('Strelka', '3', 'white')
# # # print(bobik.name)
# # # print(strelka.name)
# # # print(bobik.ushi)

# # # bobik.ushi = 'Нет ушей'
# # # print(bobik.ushi)
# # # print(strelka.ushi)

# # # print(f'У меня есть собака по кличке {bobik.name.translate(bobik)}. Ему {bobik.age} лет, он {bobik.color.lower()} цвета и у него {bobik.ushi.lower()}')
# # #------------------------------

# # from random import random


# # class Human:
# #     def __init__(self, name, weight, nationality) -> None:
# #         self.name = name
# #         self.age = 0
# #         self.weight = weight
# #         self.nationality = nationality

# #     def birth(self):
# #         import random

# #         print(f'happy birth {self.name}!')
# #         self.age += 1
# #         self.weight += random.randint(3,8)
# # human1 = Human('John', 3.700, 'American')
# # human2 = Human('Bakr', 3, 'Kyrgyz')

# # # print(id(human1))
# # # print(id(human2))

# # print(human1.name, human1.age, human1.weight, human1.nationality)
# # print(human2.name, human2.age, human2.weight, human2.nationality)

# # print('After one year: ')
# # (human1.birth())
# # (human2.birth())

# # print(human1.name, human1.age, human1.weight, human1.nationality)
# # print(human2.name, human2.age, human2.weight, human2.nationality)


# # print('After 3 month: ')
# # human1.birth()
# # print(human1.name, human1.age, human1.weight, human1.nationality)
# # print(human2.name, human2.age, human2.weight, human2.nationality)






# class Student:
#     univer = 'KNU'
#     def __init__(self, first_name, last_name) -> None:
#         self.name = first_name
#         self.last = last_name
#         self.books = []
#         self.languages = {}
#         self.knowledge = 0
#         self.is_ready_to_work = False
    
#     def add_points(self, point):
#         self.knowledge += point
#         if self.knowledge >= 500:
#             self.is_ready_to_work = True
#             point = (f'{self.name} is ready to work')

#     def read_book(self,book):
#         self.books.append(book)
#         self.add_points(100)

#     def do_homework(self):
#         self.add_points(50)
    
#     def do_real_project(self):
#         self.add_points(125)

#     def learn_new_language(self, language, point):
#         if not 1 < point <= 100:
#             raise Exception('Your point out of range!')
#         self.languages.update({language:point})
#         self.add_points(100)

# st1 = Student('Kalash', 'Acosador')
# st2 = Student('Mike', 'Beky')
# print(st1.name)
# print(st2.name)
# print('Before study Kalash:', st1.is_ready_to_work)
# st1.read_book('Game of Throrens')
# st1.read_book('Martin Iden')
# st1.read_book('Eugene Onegin')
# st1.read_book('Richest man on Vavilon')
# st1.do_real_project()
# st1.do_homework()
# st1.do_homework()
# st1.learn_new_language('Python', 90)
# print(st1.name, st1.books, st1.knowledge, st1.languages)
# print(st1.univer)




