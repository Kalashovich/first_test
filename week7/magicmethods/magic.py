# magic methods
# dunder methods - (double userscore) __init__

# res = 5 + 5 # __add__
# print(res)


# class A(int):

# ob = A()

# print(dir[ob])


# Магические методы сравнения:

# __eq__(self, other) = ==
# __ne__(self, other) = !=
# __lt__(self, other) = <
# __gt__(self, other) = 7>6
# __le__(self, other) = <=
# __ge__(self, other) = >=


# class Word(str):
#     def __new__(cls, word):
#         word = word.split(' ')
#         word = ''.join(word)
#         return super().__new__(cls, word)

#     def __init__(self, word) -> None:
#         self.word = word
    
#     def __gt__(self, other: str) -> bool:
#         print('gt сработал!')
#         return len(self) > len(other)
    
#     def __lt__(self, other: str) -> bool:
#         print('lt сработал')
#         return len(self) < len(other)
    
#     def __qe__(self, other: object) -> bool:
#         return len(self) == len(other)

# word1 = Word('Kalashovich')
# word2 = Word('Kalashovich q2')
# res = word1 > word2
# print(res)
# print(word1 < word2)
# print(word1 == word2)

# Конструктор -> __new__
# Инициализатор -> __init__
# Деструктор -> __del__


# class Converter(float):
#     def __new__(cls, number): # 
#         print(cls, '!!!')
#         return super().__new__(cls, number ** 2)
    
#     def __init__(self, number) -> None:
#         print(self, '!!!!!')
#         self.number = number
#         self.slovo = 'Kalashovich'

# ob = Converter(5.9)
# print(ob.number, '!')
# print(ob)




# class Human:
#     def __new__(cls, str_):
#         return 'строка ' + str_
        
#     def __init__(self, str_) -> None:
#         self.str_ = str_

# ob = Human('Islos')
# ob1 = Human('ISLOSS')
# print(ob)
# print(ob1)



# randint(0,100) 0-30 -> Privet 
# 31 - 80 -> Poka
# 81 - 100 -> kak

# if 0 < random < 30:
#     print('привет')

# elif 31 < random < 80:
#     print('пока')


# class Base:
#     def __init__(self, str_):
#         self.str_ = str_

#     def __repr__(self) -> str:
#         return f'Класс {self.__class__.__name__}\nОбъект: {self.str_}'
    
#     def __str__(self):
#         return f'Объект {self.str_}'
    

# word = Base('Hello world')
# print(word)
# print(repr(word))



# class Cifra(int):
#     def __new__(cls, number):
#         print('вызов')
#         instans = super().__new__(cls)
#         if not 0 < number < 100:
#             raise ValueError('Введите чилов от 0 до 100!')
#         return instans
    
#     def __init__(self, number):
#         self.number = number
    
#     def __add__(self, other):
#         print('add сработал')
#         return self.number + other.number

# value1 = Cifra(85)
# value2 = Cifra(99)
# print(value1 + value2)


# __sub__ -
# __mul__ *
# __floordiv__ //
# __div__ /
# __mod__ %





# class Word(str):
#     # def __new__(cls, other):
#     #     res = super().__new__(cls, other).strip()
#     #     print('new сработал')
#     #     return res




#     def __new__(cls, word):
#         if ''.join(word.split(' ')) != '':
#             return super().__new__(cls)
#         else:
#             raise Exception('String should not be empty or contain only spaces')



#     def __eq__(self, other):
#         print('qe')
#         return len(self) == len(other)

#     def __gt__(self, other):
#         print('gt')
#         return len(self) > len(other)

#     def __lt__(self, other):
#         print('lt')
#         return len(self) < len(other)

#     def __ge__(self, other):
#         print('ge')
#         return len(self) >= len(other)
        
#     def __le__(self, other):
#         print('le')
#         return len(self) <= len(other)

# word1 = Word('kalashovich')
# word2 = Word('kalashovich')

# print(word1 <= word2)

class Student:
    def __init__(self, bally):
        self.bally = bally
        self.avg_res = (bally['math'] + bally['history'] + bally['literatura']/3)

    def __gt__(self, other):
        print(f'gt сработал {self.avg_res}, {other.avg_res}')
        return self.avg_res > other.avg_res
    

kalashovich = Student({'math':100, 'history':90, 'literatura':10})
islos = Student({'math':90, 'history':100, 'literatura':100})
print(kalashovich > islos)