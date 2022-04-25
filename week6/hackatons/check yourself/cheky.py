# import lxml
# from bs4 import BeautifulSoup as bs
# import requests
# import csv


# # url = 'https://vesti.kg/'

# def g_html(url):
#     res = requests.get(url).text
#     return res

# def g_data(html):
#     soup = bs(html, 'lxml')
#     data = soup.find_all('div', class_='itemBody')
#     for i in data:
#         title = i.find('a').text.strip()
#         datas = {
#             'title': title
#         }
#         write(datas)

# def write(datas):
#     with open('list.csv', 'a') as file:
#         writer = csv.writer(file)
#         writer.writerow(({datas['title']}))

# # 30

# i = 0
# while True:
#     url = f'https://vesti.kg/itemlist.html?start={i}'
#     html = g_html(url)
#     soup = bs(html, 'lxml')
#     data = soup.find_all('div', class_='itemBody')

#     if not data:
#         break

#     g_data(html)
#     i += 30


# g_data(g_html(url))




