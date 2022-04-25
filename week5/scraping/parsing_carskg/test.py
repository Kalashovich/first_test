# import requests
# from bs4 import BeautifulSoup as bs4

# URL = 'http://www.example.com/'
# def g_html(url):
#   resp = requests.get(url)
#   return resp.text

# def g_data(html):
#   soup = bs4(html, 'lxml')
#   h1 = soup.find('h1')
#   return h1
# print(g_data(g_html))

# import requests
# from bs4 import BeautifulSoup as bs4

# BASE_URL = 'https://www.wikipedia.org/'

# def get_html(url):
#   requests_ = requests.get(url)
#   return requests_.text

# def get_data(html):
#   soup = bs4(html, 'lxml')
#   language_ = soup.find_all('div', class_='central-featured-lang lang5')
#   # small = language_.find_all('small')
#   for i in language_:
#     lang = i.find('strong').text
#     print(lang)
#     small = i.find_all('small')
#     for x in small:
#       bdi = x.find('bdi').text
#       span = x.find('span').text
#       print(bdi, span)

# get_data(get_html(BASE_URL))


#---------------------------------------------
import requests
from bs4 import BeautifulSoup as bs
import csv


url_ = 'https://makers.kg/'

def html(url):
  res = requests.get(url).text
  return res

def data(html):
  soup = bs(html, 'lxml')
  catalog = soup.find_all('div', class_='feature-cards-card-wrapper')
  for i in catalog:
    name = i.find('h3').text
    description = i.find('div', class_='feature-cards-card-info-subtitle').text
    image_link = i.find('img', class_='feature-cards-card-image').get('src')
    image_link = 'https://makers.kg/' + image_link

    data = {
      'name': name,
      'description': description,
      'image_link' : image_link
    }
    
    write_to_csv(data)
def write_to_csv(data):
  with open('project8.csv', 'a') as file:
    #   fieldname = ['Имя', 'Описание', 'Ссылка']
    #   writer = csv.DictWriter(file,fieldname)
    #   writer.writerow({
    #       'Имя': data.get('name'),
    #       'Описание': data.get('description'),
    #       'Ссылка': data.get('image_link')
    #   })
      writer = csv.writer(file)
      writer.writerow((data['name'], data['description'], data['image_link']))

data(html(url_))