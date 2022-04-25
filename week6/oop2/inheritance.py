# # # Принципы в ООП:
# # # 1. Наследование
# # # 2. Инкапсуляция
# # # 3. Полиморфизм

# # # 4. Астракция
# # # 5. Абригация
# # # 6. Композиция

# # # Наследование - позволяет принимать родительские методы, аттрибуты и поведенияю.

# # # Родительский класс
# # # Дочерние класс

# # # -------------------------------------------------------

class Employer:
    bonus = 1.5
    def __init__(self, name,lastname, salary ):
        self.name = name
        self.lastname = lastname
        self.salary = salary

    def g_fullname(self):
        return f'{self.name} {self.lastname}'
    
    def give_bonus(self):
        self.salary = self.salary * self.bonus

# emp1 = Employer('Kalash', 'Acosador', 15_000)
# print(emp1.g_fullname())
# emp1.give_bonus()
# print(emp1.salary)

class Developer(Employer):
    def __init__(self, name, lastname, salary, prog_lang):
        Employer.__init__(self, name, lastname, salary)
        self.prog_lang = prog_lang
    
class Manager(Employer):
    def __init__(self, name, lastname, salary, emps=None):
        super().__init__(name, lastname, salary)
        if emps == None:
            self.emps = []
        else:
            self.emps = emps
    def add_emps(self, emp):
        if emp not in self.emps:
            self.emps.append(emp)
        else:
            print('Рабочий уже в нем')
    def show_emps(self):
        res = []
        for i in self.emps:
            res.append(i.g_fullname())
        return res

dev1 = Developer('Jake', 'Kalashovich', 10_000, 'Python')
print(dev1.g_fullname())
dev1.give_bonus()
print(dev1.prog_lang)
print(dev1.salary)

dev2 = Developer('Ilka', 'Makarivo', 50_000, 'Javas')
dev3 = Developer('Mika', 'Kamazod', 100_000, 'Robby')
manager = Manager('Sally', 'Islosbekovich', 15, [dev1, dev3])
manager.show_emps()
manager.add_emps(dev2)
print(f'У менеджера {manager.g_fullname()}, есть {manager.show_emps()} разработчики. Его зарплата {manager.salary}')

# # ----------------------------------------



# class Post:
#     def __init__(self, user) -> None:
#         self.user = user
#         self.posts = []
#         self.id = 0
#     # CRUD 
#     def create_post(self, title, body, image):
#         self.id += 1
#         post = dict(id=self.id, title=title, body=body, image=image)
#         self.posts.append(post)
#         return {'status': 201, 'msg': 'Успешно создано'}
    
#     def retrieve_post(self, post_id):
#         for i in self.posts:
#             if i.get('id') == post_id:
#                 return i
#         return {'status': 404, 'msg': 'Not found'}

#     def list_of_post(self):
#         return self.posts  
    
#     def update_post(self, post_id, **kwargs):
#         for i in self.posts:
#             if i.get('id') == post_id:
#                 i.update(kwargs)
#                 return {'status': 200, 'msg': 'Успешно обновлен'}
#         return {'status': 404, 'msg': 'Не найдено'}
    
#     def delete_post(self,post_id):
#         for i in self.posts:
#             if i.get('id') == post_id:
#                 self.posts.pop(self.posts.index(i))
#                 return {'status': 200, 'msg': 'Удалено'}
#         return {'status': 404, 'msg': 'Не найдено'}

# acc1 = Post('IsosIslosovich')
# acc1.create_post('Good news', 'Моя сестра Бакытгуль родила девочку!!', 'https://i.pinimg.com/originals/f7/05/2e/f7052ed865359c0d3d40f9c415de5dfc.jpg')

# acc1.create_post('На прогулке', 'Сегодня отличная погода', 'https://proprikol.ru/wp-content/uploads/2021/01/kartinki-schastlivyh-lyudej-6.jpg')

# acc1.create_post('я беремена', 'я хочу поделиться с...', 'https://imya-sonnik.ru/images/son/image/sonnik-beremennost.jpg')

# # print(acc1.posts)

# # print(acc1.retrieve_post(1))
# # print(acc1.retrieve_post(5))
# print(acc1.update_post(2, title='я тебя не люблю', body='С тобой хотел', image='https://yt3.ggpht.com/ytc/AKedOLS63ksVo0Jhx3me-vCFazimIued22diOx750aU0=s900-c-k-c0x00ffffff-no-rj'))
# print(acc1.retrieve_post(2))
# print(acc1.delete_post(2))
# print(acc1.retrieve_post(2))
# print(acc1.posts)
#-------------------------------------------
from abc import ABC, abstractmethod


class ChessPiece(ABC):
    name = 'Piece'

    # def __init__(self, name) -> None:
        # self.name =  name
    
    def show_name(self):
        print(f'Hello, i am {self.name}')

    @abstractmethod
    def move(self):
        pass

class Queen(ChessPiece):
    name = 'Queen'
    
    def move(self):
        print('куда хочу')
    
class Pawn(ChessPiece):
    name = 'Pawn'
    def move(self):
        print('На одну клетку вперед')
    
q = Queen()
p = Pawn()
q.show_name()
p.show_name()
q.move()
p.move()
