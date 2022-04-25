# Создайте класс мобильного телефона. Определите непубличные атрибуты для imei, уровня заряда батареи, краткой информации об установленной ОС. Изначальный уровень заряда
# батареи – 100%, он не может опуститься ниже 0. Методы доступа к данным расходуют 
# 0,5 % заряда при каждом обращении.
# Определите 2 публичных метода: для прослушивания музыки, и для просмотра видео.
# При каждом прослушивании музыки расходуется 5% заряда, а при просмотре видео – 7%.
# Если заряд достигает уровня ниже 10% - не давайте пользователю просматривать видео. При
# полной разрядке все методы телефона не доступны (выбрасывайте ошибку, что телефон
# разряжен).
# Также предусмотрите возможность зарядки батареи.


# class Phone:
#     def __init__(self, imei, os):
#         self._imei = imei
#         self._os_info = os
#         self.__battery_lv = 100
    
#     def get_info(self):
#         if self.__battery_lv  <= 0:
#             raise Exception('Телефон разряжен!')

#         if self.__battery_lv - 0.5 < 0:
#             self.__battery_lv = 0
#             raise Exception('Телефон разряжен!')
        
#         self.__battery_lv -= 0.5    
#         print(f'OS: {self._os_info}\nImMEI {self._imei}')

#     @property
#     def battery_level(self):
#         if self.__battery_lv  <= 0:
#             raise Exception('Телефон разряжен!')
#         self.__battery_lv -= 0.5
#         if self.__battery_lv - 0.5 < 0:
#             self.__battery_lv = 0
#             raise Exception('Телефон разряжен!')        
#         self.__battery_lv -= 0.5
#         print(f'Уровень заряда: {self.__battery_lv}')
    
#     @battery_level.setter
#     def battery_level(self, charge_level):
#         if self.__battery_lv < charge_level and charge_level <= 100:
#             self.__battery_lv = charge_level
#             print(f'Телефон заряжен на {self.__battery_lv} процентов!')
#         else:
#             raise Exception('Вы не можете разрадить уровнень батареи')

#     def play_music(self):
#         if self.__battery_lv <= 0:
#             raise Exception('Телефон разряжен!')

#         if self.__battery_lv - 5 < 0:
#             self.__battery_lv = 0
#             raise Exception('Телефон разряжен!')

#         self.__battery_lv -= 5
#         print('Слушаем музыку')

#     def play_video(self):
#         if self.__battery_lv <= 0:
#             raise Exception('Телефон разряжен!')
#         if self.__battery_lv <= 10:
#             print('У вас недостаточно заряда батереи для просмотра видео')
#         self.__battery_lv -= 7
#         print('Смотрим видео')


# apple = Phone('12312312312', 'iOS')
# apple.play_music()
# apple.play_video()
# apple.get_info()
# for i in range(1,10):
#     apple.play_video()

# apple.battery_level
# apple.battery_level = 90
# apple.battery_level


#-----------------------------------------------------------------------


# Class methods, instans methods, static methods

# Методы экземляра класса (Instans methods) - это те методы в ООП которые могут изменять состояние экземляра класса: def methods(self)



# Методы класса(class methods) - это те методы, которые могут изменять состояние самого класса:
# @classmethod - это декоратор, которые обозначает что метод являеся методом класса
# def methods(cls) - cls - это ссылка на сам класс это ссылка на сам

# Статические методы(static methods) - это те методы, которые не могут изменять состояние экземпляра класса так и самого класса:
# @staticmethod - это декоратор который обозначает статический метод 
# def method():



# class Person:
#     surname = 'Kalashovich'
#     def __init__(self, name, age) -> None:
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_bithday_date(cls, name, year):
#         print(cls, '!!!!!')
#         from datetime import date
#         cls.surname = 'lanister'
#         age = date.today().year - year
#         return cls(name, age)

#     @staticmethod
#     def isAdult(age):
#         if age >= 18:
#             print('ИСлос')
#         else:
#             print('Леопард')
# acosador = Person('Kalashovich', 25)
# print(acosador.surname)
# print(acosador.surname)
# Person.isAdult(acosador.age)
# acosador.isAdult(17)

# islos = Person.from_bithday_date('Islos', 1988)
# print(islos.name)
# print(islos.surname)
# print(islos.age)
# Person.isAdult(islos.age)

# islosovich = Person('\nIslosovich', 20)
# print(islosovich.name)
# print(islosovich.surname)
# print(islosovich.age)



class Date():
    def __init__(self, day, month, year) -> None:
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def date_from_string(cls, str_):
        day, month, year = map(int, str_.split('.'))
        return cls(day, month, year)


    def string_to_db(self):
        return f'{self.year}-{self.month}-{self.day}'

date = Date(15,4,2022)
print(date.string_to_db())
string_date = '15.4.2022'
# day, month, year = map(int, string_date.split('.'))
# date1 = Date(day, month, year)
# print(date1.string_to_db())
date2 = Date.date_from_string('09.02.2021')
print(date2.string_to_db())






















































# BOGDAN:


# # Декоратор трехуровневый, что позволяет нам самим настроить, 
# # сколько процентов будет потреблять действие
# def decrease_battery(persent=0.5):
#     def decorator(func):
#         # Декоратор принимает self, и все остальное, чтобы 
#         # метод нормально работал при наличии параметров
#         def wrapper(self, *args, **kwargs):
#             # Если батарея разряжена, вызываем ошибку
#             if self.__battery <= 0:
#                 raise Exception('Battery is dead')
#             # Изменяем батарею, если заряд опускается ниже нуля, 
#             # вместо отрицательного значения ставим 0
#             # P.S. здесь используется "моржовый оператор", рекомендую ознакомиться с ним
#             self.__battery = new_charge if (new_charge := self.__battery - persent) > 0 else 0
#             # Возвращаем результат функции
#             return func(self, *args, **kwargs)
#         return wrapper
#     return decorator

# @property
# @decrease_battery() # Не забывайте ставить скобки
# def battery(self):
#     return self.__battery

# @decrease_battery(persent=7) # Здесь мы отнимаем 7% вместо стандартных 0.5
# def video(self):
#     pass


#----------------------------------------------END--------------------