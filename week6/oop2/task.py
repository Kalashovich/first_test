# class Class1:
#   who = 'Студент'
#   def __init__(self, name, surname):
#     self.name = name
#     self.surname = surname
    
#   def get_fullname(self):
#       return f'Вас зовут {self.name}, Ваша фамилия {self.surname}'

#   def get_info(self):
#     return f'Вы - {self.who}'

  

# class Class2(Class1):
#   def __init__(self,name, surname, age, book):
#     Class1.__init__(self, name, surname)
#     self.book = book
#     self.age = age

#   def like_book(self):
#       return f'Ваша любимая книга {self.book}'
#   def get_age(self):
#       return f'Ваш возраст {self.age}'


# st1 = Class2('Kalash', 'Kalashovich', 15, 'Margarita and Siebastyan')
# print(st1.get_info(), st1.get_fullname(),st1.like_book(),st1.get_age())




# class MyString:
#   def __init__(self, word):
#     self.word = word
#     str().__init__(self)
    
#   def append(self, word):
#     return self.ls.append(self.word)

#   def pop(self, word):
#     return self.ls.pop(self.word)

# example = MyString('String')
# example.append('привет')




# class Person:
#   def __init__(self, name, age):
#     self.name = name
#     self.age = age

#   def display(self):
#     return f'Вас зовут {self.name}, ваш возраст {self.age}'

# class Student:
#   def __init__(self, name, age, faculty):
#     Person.__init__(self, name, age)
#     self.faculty = faculty

#   def display_student(self):
#     return f'Вы учитесь в {self.faculty}'

# person1 = Person('Maria', 32)
# student1 = Student('Kalash', 19, 'PI')
# print(person1.display())
# print(student1.display_student())


import datetime

class Smartphone(str):
  battery = 0
  def __init__(self, name, color, memory):
    self.name = name 
    self.color = color
    self.memory = memory

  def charge(self, *args):
    return self.battery + args

class Iphone(Smartphone):
  def __init__(self, name, color, memory, ios):
    Smartphone.__init__(self, name, color, memory)
    self.ios = ios

  def send_imessage(self):
    return f'Отпрвлено от {self.name}, с телефона {self.ios}, по цвету {self.color} '

class Samsung(Smartphone):
  def __init__(self, name, color, memory, android):
    Smartphone.__init__(self, name, color, memory)
    self.android = android

  def show_time(self):
    return datetime.datetime.now()

iphone = Iphone('xr', 'blue', '64', '11')
samsung = Samsung('a50', 'white', '64', '11')

print(iphone.send_imessage())
print(samsung.show_time())