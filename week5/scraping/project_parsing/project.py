
import requests
from bs4 import BeautifulSoup as bs
import csv

# base_url = 'https://www.makers.kg'

# def get_html(url):
#   req = requests.get(url)
#   return req.text

# def get_data(html):
#     soup = bs(html, 'lxml')
#     data = soup.find_all('div', class_='feature-cards-card-info-wrapper')
#     for i in data:
#         p = i.find('div', class_='feature-cards-card-info-subtitle').text
#         print(p)

# get_data(get_html(base_url))


# base_url = 'http://www.imdb.com/chart/top'
url = 'https://news.google.com'

def get_html(url):
  res = requests.get(url).text
  return res

title_list = []
def get_data(html):
  soup = bs(html, 'lxml')
  data = soup.find_all('a', class_='VDXfz')
  for i in data:
    title_news = i.find('h3', class_='ipQwMb ekueJc RD0gLb').text
    title_list.append(title_news)

print(title_list)
# def get_html(url):
#   req = requests.get(url).text
#   return req

# def get_data(html):
#   soup = bs(html, 'lxml')
#   data = soup.find_all('td', class_='titleColumn')
#   for i in data:
#     name_of_films = i.find('a').text
#     print(name_of_films)

# get_data(get_html(base_url))
# ---------------------------------------------------------------------------------------------------------------------------------------------

# url = 'https://www.kivano.kg/mobilnye-telefony'

# def get_html(url):
#   res = requests.get(url).text
#   return res

# def data(html):
#   soup = bs(html, 'lxml')
#   data = soup.find_all('div', class_='item product_listbox oh')
  

#   for i in data:
#     price = i.find('div', class_='listbox_price text-center').find('strong').text
#     charac = i.find('div', class_='product_text pull-left')
#     d = i.find('div', class_='listbox_title oh')
#     harac = [i.strip() for i in charac if i != d]
#     telefon = i.find('strong').text
#     link = i.find('img').get('src')
#     link = 'https://www.kivano.kg/' + link

#     for x in harac:

#       datas = {
#       'name_of_product': telefon,
#       'xarak': x,
#       'price': price,
#       'image_link': link
#       }

#     write_to_csv(datas)

# def write_to_csv(datas):
#   with open('project_mini.csv', 'a') as file:
#     writer = csv.writer(file)
#     writer.writerow((datas['name_of_product'], datas['xarak'], datas['price'], datas['image_link']))

# data(get_html(url)) 











# base_url = 'http://www.imdb.com/chart/top'

# def get_html(url):
#   req = requests.get(url).text
#   return req

# dict_ = dict()

# def get_data(html):
#   soup = bs(html, 'lxml')
#   data = soup.find_all('td', class_='titleColumn')
#   for i in data:
#     name_of_films = i.find('a').text
#     link = i.find('a')['href']
#     link = 'http://www.imdb.com/' + link



#     datas = {
#       name_of_films: link
#     }
#     # print(datas)
#   print([k for k in datas.keys() if input('Введите название: ') in datas])

    # for i in name_of_films:
    #   if spisok.lower() == i.lower():
    #     print(datas['name_of_films'])
    #   else:
    #     pass



# get_data(get_html(base_url))
# Dances with Wolves

# The Shawshank Redemption
# The Shawshank Redemption

# base_url = 'http://www.imdb.com/chart/top'

# def get_html(url):
#   req = requests.get(url).text
#   return req

# dict_ = dict()

# def get_data(html):
#   soup = bs(html, 'lxml')
#   data = soup.find_all('td', class_='titleColumn')
#   for i in data:
#     name_of_films = i.find('a').text
#     link = i.find('a')['href']
#     link = 'http://www.imdb.com/' + link



#     datas = {
#       name_of_films: link
#     }   
    
   
    

#     spisok1 = []     
#     for k,v in datas.items():
#       spisok1.append(k.lower())
#       spisok1.append(v)
    
#     def get_link(spisok = spisok1, polz= pol.lower()):
#        for x in spisok:
#         if polz in x:
#           print(spisok[1])
    

#     get_link()
   
        
# pol = input('Введите название фильма:')  



# get_data(get_html(base_url))


url = 'https://news.google.com'

def get_html(url):
  res = requests.get(url).text
  return res



def get_data(html):
  soup = bs(html, 'lxml')
  data = soup.find_all('h4', class_='ipQwMb ekueJc RD0gLb')
  title_list = []
  for i in data:
    title_news = i.find('a', class_='DY5T1d RZIKme').text
    title_list.append(title_news)

  print(title_list)
# keyword = (input('Поиск: ')).lower()

# def dva(headline = title_list, keyword):
#   for i in headline:
#     if keyword in i:
#       print(headline)
      
#   dva()
  
  

get_data(get_html(url))


