# Инкапсуляция:
# 1. Связь данных с методами который этими данными управялют
# 2. Набор инструментов для управления доступом или методами которые управляют этими данными

# Инкасуляция как связь

# class Phone:
#     number = '0772270567'
    
#     def print_number(self):
#         print(f'Мой номер: {self.number}')


# my_phone = Phone()
# my_phone.print_number()

# Инкапсуляция как управление доступом
# 3 уровня доступа в питоне:
#     1. Публичный (public) - number
#     2. Защищенный (_protected, parent/child) - _number
#     3. Приватный (__private, частный только в текущем классе) - __number


# class Car:
#     def __init__(self) -> None:
#         self.marka = 'Honda' #public
#         self._model = 'FIT' #protected
#         self.__motor = 'ABC' #private


# class Audi(Car):
#     pass
# car1 = Audi()
# print(car1.marka)
# print(car1._model)
# print(car1.__motor)



# car = Car()
# print(car.marka)
# print(car._model)
# print(car.__motor)
# car.marka = 'BMW'
# print(car.marka)
# car._model = 'Accord'
# print(car._model)
# car.__motor = 'qwerty'
# print(car.__motor)




# class Phone:
#     username = 'Kalashovich'
#     _caller = 'Islos'
#     __count = 100
#     def call(self):
#         print(f'Тебе звонит {self._caller}')

#     def __turn_on(self):
#         self.__count += 1
#         print('allo')

# phone = Phone()
# print(phone.username)
# phone.call()
# # print(phone._caller)
# phone._Phone__turn_on()
# # print(phone.__count)
# print(phone._Phone__count)


# getter & setter
# Они используют для получения и установки значения, чтобы добавить логику проверки при получении данных.
# Еще чтобы избежать прямого доступа к защищенному полю класса




# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.age = 0
#     def display_info(self):
#         print(f'Имя: {self.name}\nВозраст: {self.age}')


# kalashovich = Person('Kalashovich')
# print(kalashovich.name)
# print(kalashovich.age)
# kalashovich.name = 'Acosador'
# kalashovich.age = -18
# print(kalashovich.display_info())
# print(kalashovich.name)
# print(kalashovich.age)

#---------------------------------------------
# class Person:
#     def __init__(self, name):
#         self.name = name
#         self.__age = 0
#     def display_info(self):
#         print(f'Имя: {self.name}\nВозраст: {self.__age}')
    
#     def set_age(self, age): # setter
#         if 0 < age < 140: self.__age = age
#         else: print('Недопустимый возраст!')
#     def get_age(self): return self.__age

# tom = Person('Kalash')
# tom.display_info()
# tom.set_age(-18)
# tom.set_age(25)
# # print(tom.get_age())
# tom.display_info()

# Аннотации свойств

# @property



# class Person:
#     __name = 'Kalashovich'
#     __age = 22
    
#     @property
#     def name(self):
#         print(self.__name)
    
#     @name.setter
#     def name(self, name):
#         self.__name = name
    
#     @property
#     def age(self):
#         print(self.__age)

#     @age.setter
#     def age(self, age):
#         if 0 < age < 150:
#             self.__age = age
#         else: print('Недопустимый возраст!')


# ob  = Person()
# ob.name
# ob.name = 'Masha'
# ob.name
# ob.age = 1600
# ob.age = 40
# ob.age
# ob.get_name()
# ob.set_age(50)
# ob.get_name()
# ob.__age



# SOLID-принципы Дяди Боба расшифровываются следующим образом:

# S – Принцип единственной ответственности (Single Responsibility Principle),

# O – Принцип открытости/закрытости (Open‐Closed Principle),

# L – Принцип подстановки Барбары Лисков (Liskov Substitution Principle),

# I – Принцип разделения интерфейсов (Interface Segregation Principle),

# D – Принцип инверсии зависимостей (Dependency Inversion Principle).

# Интерфейс - Абстрактный класс
# Пользователь - это дочерний класс


# Не создавайте слишком большие абстрактные классы, создавайте мелокзернистые абастракции.
# Не наследуйтесь от Абстрактные классов которые не будут использованы в дочернем классе

