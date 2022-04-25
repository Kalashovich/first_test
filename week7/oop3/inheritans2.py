# class Auto:
#     def play_music_at_station(self):
#         print('Music is playing')

#     def ride(self):
#         print('We are riding on the ground')

# class Airplane:
#     def fly(self):
#         print('We are flying')

# class FutureAuto(Auto, Airplane):
#     pass
# obj1 = FutureAuto()
# obj1.fly()


# Множественное наследование - это когда дочерний класс наследуется от куда или более классов.

# MRO (Method Resolution Order) - поиск родительских классов. Был создан для решения проблемы ромбов
#============================================
# class Zero:
#     def say(self):
#         print('class Zero')

# class First:
#     # def say(self):
#     #     print('class First')
#     pass

# class Second(First, Zero):
#     # def say(self):
#     #     print('class Second')
#     pass
# class Third(Zero):
#     def say(self):
#         print('class Third')

# class Four(Second, Third):
#     def say(self):
#         super().say()
#         print('class Fourth')

# ob = Four()
# ob.say()
# print(Four.__mro__)



# class Y:
#     pass

# class X:
#     pass

# class A(X, Y):
#     pass

# class B(Y,X):
#     pass

# class G(A, B): # class G(A, B):
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases X, Y
    # pass

# class MyMRO(type):
#     def mro(cls):
#         return (cls, A,B,X,Y, object)

# class G(A,B, metaclass=MyMRO):
#     def say(self):
#         print("Hello")


# ob = G()
# ob.say()

#========================================================
# # Mixins(Миксины)

# class MusicPlayerMixin:
#     def play_music_on_station(self):
#         print('Music is playing')

# class Machines:
#     def start_engine(self):
#         print('Started engine')

# class Auto(Machines, MusicPlayerMixin):
#     # def play_song_on_station(self):
#     #     print('Music is playing')
#     pass 

# class Plane(Machines):
#     pass 

# class Boat(Machines):
#     pass 

# class SmartClock(Machines, MusicPlayerMixin):
#     # def play_song_on_station(self):
#     #     print('Music is playing')
#     pass

# obj = Boat()
# obj.play_music_on_station()

#=====================================================

# SOLID-принципы Дяди Боба расшифровываются следующим образом:

# S – Принцип единственной ответственности (Single Responsibility Principle),

# O – Принцип открытости/закрытости (Open‐Closed Principle),

# L – Принцип подстановки Барбары Лисков (Liskov Substitution Principle),

# I – Принцип разделения интерфейсов (Interface Segregation Principle),

# D – Принцип инверсии зависимостей (Dependency Inversion Principle).

# Классы, функции должны быть открыты для расширения, но закрыты для изменения


# class FlyMixin:
#     def fly(self):
#         print('Мы можем лететь со скоростью до 500 км в час в воздухе')
# class Car(FlyMixin):
#     def ride(self):
#         print('Мы можешь разогнаться до 250 км в час')
# class SportCar(Car):
#     def ride(self):
#         print('Мы можем разогнаться до 500 км в чем')
# Car.ride()
# Car.fly()
