import requests
from bs4 import BeautifulSoup as bs
import csv


url = 'https://www.mashina.kg/search/all/'

def get_html(url):
    res = requests.get(url).text
    return res

def get_data(html):
    soup = bs(html, 'lxml')
    data = soup.find_all('div', class_='list-item list-label')
    image = soup.find_all('div', class_='thumb-item-carousel brazzers-daddy')


    for i in data:
        name_of_car = i.find('h2', class_='name').text.strip()
     
        price_of_car = i.find('strong').text.strip()
   
        image_of_car = i.find('img').get('title src')
        print(image_of_car)

        miles = i.find('p', class_='year-miles').text.strip()
        body_type = i.find('p', class_='body-type').text.strip()
        volume = i.find('p', class_='volume').text.strip()
        full_xarak = [miles, body_type, volume]
            
        datas = {
                    'name': name_of_car,
                    'price': price_of_car,
                    'image': image_of_car,
                    'xarak': full_xarak
                }



        write_to_scv(datas)

def write_to_scv(datas):
    with open('data.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow((datas['name'], datas['price'], datas['xarak'], datas['image']))   


get_data(get_html(url))