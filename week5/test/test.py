
# with open('task1.txt', 'r') as task:
#     for i in task:
#         print(i)

# with open('task1.txt', 'w') as file1:
#     file1.write('1 2 3 4 5 6 7 8 9 10')

# with open('task4.txt', 'w+') as file:
#     file.writelines('1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15')



# with open('/home/kalashovich/Desktop/ev.19/week5/test/task4.txt', 'r') as file:
#     data = file.read()


# with open('task4.txt', 'r') as file:
#     ls = []
#     max__ = []
#     min__ = []
#     for i in file:
#         r = i.replace('\n', '')
#         ls.append(r)
#         max__.append(max(ls))
#         min__.append(min(ls))
# with open('task5.txt', 'a+') as file2:
#     print(file2.write(str(set(max__))))
#     print(file2.write(str(set(min__))))
# ma = set(max__)
# mi = set(min__)
# print(str(ma))
# print(str(mi))


# with open('task4.txt', 'r+') as file:
#     ls = [int(i.replace('\n', '')) for i in list(file)]
#     with open('task5.txt', 'w') as file1:
#         file1.writelines(str(ls[0]))
#         file1.writelines('\n')
#         file1.writelines(str(ls[-1::]))


# with open('task4.txt', 'w+') as file:
#   file.writelines('1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n11\n12\n13\n14\n15')
#   with open('task4.txt', 'r') as file1:
#       print(file.read())

