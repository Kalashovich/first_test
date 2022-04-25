# # def say_hello():
# #     print('hello world')
# #     return 'hello world'

# # # print(say_hello())


# # func = say_hello
# # print(type(func))
# # print(func())


# # DRAY - dont repeat yourself


# # SOLID 


# # 1. S - single responsibility (Принцип единой обязанности)
# list_of_names = ['kalash', 'marina', 'islos', 'okroshka']

# def append_to_list(name):
#     list_of_names.append(name)
#     # print(list_of_names) # Вторая объязанность

# def read_list():
#     print(list_of_names)

# def delete_name(name):
#     if name not in list_of_names:
#         print('Ошибка! Такого имени нет в списке')
#         return None
#     list_of_names.remove(name)

# append_to_list('kalashovich')
# read_list()
# delete_name('kalashovich')
# delete_name('mak')
# read_list()

# Функция высшего порядка - это функция которая в качестве аргумента принимает другую функцию. 

# Декоратор - это функция , которая позволяет без изменения кода обернуть другую функцию для расширения функционала обернотой функции.

# def decorator(func):
#     print(func)
#     print('Ya decorator')
#     return func()


# def hello():
#     print('Ya func, hello :)')
#     return 'hello'

# print(hello())
# res = decorator(hello)
# print(res)

# def to_uppercase(func):
#     def wrapper():
#         original_text = func()
#         mod = original_text.upper()
#         return mod
#     return wrapper

# @to_uppercase
# def get_text():
#     return 'Hello'
# print(get_text())


# def benchmark(func):
#     import time
#     start = time.time()
#     func()
#     end = time.time()
#     print(f'Время выполнения функции {func.__name__}, заняло: {end - start}')

# def loop():
#     range_number = 1000000
#     i = 0
#     while i <= range_number:
#         print(i)
#         i += 1
# benchmark(loop)

# Pythonic way -> @benchmark
# Синтаксический сахар - это красота кода

# def benchmark(func):
#     def wrapper():
#         import time
#         start = time.time()
#         func()
#         end = time.time()
#         print(f'Время выполнения функции {func.__name__} занял: {end - start}')
#     return wrapper

# @benchmark
# def loop():
#     range_number = 10000000
#     i = 0
#     while i <= range_number:
#         print(i)
#         i += 1
# loop()
#-------------------------------------------------------------

# def capital_name(func):
#     def wrapper(name):
#         mod = name.capitalize()
#         return func(mod)
#     return wrapper

# @capital_name
# def say_hello(name):
#     return f'hello {name}'
# @capital_name
# def say_whatsapp(name):
#     return f'Whats up {name}'

# print(say_hello('kalash'))
# print(say_whatsapp('kalash'))

#---------------------------------------------------------------------------------

# def strong(func):
#     def wrapper(*args, **kwargs):
#         return '<strong>' + func() + '</strong>'
#     return wrapper

# def div(func):
#     def wrapper(*args, **kwargs):
#         return '<div>' + func() + '</div>'
#     return wrapper

# @div
# @strong
# def get():
#     return 'kalash'

# print(get())
#--------------------------------------------------------


# def one(func):
#   def wrapper(*args, **kwargs):
#     print(f'Вызываю функцию {func.__name__}')
#     func()
#     res = print(f'Вызов функции {func.__name__} прошел успешно')
#     return res
#   return wrapper

# @one
# def two():
#   print('Я функция 2')

# two()


#---------------------------------------------------
# import datetime

# def decorator(func):
#   def wrapper(*args, **kwargs):
#     res = print(f'Функция запущена {datetime.datetime.now()}\n{func()}')
#     return res
#   return wrapper

# @decorator
# def func():
#   return ('Hello world!')

# func()
#--------------------------------------------------------------------------

def jirniy(func):
  def wrapper():
    
    return f'<b>{func()}</b>'
  return wrapper

def kursiv(func):
  def wrapper():
    return f'<i>{func()}</i>'
  return wrapper

def pocherkivanie(func):
  def wrapper():
      
    return f'<u>{func()}</u>'
  return wrapper


@jirniy
@kursiv
@pocherkivanie
def func():
  return ('Hello world!')

print(func())

# @kursiv
# def func():
#   return ('Hello world!')

# func()

# @jirniy
# def func():
#   return ('Hello world!')

# func()



# def b(func):
#   def wrapper():
#     return '<b\>' + func() + '<\/b\>'
#   return wrapper
# def i(func):
#   def wrapper():
#         return '<i>'+func()+'</i>'  
#   return wrapper
# def u(func):
#     def wrapper():
#         return '<u>'+func()+'</u>'
#     return wrapper
# @b
# @i
# @u
# def main():
#   return 'hello world'
  
# print(main())