# # while expression:
# #     <body>

# # i = 1
# # while i <= 10:
# #     print(f'Цикл выполнился {i} - раз')
# #     i += 1

# # print('Цикл закончился')


# # name1 = ''
# # name2 = ''
# # i = 0

# # while name1.lower() != 'john' and name2.lower() != 'raychel':
# #     name1 = input('Vvedite ima: \n')
# #     name2 = input('Vvedite ima2: \n')
# #     i += 1
# #     if i > 6:
# #         print('Цикл закончился')
# #         break
# # else:
# #     print('Вы ввели правильное имя пользователя')


# # admin = ['Kalash', 'ilovepython']
# # i = 3
# # password = None


# # while admin[1] != password:
# #     password = input('Введите пароль! \n> ')
# #     i =+ 1
# #     if i == 0:
# #         print('Вы заблокированы')
# #         break
# # else:
# #     print('Вы вошли в систему')




# # for <variable> in <iter object>:
#     # <body>

# # pizza = ['first_item', 'second_item', 'third_item', 'fourth_item', 'fifth_item', 'sixth_item']
# # for i in pizza:
# #     print(f'Eating {i} of pizza')





# # pizza = ['first_item', 'second_item', 'third_item', 'fourth_item', 'fifth_item', 'sixth_item']
# # spisok = []
# # for i in pizza:
# #     new_item = i.split('_')
# #     spisok.append(new_item[0].capitalize())
    
    
# # print(spisok)



# pizza = ['first_item', 'second_item', 'third_item', 'fourth_item', 'fifth_item', 'sixth_item']
# spisok = []
# # i = 0
# # while i < len(pizza):
# #     spisok.append(pizza[i].split('_')[0].capitalize())
# #     i += 1
# # print(spisok)


# # str_ = [1,2,3,4,5,6,7,8]
# # print(str_)
# # i = str_.__iter__()
# # print(i)
# # print(i.__next__())
# # print(i.__next__())
# # print(i.__next__())
# # print(i.__next__())
# # print(i.__next__())
# # print(i.__next__())
# # print(i.__next__())
# # print(i.__next__())



# nums = [1,2,3,4,5,6,7,8,9,11,12,13] # target 9
# target = 9
# for i in range(0, len(nums)):
#     num = target - nums[i]
#     if num in nums:
#         if num == nums[i]:
#             continue
#         k = nums.index(num)
#         print(f'Otvet: {i}, {k}')
#         break
       
pizza = ['first_item', 'second_item', 'third_item', 'fourth_item', 'fifth_item', 'sixth_item']
spisok = [1,2,3]
for i in pizza:
    print(i)
    if i.startswith('second'):
        continue
    else:
        spisok.append(i)

print(spisok)




