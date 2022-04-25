# # # range
# # # list comprehension
# # # dict comprehension

# # # range -> start:end:[step]

# # # ls = list(range(1,100,2))
# # # print(ls)

# # # for i in range(1,100,25):
# #     # print(i)

# # # for i in range(100,-1,-2):
# #     # print(i)

# # # hello = 'Hello world!'
# # # for i in range(0, len(hello)): # всегда тип данных int
# #     # print(hello[i])

# # #==================================================================================
# # # list comprehension



# # # nwlist = [expression for i in iterable <if condition == True>]


# # # ls = []
# # # for i in range(0,100,2):
# # #     print(i)
# # #     ls.append(i)


# # # ls = [i for i in range(0,100,2)]
# # # print(ls)

# # # print([i for i in range(0,100,2)])


# # # ls = [i * i for i in range(1,10)]
# # # print(ls)

# # # print([i * i for i in range(1,11)])


# fruits = ['apple', 'banana', 'cherry', 'kiwi', 'mango']

# # # ls = [i.upper() for i in fruits]
# # # print(ls)
# # # ls = [i.capitalize() for i in fruits]
# # # print(ls)

# # ls = [i for i in fruits if 'a' in i]
# # print(ls)



# ls = [i for i in fruits if i != 'apple']
# print(ls)
# print([i for i in fruits if i != 'apple'])

# ls = [1,2,3,4,5,6,7,8,9]
# nwls = [i for i in ls if i % 2 == 0 if i % 3 == 0]
# print(nwls)

# nlist = [[1,2,3,4], [5,6,7], [8,9]]
# ls = [num for it in nlist for num in i]
# print(ls)

# ls = []
# for i in nlist:
#     for num in i:
#         ls.append(num)
# print(ls)


# from datetime import datetime

# start = datetime.now()
# # ls = []
# # for i in range(1,100000000): # 100млн
# #     ls.append(i)

# ls = [i for i in range(1,100000000)]
# print(datetime.now() - start)

# ls = [i+10 if i==8 else i+1 for i in range(1,100) if i%2==0]
# print(ls)


# ls = [i+10 for i in range(1,100) if i%2==0]
# print(ls)


# ls = [i**2 if i%2==0 else i**3 for i in range(1, 101)]
# print(ls)
#==================================================================================
# dict comprehension
# dict_ = {
#     'key1': 'value1',
#     'key2': 'value2'
# }
# nw = {key: value*2 for key, value in dict_.items()}
# print(nw)

# print({key: None  for key, value in dict_.items()})

# dict_ = {n:n**2 for n in range(1,11)}
# print(dict_)

# print({n:n**2 for n in range(1,11)})


# dict1 = {
#     'a': 1,
#     'b': 2,
#     'c': 3,
#     'd': 4,
#     'e': 5,
#     'f': 6
# }

# print({key: 'even' if value%2==0 else 'odd' for key, value in dict1.items()})




# name = ['Jom', 'Jamie', 'Tirion','Peter','Sansa']

# dict_name = {
#     i+1:value for i,value in enumerate(name)
# }
# print(dict_name)

# print({i+1:value for i,value in enumerate(name)})

# ran = int(input())
# print({i:i**2 for i in range(1,500) if i%ran==0})


dict1 = {
  'khasan': 1,
  'kalash': 2,
  'atay': 3
}
print({key:'even' if value%2==0 else 'odd' for key, value in dict1.items()})