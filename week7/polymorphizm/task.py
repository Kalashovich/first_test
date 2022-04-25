"""
3. Создайте 3 класса: Person, Employee и Student, при этом Employee и Student должны наследоваться от Person.
Определите во всех трёх классах метод get_info():
- для класса Person он должен возвращать следующее: “Привет, меня зовут Иван Петров”.
- для класса Employee он должен возвращать: “Привет, меня зовут Иван Петров, я работаю в компании “Рога и копыта” на должности “директор”.
- для класса Student должно возвращаться: “Привет, меня зовут Иван Петров, я учусь в КГТУ на 3 курсе”.

Определите функцию get_human_info(), которая будет принимать объект одного из трёх классов, вызывать метод get_info и печатать результат.
"""


# class Person:
#     def __init__(self, name,lastname):
#         self.name = name
#         self.lastname = lastname

#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.lastname}'

# class Employee(Person):
#     def __init__(self, name,lastname,company, rank):
#         super().__init__(name,lastname)
#         self.company = company
#         self.rank = rank


#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.lastname}, я работаю в компании {self.company} на должности {self.rank}'

# class Student(Person):
#     def __init__(self, name, lastname, univer, cours):
#         super().__init__(name, lastname)
#         self.univer = univer
#         self.cours = cours
#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.lastname}, я учусь в {self.univer} на {self.cours} курсе'


# person = Person('Иван', "Петров")
# emp = Employee("Иван", "Петров", "Рога и копыта", "директор")
# stud = Student("Иван", "Петров", "КГТУ", 3)


# def get_human_info(*args):
#     for i in args: 
#         print(i.get_info())

        
# get_human_info(person, emp, stud)




# class Person:
#   def init(self, name, surname):
#     self.name = name
#     self.surname = surname

#   def get_info(self):
#     return f'Привет, меня зовут {self.name} {self.surname}'

# class Employee(Person):
#   def init(self, name, surname, work, status):
#     super().init(name, surname)
#     self.work = work
#     self.status = status

#   def get_info(self):
#     return super().get_info() + f', я работаю в компании {self.work} на должности {self.status}'

# class Student(Person):
#   def init(self, name, surname, university, course):
#     super().init(name, surname)
#     self.university = university
#     self.course = course

#   def get_info(self):
#     return super().get_info() + f', я учусь в {self.university} на {self.course} курсе'

# def get_human_info(obj):
#   print(obj.get_info())

# per1 = Person('Ivan', 'Petrov')
# emp1 = Employee('Ivan', 'Petrov', 'Roga i Kopyta', 'director')
# std1 = Student('Ivan', 'Petrov', 'KSTU', 3)

# get_human_info(per1)
# get_human_info(emp1)
# get_human_info(std1)



"""
4. Объявите абстрактный класс геометрических фигур Shape и определите в нём абстрактный метод get_area() для расчёта площади фигуры, которые необходимо переопределить в дочерних классах.
Затем наследуйте от Shape три класса: Triangle, Square и Circle.

- треугольник создаётся с заданными основанием и высотой
- квадрат создаётся с заданной длиной стороны
- круг создаётся с заданным радиусом

Переопределите в каждом из классов метод get_area() таким образом, чтобы он рассчитывал площадь для конкретной фигуры.
Затем создайте от каждого из трёх классов по экземпляру, и вызовите у каждого метод get_area().

Подсказка: для создания абстрактных классов воспользуйтесь модулем [abc](https://docs.python.org/3/library/abc.html)
"""
from abc import ABC, abstractmethod
from math import pi


class Shape:
    def __init__(self,name):
        self.name = name

    @abstractmethod
    def get_area(self):
        pass

class Triangle(Shape):
    def __init__(self,name, a,b ):
        super().__init__(name)
        self.a = a
        self.b = b

    def get_area(self):
        print(self.name, (self.a * self.b)/2)

class Square(Shape):
    def __init__(self, name, len):
        super().__init__(name)
        self.len = len
    def get_area(self):
        print(self.name , self.len ** 2)

class Circle(Shape):
    def __init__(self,name, radius):
        super().__init__(name)
        self.radius = radius

    def get_area(self):
        print(self.name,pi * self.radius ** 2) 

tri = Triangle('триугольник',10,5)
sq = Square('квадрат', 100)
cir = Circle('круг', 10)
for i in (tri, sq, cir):
    i.get_area()
