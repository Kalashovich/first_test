import requests
from bs4 import BeautifulSoup as bs
import csv
from multiprocessing import Pool

# url = f'https://www.mashina.kg/search/all/?page={i}'

def get_html(url):
    res = requests.get(url).text
    return res

def get_data(html):
    soup = bs(html, 'lxml')
    data = soup.find_all('div', class_='list-item list-label')
    

    for i in data:
            name_of_car = i.find('h2', class_='name').text.strip()
        
            price_of_car = i.find('strong').text.strip()
            try:
                image_of_car = i.find('img', class_='lazy-image').get('data-src')
            except:
                image_of_car = 'Нет картины'
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

links = []
def get_link():
    i = i

    while True:
        url = f'https://www.mashina.kg/search/all/?page={i}'
        html = get_html(url)

        soup = bs(html, 'lxml')
        data = soup.find_all('div', class_='list-item list-label')

        if not data:
            break

        get_data(html)
        i += 1
        links.append(url)
    


# get_data(get_html(url))


with Pool(1) as proc:
    get_link()
    proc.map(get_data, links)

