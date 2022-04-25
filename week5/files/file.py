# Работа с файлами

# Указатель
# open (<Путь до вашего файла>)

# file = open('/home/kalashovich/Desktop/ev.19/week5/files/text.txt') # Абсолютный путь
# # file = open('week5/text.txt') # Относительный путь
# print(file.read())


# Режимы для работы с файлами
# 1. r/r+ (read)
# 2. w/w+ (write)
# 3. a/a+ (append)
# t = text, b = binary, x = exlus


# file = open('/home/kalashovich/Desktop/ev.19/week5/files/text.txt')
# file = open('text.txt', 'r') # file = open('week5/files/text.txt')
# data = file.read()
# data = data.split('\n')
# data = file.readlines()
# print(data)
# file.close()


# Контекстный менеджер


# with open('text.txt') as files:
#     data = files.read()
#     print(data)
# print(file.read()) - Ошибка


# with open('text.txt', 'w') as file:
#     file.write('Harasho')


# write
# writelines

# ls = ['hello', 'my name is Islos', 'Islos chortila', 'Kalashovich top']
# with open('/home/kalashovich/Desktop/ev.19/week5/files/text.txt', 'w') as file:
#     file.writelines(line + '\n' for line in ls)

# with open('/home/kalashovich/Desktop/ev.19/week5/files/text.txt', 'a') as file:
#     file.write('\n' + 'New string')


# file.tell() -> Возвращает индекс где находится указатель
# file.seek(int) -> Перемещает указатель на указанный int

# ------------------------------------------------------------------------------------
try:
    from PIL import Image
except ImportError:
    import Image

import pytesseract
import re

def get_imei_code(image):
    list_of_imei = []
    for i in image:

        string1 = pytesseract.imei_to_string(image)
        # print(string1)
        list_of_imei.append(re.findall(r'IME.\d.\s\d+', string1))
        print(list_of_imei)

    with open('imeicode.txt', 'w') as file:
        for i in list_of_imei[0]:
            file.write(i)

get_imei_code('/home/kalashovich/Desktop/ev.19/week5/files/imei.jpg')